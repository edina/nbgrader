import os


def get_username():
    """Get the username of the login in user.
    
    This is the '1_abc' user, rather than the 'joyvan' user
    """
    print("returning user name", os.environ.get('JUPYTERHUB_USER', None))
    return os.environ.get('JUPYTERHUB_USER', None)

def get_coursecode():
    """Get the code of the current course in user as conencted from.
    
    This has come via the LTI connection
    """
    return os.environ.get('NAAS_COURSE_ID', None)

def self_owned(path):
    """Is the path owned by the current user of this process?"""
    return True