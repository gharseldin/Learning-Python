def insert_element_at_position(nums, element, position):
    """
    Args:
     nums(list_int32)
     element(int32)
     position(int32)
    Returns:
     list_int32
    """
    # Write your code here.
    for i in range(len(nums) - 1, position - 2, -1):
        nums[i] = nums[i - 1]

    nums[position - 1] = element

    return nums
