"""
Data Structures and Algorithms in Python
Beginner-friendly project for VS Code.
Run: python main.py
"""

from collections import deque


def array_example():
    numbers = [10, 20, 30, 40, 50]
    print("\n--- ARRAY ---")
    print("Numbers:", numbers)
    print("First number:", numbers[0])
    numbers.append(60)
    print("After adding 60:", numbers)


def stack_example():
    stack = []
    stack.append("Book 1")
    stack.append("Book 2")
    stack.append("Book 3")

    print("\n--- STACK (Last In, First Out) ---")
    print("Stack:", stack)
    print("Removed:", stack.pop())
    print("Remaining:", stack)


def queue_example():
    queue = deque()
    queue.append("Person 1")
    queue.append("Person 2")
    queue.append("Person 3")

    print("\n--- QUEUE (First In, First Out) ---")
    print("Queue:", list(queue))
    print("Served:", queue.popleft())
    print("Remaining:", list(queue))


def linear_search(numbers, target):
    """Return the index of target, or -1 if it is not found."""
    for index, number in enumerate(numbers):
        if number == target:
            return index
    return -1


def binary_search(numbers, target):
    """Search a sorted list and return the target's index, or -1."""
    left = 0
    right = len(numbers) - 1

    while left <= right:
        middle = (left + right) // 2

        if numbers[middle] == target:
            return middle
        if numbers[middle] < target:
            left = middle + 1
        else:
            right = middle - 1

    return -1


def bubble_sort(numbers):
    """Return a sorted copy of the input list."""
    result = numbers.copy()
    size = len(result)

    for i in range(size):
        swapped = False
        for j in range(0, size - i - 1):
            if result[j] > result[j + 1]:
                result[j], result[j + 1] = result[j + 1], result[j]
                swapped = True
        if not swapped:
            break

    return result


class Node:
    """One item in a linked list."""

    def __init__(self, data):
        self.data = data
        self.next = None


class LinkedList:
    """A simple singly linked list."""

    def __init__(self):
        self.head = None

    def add(self, data):
        new_node = Node(data)

        if self.head is None:
            self.head = new_node
            return

        current = self.head
        while current.next is not None:
            current = current.next
        current.next = new_node

    def display(self):
        current = self.head
        while current is not None:
            print(current.data, end=" -> ")
            current = current.next
        print("None")


def main():
    print("=" * 44)
    print(" DATA STRUCTURES AND ALGORITHMS IN PYTHON")
    print("=" * 44)

    array_example()
    stack_example()
    queue_example()

    numbers = [40, 10, 30, 20, 50]
    print("\n--- SEARCHING AND SORTING ---")
    print("Original numbers:", numbers)
    print("Linear search for 30 (index):", linear_search(numbers, 30))

    sorted_numbers = bubble_sort(numbers)
    print("Sorted numbers:", sorted_numbers)
    print("Binary search for 30 (index):", binary_search(sorted_numbers, 30))

    print("\n--- LINKED LIST ---")
    linked_list = LinkedList()
    for value in (10, 20, 30):
        linked_list.add(value)
    linked_list.display()

    print("\nProgram finished successfully.")


if __name__ == "__main__":
    main()
