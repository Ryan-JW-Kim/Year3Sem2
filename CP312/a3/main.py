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

def q2():
    
    def func(ls, start, end, counter):

        if (end-start) > 1:
            
            middle = (left + right) // 2

            temp_left = func(ls, start, middle, counter)
            temp_right = func(ls, middle, end, counter)
        
        else:
            return 

def q3():
    pass

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

def test_q3():
    C1 = [1, 2, 3, 4, 5, 6]
    C2 = [2, 3, 4, 1, 2, 4]
    A = q3(C1, C2)
    print(A)
    
test_q1()
# test_q2()
# test_q3()