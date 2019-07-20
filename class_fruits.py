"""
Created on July 14, 2019
@author: Risasi

"""

class Fruits:
    cost = '90' #class veriable

    def __init__(self, name):
        self.name = name
        print("Fruits is " + self.name)

banana = Fruits('banana')
apple = Fruits('apple')

print('cost of banana is ' + banana.cost)
print('cost of apple is ' + apple.cost)
print('cost of Fruits is ' + Fruits.cost)
