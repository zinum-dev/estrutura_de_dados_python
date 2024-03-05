# Problema: Implementar uma função que inverta os elementos de uma lista/array

def invert(list:list):
    reversed = []
    for i in list:
        reversed.insert(0,i)
    return reversed


list = [1,2,3,4,5,6]
print(list)
reverserd = invert(list)
print(reverserd)