def detect_ai(text):
    dash_count = count_dashes(text)
    parenthesis_count = count_parentheses(text)
    big_words_count = count_big_words(text)

    if dash_count >= 2:
        return "AI"

    if parenthesis_count >= 2:
        return "AI"

    if big_words_count >= 3:
        return "AI"

    return "Human"

def count_dashes(s):
    count = 0

    for char in s:
        if char == '-':
            count += 1

    return count

def count_parentheses(s):
    count = 0
    open_count = 0

    for char in s:

        if char == '(':
            open_count += 1

        elif char == ')':
            if open_count > 0:
                count += 1
                open_count -= 1

    return count

def count_big_words(s):
    count = 0
    word = []

    for char in s:
        if char != ' ':
            word.append(char)
        else:
            length = len(word)
            if length >= 7:
                count += 1

            word = []

    return count





# TEST 1 - return "Human"
print(detect_ai("The quick brown fox jumped over the lazy dog."))

# TEST 2 - return "Human"
print(detect_ai("The hypersonic brown fox - jumped (over) the lazy dog."))

# TEST 3 - return "AI"
print(detect_ai("Yes - you're right! I made a mistake there - let me try again."))

# TEST 4 - return "AI"
print(detect_ai("The extraordinary students were studying vivaciously."))

# TEST 5 - return "AI"
print(detect_ai("The (excited) student was (coding) in the library."))