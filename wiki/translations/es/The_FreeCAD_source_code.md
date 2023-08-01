# The FreeCAD source code/es
El [código fuente de FreeCAD](https://github.com/FreeCAD/FreeCAD) se maneja con git, y es público, abierto y disponible bajo la [licencia LGPL](https://en.wikipedia.org/wiki/GNU_Lesser_General_Public_License). Puede ser copiado, descargado, leído, analizado, redistribuido y modificado por cualquiera. Si planeas hacer modificaciones que deseas que se incluyan en el propio código oficial, recuerda que tus cambios tendrán que ser aprobados por los desarrolladores de FreeCAD, por lo que es aconsejable discutir primero tus intenciones e ideas en el [forum](http://forum.freecadweb.org), para evitar el riesgo de que tus cambios sean rechazados por alguna razón que no hayas previsto.

A continuación encontrarás algunas pistas e información útil para ponerte al día si estás interesado en explorar el código de FreeCAD.

-   El código de FreeCAD está programado principalmente en *C++*, pero se basa en gran medida en *Python*. Una gran parte de su funcionalidad proporciona enlaces Python asociados, y es parte de la filosofía central del desarrollo de FreeCAD ofrecer siempre acceso a Python a cualquier nueva característica implementada en C++. Para conseguirlo, CPython (las herramientas de interfaz C proporcionadas por el propio Python) y especialmente [PyCXX](http://cxx.sourceforge.net/) son muy utilizadas en todo FreeCAD. Muchas plantillas y herramientas personalizadas también se proporcionan en el propio código de FreeCAD para facilitar la construcción de los enlaces de python asociados. Algunas partes de más alto nivel del código de FreeCAD están codificadas completamente en Python.

-   El código fuente de FreeCAD es totalmente *multi-plataforma*, y se tiene mucho cuidado de permitir el uso de la aplicación en el mayor número posible de plataformas y configuraciones, y no poner a los usuarios existentes en situaciones difíciles. Por lo tanto, en la medida de lo posible, se evitan las nuevas versiones de los componentes necesarios mientras no estén disponibles de forma amplia y fácil en todas las plataformas, y la compatibilidad con versiones anteriores (la posibilidad de abrir un archivo producido con una versión antigua de FreeCAD en una versión más reciente) es una prioridad importante.

-   Casi toda la funcionalidad de FreeCAD está separada en dos partes diferentes, llamadas *App* y *Gui*. Esta separación se refleja en todas partes en la estructura de archivos del código fuente. App contiene toda la funcionalidad que necesita para funcionar en modo de consola pura (sin GUI). Como FreeCAD puede compilarse y ejecutarse sin su interfaz gráfica de usuario, el código de App es independiente de cualquier biblioteca relacionada con la interfaz gráfica de usuario. Gui contiene todo el código necesario para ejecutarse en modo GUI, y está construido alrededor de la funcionalidad de la App.

-   Most of FreeCAD\'s functionality is implemented in **Modules**. FreeCAD without its module is a simple container window that can just open and save a file. All the geometry tools and workbenches are implemented in Modules. Modules can be written in C++, in Python, or combining the best of the two worlds. They can be hybrid C++/Python modules, where solid core functionality is programmed in C++ and end-user tools are written in Python making them easier to extend and adapt by FreeCAD users. Each module usually defines and creates a **Workbench** in the FreeCAD interface, when used in GUI mode, usually with the same name, but it is not mandatory for modules to contain a workbench.

-   FreeCAD modules often **depend on other modules**. Most modules that use solid geometry depend on the **Part** module, which is the most fundamental module of FreeCAD, and implements most of the interfacing with OpenCascade. Although other module can use OpenCascade functionality directly, they often rely on higher-level functions provided by Part.

-   Modules are always **initialized** from Python. Even if they are written fully in C++, they always contain a minimal Python/CPython structure.

-   FreeCAD is an avid user of **other open-source libraries**. Besides Python and Qt, used by the core and almost all of the modules, the two heavyweight libraries used throughout most modules are [OpenCascade Technology](https://en.wikipedia.org/wiki/Open_Cascade_Technology) (OCCT) and [Coin3D](http://www.coin3d.org/). OpenCascade is used to create and manage all the solid geometry of FreeCAD, while coin3D is used to manage the 3D view. OpenCascade is used mainly in the App world, and coin3D exclusively in the Gui world. A basic understanding of OpenCascade is fundamental to do any geometry-related work with FreeCAD. More specific modules make use of more specific libraries, and since there are usually no restrictions on that point apart from these libraries to be easily available on all platforms, the list of dependencies of a full FreeCAD installation with all its modules can be quite large.

-   FreeCAD\'s **document objects**, which are all the objects contained in a FreeCAD document, are what appear in the Tree View in the GUI and in FreeCAD.ActiveDocument.Objects() in Python. They may or may not have any geometrical data, and may or may not show anything in the 3D view. They are always separated in App and Gui parts. The Gui part is not loaded when running in console mode. Standard geometrical objects, such as those found in Part or PartDesign, have their OpenCascade-based geometry defined in their App counterpart, while the Gui counterpart (also usually called \"View Provider\") is responsible for creating a coin3D representation of that geometry, which will be inserted into the main coin3D scene graph of the 3D view.

-   The basic directory structure of the source code is organized like this:
    -   **App**: contains the FreeCAD console-mode application, defines basic structures and base classes for document objects, that are used by modules to build their own.
    -   **Base**: contains core functionality commonly used everywhere in FreeCAD: 3D vectors, units, matrices, placements, etc.
    -   **Gui**: contains the FreeCAD GUI-mode application, defines the 3D view, contains many tools and functions to be used by workbenches to interact with the interface and with the 3D view, defines base classes for view providers.
    -   **Doc**: contains mainly an all-in-one Qt help file generated from this wiki.
    -   **Mod**: contains all the modules, themselves further separated into App and Gui (except for python modules, which don\'t always follow that rule so clearly).

### Related

-   [Source Code Management](Source_code_management.md)
-   The [Power users hub](Power_users_hub.md) contains a lot of documentation about modules, OpenCascade and Coin3D, mainly for the Python programmer. However, as the functionality is similar, these pages will be of interest to the C++ programmer as well.
-   [FCStd](File_Format_FCStd.md) - the FreeCAD file format



---
![](images/Button_right.svg) [documentation index](../README.md) > [Developer Documentation](Category_Developer Documentation.md) > The FreeCAD source code/es
