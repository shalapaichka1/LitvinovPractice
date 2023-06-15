def sort_array(source_array):
    arr = sorted([i for i in source_array if i % 2 != 0])
    for i,el in enumerate(source_array):
        if el % 2 != 0:
            source_array[i] = arr[0]
            arr.remove(arr[0])
    return source_array
