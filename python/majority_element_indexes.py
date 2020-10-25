from collections import defaultdict
from typing import Dict, List


def majority_element_indexes(elements: List[int]) -> List[int]:
    '''
    Return a list of the indexes of the majority elements.
    >>> majority_element_indexes([1, 1, 2])
    [0, 1]
    >>> majority_element_indexes([1, 2])
    []
    >>> majority_element_indexes([])
    []
    '''
    ret = []
    size = len(elements) // 2
    d: Dict[int, List[int]] = dict()
    for i, e in enumerate(elements):
        d.setdefault(e, []).append(i)

    for k in d:
        if len(d[k]) > size:
            ret.extend(d[k])
            break

    return ret
