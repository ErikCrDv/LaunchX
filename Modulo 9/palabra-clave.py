def ReporteMision(
    horaPrelanzamiento, 
    tiempoVuelo, 
    destino, 
    tanqueExterno,
    tanqueInterno
):
    return f"""
    Mision a { destino }
    Tiempo Total: { horaPrelanzamiento + tiempoVuelo } minutos
    Combustible restante: { tanqueInterno + tanqueExterno } galones
    """

print(ReporteMision( 12, 29, "Luna", 200000, 300000))


def ReporteMision2(
    destino, 
    *minutos,
    **combustible
):
    return f"""
    Mision 2 a { destino }
    Tiempo Total: { sum( minutos ) } minutos
    Combustible restante: { sum( combustible.values() ) } galones
    """

print(ReporteMision2("SATURNO", 100, 200, 300, principal=400000, externo=500000))


def ReporteMision3(
    destino, 
    *minutos,
    **combustible
):
    reporte = f"""
    Mision 2 a { destino }
    Tiempo Total: { sum( minutos ) } minutos
    Combustible restante: { sum( combustible.values() ) } galones
    """

    for tanque, capacidad in combustible.items():
        reporte += f"Tanque { tanque } --> { capacidad } galones restantes\n"
    
    return reporte

print(ReporteMision3("SATURNO", 100, 200, 300, principal=400000, externo=500000))

