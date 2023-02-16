def binary_search(ls, left, right, target):

    if left > right:
        return False

    middle = (left + right) // 2

    if target == ls[middle]:
        return middle
    
    elif target < ls[middle]:
        return binary_search(ls, left, middle-1, target)
    
    else:
        return binary_search(ls, middle+1, right, target)

def question_1_final_incorrect(l1, l2):
    
    # N squared time
    n = len(l1)
    sums = []
    for i in range(n):
        for j in range(n):
            sums.append(l1[i] + l1[j])
    
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

    # loop goes N^2 times
    for num in l2:

        # loop goes N times
        for s in duplicates_removed:
            
            target = s - num
            # At worst logn (binary seach time)
            if binary_search(l2, 0, n-1, target):

                print(f"{l2} {0} {n-1} {target}")
                return True
        
    # By max rule the algo is n^2logn
    return False

def question_1_final(l1, l2):
    
    l2.sort()
    n = len(l1)

    for i in range(n):
        for j in range(n):
            s = l1[i] + l1[j]

             

    return False

def find_max(ls, left, right):

    middle = (left + right) // 2

    if ls[middle-1] < ls[middle]:
        return find_max(ls, middle+1, right)
    
    elif ls[middle+1] > ls[middle]:
        return find_max(ls, left, middle-1)

    elif ls[middle] == ls[middle+1] or ls[middle] == ls[middle-1]:
        return middle

def find_end_of_left_segment(ls, left, right):

    if ls[right] > ls[right-1]:
        return right
    
    middle = (left + right) // 2

    if ls[middle] < ls[right]:
        return find_end_of_left_segment(ls, middle, right)

    elif ls[left] < ls[middle]:
        return find_end_of_left_segment(ls, left, middle)

def find_end_of_right_segment(ls, left, right):
    
    middle = (left + right) // 2

    if left == middle:
        return left

    if ls[left] > ls[middle]:
        return find_end_of_right_segment(ls, left, middle)

    elif ls[middle] > ls[right]:
        return find_end_of_right_segment(ls, middle, right)

def question_2_final (ls):

    n = len(ls)
    index_of_mid = find_max(ls, 0, n-1)

    print(index_of_mid)

    p = find_end_of_left_segment(ls, 0, index_of_mid)
    q = find_end_of_right_segment(ls, index_of_mid, n-1)

    return (p+1, q+1)

# q1_a = [100, 302,4030, 202, 20202, 1000]
# q1_b = [7, 8, 9, 14, 3, 2, 5]

# print(question_1_final(q1_a, q1_b))


q2_ls = [2,3,4,5,6,2,1]
print(question_2_final(q2_ls))