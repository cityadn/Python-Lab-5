import re
def vowel_or_consanant(letter):
    vowels = ['a', 'e', 'i', 'o', 'u']
    if letter in vowels and type(letter) == str:
        return "It's a vowel"
    elif letter.isnumeric() == True or (bool(re.match('^[a-zA-Z0-9]*$', letter)) == False):
        return "It's not a character"
    else:
        return "It's a consanant"

letter = input("Enter a letter:\n")
while len(letter) != 1:
    letter = input("Enter a letter:\n")
print(vowel_or_consanant(letter))
