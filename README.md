# **<center>Grupo 1: Los Huaqueros de Eldlich The Golden Lord 2020-I ALGORITMOS PARALELOS Y DISTRIBUIDOS</center>**
### Datos Academicos

- **Universidad:** Universidad Nacional de San Antonio Abad del Cusco
- **Facultad:** Facultad de ingenieria electrica, electronica, informatica y mecanica
- **Escuela Profesional:** Ingenieria Informatica y de Sistemas
#### Ingeniera:
- **Quintanilla Portugal Roxana Lisette**
#### Trabajo:
- Documentar y entender un programa paralelizable.
- Elegimos un programa y lo ejecutamos en google colaboratory
#### Colaboradores:
- **GABRIELA FARFAN ENRIQUEZ** [Gabi](https://github.com/gabrielafarfan1)
- **SEBASTIAN ISRAEL MACEDO GHEILER**  [Sebas](https://github.com/sebasmacedohotmailcom)
- **VICTOR URQUIZO CARBAJAL** [Victor](https://github.com/victorUrquizo)
- **HUAHUATICO SORIA RONALD** [Romehe](https://github.com/Romehe369)
- **NAOMI ISABEL MASIAS USCAMAYTA** [Naomi](https://github.com/naomi159)
- **IVAN ARTHUR QUISPE HUARHUA** [Ivan](https://github.com/ivan-qh)
- **MICHAEL ANTONNI MAMANI QUINTA** [Antoni](https://github.com/Michael-Antonni)
- **FRANK EDISON PUMAYALLI CUSICUNA** [Frank](https://github.com/frankpumacusi)
---
## Tema

.Programa que soluciona un sudoku nxn, con un algoritmo de backtraking.

### Implementado en:
- Lenguaje:C++ and Python
[Obtener C++](https://visualstudio.microsoft.com/es/thank-you-downloading-visual-studio/?sku=Community&rel=16)
[Obtener Python](https://www.python.org/downloads/)
- Editor: Visual Studio Code and Google Colab
[Ir a Colab](https://colab.research.google.com/notebooks/intro.ipynb)
[Obtener Visual Studio Code](https://code.visualstudio.com/download)
### Enlace de diario personal
-[Documento de Presentacion](https://docs.google.com/presentation/d/1e4iR5D2NYpV1ujiJVhsh8q3OvkaRal6wfqB3RgLqrEc/edit?usp=sharing)
### Descripcion del problema
Supongamos que tenemos una cuadrícula de Sudoku y tenemos que resolver este famoso problema de laberinto de números, Sudoku. Sabemos que el Sudoku es una cuadrícula de números de N x N, y toda la cuadrícula también se divide en cuadros de sqrt(N) x sqrt(N). Hay algunas reglas para resolver el Sudoku.
Tenemos que usar los dígitos del 1 al N para resolver este problema.

-No se puede repetir un dígito en una fila, una columna o en una casilla de sqrt(N) x sqrt(N).

Usando el algoritmo de Bractraking paralelo intentaremos resolver el problema de Sudoku. Cuando alguna celda se llena con un dígito, comprueba si es válido o no. Cuando no es válido, busca otros números. Si se marcan todos los números del 1 al N y no se encuentra ningún dígito válido para colocar, retrocede a la opción anterior. Y finalmente se intentara con todas las opciones posibles. Caso que no se encuentre ninguna solucion el programa nos enviara un mensaje de que "No existe Solucion"

#### ¿Porque paralelizamos y Como?
Paralelisamos porque nuestro algoritmo se demora en resolver programas complejos
