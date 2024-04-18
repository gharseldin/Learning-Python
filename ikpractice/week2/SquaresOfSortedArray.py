def generate_sorted_array_of_squares(numbers):
    size = len(numbers)

    s = 0
    e = size - 1

    result = [None] * size
    result_end = size - 1
    while s <= e:
        if abs(numbers[s]) > abs(numbers[e]):
            result[result_end] = numbers[s] ** 2
            s += 1
        else:
            result[result_end] = numbers[e] ** 2
            e -= 1
        result_end -= 1
    return result
