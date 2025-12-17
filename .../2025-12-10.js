function parseBold(markdown) {
    let mdLength = markdown.length;
    let htmlString = markdown;
    let bAstOpen = false;
    let bUndOpen = false;

    for (let i = 0; i < mdLength; i++) {
        if (!bAstOpen) {
            htmlString = htmlString.replace("**", "<b>")
            bAstOpen = true;
        } else {
            htmlString = htmlString.replace("**", "</b>")
            bAstOpen = false;
        }
        if (!bUndOpen) {
            htmlString = htmlString.replace("__", "<b>")
            bUndOpen = true;
        } else {
            htmlString = htmlString.replace("__", "</b>")
            bUndOpen = false;
        }
    }

    let substring = markdown.includes("**")

    return htmlString;
}

result1 = parseBold("**This is bold**")
console.log(result1)