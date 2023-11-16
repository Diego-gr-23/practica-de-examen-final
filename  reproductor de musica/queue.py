from node import Node
from musica import Musica


class Queue:

    def __init__(self, maximun: int | None = None):
        self.size = 0
        self.max = maximun
        self.head: Node | None = None
        self.tail: Node | None = None

    def is_empty(self) -> bool:
        return self.head is None and self.tail is None

    def pop(self):
        if self.is_empty():
            raise Exception('Subdesbordamiento')
        elif self.head is self.tail:
            current = self.head
            self.head = None
            self.tail = None
            self.size = 0
            return current
        else:
            current = self.head
            self.head = self.head.next
            current.next = None
            self.size -= 1

            return current.data

    def push(self, data: Musica):
        if self.size == self.max:
            raise OverflowError
        else:
            if self.is_empty():
                new_node = Node(data)
                self.head = new_node
                self.tail = new_node
                self.size += 1
            else:
                new_node = Node(data)
                self.tail.next = new_node
                self.tail = new_node
                self.size += 1

    def transversal(self):
        current = self.head
        result = ''
        while current is not None:
            result += str(current)
            current = current.next

            if current is not None:
                result += ' \n'

        return result
