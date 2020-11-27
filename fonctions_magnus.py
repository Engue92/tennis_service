# programme pour encoder les fonctions en prennant en compte la gravité et l'effet Magnus

def f1(T, PX, PY, PZ, VX, VY, VZ):
    return (VX)

def f2(T, PX, PY, PZ, VX, VY, VZ):
    return (VY)

def f3(T, PX, PY, PZ, VX, VY, VZ):
   return (VZ)

def f4(T, PX, PY, PZ, VX, VY, VZ):
    return (((0.00139)*(VX)**2) / 0.058  + (0.0021436*(VX)**2) / (2 + VX*12))

def f5(T, PX, PY, PZ, VX, VY, VZ):
    g = -9.81
    return (g + ((0.00139)*(VY)**2) / 0.058 + (0.0021436*(VY)**2) / (2 + VY*12))

def f6(T, PX, PY, PZ, VX, VY, VZ):
    return (((0.00139)*(VZ)**2) / 0.058  + (0.0021436*(VZ)**2) / (2 + VZ*12))

