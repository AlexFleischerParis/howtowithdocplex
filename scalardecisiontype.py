from docplex.mp.model import Model

mdl = Model(name='scalar decision type')

binaryVar = mdl.binary_var(name='binaryVar')
integerVar = mdl.integer_var(name='integerVar')
continuousVar = mdl.continuous_var(name='continuousVar')

decisionVars=[binaryVar,integerVar,continuousVar]

mdl.add_constraint(binaryVar<=2.5, 'ctBin')
mdl.add_constraint(integerVar<=2.5, 'ctInt')
mdl.add_constraint(continuousVar<=2.5, 'ctContinuous')

mdl.maximize(binaryVar+integerVar+continuousVar)

mdl.solve()

for v in decisionVars:
    print(v.name," = ",v.solution_value)

'''

which gives

binaryVar  =  1.0
integerVar  =  2.0
continuousVar  =  2.5


'''
