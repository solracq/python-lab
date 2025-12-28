'''

@author: Solrac
'''

def parentesis_validation(lista):
    op = ['{', '[', '(']
    cp = ['}', ']', ')']
    stack = []
    
    for i in range(len(lista)):
        if lista[i] in op:
            stack.append(lista[i])
        elif lista[i] in cp:
            position = cp.index(lista[i])
            if len(lista) > 0 and stack[len(stack)-1] == op[position]:
                stack.pop
            else:
                return "UNBALANCED"
    if len(stack) == 0:
        return "BALANCED"
    
lista = ['{', '(', ')', '[', ']', '}']
print(lista)
print(parentesis_validation(lista))