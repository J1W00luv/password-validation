import string

lowercase = string.ascii_lowercase
uppercase = string.ascii_uppercase
symbols = string.digits + string.punctuation

isStrong2 = False

while isStrong2 == False:
    userPassword = input("Enter your password: ")
    isStrong = [False for x in range(3)]

    if len(userPassword) >= 8:
        for x in userPassword:
            if x in lowercase:
                isStrong[0] = True
            elif x in uppercase:
                isStrong[1] = True
            elif x in symbols:
                isStrong[2] = True
            else:
                print("Error: Seems like you used a banned character")
    else:
        print("Error: Password is too short")
    
    if isStrong[0] == True and isStrong[1] == True and isStrong[2] == True:
        isStrong2 = True
    elif len(userPassword) >= 8: # only display error if the previous one (too short) is not shown
        print("Error: Password is not strong enough. Try using uppercase & lowercase letters and special symbols!")

print("Good job")