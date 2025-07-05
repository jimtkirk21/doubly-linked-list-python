# Doubly Linked List in Python

A complete, easy-to-understand implementation of a **Doubly Linked List** in Python, with OOP principles, encapsulation, private attributes, and practical examples for each method.

---

## Project Structure

```plaintext
.
├── doubly_linked_list.py   # Core data structure
├── test_dll.py             # Usage examples & tests
├── README.md               # This file
└── LICENSE                 # Open source license
🚀 Features
✔️ Node Class
Each node stores:

value: The data.

next: Pointer to the next node.

prev: Pointer to the previous node.

DoublyLinkedList Class
Below is a breakdown of all available methods, what they do, and how to use them.

Methods & Examples

| #  | Method                | Purpose                             |
| -- | --------------------- | ----------------------------------- |
| 1  | `append()`            | Add a node to the end               |
| 2  | `prepend()`           | Add a node to the beginning         |
| 3  | `pop()`               | Remove the last node                |
| 4  | `pop_first()`         | Remove the first node               |
| 5  | `insert()`            | Insert a node at an index           |
| 6  | `remove()`            | Remove node at index                |
| 7  | `get()`               | Get node by index                   |
| 8  | `set_value()`         | Update node value by index          |
| 9  | `reverse()`           | Reverse entire list                 |
| 10 | `reverse_between()`   | Reverse sublist between two indices |
| 11 | `partition_list()`    | Partition list around a value       |
| 12 | `swap_pairs()`        | Swap every two adjacent nodes       |
| 13 | `is_palindrome()`     | Check if list is a palindrome       |
| 14 | `find_middle_node()`  | Return middle node                  |
| 15 | `find_kth_from_end()` | Return k-th node from end           |
| 16 | `has_loop()`          | Check for cycle/loop                |
| 17 | `remove_duplicates()` | Remove duplicate nodes              |
| 18 | `binary_to_decimal()` | Convert binary to decimal           |
| 19 | `make_empty()`        | Reset list to empty                 |
| 20 | `print_list()`        | Display list nicely                 |

1. append(value)
Add a new node to the end of the list.

dll = DoublyLinkedList(1)
dll.append(2)
dll.append(3)
dll.print_list()  # 1 <-> 2 <-> 3 <-> None

2. prepend(value)
Add a new node to the beginning of the list.

dll = DoublyLinkedList(2)
dll.prepend(1)
dll.print_list()  # 1 <-> 2 <-> None

3. pop()
Remove and return the last node.


dll = DoublyLinkedList(1)
dll.append(2)
node = dll.pop()
print(node.value)  # 2
dll.print_list()   # 1 <-> None

4. pop_first()
Remove and return the first node.

dll = DoublyLinkedList(1)
dll.append(2)
node = dll.pop_first()
print(node.value)  # 1
dll.print_list()   # 2 <-> None
insert(index, value)

5. Insert a node at a specific index.

dll = DoublyLinkedList(1)
dll.append(3)
dll.insert(1, 2)
dll.print_list()  # 1 <-> 2 <-> 3 <-> None

6. remove(index)
Remove and return a node at a specific index.

dll = DoublyLinkedList(1)
dll.append(2)
dll.append(3)
node = dll.remove(1)
print(node.value)  # 2
dll.print_list()   # 1 <-> 3 <-> None

7. get(index)
Get the node at a given index.

dll = DoublyLinkedList(1)
dll.append(2)
dll.append(3)
node = dll.get(2)
print(node.value)  # 3

8. set_value(index, value)
Update the value of the node at a specific index.

dll = DoublyLinkedList(1)
dll.append(2)
dll.set_value(1, 20)
dll.print_list()  # 1 <-> 20 <-> None

9. reverse()
Reverse the entire list in place.

dll = DoublyLinkedList(1)
dll.append(2)
dll.append(3)
dll.reverse()
dll.print_list()  # 3 <-> 2 <-> 1 <-> None

10. reverse_between(start, end)
Reverse a sublist between given start and end indices.

dll = DoublyLinkedList(1)
dll.append(2)
dll.append(3)
dll.append(4)
dll.reverse_between(1, 3)
dll.print_list()  # 1 <-> 3 <-> 2 <-> 4 <-> None

11. partition_list(x)
Rearrange the list so that all nodes with values less than x come before nodes greater or equal to x.

dll = DoublyLinkedList(3)
dll.append(5)
dll.append(8)
dll.append(5)
dll.append(10)
dll.append(2)
dll.append(1)
dll.partition_list(5)
dll.print_list()  # 3 <-> 2 <-> 1 <-> 5 <-> 8 <-> 5 <-> 10 <-> None

12. swap_pairs()
Swap every two adjacent nodes’ values.

dll = DoublyLinkedList(1)
dll.append(2)
dll.append(3)
dll.append(4)
dll.swap_pairs()
dll.print_list()  # 2 <-> 1 <-> 4 <-> 3 <-> None

13. is_palindrome()
Check if the linked list is a palindrome.

dll = DoublyLinkedList(1)
dll.append(2)
dll.append(3)
dll.append(2)
dll.append(1)
print(dll.is_palindrome())  # True

14. find_middle_node()
Find the middle node.

dll = DoublyLinkedList(1)
dll.append(2)
dll.append(3)
dll.append(4)
dll.append(5)
print(dll.find_middle_node().value)  # 3

15. find_kth_from_end(k)
Find the k-th node from the end.

dll = DoublyLinkedList(1)
dll.append(2)
dll.append(3)
dll.append(4)
dll.append(5)
print(dll.find_kth_from_end(2).value)  # 4

16. has_loop()
Detect if the list has a cycle.

dll = DoublyLinkedList(1)
dll.append(2)
dll.append(3)
# Create a loop manually
dll.tail.next = dll.head
print(dll.has_loop())  # True

17. remove_duplicates()
Remove duplicate nodes.

dll = DoublyLinkedList(1)
dll.append(2)
dll.append(1)
dll.append(3)
dll.append(2)
dll.remove_duplicates()
dll.print_list()  # 1 <-> 2 <-> 3 <-> None

18. binary_to_decimal()
Treat the list as a binary number and convert it to decimal.

dll = DoublyLinkedList(1)
dll.append(0)
dll.append(1)
dll.append(1)
print(dll.binary_to_decimal())  # 11 in binary => 11 decimal => 3

## How to Run Tests

R1. Clone this repository:
    ```bash
    git clone https://ghttps://github.com/jimtkirk21/doubly-linked-list-python.git
    cd your-repo-name
    ```

2. Run all tests:
    ```bash
    python3 test_linked_lists.py
    ```

License
This project is licensed under the MIT License — see LICENSE for details.

Contributing
Contributions and pull requests are always welcome. Please open an issue first to discuss what you’d like to change!

Author
Adam Bulenda
GitHub