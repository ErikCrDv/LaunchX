
new_planet = ''
planets = []

print('Escriba ok cuando termine de ingresar los datos')
while new_planet.lower() != 'ok':

    if( new_planet ): 
        planets.append( new_planet )

    new_planet = input('Ingrese un planeta: ')


for planet in planets:
    print( planet )