def giveName(email):		#FUnction to split the email to return the name
    separateName = []		#Declaring a list to store the split
    separateName = email.split("@")			#Split if we find @ in the email
    if "_" in separateName[0]:				#After spliting if we find '_' symbol than split again
        fullName = separateName[0].split("_")
        fullNameJoin = " ".join(fullName)		#Using join we are joining two string together with a space in between
        returName = fullNameJoin.title()		#title() is used to uppercase the frist letter
        return returName
    else:		#If there is no '_' than return the initial split
        returName = separateName[0].title()     #So, that we can convert the list (separateName) to a string variable (returName)
        return returName

userData = {}
while True:
    email = input("Email: ")
    if(email == ''):
        break
    nameGuessed = giveName(email)
    print("Is your name", nameGuessed, "? (y/n)", end=" ")
    reCheckName = input()[0]		#[0] is used to take only 1 character as an input from the user
    if reCheckName == 'y' or reCheckName == 'Y':
        userData[nameGuessed] = email;
    else:
        nameTyped = input("Name: ")
        if nameTyped in userData:		#To check if there is same name in the dictionary
            print("Name already exists is the database. Re-enter Name: ", end="")
            nameTyped = input()
            userData[nameTyped] = email;
        else:
            userData[nameTyped] = email;

#print(userData)
print("\n")
#Printing the key:value pair that is stored in the dictionary
for key, value in userData.items():
    print(key, "(", value, ")")