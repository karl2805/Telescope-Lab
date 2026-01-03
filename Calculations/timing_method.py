from astropy import units as u
import numpy as n

    



recorded_time = 2.3 * u.min
d_recorded_time = 10 * u.second

theta = ((2 * n.pi * recorded_time) / u.day) * u.rad

d_theta = ((2 * n.pi * d_recorded_time) / u.day) * u.rad

print("Timing Method", theta.to(u.deg), d_theta.to(u.deg))
print("Percentage Error", ((d_theta / theta) * 100).to(u.dimensionless_unscaled))