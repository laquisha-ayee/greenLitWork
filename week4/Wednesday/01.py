def is_empty(obj):
    if isinstance(obj, list):
        return len(obj) == 0
    if isinstance(obj, dict):
        return len(obj) == 0
    #handle unexpected types
    raise TypeError("Input must be a list or dict")



print(is_empty({"x": 5, "y": 42}))  
print(is_empty({}))                 
print(is_empty([None, False, 0]))  