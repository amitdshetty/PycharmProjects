import sys


# m is size of coins array (number of different coins)
def minCoins(coins, m, currency):
    # base case
    if (currency == 0):
        return 0
    # Initialize result
    result = sys.maxsize
    for i in range(0, m):
        if (coins[i] <= currency):
            sub_res = minCoins(coins, m, currency - coins[i])
            if (sub_res != sys.maxsize and sub_res + 1 < result):
                result = sub_res + 1
    return result

def main():
    coins = [9, 6, 5, 1]
    m = len(coins)
    currency = 11
    print("Minimum coins required is", minCoins(coins, m, currency))

if __name__ == '__main__':
    main()

"""
Sample Output:

Minimum coins required is 2
"""