
def function(ls, target):

	n = len(ls)

	for i in range(n):
		for j in range(n):

			if i != j and abs(ls[i] - ls[j]) <= target:
				return True

	return False

	pass


a = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
b = [1, 1, 3, 57, 5, 6, 7, 8, 9, 10]

j = 11

out = function(a, j)

print(f"Expected: True  Got: {out}")