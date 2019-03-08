def kangaroo(x1, v1, x2, v2):
    if v1>v2:
        if ((x1-x2)%(v2-v1))==0:
            return "YES"
        else:
            return "NO"
    else:
        return "NO"

    
result = kangaroo(x1,v1,x2,v2)