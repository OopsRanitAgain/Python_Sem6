import numpy as np

def remainingArray(data,low,high):
    s ='   '*low
    return s+' '.join(str(v) for v in data[low:high+1])

def binarySearch(data, key):
    low = 0
    high = len(data) - 1
    location = -1
    while low <= high and location == -1:
        mid = (low + high) // 2
        if key == data[mid]:
            location = mid
        elif key < data[mid]:
            high = mid - 1
        else:
            low = mid + 1
        print(remainingArray(data,low,high))
    return location

def main():
    data = np.random.randint(11, 101, 10)
    print(f'Unsorted Data: {data}')
    
    data.sort()
    print(f'Sorted Data: {data}')
    
    key = int(input('Enter a Key You want to locate (-1 to quit): '))
    
    while key != -1:
        loc = binarySearch(data, key)
        if loc == -1:
            print(f'Key {key} NOT found')
        else:
            print(f'Key is found at location: {loc}')
        key = int(input('Enter a Key You want to locate (-1 to quit): '))

if __name__ == '__main__':
    main()
