import string
import random

def ran_pass_gen():
    str1 = string.ascii_lowercase
    str2 = string.ascii_uppercase
    digit1 = string.digits
    punc1 = string.punctuation

    password_len = int(input('Enter Password Length $: '))

    password = []
    password.extend(list(str1))
    password.extend(list(str2))
    password.extend(list(digit1))
    password.extend(list(punc1))

    # random.shuffle(password)
    # print("".join(password[0:password_len]))

    print('Your Password is: ')
    print("".join(random.sample(password, password_len)))


if __name__ == '__main__':
  ran_pass_gen()