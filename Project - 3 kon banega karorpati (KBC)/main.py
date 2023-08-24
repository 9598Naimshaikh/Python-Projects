# a program capable of displaying questions to the user like KBC.
# Use List data type to store the questions and their correct answers.
# display the final amount the person is taking home after playing the game.


name = input("Welcome to 'KBC' please enter your name $: ")

questions = [
    "\n1. Who is the richest man in the world ?",
    "\n2. Who is the founder of 'PYTHON' language ?",
    "\n3. Who is the dangerous batsman in the world ?",
    "\n4. Who is the most expensive player sold in IPL auction in 2023 ?",
    "\n5. what is the most expensive currency in the world ?"
]

answer = [
    [
  "(a). Bernard Arnault & family", "(b). Elon Musk", "(c). Jeff Bezos",
  "(d). Gautam Adani\n"
    ],
    [
        "(a). James Gosling", "(b). Brendan Eich", "(c). Guido van Rossum",
        "(d). Bjarne Stroustrup\n"
    ],
    [
        "(a). Virat Kohli", "(b). AB De Villiers", "(c). Alex Hales",
        "(d). Jos Butler\n"
    ],
    [
        "(a). Sam Curran", "(b). Cameron green", "(c). Ben Stokes",
        "(d). Nicholas Pooran\n"
    ],
    [
        "(a). Jordanian Dinar", "(b). Omani Rial", "(c). Kuwaiti Dinar",
        "(d).Bahraini Dinar\n"
    ]
    ]


if __name__ == '__main__':
    price = 0
    while True:
        print(questions[0])   # print the qustion[0]index....
        for i in answer[0]:   # print the answer[0]index all elements....
            print(i)

        user_input = input("Please enter answer-- 'a' or 'b' or 'c' or 'd' $$: ")   # choose answer....
        if (user_input.lower() == 'a'):
            price += 2000000
            print(f"Congrats {name}..! You win 🤑 {price} Rs.")
        else:
            print(f"Sorry {name!r}..! Your answer is wrong ❌.")
            print('Sorry..! better luck next time')
            break

        
        print(questions[1])  # print the qustion[1]index....
        for i in answer[1]:  # print the answer[1]index all elements....
            print(i)
    
        user_input = input("Please enter answer- 'a' or 'b' or 'c' or 'd' $$: ")
        if (user_input.lower() == 'c'):
            price += 2000000
            print(f"Congrats {name}..! You win 🤑 {price} Rs.")
        else:
            print(f"Sorry {name!r}..! Your answer is wrong ❌.")
            print('Sorry..! better luck next time')
            break

        
        print(questions[2])  # print the qustion[2]index....
        for i in answer[2]:  # print the answer[2]index all elements....
            print(i)
    
        user_input = input("Please enter answer- 'a' or 'b' or 'c' or 'd' $$: ")
        if (user_input.lower() == 'b'):
            price += 2000000
            print(f"Congrats {name}..! You win 🤑 {price} Rs.")
        else:
            print(f"Sorry {name!r}..! Your answer is wrong ❌.")
            print('Sorry..! better luck next time')
            break



        print(questions[3])   # print the qustion[3]index....
        for i in answer[3]:   # print the answer[3]index all elements....
            print(i)
    
        user_input = input("Please enter answer- 'a' or 'b' or 'c' or 'd' $$: ")
        if (user_input.lower() == 'a'):
            price += 2000000
            print(f"Congrats {name}..! You win 🤑 {price} Rs.")
        else:
            print(f"Sorry {name!r}..! Your answer is wrong ❌.")
            print('Sorry..! better luck next time')
            break


        print(questions[4])  # print the qustion[4]index....
        for i in answer[4]:  # print the answer[4]index all elements....
            print(i)
    
        user_input = input("Please enter answer- 'a' or 'b' or 'c' or 'd' $$: ")
        if (user_input.lower() == 'c'):
            price += 2000000
            print(f"Congrats {name}..! You win 🤑 {price} Rs.")
        else:
            print(f"Sorry {name!r}..! Your answer is wrong ❌.")
            print('Sorry..! better luck next time')
            break


        if (price==10000000):
            print(f"\nCongratulations {name!r}..!, You have won one crore rupees🤑🤑.")
            print("10000000 Rs.")
            break
        else:
            print(f"\nSorry {name}..! You didn't win 1 crore.")
            print('Sorry..! better luck next time')
            break
