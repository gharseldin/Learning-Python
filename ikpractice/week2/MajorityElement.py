def majority_element(nums):
    counter_map = {}
    for num in nums:
        if num in counter_map:
            count = counter_map[num]
            counter_map[num] = count + 1
        else:
            counter_map[num] = 1
    max_pair = [0, 0]
    for key in counter_map.keys():
        if counter_map[key] > max_pair[1]:
            max_pair = [key, counter_map[key]]

    return max_pair[0]
