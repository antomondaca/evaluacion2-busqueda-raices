# Evaluación de Laboratorio 2: La raíz que se esconde

Ramo: Computación Numérica INF-123

Integrantes:
- Antonella Mondaca
- Luis Manzur

## Descripción del Proyecto

Este repositorio contiene el desarrollo de la Evaluación 2, cuyo objetivo es implementar y comparar seis métodos de búsqueda de raíces, los cuales son:

- Bisección
- Falsa Posición
- Punto Fijo
- Secante
- Newton-Raphson
- Newton-Raphson Mejorado

Con estos métodos analizamos distintas funciones (polinómica, logarítmica, exponencial, trigonométrica y mixta), incluyendo el análisis crítico de una función con raíz doble que solo toca el eje x.

Para todas las funciones usamos una tolerancia de 1e-6 y un tope de 100 iteraciones, y medimos el error como |x_k - raíz|.

## Estructura del Repositorio

De acuerdo a la rúbrica solicitada, el proyecto se organiza de la siguiente manera:

- `src/scripts/`: contiene todos los scripts de Python con la implementación de los métodos y las funciones.
- `src/assets/`: carpeta donde se guardan los gráficos generados en formato PNG (funciones con sus raíces y gráficos de convergencia).
- `src/data/`: contiene los archivos CSV generados por cada función con los datos (x, f(x)) y el resumen de convergencia.
- `informe.md`: documento con las respuestas a las preguntas de convergencia y la conclusión argumentada.
- `requirements.txt`: lista de dependencias necesarias (numpy, matplotlib).

## ¿Qué hace cada script?

Todos los scripts están en `src/scripts/` y se conectan desde `main.py`:

- `main.py`: es el script principal. Recorre las funciones, crea la carpeta data/, genera un CSV por función con las columnas (x, f(x)), ejecuta los seis métodos sobre cada función y al final escribe el resumen de convergencia y llama a las gráficas.
- `funciones.py`: acá está el diccionario `Funciones` con todo lo que necesita cada caso: la función f(x), su derivada (df) y segunda derivada (d2f), la función de punto fijo (g), el intervalo [a, b], las estimaciones x0 y x1, los límites para graficar, si la raíz es doble y su raíz conocida.
- `biseccion.py`: método de bisección (cerrado, usa el teorema de Bolzano).
- `falsa_posicion.py`: método de la falsa posición (cerrado).
- `punto_fijo.py`: iteración funcional de punto fijo usando g(x).
- `secante.py`: método de la secante.
- `new_raphson.py`: método de Newton-Raphson.
- `newton_mejorado.py`: Newton-Raphson mejorado, que es aplicar Newton sobre f/f' (por eso sirve para raíces dobles).
- `graficos.py`: genera las gráficas de cada función con su raíz, la convergencia |error| vs iteración en escala log y el resumen de iteraciones por método y función.

>Nota: los métodos devuelven siempre (raíz, iteraciones, historial de errores, si convergió o no), así que el main los puede usar todos de la misma forma.

## Configuración del Entorno Virtual (venv)

Para ejecutar este proyecto, utilizamos un entorno virtual local de Python. Esto nos permite aislar las dependencias del proyecto sin afectar la instalación global de Python en tu sistema.

### 1) Crear el entorno virtual

Desde la raíz del repositorio, abre tu terminal y ejecuta el siguiente comando para crear el entorno en una carpeta llamada venv/:

```bash
python -m venv venv
```
>(Nota: la carpeta venv/ ya está ignorada en el .gitignore, así que no se sube al repositorio).

### 2) Activar el entorno

Debes activar el entorno antes de instalar las dependencias o correr los scripts:

En Linux / macOS:
```
source venv/bin/activate
```

En Windows:
```
venv\Scripts\activate
```

Una vez activado, verás (venv) al inicio de la línea de comandos de tu terminal.

### 3) Instalar dependencias

Con el entorno activado, instala las librerías requeridas ejecutando:

```
pip install -r requirements.txt
```

Esto instalará numpy para los cálculos numéricos y matplotlib para la generación de gráficos.

### 4) Ejecución del Código

Una vez que el entorno está activo y las dependencias instaladas, corre el script principal desde la raíz del repositorio:

```
python src/scripts/main.py
```

Los CSV se guardan solos en `src/data/` y los PNG en `src/assets/`.

>Nota sobre gráficos: si estás corriendo los scripts en un entorno sin interfaz gráfica, no hay problema, porque matplotlib guarda los gráficos directamente en la carpeta src/assets/ usando savefig() en lugar de mostrarlos en pantalla con show().

### 5) Desactivar el entorno

Cuando termines de trabajar, puedes salir del entorno virtual simplemente ejecutando:

```
deactivate
```
