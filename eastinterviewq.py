from collections import defaultdict
from collections import Counter
import enum
from tkinter import W
'''
Return a list of the indexs of the majority element.
Majority element is the element that appears more than
floor(n/2) times.
If there is no majority element, return []
>>> majority_element_indexes([1,1,2])
[0,1]
'''

def not_my_func(lst):
    if lst == []:
        return []
    vid_list = lst 
    count = Counter(vid_list)
    top_elems = sorted( # sorted always takes O(nlog n), the key doesn't affect it
        count.keys(),
        key= lambda k: count[k], reverse=True
    )
    maj_elem = top_elems[0]
    #there exists a majority element
    if count[maj_elem] > len(vid_list) // 2:
        return [ # O(n)
            i for i,elem in enumerate(vid_list) if elem == maj_elem
        ]
    else:
        return []

def better_fun(lst):
    if lst == []:
        return []
    count = Counter(lst)
    # This is the highest frequency that an item occurs
    max_count = max(count.values())
    maj_elem = [
        elem for elem,counter in count.items() if counter == max_count
    ][0]
    if count[maj_elem] > len(lst) //2:
        return [
            i for i,val in enumerate(lst) if val == maj_elem
        ]
    else:
        return []

def majority_element_indexes(lst):
    set_lst = set(lst)
    dict_of_lst = {}
    positions = []
    for val in lst:
        dict_of_lst.setdefault(val, 0) 
    for val in set_lst:
        dict_of_lst[val] = lst.count(val)
    most_freq = sorted(dict_of_lst, key = lambda k:dict_of_lst[k], reverse=True)[0]
    for i, val in enumerate(lst):
        if val == most_freq:
            positions.append(i)
    print(positions)



my_list = [6,1,1,1,2,1,5,5,1,6,6,6,6,6,6,6,6]
majority_element_indexes(my_list)
print(not_my_func(my_list))
print(better_fun(my_list))