def validar_programa(lineas):
    errores = []

    if not lineas:
        errores.append("El programa está vacío.")
        return errores

    if lineas[0].strip() != "INICIO":
        errores.append("El programa debe comenzar con INICIO.")

    if lineas[-1].strip() != "FIN":
        errores.append("El programa debe terminar con FIN.")

    for i, linea in enumerate(lineas[1:-1], start=2):
        partes = linea.strip().split()

        if not partes:
            continue

        comando = partes[0]

        if comando == "AVANZAR":
            if len(partes) != 2 or not partes[1].isdigit():
                errores.append(f"Error sintáctico en línea {i}: AVANZAR debe llevar un número.")
        elif comando == "GIRAR":
            if len(partes) != 2 or partes[1] not in ["DERECHA", "IZQUIERDA"]:
                errores.append(f"Error sintáctico en línea {i}: GIRAR debe llevar DERECHA o IZQUIERDA.")
        elif comando == "DETENER":
            if len(partes) != 1:
                errores.append(f"Error sintáctico en línea {i}: DETENER no lleva parámetros.")
        else:
            errores.append(f"Error sintáctico en línea {i}: comando no reconocido.")

    return errores
