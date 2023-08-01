# Third Party Libraries
## Overview

These are libraries which FreeCAD uses as third party dependencies during compilation. They are usually [dynamically linked libraries](https://en.wikipedia.org/wiki/Dynamic_loading) and have an extension `.so` in Linux/MacOS and `.dll` in Windows, and are accompanied by their header files `.h` or `.hpp` or similar. If a modified library is necessary, or a wrapper class is needed, the code of the modified library, or the wrapper, has to become part of the FreeCAD source code, and compiled together with it.

The dependencies need to be installed in the system before proceeding with compilation; see [compile on Linux](Compile_on_Linux.md), [compile on Windows](Compile_on_Windows.md), and [compile on MacOS](Compile_on_MacOS.md) for more information.

If you are compiling using Windows, consider using the [LibPack](#LibPack.md) instead of trying to install the libraries individually.

## Links

++++
| Library name        | Version needed          | Link to get it                                                                |
+=====================+=========================+===============================================================================+
| Python              | \>= 3.6                 | <http://www.python.org/>                                                      |
++++
| Boost               | \>= 1.33                | <http://www.boost.org/>                                                       |
++++
| OpenCASCADE         | \>= 7.3                 | <http://www.opencascade.org>                                                  |
++++
| Qt                  | \>= 5.4                 | <https://www.qt.io/>                                                          |
++++
| Shiboken2           |          | <https://wiki.qt.io/Qt_for_Python/Shiboken>                                   |
|                     | **same as Qt** |                                                                               |
|                     |                      |                                                                               |
++++
| PySide2             |          | <https://wiki.qt.io/Qt_for_Python/Shiboken>                                   |
|                     | **same as Qt** |                                                                               |
|                     |                      |                                                                               |
++++
| Coin3D              | \>= 3.x                 | <https://github.com/coin3d/coin>                                              |
++++
| SoQt (deprecated)   | \>= 1.2                 | <https://github.com/coin3d/soqt>                                              |
++++
| Quarter             | \>= 1.0                 | <https://github.com/coin3d/quarter>                                           |
++++
| Pivy                | \>= 0.6.5               | <https://github.com/coin3d/pivy/>                                             |
++++
| FreeType            | \>= XXX                 | XXX                                                                           |
++++
| PyCXX               | \>= XXX                 | XXX                                                                           |
++++
| KDL                 | \>= XXX                 | <https://orocos.org/wiki/orocos/kdl-wiki.html>                                |
++++
| Point Cloud Library | \>= XXX                 | XXX                                                                           |
++++
| Salome SMESH        | \>= XXX                 | XXX                                                                           |
++++
| VTK                 | \>= 6.0                 | XXX                                                                           |
++++
| Ply                 | \>= 3.11                | <https://www.dabeaz.com/ply/>                                                 |
++++
| Xerces-C++          | \>= 3.0                 | <https://xerces.apache.org/xerces-c/>                                         |
++++
| Eigen3              | \>= 3.0                 | <http://eigen.tuxfamily.org/index.php?title=Main_Page>                        |
++++
| Zipios++            | \>= 0.1.5               | <https://snapwebsites.org/project/zipios>, <https://github.com/Zipios/Zipios> |
++++
| Zlib                | \>= 1.0                 | <http://www.zlib.net/>, <https://github.com/madler/zlib>                      |
++++
| libarea             | \>= 0.0.20140514-1      | <https://github.com/danielfalck/libarea>                                      |
++++
|                     |                         |                                                                               |
++++

## Details

### Python

**Version:** 3.3 or higher

**License:** Python 3.3 license


**Python 2 became obsolete in 2019. Further development of FreeCAD will use exclusively Python 3; compatibility with Python 2 won't be tested, so old workbenches and macros that use this version will have to be updated or they may stop working. Please post on the [https://forum.freecadweb.org/ FreeCAD forum] if you encounter problems with Python 3.**

Python is a popular all-purpose scripting language that is widely used in Linux and open source software. In FreeCAD, Python is used during compilation and also at runtime in different ways. It is used

-   to write test scripts to test for different conditions, such as memory leaks, to ensure functionality of the software after changes, for post build checks, and test coverage tests,
-   to write [macros](macros.md) and macro recording,
-   to implement application logic for standard packages,
-   to implement auxiliary tools such as the [Addon Manager](Std_AddonMgr.md),
-   to implement entire workbenches like [Draft](Draft_Workbench.md) and [Arch](Arch_Workbench.md),
-   to dynamically load packages,
-   to implement rules for design (knowledge engineering),
-   to do fancy Internet interactions like work groups and PDM

On Linux, Python is usually already installed in your distribution. For Windows you can get a precompiled binary from [Python.org](http://www.python.org/) or use [ActiveState Python](http://www.activestate.com/), though it is harder to get the debug libraries from the latter one.

Python was chosen as the scripting language for FreeCAD for different reasons:

-   It is more object oriented than Perl and Tcl.
-   The code is more readable than Perl and Visual Basic.
-   It is easier to embed in another application, unlike, say, Java.

In summary, Python is well documented, and it\'s easy to embed and extend in a C++ application. It is also well tested and has strong support from the open source community. Read more about Python and browse the official documentation at [Python.org](http://www.python.org).

### Boost

**Version:** 1.33 or higher

**License:** Boost Software License - Version 1.0

The Boost C++ libraries are collections of peer-reviewed, open source libraries that extend the functionality of C++. They are intended to be widely useful across a broad spectrum of applications, and to work well with the C++ Standard Library. The Boost license is designed to encourage their use in both open source and closed source projects.

Due to their popularity and stability, many Boost libraries have been accepted for incorporation into the C++11 standard, and more are planned for inclusion in subsequent C++ standards.

In order to ensure efficiency and flexibility, Boost makes extensive use of templates. Boost has been a source of extensive work and research into generic programming and meta-programming in C++. Read more about Boost by visiting the [Boost homepage](http://www.boost.org/).

### OpenCASCADE Technology 

**Version:** 6.7 or higher

**License:** version 6.7.0 and later are governed by the [GNU Lesser General Public License (LGPL) version 2.1 with additional exception](https://www.opencascade.com/content/licensing). Earlier versions use the [Open CASCADE Technology Public License](https://www.opencascade.com/content/occt-public-license).

OpenCASCADE Technology (OCCT) is a full-featured, professional grade CAD kernel. It was developed in 1993 and originally called CAS.CADE, by Matra Datavision in France for the Strim (Styler) and Euclid Quantum applications. In 1999 it was released as open source software, and since then it\'s been called OpenCASCADE.

OCCT is a big and complex set of C++ libraries that provide functionality required by a CAD application:

-   A complete STEP compliant geometry kernel.
-   A topological data model and needed functions to work with shapes (cut, fuse, extrude, and many others).
-   Standard import and export processors for files like STEP, IGES, VRML.
-   A 2D and 3D viewer with selection support.
-   A document and project data structure with support for save and restore, external linking of documents, recalculation of design history (parametric modeling) and a facility to load new data types as an extension package dynamically.

There are two main versions of OpenCASCADE in existence in different Linux distributions. One is distributed by the original developers; it is known as OCCT, and is packaged under the names `occ` or `occt`. The other version is the \"community edition\", abbreviated OCE, and is normally found with the `oce` name. FreeCAD can compile against either version, however, since 2016 FreeCAD recommends compiling against the official OCCT libraries rather than the OCE ones. The reason is that the community edition lacks important bug fixes and functions that make using FreeCAD better.

To learn more visit the [OpenCASCADE website](http://www.opencascade.org).

### Qt

**Version:** 4.1 or higher

**License:** GPL v2.0/v3.0 or Commercial; from version 4.5 on also LPGL v2.1.

Qt is one of the most popular graphical user interface (GUI) toolkits available in the open source world. FreeCAD uses this toolkit to draw the interface of the program. For this, the Qt Designer application is very useful as it allows developers to quickly draw the dialogs and windows, export them as XML resource files, and then load these interfaces at runtime.

Further information about Qt libraries and their programming documentation are available at [Qt Documentation](https://doc.qt.io/?hsCtaTracking=f641fd1a-772b-4957-964b-dad954b8d702%7C46c97dac-f1f6-49b3-ae46-8070fc35ea13).

#### Shiboken2 and Pyside2 

Shiboken is the Python binding generator that Qt for Python uses to create the PySide module, in other words, it is the system that is used to expose the Qt C++ API to the Python language.

The original Shiboken and PySide packages were meant to be used with Python 2 and Qt4; since these two versions are considered obsolete in 2019, please use Shiboken2 and PySide2, which work with Python 3 and Qt5. New development of FreeCAD is done with Python 3 and Qt5, so compatibility with Python 2 and Qt4 is not guaranteed after FreeCAD 0.18.

Read more about Shiboken and Pyside on [Qt for Python](https://wiki.qt.io/Qt_for_Python/Shiboken).

### Coin3D

**Version:** 3.0 or higher

**License:** BSD 3-clause license

Coin3D is a high-level 3D graphics library with a C++ application programming interface. It uses scenegraph data structures to render real-time graphics suitable for all kinds of scientific and engineering visualization applications.

Coin3D is built on the industry-standard OpenGL immediate mode rendering library, and adds abstractions for higher-level primitives, provides 3D interactivity, and contains many complex optimization features for fast rendering that are transparent for the application programmer.

Coin3D is compatible with SGI\'s Open Inventor 2.1 API. This API has become the de facto standard graphics interface for 3D visualization in the scientific and engineering community. It has proved its worth since the year 2000 as a major building block in thousands of engineering applications around the world.

Coin3D (Open Inventor) is used as the 3D viewer in FreeCAD because the OpenCASCADE viewer (AIS and Graphics3D) has limitations and performance bottlenecks, especially with large-scale engineering rendering; other things like textures or volumetric rendering are not entirely supported by the OpenCASCADE viewer.

Coin3D is portable over a wide range of platforms: UNIX, Linux, BSD, macOS, and Microsoft Windows operating systems. To read more about this library visit [Coin3D homepage](https://github.com/coin3d/coin).

#### SoQt (deprecated) 

**Version:** 1.2.0 or higher

**License:** BSD 3-clause license

SoQt is the Coin3D (Open Inventor) binding to the Qt GUI toolkit.

SoQt is no longer used in FreeCAD, it was replaced by Quarter which is a more recent Qt binding.

#### Quarter

**Version:** 1.0 or higher

**License:** BSD 3-clause license

Quarter is a newer Coin3D binding to the Qt toolkit. A version of it is included in the source code of FreeCAD so it is compiled together with it.

#### Pivy

**Version:** 0.6.3 or higher

**License:** BSD 3-clause license

[Pivy](Pivy.md) is a library that wraps the Coin3d library for use in [Python](Python.md). It is not needed to build FreeCAD or to start it, but it is needed as a runtime dependency by the [Draft Workbench](Draft_Workbench.md), and by other workbenches that use it internally, like [Arch](Arch_Workbench.md) and [BIM](BIM_Workbench.md).

If you are not going to use these workbenches, you won\'t need Pivy.

### Ply

**Version:** 3.11 or higher

**License:** BSD 3-clause license

Ply is the Python-Lex-Yacc parser. It is used as a runtime dependency by the [OpenSCAD Workbench](OpenSCAD_Workbench.md). If you don\'t use this workbench, you may not need this package.

For more information see [Ply homepage](https://www.dabeaz.com/ply/)

### Xerces-C++ 

**Version:** 3.0 or higher

**License:** Apache Software License Version 2.0

Xerces-C++ is a validating XML parser written in a portable subset of C++. Xerces-C++ makes it easy to give your application the ability to read and write XML data. A shared library is provided for parsing, generating, manipulating, and validating XML documents. Xerces-C++ is faithful to the XML 1.0 recommendation and associated standards.

The parser is used for saving and restoring parameters in FreeCAD. For more information see [Xerces-C++ homepage](https://xerces.apache.org/xerces-c/).

### Eigen3

**Version:** 3.0 or higher

**License:** Starting from the 3.1.1 version, it is licensed under the [Mozilla Public License 2.0](http://www.mozilla.org/MPL/2.0). Earlier versions were licensed under the [GNU Lesser General Public License 3](https://www.gnu.org/licenses/lgpl-3.0.en.html).

Eigen is a C++ template library for linear algebra: matrices, vectors, numerical solvers, and related algorithms.

If you just want to use Eigen, you can use the header files right away. There is no binary library to link to, and no configured header file. Eigen is a pure template library defined in the headers.

Eigen is used in FreeCAD for many vector operations in 3D space. To learn more, visit [Eigen homepage](http://eigen.tuxfamily.org/index.php?title=Main_Page).

### Zipios++

**Version:** 0.1.5 or higher

**License:** GNU Lesser General Public License 2.1

Zipios++ is a C++ library for reading and writing `.zip` files. Access to individual entries is provided through standard C++ iostreams. A simple read-only virtual file system that mounts regular directories and `.zip` files is also provided. The structure and public interface of Zipios++ are loosely based on the `java.util.zip` package of Java.

FreeCAD\'s native file format `.FCstd` is in reality a `.zip` file that stores and compresses other types of data within it, such as BREP and XML files. Therefore, Zipios++ is used to save and open compressed archives, including FreeCAD files.

A copy of Zipios++ is included in the source code of FreeCAD so it is compiled together with it. If you want to use an external Zipios++ library, provided by your operating system, you may set -DFREECAD_USE_EXTERNAL_ZIPIOS=ON with `cmake`.

Zipios++ uses the Zlib library to perform the actual decompression of files.

#### Zlib

**Version:** 1.0 or higher

**License:** zlib license

Zlib is designed to be a free, general-purpose, lossless data-compression library for use on any computer hardware and operating system. It implements the `DEFLATE` compression algorithm commonly used in `.zip` and `.gzip` files.

A copy of this library is included in the source code of FreeCAD so it is compiled together with it.

### libarea

**Version:** 0.0.20140514-1 or higher

**License:** BSD 3-clause license

Libarea is a software library to compute profile and pocket operations which are used in computer aided manufacturing (CAM) software. It was created by Dan Heeks for his HeeksCNC project.

A copy of the library is included with the source code of the [Path Workbench](Path_Workbench.md), so it is compiled together with it.

## LibPack

LibPack is a convenient package with FreeCAD\'s build dependencies collected together. It is only needed if you are compiling FreeCAD on Windows with Visual Studio 2015 and above. You can find the latest LibPack on the [releases page](https://github.com/FreeCAD/FreeCAD/releases).

If you\'re working under Linux, you don\'t need the LibPack, as you can get the dependencies from your distribution\'s repositories as mentioned in the [compile on Linux](Compile_on_Linux.md) page.

### FreeCAD 12.1.2 

See the announcement in the forum: [New libpacks for Windows with Qt5.12, OCC7.3 and Python 3.6 by apeltauer](https://forum.freecadweb.org/viewtopic.php?f=4&t=35789)

It includes among other things: Boost 1.67, Coin3D 4.0.0a, Eigen3, Open CASCADE Technology 7.3.0, Python 3.6.8, PySide2, Qt 5.12.1, Salome SMESH, Shiboken2, vtk7, Xerces-C, Zipios++, zlib 1.2.11



---
⏵ [documentation index](../README.md) > [Developer Documentation](Category_Developer Documentation.md) > Third Party Libraries
