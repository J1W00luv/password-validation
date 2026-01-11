# Password Strength Checker

## **Aim:**
To create a program that will check password strength by making sure user input is long, is a complicated combination of characters, and both capital & lower letters.

## **Method:**
	1. Research: Find out about minimum requirements for passwords.
	2. Pre-Coding: Create a pseudocode for the program.
	3. Code & Test: Implement the code and test it.

## **Problems i had during execution:**

| Problem | Description | Solution |
| ------- | ----------- | -------- |
| Array Setting | The array that was responsible for tracking how many conditions for the strong password are met was set outside the loop and never reset. | Put the setting array to all values being False inside the loop before checking if the conditions are met. | 
| Error Displaying Errors | The same error message was displayed a couple of times when checking for met conditions. | Add the condition to only display first first weakness found, also change "for in" loop to "for in range" to create a counter inside the loop. |



## **Testing results:**

| Input | Conditions Checked | Expected Output | Actual Output |
| ----- | ------------------ | --------------- | ------------- |
| password | common password, no uppercase, no symbols | error (common) | Error: Your password is too common |
| 123456 | common password, too short, no lowercase, no uppercase | error (common) | Error: Your password is too common |
| HELLO123 | no lowercase | error | Error: Your password does not have a lowercase letter |
| hello1234 | no uppercase | eroror | Error: Your password does not have an uppercase letter |
| HelloWorld | no symbols | error | Error: Your password does not have a special symbol or a digit |
| HelloWorld(0) | all met | cheer message | Well done! Your password is strong |


## **Conclusion:**
I have successfully written a program to validate passwords by making sure they are at least 8 characters long, have both uppercase and lowercase letters, and are not in the list of commonly used passwords.

## **Next steps:**
My program could be improved by making the code more efficient in general.


