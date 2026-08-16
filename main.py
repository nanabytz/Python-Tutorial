#print("Hello world")
# This is a sample Python script.
#import numbers
#from itertools import count
#from random import choice

# Press Shift+F10 to execute it or replace it with your code.
# Press Double Shift to search everywhere for classes, files, tool windows, actions, and settings.


#def print_hi(name):
    # Use a breakpoint in the code line below to debug your script.
    #print(f'Hi, {name}')  # Press Ctrl+F8 to toggle the breakpoint.


# Press the green button in the gutter to run the script.
#if __name__ == '__main__':
    #print_hi('PyCharm')

# See PyCharm help at https://www.jetbrains.com/help/

s_username="nan"
s_password="123"

uname = input("Username: ")
password = input("Password: ")

def validate():
    if s_username == uname and s_password == password:
        return "correct"
    else:
        return "wrong"

a=validate()
print(a)

  
