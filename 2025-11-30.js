function detectAI(text) {
    let dashCount = countDashes(text)
    let parethesesCount = countParentheses(text)
    let bigWordsCount = countBigWords(text)

    if (dashCount >= 2) {
        return "AI"
    }
    if (parethesesCount >= 2) {
        return "AI"
    }
    if (bigWordsCount >= 3) {
        return "AI"
    }

    return "Human";
}

function countDashes(text) {
    let count = 0

    for (let char of text) {
        if (char === '-') {
            count++
        }
    }

    return count;
}

function countParentheses(text) {
    let count = 0
    let open_count = 0

    for (let char of text) {
        if (char === '(') {
            open_count++
        }
        else if (char === ')') {
            if (open_count > 0) {
                count++
                open_count--
            }
        }
    }

    return count;
}

function countBigWords(text) {
    let count = 0
    let word = []

    for (let char of text) {
        if (char !== ' ') {
            word.push(char);
        }
        else {
            let length = word.length;
            if (length >= 7) {
                count++;
            }

            word = [];
        }
    }

    return count;
}




// TEST 1 - return "Human"
let result1 = detectAI("The quick brown fox jumped over the lazy dog.")
console.log(result1);

// TEST 2 - return "Human"
let result2 = detectAI("The hypersonic brown fox - jumped (over) the lazy dog.")
console.log(result2);

// TEST 3 - return "AI"
let result3 = detectAI("Yes - you're right! I made a mistake there - let me try again.")
console.log(result3);

// TEST 4 - return "AI"
let result4 = detectAI("The extraordinary students were studying vivaciously.")
console.log(result4);

// TEST 5 - return "AI"
let result5 = detectAI("The (excited) student was (coding) in the library.")
console.log(result5);