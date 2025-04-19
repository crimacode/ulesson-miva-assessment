# Problem 1: Plus One
def plus_one(digits):
    """
    Given a list of digits representing a number, increment the number by one.
    """
    # Traverse the list from the last digit backwards
    for i in range(len(digits) - 1, -1, -1):
        if digits[i] == 9:
            # If the digit is 9, it becomes 0 and we carry the 1 to the next more significant digit
            digits[i] = 0
        else:
            # If the digit is not 9, just add one to this digit and we're done
            digits[i] += 1
            return digits
    # If we exited the loop, it means all the digits were 9
    # In this case, we have carried through all digits and need to add a new 1 at the front
    digits.insert(0, 1)
    return digits

# Problem 2: Alternate Min-Max Rearrangement
def alternate_min_max(arr):
    """
    Rearrange the array so that elements alternate between the smallest, largest, 
    second-smallest, second-largest, and so on.
    """
    # First, sort the array to get the elements in ascending order
    sorted_arr = sorted(arr)
    result = []
    left, right = 0, len(sorted_arr) - 1

    # Use two pointers to pick from the sorted list: one from the start (smallest), one from the end (largest)
    while left <= right:
        # Take the next smallest element
        result.append(sorted_arr[left])
        left += 1
        if left <= right:
            # Take the next largest element (only if there are elements remaining)
            result.append(sorted_arr[right])
            right -= 1

    # If the array has an odd number of elements, the middle element will be added in the last iteration 
    # when left == right, so it's already handled by the loop.
    return result

# Example usage:
print(plus_one([1, 2, 3]))     # Expected output: [1, 2, 4]
print(plus_one([4, 3, 2, 1]))  # Expected output: [4, 3, 2, 2]
print(plus_one([9]))           # Expected output: [1, 0]

print(alternate_min_max([13, 7, 8, 3, 2, 10, 15, -1]))   # Expected output: [-1, 15, 2, 13, 3, 10, 7, 8]
print(alternate_min_max([-5, -12, -1, 7, 14, -7, 3, 6]))  # Expected output: [-12, 14, -7, 7, -5, 6, -1, 3]
print(alternate_min_max([3, 6, 9, -10, -5, -2, 0, 8]))    # Expected output: [-10, 9, -5, 8, -2, 6, 0, 3]
