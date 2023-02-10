def question_1_bf(l1, l2):
    n = len(l1)
    m = len(l2)

    sums = []

    for i in range(n):
        for j in range(n):
            if l1[i] + l1[j] not in sums:
                sums.append(l1[i]+l1[j])

    for i in range(m):
        for j in range(m):
            if l2[i] + l2[j] in sums:
                return True

    return False


def question_1_sorted(l1, l2):
    l1.sort()
    l2.sort()



q1_a = [1, 2, 5, 6, 7, 3, 4]
q2_b = [7, 8, 9, 14, 3, 2, 5]

print(question_1_sorted(q1_a, q2_b))
