
# Interpolación de Lagrange
``` De Miguel Ángel Zapata Vargas```

Este proyecto implementa el método de **Interpolación de Lagrange** en Python para aproximar funciones matemáticas continuas mediante un polinomio interpolador $P_n(x)$ a partir de $n+1$ nodos de evaluación.

El sistema calcula de forma automática el polinomio simbólico simplificado, permite realizar la evaluación/interpolación en cualquier punto $x_0$, y presenta una tabla detallada con el error absoluto, el error relativo y el error máximo absoluto en el intervalo.

---

## Requisitos del Sistema

Para ejecutar el código fuente correctamente se requiere Python 3.10 o superior y los paquetes listados en `requirements.txt`:

* **numpy** (`2.5.3`)
* **sympy** (`1.14.0`)
* **tabulate** (`0.10.0`)
* **mpmath** (`1.3.0`)

---

## Guía de Instalación y Ejecución

### Opción A: Ejecución Directa (Si las librerías ya están instaladas)

Si el entorno de Python local ya cuenta con `numpy`, `sympy` y `tabulate`, ejecute directamente el comando:

```bash
python main.py

```
Este ejecuta el archivo main, que corresponde al menú de inicio.

---

### Opción B: Configuración mediante Entorno Virtual (Recomendado)

#### 🐧 En Linux / macOS

1. Abra una terminal en la dirección raíz del proyecto que descargó.
2. Cree y active un entorno virtual:
```bash
python3 -m venv .venv

```


* **En Bash / Zsh:**
```bash
source .venv/bin/activate

```


* **En Fish Shell:**
```fish
source .venv/bin/activate.fish

```




3. Instale las dependencias del proyecto:
```bash
pip install -r requirements.txt

```


4. Ejecute la aplicación:
```bash
python main.py

```



#### 🪟 En Windows

1. Abra la consola (`cmd` o PowerShell) en la carpeta raíz del proyecto.
2. Cree y active el entorno virtual:
```powershell
python -m venv .venv
.\.venv\Scripts\activate

```


3. Instale las dependencias:
```cmd
pip install -r requirements.txt

```


4. Ejecute la aplicación:
```cmd
python main.py

```



---

## Sintaxis para el Ingreso de Funciones

El programa utiliza `SymPy` con análisis de multiplicación implícita integrado, lo que permite ingresar expresiones de forma matemática directa o mediante sintaxis estándar de Python.

### Operadores Básicos

| Operación | Sintaxis manual | Ejemplo de entrada |
| --- | --- | --- |
| **Suma / Resta** | `+` / `-` | `2x + 5` ó `2*x + 5` |
| **Multiplicación** | `*` o implícita | `3x**2` ó `3*x**2` |
| **División** | `/` | `(x + 1) / (x - 2)` |
| **Potenciación** | `**` | `x**3 + 2x**2` |

### Funciones Trigonométricas y Especiales (SymPy / NumPy)

Puedes utilizar las siguientes funciones matemáticas estándar directamente en la entrada de $f(x)$:

* **Trigonométricas:** `sin(x)`, `cos(x)`, `tan(x)`
* **Trigonométricas Inversas:** `asin(x)`, `acos(x)`, `atan(x)`
* **Exponenciales y Logarítmicas:**
* `exp(x)` (para $e^x$)
* `log(x)` o `ln(x)` (logaritmo natural)
* `log(x, 10)` (logaritmo en base 10)


* **Raíces:** `sqrt(x)` (para $\sqrt{x}$)

#### Ejemplos de entradas válidas en el programa:

* `2x**3 + 5`
* `sin(x) + cos(2x)`
* `exp(-x) * (x**2 - 1)`
* `sqrt(x + 4) / x`

---

## Estructura del Código

* `main.py`: Punto de entrada interactivo con la estructura del menú principal.


* `lagrange.py`: Módulo que procesa la función $f(x)$, recibe los nodos $x_i$, calcula $y_i = f(x_i)$, genera el polinomio $P_n(x)$ simplificado, e interpole midiendo los errores.


* `requirements.txt`: Especificación de dependencias para el aislador de entorno.



```

```