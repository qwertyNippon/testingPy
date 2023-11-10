def cityList(x):
    lst=[]
    x = x.replace(' ','-')
    print(x)
    x = x.split(',')
    # print(x) 
    # print(x[0])
    for i in range(0, len(x), 4):
        lst.append(x[i])
    print(lst)
    for i in range(len(lst)):
        lst=','.join(lst)
        lst=lst.replace('-', ' ')
        lst=lst.split(',')
    print(lst)


cityList('les Escaldes,Andorra,Escaldes-Engordany,3040051,Dubai,United Arab Emirates,Dubai,292223,Andorra la Vella,Andorra,Andorra la Vella,3041563')