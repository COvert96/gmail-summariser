import pickle
import os.path
import email
from google_auth_oauthlib.flow import InstalledAppFlow
from google.auth.transport.requests import Request
from googleapiclient.discovery import build
import base64
from .utils import get_time_n_hours_ago

# Constants for the path to the token and credentials
TOKEN_PATH = "config/token.pickle"
CREDENTIALS_PATH = "config/credentials.json"


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


def fetch_emails_from_last_n_hours(n=12):
    """
    Fetch emails from the last n hours.
    """
    service = authenticate_and_get_service()
    query_time = get_time_n_hours_ago(n)

    results = service.users().messages().list(userId='me', q=f'after:{query_time} is:important is:unread').execute()
    messages = results.get('messages', [])

    emails = []
    if messages:
        for message in messages:
            msg = service.users().messages().get(userId='me', id=message['id']).execute()
            decoded_bytes = base64.urlsafe_b64decode(msg['raw'].encode('ASCII'))
            mime_msg = email.message_from_bytes(decoded_bytes)
            emails.append(mime_msg)
            # mark_as_read(service, 'me', message['id']) # Optionally mark emails as read after they have been processed

    return emails

