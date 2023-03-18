
def q2(coins, weights, target):
    
    V = []
    n = len(coins)

    for i in range(target+1): 
        V.append(0)
    
    for i in range(0, n): # For a growing pool of coin demoninations
        for j in range(0, target): # For every possible target value from 0 to target
            j = target - j

            current_solution = V[j]

            if coins[i] <= j: # If the value of the current coin could be used in the solution
                    
                    k = j // coins[i] # Maximum instances this coin can be used in the solution

                    other_solution = V[j-(coins[i] * k)] + weights[i] * k # Predict the value outcome of maximal inclusion of i
                    
                    if other_solution < current_solution or current_solution == 0:
                        V[j] = other_solution

    return V[target]

def test_q2():
    
    coins = [1, 2, 5]
    weights = [2, 3, 40]
    target_value = 10
    optimal_weight = 15
    result = q2(coins, weights, target_value)
    assert result == optimal_weight, f"C: {coins}\nW: {weights}    Target: {target_value}\nExpected {optimal_weight} got {result}\n\n"

def q2_brute_force_check_optimal():
    pass

def q2_brute_force_disprove_optimal():

    coin_values = [1, 2, 5]
    target = 24

    from itertools import permutations
    permu_weights = list(permutations(list(range(1, 100)), 3))

    for peru in permu_weights:
        weights = list(permu)

        ratios = {}

        for i in range(len(coin_values)):
            ratios[coin_values[i] / weights[i]] = [coin_values[i], weights[i]]

        keys = list(ratios.keys())
        keys.sort(reverse=True)

        # result = {}
        # for key in keys:


test_q2()
