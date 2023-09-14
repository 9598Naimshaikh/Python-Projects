# Question: Anagram Checker

# Write a Python program that takes two strings as input and determines whether they are anagrams of each other.
# An anagram is a word or phrase formed by rearranging the letters of another,
# using all the original letters exactly once.


def Anagrams(word1, word2):
    word1 = "".join(sorted(word1.lower()))
    word2 = "".join(sorted(word2.lower()))

    print(word1)
    print(word2)

    if word1 == word2:
        print("Yes.! Anagrams")
    else:
        print("Not.! Anagrams")


if __name__ == "__main__":
    str1 = input("enter a first anagram string: ")
    str2 = input("enter a second anagram string: ")

    Anagrams(str1, str2)
