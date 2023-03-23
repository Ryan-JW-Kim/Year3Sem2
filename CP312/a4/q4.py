from pandas import *
def q4(X):
    
    # Create a reverse of the list to compare for longest common subsequence
    Y = X[::-1]

    # Initialize empty matrix
    n = len(X)
    C = [[0 for _ in range(len(X)+1)] for __ in range(len(X)+1)]
    D = [[0 for _ in range(len(X)+1)] for __ in range(len(X)+1)]

    # Simple case check
    if X == Y:
        return X

    elif X == "":
        return ""

    # Filling the matrix
    for i in range(1,n+1):
        for j in range(1,n+1):
            ii = i-1
            jj = j-1

            if Y[ii] == X[jj]:
                C[i][j] = C[i-1][j-1] + 1
                D[i][j] = "up-left"

                # print(f"Found Equals: {X[i]} and {Y[j]}  {i},{j}")

            else:

                m = max(C[i-1][j], C[i][j-1])
            
                if m == C[i-1][j]:
                    C[i][j] = C[i-1][j]
                    D[i][j] = "up"

                elif m == C[i][j-1]:
                    C[i][j] = C[i][j-1]
                    D[i][j] = "left"
    
    # Complete answer retrival via back pointers
    row = n
    column = n
    LCS_palindrome = ""

    while row > 0 and column > 0:

        if D[row][column] == "up-left":
            LCS_palindrome += Y[row-1]
            row -= 1
            column -= 1
    
        elif D[row][column] == "up":
            row -= 1
        
        elif D[row][column] == "left":
            column -= 1
        
    return LCS_palindrome

def test_q4():
    
    test_sequence = "strabetubsa"
    real = "abeba"
    result = q4(test_sequence)
    assert len(real) == len(result), f"Expected: {real} ({len(real)}) Got: {result} ({len(result)})"

    test_sequence = "babad"
    real = "bab"
    result = q4(test_sequence)
    assert len(real) == len(result), f"Expected: {real} ({len(real)}) Got: {result} ({len(result)})"

    test_sequence = "cbbd"
    real = "bb"
    result = q4(test_sequence)
    assert len(real) == len(result), f"Expected: {real} ({len(real)}) Got: {result} ({len(result)})"

    test_sequence = "racecar"
    real = "racecar"
    result = q4(test_sequence)
    assert len(real) == len(result), f"Expected: {real} ({len(real)}) Got: {result} ({len(result)})"

    test_sequence = "Helleworld"
    real = "elle"
    result = q4(test_sequence)
    assert len(real) == len(result), f"Expected: {real} ({len(real)}) Got: {result} ({len(result)})"

test_q4()