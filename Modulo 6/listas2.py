planetas = [
    'Mercury', 
    'Venus', 
    'Earth', 
    'Mars', 
    'Jupiter', 
    'Saturn', 
    'Uranus', 
    'Neptune'
]

NombrePlaneta = input("Introduzca el nombre de un planeta: ")
NombreCap = NombrePlaneta[0].upper() + NombrePlaneta[1:].lower()


idx = planetas.index( NombreCap ) 
print(f'Los planetas mas cerca del sol son { planetas[ :idx ] }')
print(f'Los planetas mas lejos del sol son { planetas[ idx + 1: ] }')
# planetas.index(  )

# planetas.pop()  # Goodbye, Pluto
# print(f'De nuevo hay { len(planetas) } planetas')

# gravity_on_planets = [0.378, 0.907, 1, 0.379, 2.36, 0.916, 0.889, 1.12]