def missingNumber(arr):
    n=len(arr)
    n=n+1
    total_Sum=(n*(n+1))//2
    Sum=0
    for i in range(len(arr)):
        Sum+=arr[i]
    return total_Sum-Sum

arr=list(map(int,input().split()))
print(missingNumber(arr))