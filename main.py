from typing import Union

def is_caps(word: str) -> Union[str, bool]:
    # Если слово из 1 буквы
    def one_letter_check() -> bool:
        return len(word) == 1

    def first_letter_check() -> bool:
        return word[0] == word[0].lower()

    def other_letters_check() -> bool:
        return word[1:] == word[1:].upper()

    def all_word_check() -> bool:
        return word == word.upper()

    if one_letter_check():
        return "ONE"
    elif all_word_check():
        return 'ALL'
    elif all([first_letter_check(), other_letters_check()]):
        return 'PART'

    return False


def corrector(word: str, word_type: str) -> str:
    if word_type == 'ONE':
        if word == word.lower():
            return word.upper()
        else:
            return word.lower()
    elif word_type == 'ALL':
        return word.lower()
    elif word_type == 'PART':
        return word[0].upper() + word[1:].lower()
    return 'Something wrong'


def main(word):
    word_type = is_caps(word)
    if not word_type:
        print(word)
    else:
        print(corrector(word, word_type))

main(input())