'''

docplex version of the OPL CPLEX knapsack model

'''

from docplex.mp.model import Model

mdl = Model(name='knapsack')

NbResources = 7;
Resources=range(0,NbResources)
NbItems = 12;
Items=range(0,NbItems)
Capacity = [ 18209, 7692, 1333, 924, 26638, 61188, 13360 ];
Value = [ 96, 76, 56, 11, 86, 10, 66, 86, 83, 12, 9, 81 ];
Use = [
      [ 19,   1,  10,  1,   1,  14, 152, 11,  1,   1, 1, 1 ],
      [  0,   4,  53,  0,   0,  80,   0,  4,  5,   0, 0, 0 ],
      [  4, 660,   3,  0,  30,   0,   3,  0,  4,  90, 0, 0],
      [  7,   0,  18,  6, 770, 330,   7,  0,  0,   6, 0, 0],
      [  0,  20,   0,  4,  52,   3,   0,  0,  0,   5, 4, 0],
      [  0,   0,  40, 70,   4,  63,   0,  0, 60,   0, 4, 0],
      [  0,  32,   0,  0,   0,   5,   0,  3,  0, 660, 0, 9]];

MaxValue = max(Capacity);

mdl.Take = mdl.integer_var_list(NbItems,0,MaxValue,name="Take")

for r in Resources:
    mdl.add(mdl.sum(Use[r][i]*mdl.Take[i] for i in Items)<=Capacity[r]);

mdl.maximize(mdl.sum(mdl.Take[i]*Value[i] for i in Items))

mdl.solve(log_output=True,)

for i in Items:
    print(i," ==> ",int(mdl.Take[i].solution_value))

'''

0  ==>  0
1  ==>  0
2  ==>  0
3  ==>  154
4  ==>  0
5  ==>  0
6  ==>  0
7  ==>  913
8  ==>  333
9  ==>  0
10  ==>  6499
11  ==>  1180

'''
