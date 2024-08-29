import matplotlib.pyplot as plt
import random
import numpy as np
#defining search space

x = [-10,10]
y = [-10,10]

# defining initial  and minimal temperature(T) and cooling rate(alpha)

T = 1.0
alpha = 0.99
t_min = 0.01

#defining the energy function and boltzmann constant

E = lambda x: ( x[0]**2 ) + ( x[1]**2 )

k = E((max(x),max(y))) ** 0.5

# Not considering minimum energy as a criteria for stopping, since we want to FIND the minima

point = (random.uniform(-10,10),random.uniform(-10,10))
init = point
E1 = E(point)

dt = 0
min_dE = 0.001


# define the pointlist for plotting

plots = []


# defining the check condition

def Check(de,t,p,const=1) -> bool:
    if de > 0:
        return True
    if np.exp(de/(t*const)) > p:
        return True
    return False


# loop over T, annealing while the temperature cools.

while T > t_min:
    print(T,point)
# initialis the new point, and calculate the new energy, dE and random float

    p_new = (point[0] + random.uniform(-0.1,0.1),point[1]+random.uniform(-0.1,0.1))
    E_new = E(p_new)
    dE = E1 - E_new
    p = random.random()
    print(dE)
    print(np.exp((dE) / T ) )
    print(p)

    if Check(dE,T,p):

        plots.append(point)
        E1 = E_new
        point = p_new
        T = T*alpha
        print(dE)


# check for how much the function is changing

    if dE >= 0 and dE < 0.0001 :
        dt+=1
    else:
        dt = 0

# stop if the function isn't changing a lot anymore.

    if dt == 10:
        break


# plotting graphs

print("INIT = ",init)
print("END = ",point)


x = np.linspace(-10,10,1000)
y = np.linspace(-10,10,1000)

x,y = np.meshgrid(x,y)

z = x**2 + y**2

plots  = np.asarray(plots)

fig,ax = plt.subplots()

ax.contour(x,y,z)
ax.scatter(plots[:,0],plots[:,1],color='red',s=0.1)
ax.scatter(plots[-1,0],plots[-1,1],color='black',s=1)
ax.scatter(plots[0,0],plots[0,1],color='yellow',s=1)

plt.show()