def reverse_array(nums):
    """
    Args:
     nums(list_int32)
    Returns:
     list_int32
    """
    # Write your code here.

    nums_reversed = []
    for num in nums[::-1]:
        nums_reversed.append(num)
    return nums_reversed
