# Question: Fibonacci Series
# Write a Python program that generates and prints the Fibonacci series up to a given number of terms n. The Fibonacci series is a sequence of numbers in which each number is the sum of the two preceding ones, usually starting with 0 and 1.

# Your program should take an integer input n and output the Fibonacci series up to the nth term.


def fibonacci_series(num):
    a = 0
    b = 1
    if num == 1:
        print(a)
    else:
        print(a)
        print(b)
        for i in range(2, num):
            c = a + b
            a = b
            b = c
            print(c)


if __name__ == "__main__":
    num = int(input("Enter a num: "))
    fibonacci_series(num)
