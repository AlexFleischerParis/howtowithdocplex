from docplex.mp.model import Model

mdl = Model(name='floor')

r=range(0,4)
x=[1.5,4.0,2.0001,5.9999]

y = mdl.integer_var_list(4,0,1000,name="y")
f = mdl.continuous_var_list(4,0,0.99999,name="f")

for i in r:
    mdl.add(x[i]==y[i]+f[i])

mdl.solve()

for i in r:
    print(x[i]," ==> ",y[i].solution_value)

"""

which gives

1.5  ==>  1.0
4.0  ==>  4.0
2.0001  ==>  2.0
5.9999  ==>  5.0

"""
    

    



