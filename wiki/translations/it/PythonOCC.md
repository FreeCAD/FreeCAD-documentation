

## Description


<div class="mw-translate-fuzzy">

[PythonOCC](http://www.pythonocc.org/) è un progetto abbastanza giovane e dinamico che mira a unire la gamma di funzioni di OpenCascade in un modulo python. Questo è un metodo molto differente da quello di FreeCAD, che utilizza solo alcuni componenti di OpenCascade, e che risulta una struttura molto più semplice.


</div>


<div class="mw-translate-fuzzy">

PythonOCC, d\'altra parte, dato che fornisce l\'accesso a tutte le classi e funzioni OCC, è molto complesso, ma è anche molto potente. È quindi una bella aggiunta a FreeCAD. Quando si è limitati dalle funzionalità OCC disponibili in FreeCAD per gli script python, è il momento di caricare pythonOCC.


</div>

## Usage


<div class="mw-translate-fuzzy">

Attualmente nel modulo Parte abbiamo i metodi: **Part.\_\_toPythonOCC\_\_()** e **Part.\_\_fromPythonOCC\_\_()** per scambiare entità TopoDS\_Shape da o per pythonOCC. Questo permette di utilizzare tutta la potenza di OCC in python (con pythonocc) e poi di mettere nuovamente le forme risultanti in FreeCAD.


</div>

PythonOCC is internally used by the [IFC](Arch_IFC.md) viewer included with the [IfcOpenShell](IfcOpenShell.md) libraries. IfcOpenShell is used to read and write [IFC](Arch_IFC.md) documents with FreeCAD. PythonOCC is only needed to launch IfcOpenShell\'s integrated viewer, otherwise it is not necessary.

## Installation

PythonOCC must be compiled from source. For this you need to get the corresponding development files for [OpenCASCADE Technology](OpenCASCADE.md) (OCCT) and SWIG. The older version of PythonOCC was intended to wrap around OCE 0.18, the community edition of OCCT 6.9.x, which is now unmaintained. The newest version of PythonOCC is now intended to work with the recent, official OCCT 7.4 version.

Together with OCCT 7.4, PythonOCC requires fairly recent dependencies like Python 3.7, CMake 3.12, and SWIG 3.0.11. Python 2 is no longer supported.

It is also possible to install pre-compiled PythonOCC libraries using [Conda](Conda.md). For more information and compilation instructions, see the main project\'s repository, [tpaviot/pythonocc-core](https://github.com/tpaviot/pythonocc-core).

## Compilation

You can also self compile pythonOCC (see [instructions](https://github.com/tpaviot/pythonocc-core/blob/master/INSTALL.md)). Below is the procedure for Debian/Ubuntu using distro-provided opencascade packages:

    git clone git://github.com/tpaviot/pythonocc-core.git pythonocc
    cd pythonocc
    mkdir build
    cd build
    cmake -DOCE_INCLUDE_PATH=/usr/include/opencascade -DOCE_LIB_PATH=/usr/lib/x86_64-linux-gnu ..
    make

## More information 

-   Project page: [pythonocc.org](http://www.pythonocc.org/)
-   Newer version compatible with OCCT 7.4, [tpaviot/pythonocc-core](https://github.com/tpaviot/pythonocc-core).
-   Older version compatible with OCE 0.18, the community edition of OCCT 6.9.x, [tpaviot/pythonocc](https://github.com/tpaviot/pythonocc).
-   [IfcPlusPlus compiled on Gentoo - questions and alternatives?](https://forum.freecadweb.org/viewtopic.php?f=39&t=33254)


{{Powerdocnavi

}} 

[Category:Developer Documentation{{\#translation:}}](Category:Developer_Documentation.md) [Category:Python Code{{\#translation:}}](Category:Python_Code.md)
