import random

from pulp import *

def generate_instance(n):
    #Se definen utilidades y peso de artículos, y límite máximo de peso de mochila 

    u,v = {}, {}
    for i in range(n):
        u[i] = random.randint(0,100)
        v[i] = random.randint(0,100)

    C = random.uniform(0,1)*sum(v[i] for i in range(n))
    return u,v,C


#Resolvemos el problema con n objetos
n = 10

#Se genera una instancia aleatoria con la función definida anteriormente
u,v,V = generate_instance(n)


#Definición de modelo.
model = LpProblem("Mochila",LpMaximize) #Se declara que problema es de maximización

X = {}
for j in range(n):
	X[j] = LpVariable(f'x_{j}',0,1,LpBinary)

#B = binario
#obj representa los coeficientes de las variables en la funcion objetivo
#Valor obj por defecto= 0
#model.variables.add(names=["x[{0}]".format(i) for i in range(n)], types = ['B']*n, obj = [u[i] for i in range(n)])
#for i in PRODUCTORS:
#    if len(Ni[i])>0:
model += lpSum([X[i]*u[i] for i in range(n)]), "F.O"
model += lpSum([X[i]*v[i] for i in range(n)])>=1, "r1"

#return model,X

#######################
# Ejemplo
#######################
    


#Se crea un modelo


#Se resuelve el modelo
model.solve()

#Resultados
#Valor objetivo
for i in range(n):
    print(X[i].varValue,X[i].name)
    
#print(value(model.objective))
print(value(model.objective))

#print('Fración de los objetos que llevamos',len([i for i in range(n) if mod.solution.get_values("x[{0}]".format(i)) == 1])/n)

#Valor objetivo
#print('Valor objetivo', mod.solution.get_objective_value())