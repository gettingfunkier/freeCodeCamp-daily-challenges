function speedCheck(speedMph, speedLimitKph) {
    let speedKph = speedMph * 1.60934

    if (speedKph <= speedLimitKph) {
        return "Not Speeding"
    }

    else if (speedKph <= speedLimitKph + 5) {
        return "Warning"
    }

    else {
        return "Ticket"
    }
}