"""
Author: Or Cohen
Date: 23/04/24
"""
def deep_sorted(x):
    """
    >>> deep_sorted({"a": 5, "c": 6, "b": [1, 3, 2, 4]})
    {'a': 5, 'b': [1, 2, 3, 4], 'c': 6}
    >>> deep_sorted({"a": (1, 3, 2), "d": {"c": 4, "b": 5}, "c": [1,3,2], "b": 4})
    {'a': (1, 2, 3), 'b': 4, 'c': [1, 2, 3], 'd': {'b': 5, 'c': 4}}
    >>> deep_sorted([2,1,'ab'])
    [1, 2, 'ab']
    """
    if isinstance(x, dict):
        # sort dictionary by key and recursively apply deep_sorted to values
        return {k: deep_sorted(v) for k, v in sorted(x.items())}
    elif isinstance(x, (list, tuple, set)):
        # recursively apply deep_sorted to elements, then sort them
        sorted_x = sorted((deep_sorted(v) for v in x), key=lambda v: str(v))
        # return the sorted elements and converting back to the original type
        if isinstance(x, tuple):
            return tuple(sorted_x)
        elif isinstance(x, set):
            return set(sorted_x)
        return sorted_x
    else:        
        return x

if __name__ == '__main__':
    import doctest
    doctest.testmod()
    x=eval(input())
    print(deep_sorted((x)))