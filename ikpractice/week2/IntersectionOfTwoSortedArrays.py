def get_intersection(numbers1, numbers2):
    i1 = 0
    i2 = 0

    result = set()
    while i1 < len(numbers1) and i2 < len(numbers2):
        if numbers1[i1] == numbers2[i2]:
            result.add(numbers1[i1])
            i1 += 1
            i2 += 1
        elif numbers1[i1] > numbers2[i2]:
            i2 += 1
        else:
            i1 += 1
    if len(result) == 0:
        return [-1]
    else:
        result_list = []
        for item in result:
            result_list.append(item)
        result_list.sort()
        return result_list