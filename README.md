# Proyecto 1 ADA II :rocket:

## Descripción :page_facing_up:

### Moderando el Conflicto Interno de Opiniones en una Red Social (ModCI)

Este proyecto consiste en aplicar tres estrategias algorítmicas (fuerza bruta, voraz y programación dinámica) para moderar el conflicto interno de opiniones en una red social. Cada grupo de agentes tiene opiniones cuantificadas sobre dos afirmaciones y un nivel de rigidez que determina qué tan fácil es cambiar su opinión. El objetivo es aplicar una estrategia de moderación que reduzca el conflicto interno de la red social sin sobrepasar un presupuesto de esfuerzo.

Este ejercicio académico permite comparar distintas estrategias de resolución de problemas combinatorios, analizar su rendimiento, y construir una herramienta interactiva para visualizar y probar soluciones.

---

## Instrucciones para ejecutar el código :computer:

> ⚠️ Este proyecto utiliza código fuente en Python para la lógica y una interfaz gráfica con Tkinter para la carga, visualización y ejecución de estrategias.

### 1. Clonar el repositorio

```bash
git clone https://github.com/Heisuzul/proyectoIADA.git
cd proyectoIADA
```

---

### 2. Ejecutar la interfaz en Python

#### Requisitos:
- Python 3.x
- Tkinter (ya incluido con Python en la mayoría de distribuciones)

```bash
cd src/interfaz
python interfaz.py
```

---

### 3. Estructura del proyecto

```
proyectoIADA/
│
├── data/
│   ├── BateriaPruebas/           # Carpeta con 30 archivos de entrada para pruebas
│   │   ├── Prueba1.txt
│   │   ├── Prueba2.txt
│   │   ├── ...
│   │   └── Prueba30.txt
│   ├── entrada.txt               
│   └── entrada2.txt              
│
├── src/
│   ├── data/                     
│   ├── logica/                   
│   │   ├── modciFB.py            # Algoritmo de Fuerza Bruta
│   │   ├── modciPD.py            # Algoritmo de Programación Dinámica
│   │   ├── modciV.py             # Algoritmo Voraz
│   │   └── utils.py              # Funciones auxiliares: lectura, esfuerzo, CI, etc.
│   └── vista/
│       └── interfazRS.py         # Interfaz gráfica en Tkinter para ejecución y visualización
│
├── tests/
│   ├── outputs/                  # Salidas generadas por cada algoritmo a partir de cada prueba
│   │   ├── salida_FB_Prueba1.txt
│   │   ├── salida_PD_Prueba30.txt
│   │   └── ...
│   └── __init__.py              # Inicializador para pruebas automáticas
│
├── Enunciado.pdf                 # Documento oficial del proyecto
├── README.md                     # Instrucciones de instalación, uso y créditos del proyecto


```

---

### 4. Formato de los archivos

#### Entrada (`data/entrada.txt`)
```
3
3, -100, 50, 0.5
1, 100, 80, 0.1
1, -10, 0, 0.5
80
```

#### Salida (`data/salida_FB.txt`, `salida_V.txt`, `salida_PD.txt`)
```
15166.66
75
1
0
0
```

---

### 5. Ejecutar solo lógica (opcional)

Si deseas correr únicamente los algoritmos desde consola para pruebas rápidas:

```bash
cd src/logica
python modciFB.py
python modciV.py
python modciPD.py
```

---

## Institución :mortar_board:

- **Universidad:** Universidad del Valle, Cali, Colombia.
- **Curso:** Análisis y Diseño de Algoritmos II
- **Semestre:** 2025-01

---

## Contribuyentes :busts_in_silhouette:



- [Mina Garcia, Heidy](https://github.com/Heisuzul) - 201931720
- [Mosquera Zapata, Wilson Andrés](https://github.com/andresengineer) - 202182116
- [Ortiz Alvarez, Hassen David](https://github.com/hassen2208) - 20
- [Rodriguez Marulanda, Alejandro](https://github.com/Alejand2r) - 202042954
