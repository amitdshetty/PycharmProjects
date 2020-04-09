import sys

def coin_change_greedy(denomination, denominations):
    n = len(denominations)
    coins_used = []

    i = n - 1
    while (i >= 0):
        while (denomination >= denominations[i]):
            denomination -= denominations[i]
            coins_used.append(denominations[i])
        i -= 1
    print("Coins used:")
    for i in range(len(coins_used)):
        print(str(coins_used[i]))
    print('Minimum coins needed using greedy algorithm: {}'.format(len(coins_used)))

def coin_change_dynamic(coins, V):
    m = len(coins)
    table = [0 for i in range(V + 1)]

    table[0] = 0

    for i in range(1, V + 1):
        table[i] = sys.maxsize

    for i in range(1, V + 1):
        for j in range(m):
            if (coins[j] <= i):
                sub_res = table[i - coins[j]]
                if (sub_res != sys.maxsize and
                        sub_res + 1 < table[i]):
                    table[i] = sub_res + 1
    return table[V]

def main():
    coins = [1,2,4,8]
    total = 22
    print('Greedy Algorithm')
    coin_change_greedy(total, coins)
    no_of_coins_using_dynamic_prog = coin_change_dynamic(coins, total)
    print('\nDynamic Algorithm')
    print('Minimum coins needed using dynamic algorithm: {}'.format(no_of_coins_using_dynamic_prog))

if __name__ == '__main__':
    main()

"""
Sample Output: 

Coins used:
8
8
4
2
Minimum coins needed using greedy algorithm: 4
Greedy Algorithm

Dynamic Algorithm

Minimum coins needed using dynamic algorithm: 4
"""