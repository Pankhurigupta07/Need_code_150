#Contains Duplicates
def contain_duplicate(arr,n):
    for i in range(n):
        for j in range(i+1,n):
            if(arr[i]==arr[j]):
                return True
                
    return False

arr=[int(x) for x in input().split()]

print(contain_duplicate(arr,len(arr)))