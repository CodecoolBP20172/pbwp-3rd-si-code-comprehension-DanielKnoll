"""In this guess a number game the following commands will be executed:
First the import command allowing access to random module's definitions and statements by granting access
to the module.
"""
import random

guessesTaken = 0  # Value declaration for a new variable named guessTaken. It takes part in the while loop below.

print('Hello! What is your name?')  # This displays the given string on the screen for the user.

"""Another declaration, the value will continuously reading from the user's keyboard until (s)he presses enter.
The input function always returns string type, so myName variable will store a string after execution.
Input can also send string to the screen like print does, so the previous line could be combined this thus
making the code DRYer.
"""
myName = input()

"""Another declaration. The value will be received from the random module's randit function,
which generates an integer number according to the arguments. In this case the value will be
between 1-20, including 1 and 20. The 'random.' shows that randint is not a built-in function.
"""
number = random.randint(1, 20)

"""This sends another string message to the user's screen with the print command.
But in this case the myName variable's value will be included into the string by the '+' string operator.
With the second add operator the rest of the text will be congratulated to the string.
"""
print('Well, ' + myName + ', I am thinking of a number between 1 and 20.')

"""In this loop the program sends a string to the screen, waits for an input from the user,
converts the received string value to integer number for the comparisons. Increases the iterator variable
by one and executes the following comparisons:
- Checks if the received value is lower compared to the randomly generated number.
- Checks if it is higher.
- Checks if the two values are equal.
The relational operator compares operands on both its sides and decides the relation between the two value.
Due to the if keyword the command(s) indented deeper in the following line will be only executed when the
comparison returns true value. Otherwise the indented command block will be skipped and the program proceeds
to the next line with the same indentation level.
From the three condition only one will return true value in a loop. In the first two if statements the program
informs the user that the given number is either lower or higher than the expected. Then the interpreter
jumps back to line with the while keyword and it preforms it's own comparison between the iterator value
and the set integer number. The user will have 5 loops to give a value equal to the generated number.
If this not happens the program will continue with the next line with the same indentation level as while.
If the user guesses the random value in one of the loops the and the equal comparison returns true the break
command will be executed and the interpreter jumps to the next command line (aligned with while).
Should have used if-elif-else statement.
"""
while guessesTaken < 6:
    print('Take a guess.')
    guess = input()
    guess = int(guess)

    guessesTaken += 1

    if guess < number:
        print('Your guess is too low.')

    if guess > number:
        print('Your guess is too high.')

    if guess == number:
        break

"""In these comparison the program handles the two possible outcomes.
If the user guessed the generated number the iterator value will be converted to string type and that will be
the new value of the variable. This was necessary because print can only use string types.
Then strings and variable values will be concatenationed and sent to the screen to congratulate the user's
incidental success.
At the other outcome the comparison uses the not equal relational operator and if that returns true similar
commands will be executed but the message is different. It will look down on the user and reveals the generated
number.

You guessed right I don't like RND games. This has around 0.23% probability (1-(19/20)^5).
"""
if guess == number:
    guessesTaken = str(guessesTaken)
    print('Good job, ' + myName + '! You guessed my number in ' + guessesTaken + ' guesses!')

if guess != number:
    number = str(number)
    print('Nope. The number I was thinking of was ' + number)
