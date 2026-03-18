def traducir_linea(linea):
    partes = linea.strip().split()

    if not partes:
        return None

    comando = partes[0]

    if comando == "INICIO":
        return "Robot inicia ejecución."
    elif comando == "FIN":
        return "Robot finaliza ejecución."
    elif comando == "AVANZAR":
        return f"Robot avanza {partes[1]} pasos."
    elif comando == "GIRAR":
        return f"Robot gira hacia la {partes[1].lower()}."
    elif comando == "DETENER":
        return "Robot se detiene."
    else:
        return f"Instrucción desconocida: {linea}"
