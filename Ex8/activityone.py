#Given array of integers, find the minimal possible sum of some of its k consecutive elements using algorithms and data structures

#Solution #1
# def solution(A, K):
#     return sum(sorted(A)[0:K])
# print(solution([1, 3, 1, 2, 4, 3, 4], 2))

# #Solution #2
# def solution(A, K):
#     n = len(A)
#    # k is the number of elements to be considered
#     if n < K:
#         return "Invalid input"

#     min_sum = sum(A[0:K]) # min_sum is the sum of the first K elements
#     curr_sum = min_sum # curr_sum is the sum of the first K elements

#     for i in range(1, n - K + 1): # i is the index of the first element of the subarray
#         curr_sum = curr_sum - A[i - 1] + A[i + K - 1] # curr_sum is the sum of the first K elements
#         min_sum = min(min_sum, curr_sum) # min_sum is the sum of the first K elements
#     return min_sum

# A = [1, 3, 1, 2, 4, 3, 4]
# k = 3
# print("Minimal possible sum of its",k, "consecutive elements:", solution(A, k))

#Solution #3
def solution(input_Arr, k):
    sum = input_Arr[0]
    for i in range(1, k):
        sum += input_Arr[1]
    max_sum = sum
    for i in range(k, len(input_Arr)):
        if i + k > len(input_Arr):
            break
        else:
            sum = sum - input_Arr[i - k] + input_Arr[i]
            max_sum = max(max_sum, sum)
    return max_sum

print(solution([1, 3, 1, 2, 4, 3, 4], 2))
               
            
            
            