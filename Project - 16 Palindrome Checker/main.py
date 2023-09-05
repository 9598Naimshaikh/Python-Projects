## Question: Palindrome Checker ?

def palindrome_checker(word):
    word = word.lower()
    reverse_word = word[::-1]

    print(f'Word: {word}')
    print(f'Reverse Word: {reverse_word}')
    
    if word == reverse_word:
        print('Yes.! Palindrome.')
    else:
        print('Not.! Palindrome.')


if __name__=='__main__':
    word = input('Enter a word: ')
    palindrome_checker(word)