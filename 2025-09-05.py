def is_valid_ipv4(ipv4):
    if not check_len(ipv4):
        return False

    if not check_type(ipv4):
        return False

    if not check_interval(ipv4):
        return False

    if not check_leading_zero(ipv4):
        return False

    return True

def check_len(ipv4):
    octets = ipv4.split('.')
    if len(octets) != 4:
        return False
    return True

def check_type(ipv4):
    octets = ipv4.split('.')
    for octet in octets:
        if not octet.isdigit():
            return False
    return True

def check_interval(ipv4):
    octets = ipv4.split('.')
    for octet in octets:
        if int(octet) < 0 or int(octet) > 255:
            return False
    return True

def check_leading_zero(ipv4):
    octets = ipv4.split('.')
    for octet in octets:
        if octet.startswith('0'):
            if int(octet) != 0:
                return False
            if len(octet) != 1:
                return False
    return True





# TEST 1 - return True
print(is_valid_ipv4("192.168.1.1"))

# TEST 2 - return True
print(is_valid_ipv4("0.0.0.0"))

# TEST 3 - return False
print(is_valid_ipv4("255.01.50.111"))

# TEST 4 - return False
print(is_valid_ipv4("255.00.50.111"))

# TEST 5 - return False
print(is_valid_ipv4("256.101.50.115"))

# TEST 6 - return False
print(is_valid_ipv4("192.168.101."))

# TEST 7 - return False
print(is_valid_ipv4("192168145213"))