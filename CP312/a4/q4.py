
def q4(s):
    
    r = ""
    for i in range(len(s)):
        i = len(s) - i - 1
        r += s[i]

    n = len(s)
    P = [[0 for _ in range(len(s))] for __ in range(len(s))]

    if s == r:
        return len(s)
    
    for i in range(n):
        for j in range(n):
            if s[i] == r[j]:

                if i != 0 and j != 0:
                    P[i][j] = P[i-1][j-1] + 1

                else:
                    P[i][j] = 1

            else:

                P[i][j] = max(P[i-1][j] if i != 0 else 0, P[i][j-1] if j != 0 else 0)
    
    return P[n-1][n-1]

def test_q4():
    
    test_sequence = "strabetubsa"
    real = "abeba"
    result = q4(test_sequence)
    assert len(real) == result, f"Expected: {real} ({len(real)}) Got: {result} ({result})"


test_q4()