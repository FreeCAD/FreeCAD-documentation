

## Descripción


<div class="mw-translate-fuzzy">

[PythonOCC](PythonOCC/es.md) es un proyecto que tiene como objetivo proporcionar toda la gama de [Tecnología OpenCASCADE](OpenCASCADE/es.md) (OCCT) funciona a través del módulo [Python](Python/es.md) `OCC`. Este es una aproximción diferente al de FreeCAD, donde sólo ciertos componentes de OCCT son expuestos a través del [Ambiente de trabajo Piezas](Part_Workbench/es.md).


</div>

PythonOCC, por otro lado, proporciona acceso a todas las clases y funciones de OCCT, por lo que es complejo pero también muy potente. Por lo tanto, cuando estás limitado por la funcionalidad de OCCT de FreeCAD, usar `OCC` es una buena alternativa.

## Utilización


<div class="mw-translate-fuzzy">

El [Módulo de las Piezas](Part_Workbench/es.md) tiene los métodos `Parte.__aPythonOCC__()` y `Parte.__dePythonOCC__()` para intercambiar `TopoDS_Shape` ([Piezas TopoForma](Part_TopoShape/de.md)) entidades hacia y desde PythonOCC. Estos métodos nos permiten utilizar toda la potencia de OCCT en Python y luego poner las formas resultantes de nuevo en los objetos de FreeCAD.


</div>

PythonOCC es usado internamente por el visor [IFC](Arch_IFC/es.md) incluido en las librerías [IfcOpenShell](IfcOpenShell/es.md). IfcOpenShell se utiliza para leer y escribir documentos [IFC](Arch_IFC/es.md) con FreeCAD. PythonOCC sólo es necesario para lanzar el visor integrado de IfcOpenShell, de lo contrario no es necesario.

## Instalación

PythonOCC debe ser compilado desde la fuente. Para ello es necesario obtener los correspondientes archivos de desarrollo para [Tecnología OpenCASCADE](OpenCASCADE/es.md) (OCCT) y SWIG. La versión antigua de PythonOCC estaba destinada a envolver OCE 0.18, la edición comunitaria de OCCT 6.9.x, que ahora no se mantiene. La nueva versión de PythonOCC está pensada para trabajar con la reciente versión oficial de OCCT 7.4.

Junto con OCCT 7.4, PythonOCC requiere dependencias bastante recientes como Python 3.7, CMake 3.12, y SWIG 3.0.11. Python 2 ya no está soportado.

También es posible instalar bibliotecas precompiladas de PythonOCC usando [Conda](Conda/es.md). Para más información e instrucciones de compilación, ver el repositorio principal del proyecto, [tpaviot/pythonocc-core](https://github.com/tpaviot/pythonocc-core).

## Compilation

You can also self compile pythonOCC (see [instructions](https://github.com/tpaviot/pythonocc-core/blob/master/INSTALL.md)). Below is the procedure for Debian/Ubuntu using distro-provided opencascade packages:

    git clone git://github.com/tpaviot/pythonocc-core.git pythonocc
    cd pythonocc
    mkdir build
    cd build
    cmake -DOCE_INCLUDE_PATH=/usr/include/opencascade -DOCE_LIB_PATH=/usr/lib/x86_64-linux-gnu ..
    make

## Más información {#más_información}

-   Página del proyecto: [pythonocc.org](http://www.pythonocc.org/)
-   La nueva versión es compatible con la OCCT 7.4, [tpaviot/pythonocc-core](https://github.com/tpaviot/pythonocc-core).
-   Versión anterior compatible con OCE 0.18, la edición comunitaria de la OCCT 6.9.x, [tpaviot/pythonocc](https://github.com/tpaviot/pythonocc).
-   [IfcPlusPlus compilado en Gentoo - ¿preguntas y alternativas?](https://forum.freecadweb.org/viewtopic.php?f=39&t=33254)


{{Powerdocnavi

}} 

[Category:Developer Documentation{{\#translation:}}](Category:Developer_Documentation.md) [Category:Python Code{{\#translation:}}](Category:Python_Code.md)
