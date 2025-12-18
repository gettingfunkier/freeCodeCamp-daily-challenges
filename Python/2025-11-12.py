def generate_signature(name, title, company):
    prefix_switch_1 = ["a", "b", "c", "d", "e", "f", "g", "h", "i"]
    prefix_switch_2 = ["j", "k", "l", "m", "n", "o", "p", "q", "r"]
    prefix_switch_3 = ["q", "r", "s", "t", "u", "v", "w", "x", "y", "z"]

    prefix_condition = name[0].lower()

    if prefix_condition in prefix_switch_1:
        return f">>{name}, {title} at {company}"
    elif prefix_condition in prefix_switch_2:
        return f"--{name}, {title} at {company}"
    elif prefix_condition in prefix_switch_3:
        return f"::{name}, {title} at {company}"