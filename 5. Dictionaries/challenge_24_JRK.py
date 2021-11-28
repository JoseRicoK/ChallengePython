from collections import Counter

print('\nWelcome to the Frequency Analysis App')
caracteres = '".,:;-_ç0987654321<>+*Ç}][{ '
alf = 'abcdefghijklmnñopqlsrtuvwxyz'
num = 0
while num < 3:
    num += 1
    frase = input('\nEnter a word or phrase to count the occurrence of each letter: ').lower()
    for x in range(len(caracteres)):
        frase = frase.replace(caracteres[x],"")
    print(f'\nHere is the frequency analysis from key phrase {num}:')
    print('Letter  Occurrence  Percentage')
    for letra in alf:
        ca = frase.count(letra)
        if ca > 0:
            print(f'{letra}       {ca}       {round(ca/len(frase)*100, 2)}%')
    print('\nLetters ordered from highest occurrence to lowest:')
    n=100
    counter=Counter(frase)
    res = [letter[0] for letter in counter.most_common(n)]
    print(res)
#[JRK]