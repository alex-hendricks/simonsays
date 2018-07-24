from getpass import getpass
# this script shows how to get user input

print "What is your name?"
name = raw_input()

color = getpass('what is your favorite color? ')

print "Hi", name
print "your favorite color is: ", color
