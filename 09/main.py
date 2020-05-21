word = input('Enter the word: ')
new_word = ''
for x in range (1,len(word),2):
    new_word += word[x]
print(new_word)
