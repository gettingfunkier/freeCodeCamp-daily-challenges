function generateSignature(name, title, company) {
    const prefixCondition = name[0].toLowerCase()

    if (/[a-i]/.test(prefixCondition)) return `>>${name}, ${title} at ${company}`
    else if (/[j-r]/.test(prefixCondition)) return `--${name}, ${title} at ${company}`
    else if (/[s-z]/.test(prefixCondition)) return `::${name}, ${title} at ${company}`

}