def promedio( combustibles ):
    return sum( combustibles ) / len( combustibles )

def lectorCombustible( combustible1, combustible2, combustible3 ):
    return f"""Reporte: 
    PROMEDIO: { promedio([combustible1, combustible2, combustible3])}%
        Combustible 1: {combustible1}%
        Combustible 2: {combustible2}%
        Combustible 3: {combustible3}% 
        """

print( lectorCombustible( 10, 20, 30 ) )