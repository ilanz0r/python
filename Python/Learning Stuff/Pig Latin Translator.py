# Pig latin "translator"
"""
Basically this program takes an input from user (namely /word/), checks
if it is an actual word (only alphabetical characters, make sure it's not empty)
and then moves the first letter to the end, and adds "ay" to the beginning.
For example: apple -> pllea -> aypllea
"""
print ("Welcome to PygLatin!")

original_word = input('Input word: ')
original_word = original_word.lower()
# Check if word is valid
if original_word == "":
    print ("Blanks not allowed!"); exit()
elif original_word.isalpha() == False:
	print ("Only alphabetical chars allowed!"); exit()
first_letter = original_word[0]
# Consonant or vowel as first letter?
if first_letter == "a" or first_letter == "e" or first_letter == "i" or first_letter == "o" or first_letter == "u":
# Since it's a vowel, you just add "way" to the end.
    new_word = original_word + "way"; print ("Your new word is: " + new_word)
else: # Since it's a consonant, I take the word, chop off the first letter, add it to the end using the first_letter var, then I add "hay", then print it.
    temp = len(original_word); tempword = original_word[1:temp] + first_letter + "ay"; print ("Your new word is " + tempword)