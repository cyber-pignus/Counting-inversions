def merge(arr, z, left_side, mid, right_side): 
    c = left_side     
    d = mid + 1 
    k = left_side     
    inver_count = 0
  
    while c <= mid and d <= right_side: 
  
        if arr[c] <= arr[d]: 
            z[k] = arr[c] 
            k += 1
            c += 1
        else: 
            z[k] = arr[d] 
            inver_count += (mid-c + 1) 
            k += 1
            d += 1

    while c <= mid: 
        z[k] = arr[c] 
        k += 1
        c += 1

    while d <= right_side: 
        z[k] = arr[d] 
        k += 1
        d += 1

    for loop_var in range(left_side, right_side + 1): 
        arr[loop_var] = z[loop_var] 
          
    return inver_count 
    
def mergeSort(arr, n): 
    n = len(arr)
    z = [0]*n 
    return _mergeSort(arr, z, 0, n-1) 
  
def _mergeSort(arr, z, left_side, right_side): 
    inver_count = 0
    if left_side < right_side: 

        mid = (left_side + right_side)//2
  
  
        inver_count += _mergeSort(arr, z, left_side, mid) 
  
        inver_count += _mergeSort(arr, z, mid + 1, right_side) 
  
        inver_count += merge(arr, z, left_side, mid, right_side) 
    return inver_count    
    

num= int(input("enter the number of elements :"))
arr = []
print("enter the array :")
for c in range(0,num):
   arr.append(int(input()))
result = mergeSort(arr, num) 
print("Number of inversions are", result) 


