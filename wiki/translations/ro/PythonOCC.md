# PythonOCC/ro
## Description

[PythonOCC](PythonOCC.md) is a project that aims at providing the entire range of [OpenCASCADE Technology](OpenCASCADE.md) (OCCT) functions through the [Python](Python.md) module `OCC`. This is a different approach from FreeCAD\'s, where only certain components of OCCT are exposed through the [Part Workbench](Part_Workbench.md).

PythonOCC, on the other hand, provides access to all OCCT classes and functions so it is complex but also very powerful. Therefore, when you are limited by FreeCAD\'s OCCT functionality, using `OCC` is a good alternative.

## Usage

The [Part Workbench](Part_Workbench.md) has the methods `Part.__toPythonOCC__()` and `Part.__fromPythonOCC__()` to exchange `TopoDS_Shape` ([Part TopoShape](Part_TopoShape.md)) entities to and from PythonOCC. These methods allow us to use the full power of OCCT in Python and then put the resulting shapes back into FreeCAD objects.

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

[Category:Developer Documentation](Category:Developer_Documentation.md) [Category:Python Code](Category:Python_Code.md)

---
[documentation index](../README.md) > [Developer Documentation](Category:Developer Documentation.md) > PythonOCC/ro
