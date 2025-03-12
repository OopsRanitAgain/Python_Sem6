#merge.py

def merge_sort(data):
    subarray(data,0,len(data)-1)

def subarray(data,low,high):
    if(high - low) > 0:
        m1 = (low+high)//2
        m2 = m1 + 1
        subarray(data,low,high)
        subarray(data,m2,high)
        merge_array(data,low,m1,m2,high)

def merge_array(data,low,m1,m2,high):
    l_index = low
    r_index = m2
    c_index = low
    merged = [0]*len(data)
    while l_index <= m1 and r_index <= high:
        if data[l_index] < data[r_index]:
            merged[c_index] = data[l_index]
            l_index += 1
        else:
            merged[c_index] = data[r_index]
            r_index += 1
        c_index += 1
    if l_index <= m1+1:
        merged[c_index:high+1] = data[r_index:high+1]
    else:
        merged[c_index:high+1] = data[l_index:m1+1]
    data[low:high+1] = merged[low:high+1]