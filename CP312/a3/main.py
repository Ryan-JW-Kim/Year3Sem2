import sys

def q1(citations):

    n = len(citations)

    left = 0
    right = n-1

    while left <= right:

        middle = (left+right) // 2

        if citations[middle] > middle+1: # Still within the K-index range
            left = middle + 1
        
        elif citations[middle] == middle+1:
            left = middle
            right -= 1

        else:
            right = middle - 1
        

    return middle if citations[middle] != 0 else -1

def recur1(ls, left, right):
    
    if len(ls) == 0:
        return "FAIL"
    
    # Base Case
    if left >= right:
        return ls[left]
    
    # If not Base Case, Divide
    middle = (left + right) // 2
    l_result = recur1(ls, left, middle)
    r_result = recur1(ls, middle+1, right)

    # Base Case for the number of Instances required to be majority
    majority_target = ((right-left) // 2) + 1
    if majority_target == 1 and l_result == r_result:
        return l_result
    
    elif majority_target == 1:
        return "FAIL"
    
    # Counting the number of instance of possible majority from Left
    l_count = 0
    if l_result != "FAIL":
        for i in range(left, right+1):
            if ls[i] == l_result:
                l_count += 1
    
    # Counting the number of instance of possible majority from Right
    r_count = 0
    if r_result != "FAIL":
        for i in range(left, right+1):
            if ls[i] == r_result:
                r_count += 1 
        
    # Is Left possibility the majority
    if l_count >= majority_target:
        return l_result
    
    # Is Right possibility the majority
    elif r_count >= majority_target:
        return r_result

    else:
        return "FAIL"

def q2(ls):

    result = recur1(ls, 0, len(ls)-1) 
    return result

def q3(A, B):
    
    A.sort()
    B.sort()

    result = []

    for i in range(len(A)):
        result.append((A[i], B[i]))

    return result

def test_q1():

    C = [17, 17, 12, 10, 7, 4, 2, 2, 1, 1, 1]
    A = q1(C)
    assert A == 4, f"Expected: \"4\" got {A} instead..."

    C = [17, 17, 12, 10, 7, 6, 2, 2, 1, 1, 1]
    print(C)
    print(list(range(1,len(C))))
    A = q1(C)
    assert A == 5, f"Expected: \"5\" got {A} instead..."

    C = [9, 9, 8, 7]
    A = q1(C)
    assert A == 3, f"Expected: \"3\" got {A} instead..."

    C = [3, 0, 0, 0]
    A = q1(C)
    assert A == 0, f"Expected: \"0\" got {A} instead..."

    C = [0, 0, 0, 0]
    A = q1(C)
    assert A == -1, f"Expected: \"-1\" got {A} instead..."

    print('Well done... Q1 completed')

def test_q2():

    A = ['a', '2', '2', 'c', 'v', '2', '2']
    result = q2(A)
    assert result == '2', f"Expected: 2 got {result}"

    A = []
    result = q2(A)
    expect = "FAIL"
    assert result == expect, f"Expected {expect} got {result}" 

    A = ['1', '2', '3']
    result = q2(A)
    expect = "FAIL"
    assert result == expect, f"Expected {expect} got {result}"

    A = ['A', 'A', 'B', 'C', 'D', 'E', 'E', 'E', 'E', 'E', 'E', 'E']
    result = q2(A)
    expect = "E"
    assert result == expect, f"Expected {expect} got {result}"

def test_q3_summation(pairs, b=None):

    sum = 0

    if b == None:
        for (p1, p2) in pairs:
            # print(f"Ai:{p1} + Bi:{p2} ---- ({(p1-p2)**2})")
            sum += (p1 - p2)**2
    
    else:
        for i in range(len(pairs)):
            sum += (pairs[i] - b[i])**2
    return sum

def test_q3_minimized(A, B):

    import itertools
    possible_A = list(itertools.permutations(A))
    possible_B = list(itertools.permutations(B))

    all_sums = []
    for A in possible_A:
        for B in possible_B:
            A, B = list(A), list(B)
            summation = test_q3_summation(A, B)

            all_sums.append(summation)

    minimal = min(all_sums)

    for A in possible_A:
        for B in possible_B:
            A, B = list(A), list(B)
            summation = test_q3_summation(A, B)

            if summation == minimal:

                pairs = []
                for i in range(len(A)):
                    pairs.append((A[i], B[i]))

                d = {'Sum': summation,
                     "A": A,
                     'B': B,
                     'P': pairs}
                
                return d

def test_q3():
    C1 = [1, 2, 3, 4, 5, 6]
    C2 = [2, 3, 4, 1, 2, 4]
    pairs = q3(C1, C2)
    sum = test_q3_summation(pairs)
    
    print(f"Result: {sum}\nGiven Pairs:{pairs}")

    result_dict = test_q3_minimized(C1, C2)

    print(f"R:{pairs}")
    print(f"I:{result_dict['P']}")
    
# test_q1()
# test_q2()
test_q3()