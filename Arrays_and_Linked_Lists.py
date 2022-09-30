''' There are fixed-size arrays and extensible arrays.
for 'in' or 'not in' built-in functions they use linear search algorithm 
checking the array for the first occurence of the input value.
Most effective for unsorted and short lists.

Binary search is faster but requires that the arrays elements are sorted first.
'''


class Node:
    # Creating a node
    def __init__(self, item):
        self.item = item
        self.next = None


class LinkedList:

    def __init__(self):
        self.head = None
        
    def traverse(self):
        node = self.head
        while node != None:
            print(node.item)
            node = node.next

    # if __name__ == '__main__':

linked_list = LinkedList()

# Assign item values
linked_list.head = Node(1)
second = Node(2)
third = Node(3)
fourth = Node(4)
fifth = Node(5)

# Connect nodes
linked_list.head.next = second
second.next = third
third.next = fourth
fourth.next = fifth
fifth.next = None

'''Applications of Linked Lists:
Dynamic memory allocation
Implemented in stack and queue
In undo functionality of softwares
Hash tables, 
Graphs
'''

def insert(llist, obj, position):
    '''The time-complexity: O(n), Ω(1) '''
    if position == 0:
        obj.next = llist.head
        llist.head = obj

    else:
        node = llist.head
        for n in range(1, position):
            prev_node = node
            node = node.next

        prev_node.next = obj

        if node == None:
            obj.next = None
        else:
            obj.next = node
        
    

def delete(llist, obj):
    ''' The time complexity is: O(n) and Ω(1)'''
    node = llist.head
    if obj == llist.head.item:
        llist.head = llist.head.next
        llist.head.next = None
    else:    
        while obj != node.item and node != None:
            prev_node = node
            node = node.next
        prev_node.next = node.next
        node.next = None


hi = Node('hi')

insert(linked_list, hi, 3)
linked_list.traverse()
print(' ')

delete(linked_list, 'hi')
linked_list.traverse()
print(' ')

delete(linked_list, 1)
linked_list.traverse()
