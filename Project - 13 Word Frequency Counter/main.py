# Question: Word Frequency Counter
# Write a Python program that takes a sentence input from the user and counts the frequency of each word in the sentence.

# Your program should take a sentence input and output a dictionary where keys are words and values are the corresponding frequencies.


def word_frequency(sentence):
    words = sentence.split()
    frequency_dict = {}

    for word in words:
        word = word.lower()
        if word in frequency_dict:
            frequency_dict[word] += 1
        else:
            frequency_dict[word] = 1

    return frequency_dict


# Input from the user
user_sentence = input("Enter a sentence: ")
result = word_frequency(user_sentence)

print("Word frequencies:", result)
