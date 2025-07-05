# ------------------------------
# Node class for doubly linked list
# ------------------------------
class Node:
    def __init__(self, value):
        self.value = value
        self.next = None
        self.prev = None

# ------------------------------
# Doubly LinkedList class with methods
# ------------------------------
class DoublyLinkedList:
    def __init__(self, value):
        new_node = Node(value)
        self.__head = new_node
        self.__tail = new_node
        self.__length = 1

     # -------------------------------
    # Properties: head, tail, length
    # -------------------------------
    @property
    def head(self):
        return self.__head

    @head.setter
    def head(self, node):
        self.__head = node

    @property
    def tail(self):
        return self.__tail

    @tail.setter
    def tail(self, node):
        self.__tail = node

    @property
    def length(self):
        return self.__length

    @length.setter
    def length(self, value):
        if value >= 0:
            self.__length = value
        else:
            raise ValueError("Length cannot be negative.")

    # -------------------------------
    # Core methods (unchanged logic)
    # -------------------------------
    def print_list(self):
        """Print the linked list in a readable format."""
        if self.__head is None:
            print("empty list")
        else:
            values = []
            temp = self.__head
            while temp:
                values.append(str(temp.value))
                temp = temp.next
            values.append("None")
            print(" <-> ".join(values))

    def make_empty(self):
        """Reset the linked list to empty"""
        self.__head = None
        self.__tail = None
        self.__length = 0

    def append(self, value):
        """Add a node at the end"""
        new_node = Node(value)
        if self.__length == 0:
            self.__head = new_node
            self.__tail = new_node
        else:
            self.__tail.next = new_node
            new_node.prev = self.__tail
            self.__tail = new_node
        self.__length += 1
        return True

    def pop(self):
        """Remove and return the last node"""
        if self.__length == 0:
            return None
        temp = self.__tail
        if self.__length == 1:
            self.__head = None
            self.__tail = None
        else:
            self.__tail = self.__tail.prev
            self.__tail.next = None
            temp.prev = None
        self.__length -= 1
        return temp

    def prepend(self, value):
        """Add a node at the beginning"""
        new_node = Node(value)
        if self.__length == 0:
            self.__head = new_node
            self.__tail = new_node
        else:
            new_node.next = self.__head
            self.__head.prev = new_node
            self.__head = new_node
        self.__length += 1
        return True

    def pop_first(self):
        """Remove and return the first node"""
        if self.__length == 0:
            return None
        temp = self.__head
        if self.__length == 1:
            self.__head = None
            self.__tail = None
        else:
            self.__head = self.__head.next
            self.__head.prev = None
            temp.next = None
        self.__length -= 1
        return temp

    def get(self, index):
        """Return the node at the specified index"""
        if index < 0 or index >= self.__length:
            return None
        if index < self.__length / 2:
            temp = self.__head
            for _ in range(index):
                temp = temp.next
        else:
            temp = self.__tail
            for _ in range(self.__length - 1, index, -1):
                temp = temp.prev
        return temp

    def set_value(self, index, value):
        """Set the value at the specified index"""
        temp = self.get(index)
        if temp:
            temp.value = value
            return True
        return False

    def insert(self, index, value):
        """Insert a node at the specified index"""
        if index < 0 or index > self.__length:
            return False
        if index == 0:
            return self.prepend(value)
        if index == self.__length:
            return self.append(value)
        new_node = Node(value)
        before = self.get(index - 1)
        after = before.next
        new_node.prev = before
        new_node.next = after
        before.next = new_node
        after.prev = new_node
        self.__length += 1
        return True

    def remove(self, index):
        """Remove and return the node at the specified index"""
        if index < 0 or index >= self.__length:
            return None
        if index == 0:
            return self.pop_first()
        if index == self.__length - 1:
            return self.pop()
        temp = self.get(index)
        temp.prev.next = temp.next
        temp.next.prev = temp.prev
        temp.next = None
        temp.prev = None
        self.__length -= 1
        return temp

    def is_palindrome(self):
        """Check if the list is a palindrome"""
        if self.__length <= 1:
            return True
        left = self.__head
        right = self.__tail
        for _ in range(self.__length // 2):
            if left.value != right.value:
                return False
            left = left.next
            right = right.prev
        return True

    def reverse(self):
        """Reverse the entire linked list"""
        temp = self.__head
        while temp:
            temp.prev, temp.next = temp.next, temp.prev
            temp = temp.prev
        self.__head, self.__tail = self.__tail, self.__head

    def partition_list(self, x):
        """Partition list around value x"""
        if not self.__head:
            return
        dummy1 = Node(0)
        dummy2 = Node(0)
        prev1 = dummy1
        prev2 = dummy2
        current = self.__head
        while current:
            next_node = current.next
            current.next = current.prev = None
            if current.value < x:
                prev1.next = current
                current.prev = prev1
                prev1 = current
            else:
                prev2.next = current
                current.prev = prev2
                prev2 = current
            current = next_node
        prev1.next = dummy2.next
        if dummy2.next:
            dummy2.next.prev = prev1
        self.__head = dummy1.next
        if self.__head:
            self.__head.prev = None
        self.__tail = prev2

    def reverse_between(self, start, end):
        """Reverse sublist from index start to end (exclusive)"""
        if self.__length <= 1 or start == end:
            return
        dummy = Node(0)
        dummy.next = self.__head
        self.__head.prev = dummy
        prev = dummy
        for _ in range(start):
            prev = prev.next
        current = prev.next
        for _ in range(end - start):
            move = current.next
            current.next = move.next
            if move.next:
                move.next.prev = current
            move.next = prev.next
            prev.next.prev = move
            prev.next = move
            move.prev = prev
        self.__head = dummy.next
        self.__head.prev = None

    def swap_pairs(self):
        """Swap adjacent node values in pairs"""
        current = self.__head
        while current and current.next:
            current.value, current.next.value = current.next.value, current.value
            current = current.next.next

    def find_middle_node(self):
        """Return the middle node"""
        slow = fast = self.__head
        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next
        return slow

    def has_loop(self):
        """Check if the list has a loop"""
        slow = fast = self.__head
        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next
            if slow == fast:
                return True
        return False

    def find_kth_from_end(self, k):
        """Find k-th node from the end"""
        slow = fast = self.__head
        for _ in range(k):
            if fast is None:
                return None
            fast = fast.next
        while fast:
            slow = slow.next
            fast = fast.next
        return slow

    def remove_duplicates(self):
        """Remove duplicate values in the list"""
        seen = set()
        current = self.__head
        while current:
            if current.value in seen:
                next_node = current.next
                if current.prev:
                    current.prev.next = current.next
                if current.next:
                    current.next.prev = current.prev
                if current == self.__tail:
                    self.__tail = current.prev
                if current == self.__head:
                    self.__head = current.next
                self.__length -= 1
                current = next_node
            else:
                seen.add(current.value)
                current = current.next

    def binary_to_decimal(self):
        """Convert binary representation to decimal"""
        decimal = 0
        current = self.__head
        while current:
            decimal = decimal * 2 + current.value
            current = current.next
        return decimal