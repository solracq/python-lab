"""
@author: Solrac
"""
"""Stack class that mimics the stack linear data behaivour."""


class Stack:
    def __init__(self):
        self._items = [] # private class variable. It shouldn't be used outside of the Stack class.

    def push(self, item):
        self._items.append(item)

    def pop(self):
        return self._items.pop()

    def top(self):
        return self._items[len(self._items)-1]

    def size(self):
        return len(self._items)

    def is_empty(self):
        if self.size() == 0:
            return True
        else:
            return False

    def __repr__(self):
        return f'{type(self).__name__} at 0x{id(self):x}, size={len(self)}>'

    def __len__(self):
        return len(self._items)

# if __name__ == "__main__":
#     stack = Stack()
#     stack.push(5)
#     stack.push(7)
#     stack.push(9)
#     print(stack._items) # private variable of the Stack class CANNOT be used here
#     print(stack.__len__()) # Not needed, instead use len(stack)
#     print(len(stack))
#     print(stack.pop())
#     print(stack._items)
#     print(type(stack)) # Any object is an instance of its type
#     print(stack.top())
#     print(stack.size())
#     print(f"Is the stack empty? {stack.is_empty()}")
#     print(stack.pop())
#     print(stack.pop())
#     print(f"Is the stack empty? {stack.is_empty()}")