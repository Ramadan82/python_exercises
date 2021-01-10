intervals = [[1, 100],
			[10, 50],
			[15, 65]]
maximum = float('-inf')
minimum = float('inf')
for row in intervals:
	if row[0] > maximum:
		maximum = row[0]
	if row[1] < minimum:
			minimum = row[1]
print [maximum, minimum]
