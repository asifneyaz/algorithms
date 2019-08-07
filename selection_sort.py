def smallest_element(array):
    smallest = array[0]
    smallest_index = 0
    for i in range(1,len(array) - 1):
        if array[i] < smallest:
            smallest = array[i]
            smallest_index = i
    return smallest_index

def selection_sort(array):
    sort_array = []
    for j in range (0, len(array)):
        smallest = smallest_element(array)
        sort_array.append(array.pop(smallest))
    return sort_array

print(selection_sort([5, 1, 2, 9]))
            
