

def median(array: list):
    array_length = len(array)
    if array_length:
        half_index = int(array_length / 2)
        _sort_array(array)
        if array_length % 2 == 0:
            return array[half_index-1:half_index+1]
        else:
            return [array[half_index]]
    else:
        return


def _sort_array(array: list):
    unsorted_array_length = len(array) - 1
    is_sorted = False

    while not is_sorted:
        is_sorted = True
        for i in range(unsorted_array_length):
            if array[i] > array[i + 1]:
                is_sorted = False
                array[i], array[i + 1] = array[i + 1], array[i]



