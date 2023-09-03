from datetime import datetime, timedelta


def get_time_n_hours_ago(n=12):
    """
    Return a formatted string representation of the UTC time n hours ago.
    """
    n_hours_ago = datetime.utcnow() - timedelta(hours=n)
    return n_hours_ago.strftime('%Y-%m-%dT%H:%M:%S+00:00')
