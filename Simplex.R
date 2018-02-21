#Example of Simplex Maximization

#import linprog library
library(linprog)

#Objective Function
Obj <- c(-6,-8)

#Constraints
con <- rbind( c(-3,-1),
              c(-5,-2))

#RHS of constraints
rhs <- c(-4,-7)


#Solve for maximization problem using simplex
solveLP(Obj,rhs,con, TRUE)
