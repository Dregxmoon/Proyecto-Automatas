from lexer import analizar_lexico
from parser import validar_programa
from translator import traducir_linea

RUTA_ARCHIVO = "../ejemplos/programa.txt"

def main():
    try:
        with open(RUTA_ARCHIVO, "r", encoding="utf-8") as archivo:
            lineas = [linea.strip() for linea in archivo if linea.strip()]
    except FileNotFoundError:
        print("No se encontró el archivo del programa.")
        return

    print("=== ANALISIS LEXICO ===")
    for i, linea in enumerate(lineas, start=1):
        tokens = analizar_lexico(linea)
        print(f"Línea {i}: {tokens}")

    print("\n=== ANALISIS SINTACTICO ===")
    errores = validar_programa(lineas)

    if errores:
        for error in errores:
            print(error)
        print("\nEl programa tiene errores. No se puede traducir.")
        return

    print("Programa válido.")

    print("\n=== TRADUCCION ===")
    for linea in lineas:
        salida = traducir_linea(linea)
        if salida:
            print(salida)

if __name__ == "__main__":
    main()
