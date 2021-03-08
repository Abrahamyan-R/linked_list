class List:
    class __Node:
        def __init__(self, data):
            self.data = data
            self.next = None
            self.prev = None

    def __init__(self):
        self.__head = self.__tail = None
        self.__size = 0

    def __iter__(self):
        curr_node = self.__head
        while curr_node is not None:
            yield curr_node.data
            curr_node = curr_node.next

    def __len__(self):
        return self.__size

    def is_empty(self):
        return self.__head is None

    def push_back(self, value):
        new_node = self.__Node(value)

        if self.is_empty():
            self.__head = self.__tail = new_node
            self.__size += 1
            return

        self.__tail.next = new_node
        new_node.prev = self.__tail
        self.__tail = new_node

        self.__size += 1

    def push_front(self, value):
        new_node = self.__Node(value)

        if self.is_empty():
            self.__head = self.__tail = new_node
            self.__size += 1
            return

        self.__head.prev = new_node
        new_node.next = self.__head
        self.__head = new_node

        self.__size += 1

    def pop_back(self):
        if self.is_empty():
            # Throw custom exception
            pass

        if self.__head == self.__tail:
            self.__head = self.__tail = None
            return

        self.__tail = self.__tail.prev
        self.__tail.next.prev = None
        self.__tail.next = None

    def pop_front(self):
        if self.is_empty():
            # Throw custom exception
            pass

        if self.__head == self.__tail:
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