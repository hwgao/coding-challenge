class Link:
    def __init__(self, val, next=None):
        self.val = val
        self.next = next

    def __str__(self):
        if not self.next:
            return f"Link({self.val})"
        else:
            return f"Link({self.val}, {self.next})"


def merge_k_linked_lists(linked_lists):
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
    ...     Link(1, Link(2)) 
    ...     ]))
    Link(1, Link(2))
    >>> print(merge_k_linked_lists([]))
    None
    >>> print(merge_k_linked_lists(None))
    None
    """

    if not linked_lists:
        return None

    result = linked_lists[0]

    def _helper(item: Link):
        nonlocal result
        if not result:
            result = item
        else:
            link = result
            while True:
                if link.next:
                    if link.next.val >= item.val:
                        temp = link.next
                        link.next = item
                        item.next = temp
                        break
                else:
                    link.next = item
                    break
                link = link.next

    for link in linked_lists[1:]:
        while link:
            _helper(Link(link.val))
            if not link.next:
                break
            link = link.next

    return result
