
from random import *
from docplex.cp.model import CpoModel

n=10

v=[randint(0,20) for i in range(0,n)]


mdl = CpoModel(name='buses')

#decision variables

x = mdl.integer_var_list(n,0,1000,name="x")
y = mdl.integer_var_list(n,0,1000,name="y")
perm = mdl.integer_var_list(n,0,n-1,name="perm")

for i in range(0,n):
    mdl.add(x[i]==v[i])

#order
for i in range(0,n-1):
    mdl.add(y[i]<=y[i+1])

for i in range(0,n):
    mdl.add(y[i]==mdl.element(x,perm[i]))

#allDiff
mdl.add(mdl.all_diff(perm))   

msol=mdl.solve()

# Dislay solution
print("input= ",end=" ")
for i  in range(0,n):
    print(msol[x[i]],end=" ")
print()    

print("perm= ",end=" ")
for i  in range(0,n):
    print(msol[perm[i]],end=" ")
print()    

print("output= ",end=" ")
for i  in range(0,n):
    print(msol[y[i]],end=" ")
print()

"""

gives

input=  20 12 3 18 6 3 17 16 8 20 
perm=  2 5 4 8 1 7 6 3 0 9 
output=  3 3 6 8 12 16 17 18 20 20

"""

 
