def majorityElement(nums):
    n=len(nums)
    d={}
    for i in range(len(nums)):
        if nums[i] in d:
            d[nums[i]]+=1
        else:
            d[nums[i]]=1
       
    for key,value in d.items():
        if value>n//2:
            return key
        
arr=list(map(int,input().split()))
print(majorityElement(arr))      