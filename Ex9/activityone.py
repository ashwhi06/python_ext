def binary_search(lst, target):
    #base case
    if len(lst) == 0:
        return False
    mid = len(lst) // 2
    if lst[mid] == target:
        return True
    #recursive case
  
    elif lst[mid] < target:
        return binary_search(lst[mid + 1:len(lst)], target)
    elif lst[mid] > target:
        return binary_search(lst[:mid], target)