import random

thesaurus = {'hot':['balmy', 'summery', 'tropical', 'boiling', 'scorching'], 'cold':['chilly', 'cool', 'freezing', 'frigid', 'polar'],"happy":['content', 'cheery', 'merry', 'jovial', 'jocular'],"sad":['unhappy', 'downcast', 'miserable', 'glum', 'melancholy']}

print('\nWelcome to the Thesaurus App!')
print('\nChoose a word from the thesaurus and I will give you a synonym.')
print('\nHere are the words in the thesaurus:\n\t-hot\n\t-cold\n\t-happy\n\t-sad')
palabra = input('\nWhat word would you like a synonym for: ').lower()
if palabra in thesaurus:
    print(f'A synonym for {palabra} is {random.choice(thesaurus[palabra])}.')
else:
    print("I'm sorry, that word is not currently in the thesaurus.")
todo = input('\nWould you like to see the whole thesaurus (yes/no): ')
if todo == 'yes':
    for palabras in thesaurus:
        print(f'\n{palabras.title()} synonyms are:')
        for synonims in thesaurus[palabras]:
            print(f'\t-{synonims}')
elif todo == 'no':
    print('I hope you enjoyed the program. Thank you!')