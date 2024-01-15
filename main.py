"""
This slot is about basic input and output with Python

About output:
    Basic output is show some information in the console. Ex: print the word "hello" on screen
    To do this, we use syntax:
        print(x)
    with x is the string that we wanna to show (string is a variance type in Python such as "hello my love"

    Advanced usage is
        print(data1, data2, sep)
    sep is seperator, it will be displayed between two data.
    The default sep is a space
    For example, print("Hello", "World") -> "Hello World" but print("Hello", "World", sep='') -> "HelloWorld"
    There can be more than two data (exactly, more than one output string parameter)

About input:
    We always need to read data that user input to our program
    To do this, we use the syntax
        x = input()
    with x is the destination variance that store the input data.
    All the input data will be stored as a string.
    For example, we input number 12, the stored data will be "12". Note that 12 is number and "12" is a string

    Moreover, we can pass a prompt into this syntax to notify the user.
    For example, the following command:
        s = input("Input your name:")
    the program will print the string "Input your name:" and the user will input their data.
    Finally, that data will be stored in s

And the following code is some practical example.
"""

print("Hello_world")

print("Hello", "Nguyet")

print("Hello", "World", sep="")

print("This", "is", "a sentence", "with 3 words")




