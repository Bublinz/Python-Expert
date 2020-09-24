#This program will accept words, sentence and display the number of vowels and consonants in such input

print('Make a sentence.')
vowel = ['a', 'e', 'i', 'o', 'u', 'A', 'E', 'O', 'U']
consonant = ['b', 'c', 'd', 'f', 'g', 'h', 'j', 'k', 'l', 'm', 'n', 'p', 'q', 'r', 's', 't', 'v', 'w', 'x', 'y', 'z', 'B', 'C', 'D', 'F', 'G', 'H', 'J', 'K', 'L', 'M', 'N', 'P', 'Q', 'R', 'S', 'T', 'V', 'W', 'X', 'Y', 'Z']

def ben(vowel,consonant):
        be = input()
        Vcount = 0
        Ccount = 0
        for me in be:
                if me in vowel:
                        Vcount += 1
                else:
                        Ccount += 1
                print('The vowel sound are: ' +  str(Vcount) )
                print('The consonant sound are: ' + str(Ccount) )
ben('vowel','consonant')






