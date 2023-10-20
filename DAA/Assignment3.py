def knapsack_max_value(max_weight, items):
    n = len(items)
    dp = [[0 for _ in range(max_weight + 1)] for _ in range(n + 1)]

    for i in range(n + 1):
        for w in range(max_weight + 1):
            if i == 0 or w == 0:
                dp[i][w] = 0
            elif items[i - 1].weight <= w:
                dp[i][w] = max(dp[i - 1][w], dp[i - 1][w - items[i - 1].weight] + items[i - 1].value)
            else:
                dp[i][w] = dp[i - 1][w]

    return dp[n][max_weight]

class Item:
    def __init__(self, value, weight):
        self.value = value
        self.weight = weight

items = [
    Item(60, 10),
    Item(100, 20),
    Item(120, 30)
]

max_weight = 50
best_value = knapsack_max_value(max_weight, items)
print("Best value:", best_value)
