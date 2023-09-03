from plyer import notification


def send_notification(title, message, duration=10, app_name="Email Summariser", app_icon='../../assets/app-2.ico'):
    """
    Send a desktop notification.

    Args:
        title (str): The title of the notification.
        message (str): The body or main content of the notification.
        duration (int, optional): How long the notification should be visible. Defaults to 10 seconds.
        app_name (str, optional): Name of the app sending the notification. Defaults to "Email Summarizer".
        app_icon (str, optional): Path to the icon to be displayed in the notification. Defaults to None.

    Returns:
        None
    """
    notification.notify(
        title=title,
        message=message,
        app_name=app_name,
        app_icon=app_icon,  # You can add an '.ico' icon path here
        timeout=duration
    )


if __name__ == '__main__':
    # Example usage:
    send_notification("New Email Summary", "You have 3 new emails that have been summarised!")
