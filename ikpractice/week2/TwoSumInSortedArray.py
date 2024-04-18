def pair_sum_sorted_array(numbers, target):
    start = 0
    end = len(numbers) - 1

    while start != end:
        total = numbers[start] + numbers[end]
        if total == target:
            return [start, end]
        elif total > target:
            end -= 1
        else:
            start += 1

    return [-1, -1]