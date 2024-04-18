def get_intersection_with_maintained_frequency(a, b):
    """
    Args:
     a(list_int32)
     b(list_int32)
    Returns:
     list_int32
    """
    # Write your code here.
    intersection = []
    negative_numbers = [0] * 1000001
    positive_numbers = [0] * 1000001
    for number in a:
        if number < 0:
            num = number * -1
            negative_numbers[num] += 1
        else:
            positive_numbers[number] += 1

    for number in b:
        if number < 0:
            num = number * -1
            if negative_numbers[num] > 0:
                intersection.append(number)
                negative_numbers[num] -= 1
        else:
            if positive_numbers[number] > 0:
                intersection.append(number)
                positive_numbers[number] -= 1

    return intersection
