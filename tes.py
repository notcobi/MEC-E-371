# Solve the following problems using Python and submit your code.

# A stainless steel piping system (k = 13.2 W/m/K) with inner diameter 6 cm and outer diameter 6.5 cm is transporting steam at 402oC. 
# The 3.5-cm thick insulating layer that covers the pipe helps limit the heat transfer, 
# which takes place between the steam and the surroundings at 4oC by radiation and
#  natural convection with hcombined = 20 W/m2/K. The heat transfer coefficient 
# inside the pipe is 75 W/m2/K, and the thermal conductivity of the insulation 
# is 0.036 W/m/K. Determine the rate of heat loss (in W) from the steam per unit
# length of the pipe.

import math
import numpy as np

# Convective heat resistance
def R_conv(h, A):
    return 1/(h*A)

# Conductive heat resistance for a cylinder
def R_cond_cyl(k, r_1, r_2, L):
    return math.log(r_2/r_1)/(2*math.pi*k*L)

# Conductive heat resistance for a plane wall
def R_cond_plane(k, A, L):
    return L/(k*A)

# Heat resistance for sphere
def R_cond_sphere(k, r_1, r_2):
    return 1/(4*math.pi*k)*(1/r_1 - 1/r_2)

# begin solution
r_inner = 0.06/2 # m
r_outer = 0.065/2 # m
r_insulation = 0.065/2 + 0.035 # m

k_steel = 13.2 # W/m/K
k_insulation = 0.036 # W/m/K
h_combined = 20 # W/m^2/K
h_inner = 75 # W/m^2/K

l = 1 # m

# Convection inside pipe
A_inner = math.pi*2*r_inner*l
R_inner = R_conv(h_inner, A_inner)

# Conduction through steel
R_steel = R_cond_cyl(k_steel, r_inner, r_outer, l)

# Conduction through insulation
R_insulation = R_cond_cyl(k_insulation, r_outer, r_insulation, l)

# Convection outside pipe
A_outer = math.pi*r_insulation**2
R_outer = R_conv(h_combined, A_outer)

# Total resistance
R_total = R_inner + R_steel + R_insulation + R_outer

# Heat loss
Q = (402 - 4)/R_total


print("Heat loss: {:.2f} W".format(Q))




