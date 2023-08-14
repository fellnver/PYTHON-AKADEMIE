'''
projekt_2.py: druhý projekt do Engeto Online Python Akademie
author: Veronika Fellnerova
email: veronika.fellnerova@seznam.cz
discord: Verca F.#5057
'''

import random

print('''Hi there!
-----------------------------------------------
I've generated a random 4 digit number for you.
Let's play a bulls and cows game.
-----------------------------------------------
Enter a number:''')


#Generating random digit
def generate_random_number():
    first_digit = random.randint(1, 9)

    digits = list(range(10))
    digits.remove(first_digit)
    random.shuffle(digits)

    my_number = ''.join(str(digit) for digit in digits[:3])
    my_number = str(first_digit) + my_number
    return(my_number)

generated_number = generate_random_number() #Note type STRING

#print(generated_number) - used for testing


#Function for checking unique number
def has_unique_digits(number):
    digit_set = set(str(number))  # Convert the number to a string and create a set of its digits (set can only have unique numbers so if it equals, its unique)
    return len(digit_set) == len(str(number))


#Function to describe guessing skills of player
def get_guesses_rank(guesses):
    if guesses <= 10:
        return 'amazing.'
    elif 20 > guesses > 10:
        return 'average.'
    else:
        return 'not so good.'


# GAME #
bulls = 0
guesses = 0

while bulls < 4:

    user_number = input('----------------------------------------------- \n>>> ') #Note: type STRING
    guesses += 1 #Counting guesses

    if user_number == generated_number:
        bulls = 4 #For while cycle to be terminated
        if guesses == 1:
            print(f"Correct, you've guessed the right number in 1 guess!")
        else:
            print(f"Correct, you've guessed the right number in {guesses} guesses!")
        print(f"That's {get_guesses_rank(guesses)}")

    else:
        cows = 0 #Reset cows and bulls for each guess
        bulls = 0
        try:
            int(user_number) #Checking if input is int
            if len(user_number) == 4 and has_unique_digits(user_number) and user_number[0] != '0':

                #Counting cows
                for position in user_number:
                    if position in generated_number:
                        cows += 1

                #Counting bulls
                for position in range(4):
                    if user_number[position] == generated_number[position]:
                        bulls += 1
                        cows -= 1
                
                #Singular or plural print
                if cows == 1:
                    cow_cows = 'cow'
                else:
                    cow_cows = 'cows'
                if bulls == 1:
                    bull_bulls = 'bull'
                else:
                    bull_bulls = 'bulls'
                print(f'{bulls} {bull_bulls}, {cows} {cow_cows}')

            else:
                print('Not a 4-digit number / doesnt have unique digits / starts with zero')

        except ValueError:
            print("Input is not an int.")