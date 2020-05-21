word = input('Enter the word: ')

if len(word)>=2:
    print(f'{word[:2]}{word[-2:]}')
else:
    print('Empty string')