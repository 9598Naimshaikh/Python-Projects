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



## 6. Create a Fibonacci Series By using Recursion..
"""
def fib_recursion(num):
    if num == 0:
        return 0
    elif num == 1:
        return 1
    else:
        return fib_recursion(num-1) + fib_recursion(num-2)
    

num = int(input('Enter a num: '))
print(fib_recursion(num))

# #if you want to input to number of terms then do this..
# num = int(input('which number of term do you want to genrate fibonacci: '))
# for n in range(num):
#     print(fib_recursion(n))
"""


## 1. Genrate an infinite fibonacci series by using Generator..
"""
def fibonacci_genrator():
    a, b = 0, 1
    while True:
        yield a
        a, b = b, a+b

f1 = fibonacci_genrator()
print(next(f1))
print(next(f1))
print(next(f1))
print(next(f1))
print(next(f1))
print(next(f1))
print(next(f1))
"""