def get_pivot_index(numbers):
    """
    Args:
     numbers(list_int32)
    Returns:
     int32
    """
    # Write your code here.
    for i in range(len(numbers)):
        sum_left = summation(numbers, 0, i)
        sum_right = summation(numbers, i + 1, len(numbers))
        if sum_left == sum_right:
            return i

    return -1


def summation(nums: [], start: int, end: int) -> int:
    result = 0
    for num in nums[start:end:1]:
        result += num
    return result
