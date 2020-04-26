def list_true(n):
    list1 = [False,False]
    for i in range(2,n+1):
        list1.append(True)
    return list1


def mark_false(bool_list, p):
    for i in range(p,len(bool_list)):
        if(i==p):
            bool_list[i] = True
        elif(i%p==0):
            bool_list[i] = False
    return bool_list


def find_next(bool_list, p):
    global result
    for i in range (p+1,len(bool_list)):
        if(bool_list[i]==True):
            result = i
            break
        elif(bool_list[i]!=True):
            result = None
    return result


def prime_from_list(bool_list):
    list4 = []
    for i in range (0,len(bool_list)):
        if(bool_list[i]==True):
            list4.append(i)
    return list4




def sieve(n):
    blist = list_true(n)
    p=2
    while p :
        blist = mark_false(blist,p)
        p = find_next(blist,p)
    q = prime_from_list(blist)
    return q

print(sieve(20))
