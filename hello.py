# # This program says hello and asks for my name.
# print('Hello world!')
# print('What is your name?') # ask for their name
# myName = input()
# print('It is good to meet you, ' + myName)
# print('The length of your name is:')
# print(len(myName))
# print('What is your age?') # ask for their age
# myAge = input()
# print('You will be ' + str(int(myAge) + 1) + ' in a year.')

# while True:
#     print('Who are you?')
#     name = input()
#     if name != 'Joe':
#         continue
#     print('Hello, Joe. What is the password? (It is a fish.)')
#     password = input()
#     if password == 'swordfish':
#         break
# print('Access granted.')


name = ''
while not name:
 print('Enter your name:')
 name = input()
print('How many guests will you have?')
numOfGuests = int(input())
if numOfGuests:
 print('Be sure to have enough room for all your guests.')
print('Done')
