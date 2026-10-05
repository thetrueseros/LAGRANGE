import numpy as np
import os
import sympy as sp
from sympy.parsing.sympy_parser import parse_expr as pexpr, standard_transformations as strans, implicit_multiplication_application as ima
from tabulate import tabulate as t

def EjecutarLagrange():
    x = sp.Symbol('x')
    LimpiarConsola()
    print("=" * 60)
    print("        INTERPOLACIÓN Y POLINOMIO DE LAGRANGE")
    print("=" * 60)

    # 1. Ingreso de la función f(x)
    funcion_str = input("\nIngrese la función f(x) a aproximar (ej: 2x**3 + 5x + 8, sin(x), exp(x)):\nf(x) = ")
    
    try:
        transformaciones = strans + (ima,)
        expresion = pexpr(funcion_str, transformations=transformaciones)
        f_eval = sp.lambdify(x, expresion, 'numpy')
    except Exception as e:
        print(f"\nError al procesar la función: {e}")
        input("Presione enter para regresar.")
        return

    # 2. Ingreso de puntos (n + 1 puntos)
    print("\n--- INGRESO DE PUNTOS ---")
    try:
        n_puntos = int(input("Ingrese la cantidad de puntos (n + 1): "))
        if n_puntos < 2:
            print("Se necesitan al menos 2 puntos para interpolar.")
            input("Presione enter para regresar.")
            return
    except ValueError:
        print("Debe ingresar un número entero válido.")
        input("Presione enter para regresar.")
        return

    x_puntos = []
    print(f"\nIngrese los {n_puntos} valores de x (nodos de interpolación):")
    for i in range(n_puntos):
        val_x = PedirNumero(f"  x[{i}] = ")
        x_puntos.append(val_x)

    # Calcular y_i = f(x_i)
    y_puntos = [float(f_eval(vx)) for vx in x_puntos]

    # Mostrar la tabla de nodos evaluados
    tabla_nodos = [[i, x_puntos[i], y_puntos[i]] for i in range(n_puntos)]
    print("\nNODOS DE INTERPOLACIÓN GENERADOS (x_i, y_i = f(x_i)):")
    print(t(tabla_nodos, headers=["i", "x_i", "y_i = f(x_i)"], tablefmt="fancy_grid", floatfmt=".8f"))

    # 3. Construcción del Polinomio de Lagrange P_n(x)
    P_n_sym = 0
    L_i_lista = []

    for i in range(n_puntos):
        L_i = 1
        for j in range(n_puntos):
            if i != j:
                L_i *= (x - x_puntos[j]) / (x_puntos[i] - x_puntos[j])
        L_i_lista.append(L_i)
        P_n_sym += y_puntos[i] * L_i

    # Simplificar polinomio resultante
    P_n_simplificado = sp.simplify(P_n_sym)
    P_n_eval = sp.lambdify(x, P_n_simplificado, 'numpy')

    print("\n" + "=" * 60)
    print("POLINOMIO DE LAGRANGE OBTENIDO P_n(x):")
    print(f"P_n(x) = {P_n_simplificado}")
    print("=" * 60)

    # 4. Punto a evaluar x_eval
    print("\n--- EVALUACIÓN E INTERPOLACIÓN EN UN PUNTO ---")
    x_eval = PedirNumero("Ingrese el punto x_0 en el que desea interpolar/evaluar: ")

    # Evaluaciones
    f_x0 = float(f_eval(x_eval))
    Pn_x0 = float(P_n_eval(x_eval))

    # Errores en x_0
    error_abs_x0 = abs(f_x0 - Pn_x0)
    error_rel_x0 = (error_abs_x0 / abs(f_x0)) if f_x0 != 0 else 0.0

    # 5. Cálculo del Error Máximo en el intervalo definido por los nodos
    a_inter = min(x_puntos)
    b_inter = max(x_puntos)
    
    puntos_muestreo = np.linspace(a_inter, b_inter, 500)
    f_m = f_eval(puntos_muestreo)
    Pn_m = P_n_eval(puntos_muestreo)
    
    # Manejo si la evaluación da un escalar constante
    if np.isscalar(Pn_m):
        Pn_m = np.full_like(puntos_muestreo, Pn_m)

    errores_en_intervalo = np.abs(f_m - Pn_m)
    error_maximo = float(np.max(errores_en_intervalo))

    # 6. Muestreo de Resultados Finales
    resultados = [
        ["Punto evaluado (x_0)", f"{x_eval:.8f}"],
        ["Valor Real f(x_0)", f"{f_x0:.8f}"],
        ["Valor Interpolado P_n(x_0)", f"{Pn_x0:.8f}"],
        ["Error Absoluto |f(x_0) - P_n(x_0)|", f"{error_abs_x0:.8e}"],
        ["Error Relativo en x_0", f"{error_rel_x0:.8e}"],
        [f"Error Máximo en [{a_inter:.2f}, {b_inter:.2f}]", f"{error_maximo:.8e}"]
    ]

    print("\nTABLA DE RESULTADOS Y ERRORES:")
    print(t(resultados, headers=["Métrica / Parámetro", "Valor"], tablefmt="fancy_grid"))

    input("\nProceso finalizado. Presione Enter para regresar al menú principal.")

def LimpiarConsola():
    if os.name == 'nt':
        os.system('cls')
    else:
        os.system('clear')

def PedirNumero(mensaje):
    while True:
        entrada = input(mensaje).strip()
        if not entrada:
            print("No ingresó ningún carácter. Intente nuevamente.")
            continue
        try:
            return float(entrada)
        except ValueError:
            print("Caracter inválido. Ingrese un valor numérico (entero o decimal).")