
def q4(string):
    return "1"

def test_q4():
    
    test_sequence = "abeba"
    real = "abeba"
    result = q4(test_sequence)
    assert len(real) == len(result), f"Expected: {real} ({len(real)}) Got: {result} ({len(result)})"


test_q4()