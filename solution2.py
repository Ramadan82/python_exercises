n = 153
m = str(n)
sum = 0
for i in range(0, len(m)):
	sum += int(m[i])**int(len(m))
if sum == n:
     print "True"
else: 
    print "False"  
