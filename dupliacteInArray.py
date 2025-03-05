def duplicate(data):
    for i in range(len(data)):
        for j in range(i+1,len(data)):
            if data[i]==data[j]:
                return f'Data has a Duplicate'
    return f'Data does not have duplicate'

import numpy as np

data = np.random.randint(1,50,10)
print(data)

print(duplicate(data))
