# Compiling (Speeding up)/ro
{{TOCright}}

## Overview


<div class="mw-translate-fuzzy">

Atunci când dezvoltați FreeCAD, trebuie să compilați din surse, iar faza de compilare / construire poate începe să mînânce un timp valoros din timpul de dezvoltare. Iată câteva sfaturi pentru a scurta acest proces și a face timpul de compilare/construcție mai eficient.


</div>

## CCache


<div class="mw-translate-fuzzy">

### CCache 

Instalează ccache în compilările cache


</div>

[Ccache](https://ccache.dev/) speeds up recompilation by caching previous compilations and detecting when the same compilation is done again. Ccache is free software, released under GPLv3 or later.

On most systems ccache will be automatically detected and enabled, you can use the `FREECAD_USE_CCACHE` `cmake` option to control this behavior.

## Disable modules 


<div class="mw-translate-fuzzy">

### Dezactivarea modulelor 

Utilizați cmake-curses-gui, cmake-qt-gui sau flag cmake pentru a dezactiva modulele pe care nu lucrați


</div>

For example, to avoid building the FEM and Mesh workbenches:


```python
cmake -DBUILD_FEM=OFF -DBUILD_MESH=OFF ../freecad-source
```

Use `cmake-gui`, `cmake-curses-gui`, or `cmake-qt-gui` to display all the possible variables that can be edited in the configuration; using these interfaces you can easily switch on or off different workbenches.

## Number of jobs in parallel 


<div class="mw-translate-fuzzy">

### make -j 

Utilizați -j \# pentru a specifica numerul sarcinilor/jobs. O sugestie ar fi, numărul de nuclee de pe computer, e.g.

    make -j $(nproc)


</div>

Run four compilation commands in parallel:


```python
make -j4
```

Compile as many files in parallel as the number of CPU cores in your system. This is useful if you have many cores and want to use them all to compile the software.


{{code|code=
make -j$(nproc)
}}

Compile as many files in parallel as the number of CPU cores in your system, minus two. Use this so that your system is still responsive to do some other task; for example, two cores will allow you to use a browser, while the rest of the cores keep compiling the software on the background.


{{code|code=
make -j$(nproc --ignore=2)
}}

## distcc


<div class="mw-translate-fuzzy">

### distcc 

Distcc poate fi utilizat pentru compilarea distribuită în rețea.


</div>

[Distcc](https://www.distcc.org/) should always generate the same results as a local compilation. It is free, simple to install and use, and often two or more times faster than compiling locally.

FreeCAD dev \'etrombly\' has published a short explanation on [how to install distcc to compile FreeCAD on a network of computers using Docker](https://forum.freecadweb.org/viewtopic.php?f=4&t=50810&p=459142#p458614).



---
![](images/Right_arrow.png) [documentation index](../README.md) > [Developer_Documentation](Category_Developer_Documentation.md) > [Developer](Category_Developer.md) > Compiling (Speeding up)/ro
