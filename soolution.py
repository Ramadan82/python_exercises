# class Solution:

n = 153
original = n
sum = 0
length = 0
bases = []
while n > 0:
    digit = n%10
    bases.append(digit)
    n = n/10
    length +=1
for base in bases:
    sum = sum + (base**length)
if sum == original:
     print "True"
else: 
    print "False"  