from symbols import TOKENS #importa el diccionario con los token para el analisis lexico

#Funcion que detecta si la cadena esta formada solo por digitos
def es_numero(cadena):
    return cadena.isdigit()

#Esta funcion es la que extrae linea por linea del archivo de texto con el script de instrucciones del prorama
def analizar_lexico(linea):
    partes = linea.strip().split() #Separa los componentes de la linea en palabras y quita los espacios.
    resultado = [] #Lista donde se guardan los resultados

    #Ciclo que recorre cada palabra 
    for parte in partes:
        #Verificador de palaras reservadas, basandose en el documento de simbolos
        if parte in TOKENS:
            resultado.append((TOKENS[parte], parte))
        #Verifica si es numero
        elif es_numero(parte):
            resultado.append(("TK_NUMERO", parte))
        #Si no es valido marca error lexico
        else:
            resultado.append(("ERROR_LEXICO", parte))
    #Regres los resultados
    return resultado
