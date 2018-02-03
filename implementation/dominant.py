

def dominant(array: list):
    elements_dict = {}
    most_common_element, highest_count, index = 0, 0, 0
    for idx, element in enumerate(array):
        counter = elements_dict.get(element, 0)
        counter += 1
        if counter >= highest_count:
            most_common_element, highest_count, index = element, counter, idx
        elements_dict[element] = counter

    return most_common_element, highest_count, index
