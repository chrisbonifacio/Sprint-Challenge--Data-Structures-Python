class Node:
    def __init__(self, value=None, next_node=None):
        # the value at this linked list node
        self.value = value
        # reference to the next node in the list
        self.next_node = next_node

    def get_value(self):
        return self.value

    def get_next(self):
        return self.next_node

    def set_next(self, new_next):
        # set this node's next_node reference to the passed in node
        self.next_node = new_next


class LinkedList:
    def __init__(self):
        # reference to the head of the list
        self.head = None

    def __str__(self):
        current = self.head

        values = []

        while current:
            values.append(current.get_value())
            current = current.get_next()

        return f"{values}"

    def add_to_head(self, value):
        node = Node(value)
        if self.head is not None:
            node.set_next(self.head)

        self.head = node

    def contains(self, value):
        if not self.head:
            return False
        # get a reference to the node we're currently at; update this as we traverse the list
        current = self.head
        # check to see if we're at a valid node
        while current:
            # return True if the current value we're looking at matches our target value
            if current.get_value() == value:
                return True
            # update our current node to the current node's next node
            current = current.get_next()
        # if we've gotten here, then the target node isn't in our list
        return False

    def reverse_list(self):
        # TO BE COMPLETED
        prev = None
        curr = self.head
        nex = None

        while curr:
            # Before changing next of current,
            # store next node
            nex = curr.get_next()  # next = curr -> next

            # Now change next of current
            # This is where actual reversing happens
            curr.next_node = prev  # curr -> next = prev

            # Move prev and curr one step forward
            prev = curr
            curr = nex

        self.head = prev

        return self


linked_list = LinkedList()

linked_list.add_to_head('a')
linked_list.add_to_head('b')
linked_list.add_to_head('c')
linked_list.add_to_head('d')
print(linked_list)
linked_list.reverse_list()
print(linked_list)
