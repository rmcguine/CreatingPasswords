#Prompt the user to enter two words and a number, storing each into separate variables.
favoriteColor = input('Enter favorite color: \n')
petName = input('Enter your pet\'s name: \n')
favoriteNumber = int(input('Enter your favorite number: \n'))

#Then, output those three values on a single line separated by a space.
print('%s %s %d' % (favoriteColor, petName, favoriteNumber))

#Output two passwords using a combination of the user input.
password1 = (favoriteColor + '_' + petName)
print('First password:', password1)

password2 = str(favoriteNumber) + (favoriteColor) + str(favoriteNumber)
print('Second password:', password2)

#Output the length of each password (the number of characters in the strings)
print(('Number of characters in %s:' % (password1)), len(password1))
print(('Number of characters in %s:' % (password2)), len(password2))