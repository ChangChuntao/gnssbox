import math
from gnssbox.coordTran.xyz2blh import xyz2blh
from gnssbox.coordTran.blh2xyz import blh2xyz
# ABMF00GLP,2919786.0,-5383745.0,1774604.0,16.262,-61.528,-25.268
system = 'GRS80'
B,L,H = xyz2blh(-2375667.7598, 3624137.1503, 4664612.5153, system)
print(math.degrees(B),math.degrees(L),H)

# X,Y,Z = blh2xyz(B,L,H,system)
# print(X,Y,Z)