def binary_search(lst, target):
    #base case
    if len(lst) == 0: #if the list is empty, return False
        return False
    mid = len(lst) // 2 #find the middle element of the list
    if lst[mid] == target: #if the middle element is the target, return True
        return True
    #recursive case
  
    elif lst[mid] < target: #if the middle element is less than the target, search the right half of the list
        return binary_search(lst[mid + 1:len(lst)], target) #because the list is sorted, we can assume that the right half of the list is sorted as well
    elif lst[mid] > target: #if the middle element is greater than the target, search the left half of the list
        return binary_search(lst[:mid], target) #because the list is sorted, we can assume that the left half of the list is sorted as well
    
print(binary_search([1,2,3,4,5,6,7,8,9,10], 11))