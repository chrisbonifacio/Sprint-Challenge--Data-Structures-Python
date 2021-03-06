from doubly_linked_list import DoublyLinkedList


class RingBuffer:
    def __init__(self, capacity):
        self.capacity = capacity
        self.current = None
        self.storage = DoublyLinkedList()

    def append(self, item):
        # if not at capacity, append to end of list
        if self.storage.length < self.capacity:
            self.storage.add_to_tail(item)
            self.current = self.storage.tail

        # if at capacity, connect storage head to tail
        if self.storage.length >= self.capacity:
            if self.current is self.storage.tail:
                self.storage.tail.next = self.storage.head

            self.current.value = item
            self.current = self.current.next

    def get(self):
        # Note:  This is the only [] allowed
        list_buffer_contents = []

        # TODO: Your code here
        current = self.storage.head

        while current:
            list_buffer_contents.append(current)
            current = current.next
            if current is self.storage.head:
                break

        return [item.value for item in list_buffer_contents]

# ----------------Stretch Goal-------------------


class ArrayRingBuffer:
    def __init__(self, capacity):
        pass

    def append(self, item):
        pass

    def get(self):
        pass
