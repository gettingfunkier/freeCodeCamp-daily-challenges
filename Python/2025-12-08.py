def convert_to_kgs(lbs):
    kgs = format(lbs * 0.453592, '.2f')

    if lbs == 1:
        return f"{lbs} pound equals {kgs} kilograms."

    elif float(kgs) == 1:
        return f"{lbs} pounds equals {kgs} kilogram."

    else:
        return f"{lbs} pounds equals {kgs} kilograms."