'''
@author: Solrac
'''
import LinkedList

def createNodes():
    node1 = LinkedList.Node(3)
    node2 = LinkedList.Node(5)
    node3 = LinkedList.Node(7)
    node4 = LinkedList.Node(9)
    
    node1.next = node2
    node2.next = node3
    node3.next = node4
    node4.next = None

    node1.traverse()
    
if __name__ == "__main__":
    print(createNodes())
