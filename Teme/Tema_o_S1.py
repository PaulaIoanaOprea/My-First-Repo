#ex.1
cuvant_impar = (input('Va rugam intruduceti cuvantul:'))
if len(cuvant_impar) % 2 != 0:
   litera_mijloc = cuvant_impar [len(cuvant_impar) // 2]
   print(f'Caracterul din mijloc este {litera_mijloc}')
else:
   print(f'Cuvantul introdus nu este impar')

# ex.2
palindrom = input('Introduceti un cuvant palindrom:')
Paula = palindrom[::-1]
assert palindrom == Paula , f'Cuvantul {palindrom} nu este un palindrom'
print (f' Cuvantul {palindrom} este un palindrom')

# ex.3
text, text_1 = input('Introduceti variabilele de la tastatura:').split()
print(text)
print(text_1)

# ex.4
string = input('Introdu string:')
string_1 = string [0]
string_final = string_1+string[1:-1].replace(string_1, string_1.upper())+string[-1]
print(string_final)

# ex.5
user = input('Introduceti user-ul:')
parola = input('Introduceti parola:')
print(f"Parola pt user {user} este {'*' * len(parola)} si are {len(parola)} caractere")











