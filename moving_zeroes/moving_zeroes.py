'''
Input: a List of integers
Returns: a List of integers
'''


def moving_zeroes(arr):
    # Your code here
    # loop thru the arr
    for i in range(0, len(arr)):
        # print(arr[i])
        # loop thru same arr starting at index i + 1

        for x in range(i + 1, len(arr)):
            if arr[i] == 0 and arr[x] is not None:
                print('arr', arr)
                arr[i], arr[x] = arr[x], arr[i]

    return arr


# print(moving_zeroes([0, 3, 1, 0, -2]))


if __name__ == '__main__':
    # Use the main function here to test out your implementation
    arr = [0, 3, 1, 0, -2]

    print(f"The resulting of moving_zeroes is: {moving_zeroes(arr)}")
