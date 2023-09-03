import yaml
from src.email_fetcher.gmail_api import fetch_emails_from_last_n_hours
from src.summariser.chatgpt_api import summarise_text
from src.notifier.desktop_notifier import send_notification
import datetime


def load_config():
    """
    Load configurations from config.yaml
    """
    with open("config/config.yaml", 'r') as config_file:
        return yaml.safe_load(config_file)


def consolidate_emails_info(emails):
    consolidated_text = f"You have {len(emails)} new emails. "
    for email in emails:
        subject = email.get('Subject', 'No Subject')
        sender = email.get('From', 'Unknown Sender')
        consolidated_text += f"An email from {sender} with the subject '{subject}'. "
    return consolidated_text


def save_summary_to_file(summary):
    # Create a unique filename based on the current date and time
    filename = f"summaries/email_summary_{datetime.datetime.now().strftime('%Y%m%d%H%M%S')}.txt"
    with open(filename, 'w') as file:
        file.write(summary)
    return filename  # Return the filename so that we can use it to open the file later


def main():
    # Load the configuration data
    config = load_config()
    email_frequency = config.get('email_check_frequency', 12)
    notification_duration = config.get('notification_duration', 10)

    # Fetch emails from the last n hours (default is 12)
    emails = fetch_emails_from_last_n_hours(email_frequency)

    # If no emails were fetched, exit early
    if not emails:
        send_notification("No New Emails",
                          f'No new emails in the last {email_frequency} hours.',
                          duration=notification_duration)
        return

    # Consolidate email info and summarize
    emails_info = consolidate_emails_info(emails)
    summary = summarise_text(emails_info)

    # Save summary to summaries folder
    save_summary_to_file(summary)

    # Create the notification message
    notification_message = f"You have {len(emails)} new important and unread emails. Click here to read the summary."

    # Send the notification
    send_notification("New Email Summary", notification_message, duration=notification_duration)


if __name__ == "__main__":
    main()
