
def q4(string):
    
    string2 = str(list(string)[::-1])
    n = len(string)
    m = n

    C = []

    for i in range(n):
        C.append([])

        for j in range(n):
            C[i].append(0)

    for i in range(n):
        for j in range(n):
            if string[i] == string2[j]:
                C[i][j] = C[i-1][j-1] + 1

            else:
                C[i][j] = max(C[i-1][j], C[i][j-1])
    
    return C[n-1][n-1]

def test_q4():
    
    test_sequence = "strabetubsa"
    real = "abeba"
    result = q4(test_sequence)
    assert len(real) == len(result), f"Expected: {real} ({len(real)}) Got: {result} ({len(result)})"


test_q4()