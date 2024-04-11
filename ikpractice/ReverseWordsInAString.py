def reverse_words(s):
    """
    Args:
     s(str)
    Returns:
     str
    """
    # Write your code here.
    words = s.split(' ')
    reversed_words = []
    for word in words[::-1]:
        reversed_words.append(word)
    result = ""
    for word in reversed_words:
        result += " " + word

    return result.strip()
