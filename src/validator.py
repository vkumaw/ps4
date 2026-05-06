VALID_CONTENT_TYPES = ["SHORT", "LONG"]

VALID_PLATFORMS = ["Instagram", "YouTube"]

def validate_content_row(row):

    if row["content_type"] not in VALID_CONTENT_TYPES:
        return False

    if not (0 <= row["created_timestamp"] <= 23):
        return False

    return True

def safe_get(dictionary, key, default_value):

    return dictionary.get(key, default_value)
    

