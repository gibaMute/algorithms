# python function to find minumum
# in arr[] of size n
 
 
def smallest(list):
    small= list[0]
    for i in list:
        if i<small:
            small=i
    return small
