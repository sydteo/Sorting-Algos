def simplsScan(P, T):
    i = 0
    j = 0
    k = 0
    m = len(P)
    n = len(T)

    while j < n:
        if T[j] != P[k]:
            i += 1
            j = i
            if (j > n-m):
                break
            k = 0
        else:
            j += 1
            k += 1
            if (k == m):
                return i
    return -1

print("index is found at: ", simplsScan("syd","teosdysyd"))