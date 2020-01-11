def toJadenCase(string):
    a = string.split()
    r = []
    m=[]
    g = []
    for i in range(len(a)):
        h = a[i];
        for j in range(len(h)):
            if j==0:
                r.append(h[j].upper())
            else:
                r.append(h[j])
        r.append(" ")
        t = "".join(r)
    return(t)