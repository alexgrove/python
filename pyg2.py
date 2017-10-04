pyg = 'ay'
vowel = "aeiou"
gameRunning = True
while gameRunning == True:
    original = input('Enter a word: ')

    if original == "quit":
        break
    else:
        pass	
    if len(original) > 0 and original.isalpha():
        word = original.lower()
        if word[0] in vowel:
                print (original + pyg)
        else:
            word = original.lower()
            first = word[0]
            new_word = word+first+pyg
            new_word = new_word[1:len(new_word)]
            print (new_word)
    else:
        print ('empty')
print("Quitting...")