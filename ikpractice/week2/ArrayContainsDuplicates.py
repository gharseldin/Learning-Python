def check_if_array_contains_duplicate(nums):
    distinct_elements_set = set()
    for num in nums:
        distinct_elements_set.add(num)
    if len(nums) == len(distinct_elements_set):
        return False
    else:
        return True