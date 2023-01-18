def print_items(item_list):
    """
    >>> print_items([1,2,3]) #doctest: +NORMALIZE_WHITESPACE
    <BLANKLINE>
     1
    <BLANKLINE>
     2
    <BLANKLINE>
     3
    """
    for item in item_list:
        print("\n", item)
