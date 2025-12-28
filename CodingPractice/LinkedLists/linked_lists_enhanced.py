class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

class LinkedList:
    def __init__(self):
        self.head = None

    def print_list(self):
        curr = self.head
        while curr:
            print(curr.data, end=" ")
            curr = curr.next

    def push(self, data):
        node = Node(data)
        if self.head:
            node.next = self.head
        self.head = node

    def insert(self, previous_node, data):
        if previous_node:
            node = Node(data)
            node.next = previous_node.next
            previous_node.next = node
        else:
            raise ValueError(f"{previous_node} doesn't exist")

    def add(self, data):
        node = Node(data)
        if self.head is None:
            self.head = node
        curr = self.head
        while curr.next:
            curr = curr.next
        curr.next = node

    def lremove(self):
        self._validate_head_exists()
        self.head = self.head.next

    def remove(self):
        self._validate_head_exists()
        last = self.head
        while last.next:
            previous = last
            last = last.next
        previous.next = None

    def remove_middle(self, data):
        self._validate_head_exists()
        node = self.head
        while node.next:
            if node.data == data:
                previous.next = node.next
                break
            previous = node
            node = node.next

    def _validate_head_exists(self):
        if self.head is None:
            raise ValueError("List is empty, cannot remove item")

    def sort_list(self):
        array = []
        curr = self.head
        while curr:
            array.append(curr.data)
            curr = curr.next
        array.sort()
        curr = self.head
        for value in array:
            curr.data = value
            curr = curr.next


if __name__ == "__main__":
    ll = LinkedList()
    ll.head = Node(1)

    node2 = Node(2)
    node3 = Node(3)
    node4 = Node(4)
    node5 = Node(5)

    ll.head.next = node2
    node2.next = node3
    node3.next = node4
    node4.next = node5

    ll.push(9)
    ll.insert(node3, 8)
    ll.add(6)

    ll.print_list()
    print("\n")

    ll.lremove()
    ll.remove()
    ll.remove_middle(8)
    ll.print_list()