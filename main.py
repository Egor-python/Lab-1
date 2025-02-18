def is_correct(word: str) -> bool:
    correct_word: str = 'hello'
    correct_word_len = len(correct_word)
    i = 0
    l_count = 0
    for letter in word:
        if i == correct_word_len:
            break
        if l_count > 1 and letter == 'l':
            continue
        if letter == correct_word[i-1] and correct_word[i-1] != 'l':
            continue
        if letter == correct_word[i]:
            if letter == 'l':
                l_count += 1
            i += 1

    if i == correct_word_len:
        return True
    else:
        return False


word = input()
answer: bool = is_correct(word)
if answer:
    print("YES")
else:
    print("NO")