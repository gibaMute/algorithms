def smallest(list):
    small= list[0]
    for i in list:
        if i<small:
            small=i
    return small