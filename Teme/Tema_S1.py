''' ex. 1
Variabila - un loc din memorie in care punem valori, tinem anumite date
              - o cutie in care  punem diferite obiecte de care avem nevoie
'''

# ex.2
telefon_mobil = 'nokia' #string
model_telefon = 'smart'

ani_de_liceu = 4 #integer

nota_tema = 5.75 #float

imi_plac_pisicile = True #bool

# ex.3
print(type(telefon_mobil))
print(type(model_telefon))
print(type(ani_de_liceu))
print(type(nota_tema))
print(type(imi_plac_pisicile))

# ex.4
nota_tema = round(nota_tema)
print(round(nota_tema))
print(type(nota_tema))

# ex.5
print(f'Am primit un telefon, este marca {telefon_mobil}, de tipul {model_telefon}')
print(f'Am uitat toata informatica din cei {ani_de_liceu} ani de liceu')
print(f'Pentru tema anterioara nu cred ca merit nici macar nota {nota_tema}')
print(f'Locuiesc la curte si imi plac animalele {imi_plac_pisicile}')
#
# # ex.6
# numele = input('Introdu numele' )
# prenumele = input('Introdu prenumele')
# nume_complet = (len(numele)+len(prenumele))
# print(nume_complet)
# print(f'Numele complet are {nume_complet} caractere')
#
# # ex.7
# lungimea = int(input('Va rugam introduceti lungimea'))
# latimea = int(input('Va rugam introduceti latimea'))
# print(f'Aria dreptunghiului este {lungimea*latimea}')

# ex.8
text = 'Coral is either the stupidest animal or the smartest rock'
cuvant_the = text.split()
print(cuvant_the.count('the'))

# ex.9
text = 'Coral is either the stupidest animal or the smartest rock'
print(text.replace('the','THE'))

# ex.10
text_1 = 'Coral is either the stupidest animal or the smartest rock'
text_2 = text_1.isdigit()
print(type(text_2))
assert text_2 == False, 'Eroare! Acest string nu contine numere.'
print('Am verificat assert-ul, textul are doar litere!')











