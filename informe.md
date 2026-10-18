# Informe "La raíz que se esconde"

**Ramo:** Computación Numérica INF-123

**Evaluación:** Laboratorio 2 — búsqueda de raíces y análisis de convergencia

**Integrantes:** Antonella Mondaca, Luis Manzur

---

## 1. Cómo trabajamos (ambiente controlado)

Implementamos los seis métodos (bisección, falsa posición, punto fijo, secante, Newton Raphson y Newton Raphson mejorado) y los corrimos sobre seis funciones, una por categoría más el caso de raíz doble. Para que fuera factible fijamos la tolerancia en 1e-6 y un tope de 100 iteraciones para todos los métodos.

Estas son las funciones, con su intervalo (métodos cerrados), sus estimaciones iniciales (métodos abiertos) y su raíz:

| Categoría | Función | Intervalo [a, b] | x₀, x₁ | Raíz |
|---|---|---|---|---|
| Polinómica simple | x³ − x − 2 | [1, 2] | 1.5, 2.0 | 1.521380 |
| Polinómica doble | (x − 2)² | [1, 3] | 1.2, 1.4 | 2.000000 |
| Logarítmica | ln(x) + x − 4 | [2, 3] | 2.5, 3.0 | 2.926271 |
| Exponencial | e⁻ˣ − x | [0, 1] | 0.5, 0.8 | 0.567143 |
| Trigonométrica | cos(x) − x | [0, 1] | 0.5, 0.8 | 0.739085 |
| Mixta | √x − cos(x) | [0.1, 1] | 0.5, 0.9 | 0.641714 |

Para demostrar que la raíz está dentro del rango usamos el teorema de Bolzano. En cinco de las seis funciones se cumple, excepto con la raíz doble, donde la curva toca solamente el eje x en vez de cruzarlo, así que Bolzano y los métodos cerrados no tienen por dónde entrar por así decirlo. En vez de usar |xₖ − xₖ₋₁| como error, ocupamos el error real |xₖ − raíz|, ya que pusimos las raíces exactas en todas las funciones como parámetro de comparación.

---

## 2. ¿Qué método convergió en menos iteraciones en cada función y por qué?

Esta es la tabla de iteraciones hasta converger (con una F marcamos los que alcanzaron el tope de 100):

| Función | Bisección | Falsa Posición | Punto Fijo | Secante | Newton | Newton Mejorado |
|---|---|---|---|---|---|---|
| Polinómica simple | 19 | 11 | 6 | 3 | 2 | 2 |
| Polinómica doble | — | — | 100 (F) | 14 | 10 | 1 |
| Logarítmica | 19 | 4 | 13 | 3 | 3 | 3 |
| Exponencial | 18 | 6 | 20 | 3 | 2 | 2 |
| Trigonométrica | 19 | 5 | 32 | 3 | 3 | 3 |
| Mixta | 17 | 4 | 100 (F) | 3 | 2 | 2 |

Como podemos ver, en todos se estableció como ganador a los metodos de Newton Raphson. La razón de esto es por la información que maneja cada método. 

El método de la Bisección solo sabe si la función cambia de signo, obteniendo solamente 1 dígito de precisión en cada iteración, por ello es el que converge en más iteraciones. De la misma forma funcionan el método de Falsa Posición junto a Punto Fijo puesto que estos dependen de la recta secante o la función g respectivamente, avanzando poco a poco. El método de la secante es mucho más rápida dado a que se tienen 2 puntos de referencia. Y finalmente los métodos de Newton Raphson son mucho más rápidos ya que aprovechan la derivada de la función.

---

## 3. ¿Qué orden de convergencia tiene cada método y cómo se refleja en el gráfico |error| vs iteración?

Los órdenes que observamos:

| Método | Orden | Cómo se ve en el gráfico log |
|---|---|---|
| Bisección | Lineal | Recta con pendiente constante |
| Falsa posición | Lineal | Recta, un poco más empinada que bisección |
| Punto fijo | Lineal (factor \|g'\|) | Recta de pendiente suave |
| Secante | Superlineal (~1.618) | Curva que se va empinando |
| Newton-Raphson | Cuadrático (raíz simple) | Caída muy abrupta al final |
| Newton mejorado | Cuadrático | Caída aún más abrupta |

Lo que pasa aquí es que el gráfico se encuentra en escala logaítmica, por ende la convergencia lineal se ve como una línea recta, mientras que la cuadrática es mucho más empinada, ya que obtiene dos dígitos significativos extra en cada iteración.

Se ve clarísimo comparando los gráficos que la bisección es una recta pareja que baja de a poquito, y al lado el Newton y el Newton mejorado son dos o tres puntos que bajan de golpe. El de Newton incluso llega a errores del orden de 1e-13, cosa que un método lineal no consigue en tan pocos pasos.

---

## 4. ¿Qué métodos requieren un intervalo con cambio de signo y cuáles no?

- Sí lo requieren (métodos cerrados): Bisección y falsa posición. Ambos parten de un intervalo [a, b] y necesitan f(a)·f(b) < 0 para "encerrar" la raíz. Si no hay cambio de signo, técnicamente no se puede saber de dónde partir.
- No lo requieren (métodos abiertos): Punto fijo, secante y Newton Raphson. Estos parten de una o dos estimaciones y se van acercando, pero no garantizan nada, pueden converger a otra raíz o directamente escaparse.

La demostración está en la función de raíz doble (x − 2)². Como la curva solo toca el eje, no hay cambio de signo y nuestra bisección y falsa posición detectan esto y devuelven "No aplica", por ende no es que fallen, es que no se pueden aplicar.

---

## 5. En la función que toca el eje x (raíz doble): ¿qué métodos fallan o no aplican y cuál se comporta mejor?

Los resultados en (x − 2)²:

| Método | Resultado | Iteraciones | Error final |
|---|---|---|---|
| Bisección | No aplica | — | — |
| Falsa posición | No aplica | — | — |
| Punto fijo | Falla | 100 | 4.58e-02 |
| Secante | Converge (lento) | 14 | 7.19e-04 |
| Newton-Raphson | Converge (lento) | 10 | 7.81e-04 |
| Newton mejorado | Converge | 1 | 0.00e+00 |

Viendo esto podemos concluir:

- Bisección y falsa posición no aplican, porque no hay cambio de signo.
- Punto fijo falla. Elegimos g(x) = x + 0.2(x − 2)². La condición para que el punto fijo converja es |g'(raíz)| < 1, y acá g'(x) = 1 + 0.4(x − 2), o sea g'(2) = 1 exactamente. Queda justo en el límite y en las 100 iteraciones ni se acerca.
- Secante y Newton convergen, pero lentito y con poca precisión. En una raíz doble la derivada se anula en la raíz, y eso le quita a Newton su orden cuadrático: pasa a converger linealmente. Además, como el error en x es cuadrático en f cerca de la raíz, el criterio |f(xₙ)| < 1e-6 se cumple cuando x todavía está a aprox. 8e-4 de la raíz. Por eso quedan marcados "Convergió" con un error real del orden de 1e-4. Llegado al tope de precisión que la raíz doble permite con ese criterio.
- El Newton mejorado se comporta muchísimo mejor: converge en 1 iteración con error 0. La razón es que su fórmula equivale a aplicar Newton sobre f/f' en lugar de sobre f. En una raíz doble, f/f' = (x−2)/2 es una recta, y Newton le pega a una recta en un solo paso, tomando todo mucho más simple.

---

## 6. ¿Cómo influyen el intervalo inicial y la estimación inicial en la cantidad de iteraciones y en si el método converge?

Notamos tres cosas:

- En bisección, manda el ancho del intervalo. El número de iteraciones depende casi solo de [a, b], porque con ancho 1 salen 19–20 iteraciones, y en la Mixta (ancho 0.9) salieron 17. Achicar el intervalo ayuda, pero hasta cierto punto, porque siempre es lineal.
- En punto fijo, manda la función g que uno elige. Se nota en la enorme diferencia de iteraciones. Cambiar g por otra puede cambiar por completo el resultado.
- En secante y Newton, mientras más cerca de la raíz esté la estimación inicial, menos iteraciones. Ambos andan muy bien cerca de la raíz, pero son métodos abiertos, o sea, que una estimación mala puede hacerlos converger a otra raíz o alejarse.

---

## 7. ¿Qué método recomiendan según el tipo de función, considerando velocidad y robustez?

Nuestra recomendación, resumiendo lo que vimos:

- Si se puede calcular la derivada, enseguida Newton-Raphson, y si sospechamos raíz múltiple, el Newton mejorado. Son los que menos iteraciones piden y los más precisos en raíces simples.
- Si se necesita un resultado garantizado entonces bisección. Es más lento, pero siempre que haya cambio de signo va a converger.
- Si se quiere un punto medio, la falsa posición. Mantiene el intervalo cerrado pero converge más rápido que la bisección.
- Punto fijo lo usaríamos con cuidado, solo cuando tengamos una g con |g'| < 1 garantizado cerca de la raíz.

---

## 8. Conclusión

**Qué método elegir según el tipo de función?** Para funciones suaves donde tenemos la derivada nos quedamos con Newton Raphson (y con el mejorado cuando hay una raíz múltiple), porque en todas ellas se resolvió en 2–3 iteraciones frente a las 19 de la bisección. La bisección la dejamos para irnos a la segura, porque es lenta pero no falla mientras exista cambio de signo. La falsa posición es como un punto intermedio.

**Qué pasó en la raíz doble y qué nos enseña?** Fue el caso que más nos hizo pensar, porque muestra que tener raíz no es lo mismo que cambiar de signo. La función (x − 2)² sí tiene raíz, pero la toca sin cruzar, y eso deja fuera a la bisección y a la falsa posición, que dependen meramente del signo. Además, a los métodos que sí aplican les cuesta, por ejemplo el punto fijo divergió, y Newton y secante bajaron su orden cuadrático a lineal por culpa de la derivada que se anula. El que se salvó fue el Newton mejorado, que en una iteración llegó a la raíz exacta, porque al trabajar sobre f/f' convierte la raíz doble en una raíz simple. En conclusión: Tener raíz no basta para que todos los métodos sirvan, pues hay que fijarse también en cómo la curva se comporta cerca de ella.

**Cómo cambió el número de iteraciones al mover el intervalo o la estimación inicial?** Se notó sobre todo en los métodos lineales y en el punto fijo. En bisección el número de iteraciones quedó amarrado al ancho del intervalo (17 a 20 según la función), y en punto fijo varió de 6 a 32 iteraciones (y hasta falló en la Mixta) solo por cómo quedaba la g elegida. Los métodos de Newton fueron mucho más estables frente a distintos puntos de partida, siempre que la estimación no estuviera demasiado lejos de la raíz.

---