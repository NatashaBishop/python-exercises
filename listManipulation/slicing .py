# syntax: collection[start:stop:step]  
# collection = list, string, array, and so on
# start = where the slicing  tarts
# stop = where the operation stops
# step = the sequence of iterating through the elements. 2 means every second element, 3 - every third
list1 = [2,4,6,8,10,12]
print(list1[2:])
# [6, 8, 10, 12]
list1 = [2,4,6,8,10,12]
print(number_list[:2]) #starts at zero index - up t two, index 2 is not included, from start to up to index 2
# [2, 4]
list1 = [2,4,6,8,10,12]
print(number_list[::2]) # all the list with step 2
# [2, 6, 10]
