'''
@author: Solrac
'''
"""Implementing the Queue linear data structure."""

class Queue:
    """Queue implementation through lists"""
    def __init__(self):
        self._items = []

    def enqueue(self, item):
        self._items.append(item)

    def dequeue(self):
        return self._items.pop()

    def front(self):
        return self._items[0]

    def rear(self):
        return self._items[len(self._items)-1]

    def is_null(self):
        if len(self._items) == 0:
            return True
        else:
            return False

    def is_full(self):
        return "\nThis list based Queue implementation cannot implement full Queues"

# if __name__ == "__main__":
#     queue = Queue()
#     queue.enqueue(5)
#     queue.enqueue(7)
#     queue.enqueue(9)
#     print(f"Is Queue full? {queue.is_full()}")
#     print(f"Is Queue empty? {queue.is_null()}")
#     print(queue.rear())
#     print(queue.front())
#     for i in range(3):
#         queue.dequeue()
#     print(f"Is Queue empty? {queue.is_null()}")