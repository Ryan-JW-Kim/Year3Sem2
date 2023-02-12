
def question_1_final_solution(l1, l2):
    
    # N squared time
    n = len(l1)
    sums = []
    for i in range(n):
        for j in range(n):
            sums.append(l1[i] + l2[j])
    
    # At worst nlogn
    sums.sort()

    # At worst N time (generally less)
    duplicates_removed = []
    for s in sums:
        if duplicates_removed == []:
            duplicates_removed.append(s)
        
        else:
            if s != duplicates_removed[-1]:
                duplicates_removed.append(s)
    
    # At worst nlogn
    l2.sort()

    # At worst for loop goes N times
    for s in duplicates_removed:

        # At worst logn (binary seach time)
        if binary_search(l2, 0, n-1, s):
            return True
    
    # By max rule the algo is nlogn
    return False
    

def question_2(ls):
    pass



q1_a = [100, 200, 50, 60, 70, 30, 40]
q1_b = [7, 8, 9, 14, 3, 2, 5]
print(question_1_sorted(q1_a, q1_b))


# q2_ls = [1,2,3,4,5,1,1,1,1,1,5,4,3,1]
# print(question_2(q2_ls))