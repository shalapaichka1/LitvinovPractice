def sort_array(source_array):
    numbers = []
    indexes = []
    for i, el in enumerate(source_array):
        if el % 2 == 1:
            numbers.append(el)
            indexes.append(i)
    numbers.sort()
    for i, index in enumerate(indexes):
        source_array[index] = numbers[i]
    return source_array