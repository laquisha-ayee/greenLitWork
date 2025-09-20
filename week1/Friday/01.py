```python
# [6 2 8] [3 1 8]
#         [3 1] [8]
#         [1 3] [8]
#         [3][1] []
# [2 6 8] [1 3 8]
# [1 2 3 6 8 8]
def merge(left, right):
    print(f"merge({left = }, {right = })")
    # put together in one longer array
    result = []
    while left and right:
        if left[0] < right[0]:
            result.append(left.pop(0))
        else:
            result.append(right.pop(0))
    # add any remaining elements from left and right
    # determine whether left or right has elements remaining
    result = [*result, *left, *right]
    print(f"{result = }")
    return result


def merge_sort(array):
    print(f"merge_sort({array = })")
    if len(array) < 2:
        return array

    middle_index = len(array) // 2

    left = array[:middle_index]
    right = array[middle_index:]

    sorted_left = merge_sort(left)
    sorted_right = merge_sort(right)

    result = merge(sorted_left, sorted_right)
    print(f"{result = }")
    return result
```