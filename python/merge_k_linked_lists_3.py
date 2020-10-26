from typing import List
from queue import PriorityQueue


class Link:
    def __init__(self, val, next=None):
        self.val = val
        self.next = next

    def __str__(self):
        if not self.next:
            return f"Link({self.val})"
        else:
            return f"Link({self.val}, {self.next})"


def merge_k_linked_lists(linked_lists: List[Link]):
    """
    Merge k sorted linked lists into on sorted linked list.
    >>> print(merge_k_linked_lists([
    ...     Link(1, Link(2)), 
    ...     Link(3, Link(4))
    ...     ]))
    Link(1, Link(2, Link(3, Link(4))))
    >>> print(merge_k_linked_lists([
    ...     Link(1, Link(2)), 
    ...     Link(2, Link(4)), 
    ...     Link(3, Link(3))
    ...     ]))
    Link(1, Link(2, Link(2, Link(3, Link(3, Link(4))))))
    >>> print(merge_k_linked_lists([
    ...     Link(1, Link(2)), 
    ...     Link(2, Link(4)), 
    ...     Link(3, Link(3, Link(5)))
    ...     ]))
    Link(1, Link(2, Link(2, Link(3, Link(3, Link(4, Link(5)))))))
    >>> print(merge_k_linked_lists([
    ...     Link(1, Link(2)) 
    ...     ]))
    Link(1, Link(2))
    """
    pq = PriorityQueue()
    for index, link in enumerate(linked_lists):
        pq.put((link.val, index, link.next))
    start = Link(0)
    end = start
    while not pq.empty():
        val, index, next_link = pq.get()
        end.next = Link(val)
        end = end.next
        if next_link:
            pq.put((next_link.val, index, next_link.next))
    return start.next
