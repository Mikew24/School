def triangle(num):
    numspaces=""
    while(num>=1):
        k=""
        do = num
        while do>0:
            k=k+'*'
            do-=1
        k=numspaces+k
        print(k)
        num-=1
        numspaces=numspaces+' '
def jumpMaximum(list, min, max):
    a=list[0]
    listinrange=[]
    for elem in list:
        if elem>=min and elem<=max:
            listinrange.append(elem)

    # b=list[0]
    # c = list.index(a)
    # list[0]=a
    # list[c]=b
    return listinrange
print(jumpMaximum([5,8,3,21,7,4,14], 4, 14))
triangle(7)