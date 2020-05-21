## PLAN ##
# create a helper fn to sort the arr in order to make accurate comparisons
# test rounds https://singlenumber.ben--griffin.repl.run


def single_number(arr):
    # create a variable to hold the index that only appears once
    # start at index 0 of our arr and only change inside our for loop
    appears_once = arr[0]

    # loop through the arr starting at index 0
    for i in range(1, len(arr)):
        # update appears once using the `^ XOR`	operator which, sets each bit to 1 if only one of two bits is 1
        appears_once = appears_once ^ arr[i]

    return appears_once


if __name__ == '__main__':
    # Use the main function to test your implementation
    arr = [1, 1, 4, 4, 5, 5, 3, 3, 9, 0, 0]

    print(f"The odd-number-out is {single_number(arr)}")

"""
def quick_sort(arr):
    # sort the arr using quick sort
    # base case if our arr is 0 or 1
    if len(arr) < 2:
        return arr  # already sorted

    # otherwise we want to create 3 vars: pivot, left, right
    else:
        # pivot is our arr[0]
        # left is empty arr
        # right is empty arr
        pivot = arr[0]
        left = []
        right = []

        # loop through the arr starting at index 1 bc our pivot starts at index 0
        for i in arr[1:]:
            # anything smaller than the current index in loop is put in left arr
            if i <= pivot:
                left.append(i)
            # anything larger than the current index in loop is put in right arr
            else:
                right.append(i)

    # we want to return the outcome of our recursive call bc all we are doing above is Dividing and we need to conquer
    return quick_sort(left) + [pivot] + quick_sort(right)


print(quick_sort([1, 1, 4, 4, 5, 5, 3, 3, 9, 0, 0]))
'''
Input: a List of integers where every int except one shows up twice
Returns: an integer
'''


def single_number(arr):
    # create var for two seperate arrs and a prev pointer
    a = []
    b = []
    prev = 0
    # sorth the arr using quick_sort helper function
    sorted_arr = quick_sort(arr)
    print("SA", sorted_arr)

    # loop thru sorted arr
    for i in range(0, len(sorted_arr)):
        # # if arr[i] != prev push arr[i] to a and push(1) to b
        if arr[i] != prev:
            a.append(arr[i])
            b.append(int(1))
            # print('[b]', [b])
            a = quick_sort(a)
            print("Aaaa", a)
        # # otherwise add 1 to end of arr b
        else:
            b[len(b)-1] += 1
            # b = quick_sort(b)
    # assign arr[i] to prev variable every loop so we move up one spot in our arr
        prev = arr[i]
    # return [b]
    print("A", a)
    result = 0
    for x in b:
        # print("I AM BBBBx", x)
        if x == 1:
            result = x
    return result
"""
