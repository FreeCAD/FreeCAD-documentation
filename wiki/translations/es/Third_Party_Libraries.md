





{{TOCright}}


<div class="mw-translate-fuzzy">

### Resumen

Estas son bibliotecas que no se han cambiado en el proyecto de FreeCAD. Son utilizadas básicamente sin cambios como bibliotecas de vínculos dinámicos (\*.so o \*.dll). Si se necesita un cambio o una clase que las envuelva, entonces el código del envoltorio o la biblioteca modificada tienen que moverse al paquete base de FreeCAD. Las bibliotecas utilizadas son:


</div>

The dependencies need to be installed in the system before proceeding with compilation; see [compile on Linux](Compile_on_Linux.md), [compile on Windows](Compile_on_Windows.md), and [compile on MacOS](Compile_on_MacOS.md) for more information.


<div class="mw-translate-fuzzy">

Considera el uso de [LibPack](#LibPack/es.md) en lugar de descargar e instalar todo por tu cuenta.


</div>


<div class="mw-translate-fuzzy">

### Enlaces


</div>


<div class="mw-translate-fuzzy">

  Nombre biblioteca   Versión necesitada   Enlace para conseguirla
  ------------------- -------------------- --------------------------------------------------------
  Python              \>= 2.5.x            <http://www.python.org/>
  OpenCasCade         \>= 5.2              <http://www.opencascade.org>
  Qt                  \>= 4.1.x            <http://www.qtsoftware.com>
  Coin3D              \>= 2.x              <http://www.coin3d.org>
  ODE                 \>= 0.10.x           <http://www.ode.org>
  SoQt                \>= 1.2              <http://www.coin3d.org>
  Xerces-C++          \>= 2.7.x \< 3.0     <http://xml.apache.org/xerces-c/>
  GTS                 \>= 0.7.x            <http://gts.sourceforge.net/>
  Zlib                \>= 1.x.x            <http://www.zlib.net/>
  Boost               \>= 1.33.x           <http://www.boost.org/>
  Eigen3              \>= 3.0.1            <http://eigen.tuxfamily.org/index.php?title=Main_Page>

  : Tabla de enlaces


</div>


<div class="mw-translate-fuzzy">

### Detalles


</div>


<div class="mw-translate-fuzzy">

#### Python

**Versión:** 2.5 o superior


</div>


<div class="mw-translate-fuzzy">

**Licencia:** Python 2.5 licencia


</div>


{{VeryImportantMessage|Python 2 became obsolete in 2019. Further development of FreeCAD will use exclusively Python 3; compatibility with Python 2 won't be tested, so old workbenches and macros that use this version will have to be updated or they may stop working. Please post on the [https://forum.freecadweb.org/ FreeCAD forum] if you encounter problems with Python 3.}}

Python is a popular all-purpose scripting language that is widely used in Linux and open source software. In FreeCAD, Python is used during compilation and also at runtime in different ways. It is used

-   to write test scripts to test for different conditions, such as memory leaks, to ensure functionality of the software after changes, for post build checks, and test coverage tests,
-   to write [macros](macros.md) and macro recording,
-   to implement application logic for standard packages,
-   to implement auxiliary tools such as the [Addon Manager](Addon_Manager.md),
-   to implement entire workbenches like [Draft](Draft_Workbench.md) and [Arch](Arch_Workbench.md),
-   to dynamically load packages,
-   to implement rules for design (knowledge engineering),
-   to do fancy Internet interactions like work groups and PDM


<div class="mw-translate-fuzzy">

Puedes utilizar el código fuente o los binarios de <http://www.python.org/> o utilizar alternativamente ActiveState Python de <http://www.activestate.com/> aunque es algo difícil conseguir las bibliotecas depuradas de ActiveState.


</div>

Python was chosen as the scripting language for FreeCAD for different reasons:

-   It is more object oriented than Perl and Tcl.
-   The code is more readable than Perl and Visual Basic.
-   It is easier to embed in another application, unlike, say, Java.

In summary, Python is well documented, and it\'s easy to embed and extend in a C++ application. It is also well tested and has strong support from the open source community. Read more about Python and browse the official documentation at [Python.org](http://www.python.org).


<div class="mw-translate-fuzzy">

#### Boost


</div>


<div class="mw-translate-fuzzy">

**Versión:** 1.33.x


</div>

**Licencia:** Boost Software License - Versión 1.0


<div class="mw-translate-fuzzy">

Las bibliotecas C++ Boost son una colección de evaluación de pares, bibliotecas de código libre que extienden la funcionalidad de C++. Las bibliotecas se licencian bajo la licencia de software de Boost, diseñada para permitir que Boost sea utilizado con proyectos de código abierto o cerrado. Muchos de los fundadores de Boost están en el comité del estándar C++ y diversas bibliotecas de Boost han sido aceptadas para incorporarse al informe técnico 1 de C++0x.


</div>

Due to their popularity and stability, many Boost libraries have been accepted for incorporation into the C++11 standard, and more are planned for inclusion in subsequent C++ standards.


<div class="mw-translate-fuzzy">

En orden de asegurar la eficiencia y flexibilidad, Boost hace un uso extensivo de las plantillas. Boost ha sido una fuente de trabajo extensivo e investigación en programación general y meta-programación en C++.


</div>


<div class="mw-translate-fuzzy">

#### OpenCasCade


</div>


<div class="mw-translate-fuzzy">

**Versión:** 5.2 o superior


</div>


<div class="mw-translate-fuzzy">

**Licencia:** OCTPL


</div>


<div class="mw-translate-fuzzy">

OCC es un kernel de CAD completo. Originalmente, fue desarrollado por Matra Datavision en Francia para las aplicaciones Strim y Euclid Quantum y después lo pasaron a código libre. Es una enorme biblioteca y hace que sea posible una aplicación de CAD libre en primer lugar, proporcionando algunos paquetes que serían complicados o imposibles de implementar en un proyecto de código libre:

-   Un kernel de geometría que admite STEP
-   Un modelo topológico de datos y todas las funciones necesarias para trabajar con (cortar, fusionar, extruir, etc.)
-   Procesadores estándar de importación / Exportación como STEP, IGES, VRML
-   Visores 3D y 2D con soporte para la selección
-   Un documento y estructura de datos de proyecto con soporte para guardar y restaurar, vinculación externa de documentos, recalculo del historial de diseño (modelado paramétrico) y una facilidad de cargar nuevos tipos de datos como un paquete de extensión dinámicamente


</div>

OCCT is a big and complex set of C++ libraries that provide functionality required by a CAD application:

-   A complete STEP compliant geometry kernel.
-   A topological data model and needed functions to work with shapes (cut, fuse, extrude, and many others).
-   Standard import and export processors for files like STEP, IGES, VRML.
-   A 2D and 3D viewer with selection support.
-   A document and project data structure with support for save and restore, external linking of documents, recalculation of design history (parametric modeling) and a facility to load new data types as an extension package dynamically.

There are two main versions of OpenCASCADE in existence in different Linux distributions. One is distributed by the original developers; it is known as OCCT, and is packaged under the names `occ` or `occt`. The other version is the \"community edition\", abbreviated OCE, and is normally found with the `oce` name. FreeCAD can compile against either version, however, since 2016 FreeCAD recommends compiling against the official OCCT libraries rather than the OCE ones. The reason is that the community edition lacks important bug fixes and functions that make using FreeCAD better.


<div class="mw-translate-fuzzy">

Para conocer más sobre OpenCasCade echa un vistazo a la página de OpenCasCade o <http://www.opencascade.org>.


</div>


<div class="mw-translate-fuzzy">

#### Qt


</div>


<div class="mw-translate-fuzzy">

**Versión:** 4.1.x o superior


</div>


<div class="mw-translate-fuzzy">

**Licencia:** GPL v2.0/v3.0 o Comercial (desde la versión 4.5 también en LPGL v2.1)


</div>


<div class="mw-translate-fuzzy">

No creo que necesite decir mucho sobre Qt. Es uno de las utilidades para interfaces gráficas de usuario GUI más utilizadas en los proyectos de código libre. Para mi el punto más importante para utilizar Qt es Qt Designer y la posibilidad de cargar letreros de diálogo completos como recursos (XML) e incorporar complementos (widgets) especializados. En una aplicación de CAX la interacción con el usuario y los letreros de diálogo son de lejos la parte más importante del código y un buen diseñador de letreros de diálogo es muy importante para extender FreeCAD fácilmente con nuevas funcionalidades. Puedes encontrar información complementaria y una muy buena documentación de ayuda en línea en <http://www.qtsoftware.com>.


</div>

Further information about Qt libraries and their programming documentation are available at [Qt Documentation](https://doc.qt.io/?hsCtaTracking=f641fd1a-772b-4957-964b-dad954b8d702%7C46c97dac-f1f6-49b3-ae46-8070fc35ea13).

#### Shiboken2 and Pyside2 

Shiboken is the Python binding generator that Qt for Python uses to create the PySide module, in other words, it is the system that is used to expose the Qt C++ API to the Python language.

The original Shiboken and PySide packages were meant to be used with Python 2 and Qt4; since these two versions are considered obsolete in 2019, please use Shiboken2 and PySide2, which work with Python 3 and Qt5. New development of FreeCAD is done with Python 3 and Qt5, so compatibility with Python 2 and Qt4 is not guaranteed after FreeCAD 0.18.

Read more about Shiboken and Pyside on [Qt for Python](https://wiki.qt.io/Qt_for_Python/Shiboken).


<div class="mw-translate-fuzzy">

#### Coin3D


</div>


<div class="mw-translate-fuzzy">

**Versión:** 2.0 o superior


</div>


<div class="mw-translate-fuzzy">

**Licencia:** GPL v2.0 o Comercial


</div>


<div class="mw-translate-fuzzy">

Coin es una biblioteca de gráficos 3D de alto nivel con una interfaz de programación para aplicaciones en C++. Coin utiliza estructuras de datos de la escena gráfica para renderizar gráficos en tiempo real adecuados para la mayoría de aplicaciones de visualización para ingeniería y científicos.


</div>


<div class="mw-translate-fuzzy">

Coin está construido sobre el estándar de la industria OpenGL bibloteca de modo de renderizado inmediato, y añade abstracción para primitivas de nivel superior, proporciona interactividad 3D, aumenta enormemente la conveniencia y productividad de los programadores, y contiene muchas características de optimización complejas para un renderizado rápido que son transparentes para el programador de la aplicación.


</div>


<div class="mw-translate-fuzzy">

Coin está basado en el SGI de la API de Open Inventor. Open Inventor, para aquellos que no están familiarizados con él, hace tiempo que se ha convertido en el estándar de las bibliotecas gráficas para software de visualización y simulación en la comunidad de ingeniería y científica. Se ha probado sobre un periodo de más de 10 años, su madurez contribuye a su éxito como un bloque de construcción principal en miles de aplicaciones de ingeniería de larga escala alrededor del mundo.


</div>


<div class="mw-translate-fuzzy">

Utilizaremos OpenInventor como visor 3D porque el visor de OpenCasCade (AIS y Graphics3D) tiene serias limitaciones cuellos de botella de rendimiento, especialmente cuando se trata de renderizado de ingeniería de larga escala. Otras cosas como texturas o renderizado volumétrico no están soportados realmente, etc.


</div>


<div class="mw-translate-fuzzy">

Coin es portable sobre un amplio rango de plataformas: Cualquier plataforma UNIX / Linux / \*BSD, todos los sistemas operativos de Microsoft Windows, y Mac OS X.


</div>


<div class="mw-translate-fuzzy">

#### SoQt


</div>

**Versión:** 1.2.0 o superior


<div class="mw-translate-fuzzy">

**Licencia:** GPL v2.0 o Comercial


</div>


<div class="mw-translate-fuzzy">

SoQt es la cubierta de Inventor para Qt Gui Toolkit. Por desgracia, ya no es LGPL así que tenemos que eliminarlo del código base de FreeCAD y vincularlo como una biblioteca. Tiene el mismo modelo de licencia que Coin. Y tienes que compilarlo con tu versión de Qt.


</div>

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


<div class="mw-translate-fuzzy">

#### Xerces-C++ 


</div>


<div class="mw-translate-fuzzy">

**Versión:** 2.7.0 o superior


</div>

**Licencia:** Apache Software License Versión 2.0


<div class="mw-translate-fuzzy">

Xerces-C++ es un analizador de validación XML escrito en C++. Xerces-C++ hace sencillo darle a tu aplicación la capacidad de leer y escribir datos XML. Una biblioteca compartida se proprciona para analizar, generar, manipular, y validar documentos XML.


</div>


<div class="mw-translate-fuzzy">

El analizador es utilizado para guardar y restaurar parámetros en FreeCAD.


</div>

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


<div class="mw-translate-fuzzy">

#### Zlib


</div>


<div class="mw-translate-fuzzy">

**Versión:** 1.x.x


</div>


<div class="mw-translate-fuzzy">

**Licencia:** zlib


</div>


<div class="mw-translate-fuzzy">

zlib está diseñado para ser libre, de propósito general, legalmente sin estorbos, eso es, no está cubierto por ningún tipo de patentes. Es una biblioteca de compresión de datos con mínimas perdidas para utilizarse en virtualmente cualquier hardware y sistema operativo. El formato de datos zlib es portable a través de las plataformas. A diferencia del método de compresión utilizada en la compresión de Unix y en el formato de imágenes GIF, el método de compresión utilizado en zlib esencialmente nunca expande los datos. (LZW puede duplicar o triplicar el tamaño del archivo en casos extremos.) La huella de memoria de zlib también es independiente de las entradas de datos y se puede reducir, si es necesario, con algunas perdidas en la compresión.


</div>

A copy of this library is included in the source code of FreeCAD so it is compiled together with it.

### libarea

**Version:** 0.0.20140514-1 or higher

**License:** BSD 3-clause license

Libarea is a software library to compute profile and pocket operations which are used in computer aided manufacturing (CAM) software. It was created by Dan Heeks for his HeeksCNC project.

A copy of the library is included with the source code of the [Path Workbench](Path_Workbench.md), so it is compiled together with it.


<div class="mw-translate-fuzzy">

### LibPack

LibPack es un paquete conveniente con todas las bibliotecas de arriba empaquetadas juntas. Está disponible actualmente para la plataforma Windows en la página de [Descargas](Download/es.md)! Si trabajas en Linux no necesitas LibPack, en su lugar asegúrate de utilizar los repositorios de paquetes de tu distribución Linux.


</div>

If you\'re working under Linux, you don\'t need the LibPack, as you can get the dependencies from your distribution\'s repositories as mentioned in the [compile on Linux](Compile_on_Linux.md) page.

### FreeCAD 12.1.2 

See the announcement in the forum: [New libpacks for Windows with Qt5.12, OCC7.3 and Python 3.6 by apeltauer](https://forum.freecadweb.org/viewtopic.php?f=4&t=35789)

It includes among other things: Boost 1.67, Coin3D 4.0.0a, Eigen3, Open CASCADE Technology 7.3.0, Python 3.6.8, PySide2, Qt 5.12.1, Salome SMESH, Shiboken2, vtk7, Xerces-C, Zipios++, zlib 1.2.11


<div class="mw-translate-fuzzy">


{{docnav/es|CompileOnMac/es|Third Party Tools/es}}


</div>


 

[Category:Developer Documentation{{\#translation:}}](Category:Developer_Documentation.md)
