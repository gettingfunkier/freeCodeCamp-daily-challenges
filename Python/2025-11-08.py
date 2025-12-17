def can_post(message):
    if len(message) <= 40: return "short post"
    if len(message) <= 80: return "long post"
    else:
        return "invalid post"