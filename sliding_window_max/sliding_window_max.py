'''
Input: a List of integers as well as an integer `k` representing the size of the sliding window
Returns: a List of integers
'''

## Plan ##
# loop thru nums arr
# # find way to wrap items in arr == k
# # in that arr find largest number


def sliding_window_max(nums, k):
    # loop thru the arr using k as our end point
    result = []
    for i in range(0, len(nums) - k + 1):
        # max nums varable needed
        max_values = nums[i]
        # loop through arr again tracking the largest element
        for j in range(0, k):
            if nums[i + j] > max_values:
                max_values = nums[i+j]
        result.append(max_values)
        # print(max_values)
    return result
    # pass


arr1 = [1, 2, 3, 2, 4, 1, 5, 6, 1]
k1 = 3
print(sliding_window_max(arr1, k1))

# if __name__ == '__main__':
#     # Use the main function here to test out your implementation
#     arr = [1, 3, -1, -3, 5, 3, 6, 7]
#     k = 3

#     print(f"Output of sliding_window_max function is: {sliding_window_max(arr, k)}")
