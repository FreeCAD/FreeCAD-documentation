# Third Party Libraries/es
{{TOCright}}

## Resumen

Estas son bibliotecas que FreeCAD utiliza como dependencias de terceros durante la compilación. Normalmente son [bibliotecas enlazadas dinámicamente](https://en.wikipedia.org/wiki/Dynamic_loading) y tienen una extensión `.so` en Linux/MacOS y `.dll` en Windows, y van acompañadas de sus archivos de cabecera `.h` o `.hpp` o similares. Si se necesita una biblioteca modificada, o una clase envolvente, el código de la biblioteca modificada, o la envolvente, tiene que formar parte del código fuente de FreeCAD, y compilarse junto con él.

Las dependencias deben ser instaladas en el sistema antes de proceder a la compilación; ver [compilar en Linux](Compile_on_Linux/es.md), [compilar en Windows](Compile_on_Windows/es.md), y [compilar en MacOS](Compile_on_MacOS/es.md) para más información.

Si está compilando con Windows, considere usar el [LibPack](#LibPack.md) en lugar de intentar instalar las bibliotecas individualmente.

## Enlaces

+---------------------+-------------------------+-------------------------------------------------------------------------------+
| Nombre biblioteca   | Versión necesaria       | Enlace para obtenerla                                                         |
+=====================+=========================+===============================================================================+
| Python              | \>= 3.6                 | <http://www.python.org/>                                                      |
+---------------------+-------------------------+-------------------------------------------------------------------------------+
| Boost               | \>= 1.33                | <http://www.boost.org/>                                                       |
+---------------------+-------------------------+-------------------------------------------------------------------------------+
| OpenCASCADE         | \>= 7.3                 | <http://www.opencascade.org>                                                  |
+---------------------+-------------------------+-------------------------------------------------------------------------------+
| Qt                  | \>= 5.4                 | <https://www.qt.io/>                                                          |
+---------------------+-------------------------+-------------------------------------------------------------------------------+
| Shiboken2           |          | <https://wiki.qt.io/Qt_for_Python/Shiboken>                                   |
|                     | **same as Qt** |                                                                               |
|                     |                      |                                                                               |
+---------------------+-------------------------+-------------------------------------------------------------------------------+
| PySide2             |          | <https://wiki.qt.io/Qt_for_Python/Shiboken>                                   |
|                     | **same as Qt** |                                                                               |
|                     |                      |                                                                               |
+---------------------+-------------------------+-------------------------------------------------------------------------------+
| Coin3D              | \>= 3.x                 | <https://github.com/coin3d/coin>                                              |
+---------------------+-------------------------+-------------------------------------------------------------------------------+
| SoQt (deprecated)   | \>= 1.2                 | <https://github.com/coin3d/soqt>                                              |
+---------------------+-------------------------+-------------------------------------------------------------------------------+
| Quarter             | \>= 1.0                 | <https://github.com/coin3d/quarter>                                           |
+---------------------+-------------------------+-------------------------------------------------------------------------------+
| Pivy                | \>= 0.6.5               | <https://github.com/coin3d/pivy/>                                             |
+---------------------+-------------------------+-------------------------------------------------------------------------------+
| FreeType            | \>= XXX                 | XXX                                                                           |
+---------------------+-------------------------+-------------------------------------------------------------------------------+
| PyCXX               | \>= XXX                 | XXX                                                                           |
+---------------------+-------------------------+-------------------------------------------------------------------------------+
| KDL                 | \>= XXX                 | XXX                                                                           |
+---------------------+-------------------------+-------------------------------------------------------------------------------+
| Point Cloud Library | \>= XXX                 | XXX                                                                           |
+---------------------+-------------------------+-------------------------------------------------------------------------------+
| Salome SMESH        | \>= XXX                 | XXX                                                                           |
+---------------------+-------------------------+-------------------------------------------------------------------------------+
| VTK                 | \>= 6.0                 | XXX                                                                           |
+---------------------+-------------------------+-------------------------------------------------------------------------------+
| Ply                 | \>= 3.11                | <https://www.dabeaz.com/ply/>                                                 |
+---------------------+-------------------------+-------------------------------------------------------------------------------+
| Xerces-C++          | \>= 3.0                 | <https://xerces.apache.org/xerces-c/>                                         |
+---------------------+-------------------------+-------------------------------------------------------------------------------+
| Eigen3              | \>= 3.0                 | <http://eigen.tuxfamily.org/index.php?title=Main_Page>                        |
+---------------------+-------------------------+-------------------------------------------------------------------------------+
| Zipios++            | \>= 0.1.5               | <https://snapwebsites.org/project/zipios>, <https://github.com/Zipios/Zipios> |
+---------------------+-------------------------+-------------------------------------------------------------------------------+
| Zlib                | \>= 1.0                 | <http://www.zlib.net/>, <https://github.com/madler/zlib>                      |
+---------------------+-------------------------+-------------------------------------------------------------------------------+
| libarea             | \>= 0.0.20140514-1      | <https://github.com/danielfalck/libarea>                                      |
+---------------------+-------------------------+-------------------------------------------------------------------------------+
|                     |                         |                                                                               |
+---------------------+-------------------------+-------------------------------------------------------------------------------+

## Detalles

### Python

**Versión:** 3.3 o superior

**Licencia:** Python 3.3 licencia


**Python 2 quedó obsoleto en 2019. El futuro desarrollo de FreeCAD utilizará exclusivamente Python 3; no se probará la compatibilidad con Python 2, por lo que los antiguos ambientes de trabajo y macros que utilizan esta versión tendrán que ser actualizados o pueden dejar de funcionar. Por favor, publica en el [https://forum.freecadweb.org/ foro de FreeCAD] si encuentras problemas con Python 3.**

Python es un popular lenguaje de guionización multipropósito que es ampliamente utilizado en Linux y en el software de código abierto. En FreeCAD, Python se utiliza durante la compilación y también en tiempo de ejecución de diferentes maneras. Se utiliza

-   para escribir guiónes de prueba para comprobar diferentes condiciones, como fugas de memoria, para asegurar la funcionalidad del software después de los cambios, para las comprobaciones posteriores a la compilación, y las pruebas de cobertura,
-   para escribir [macros](macros/es.md) y grabación de macros,
-   para implementar la lógica de la aplicación para los paquetes estándar,
-   para implementar herramientas auxiliares como el [Gestor Complementos](Addon_Manager/es.md),
-   para implementar bancos de trabajo completos como [Borrador](Draft_Workbench/es.md) y [Arquitectura](Arch_Workbench/es.md),
-   para cargar dinámicamente paquetes,
-   para implementar reglas de diseño (ingeniería del conocimiento),
-   para hacer interacciones de lujo en Internet como grupos de trabajo y PDM

En Linux, Python suele estar ya instalado en tu distribución. Para Windows puedes obtener un binario precompilado de [Python.org](http://www.python.org/) o utilizar [ActiveState Python](http://www.activestate.com/), aunque es más difícil obtener las librerías de depuración de esta última.

Python fue elegido como el lenguaje de guionización para FreeCAD por diferentes razones:

-   Es más orientado a objetos que Perl y Tcl.
-   El código es más legible que Perl y Visual Basic.
-   Es más fácil de incrustar en otra aplicación, a diferencia de, por ejemplo, Java.

En sinopsis, Python está bien documentado y es fácil de integrar y extender en una aplicación C++. También está bien probado y tiene un fuerte apoyo de la comunidad de código abierto. Lee más sobre Python y explora la documentación oficial en [Python.org](http://www.python.org).

### Boost

**Versión:** 1.33 o superior

**Licencia:** Boost Software Licencia - Versión 1.0

Las bibliotecas Boost C++ son colecciones de bibliotecas de código abierto revisadas por pares que amplían la funcionalidad de C++. Están pensadas para ser ampliamente útiles en un amplio espectro de aplicaciones, y para funcionar bien con la biblioteca estándar de C++. La licencia de Boost está diseñada para fomentar su uso tanto en proyectos de código abierto como de código cerrado.

Due to their popularity and stability, many Boost libraries have been accepted for incorporation into the C++11 standard, and more are planned for inclusion in subsequent C++ standards.

En orden de asegurar la eficiencia y flexibilidad, Boost hace un uso extensivo de las plantillas. Boost ha sido una fuente de trabajo extensivo e investigación en programación general y meta-programación en C++. Para saber más sobre Boost, visite la página [Boost página inicio](http://www.boost.org/).

### OpenCASCADE Tecnología 

**Versión:** 6.7 o superior

**Licencia:** versión 6.7.0 y posteriores se rigen por la [Licencia Pública General Reducida de GNU (LGPL) versión 2.1 con una excepción adicional](https://www.opencascade.com/content/licensing). Las versiones anteriores utilizan la [Open CASCADE Licencia pública tecnológica](https://www.opencascade.com/content/occt-public-license).

La tecnología OpenCASCADE (OCCT) es un kernel CAD profesional con todas las funciones. Fue desarrollado en 1993 y originalmente llamado CAS.CADE, por Matra Datavision en Francia para las aplicaciones Strim (Styler) y Euclid Quantum. En 1999 se publicó como software de código abierto, y desde entonces se llama OpenCASCADE.

OCCT is a big and complex set of C++ libraries that provide functionality required by a CAD application:

-   A complete STEP compliant geometry kernel.
-   A topological data model and needed functions to work with shapes (cut, fuse, extrude, and many others).
-   Standard import and export processors for files like STEP, IGES, VRML.
-   A 2D and 3D viewer with selection support.
-   A document and project data structure with support for save and restore, external linking of documents, recalculation of design history (parametric modeling) and a facility to load new data types as an extension package dynamically.

There are two main versions of OpenCASCADE in existence in different Linux distributions. One is distributed by the original developers; it is known as OCCT, and is packaged under the names `occ` or `occt`. The other version is the \"community edition\", abbreviated OCE, and is normally found with the `oce` name. FreeCAD can compile against either version, however, since 2016 FreeCAD recommends compiling against the official OCCT libraries rather than the OCE ones. The reason is that the community edition lacks important bug fixes and functions that make using FreeCAD better.

Para obtener más información, visite el [OpenCASCADE sitio web](http://www.opencascade.org).

### Qt

**Versión:** 4.1 o superior

**Licencia:** GPL v2.0/v3.0 o Comercial; desde versión 4.5 también en LPGL v2.1.

Qt es uno de los juegos de herramientas de interfaz gráfica de usuario (GUI) más populares disponibles en el mundo del código abierto. FreeCAD utiliza este kit de herramientas para dibujar la interfaz del programa. Para ello, la aplicación Qt Designer es muy útil, ya que permite a los desarrolladores dibujar rápidamente los diálogos y ventanas, exportarlos como archivos de recursos XML, y luego cargar estas interfaces en tiempo de ejecución.

Further information about Qt libraries and their programming documentation are available at [Qt Documentation](https://doc.qt.io/?hsCtaTracking=f641fd1a-772b-4957-964b-dad954b8d702%7C46c97dac-f1f6-49b3-ae46-8070fc35ea13).

#### Shiboken2 and Pyside2 

Shiboken is the Python binding generator that Qt for Python uses to create the PySide module, in other words, it is the system that is used to expose the Qt C++ API to the Python language.

The original Shiboken and PySide packages were meant to be used with Python 2 and Qt4; since these two versions are considered obsolete in 2019, please use Shiboken2 and PySide2, which work with Python 3 and Qt5. New development of FreeCAD is done with Python 3 and Qt5, so compatibility with Python 2 and Qt4 is not guaranteed after FreeCAD 0.18.

Read more about Shiboken and Pyside on [Qt for Python](https://wiki.qt.io/Qt_for_Python/Shiboken).

### Coin3D

**Versión:** 3.0 o superior

**Licencia:** Licencia BSD de 3 cláusulas

Coin3D es una biblioteca de gráficos 3D de alto nivel con una interfaz de programación de aplicaciones C++. Utiliza estructuras de datos scenegraph para renderizar gráficos en tiempo real adecuados para todo tipo de aplicaciones de visualización científica y de ingeniería.

Coin3D se basa en la biblioteca de renderizado de modo inmediato OpenGL, estándar industrial, y añade abstracciones para primitivas de nivel superior, proporciona interactividad 3D y contiene muchas funciones de optimización complejas para un renderizado rápido y transparente para el programador de la aplicación.

Coin3D es compatible con la API Open Inventor 2.1 de SGI. Esta API se ha convertido en la interfaz gráfica estándar de facto para la visualización 3D en la comunidad científica y de ingeniería. Desde el año 2000 ha demostrado su valía como elemento fundamental en miles de aplicaciones de ingeniería de todo el mundo.

Coin3D (Open Inventor) se utiliza como visor 3D en FreeCAD porque el visor de OpenCASCADE (AIS y Graphics3D) tiene limitaciones y cuellos de botella en el rendimiento, especialmente con el renderizado de ingeniería a gran escala; otras cosas como las texturas o el renderizado volumétrico no son totalmente compatibles con el visor de OpenCASCADE.

Coin3D es portátil en una amplia gama de plataformas: Sistemas operativos UNIX, Linux, BSD, MacOS X y Microsoft Windows. Para obtener más información sobre esta biblioteca, visite [Coin3D página de inicio](https://github.com/coin3d/coin).

#### SoQt (obsoleto) 

**Versión:** 1.2.0 o superior

**Licencia:** Licencia BSD de 3 cláusulas

SoQt es el enlace de Coin3D (Open Inventor) con el juego de herramientas de interfaz gráfica de usuario Qt.

SoQt is no longer used in FreeCAD, it was replaced by Quarter which is a more recent Qt binding.

#### Quarter

**Versión:** 1.0 o superior

**Licencia:** Licencia BSD de 3 cláusulas

Quarter is a newer Coin3D binding to the Qt toolkit. A version of it is included in the source code of FreeCAD so it is compiled together with it.

#### Pivy

**Versión:** 0.6.3 o superior

**Licencia:** Licencia BSD de 3 cláusulas

[Pivy](Pivy.md) is a library that wraps the Coin3d library for use in [Python](Python.md). It is not needed to build FreeCAD or to start it, but it is needed as a runtime dependency by the [Draft Workbench](Draft_Workbench.md), and by other workbenches that use it internally, like [Arch](Arch_Workbench.md) and [BIM](BIM_Workbench.md).

If you are not going to use these workbenches, you won\'t need Pivy.

### Ply

**Versión:** 3.11 o superior

**Licencia:** Licencia BSD de 3 cláusulas

Ply is the Python-Lex-Yacc parser. It is used as a runtime dependency by the [OpenSCAD Workbench](OpenSCAD_Workbench.md). If you don\'t use this workbench, you may not need this package.

For more information see [Ply homepage](https://www.dabeaz.com/ply/)

### Xerces-C++ 

**Versión:** 3.0 o superior

**Licencia:** Apache Software Licencia Versión 2.0

Xerces-C++ es un analizador sintáctico XML de validación escrito en un subconjunto portátil de C++. Xerces-C++ hace que sea fácil dar a su aplicación la capacidad de leer y escribir datos XML. Se proporciona una biblioteca compartida para analizar, generar, manipular y validar documentos XML. Xerces-C++ es fiel a la recomendación XML 1.0 y a los estándares asociados.

El analizador sintáctico se utiliza para guardar y restaurar parámetros en FreeCAD. Para más información, consulte [Página de inicio de Xerces-C++](https://xerces.apache.org/xerces-c/).

### Eigen3

**Versión:** 3.0 o superior

**License:** Starting from the 3.1.1 version, it is licensed under the [Mozilla Public License 2.0](http://www.mozilla.org/MPL/2.0). Earlier versions were licensed under the [GNU Lesser General Public License 3](https://www.gnu.org/licenses/lgpl-3.0.en.html).

Eigen is a C++ template library for linear algebra: matrices, vectors, numerical solvers, and related algorithms.

If you just want to use Eigen, you can use the header files right away. There is no binary library to link to, and no configured header file. Eigen is a pure template library defined in the headers.

Eigen is used in FreeCAD for many vector operations in 3D space. To learn more, visit [Eigen homepage](http://eigen.tuxfamily.org/index.php?title=Main_Page).

### Zipios++

**Versión:** 0.1.5 o superior

**Licencia:** Licencia Pública General Reducida de GNU 2.1

Zipios++ is a C++ library for reading and writing `.zip` files. Access to individual entries is provided through standard C++ iostreams. A simple read-only virtual file system that mounts regular directories and `.zip` files is also provided. The structure and public interface of Zipios++ are loosely based on the `java.util.zip` package of Java.

FreeCAD\'s native file format `.FCstd` is in reality a `.zip` file that stores and compresses other types of data within it, such as BREP and XML files. Therefore, Zipios++ is used to save and open compressed archives, including FreeCAD files.

A copy of Zipios++ is included in the source code of FreeCAD so it is compiled together with it. If you want to use an external Zipios++ library, provided by your operating system, you may set -DFREECAD_USE_EXTERNAL_ZIPIOS=ON with `cmake`.

Zipios++ uses the Zlib library to perform the actual decompression of files.

#### Zlib

**Versión:** 1.0 o superior

**Licencia:** zlib licencia

Zlib está diseñado para ser una biblioteca de compresión de datos gratuita, de propósito general y sin pérdidas, para su uso en cualquier hardware y sistema operativo. Implementa el algoritmo de compresión `DEFLATE` comúnmente utilizado en los archivos `.zip` y `.gzip`.

A copy of this library is included in the source code of FreeCAD so it is compiled together with it.

### libarea

**Version:** 0.0.20140514-1 or higher

**Licencia:** Licencia BSD de 3 cláusulas

Libarea is a software library to compute profile and pocket operations which are used in computer aided manufacturing (CAM) software. It was created by Dan Heeks for his HeeksCNC project.

A copy of the library is included with the source code of the [Path Workbench](Path_Workbench.md), so it is compiled together with it.

## LibPack

LibPack es un conveniente paquete con las dependencias de compilación de FreeCAD reunidas. Sólo es necesario si estás compilando FreeCAD en Windows con Visual Studio 2015 y superior. Puedes encontrar el último LibPack en la página [releases](https://github.com/FreeCAD/FreeCAD/releases).

Si estás trabajando bajo Linux, no necesitas el LibPack, ya que puedes obtener las dependencias de los repositorios de tu distribución como se menciona en la página [compilar en Linux](Compile_on_Linux/es.md).

### FreeCAD 12.1.2 

See the announcement in the forum: [New libpacks for Windows with Qt5.12, OCC7.3 and Python 3.6 by apeltauer](https://forum.freecadweb.org/viewtopic.php?f=4&t=35789)

It includes among other things: Boost 1.67, Coin3D 4.0.0a, Eigen3, Open CASCADE Technology 7.3.0, Python 3.6.8, PySide2, Qt 5.12.1, Salome SMESH, Shiboken2, vtk7, Xerces-C, Zipios++, zlib 1.2.11





 

_

---
[documentation index](../README.md) > [Developer Documentation](Category_Developer Documentation.md) > Third Party Libraries/es
