def toJadenCase(string):
    a = string.split()
    r = []
    
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

print(toJadenCase("priantiko nur adi pratama"))