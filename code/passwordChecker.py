import string
import csv
import os

def readFile(file_path):
    with open(file_path, newline='') as f:
        common_passwords = ["" for x in range(len(f.readlines()))]
        counter = 0

        f.seek(0)
        
        readfile = csv.reader(f)
        
        for row in readfile:
            common_passwords[counter] = row[0]
            counter += 1
    return common_passwords[1:]

def getPassword():
    user_password = input("Enter your password: ")
    return user_password

def isCommon(user_password, common_passwords):
    for password in common_passwords:
        if user_password == password:
            return False
    return True

def isLong(user_password):
    if len(user_password) >= 8:
        return True
    return False

def isPresent(user_password, array):
    for x in user_password:
        if x in array:
            return True
    return False

def main():
    os.system('cls' if os.name == 'nt' else 'clear')

    filePath = r"common_passwords.csv"
    commonPasswords = readFile(filePath)

    isStrong = False

    lowercase = string.ascii_lowercase
    uppercase = string.ascii_uppercase
    symbols = string.digits + string.punctuation

    errors = ["Error: Your password is too common", "Error: Your password is too short",
              "Error: Your password does not have a lowercase letter", "Error: Your password does not have an uppercase letter",
              "Error: Your password does not have a special symbol or a digit"]

    while isStrong == False:
        userPassword = getPassword()
        isValid = [False for x in range(5)] # array to track met conditions for a strong password

        isValid[0] = isCommon(userPassword, commonPasswords)
        isValid[1] = isLong(userPassword)
        isValid[2] = isPresent(userPassword, lowercase)
        isValid[3] = isPresent(userPassword, uppercase)
        isValid[4] = isPresent(userPassword, symbols)

        validCount = 0 # to count amount of met conditions

        for x in range(5): # 5 is length of isValid array
            if isValid[x] == True:
                validCount += 1
            elif (x - validCount) == 0: # check to only print one (first) error at a time
                print(errors[x])

        if validCount == 5:
            isStrong = True
    
    print("Well done! Your password is strong")

main()

