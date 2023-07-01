'''
projekt_1.py: první projekt do Engeto Online Python Akademie
author: Veronika Fellnerova
email: veronika.fellnerova@seznam.cz
discord: Verca F.#5057
'''
TEXTS = ['''
Situated about 10 miles west of Kemmerer,
Fossil Butte is a ruggedly impressive
topographic feature that rises sharply
some 1000 feet above Twin Creek Valley
to an elevation of more than 7500 feet
above sea level. The butte is located just
north of US 30N and the Union Pacific Railroad,
which traverse the valley. ''',
'''At the base of Fossil Butte are the bright
red, purple, yellow and gray beds of the Wasatch
Formation. Eroded portions of these horizontal
beds slope gradually upward from the valley floor
and steepen abruptly. Overlying them and extending
to the top of the butte are the much steeper
buff-to-white beds of the Green River Formation,
which are about 300 feet thick.''',
'''The monument contains 8198 acres and protects
a portion of the largest deposit of freshwater fish
fossils in the world. The richest fossil fish deposits
are found in multiple limestone layers, which lie some
100 feet below the top of the butte. The fossils
represent several varieties of perch, as well as
other freshwater genera and herring similar to those
in modern oceans. Other fish such as paddlefish,
garpike and stingray are also present.'''
]

registrations = [
    {'user': 'bob', 'password': 123},
    {'user': 'ann', 'password': 'pass123'},
    {'user': 'mike', 'password': 'password123'},
    {'user': 'liz', 'password': 'pass123'}
                ]

user_name = input('Enter username: ')
user_password = input('Enter password: ')



if any(str(registration.get('user')) == user_name and str(registration.get('password')) == user_password for registration in registrations):
    print(f'Welcome to the app, {user_name}. We have {len(TEXTS)} texts to be analyzed.')
    num_of_text = input('Enter a number btw. 1 and 3 to select: ')
    try:
        value = int(num_of_text)
        if int(num_of_text) in range(1,len(TEXTS)+1):
            text = TEXTS[int(num_of_text)-1].replace('.',' ').replace(',',' ').replace('\n', ' ')
            words_list = list(text.split(' '))
            words_list = [space for space in words_list if space != '']


            #počet slov =54
            words_count = len(words_list)
            print(f'There are {words_count} words in the selected text.')


            #počet slov začínajících velkým písmenem =12
            words_count_upper_letter = 0
            for word in words_list:
                if word[0].isupper():
                    words_count_upper_letter += 1
            print(f'There are {words_count_upper_letter} titlecase words.')


            #počet slov psaných velkými písmeny =1 nebo 2
            words_count_upper = 0
            for word in words_list:
                if word.isupper() and not any(letter.isdigit() for letter in word):
                    words_count_upper += 1
            print(f'There are {words_count_upper} uppercase words.')


            #počet slov psaných malými písmeny =38
            words_count_lower = 0
            for word in words_list:
                if word.islower():
                    words_count_lower += 1
            print(f'There are {words_count_lower} lowercase words.')


            #počet čísel (ne cifer) =4  #sumu všech čísel (ne cifer) v textu =8540
            num_count = 0
            nums = []
            for word in words_list:
                result = any(letter.isdigit() for letter in word)
                if result is True:
                    num_count += 1
                    num = ''
                    for character in word:
                        if character.isdigit():
                            num = num + character
                    nums.append(int(num))
            print(f'There are {num_count} numeric strings.')
            print(f'The sum of all the numbers {sum(nums)}.')


            #cetnost delek slov v textu
            word_lengths = {}
            for word in words_list:
                if len(word) not in word_lengths:
                    word_lengths.update({len(word) : 1})
                else:
                    word_lengths[len(word)] += 1
            word_lengths_sorted = dict(sorted(word_lengths.items()))

            max_value = max(word_lengths.values())
            space_title = ' ' * round((((max_value + 1) - len('OCCURENCES'))/2) +0.5) + 'OCCURENCES' + ' ' * round((((max_value + 1) -len('OCCURENCES'))/2) -0.5)

            print('----------------------------------------')
            print(f'LEN|{space_title}|NR.')
            print('----------------------------------------')

            for key, value in word_lengths_sorted.items():
                stars = value * '*'
                space = ' ' * (max_value + 1 - len(stars))
                if key in range(1,10):
                    print(f'  {key}|{stars}{space}|{value}')
                elif key in range(10,100):
                    print(f' {key}|{stars}{space}|{value}')
                else:
                    print(f'{key}|{stars}{space}|{value}')

        else:
            print('number out of scope')
    except ValueError:
        print('input not an integer')
else:
    print('unregistered user, terminating the program..')