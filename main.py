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

class laptop :
    def __init__(self):
        self.ram="" 
        self.processor=""
    def display(self):
        print("Ram",self.ram)
        print("Processor",self.processor)


hp=laptop()
hp.ram="8gb"
hp.processor="i5"

hp.display()
    
    
      
