def cityList(x):
    lst=[]
    # x = x.strip( )
    x = x.replace(' ','-')
    print(x)
    x = x.split()
    print(x) 
    for i in range(len(x)+4):
        lst.append(i)
    print(lst)


cityList('les Escaldes,Andorra,Escaldes-Engordany,3040051')