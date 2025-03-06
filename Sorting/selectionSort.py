def selectionSort(arr):
    n = len(arr)
    for i in range(n):
        min_index = i
        for j in range(i+1, n):
            if arr[j] < arr[min_index]:
                min_index = j
        arr[i], arr[min_index] = arr[min_index], arr[i]

    return arr

def main():
    data = [64, 25, 12, 22, 11]
    print("Unsorted array:", data)
    
    sorted_data = selectionSort(data)
    print("Sorted array:", sorted_data)

if __name__ == '__main__':
    main()
