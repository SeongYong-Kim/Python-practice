import numpy as np

'''matrix1 = [['Bm3' 1.5]
 ['Bm3' 1.0]
 ['C4' 0.5]
 ['Bm3' 1.0]
 ['C4' 0.5]
 ['Em4' 1.5]
 ['Em4' 1.0]
 ['F4' 0.5]
 ['Em4' 1.0]
 ['F4' 0.5]
 ['G4' 1.5]
 ['F4' 0.5]
 ['G4' 0.5]
 ['F4' 0.5]
 ['Em4' 1.0]
 ['C4' 0.5]
 ['Bm3' 1.5]
 ['Bm3' 1.0]
 ['C4' 0.5]
 ['Bm3' 1.0]
 ['C4' 0.5]
 ['Em4' 1.5]
 ['Em4' 1.0]
 ['F4' 0.5]
 ['Em4' 1.0]
 ['F4' 0.5]
 ['G4' 1.0]
 ['F4' 0.5]
 ['Em4' 1.0]
 ['C4' 0.5]
 ['Bm3' 1.0]
 ['C4' 0.5]
 ['Em4' 1.5]
 ['Em4' 1.0]
 ['F4' 0.5]
 ['Em4' 1.5]
 ['Em4' 1.5]
 ['Em4' 1.5]
 ['Em4' 1.5]
 ['Bm4' 1.5]
 ['Bm4' 1.5]
 ['Bm4' 1.5]
 ['Bm4' 0.5]
 ['B4' 0.5]
 ['Bm4' 0.5]
 ['G4' 1.0]
 ['F4' 0.5]
 ['Em4' 1.0]
 ['F4' 0.5]
 ['G4' 1.5]
 ['F4' 0.5]
 ['G4' 0.5]
 ['F4' 0.5]
 ['Em4' 1.0]
 ['C4' 0.5]
 ['Bm3' 1.5]
 ['Bm3' 1.0]
 ['Bm3' 0.5]
 ['C4' 1.0]
 ['Bm3' 0.5]
 ['C4' 1.5]
 ['Em4' 1.0]
 ['Em4' 0.5]
 ['F4' 1.0]
 ['Em4' 0.5]
 ['G4' 1.0]
 ['F4' 0.5]
 ['Em4' 1.0]
 ['C4' 0.5]
 ['Bm3' 1.0]
 ['C4' 0.5]
 ['Em4' 1.5]
 ['Em4' 1.0]
 ['F4' 0.5]
 ['Em4' 1.5]
 ['Em4' 1.5]
 ['Em4' 1.5]
 ['Em4' 1.5]
 ['Bm4' 1.5]
 ['Bm4' 1.5]
 ['Bm4' 1.5]
 ['Em5' 0.5]
 ['Em5' 1.0]
 ['C5' 1.5]
 ['Bm4' 1.5]
 ['G4' 0.5]
 ['G4' 1.0]
 ['F4' 0.5]
 ['G4' 0.5]
 ['F4' 0.5]
 ['Em4' 1.0]
 ['C4' 0.5]
 ['Bm3' 1.5]
 ['Bm3' 1.0]
 ['C4' 0.5]
 ['Bm3' 1.5]
 ['Em4' 1.5]
 ['Em4' 0.5]
 ['Em4' 1.0]
 ['Em4' 1.0]
 ['F4' 0.5]
 ['G4' 1.0]
 ['F4' 0.5]
 ['Em4' 1.0]
 ['C4' 0.5]
 ['Bm3' 1.0]
 ['C4' 0.5]
 ['Em4' 0.5]
 ['Em4' 1.0]
 ['Em4' 0.5]
 ['F4' 1.0]
 ['Em4' 1.5]
 ['Em4' 1.5]
 ['Em4' 1.5]
 ['Em4' 1.5]]

matrix2 = [['Bm3' 0.5]
 ['C4' 1.0]
 ['Bm3' 1.5]
 ['Bm3' 1.5]
 ['Bm3' 0.5]
 ['C4' 1.0]
 ['Bm3' 1.5]
 ['Bm3' 1.5]
 ['Em4' 1.5]
 ['Em4' 1.0]
 ['F4' 0.5]
 ['G4' 1.0]
 ['F4' 0.5]
 ['Em4' 1.5]
 ['Em4' 1.0]
 ['C4' 0.5]
 ['Bm3' 1.5]
 ['Em4' 0.5]
 ['F4' 0.5]
 ['G4' 0.5]
 ['F4' 1.5]
 ['F4' 1.5]
 ['F4' 0.5]
 ['G4' 1.0]
 ['F4' 0.5]
 ['Em4' 1.0]
 ['C4' 0.5]
 ['Bm3' 1.0]
 ['Em4' 1.0]
 ['G4' 0.5]
 ['F4' 1.0']
 ['Em4' 0.5]
 ['C4' 0.5]
 ['Bm3' 0.5]
 ['C4' 0.5]
 ['Bm3' 1.5]
 ['Bm3' 1.0]
 ['C4' 0.5]
 ['Bm3' 1.5]
 ['F4' 0.5]
 ['G4' 1.0]
 ['G4' 1.5]
 ['G4' 1.5]
 ['Bm4' 1.5]
 ['Bm4' 1.0]
 ['Em5' 0.5]
 ['C5' 1.0]
 ['Bm4' 0.5]
 ['G4' 1.5]
 ['F4' 1.0]
 ['Em4' 0.5]
 ['F4' 0.5]
 ['G4' 0.5]
 ['F4' 0.5]
 ['Em4' 1.5]
 ['Em4' 1.5]
 ['C4' 0.5]
 ['Bm3' 1.0]
 ['Em4' 0.5]
 ['F4' 0.5]
 ['G4' 0.5]
 ['F4' 1.5]
 ['F4' 1.0]
 ['Em4' 0.5]
 ['F4' 0.5]
 ['G4' 1.0]
 ['F4' 1.0]
 ['Em4' 0.5]
 ['C4' 0.5]
 ['Bm3' 1.0]
 ['Em4' 1.0]
 ['G4' 0.5]
 ['F4' 1.0]
 ['Em4' 0.5]
 ['C4' 0.5]
 ['Bm3' 0.5]
 ['C4' 0.5]
 ['Bm3' 1.5]
 ['Bm3' 1.0]
 ['C4' 0.5]
 ['Bm3' 1.5]]

matrix3 = [['C4' 1.0]
 ['G3' 0.5]
 ['C4' 1.0]
 ['Em4' 0.5]
 ['C4' 1.5]
 ['C4' 1.0]
 ['G3' 0.5]
 ['C4' 1.0]
 ['Em4' 0.5]
 ['C4' 1.5]
 ['C5' 0.5]
 ['C5' 1.0]
 ['Bm4' 0.5]
 ['C5' 0.5]
 ['Bm4' 0.5]
 ['G4' 0.5]
 ['F4' 0.5]
 ['G4' 0.5]
 ['Bm4' 1.5]
 ['Bm4' 1.0]
 ['C5' 0.5]
 ['G4' 1.5]
 ['G4' 1.5]
 ['F4' 1.0]
 ['Em4' 0.5]
 ['C4' 0.5]
 ['Em4' 1.0]
 ['G4' 1.5]
 ['F4' 1.0]
 ['Bm4' 0.5]
 ['G4' 1.0]
 ['F4' 0.5]
 ['Em4' 1.5]
 ['Em4' 0.5]
 ['F4' 0.5]
 ['Em4' 0.5]
 ['C4' 0.5]
 ['Bm3' 0.5]
 ['G3' 0.5]
 ['C4' 1.5]
 ['C4' 1.0]
 ['Em4' 0.5]
 ['C4' 1.5]
 ['C5' 0.5]
 ['C5' 1.0]
 ['Bm4' 1.0]
 ['C5' 0.5]
 ['G4' 0.5]
 ['r' 1.0]
 ['C5' 0.5]
 ['C5' 1.0]
 ['Bm4' 1.0]
 ['C5' 0.5]
 ['G4' 0.5]
 ['r' 1.0]
 ['C5' 1.5]
 ['Bm4' 0.5]
 ['C5' 0.5]
 ['Bm4' 0.5]
 ['G4' 0.5]
 ['F4' 0.5]
 ['G4' 0.5]
 ['Bm4' 1.5]
 ['Bm4' 1.0]
 ['C5' 0.5]
 ['G4' 0.5]
 ['r' 1.0]
 ['G4' 1.0]
 ['G4' 0.5]
 ['F4' 1.0]
 ['Em4' 0.5]
 ['C4' 0.5]
 ['Em4' 1.0]
 ['G4' 0.5]
 ['G4' 1.0]
 ['F4' 1.0]
 ['Bm4' 0.5]
 ['G4' 0.5]
 ['F4' 0.5]
 ['r' 0.5]
 ['Em4' 1.5]
 ['Em4' 0.5]
 ['F4' 0.5]
 ['Em4' 0.5]
 ['C4' 0.5]
 ['Bm3' 0.5]
 ['G3' 0.5]
 ['C4' 1.5]
 ['C4' 1.0]
 ['Em4' 0.5]
 ['C4' 0.5]
 ['r' 1.0]
 ['C5' 1.5]
 ['C5' 1.0]
 ['C5' 0.5]
 ['C5' 1.5]
 ['C5' 1.5]
 ['Bm4' 1.0]
 ['C5' 0.5]
 ['G4' 1.5]
 ['C5' 1.5]
 ['Em5' 0.5]
 ['C5' 0.5]
 ['Bm4' 0.5]
 ['G4' 0.5]
 ['F4' 0.5]
 ['G4' 0.5]
 ['Bm4' 1.5]
 ['Bm4' 1.0]
 ['C5' 0.5]
 ['G4' 1.5]
 ['G4' 1.5]
 ['F4' 1.0]
 ['Em4' 0.5]
 ['C4' 0.5]
 ['Em4' 1.0]
 ['G4' 1.5]
 ['F4' 1.0]
 ['Bm4' 0.5]
 ['G4' 0.5]
 ['F4' 1.0]
 ['Em4' 1.5]
 ['Em4' 0.5]
 ['F4' 0.5]
 ['Em4' 0.5]
 ['C4' 0.5]
 ['Bm3' 0.5]
 ['G3' 0.5]
 ['C4' 1.5]
 ['C4' 1.0]
 ['Em4' 0.5]
 ['C4' 0.5]
 ['r' 1.0]]
'''


matrix4 = [[
['G4', 1.5], ['G4', 1], ['G4', 0.5], ['G4', 1.5], ['G4', 1.5],
['G4', 1], ['G4', 0.5], ['G4', 1.5], ['G4', 1.5], ['G4', 0.5],
['Bm3', 0.5], ['G4', 0.5], ['F4', 1], ['Em4', 0.5], ['C4', 1.5],
['C4', 1], ['Em4', 0.5], ['C4', 0.5], ['Em4', 1], ['G4', 0.5],
['G4', 1], ['F4', 1], ['Em4', 0.5], ['C4', 0.5], ['Em4', 1],
['G4', 0.5], ['G4', 1], ['F4', 1], ['Em4', 0.5], ['C4', 0.5],
['Em4', 1], ['G4', 1.5], ['G4', 0.5], ['F4', 0.5], ['Em4', 0.5],
['C4', 1.5], ['Em4', 0.5], ['A3', 0.5], ['C4', 1.5], ['C4', 1.5], ['r', 1.5]
['G4', 1], ['G4', 0.5], ['G4', 1], ['G4', 0.5], ['G4', 1.5],
['G4', 1], ['Bm3', 0.5], ['C5', 1], ['C5', 0.5], ['C5', 1.5],
['G4', 1.5], ['G4', 0.5], ['Bm4', 0.5], ['G4', 0.5], ['F4', 1],
['Em4', 0.5], ['C4', 1.5], ['C4', 1], ['Em4', 0.5], ['C4', 0.5],
['Em4', 1], ['G4', 1.5], ['F4', 1], ['Em4', 0.5], ['C4', 0.5],
['Em4', 1], ['G4', 1.5], ['F4', 1], ['Em4', 0.5], ['C4', 0.5],
['Em4', 1], ['Em4', 1.5], ['Em4', 0.5], ['F4', 0.5], ['Em4', 0.5],
['C4', 0.5], ['Bm3', 0.5], ['G3', 0.5], ['C4', 1.5], ['C4', 1.5], ['r', 1.5]
]]

r1 = matrix4[0]
