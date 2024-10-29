class ListNode:
    def __init__(self, data=0, next=None):
        self.data = data
        self.next = next

    def __str__(self):
        # Helper function to print the linked list
        result = []
        node = self
        while node:
            result.append(str(node.data))
            node = node.next
        return "->".join(result)


class Solution:
    def quickSort(self, head):
        """
        Sorts a linked list using the quicksort algorithm.

        :param head: ListNode - Head of the linked list to sort
        :return: ListNode - Head of the sorted linked list
        """
        if not head or not head.next:
            return head  

        def partition(start, end):
            # Partitioning function to rearrange nodes based on pivot
            pivot, prev = start, None
            curr = start
            tail = pivot

            while curr != end:
                if curr.data < pivot.data:
                    # Move nodes with smaller values to the front
                    if prev:
                        prev.next = curr.next
                    curr.next = start
                    start = curr
                    curr = prev.next if prev else tail.next
                else:
                    prev = curr
                    curr = curr.next
            return pivot, start, tail

        def quickSortRecur(start, end):
            if start == end or not start:
                return start

            pivot, left_head, pivot_tail = partition(start, end)
            left_head = quickSortRecur(left_head, pivot)
            pivot_tail.next = quickSortRecur(pivot.next, end)
            return left_head

        return quickSortRecur(head, None)


def create_linked_list(arr):
    # Helper function to create a linked list from a list of values
    if not arr:
        return None
    head = ListNode(arr[0])
    current = head
    for value in arr[1:]:
        current.next = ListNode(value)
        current = current.next
    return head


def main():
    # Sample test cases
    test_cases = [
        [1, 6, 2],
        [1, 9, 3, 8]
    ]

    # Initialize Solution object
    solution = Solution()

    # Run each test case
    for i, arr in enumerate(test_cases, 1):
        print(f"Test Case {i}: Input Linked List: {'->'.join(map(str, arr))}")
        head = create_linked_list(arr)
        sorted_head = solution.quickSort(head)
        print(f"Output Linked List: {sorted_head}\n")


if __name__ == "__main__":
    main()
