import pickle
import os.path
import email
import logging
from google_auth_oauthlib.flow import InstalledAppFlow
from google.auth.transport.requests import Request
from googleapiclient.discovery import build
import base64
from src.email_fetcher.utils import get_time_n_hours_ago

logger = logging.getLogger(__name__)

# Constants for the path to the token and credentials
current_dir = os.path.dirname(os.path.abspath(__file__))
base_dir = os.path.dirname(os.path.dirname(current_dir))

TOKEN_PATH = os.path.join(base_dir, 'config', 'token.pickle')
CREDENTIALS_PATH = os.path.join(base_dir, 'config', 'credentials.json')


def authenticate_and_get_service():
    """
    Authenticate using OAuth2.0 and return the Gmail API service object.
    """
    creds = None
    if os.path.exists(TOKEN_PATH):
        with open(TOKEN_PATH, 'rb') as token:
            creds = pickle.load(token)

    if not creds or not creds.valid:
        if creds and creds.expired and creds.refresh_token:
            creds.refresh(Request())
        else:
            flow = InstalledAppFlow.from_client_secrets_file(CREDENTIALS_PATH,
                                                             ['https://www.googleapis.com/auth/gmail.readonly'])
            creds = flow.run_local_server(port=0)
            with open(TOKEN_PATH, 'wb') as token:
                pickle.dump(creds, token)

    service = build('gmail', 'v1', credentials=creds)
    return service


def mark_as_read(service, user_id, msg_id):
    """
    Mark a given email as read.

    Args:
        service: the Gmail API service instance.
        user_id: the user's email address or 'me' for the authenticated user.
        msg_id: the ID of the email to mark as read.

    Returns:
        None
    """
    service.users().messages().modify(userId=user_id, id=msg_id, body={'removeLabelIds': ['UNREAD']}).execute()


def get_value_for_name(data_list, query_name):
    # Use list comprehension to filter the desired item and get its value
    values = [item['value'] for item in data_list if item['name'] == query_name]

    # Return the first value if the list is not empty, else return None
    return values[0] if values else None


def get_plain_text(message):
    for part in message['parts']:
        if part['mimeType'] == 'text/plain':
            return part['body']['data']
        else:
            return get_plain_text(part)


def fetch_emails_from_last_n_hours(n=12, sender_email=None):
    """
    Fetch emails from the last n hours.
    """
    service = authenticate_and_get_service()
    # query_time = get_time_n_hours_ago(n)

    if sender_email:
        query = f"is:important is:unread AND from:{sender_email}"
    else:
        query = f'newer_than:{n}h is:important is:unread'

    results = service.users().messages().list(userId='me', q=query).execute()
    messages = results.get('messages', [])

    emails = []
    if messages:
        for message in messages:
            msg = service.users().messages().get(userId='me', id=message['id']).execute()
            if 'payload' in msg:
                plain_text = get_plain_text(msg['payload'])
                headers = msg['payload']['headers']
                from_address = get_value_for_name(headers, 'From')
                subject = get_value_for_name(headers, 'Subject')
                decoded_message = base64.urlsafe_b64decode(plain_text.encode('ASCII'))
                email_data = {'from': from_address,
                              'subject': subject,
                              'body': email.message_from_bytes(decoded_message)}
                emails.append(email_data)
                # decoded_bytes = base64.urlsafe_b64decode(msg['raw'].encode('ASCII'))
                # email_data = email.message_from_bytes(decoded_bytes)
                # emails.append(email_data)
                # mark_as_read(service, 'me', message['id']) # Optionally mark emails as read after they have been
                # processed

            else:
                logger.warning(f"'payload' data is missing for message ID: {message['id']}. Message keys: {msg.keys()}")
                continue  # skip this message and proceed to the next one

    return emails


if __name__ == '__main__':
    fetch_emails_from_last_n_hours(n=12, sender_email='info@sturmendeneeve.nl')
