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