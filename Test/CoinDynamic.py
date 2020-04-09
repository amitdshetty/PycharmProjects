import sys

def minCoins(coins, m, currency):
    # table[i] will be storing the minimum
    # number of coins required for i value.
    # So table[V] will have result
    table = [0 for i in range(currency + 1)]
    table[0] = 0

    # Initialize all table values as Infinite
    for i in range(1, currency + 1):
        table[i] = sys.maxsize

    for i in range(1, currency + 1):
        # Go through all coins smaller than i
        for j in range(m):
            if (coins[j] <= i):
                sub_res = table[i - coins[j]]
                if (sub_res != sys.maxsize and
                        sub_res + 1 < table[i]):
                    table[i] = sub_res + 1
    return table[currency]

def main():
    coins = [1, 2, 4, 8]
    m = len(coins)
    currency = 22
    print("Minimum coins required is ", minCoins(coins, m, currency))

if __name__ == "__main__":
    main()

"""
Sample Problem:

Minimum coins required is  4
"""