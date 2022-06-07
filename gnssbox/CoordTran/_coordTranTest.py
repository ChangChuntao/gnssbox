import math
from gnssbox.coordTran.xyz2blh import xyz2blh
from gnssbox.coordTran.blh2xyz import blh2xyz
# ABMF00GLP,2919786.0,-5383745.0,1774604.0,16.262,-61.528,-25.268
system = 'WGS84'
B,L,H = xyz2blh(2919786.0,-5383745.0,1774604.0, system)
print(B,L,H)

X,Y,Z = blh2xyz(B,L,H,system)
print(X,Y,Z)