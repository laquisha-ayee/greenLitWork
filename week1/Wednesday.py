def findMedianSortedArrays(nums1, nums2):
    merged = sorted(nums1 + nums2)
    

    n = len(merged)
    if n % 2 == 0:
        return (merged[n // 2 - 1] + merged[n // 2]) / 2
    else:
        return merged[n // 2]

# Test Case 1
print(findMedianSortedArrays([1, 3], [2]))  

# Test Case 2
print(findMedianSortedArrays([1, 2], [3, 4]))  

# Test Case 3
print(findMedianSortedArrays([0, 0], [0, 0]))  

# Test Case 4
print(findMedianSortedArrays([], [1]))  

# Test Case 5
print(findMedianSortedArrays([2], []))  