def printKnapsack(C, pi, wi, profit):
    if C == 0:
        return
    n = len(wi)
    ans = 0
    chosenItem = -1
    for j in range(n):
        if (C - wi[j] >= 0):
            newAns = profit[C - wi[j]] + pi[j]
            if newAns > ans:
                ans = newAns
                chosenItem = j

    if chosenItem == -1:
        return

    global knapsackContents
    knapsackContents.append(wi[chosenItem])
    printKnapsack(C - wi[chosenItem], pi, wi, profit)


def knapsack(wi, pi, C):
    profit = []

    for r in range(C+1):
        profit.append(0)

    for r in range(C+1):
        for c in range(len(wi)):
            if(wi[c] <= r):
                if(profit[r] < profit[r-wi[c]] + pi[c]):
                    profit[r] = profit[r-wi[c]] + pi[c]

    print("Running Result of P({}): {}".format(C, profit))
    printKnapsack(C, pi, wi, profit)
    return profit[C]


wi = [5,6,3]
pi = [4,10,6]
C = 10
knapsackContents = []
print("\nwi:", wi)
print("pi:", pi)
print("Max Profit:", knapsack(wi, pi, C))
print("Knapsack Contents:", knapsackContents)

wi = [5, 6, 8]
pi = [7, 6, 9]
knapsackContents = []
print("\nwi:", wi)
print("pi:", pi)
print("Max Profit:", knapsack(wi, pi, C))
print("Knapsack Contents:", knapsackContents)
