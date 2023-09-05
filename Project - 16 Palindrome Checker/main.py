# Problem: Palindrome Checker

# Write a Python function that checks whether a given string is a palindrome.
# A palindrome is a word, phrase, number, or other sequences of characters that reads the same forward and backward (ignoring spaces, punctuation, and capitalization).

import string


def palindrome_checker(word):
    word = word.lower()  # convert to all lower case.
    remove_punc = word.translate(str.maketrans("", "", string.punctuation)).split() #remove punctuation and convert to string to remove space.

    modify_word = "".join(remove_punc) # join to as a string.
    reverse_word = modify_word[::-1]  # reverse the string.

    print(f"Modify_word: {modify_word}")
    print(f"Reverse Word: {reverse_word}")

    if modify_word == reverse_word:
        print("Yes.! Palindrome.")
    else:
        print("Not.! Palindrome.")


if __name__ == "__main__":
    word = input('Enter a word: ')
    palindrome_checker(word)
