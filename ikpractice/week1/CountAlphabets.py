def count_alphabets(s):
    """
    Args:
     s(str)
    Returns:
     int32
    """
    # Write your code here.
    count = 0
    for letter in s:
        if letter.isalpha():
            count += 1
    return count
