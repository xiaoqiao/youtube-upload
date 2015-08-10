import sys

def get_code(authorize_url):
    
    """Show authorization URL and return the code the user wrote."""
    message = "Check this link in your browser: {0}".format(authorize_url)
    sys.stderr.write(message + "\n")
    try: input = raw_input #For Python2 compatability
    except NameError: pass
    return input("Enter verification code: ")