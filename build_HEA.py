# This code is adopted to construct a high entropy alloy structure (lammps file) based on unary Pt NPs structure (xyz file)
#!/usr/bin/python3
import ase.io
import numpy as np
import ase.io.lammpsdata

ini = ase.io.read('l5.xyz', format = 'xyz') # l5.xyz is the xyz file for Pt NP including 1289 atoms. 


# move the center of NP to (50, 50, 50) and shuffle atoms
positions = ini.get_positions()
for i in range(len(positions)):
	positions[i] = [positions[i][j] + 50 for j in range(3)]
elements = ini.get_chemical_symbols()
np.random.shuffle(positions)
ini.set_positions(positions)


# set up HEA based on experimental ICP result
c = [0, 0.186, 0.172, 0.282, 0.273, 0.087] # This is the list showing the concentrations of Co, Ni, Pt, Ru, Ir, respectively. 
tem_sum = 0
for i in range(len(c)):
	tem_sum += c[i]
	c[i] = tem_sum
print(c)
e = ['Co', 'Ni', 'Pt', 'Ru', 'Ir']

for i in range(len(e)):	
	elements[int(len(elements)*c[i]):int(len(elements)*c[i+1])] = [e[i]]*(int(len(elements)*c[i+1]) - int(len(elements)*c[i]))
ini.set_chemical_symbols(elements)

# set up boundary condition to export lammps file
ini.set_pbc = ((False, False, False))
ini.set_cell([(100, 0, 0), (0, 100, 0), (0, 0, 100)])
ase.io.lammpsdata.write_lammps_data('final.dat', ini)






