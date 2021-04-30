"""
Assignment problem, Python Chile
Pamela Bustamante
"""

import pandas as pd
from pulp import *

df = pd.read_excel("volunteers.xlsx",index_col=0)
#print(df)

df_volunteer=df.values.tolist()
#print(df_volunteer)

n_rows,n_columns=df.shape
#print(df.shape)

prob = LpProblem("volunteers",LpMaximize)
X = {}
Z = {}

for i in range(n_rows):
	for j in range(n_columns):
		X[i,j] = LpVariable(f'x_{i,j}',0,1,LpBinary)

for j in range(n_columns):
	Z[j] = LpVariable(f'z_{j}',0,10)

prob += lpSum([ lpSum([df_volunteer[i][j]*X[i,j] for i in range(n_rows)]) -30*Z[j] for j in range(n_columns)]), "F.O" 

for j in range(n_columns):
	prob += lpSum([X[i,j] for i in range(n_rows)])+Z[j]>=3, "r1_%s"%j #numero minimo de personas por tarea

for j in range(n_columns):
	prob += lpSum([X[i,j] for i in range(n_rows)])<=5, "r2_%s"%j #numero maximo de personas por tarea

for i in range(n_rows):
	prob += lpSum([X[i,j] for j in range(n_columns)])<=3, "r3_%s"%i #numero maximo de tareas por persona

prob.solve()

print(df.index.values.tolist())

for i in range(n_rows):
	for j in range(n_columns):
	   if round(X[i,j].varValue) >0:
	        print(df.index.values.tolist()[i],j+1)
	        #print(X[i,j].varValue,X[i,j].name)

prob.writeLP("volunteers.lp")