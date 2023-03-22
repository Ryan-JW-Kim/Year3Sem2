from pandas import *
def q4(s):
    
    r = s[::-1]

    n = len(s)
    P = [[0 for _ in range(len(s))] for __ in range(len(s))]
    D = [[0 for _ in range(len(s))] for __ in range(len(s))]

    if s == r:
        return len(s)

    for i in range(n):
        for j in range(n):
            if s[i] == r[j]:
                P[i][j] = P[i-1][j-1] + 1
                D[i][j] = "up-left"

            else:
            
                if P[i-1][j] > P[i][j-1]:
                    P[i][j] = P[i-1][j]
                    D[i][j] = "up"

                else:
                    P[i][j] = P[i][j-1]
                    D[i][j] = "left"
    
    print('\n\n\n')
    print(DataFrame(P, columns=list(s), index=list(r)))
    print('\n\n\n')
    print(DataFrame(D, columns=list(s), index=list(r)))
    print('\n\n\n')

    row = n-1
    column = n-1
    LCS_palindrome = ""

    while row > 0 and column > 0:

        if D[row][column] == "up-left":
            print(s[row])
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
    assert len(real) == result, f"Expected: {real} ({len(real)}) Got: {result} ({len(result)})"


test_q4()