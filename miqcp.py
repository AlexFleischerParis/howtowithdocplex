from docplex.mp.model import Model

mdl = Model(name='miqcp')

x=[mdl.integer_var(0,40,name="x"+str(i)) for i in range(0,3)] 

mdl.add(- x[0] +     x[1] + x[2] <= 20)
mdl.add(x[0] - 3 * x[1] + x[2] <= 30)
mdl.add(x[0]**2 + x[1]**2 + x[2]**2 <= 10.0)

mdl.maximize(x[0] + 2 * x[1] + 10 * x[2] - 0.5 * ( 33 * x[0]**2 \
+ 22 * x[1]**2 + 11 * x[2]**2 - 12 * x[0] * x[1] - 23 *x [1] * x[2] ))

mdl.solve()

for i in range(0,3):
    print(x[i].name," = ",x[i].solution_value)

'''

which gives


x0  =  0
x1  =  1.0
x2  =  2.0


'''
