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

class student :
    def __init__ (self):
        self.name="nandhu"
        self.regno="8921"
    def display(self):
        print("Name:",self.name)
        print("Regno:",self.regno)


s1=student()
s2=student()
s1.name="mango"
s1.regno="123"

s2.name="raju"
s2.regno="6767"
s1.display()
s2.display()