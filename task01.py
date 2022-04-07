vowels = ['a', 'i', 'o', 'e', 'u']

word = input("Please enter your word: ")


def count_vowels(word):
    counter = 0
    # it may be omitted as string is array-like of chars
    splitted_word = list(word.lower())
    for letter in splitted_word:
        if letter in vowels:
            counter += 1
    print(counter)


count_vowels(word)
