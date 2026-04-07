def find_max(lst):
    val = 0
    for i in lst:
        if val < i:
            val = i 
    return val

def find_min(lst):
    val = 0
    for i in lst:
        if val > i:
            val = i 
    return val

def maxmin(lst):
    ans= [find_min(lst) , find_max(lst)]
    return ans

print(maxmin([2,4,1,0,2,-1]))