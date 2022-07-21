
from random import *
from docplex.mp.model import Model

n=10

r=range(0,n)

v=[randint(0,20) for i in r]


mdl = Model(name='sortvariables')

#decision variables

x = mdl.integer_var_list(n,0,1000,name="x")
y = mdl.integer_var_list(n,0,1000,name="y")
perm = mdl.binary_var_matrix(r,r,name="perm")
permx = mdl.integer_var_matrix(r,r,name="xperm")

for i in r:
    mdl.add(x[i]==v[i])

#order
for i in range(0,n-1):
    mdl.add(y[i]<=y[i+1])

#allDiff

for i in r:
    mdl.add(mdl.sum(perm[i,j] for j in r)==1)
    mdl.add(mdl.sum(perm[j,i] for j in r)==1)

for i in r:
    for j in r:
        mdl.add(mdl.if_then(perm[i,j]==0,permx[i,j]==0))
        mdl.add(mdl.if_then(perm[i,j]==1,permx[i,j]==x[j]))

#apply perm
for i in r:
    mdl.add(y[i]==mdl.sum(permx[i,j] for j in r))
        
mdl.solve()

# Dislay solution
print("input= ",end=" ")
for i  in r:
    print(int(x[i].solution_value),end=" ")
print()     

print("output= ",end=" ")
for i  in r:
    print(int(y[i].solution_value),end=" ")
print()

"""

gives

input=  17 5 17 14 2 10 12 17 14 2 
output=  2 2 5 10 12 14 14 17 17 17 

"""

 
