def majorityElementII(nums):
    n=len(nums)
    d={}
    out=[]
    for i in range(len(nums)):
        if nums[i] in d:
            d[nums[i]]+=1
        else:
            d[nums[i]]=1
       
    for key,value in d.items():
        if value>n//3:
            out.append(key)
    return out
        
arr=list(map(int,input().split()))
print(majorityElementII(arr))      