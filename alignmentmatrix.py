import string
import random
import numpy as np

#Initializing sequence length and character set
n = 16
l = ['A', 'C', 'G', 'T']



#Randomizing 2 sequences
s1 = ''.join(random.choices(l, k=n))
s2 = ''.join(random.choices(l, k=n))
print('Sequence 1: ', s1)
print('Sequence 2: ', s2)



#Assigning Score values
match = 5
mismatch = -4
go = -5



#Initializing Alignment Matrix
matrix = np.zeros([n+1,n+1], dtype=int)

matrix[0:(n+1),0] = [ i * go for i in range(n+1)]
matrix[0,0:(n+1)] = [ i * go for i in range(n+1)]

print(matrix)



#Calculating minimum penalty

for i in range(n):
    for j in range(n):
        if s1[i] == s2[j]:
            matrix[i+1][j+1] = matrix[i][j] + match
        else:
            matrix[i+1][j+1] = max(matrix[i][j+1], matrix[i+1][j], matrix[i][j]) + mismatch
    

print(matrix)




#Finding Solution Sequences after Alignment from the matrix

max = 2*n
p = n
q = n
ps1 = max
ps2 = max
g1 = np.zeros(max+1)
g2 = np.zeros(max+1)


while not(p==0 or q==0 ):
    
    if s1[p-1] == s2[q-1]:
        g1[ps1] = s1[p-1]
        g2[ps2] = s2[q-1]
        ps1 -= 1
        ps2 -= 1
        p -= 1
        q -= 1
        
    elif (matrix[p-1][q-1] + match) == matrix[p][q]:
        g1[ps1] = s1[p-1]
        g2[ps2] = s2[q-1]
        ps1 -= 1
        ps2 -= 1
        p -= 1
        q -= 1
    
    elif (matrix[p-1][q] + go) == matrix[p][q]:
        g1[ps1] = s1[p-1]
        g2[ps2] = "_"
        ps1 -= 1
        ps2 -= 1
        p -= 1
    
    elif (matrix[p][q-1] + go) == matrix[p][q]:
        g1[ps1] = s1[p-1]
        g2[ps2] = "_"
        ps1 -= 1
        ps2 -= 1
        q -= 1


while ps1 > 0:
    if p > 0:
        p -= 1
        g1[ps1] = s1[p]
        ps1 -=1
    else:
        g1[ps1] = "_"
        ps1 -= 1
while ps2 > 0:
    if q > 0:
        q -= 1
        g2[ps2] = s2[q]
        ps2 -=1
    else:
        g2[ps2] = "_"
        ps2 -= 1


print(g1)
print(g2)

        