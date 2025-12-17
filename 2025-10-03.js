function checkStrength(password) {

    const hasLength = checkLength(password)
    const hasUpperLower = checkUpperLower(password)
    const hasNumber = checkNumber(password)
    const hasSpecialCharacter = checkSpecialCharacter(password)
    // rule instances

    let rCount = 0

    if (hasLength) {rCount ++}
    if (hasUpperLower) {rCount ++}
    if (hasNumber) {rCount ++}
    if (hasSpecialCharacter) {rCount ++}

    if (rCount < 2) {return "weak"}
    else if (rCount < 4) {return "medium"}
    else {return "strong"}
}

function checkLength(p) {
    if (p.length >= 8) {
        return true
    } return false
}

function checkUpperLower(p) {
    const
        upper = /[A-Z]/.test(p),
        lower = /[a-z]/.test(p);

    return upper && lower
}

function checkNumber(p) {
    return /[0-9]/.test(p)
}

function checkSpecialCharacter(p) {
    return /[!,@,#,$,%,^,&,*]/.test(p)
}