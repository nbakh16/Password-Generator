import random
from characters import letters_list, digits_list, punctuations_list


def passwordgenerator():
    print("---Password Generator---")
    input_letters_list = int(input("how many letters_list?\n"))
    input_digits_list = int(input("how many number?\n"))
    input_punctuations = int(input("how many symbols?\n"))

    gen_password_list = []
    for i in range(1, input_letters_list+1):
        gen_password_list.append(random.choice(letters_list))
    for i in range(1, input_digits_list+1):
        gen_password_list.append(random.choice(digits_list))
    for i in range(1, input_punctuations+1):
        gen_password_list.append(random.choice(punctuations_list))

    random.shuffle(gen_password_list)

    gen_password = ""
    for i in gen_password_list:
        gen_password += i

    print("Your generated password: " + gen_password)
    print("password length is " + str(len(gen_password)) + ".")
    if len(gen_password) < 12 or input_letters_list < 1 or input_digits_list < 1 or input_punctuations < 1:
        print("WARNING!! password is not strong enough!"
              "Ideal password should be 12 characters with consist at least one letter, number & symbol.")
    else:
        print("Password is strong enough.")


while True:
    passwordgenerator()
    while True:
        answer = str(input('Generate another password? (y/n): '))
        if answer in ('y', 'n'):
            break
        print("Invalid input.")
    if answer == 'y':
        passwordgenerator()
    else:
        print("Bye. Have a good day.")
        break
