birthdays = {'Alice': 'Apr 1', 'Bob': 'Dec 12', 'Carol': 'Mar 4'} #puts a dictionary into the variable birthdays

while True: #while true run the code below
    print('Enter a name (blank to quit)') #prints to the screen
    name = input() #stores the user input inside the name variable 
    if name == '': #if user input is left blank run if clause 
        break #breaks out of the while loop if previous if condition is True 

    if name in birthdays: #if user input is in the dictionary birthdays
        print(birthdays[name] + ' is the birthday of ' + name) #print the referenced value plus the user input 
                                                               #the [name] refers to the referenced value in the dictionary 
    else: #if the name isn't in birthdays
        print('I do not have birthday information for ' + name)
        print('What is their birthday?')
        bday = input() #user input for the birthday 
        birthdays[name] = bday # (key pair assignment) assigns bday value to name key for dictionary 
        print("Birthday database updated")

