'''
projekt_1.py: První projekt do Engeto Online Python Akademie.
author: Matěj Frolík
email: matejfrolik1@seznam.cz
discord: Mates F.#4204
'''

# texts 

texts = ['''
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

#další data
users = ('bob', 'ann', 'mike', 'liz')
password = ('123', 'pass123', 'password123', 'pass1234')
sep = '-' * 40
dblsep = '=' * 40
star = '*'
import pwinput #naistalovaný modul pwinput v terminálu: pip install pwinput

#pozdravení uživatele 
print(dblsep, end = '\n')
print(f'Welcome in our app...')
print(f"Users: {' , '.join(users)} ")
print(dblsep, end = '\n')

#zadání jména a hesla s nekonečnou možností opravy  
attemps = 0
while True:
    user = input('Choose from users: ')
    passwrd = pwinput.pwinput(prompt='Enter your password: ', mask='*')

    if user in users and passwrd in password and users.index(user) is password.index(passwrd):
        print(sep, end='\n')
        print(f'Welcome to the app, {user}')
        print('We have 3 texts to be analyzed.')
        print(sep, end='\n')
        break
    else:
        print('Unregistred user. Check if you have Caps lock on and try again...')
        attemps += 1
        continue

#zadání textu a ověření vstupu s možností někonečné opravy

attemps2 = 0
while True:
    enter_text = input("Enter text's number: ")

    if enter_text.isnumeric() and len(texts) >= int(enter_text):
        print(f'Your choice is text{enter_text}')
        break
    else:
        print('Wrong attribute or text\'s number, try it again...')
        continue
print(sep, end='\n')

#práce s vybraným textem
# 1. počet slov
# 2. počet slov začínajících velkým písmenem
# 3. počet slov psaných velkými písmeny
# 4. počet slov psaných malými písmeny
# 5. počet čísel (ne cifer)
# 6. suma všech čísel (ne cifer) v textu

selected_text = texts[int(enter_text)-1]

#funkce na výpočet počtu slov
raw_words = list()
for word in selected_text.split():
    raw_words.append(word.strip(",.:;").lower()
    )
words_count = len(raw_words)
print(f'There are {words_count} words in the selected text')

#funkce na výpočet počtu slov s počátečním velkým písmenem
upper1_count = 0
split_text = selected_text.split()
for i in split_text:
     if i.istitle():
         upper1_count = upper1_count + 1
print(f'There are {upper1_count} titlecase words')

#funkce na výpočet počtu slov ALL UPPER
upper1_count = 0
for i in split_text:
     if i.isupper() and i.isalpha():
         upper1_count = upper1_count + 1
print(f'There are {upper1_count} uppercase words')

upper1_count = 0
for i in split_text:
     if i.islower():
         upper1_count = upper1_count + 1
print(f'There are {upper1_count} lowercase words')

#ekvivalentní výpočet počtu slov ALL UPPER - funkce MAP
# all_upper = sum(map(str.isupper, selected_text.split())) 
# print(all_upper)

#počet čísela  a jejich součet pomocí comprehension syntaxe
numbers = [int(i) for i in selected_text.split() if i.isdigit()]
print(f'There are {len(numbers)} numeric strings')
print(f'The sum of all the numbers: {sum(numbers)}')

print(sep, end = '\n')



    
