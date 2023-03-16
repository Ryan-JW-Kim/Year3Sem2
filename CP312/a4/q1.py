
def q1(instances):
    pass

def calc_late(order):

    sum = 0
    count = 0

    curr = None
    for t in range(0, max(order) + 1):

        if order == []:
            return 0
        
        print(f"t:{t}")
        if curr == None:
            curr = order.pop(0)

        else:
            if curr < t:
                sum += 1

            curr = order.pop(0)

def test_q1():
    instances = [2, 4, 5, 2]
    optimal_greedy = q1(instances)
    optimal = [2, 2, 4, 5]

    print(calc_late(optimal))
    # assert optimal == optimal_greedy, f"Expected: {optimal} Got {optimal_greedy}"

    # instances = [2, 1, 4, 2]
    # optimal_greedy = q1(instances)
    optimal = [2, 1, 3, 4]
    print(calc_late(optimal))
    # assert optimal == optimal_greedy, f"Expected: {optimal} Got {optimal_greedy}"

test_q1()