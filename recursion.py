

def P (C, n, w, p):
    # Base Case
    if (C == 0):
        return 0
    
    # Keeps track of profits of subproblem + p[i], i being subproblem item's index
    solution = [-1] * n 

    # Obtain profits for taking item 0 to n for all branches
    for i in range(n):
        if (C >= w[i]):
            solution[i] = P(C - w[i],n,w,p) + p[i]
        else:
            solution[i] = 0
    
    # Finds highest profit
    largest = max(solution)
    print(solution)
    return largest


if __name__ == "__main__":
    w = [4, 6, 8]
    p = [7, 6, 9]
    print(P(14,3,w,p))
   
    