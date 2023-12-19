# User profile two 8.13

def build_profile(first, last, **user_info):
    """Build a dictionary containing verything we know about a user."""
    user_info ['first_name'] = first
    user_info ['last_name'] = last
    return user_info

user_profile = build_profile(
    'ebrahim', 'al-basry', profession = 'cloud engineer',
    education = 'masters degree',
    ethnicity = 'arab')

print(user_profile)