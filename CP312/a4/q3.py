
def q3(ls):
    
    left = 0
    right = len(ls)-1

    while left <= right:

        
        middle = (left + right) // 2

        if middle - 1 < 0:
            return ls[middle]
        
        elif middle + 1 >= len(ls):
            return ls[middle]

        v1 = ls[middle - 1]
        v2 = ls[middle]
        v3 = ls[middle + 1]

        if v1 == v2:
            
            if middle % 2 == 0: # Index middle is even:
                
                right  = middle - 1

            else:
                left = middle + 1

        elif v2 == v3:
        
            if middle % 2 == 0: # Index middle is even:
                left = middle + 1
        
            else:
                right = middle - 1 

        else:
            return v2

    return middle

        

def test_q3():

    ls = [1, 1, 3, 3, 4, 5, 5, 7, 7, 8, 8]
    real = q3_brute_force_check_optimal(ls)
    A = q3(ls)
    assert real == A, f"Expected: {real} Got: {A}"

    ls = [1, 1, 3, 3, 4, 4, 5, 5, 7, 7, 8]
    real = q3_brute_force_check_optimal(ls)
    A = q3(ls)
    assert real == A, f"Expected: {real} Got: {A}"

    ls = [1, 3, 3, 4, 4, 5, 5, 7, 7, 8, 8]
    real = q3_brute_force_check_optimal(ls)
    A = q3(ls)
    assert real == A, f"Expected: {real} Got: {A}"

    ls = [1, 1, 3, 3, 4, 4, 5, 5, 7, 7, 8, 8, 9, 10, 10, 11, 11, 12, 12]
    real = q3_brute_force_check_optimal(ls)
    A = q3(ls)
    assert real == A, f"Expected: {real} Got: {A}"


def q3_brute_force_check_optimal(ls):
    
    d = {}

    for elem in ls:
        if elem in d:
            d[elem] += 1
        
        else:
            d[elem] = 1

    for key in d:
        if d[key] == 1:
            return key
        
test_q3()