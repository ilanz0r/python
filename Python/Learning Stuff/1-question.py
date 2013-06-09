# Basic question script
name = input('What is your name, young boy? ')

result = "Alas, your name is %s!" % (name)
print (result)

gender = input('Are you a male or a female? ')
gender = gender.lower()
if gender == "male" or gender == "m":
    print ("You're a Male!")
elif gender == "female" or gender == "f":
    print ("You're a female!")
else:
    print ("Wrong choice, fella.")

from datetime import datetime
now = today.datetime()
print (now)