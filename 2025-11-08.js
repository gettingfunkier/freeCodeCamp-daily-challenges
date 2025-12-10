function canPost(message) {
    let word = []
    for (let char in message) {
        word.push(char)
    }
    let length = word.length
    if (length <= 40) {
        return "short post"
    }
    else if (length <= 80) {
        return "long post"
    }
    else {
        return "invalid post"
    }
}





// TEST 1 - return "short post"
let post1 = canPost("Hello World")
console.log(post1)

// TEST 2 - return "long post"
let post2 = canPost("This is a longer message but still under eighty characters.")
console.log(post2)

// TEST 3 - return "invalid post"

let post3 = canPost("This message is too long to fit into either of the character limits for a social media post.")
console.log(post3)