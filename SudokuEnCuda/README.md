: ¿Desea pedir? *
### Solucionador de Sudoku
Esta es una implementación de sudoku-solver codificada en tres días para tareas de clase GPU.

`` bash
nvcc -arch sm_35 -rdc = true -o sudokusolver sudokusolver.cu
./sudokusolver inp.in
''
Lo cual imprimirá la salida estándar y guardará los resultados de 95 sudoku muy difíciles en el archivo inp.sol __en menos de 2 segundos .__


La entrada debe tener la siguiente forma. Puede agregar muchos problemas, separando la línea 9 con un espacio.
''
400000805
030000000
000700000
020000060
000080400
000010000
000603070
500200000
104000000
''

## Sudoku paralelo
es difícil. La solución de cpu más popular es el retroceso, que se basa en el retroceso y la recursividad, y la recursividad no es eficiente ni complicada en las GPU.

[Esta página web] (https://www.sudoku-solutions.com/) es realmente agradable para mejorar sus habilidades de sudoku y tiene la funcionalidad "Ver pasos" para ver la lógica detrás de la solución. Hay muchas reglas que se pueden aplicar en un estado para llenar celdas de forma determinista. Como me interesa la paralización del problema, no implementé estas reglas. Me he centrado en paralelizar e implementar solo la lógica básica. La lógica básica es esta:
1. Para cada celda (de 81), si está vacía, averigüe el conjunto de dígitos que no se utilizan en la fila, columna o grupo de celdas al que corresponde la celda. Este conjunto es el conjunto de posibilidades de cada celda.
2. Si el conjunto está vacío, esta configuración / placa no es válida (lo que puede suceder como resultado de una suposición incorrecta)
3. Si el conjunto consta de un solo elemento, llene la celda con el único valor posible.
4. Si hay más de un dígito en el conjunto, no hacemos nada.

Seguimos repitiendo este proceso hasta que resolvemos el sudoku o el progreso se detiene. Cuando no hay progreso, programamos una bifurcación:
1. Encuentra el número de dígitos en el conjunto más pequeño.
2. De las celdas con conjuntos más pequeños, elija la que tenga un ID de subproceso más pequeño.
3. Bifurque la celda generando nuevos tableros para cada valor posible de la celda. Cada placa obtiene un valor diferente para la celda y comienzan a aplicar nuestra lógica simple en las placas bifurcadas en paralelo.

Sí, el problema aquí es cómo bifurcar. Las GPU tienen cierta capacidad de recursividad y asignación dinámica, pero siempre es mejor asignar al principio y eso es lo que hago.

## Optimizaciones y resultados
Actual:
- Asignación estática con 50000 bloques (se observa que es suficiente para todos los ejemplos difíciles)
- Máscaras de bits para reducir el almacenamiento.

Futuro:
- Comparta mejor la tarea de generación de máscaras de bits dentro del bloque.

## Qué hace cuda-sudoku-solver.
El kernel `controller` es el kernel principal que llama a` fillSudokuSafeAndFork` repetidamente hasta que se encuentra una solución.
El programa tiene algunos valores predeterminados como #blocks y #threads.
- `# threads`: 96 = 32 * 3 que es el múltiplo más pequeño de 32 que es mayor que 81. #todo Podemos hacer 81 aquí y eliminar las declaraciones if.
- `# blocks`: solucionadores disponibles. Cada bloque trabaja en su propio bloque.
- ʻarr_dev`: tiene #bloques de muchos tableros y uno extra para la solución.
- `block_stat`: tiene el estado de cada bloque. Si es 0, el bloque está inactivo / disponible. Si es 1, entonces está activo, trabajando en una solución. Si el último elemento de block_stat (block_stat [nBlocks]) es igual a 2, tenemos una solución lista en el último elemento 81 de ʻarr_dev`.

** fillSudokuSafeAndFork ** es un núcleo bastante largo (podría dividirse en subnúcleos), los siguientes pasos se realizan en orden:
1. El bloque 0 comprueba si hay errores, detiene el proceso si no hay ningún bloque activo. Esto no debería suceder.
2. Cada bloque activo calcula máscaras binarias de filas, columnas y grupos de celdas (9 bits). El uso de máscaras binarias reduce el requisito de memoria compartida.
3. Cada subproceso se empareja con una celda de sudoku y cada subproceso calcula sus posibilidades aplicando OR a sus máscaras correspondientes. El resultado es el conjunto de valores posibles (ceros en la máscara binaria).
4. 2 y 3 repetidos hasta que no se avance.
5. después del bucle
  - si ** done_flag **, entonces copiamos el resultado en el lugar de resultados y establecemos las `stats [nBlocks]` en 2.
  - si ** error_flag **, el bloque actual es incorrecto, por lo que detectamos y establecemos la estadística en 0, por lo que el bloque se puede reprogramar.
  - si no hay ** progress_flag **, entonces necesitamos bifurcar.
    1. Usando instrucciones atómicas, elija una celda con múltiples posibilidades. Después de este punto, solo funciona el hilo correspondiente.
    2. La primera posibilidad se queda con el bloque. Para los dígitos restantes, haga una búsqueda para encontrar un bloque disponible y copie el bloque actual en el almacenamiento global new_blocks. Ahora, en la próxima iteración, los nuevos bloques trabajarán en diferentes posibilidades.