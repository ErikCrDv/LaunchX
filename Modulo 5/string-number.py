print("Welcome!")
firstPlanet = int( input("Introduzca la distancia del primer planeta:") )
secondPlanet = int( input("Introduzca la distancia del segundo planeta:") )

if firstPlanet > secondPlanet:
    print( f'La distancia entre los planetas es de { abs( firstPlanet - secondPlanet ) } km' )
    print( f'La distancia entre los planetas es de { abs( (firstPlanet - secondPlanet) * 0.621 ) } millas' )
elif firstPlanet < secondPlanet:
    print( f'La distancia entre los planetas es de { abs( secondPlanet - firstPlanet ) } km' )
    print( f'La distancia entre los planetas es de { abs( (secondPlanet - firstPlanet) * 0.621 ) } millas' )
else:
    print('Los planetas estan en el mismo punto x.x')

distancia = abs(firstPlanet - secondPlanet) * 0.621
print(f'La distancia es: { distancia } en millas')