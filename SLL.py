import gc

class Node:
    instances = 0

    def __init__(self, value = None):
        self.value = value
        self.next = None
        Node.instances += 1

class SLL:
    def __init__(self):
        self.head = None
        self.next_node = None

    #empties the list (!!! CAN NOT BE UNDONE !!!)
    def clear(self):
        self.head = None
        gc.collect()

    def prepend(self, value):
        new_node = Node(value)
        new_node.next = self.head
        self.head = new_node

    def append(self, value):
        if self.head is None:
            self.head = Node(value)
        else:
            current = self.head
            while current.next is not None:
                current = current.next
            current.next = Node(value)

    def retrieve(self, value):
        current = self.head
        while current is not None:
            if current.value == value:
                return current.value
            current = current.next
        return None

    #returns a string representation of the entire list
    def __str__(self):
        result= ""
        current = self.head
        while current is not None:
            result += str(current.value)
            current = current.next
        return result

    #delete the specified node if dound
    #if using custom classes, must supply an empty instance with item in class that is used to compare
    def delete(self, value):
        current = self.head

        if current is not None and current.value == value:
            self.head = current.next
            current = None
            return True

        prev = None
        while current is not None and current.value != value:
            prev = current
            current = current.next

        if current is None:
            return False
        else:
            prev.next = current.next
            current = None
            return True

    #inserts node into the list based on the order of the data component
    #if using customer classes, the class must have compare operators like <, <=, >, etc
    def insert_in_order(self, value):
        new_node = Node(value)

        if self.head is None or self.head.value >= value:
            new_node.next = self.head
            self.head = new_node
        else:
            current = self.head
            while current.next is not None and current.next.value < value:
                current = current.next

            new_node.next = current.next
            current.next = new_node

    #print all nodes recursively
    def print_nodes(self, node=None):
        if node is None:
            node = self.head
        if node is None:
            return None
        print(node.value)
        if node.next is not None:
            self.print_nodes(node.next)
        return

    #iterates through the list, returns data component of next node on each call of this function
    def iterate(self):
        # If there is a next node, return its data and move to the next node
        if self.next_node is not None:
            data = self.next_node.value
            self.next_node = self.next_node.next
            return data
        # Reset next_node to None when the end is reached to prepare for a new iteration if needed
        else:
            self.next_node = None  # Reset for the next iteration if you want to iterate again
            return None

    #reset iterator to begin of list
    def iterate_reset(self):
        self.next_node = self.head





