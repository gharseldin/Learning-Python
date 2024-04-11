def length_of_last_word(sentence):
    """
    Args:
     sentence(str)
    Returns:
     int32
    """
    # Write your code here.
    stripped_sentence = sentence.strip()
    words = stripped_sentence.split(' ')
    last_word_index = len(words) - 1
    last_word = words[last_word_index]
    last_word_length = len(last_word)
    return last_word_length
