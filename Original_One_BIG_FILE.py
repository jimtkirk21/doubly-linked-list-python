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
        """Initialize the linked list with the first node."""
        new_node = Node(value)
        self.head = new_node
        self.tail = new_node
        self.length = 1

    def print_list(self):
        """Print the linked list in a readable format."""
        if self.head is None:
            print("[ empty list ]")
        else:
            values = []
            temp = self.head
            while temp:
                values.append(str(temp.value))
                temp = temp.next
            print(" <-> ".join(values))

    def make_empty(self):
        """Reset the linked list to empty."""
        self.head = None
        self.tail = None
        self.length = 0

    def append(self, value):
        """Add a node to the end of the list."""
        new_node = Node(value)
        if self.length == 0:
            self.head = self.tail = new_node
        else:
            self.tail.next = new_node
            new_node.prev = self.tail
            self.tail = new_node
        self.length += 1
        return True

    def pop(self):
        """Remove and return the last node."""
        if self.length == 0:
            return None
        temp = self.tail
        if self.length == 1:
            self.head = self.tail = None
        else:
            self.tail = temp.prev
            self.tail.next = None
            temp.prev = None
        self.length -= 1
        return temp

    def prepend(self, value):
        """Add a node to the beginning of the list."""
        new_node = Node(value)
        if self.length == 0:
            self.head = self.tail = new_node
        else:
            new_node.next = self.head
            self.head.prev = new_node
            self.head = new_node
        self.length += 1
        return True

    def pop_first(self):
        """Remove and return the first node."""
        if self.length == 0:
            return None
        temp = self.head
        if self.length == 1:
            self.head = self.tail = None
        else:
            self.head = temp.next
            self.head.prev = None
            temp.next = None
        self.length -= 1
        return temp

    def get(self, index):
        """Get the node at a specific index."""
        if index < 0 or index >= self.length:
            return None
        if index < self.length / 2:
            temp = self.head
            for _ in range(index):
                temp = temp.next
        else:
            temp = self.tail
            for _ in range(self.length - 1, index, -1):
                temp = temp.prev
        return temp

    def set_value(self, index, value):
        """Set the value of a node at a specific index."""
        temp = self.get(index)
        if temp:
            temp.value = value
            return True
        return False

    def insert(self, index, value):
        """Insert a node at a specific index."""
        if index < 0 or index > self.length:
            return False
        if index == 0:
            return self.prepend(value)
        if index == self.length:
            return self.append(value)
        new_node = Node(value)
        before = self.get(index - 1)
        after = before.next
        new_node.prev = before
        new_node.next = after
        before.next = new_node
        after.prev = new_node
        self.length += 1
        return True

    def remove(self, index):
        """Remove and return a node at a specific index."""
        if index < 0 or index >= self.length:
            return None
        if index == 0:
            return self.pop_first()
        if index == self.length - 1:
            return self.pop()
        temp = self.get(index)
        temp.prev.next = temp.next
        temp.next.prev = temp.prev
        temp.prev = temp.next = None
        self.length -= 1
        return temp

    def is_palindrome(self):
        """Check if the linked list is a palindrome."""
        if self.length <= 1:
            return True
        left = self.head
        right = self.tail
        for _ in range(self.length // 2):
            if left.value != right.value:
                return False
            left = left.next
            right = right.prev
        return True

    def reverse(self):
        """Reverse the entire linked list in place."""
        temp = self.head
        while temp:
            temp.prev, temp.next = temp.next, temp.prev
            temp = temp.prev
        self.head, self.tail = self.tail, self.head

    def partition_list(self, x):
        """Partition the list around value x."""
        if not self.head:
            return
        dummy1 = Node(0)
        dummy2 = Node(0)
        prev1 = dummy1
        prev2 = dummy2
        current = self.head
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
        self.head = dummy1.next
        if self.head:
            self.head.prev = None
        self.tail = prev2

    def reverse_between(self, start, end):
        """Reverse a portion of the linked list between two indices."""
        if self.length <= 1 or start == end:
            return
        dummy = Node(0)
        dummy.next = self.head
        self.head.prev = dummy
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
        self.head = dummy.next
        self.head.prev = None

    def swap_pairs(self):
        """Swap values of each pair of nodes in the list."""
        current = self.head
        while current and current.next:
            current.value, current.next.value = current.next.value, current.value
            current = current.next.next

    def find_middle_node(self):
        """Return the middle node of the list."""
        fast = slow = self.head
        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next
        return slow

    def has_loop(self):
        """Check if the list contains a loop."""
        fast = slow = self.head
        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next
            if fast == slow:
                return True
        return False

    def find_kth_from_end(self, k):
        """Return the k-th node from the end of the list."""
        slow = fast = self.head
        for _ in range(k):
            if fast is None:
                return None
            fast = fast.next
        while fast:
            slow = slow.next
            fast = fast.next
        return slow

    def remove_duplicates(self):
        """Remove duplicate nodes from the list."""
        seen = set()
        current = self.head
        while current:
            if current.value in seen:
                next_node = current.next
                if current.prev:
                    current.prev.next = current.next
                if current.next:
                    current.next.prev = current.prev
                if current == self.tail:
                    self.tail = current.prev
                if current == self.head:
                    self.head = current.next
                self.length -= 1
                current = next_node
            else:
                seen.add(current.value)
                current = current.next

    def binary_to_decimal(self):
        """Convert binary digits stored in the list to decimal number."""
        decimal = 0
        current = self.head
        while current:
            decimal = decimal * 2 + current.value
            current = current.next
        return decimal


## ------------------------------
# Test helper functions
# ------------------------------

def check(expected, actual, message=""):
    """Check test result and print outcome in a clear format."""
    print(f"--- {message} ---")
    print(f"Expected: {expected}")
    print(f"Returned: {actual}")
    result = "PASS" if expected == actual else "FAIL"
    print(f"Result:   {result}\n")

def check_list(linked_list, expected_list, message=""):
    """Check if linked list values match the expected list."""
    actual = []
    node = linked_list.head
    while node:
        actual.append(node.value)
        node = node.next
    check(expected_list, actual, message)

def print_title(title):
    """Print a clear section title for test cases."""
    print("\n" + "="*len(title))
    print(title)
    print("="*len(title) + "\n")

# ------------------------------
# Example usage and tests
# ------------------------------

print_title("INITIAL DOUBLY LINKED LIST TEST")
dll = DoublyLinkedList(4)
dll.print_list()
check(4, dll.head.value, "Head value")
check(4, dll.tail.value, "Tail value")
check(1, dll.length, "List length")

# --------------------------------------------------

print_title("APPEND TEST")
dll = DoublyLinkedList(1)
dll.append(2)
dll.append(3)
dll.print_list()
check_list(dll, [1, 2, 3], "List after append")

# --------------------------------------------------

print_title("MAKE EMPTY & APPEND TEST")
dll = DoublyLinkedList(1)
dll.make_empty()
dll.print_list()
check(0, dll.length, "List length after make_empty")

dll.append(10)
dll.append(20)
dll.print_list()
check_list(dll, [10, 20], "List after appending to empty")

# --------------------------------------------------

print_title("POP TEST")
dll = DoublyLinkedList(1)
dll.append(2)
dll.append(3)
dll.print_list()

popped = dll.pop()
print(f"Popped value: {popped.value if popped else None}")
dll.print_list()
check_list(dll, [1, 2], "List after pop")

# --------------------------------------------------

print_title("POP ALL TEST")
dll = DoublyLinkedList(5)
dll.append(6)
dll.print_list()

dll.pop()
dll.pop()
dll.print_list()
check_list(dll, [], "List after popping all nodes")

# --------------------------------------------------

print_title("PREPEND TEST")
dll = DoublyLinkedList(2)
dll.append(3)
dll.print_list()

dll.prepend(1)
dll.print_list()
check_list(dll, [1, 2, 3], "List after prepend")

# --------------------------------------------------

print_title("POP FIRST TEST")
dll = DoublyLinkedList(1)
dll.append(2)
dll.append(3)
dll.print_list()

popped_first = dll.pop_first()
print(f"Popped first value: {popped_first.value if popped_first else None}")
dll.print_list()
check_list(dll, [2, 3], "List after pop_first")

# --------------------------------------------------

print_title("GET TEST")
dll = DoublyLinkedList(0)
dll.append(1)
dll.append(2)
dll.append(3)
dll.print_list()
check(1, dll.get(1).value, "Get node at index 1")
check(3, dll.get(3).value, "Get node at index 3")

# --------------------------------------------------

print_title("SET VALUE TEST")
dll = DoublyLinkedList(1)
dll.append(2)
dll.append(3)
dll.print_list()

dll.set_value(1, 99)
dll.print_list()
check_list(dll, [1, 99, 3], "List after set_value")

# --------------------------------------------------

print_title("INSERT TEST")
dll = DoublyLinkedList(1)
dll.append(3)
dll.insert(1, 2)  # Insert in middle
dll.insert(0, 0)  # Insert at head
dll.insert(dll.length, 4)  # Insert at tail
dll.print_list()
check_list(dll, [0, 1, 2, 3, 4], "List after inserts")

# --------------------------------------------------

print_title("REMOVE TEST")
dll = DoublyLinkedList(1)
dll.append(2)
dll.append(3)
dll.append(4)
dll.print_list()

removed = dll.remove(2)
print(f"Removed value: {removed.value if removed else None}")
dll.print_list()
check_list(dll, [1, 2, 4], "List after remove in middle")

# --------------------------------------------------

print_title("IS PALINDROME TEST")
dll = DoublyLinkedList(1)
dll.append(2)
dll.append(3)
dll.append(2)
dll.append(1)
dll.print_list()
check(True, dll.is_palindrome(), "Is palindrome")

dll = DoublyLinkedList(1)
dll.append(2)
dll.append(3)
dll.print_list()
check(False, dll.is_palindrome(), "Is not palindrome")

# --------------------------------------------------

print_title("REVERSE TEST")
dll = DoublyLinkedList(1)
dll.append(2)
dll.append(3)
dll.append(4)
dll.print_list()
dll.reverse()
dll.print_list()
check_list(dll, [4, 3, 2, 1], "List after reverse")

# --------------------------------------------------

print_title("PARTITION LIST TEST")
dll = DoublyLinkedList(3)
dll.append(8)
dll.append(5)
dll.append(10)
dll.append(2)
dll.append(1)
dll.print_list()
dll.partition_list(5)
dll.print_list()
# Expected partitioned order may vary depending on implementation

# --------------------------------------------------

print_title("REVERSE BETWEEN TEST")
dll = DoublyLinkedList(1)
dll.append(2)
dll.append(3)
dll.append(4)
dll.append(5)
dll.print_list()
dll.reverse_between(1, 4)
dll.print_list()
# Expected: [1, 4, 3, 2, 5] if reversed between index 1 and 4

# --------------------------------------------------

print_title("SWAP PAIRS TEST")
dll = DoublyLinkedList(1)
dll.append(2)
dll.append(3)
dll.append(4)
dll.print_list()
dll.swap_pairs()
dll.print_list()
check_list(dll, [2, 1, 4, 3], "List after swap_pairs")

# --------------------------------------------------

print_title("FIND MIDDLE NODE TEST")
dll = DoublyLinkedList(1)
dll.append(2)
dll.append(3)
dll.append(4)
dll.append(5)
dll.print_list()
middle = dll.find_middle_node()
print(f"Middle node value: {middle.value if middle else None}")

# --------------------------------------------------

print_title("HAS LOOP TEST")
dll = DoublyLinkedList(1)
dll.append(2)
dll.append(3)
dll.tail.next = dll.head  # Manually create loop
print(f"Has loop: {dll.has_loop()}")

dll = DoublyLinkedList(1)
dll.append(2)
dll.append(3)
print(f"Has loop: {dll.has_loop()}")

# --------------------------------------------------

print_title("FIND KTH FROM END TEST")
dll = DoublyLinkedList(1)
dll.append(2)
dll.append(3)
dll.append(4)
dll.append(5)
dll.print_list()
kth = dll.find_kth_from_end(2)
print(f"2nd node from end: {kth.value if kth else None}")

# --------------------------------------------------

print_title("REMOVE DUPLICATES TEST")
dll = DoublyLinkedList(1)
dll.append(2)
dll.append(1)
dll.append(3)
dll.append(2)
dll.print_list()
dll.remove_duplicates()
dll.print_list()
check_list(dll, [1, 2, 3], "List after remove_duplicates")

# --------------------------------------------------

print_title("BINARY TO DECIMAL TEST")
dll = DoublyLinkedList(1)
dll.append(1)
dll.append(0)
dll.print_list()
decimal = dll.binary_to_decimal()
check(6, decimal, "Binary 110 to Decimal")