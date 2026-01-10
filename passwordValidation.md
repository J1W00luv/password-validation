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



## **Testing results:**

| Input | Expected Output | Actual Output |
| ----- | --------------- | ------------- |
| HelloWorld | Error | Error: Password is not strong enough. Try using uppercase & lowercase letters and special symbols! |
| Hey1234 | Error | Error: Password is too short |
| Heyy1234 | Continuing | Good job |


## **Conclusion:**
	I have successfully written a program to validate passwords by making sure they are at least 8 characters long, have both uppercase and lowercase letters

## **Next steps:**
	My program could be improved by adding modules, checking if the user's password is in the list of common passwords, and making the code more efficient.
