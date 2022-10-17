# Compiling (Speeding up)/es
{{TOCright}}

## Vista general 

FreeCAD es una gran aplicación que puede tardar entre 10 minutos y una hora en compilarse completamente desde el código fuente. Esto depende principalmente de la CPU que tengas, y del número de núcleos que se utilicen en el proceso de compilación. Aquí hay algunos consejos para acortar ese proceso y hacer que los tiempos de compilación sean más cortos.

## CCache

Instalar `ccache` para almacenar en caché las construcciones.

## Desactivar módulos 

Cuando se utiliza `cmake` para configurar la compilación, se puede deshabilitar la compilación de ciertos bancos de trabajo que no se necesitan en este momento. Esto es útil si sólo necesita probar algunos ambientes de trabajo.

Por ejemplo, para evitar la construcción de los ambientes de trabajo FEM y Malla   *


```python
cmake -DBUILD_FEM=OFF -DBUILD_MESH=OFF ../freecad-source
```

Utiliza `cmake-gui`, `cmake-curses-gui`, o `cmake-qt-gui` para mostrar todas las posibles variables que se pueden editar en la configuración; utilizando estas interfaces puedes activar o desactivar fácilmente diferentes ambientes de trabajo.

## Número de trabajos en paralelo 

Después de la configuración con `cmake`, el programa `make` lanza el compilador C++ real para trabajar en los archivos de código fuente. Se puede acelerar la compilación trabajando en varios archivos al mismo tiempo. Esto se consigue con la opción `-j` de `make`, que denota el número de \"trabajos\" o comandos de compilación que se ejecutan simultáneamente. Esta opción es un número entero.

Ejecuta cuatro comandos de compilación en paralelo   *


```python
make -j4
```

Compilar tantos archivos en paralelo como el número de núcleos de la CPU en su sistema. Esto es útil si tienes muchos núcleos y quieres usarlos todos para compilar el software.


{{code|code=
make -j$(nproc)
}}

Compila tantos archivos en paralelo como el número de núcleos de la CPU de tu sistema, menos dos. Usa esto para que tu sistema siga respondiendo para hacer alguna otra tarea; por ejemplo, dos núcleos te permitirán usar un navegador, mientras el resto de los núcleos siguen compilando el software en segundo plano.


{{code|code=
make -j$(nproc --ignore=2)
}}

## distcc

El programa `distcc` puede utilizarse para realizar la compilación distribuida de código C y C++ en varias máquinas de una red.







[Category   *Developer_Documentation](Category_Developer_Documentation.md) [Category   *Developer](Category_Developer.md)



---
![](images/Right_arrow.png) [documentation index](../README.md) > [Developer_Documentation](Category_Developer_Documentation.md) > [Developer](Category_Developer.md) > Compiling (Speeding up)/es
