def linearSearch(data,key):
    location = -1
    for index,value in enumerate(data):
        if value == key:
            location = index
            break;
    return location


import numpy as np

def main():
    data = np.random.randint(1,101,20)
    print(data)

    key = int(input('Enter a number You want to locate in the array'))
    loc = linearSearch(data,key)

    if(loc == -1):
        print(f"{key} NOT found")
    else:
        print(f"{key} found at {loc}")

if __name__ == '__main__':
    main()