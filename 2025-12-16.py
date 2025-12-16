def speed_check(speed_mph, speed_limit_kph):
    speed_kph = speed_mph * 1.60934

    if speed_kph <= speed_limit_kph:
        return "Not Speeding"

    elif speed_kph <= speed_limit_kph + 5:
        return "Warning"

    else:
        return "Ticket"