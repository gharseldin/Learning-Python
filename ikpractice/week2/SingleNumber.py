def single_number(arr):
    margin = set()
    for num in arr:
        if num in margin:
            margin.remove(num)
        else:
            margin.add(num)

    for item in margin:
        return item
    return 0
