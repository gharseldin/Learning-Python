def find_first_occurrence(s, to_find):
    """
    Args:
     s(str)
     to_find(char)
    Returns:
     int32
    """
    # Write your code here.
    for i in range(len(s)):
        if s[i] == to_find:
            return i
    return -1
