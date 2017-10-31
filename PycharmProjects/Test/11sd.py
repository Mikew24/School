
def drawparrolelogram (rows, colums):
 s=rows*' '
 o=(rows)*" "
 x=1
 print(s)
 print(s, colums*'*')
 d = rows
 for stars in range(rows):
     print(s[x:],'*',o[x:],'*')
     x += 1

 print(colums*'*')

drawparrolelogram(5,6)
