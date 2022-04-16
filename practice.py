def knapsack(wi, pi, C):
    profit = []
    for r in range(C+1):
        profit.append(0)
    for r in range(C+1):
        for c in range(len(wi)):
            if wi[c] <= r:
                if profit[r] < profit[r-wi[c]] + pi[c]:
                    profit[r] = profit[r-wi[c]] + pi[c]
    print("Running result of {}: ({}}", C, profit)
    return profit[C]

wi = [3,4,5]
pi = [4,2,9]
print(knapsack(wi,pi,8))