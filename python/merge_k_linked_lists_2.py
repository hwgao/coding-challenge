from typing import List


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
    front_vals = {i: l for i, l in enumerate(linked_lists) if l}
    result = Link(0)
    end = result
    while len(front_vals):
        k = min(front_vals, key=lambda k: front_vals.get(k).val)
        end.next = Link(front_vals[k].val)
        end = end.next
        if front_vals[k].next:
            front_vals[k] = front_vals[k].next
        else:
            del front_vals[k]
    return result.next
