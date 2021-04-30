import random
from pulp import *

#Variables
X1 = LpVariable(f'x1',0,1000)
X2 = LpVariable(f'x2',0,1000)

#Definición de modelo.
model = LpProblem("Pinturas",LpMaximize) #Se declara que problema es de maximización

#Funcion objetivo
model += lpSum(X1*5000+X2*4000), "F.O" #default: minimization

#Se declaran restricciones
model += lpSum(6*X1+4*X2)<=24, "r1"
model += lpSum(1*X1+2*X2)<=6, "r2"
model += lpSum(-1*X1+2*X2)<=1, "r3"
model += X2<=2, "r4"

#Se resuelve el modelo
model.writeLP("Pinturas.lp")
model.solve()

#Se muestran resultados de x1 y x2
print(X1.varValue,X1.name)
print(X2.varValue,X2.name)

#Valor objetivo
print(value(model.objective))

