import numpy as np
import cvxpy as cp
profit= [12,16]
P= np.array([[1,1],[-1,2],[1,-3]])
Q= np.array([1200,0,600])

# defining the variable
s= cp.Variable(2, integer=True)

# assigning constraints
constraints = [P@s<=Q] 

# defining ojective
objective= cp.Maximize(profit@s)

#defining the problem
prob= cp.Problem(objective,constraints)

# solving the problem
prob.solve()

#printing the optimum value to maximize profit
print("Number of type A,type B dolls to be produce are :", s.value)