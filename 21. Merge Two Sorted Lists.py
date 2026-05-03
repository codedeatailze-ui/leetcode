def merge_two_sorted_lists (list_1:int , list_2:int):

    list_2.extend(list_1)
    list_2.sort()
    return list_2
print(merge_two_sorted_lists([5,8,9],[7,4,10]))
