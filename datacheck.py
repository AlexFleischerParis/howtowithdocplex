from docplex.mp.model import Model

mdl = Model(name='modeling assistance')

#to turn on modeling assistance
mdl.parameters.read.datacheck=2;

x = mdl.continuous_var(name='x')

mdl.add_constraint(x+0.3333333333<=2, 'ct')
mdl.maximize(x)

mdl.solve(log_output=True,)

'''

which gives

CPLEX Warning  1036: Decimal part of coefficient for right-hand side
in constraint 'ct' looks like 2/3 in single precision.


'''
