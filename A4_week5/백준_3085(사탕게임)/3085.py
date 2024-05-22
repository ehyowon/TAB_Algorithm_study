n = int(input())

candy = [list(input()) for _ in range(n)]
a = candy[0][0]
row, col = [], []

for i in range(n):
	cnt = 0
	for j in range(n):
		if candy[i][j] == a:
			cnt += 1
		a = candy[i][j]
	row.append(cnt)

for i in range(n):
	cnt = 0
	for j in range(n):
		if candy[j][i] == a:
			cnt += 1
		a = candy[j][i]
	col.append(cnt)

row_max = max(row)
col_max = max(col)
if row_max > col_max:
	print(row_max)
else:
	print(col_max)
