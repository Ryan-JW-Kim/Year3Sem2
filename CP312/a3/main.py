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

def q2(ls):
    
    def recur(ls, left, right):

        # Base Case of single element subarray
        if left == right:
            return [[ls[left], 1]]
        
        middle = (left + right) // 2

        # Consider both left and right sides of subarray
        left_result = recur(ls, left, middle)
        right_result = recur(ls, middle, right)
        
        # Find max instance of majority elem in left subarray
        L = 0
        for i in range(len(left_result)):
            if left_result[i][1] > left_result[L][1]:
                L = i
            
        # Find max instance of majority elem in right subarray
        R = 0
        for i in range(len(right_result)):
            if right_result[i][1] > right_result[R][1]:
                R = i
        
        # Found max instances of same GIF object on left and right sides
        if left_result[L][0] == right_result[R][0]:
            
            # Combine the counts found in both sides
            left_result[L][1] += right_result[R][1]
            return [left_result[L]]
        
        # Max Instace of both sides is left and we want to combine the count from right and return to a higher level 
        elif left_result[L][1] > right_result[R][1]:

            for i in range(len(right_result)):
                if right_result[i][0] == left_result[L][0]:
                    left_result[L][1] += right_result[i][1]
                    break
            
            return [left_result[L]]
        
        # Max Instance of both sides is right and we want to combine the count from left and return to a higher level
        elif left_result[L][1] < right_result[R][1]:

            for i in range(len(left_result)):
                if left_result[i][0] == right_result[R][0]:
                    right_result[R][1] += left_result[i][1]
                    break
            
            return [right_result[R]]

        # Max instances are different GIF objects but have the same occurence, therefore algo cant decide which is max at this layer
        else:

            # Combine instance count from right into left 
            for i in range(len(right_result)):
                if right_result[i][0] == left_result[L][0]:
                    left_result[L][1] += right_result[i][1]
                    break 
            
            # Combine instnace count from left into right
            for i in range(len(left_result)):
                if left_result[i][0] == right_result[R][0]:
                    right_result[R][1] += left_result[i][1]
                    break

            return [right_result[R], left_result[L]]

    potentials = recur(ls, 0, len(ls)-1) 

    if len(potentials) != 1:
        return "FAIL"
    
    return str(potentials[0][0])

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
    
# test_q1()
test_q2()
# test_q3()