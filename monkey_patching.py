"""
    created on june 17, 2019
    @author: Risasi
    
"""

class First:
    def __init__(self):
        pass
    def printer(self, msg):
        print(f'This is printer method and your msg is {msg}')

obj = First()
obj.printer('hi')

def display(self, my_var):
    print('This is display method')

First.printer = display
obj.printer('Hello')
