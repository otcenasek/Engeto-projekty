'''
author = 
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

users = {
    'bob' : '123',
    'ann' : 'pass123',
    'mike' : 'password1123',
    'liz' : 'pass123'
    }
separator = '-' *50
platne_volby = {1,2,3}
print(separator)
name = str(input('username:'))
password = str(input('password:'))
print (separator)
if users[name] == password:
    print ('Wellcome to the app {} \nWe have {} text to be analyzed'.format(name.capitalize(),3))
    print (separator)
else:
    quit()
vyber = input('Enter a number btw. {} and {} to select: '.format(1,3))
if str(vyber).isnumeric() == False:
    print('Nebylo zadane cislo')
    quit()
vyber = int(vyber)-1
if vyber not in range(3):
    print('input out of range')
    quit()

print (separator)
# ziska list slov, rozdeli text v miostech mezer, odstrani nezadouci znaky
slova = [slovo.strip('\n.') for slovo in TEXTS[vyber].split(' ')]

#slova.remove('')                                                                                                                                       
slova = [slovo for slovo in slova if slovo]

print('There are {}  words ion the selected text'.format(len(slova)))

# ziska seznam slov s velkym pismenem naprvnim miste
slova_title = [slovo for slovo in slova if slovo.istitle()]
print ('There are {} titlecase words'.format(len(slova_title)))

#ziska slova z velkych pismen
slova_upper = [slovo for slovo in slova if slovo.isupper() and slovo.istitle() == False]
print ('There are {} uppercase words'.format(len(slova_upper)))

#ziska slova z malych pismen
slova_lower = [slovo for slovo in slova if slovo.islower()]
print ('There are {} lowercase words'.format(len(slova_lower)))

#ziska cila
pocet_cisel = [slovo for slovo in slova if slovo.isnumeric()]
print ('There are {} numeric strings'.format(len(pocet_cisel)))

# secte cisla
soucet = 0
for i in pocet_cisel:
    soucet = soucet + int(i)
print ('The sum of all the numbers ', soucet)
print(separator)

#nejdelsi_slovo = ''

cetnost = {}
for slovo in slova:
    if str(len(slovo)) in cetnost.keys():
        cetnost[str(len(slovo))] +=1
    else:
        cetnost[str(len(slovo))] = 1

        
print(separator)
print('LEN|  OCCURENCES    |NR.')
print (separator)
for i in sorted(cetnost):
    print ('{:3}|{:16}|{}'.format(i, (int(i)*'*'), cetnost[i]))

    
    
#    if len(nejdelsi_slovo) < len(slovo):
#       nejdelsi_slovo = slovo






