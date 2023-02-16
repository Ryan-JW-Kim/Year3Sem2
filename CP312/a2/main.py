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

def question_1_final(l1, l2):
    
    n = len(l1)
    sums_l1 = []
    sums_l2 = []

    for i in range(n):
        for j in range(n):
            sums_l1.append(l2[i] + l2[j])

    for i in range(n):
            for j in range(n):
                sums_l2.append(l2[i] + l2[j])

    for i in range(n^2):
        if binary_search(sums_l2, 0, n^2-1, sums_l1[i]):
            return True


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

q1_a = [1, 2, 3, 4, 9]
q1_b = [10, 2, 7, 4, 0]

print(question_1_final(q1_a, q1_b))


# q2_ls = [2,3,4,5,6,2,1]
# print(question_2_final(q2_ls))