# Datos con los que vas a trabajar
# name = "Moon"
name = "Ganimedes"
# gravity = 0.00162 # in kms
gravity = 0.00143 # in kms
# planet = "Earth"
planet = "Marte"

text = f"""
THE { name.upper() } AND THE { planet.upper() }
-------------------------------------------------------------------------------
Planet Name: { planet }
Gravity on Ganymede: { gravity * 1000 } m/s2
"""

print( text )