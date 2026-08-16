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

class goa:
    name=""
    drink=""
    def party(self):
        print("lets party...")
    def beach(self):
        print("enjoy the beach")

ramesh = goa()
suresh = goa()

ramesh.name="Ramesh"
suresh.name="Suresh"

ramesh.drink="yes"
suresh.drink="no"

print(ramesh.name)
print("drink:",ramesh.drink)
print(suresh.name)
print("drink:",suresh.drink) 

ramesh.party()
suresh.beach()