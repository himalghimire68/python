list=['himal',21,14.7,'biratnagar',43,11.45]
list_int=[]
list_float=[]
list_str=[]
for x in list:
    if (type(x)==int):
        list_int.append(x)
    elif (type(x)==float):
        list_float.append(x)
    elif (type(x)==str):
        list_str.append(x)
print(list_int)
print(list_float)
print(list_str)


