def giveName(email):  
    separateName = email.split("@")  
    if "_" in separateName[0]:  
        fullName = separateName[0].split("_")
        fullNameJoin = " ".join(fullName)  
        return_name = fullNameJoin.title()  
        return return_name
    else:  
        return_name = separateName[0].title() 
        return return_name

def main():
    userData = {}
    while True:
        email = input("Enter your email address (or press enter to stop): ")
        if email == '':
            break
        nameGuessed = giveName(email)
        print("Is your name", nameGuessed, "? (y/n)", end=" ")
        reCheckName = input()[0]  
        if reCheckName == 'y' or reCheckName == 'Y':
            userData[nameGuessed] = email
        else:
            nameTyped = input("Name: ")
            if nameTyped in userData:  
                print("Name already exists in the database. Re-enter Name: ", end="")
                nameTyped = input()
                userData[nameTyped] = email
            else:
                userData[nameTyped] = email

    print("\n")
    for key, value in userData.items():
        print(key, "(", value, ")")

if __name__ == '__main__':
    main()
