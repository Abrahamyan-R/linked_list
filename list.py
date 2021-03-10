class List:
    class __Node:
        def __init__(self, data):
            self.data = data
            self.next = None
            self.prev = None

        def __eq__(self, other):
            if type(other) == type(self):
                return self.data == other.data
            return self.data == other

    def __init__(self):
        self.__head = self.__tail = None
        self.__size = 0

    def front(self):
        return self.__head.data if self.__head else None

    def back(self):
        return self.__tail.data if self.__tail else None

    def __iter__(self):
        curr_node = self.__head
        while curr_node is not None:
            yield curr_node.data
            curr_node = curr_node.next

    def __len__(self):
        return self.__size

    def is_empty(self):
        return self.__head is None

    def size(self):
        return self.__size

    def clear(self):
        while (not self.is_empty()):
            self.pop_back()

    def insert(self, pos, value):
        if pos < 0 or pos >= self.__size:
            # Throw custom exception
            pass

        if pos == 0:
            return self.push_front(value)

        curr_node = self.__head
        while pos > 0:
            curr_node = curr_node.next
            pos -= 1

        new_node = self.__Node(value)

        new_node.next = curr_node
        new_node.prev = curr_node.prev
        curr_node.prev.next = new_node
        curr_node.prev = new_node

        return value

    def push_back(self, value):
        new_node = self.__Node(value)

        if self.is_empty():
            self.__head = self.__tail = new_node
            self.__size += 1
            return value

        self.__tail.next = new_node
        new_node.prev = self.__tail
        self.__tail = new_node

        self.__size += 1
        return value

    def push_front(self, value):
        new_node = self.__Node(value)

        if self.is_empty():
            self.__head = self.__tail = new_node
            self.__size += 1
            return value

        self.__head.prev = new_node
        new_node.next = self.__head
        self.__head = new_node

        self.__size += 1
        return value

    def pop_back(self):
        if self.is_empty():
            # Throw custom exception
            pass

        if self.__head is self.__tail:
            self.__head = self.__tail = None
            return

        self.__tail = self.__tail.prev
        self.__tail.next.prev = None
        self.__tail.next = None

    def pop_front(self):
        if self.is_empty():
            # Throw custom exception
            pass

        if self.__head is self.__tail:
            self.__head = self.__tail = None
            return

        self.__head = self.__head.next
        self.__head.prev.next = None
        self.__head.prev = None

    def __get_node_by_index(self, index):
        if (index < 0 or index >= self.__size):
            # Throw custom exception
            pass

        curr_node = self.__head
        while index > 0:
            curr_node = curr_node.next
            index -= 1

        return curr_node

    def __getitem__(self, index):
        if isinstance(index, slice):
            indices = range(*index.indices(self.__size))
            return [self[i] for i in indices]
        return self.__get_node_by_index(index).data

    def __setitem__(self, index, value):
        node = self.__get_node_by_index(index)

        node.data = value
        return value

    def remove(self, value):
        curr_node = self.__head
        while curr_node:
            next_node = curr_node.next
            if curr_node == value:
                if curr_node is self.__head:
                    self.pop_front()
                elif curr_node is self.__tail:
                    self.pop_back()
                else:
                    curr_node.prev.next = curr_node.next
                    curr_node.next.prev = curr_node.prev
                    curr_node.prev = curr_node.next = None
            curr_node = next_node

    def reverse(self):
        if self.is_empty() or self.__size == 1:
            return

        curr_node = self.__head

        while curr_node is not None:
            tmp = curr_node.prev
            curr_node.prev = curr_node.next
            curr_node.next = tmp
            curr_node = curr_node.prev

        self.__head, self.__tail = self.__tail, self.__head

    def make_unique(self):
        if self.is_empty() or self.__size == 1:
            return

        curr_node = self.__head

        while curr_node:
            next_node = curr_node.next
            while next_node:
                tmp = next_node.next
                if curr_node == next_node:
                    if next_node is self.__tail:
                        self.__tail = next_node.prev

                    next_node.prev.next = next_node.next

                    if next_node.next:
                        next_node.next.prev = next_node.prev

                    next_node.prev = None
                    next_node.next = None
                    
                    self.__size -= 1
                next_node = tmp
            curr_node = curr_node.next