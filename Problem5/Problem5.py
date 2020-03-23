# Given an array of integers, move the elements in such a way that all 0s are at the end,
# while the non-zero elements are moved to the front in the order of their occurrence.

l = [0,0,0,0,1,0,2,3,0,0,0,4,5,0] #initializing a random list

def binSort(arr): #defining the function
    i=0 #initializing the list iterator
    zero_count =0 #initializing a counter that counts the number of 0s in the list
    while i<len(arr):
        # if there is a zero observed during iteration, it will be removed from the list and count will be incremented
        if arr[i]==0:
            arr.pop(i)
            zero_count+=1
        else:
            i+=1 #increment the iterator if the list element is 1
    arr+=[0]*zero_count #append the number of 0s to the end of list
    return arr
            
print(binSort(l))
