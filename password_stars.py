#set len to 0
length=0
#repeat until user enters a password greater than or equal to 10
while length < 10:
    #read a password from user
    password = input("Enter your password ")
    #calculate length of password
    length = len(password)
    #if password doesn't meet minimum length display an error message
    if length < 10:
        print("Your password is weak!! Please choose a password with minimum length 10")
    #otherwise print '*' equalent to length
    else:
        print('*' * length)