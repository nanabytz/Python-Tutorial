#print("Hello world")
# This is a sample Python script.
import numbers
from random import choice

# Press Shift+F10 to execute it or replace it with your code.
# Press Double Shift to search everywhere for classes, files, tool windows, actions, and settings.


#def print_hi(name):
    # Use a breakpoint in the code line below to debug your script.
    #print(f'Hi, {name}')  # Press Ctrl+F8 to toggle the breakpoint.


# Press the green button in the gutter to run the script.
#if __name__ == '__main__':
    #print_hi('PyCharm')

# See PyCharm help at https://www.jetbrains.com/help/pycharm/


a=int(input("Enter your salary: "))
b=int(input("Enter your age: "))
if a>=20000 or b<=25:
    print("your eligible")
    loan=int(input("Enter your required loan amount: "))
    if loan <= 50000:
        print("your eligible for loan")
    else:
        print("maximum loan amount is 50000")




else:
    print("your not eligible")
