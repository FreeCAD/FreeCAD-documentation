# Exposing Cplusplus to Python
**This documentation is a stub and needs more work, perhaps a written example + links to commits demonstrating in the commit history**

## How to expose c++ functionality to Python 

It becomes necessary at times to expand the FreeCAD API further by exposing functions that are available in the source code in c++ to the python. In so doing, providing an ability to trigger deep internal functionality with Python in real-time instead of needing to compile.

Below is an explanation of how one can achieve this.

The basic structure of a program to expose functionality to Python is something like this:

-   get the Py object parameters and convert them to c++ variables using PyArg_ParseTuple(),
-   use various c++ routines from **OpenCascade** and/or **FreeCAD** to produce the desired result,
-   convert the c++ result into Py object using routines like PyLong_AsLong(), Py::asObject(), etc,
-   return the Py object.

### Further Elaboration 

There are two source files required to implement a new Python binding. Assuming we wanted to expose some methods from [FreeCAD/src/Mod/Part/TopoShape.cpp](https://github.com/FreeCAD/FreeCAD/blob/master/src/Mod/Part/TopoShape.cpp), we would need to make:

-   TopoShapePy.xml - definitions of the functions for be exposed in XML format. This file is used to generate header files for our next file\...
-   TopoShapePyImp.cpp - the actual C++ code that bridges from Python to C++.

These 2 files need to be added to **../Mod/yourModule/App/CMakeLists.txt**. See [FreeCAD/src/Mod/Part/App/CMakeLists.txt](https://github.com/FreeCAD/FreeCAD/blob/master/src/Mod/Part/App/AppPartPy.cpp) for an example.

You can extend the Python version of your module by adding to **../Mod/yourModule/App/AppmyModulePy.cpp** (see [FreeCAD/src/Mod/Part/AppPartPy.cpp](https://github.com/FreeCAD/FreeCAD/blob/master/src/Mod/Part/App/AppPartPy.cpp)). The additions are accessed in Python by \"import myModule\".

Note:

1.  xxxxxPyImp routines return a PyObject* pointer (see TopoShapePyImp.cpp)
2.  AppmyModulePy.cpp routines return a Py::Object (see [FreeCAD/src/Mod/Part/AppPartPy.cpp](https://github.com/FreeCAD/FreeCAD/blob/master/src/Mod/Part/App/AppPartPy.cpp)).

### Related Links 

-   Source: <https://forum.freecadweb.org/viewtopic.php?p=314796#p314617>
-   [Forum discussion: Adding Commands in Python to C++ Workbench](https://forum.freecadweb.org/viewtopic.php?p=560639#p560639)
-   [Workbench creation](Workbench_creation.md)



---
![](images/Right_arrow.png) [documentation index](../README.md) > Exposing Cplusplus to Python
