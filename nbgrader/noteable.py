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
    print("returning course code", os.environ.get('NAAS_COURSE_CODE', None))
    course_code = os.environ.get('NAAS_COURSE_CODE', None)
    print("######## course_id:{}".format(couse_code))
    return course_code

def self_owned(path):
    """Is the path owned by the current user of this process?"""
    return True