def find_maximum_sum_subarray(numbers):
    max_sum = [numbers[0]]
    for i in range(1, len(numbers)):
        max_sum.append(max_sum[i - 1] + numbers[i])

    max_value = numbers[0]

    for i, num in enumerate(max_sum):
        if num > max_value:
            max_value = num
    for i in range(len(max_sum)):
        for j in range(i + 1, len(max_sum)):
            total = max_sum[j] - max_sum[i]
            if total > max_value:
                max_value = total
    return max_value
