import Cell as cL
import Module as mD
import Ribbon as rB
import Busbar as bR
import Resistance as rS
import PowerLoss as pL

# Cell
edge_length = 158.75
cell_voc = 680
cell_isc = 10.2
fill_factor = 80
series_resistance = 0.0016
busbar_number = 5

cell = cL.Cell(edge_length, cell_voc, cell_isc, fill_factor, series_resistance, busbar_number)
print(cell)

# Module
cell_number = 72
optic_loss = 96
size = 2
fill_factor = 80
cell_distance = 0.0025

module = mD.Module(cell, cell_number, optic_loss, size, fill_factor, cell_distance)

print(module)

# Ribbon
thickness = 0.25
width = 1
r_resistivity = 0.0225

ribbon = rB.Ribbon(thickness, width, r_resistivity)

print(ribbon)

# Busbar
edge_resistance = 0.01
middle_resistance = 0.01

busbar = bR.Busbar(edge_resistance, middle_resistance)

print(busbar)


# Resistance
r_resistance = rS.Resistance(cell, module, ribbon, busbar)

print(r_resistance)


# Power Loss
power_loss = pL.PowerLoss(module, r_resistance)

print(power_loss)
