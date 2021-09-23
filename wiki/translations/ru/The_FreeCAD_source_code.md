# The FreeCAD source code/ru
 The [FreeCAD source code](https://github.com/FreeCAD/FreeCAD) is managed with git, and is public, open and available under the [LGPL license](https://en.wikipedia.org/wiki/GNU_Lesser_General_Public_License). It can be copied, downloaded, read, analyzed, redistributed and modified by anyone. If you plan to make modifications that you wish to see included into the official code itself, remember that your changes will need to be approved by the FreeCAD developers, so it is wise to discuss first your intents and ideas on the [forum](http://forum.freecadweb.org), to avoid the risk to have your changes rejected for some reason you didn\'t foresee.

Below are some clues and useful information to get you on tracks if you are interested in exploring the FreeCAD code.

-   The FreeCAD code is programmed mainly in **C++**, but relies heavily on **Python**. A very large part of its functionality provides associated Python bindings, and it is part of the core philosophy of the FreeCAD development to always offer python access to any new feature implemented in C++. To obtain this, CPython (the C interfacing tools provided by Python itself) and specially [PyCXX](http://cxx.sourceforge.net/) are heavily used throughout FreeCAD. Many templates and custom tools are also provided in the FreeCAD code itself to turn the building of associated python bindings very easy. Some more high-level parts of the FreeCAD code are coded fully in Python.

-   The FreeCAD source code is fully **multi-platform**, and great care is taken to allow to use the application on a biggest possible number of platforms and configurations, and not put existing users in difficult situations. Therefore, as much as possible, new versions of needed components are avoided while they are not widely and easily available on all platforms, and backwards compatibility (the ability to open a file produced with an old version of FreeCAD on a newer version) is an important priority.

-   Almost all the functionality of FreeCAD is separated in two different parts, named **App** and **Gui**. This separation is reflected everywhere in the files structure of the source code. App contains all the functionality that needs to run in pure console mode (no GUI). As FreeCAD can be compiled and run without its Graphical User Interface, the code in App is independent of any GUI-related library. Gui contains all the code needed to run in GUI mode, and is built around the App functionality.

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

[Category:Developer Documentation](Category:Developer_Documentation.md)
