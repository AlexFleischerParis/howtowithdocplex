from docplex.mp.model import Model

mdl = Model(name='xyz')


x = mdl.continuous_var(name='x')
y = mdl.continuous_var(name='y')
z = mdl.continuous_var(name='z')

decisionVars=[x,y,z]

mdl.add_constraint(z<=4)

#mdl.add_constraint(x<=y<=z, 'ctxyz') does not work

mdl.add_constraint(x<=y, 'ctxy')
mdl.add_constraint(y<=z, 'ctyz')


mdl.maximize(x+y+z)

mdl.solve()

for v in decisionVars:
    print(v.name," = ",v.solution_value)

'''

which gives

x  =  4.0
y  =  4.0
z  =  4.0


'''
