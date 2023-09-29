# This python code file gives you the square root of any number until you tell it to "quit"

import math

def square_root_num(n) -> None:
    """
    Returns the square root of any number until user types "quit"
    """
    input("Hello user! I will give you the square roots of numbers. (Please enter to continue)")

    userInput = input('Please enter a number. Type "quit" to quit: ')
    answer = 0  

    while userInput.lower() != 'quit':
        intUserInput = int(userInput)
        answer = math.sqrt(intUserInput)
        print("The Square root of " + str(intUserInput) + " is " + str(answer) + ".")
        userInput = input('Please enter the next number or type "quit" to quit: ')

    print("Goodbye")

square_root_num(2)