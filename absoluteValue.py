x = -2
absolutValueOFx = abs(x) #prints: 2
#calculate absolute value of elements in the list
y = [22,-4, -42] 

print([abs(i) for i in y]) #loop through list
#output: [22, 4, 42]

import numpy as np
y = np.array(y)
print(np.abs(y))
#output: [22, 4, 42]

