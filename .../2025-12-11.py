def to_roman(num):
    M_count = 0
    D_count = 0
    C_count = 0
    L_count = 0
    X_count = 0
    V_count = 0
    I_count = 0

    roman = ""

    while num >= 1000:
        M_count += 1
        num -= 1000

    while num >= 500:
        D_count += 1
        num -= 500

    while num >= 100:
        C_count += 1
        num -= 100

    while num >= 50:
        L_count += 1
        num -= 50

    while num >= 10:
        X_count += 1
        num -= 10

    while num >= 5:
        V_count += 1
        num -= 5

    while num >= 1:
        I_count += 1
        num -= 1

    for M_count in range(M_count):
        roman += "M"

    for D_count in range(D_count):
        roman += "D"

    for C_count in range(C_count):
        roman += "C"

    for L_count in range(L_count):
        roman += "L"

    for X_count in range(X_count):
        roman += "X"

    for V_count in range(V_count):
        roman += "V"

    for I_count in range(I_count):
        roman += "I"

    return roman

print(to_roman(1001))