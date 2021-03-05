def ap( array, n):
     
    result = ar[0]
     
    for k in range(1,n):
        result = result ^ ar[k]
     
    return result
 
array = [4 , 1, 2, 1, 2]
print ("Element occurring once is", findSingle(array, len(array)))