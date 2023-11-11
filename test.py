from qwerty import*
# import string
# make a dictionary, if the alphabet isn't in it append then remove.

def cityList(x):
    # alphabets = dict(zip(string.ascii_lowercase,  range(26)))
    # print(alphabets)
    alphabets = {'a': 'A', 'b': 'B', 'c': 'C', 'd': 'D', 'e': 'E', 'f': 'F', 'g': 'G', 'h': 'H', 'i': 'I', 'j': 'J', 'k': 'K', 'l': 'L', 'm': 'M', 'n': 'N', 'o': 'O', 'p': 'P', 'q': 'Q', 'r': 'R', 's': 'S', 't': 'T', 'u': 'U', 'v': 'V', 'w': 'W', 'x': 'X', 'y': 'Y', 'z': 'Z'}
    letters='qwertyuiopasdfghjklzxcvbnmQWERTYUIOPASDFGHJKLZXCVBNM'
    # print(alphabets)
    count=0
    lst=[]
    x = x.replace(' ','-')
    # print(x)
    x = x.split(',')
    # print(x) 
    # print(x[0])
    print(x)
    for i in range(0, len(x), 4):
        lst.append(x[i])


    # print(lst)
        # for i in range(len(lst)):
        lst=','.join(lst)
        print(lst)
        lst=lst.replace('-', ' ')
        print(lst)
        lst=lst.split(',')
        print(lst)       
        lst.append(x[i])
        for x[i] in lst:
            print(x[i])
            if x[i] not in letters:
                print(x[i])
                del lst[-1]
                # lst.pop(-1)
            count+=1
            if count==5:
                break
    print(lst)

b='''
SprockhÃ¶vel,Germany,North Rhine-Westphalia,2829998,Andorra la Vella,Andorra,Andorra la Vella,3041563

'''

cityList(b)