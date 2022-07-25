from docplex.cp.model import CpoModel

mdl = CpoModel(name='scalar decision type')

binaryVar = mdl.binary_var(name='binaryVar')
integerVar = mdl.integer_var(name='integerVar')

binaryVar = mdl.binary_var(name='binaryVar')
integerVar = mdl.integer_var(name='integerVar')
intervalVar = mdl.interval_var(name="intervalVar")


decisionVars=[binaryVar,integerVar,intervalVar]

mdl.add_constraint(binaryVar<=2.5)
mdl.add_constraint(integerVar<=2.5)
mdl.add(mdl.start_of(intervalVar)<=2)
mdl.add(mdl.length_of(intervalVar)==2)


mdl.maximize(binaryVar+integerVar+mdl.end_of(intervalVar))

msol=mdl.solve()

for v in decisionVars:
    print(v.name," = ",msol[v])

'''

which gives

binaryVar  =  1
integerVar  =  2
intervalVar  =  IntervalVarValue(start=2, end=4, size=2)

'''
