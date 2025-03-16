x = -2
absolutValueOFx = abs(x) #prints: 2
#calculate absolute value of elements in the list
y = [22,-4, -42] 

print([abs(i) for i in y]) #loop through list
#output: [22, 4, 42]

import numpy as np #the most efficient performance wize
z = np.array(y)
print(np.abs(z))
#output: [22, 4, 42]

# Using map() to apply abs() to each element of map and converting it back 2 list
a = list(map(abs, y))
print(a)
#output: [22, 4, 42]
