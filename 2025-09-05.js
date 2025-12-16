function isValidIPv4(ipv4) {
    let octets = ipv4.split(".")

    if (octets.length !== 4) {
        return false
    }

    for (let octet of octets) {
        let n = Number(octet)

        if (octet === '') {
            return false
        }

        if (n < 0 || n > 255) {
            return false
        }

        if (n !== 0 && octet[0] === "0") {
            return false
        }

        if (octet[0] === "0" && octet.length !== 1) {
            return false
        }
    }

    return true
}


console.log(isValidIPv4("192.168.1.1"))
// true
console.log(isValidIPv4("0.0.0.0"))
// true
console.log(isValidIPv4("255.01.50.111"))
// false
console.log(isValidIPv4("255.00.50.111"))
// false
console.log(isValidIPv4("256.101.50.115"))
// false
console.log(isValidIPv4("192.168.101."))
// false
console.log(isValidIPv4("192168145213"))
// false
