def kaprekarNumbers(p, q):
    sq=0
    lst=[]
    for i in range(p,q+1):
        sq=i*i
        s = str(sq)
        catch = int(len(s)/2)
        if sq==1:
            lst.append(1)
        elif len(s)==2:
            s1 = int(s[0])
            s2 = int(s[1])
            #print(i,sq,s1,s2,"len==2")
            if s2!=0:
                if s1+s2==i:
                    lst.append(i)
        elif len(s)>2:
            s1 = int(s[:catch])
            s2 = int(s[catch:])
            #print(i,sq,s1,s2,"len>2")
            if s2!=0:
                if s1+s2==i:
                    lst.append(i)

    if len(lst)>0:
        for i in lst:
            print(i,end=" ")
    else:
        print("INVALID RANGE")
                
            
        
                
  


if __name__ == '__main__':
    p = int(input())

    q = int(input())

    kaprekarNumbers(p, q)