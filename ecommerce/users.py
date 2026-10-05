def parse_age(age_str):
    """Parses age string to int. Fails with ValueError if string is not numeric."""
    return int(age_str)

def get_user_email(user_obj):
    """Gets email from user object. Fails with AttributeError if user_obj is None."""
    return user_obj.email
