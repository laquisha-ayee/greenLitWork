def combinationSum(candidates, target):
    result = []

    def dfs(start, path, total):
        
        if total == target:
            result.append(path[:])
            return
        if total > target:
            return
        for i in range(start, len(candidates)):
            path.append(candidates[i])          
            dfs(i, path, total + candidates[i]) 
            path.pop()                          

    dfs(0, [], 0)
    return result


print(combinationSum([2,3,6,7], 7))
print(combinationSum([2,3,5], 8))
print(combinationSum([2], 1))
