def check_strength(password):
    def check_length(p):

        if len(p) >= 8:
            return True
        else:
            return False

    def check_upper_lower(p):

        upper = False
        lower = False

        for char in p:
            if char.isupper():
                upper = True
            elif char.islower():
                lower = True

        return upper and lower

    def check_number(p):

        for char in p:
            if char.isdigit(): return True

        return False

    def check_special_character(p):

        must_contain = ["!", "@", "#", "$", "%", "^", "&", "*"]
        if any(symbol in p for symbol in must_contain): return True

        return False

    has_length = check_length(password)
    has_upper_lower = check_upper_lower(password)
    has_number = check_number(password)
    has_special_character = check_special_character(password)
    # rule instances

    r_count = 0

    if has_length: r_count += 1
    if has_upper_lower: r_count += 1
    if has_number: r_count += 1
    if has_special_character: r_count += 1

    if r_count < 2:
        return "weak"
    elif r_count < 4:
        return "medium"
    else:
        return "strong"