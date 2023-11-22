from qwerty import*
import string
# make a dictionary, if the alphabet isn't in it append then remove.

def cityList(x):
    alphabets = dict(zip(string.ascii_lowercase,  range(26)))
    alphabetS = dict(zip(string.ascii_uppercase,  range(26)))
    # print(alphabets)
    # alphabet = {'a': 'A', 'b': 'B', 'c': 'C', 'd': 'D', 'e': 'E', 'f': 'F', 'g': 'G', 'h': 'H', 'i': 'I', 'j': 'J', 'k': 'K', 'l': 'L', 'm': 'M', 'n': 'N', 'o': 'O', 'p': 'P', 'q': 'Q', 'r': 'R', 's': 'S', 't': 'T', 'u': 'U', 'v': 'V', 'w': 'W', 'x': 'X', 'y': 'Y', 'z': 'Z'}
    # letters='qwertyuiopasdfghjklzxcvbnmQWERTYUIOPASDFGHJKLZXCVBNM ,'
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
        print(lst)


        # for i in range(len(lst)):
        lst=','.join(lst)
        # print(lst)
        lst=lst.replace('-', ' ')
        # print(lst)
        lst=lst.split(',')
        # print(lst)       
        lst.append(x[i])
        for x[i] in lst:
            # print(x[i])
            # print(lst)
            if alphabets or alphabetS or ' ' not in x[i]:
                # print(x[i])
                # del lst[-1]
                lst.pop(-1)
            if '/n' in x[i]:
                lst.pop(-1)
            count+=1
            if count==5:
                break
    print(lst)

b='''Andorra la Vella,Andorra,Andorra la Vella,3041563,SprockhÃ¶vel,Germany,North Rhine-Westphalia,2829998,Umm al Qaywayn,United Arab Emirates,Umm al Qaywayn,290594

'''

cityList(b) 

# figure out how to fix the javascript code, then add css



#attempting to fix again
#used chatgpt to help




