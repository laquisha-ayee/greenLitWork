def fourSum(nums, target):
    nums.sort()
    n = len(nums)
    result = []

    for i in range(n):
        if i > 0 and nums[i] == nums[i - 1]:
            continue
        for j in range(i + 1, n):
            if j > i + 1 and nums[j] == nums[j - 1]:
                continue
            for k in range(j + 1, n):
                if k > j + 1 and nums[k] == nums[k - 1]:
                    continue
                for l in range(k + 1, n):
                    if l > k + 1 and nums[l] == nums[l - 1]:
                        continue
                    if nums[i] + nums[j] + nums[k] + nums[l] == target:
                        result.append([nums[i], nums[j], nums[k], nums[l]])
    return result


#Test1
print(fourSum([1, 0, -1, 0, -2, 2], 0))

#Test2
print(fourSum([2, 2, 2, 2, 2], 8))

#Test4
print(fourSum([0, 0, 0, 0], 0))

