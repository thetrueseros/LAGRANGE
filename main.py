import lagrange as l
import os

def LimpiarConsola():
    if os.name == 'nt':
        os.system('cls')
    else:
        os.system('clear')

def Ejecutar():
    while True:
        LimpiarConsola()
        print("------ --- -- -- - MENÚ DE OPCIONES - -- -- --- ------")
        print("Bienvenido. Por favor, seleccione una de las opciones a continuación.")
        entrada = input("1. Interpolación de Lagrange\n"
                        "2. Salir.\n")
        entrada.strip()

        # Si el input no es un número del 1 al 2
        if not entrada.isdigit() or int(entrada) < 1 or int(entrada) > 2:
            input("Entrada inválida. Presione enter para regresar.")
            Ejecutar()
            return

        match int(entrada):
            case 1: # Ejecutar bisección
                l.EjecutarLagrange()
            case 2: # Ejecutar salir
                entradacerrar = input("¿Está seguro que desea salir? [si/no]: ").lower()
                if entradacerrar in ['si', 's']:
                    input("Presione enter para cerrar.")
                    break
                if entradacerrar in ['no', 'n']:
                    input("Presione enter para regresar.")
                    continue
            
if __name__ == "__main__":
    Ejecutar()