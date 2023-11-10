from qwerty import*
# make a dictionary, if the alphabet isn't in it append then remove.

def cityList(x):
    count=0
    lst=[]
    x = x.replace(' ','-')
    # print(x)
    x = x.split(',')
    # print(x) 
    # print(x[0])
    for i in range(0, len(x), 4):
        lst.append(x[i])
        count+=1
        if count==5:
            break
    # print(lst)
    for i in range(len(lst)):
        lst=','.join(lst)
        lst=lst.replace('-', ' ')
        lst=lst.split(',')
    print(lst)

b='''
SprockhÃ¶vel,Germany,North Rhine-Westphalia,2829998

'''

cityList(b)