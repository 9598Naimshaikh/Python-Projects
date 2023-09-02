# Question: Counting Vowels and Consonants
# Write a Python program that takes a string input from the user and counts the number of vowels and consonants in the string.
# Consider vowels to be the characters 'a', 'e', 'i', 'o', and 'u' (both lowercase and uppercase). Ignore spaces and any other characters that are not letters.

# Your program should output the count of vowels and consonants in the input string.

user_input = input("Enter anything $: ")
vowels = 0
consonants = len(user_input)

for items in user_input:
    if items.lower() == "a":
        vowels += 1
        consonants -= 1

    elif items.lower() == "e":
        vowels += 1
        consonants -= 1

    elif items.lower() == "i":
        vowels += 1
        consonants -= 1

    elif items.lower() == "o":
        vowels += 1
        consonants -= 1

    elif items.lower() == "u":
        vowels += 1
        consonants -= 1


print(f"Vowels: {vowels}, Consonants: {consonants}")
