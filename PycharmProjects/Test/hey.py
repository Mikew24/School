def issublist( list1, list2):
 x=0
 k= True
 if(len(list1)>len(list2)):
  return False
 for elem in list1:

   if elem != list2[x]:
     k=False
   x+=1
 return k
print(issublist([1,2,3],[1,2,3]))