import os


def get_username():
    """Get the username of the login in user."""
    return os.environ.get('JPY_USER', None)


def self_owned(path):
    """Is the path owned by the current user of this process?"""
    return True

