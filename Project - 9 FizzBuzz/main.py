# Question: FizzBuzz
# Write a Python program that prints the numbers from 1 to 100. But for multiples of 3, print "Fizz"
# instead of the number, and for the multiples of 5, print "Buzz".
# For numbers that are multiples of both 3 and 5, print "FizzBuzz".


for i in range(1, 100):
    if (i==3):
        print('Fizz')
        continue
    elif (i%5 == 0 and i%3 == 0):
        print('FizzBuzz')
        continue
    elif (i==5):
        print("Buzz")
        continue
    elif (i%3 == 0):
        print('Fizz')
        continue
    elif (i%5 == 0):
        print('Buzz')
        continue
    print(i)
