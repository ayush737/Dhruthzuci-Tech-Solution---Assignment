import flask as fk 

def intersection(lst1 ,lst2):
    return(set(lst1)&set(lst2))


lst1 = [4,9,5]
lst2 = [9,4,9,8,4]
print(intersection(lst1 ,lst2))