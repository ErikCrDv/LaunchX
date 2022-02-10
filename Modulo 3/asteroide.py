
velocidad = 19
asteroide = 20


if velocidad >= 25:

    if asteroide > 25:
        print( 'PELIGRO DE IMPACTO: ' )
    else:
        print( 'ADVERTENCIA' )

elif velocidad >= 20 and velocidad < 25:

    if asteroide > 25:
        print( 'PELIGRO DE IMPACTO: ' )
    else:
        print( 'RAYO - LOOK UP' )

elif velocidad == 19:
    
    if asteroide > 25:
        print( 'PELIGRO DE IMPACTO: ' )
    else:
        print( '19 km/s!: ' )
else:
    if asteroide > 25:
        print( 'PELIGRO DE IMPACTO: ' )
    else:
        print( '¡Sigue con tu día!' )


