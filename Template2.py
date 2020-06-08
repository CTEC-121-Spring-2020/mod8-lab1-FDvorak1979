"""
CTEC 121
Frank Dvorak
<assignment/lab name>
<assignment/lab description
"""

""" IPO template
Input(s): list/description
Process: description of what function does
Output: return value and description
"""
# Mod 7
'''
myDict = {}
myDict["key"] = "value1"
print(myDict.keys())
print(myDict.values())
print(myDict.items())
'''

'''
fileHandle = open("sample.txt", "r")
print()
readReturn = fileHandle.read()
print(type(readReturn))
print("*", fileHandle.read(),"*")
fileHandle.close()
print()

'''

# Mod 7 PA Prob 2
'''
print(5*'A')

'''
'''
# Mod 8 Lab 1
from graphics import *
def main():
    # section 1
    win = GraphWin("demo", 1000, 1000)
    myCircle = circle(point(500, 500), 200)
    myCircle.setFill("blue")
    myCircle.draw(win)
    win.getMouse()
'''
from graphics import *
from msdie import MSdie
from deocTest
'''
from dog import Dog

d = Dog("Dog")
print(d)
print(d.getName())
d.setName("Godzilla")

'''
# section 3

die = MSDie(6)
print("number of sides", die.getSides())
print("value: "
die.setValue(5)
die.roll()
print("value:", die.getvalue())

main()    