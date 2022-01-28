#suppose we want b * x <= 7 

from docplex.mp.model import Model
mdl = Model(name='mutiply binary by decision variable')

b = mdl.binary_var(name='b')
x = mdl.integer_var(name='x',lb=0,ub=10)

bx= mdl.integer_var(name='bx')

mdl.maximize(x)

mdl.add(bx<=7)

#Linearization

mdl.add(2*b<=bx)
mdl.add(bx<=10*b)

mdl.add(bx<=x-2*(1-b))
mdl.add(bx>=x-10*(1-b))

mdl.solve()

decisionVars=[b,x]

for v in decisionVars:
    print(v.name," = ",v.solution_value)

"""

which gives

b  =  0
x  =  10.0

"""
