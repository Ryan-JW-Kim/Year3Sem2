
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

    coins = [1]
    weights = [40]
    target_value = 3
    optimal_weight = 120
    result = q2(coins, weights, target_value)
    assert result == optimal_weight, f"C: {coins}\nW: {weights}    Target: {target_value}\nExpected {optimal_weight} got {result}\n\n"

    coins = []
    weights = []
    target_value = 0
    optimal_weight = 0
    result = q2(coins, weights, target_value)
    assert result == optimal_weight, f"C: {coins}\nW: {weights}    Target: {target_value}\nExpected {optimal_weight} got {result}\n\n"


def greedy(coins, weights, target):
     
    ratios = []
    all_data = []

    for i in range(len(coins)):    
        all_data.append({"C": coins[i], "W": weights[i], "R": coins[i]/weights[i]})
        ratios.append(all_data[-1]["R"])

    ratios.sort(reverse=True)

    weight = 0

    for r in ratios:
        for data in all_data:
            if data["R"] == r:

                # Use
                k = target // data["C"]
                weight += data["W"] * k
                target -= data["C"] * k

                data["R"] = -1

                break

    return weight

test_q2()


