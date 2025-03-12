def merge_sort(data):
    subarray(data, 0, len(data) - 1)

def subarray(data, low, high):
    if low < high:
        m1 = (low + high) // 2
        m2 = m1 + 1
        subarray(data, low, m1)  # Recursively sort the left half
        subarray(data, m2, high)  # Recursively sort the right half
        merge_array(data, low, m1, m2, high)  # Merge the two sorted halves

def merge_array(data, low, m1, m2, high):
    l_index = low
    r_index = m2
    c_index = low
    merged = [0] * (high - low + 1)  # Size of the merged array
    while l_index <= m1 and r_index <= high:
        if data[l_index] < data[r_index]:
            merged[c_index - low] = data[l_index]
            l_index += 1
        else:
            merged[c_index - low] = data[r_index]
            r_index += 1
        c_index += 1

    if l_index <= m1:
        merged[c_index - low:] = data[l_index:m1 + 1]
    else:
        merged[c_index - low:] = data[r_index:high + 1]

    data[low:high + 1] = merged

def main():
    import numpy as np
    data = np.random.randint(11, 111, 10)
    print(f'Unsorted data: {data}')
    merge_sort(data)
    print(f'Sorted data: {data}')

if __name__ == '__main__':
    main()
