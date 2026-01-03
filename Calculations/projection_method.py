from astropy import units as u
import numpy as n

def SunAngularSize():
    return (1 / m) * (d / D) * u.rad

def SunAngularError():
    return (theta * ((d_d / d) + (d_m / m) + (d_D / D)))

D = 8.5 * u.cm
d = 1.4 * u.cm

F = 350 * u.mm
f = 20 * u.mm

m = F / f

d_d = 0.1 * u.cm
d_m = 0
d_D = 0.2 * u.cm

theta = SunAngularSize()
d_theta = SunAngularError()

# print("Projection Method: ", theta.to(u.deg), d_theta.to(u.deg))

# print("Percentage Error:", (d_theta / theta) * 100)






