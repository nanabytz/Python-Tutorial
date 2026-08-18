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

class calculator :
    def __init__(self,a,b):
        self.num1=a
        self.num2=b
    def add(self):
        print("add", self.num1+self.num2)
obj1=calculator(10,2)
obj1.add()
        



     