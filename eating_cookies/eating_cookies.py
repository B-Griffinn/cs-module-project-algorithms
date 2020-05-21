'''
Input: an integer
Returns: an integer
'''

"""
3 cookies: 1 1 1
1 1 1
1 2
2 1
3
*** 4 ways to eat cookies ***
"""

"""
# PLAN #
base case: 
if n == 0: 
    return 1 bc there is technically 1 way to eat 0 cookies
elif n < 0
    return 0 bc no way to eat negative cookies
if n == 1:
    return 1 bc there is only one way to eat one cookie
else:
    return fib(n-1) + fib(n - 2) + fib(n-3)
    bc there are only 3 cookies allowed at a time
"""


def eating_cookies(n):
    if n == 0:
        return 1
    elif n < 0:
        return 0
    elif n == 1:
        return 1
    elif n > 1:
        return eating_cookies(n - 1) + eating_cookies(n - 2) + eating_cookies(n - 3)


if __name__ == "__main__":
    # Use the main function here to test out your implementation
    num_cookies = 3

    print(
        f"There are {eating_cookies(num_cookies)} ways for Cookie Monster to each {num_cookies} cookies")
