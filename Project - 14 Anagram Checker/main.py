# Question: Anagram Checker
# Write a Python program that takes two strings as input and determines whether they are anagrams of each other. An anagram is a word or phrase formed by rearranging the letters of another, using all the original letters exactly once.


def Anagrams(str1, str2):
    str1 = "".join(sorted(f.lower()))
    str2 = "".join(sorted(s.lower()))

    print(str1)
    print(str2)

    if str1 == str2:
        print("Anagrams")
    else:
        print("Not Anagrams")


if __name__ == "__main__":
    f = input("enter a first anagram string: ")
    s = input("enter a second anagram string: ")
    Anagrams(f, s)
