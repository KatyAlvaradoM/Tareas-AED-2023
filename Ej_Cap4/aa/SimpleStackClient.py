from SimpleStack import *

#para probar en una pila llena

stack = Stack(2)
for word in ['May', 'the', 'force', 'be', 'with', 'you']:
   stack.push(word)

print('After pushing', len(stack), 
      'words on the stack, it contains:\n', stack)
print('Is stack full?', stack.isFull())

print('Popping items off the stack:')
while not stack.isEmpty():
   print(stack.pop(), end=' ')
print()


"""#para probar una pila vacia
stack = Stack(3)
stack.push(2)
stack.push(3)
stack.push(12)

print('Is stack full?', stack.isFull())

while not stack.isEmpty():
   item=stack.pop()#aqui los borra 
   print(stack.pop(), end=' ')
print()
"""

