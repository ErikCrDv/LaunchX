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

print(f'Hay { len(planetas) } planetas')
print ( f'Planetas: { planetas }' )
# for planeta in planetas:
#     print ( planeta )

planetas.append('Pluto')
print(f'Ahora hay { len(planetas) } planetas')
print ( f'Planetas: { planetas }' )
print( f'El ultimo platena es: { planetas[-1] }' )

