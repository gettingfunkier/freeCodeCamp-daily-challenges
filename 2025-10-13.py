def to_12(time):
    hh = int(time[:2])
    mm = time[2:]

    if hh == 0:
        hh = 12
        return f"{hh}:{mm} AM"

    elif hh < 12:
        return f"{hh}:{mm} AM"

    elif hh == 12:
        return f"{hh}:{mm} PM"

    elif hh > 12:
        hh = hh - 12
        return f"{hh}:{mm} PM"

    return None




# TEST 1 - return "11:24 AM"
print(to_12("1124"))

# TEST 2 - return "9:00 AM"
print(to_12("0900"))

# TEST 3 - return "2:55 PM"
print(to_12("1455"))

# TEST 4 - return "11:46 PM"
print(to_12("2346"))

# TEST 5 - return "12:30 AM"
print(to_12("0030"))