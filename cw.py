"""
listSample = [1, 4, 512, 24]

def add (c, amount = 1):
    print(id(c))
    c = c + amount
    print(id(c))

def append_element_to_list (listka, element):
    print(id(listka))
    listka.append(element)
    print(id(listka))

print(id(listSample))
append_element_to_list(listSample, 5)
print(listSample)

import copy
def evil_function(toBeDestroyedList):
    toBeDestroyedList[0] [0]= 20
    print(toBeDestroyedList)

myList = [[1, 4], [2, 1], [52, 3]]

evil_function(copy.deepcopy(myList))
"""
def podwoj (x):
    return x * 2

print(podwoj(4))

myList = [2, 14, 22, 7, 6, 4, 5, 17]
myListFiltered = list(filter(lambda x: x % 2 == 0, myList))
print (myListFiltered)