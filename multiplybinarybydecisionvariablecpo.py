#suppose we want b * x <= 7 

from docplex.cp.model import CpoModel

mdl = CpoModel(name='mutiply binary by decision variable')
b = mdl.binary_var(name='b')
x = mdl.integer_var(0,10,name='x')




mdl.maximize(x)

mdl.add(b*x<=7)

msol=mdl.solve()

decisionVars=[b,x]

for v in decisionVars:
    print(v.name," = ",msol[v])

"""

which gives

b  =  0
x  =  10

"""
