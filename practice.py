def simpleScan(P,T):
    m = len(P)
    n = len(T)
    k = 0
    j = 0
    while j <= n-m:
        if T[j] != P[k]:
            j = j - k + 1
            k = 0
        else:
            j += 1
            k += 1
            if k == m:
                return j - k
    return -1

print(simpleScan("hi","ehi"))
