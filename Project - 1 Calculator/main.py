# create a calculater operators,,,,, Addition +, Substraction -, Multiplication *, division /, Exponential **, module %, Floor division //,


add = lambda a, b: a + b
sub = lambda a, b: a - b
mul = lambda a, b: a * b
div = lambda a, b: a / b
exp = lambda a, b: a ** b
mod = lambda a, b: a % b
flr_div = lambda a, b: a // b

if __name__ == "__main__":
    print("Welcome to Calculator Program...!")
    print('---------------------------------')
    while True:
        print(
            "1. Add\n2. Subtract\n3. Multiply\n4. divide\n5. Exponential\n6. Module\n7. Floor Divide\n"
        )
        try:
            choice = int(input("Enter choice (1,2,3,4,5,6,7): "))

            num1 = int(input("\nEnter a first number: "))
            num2 = int(input("Enter a second number: "))

            if choice == 1:
                print(num1, "+", num2, "=", add(num1, num2))
            elif choice == 2:
                print(num1, "-", num2, "=", sub(num1, num2))
            elif choice == 3:
                print(num1, "*", num2, "=", mul(num1, num2))
            elif choice == 4:
                print(num1, "/", num2, "=", div(num1, num2))
            elif choice == 5:
                print(num1, "**", num2, "=", exp(num1, num2))
            elif choice == 6:
                print(num1, "%", num2, "=", mod(num1, num2))
            elif choice == 7:
                print(num1, "//", num2, "=", flr_div(num1, num2))

            else:
                print("Invalid Value Please try again....!")

            # exit arguments programm...
            user_arg = input("Do you want to exit it (y/n): ")
            if user_arg.lower() == "y":
                print("\nThanks for quiting the programm...!")
                break

        except ValueError as ve:
            print("Error:", ve)
        except ZeroDivisionError:
            print("Error: Cannot divide by zero!")
        except Exception as e:
            print("An error occurred:", e)
