def knapsack(wi, pi, C):
  profit = []

  for r in range(C+1):
    profit.append(0)

  for r in range(C+1):
    for c in range(len(wi)):
      if (wi[c] <= r):
        if(profit[r] < profit[r-wi[c]] + pi[c]):
          profit[r] = profit[r-wi[c]] + pi[c]
          

  print("Running Result of P({}): {}".format(C, profit))
  return profit[C]

wi = [4, 6, 8]
pi = [7, 6, 9]

print("Max Profit:", knapsack(wi, pi, 14))

wi = [5, 6, 8]
pi = [7, 6, 9]

print("Max Profit:", knapsack(wi, pi, 14))
