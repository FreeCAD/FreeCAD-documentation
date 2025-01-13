# Conda/es
## Introducción




Esta página tiene como objetivo presentar a Conda como gestor de paquetes, dependencias y administrador ambiente para FreeCAD.

Actualmente, esta página cataloga principalmente los enlaces a los debates pertinentes del foro de FreeCAD y otros lugares de la web, pero se espera documentar los puntos más destacados de esos enlaces en esta página.

See also a [video tutorial](https://www.youtube.com/watch?v=sCs8xlrw2nM) of the contents of this page



## Motivación

La motivación para usar Conda es múltiple, como lo es el propósito de Conda.

Vamos a desglosarlo.



### Conda como un administrador de paquetes 

En primer lugar, Conda es un gestor de paquetes, similar a apt o pip.

Esto significa que podemos instalar *paquetes* con un simple conda install de varios [canales](https://docs.conda.io/projects/conda/en/latest/user-guide/concepts/channels.html#what-is-a-conda-channel) como [conda-forge](https://conda-forge.org/).

Conda Forge es análogo a [the Python Package Index (PyPI)](https://pypi.org/), un canal comunitario formado por miles de colaboradores, y sirve [freecad](https://anaconda.org/conda-forge/freecad) como un paquete de conda.



### Conda como un Gerente de la dependencia 

En primer lugar, Conda es un gestor de dependencia, también similar a apt o pip.

Conda puede manejar las dependencias e instalar las dependencias para un proyecto como FreeCAD.

¿Por qué no usar pip? pip funciona muy bien para manejar las dependencias de los proyectos que *sólo* usan pitón.

Conda funciona para múltiples lenguajes, y por lo tanto es más adecuado para gestionar las dependencias de proyectos como FreeCAD que tienen dependencias a través de una variedad de lenguajes como C / C++ y Python.



### Conda como un Gerente d\'Ambiente 

Conda tiene el concepto de un [Ambiente](https://docs.conda.io/projects/conda/en/latest/user-guide/concepts/environments.html) que es la combinación única de paquetes y versiones necesarias para ejecutar una pieza de software. Por ejemplo, un ambiente de trabajo FreeCAD.

Con los entornos, puedes fácilmente \"activarlos\" y \"desactivarlos\", o cambiar entre las versiones de los paquetes necesarios para determinadas piezas de software.

Esto es útil para probar cómo se comporta un ambiente de trabajo con un conjunto particular de paquetes. Por ejemplo, ¿cómo se comporta un ambiente de trabajo en FreeCAD 18.4 vs 19?

Los entornos de Conda permiten reproducir exactamente el mismo entorno en diferentes máquinas.

Por ejemplo, múltiples máquinas de desarrollo local, o un servidor de construcción remoto alojado por Travis CI.



## Instalación de Conda 

1\. [Instalar Miniconda](https://docs.conda.io/en/latest/miniconda.html).

2\. Verifique que su instalación fue exitosa y familiarícese con el conda *CLI*. 

## Instalando FreeCAD usando Conda 


<div class="mw-translate-fuzzy">

Primero, debes decidir si quieres instalar una versión *estable* de FreeCAD, o experimentar con el último código *inestable* de FreeCAD master.


</div>


<div class="mw-translate-fuzzy">

Las versiones estables de FreeCAD se sirven en el canal conda-forja, mientras que la última de FreeCAD maestro se sirve en el canal freecad/label/dev.


</div>

  Canal Conda           Estable?
   
  conda-forge         Si ✔️
  freecad/label/dev   No ❌

En segundo lugar, ya que se pueden crear fácilmente ambientes dedicados en conda, se recomienda crear uno para FreeCAD.

El crear comando permite crear un entorno a partir de una lista de paquetes especificados. En nuestro caso, queremos crear un entorno llamado \"fcenv\" (abreviatura de entorno FreeCAD) a partir del paquete freecad, y decirle a conda que busque el paquete freecad usando el canal conda-forge. 
```python
conda create --name fcenv --channel conda-forge freecad
```conda que siempre busque conda-forja al instalar paquetes con el siguiente comando: 
```python
conda config --add channels conda-forge
```freecad/label/dev así: 
```python
conda create --name fcenv-dev --channel freecad/label/dev freecad
```



## Discusión en el foro de FreeCAD 

-   [Hablemos de Conda](https://forum.freecadweb.org/viewtopic.php?t=39656)
-   [Solución de embalaje: (ana)conda](https://forum.freecadweb.org/viewtopic.php?f=10&t=15197)
-   [FreeCAD Conda Distribución](https://forum.freecadweb.org/viewtopic.php?f=8&t=45582)



## Ver también 

-   <https://docs.conda.io/en/latest/>
-   <https://conda-forge.org/docs/>
-   <https://docs.conda.io/projects/conda-build/en/latest/>
-   <https://anaconda.org/conda-forge/freecad>
-   <https://anaconda.org/freecad/freecad>
-   <https://github.com/FreeCAD/FreeCAD_Conda>
-   <https://github.com/FreeCAD/FreeCAD-AppImage>



---
⏵ [documentation index](../README.md) > [Developer_Documentation](Category_Developer_Documentation.md) > [Developer](Category_Developer.md) > Conda/es
