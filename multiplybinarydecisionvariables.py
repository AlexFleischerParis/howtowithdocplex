#suppose we want z=x*y

from docplex.mp.model import Model
mdl = Model(name='mutiply binary decision variables')

x = mdl.binary_var(name='x')
y = mdl.binary_var(name='y')

z= mdl.binary_var(name='z')

mdl.add(x+y<=1+z)
mdl.add(z<=x)
mdl.add(z<=y)

mdl.add(z==1)

# We could also write
#mdl.add(z==mdl.min(x,y))
# or
#mdl.add(z==(mdl.logical_and((x==1),(y==1))))


mdl.solve()

decisionVars=[x,y,z]

for v in decisionVars:
    print(v.name," = ",v.solution_value)

