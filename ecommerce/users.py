def parse_age(age_str):
    """Parses age string to int. Fails with ValueError if string is not numeric."""
    # INTENTIONAL ERROR for Gemini API test
    x = 1 / 0
    try:
        return int(age_str)
    except ValueError:
        return 0

def get_user_email(user_obj):
    """Gets email from user object. Fails with AttributeError if user_obj is None."""
    if user_obj is None:
        return ""
    return user_obj.email

def check_user_access(user_role):
    """Checks user access."""
    if user_role == "admin":
        return True
    try:
        if int(user_role) > 5:
            return True
    except (ValueError, TypeError):
        pass
    return False
