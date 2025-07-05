from doubly_linked_list import DoublyLinkedList
from helpers import print_title, check, check_list

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