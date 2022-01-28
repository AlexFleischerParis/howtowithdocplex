from docplex.cp.model import CpoModel

mdl = CpoModel(name='mutiply binary decision variables')
x = mdl.binary_var(name='x')
y = mdl.binary_var(name='y')
z = mdl.binary_var(name='z')

mdl.add(z==x*y)
msol=mdl.solve()

decisionVars=[x,y,z]


for v in decisionVars:
    print(v.name," = ",msol[v])


