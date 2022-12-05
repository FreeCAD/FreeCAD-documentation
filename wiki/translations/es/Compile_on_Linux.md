# Compile on Linux/es
**Hay un contenedor experimental FreeCAD Docker que se está probando para el desarrollo de FreeCAD. Lea más sobre ello en [Compilar en Docker](Compile_on_Docker/es.md)**


{{TOCright}}

## Vista general 

En las distribuciones recientes de Linux, FreeCAD es generalmente fácil de construir, ya que todas las dependencias suelen ser proporcionadas por el administrador de paquetes. Básicamente implica 3 pasos:

1.  Obtener el código fuente de FreeCAD
2.  Obtener las dependencias o paquetes de los que depende FreeCAD
3.  Configurar con `cmake` y compilar con `make`

A continuación, encontrará explicaciones detalladas de todo el proceso, algunos [build scripts](#Automatic_build_scripts.md), y las particularidades que puede encontrar. Si encuentras algo incorrecto o desactualizado en el texto de abajo (las distribuciones de Linux cambian a menudo), o si usas una distribución que no está en la lista, discute el tema en el [forum](https://forum.freecadweb.org/index.php), y ayúdanos a corregirlo.

<img alt="" src=images/FreeCAD_source_compilation_workflow.svg  style="width:800px;">



*Flujo de trabajo general para compilar FreeCAD desde la fuente. Las dependencias de terceros deben estar en el sistema, así como el propio código fuente de FreeCAD. CMake configura el sistema de manera que con una sola instrucción de creación se compila todo el proyecto.*

## Obtener la fuente 

### Git

La mejor manera de obtener el código es clonar el repositorio Git de sólo lectura [1](https://github.com/FreeCAD/FreeCAD). Para ello se necesita el programa `git` que se puede instalar fácilmente en la mayoría de las distribuciones de Linux. También puede obtenerse en el [sitio web oficial](http://git-scm.com/).

Git se puede instalar mediante el siguiente comando:


{{Code|lang=bash|code=
sudo apt install git
}}

El siguiente comando colocará una copia de la última versión del código fuente de FreeCAD en un nuevo directorio llamado `freecad-source`.


{{Code|lang=bash|code=
git clone https://github.com/FreeCAD/FreeCAD.git freecad-source
}}

Para más información sobre el uso de Git y la contribución de código al proyecto, véase [Gestión del código fuente](Source_code_management/rs.md).

### Archivo Fuente 

También puede descargar el código fuente como un archivo [2](https://github.com/FreeCAD/FreeCAD/releases/latest), un archivo `.zip` o `.tar.gz`, y descomprimirlo en el directorio deseado.

## Obtener las dependencias 

Para compilar FreeCAD tienes que instalar las dependencias necesarias mencionadas en [Bibliotecas de terceros](Third_Party_Libraries/es.md); los paquetes que contienen estas dependencias están listados abajo para diferentes distribuciones de Linux. Tenga en cuenta que los nombres y la disponibilidad de las bibliotecas dependerán de su distribución particular; si su distribución es antigua, algunos paquetes pueden no estar disponibles o tener un nombre diferente. En este caso, busque en la sección [Distribuciones antiguas y no convencionales](#Older_and_non-conventional_distributions.md) más abajo.

Una vez que tengas todas las dependencias instaladas, procede a [compilar FreeCAD](#Compilar_FreeCAD.md).

Ten en cuenta que el código fuente de FreeCAD tiene un tamaño de unos 500 MB; puede ser tres veces mayor si clonas el repositorio Git con todo su historial de modificaciones. Obtener todas las dependencias puede requerir la descarga de 500 MB o más de nuevos archivos; cuando estos archivos se descomprimen pueden requerir 1500 MB o más de espacio. También ten en cuenta que el proceso de compilación puede generar hasta 1500 MB de archivos adicionales ya que el sistema copia y modifica todo el código fuente. Por lo tanto, asegúrese de tener suficiente espacio libre en su disco duro, al menos 4 GB, cuando intente la compilación.


<div class="mw-collapsible mw-collapsed toccolours">

### Debian y Ubuntu 


<div class="mw-collapsible-content">

En los sistemas basados en Debian (Debian, Ubuntu, Mint, etc.) es bastante fácil conseguir instalar todas las dependencias necesarias. La mayoría de las bibliotecas están disponibles a través de `apt` o del gestor de paquetes Synaptic.

Si ya has instalado FreeCAD desde los repositorios oficiales, puedes instalar sus dependencias de construcción con esta única línea de código en un terminal:


```python
sudo apt build-dep freecad
```

Sin embargo, si la versión de FreeCAD en los repositorios es antigua, las dependencias pueden ser las incorrectas para compilar una versión reciente de FreeCAD. Por lo tanto, comprueba que tienes instalados los siguientes paquetes.

Estos paquetes son esenciales para que cualquier tipo de compilación tenga éxito:

-    `build-essential`, instala los compiladores C y C++, las librerías de desarrollo C y el programa `make`.

-    `cmake`, herramienta esencial para configurar el código fuente de FreeCAD. También puedes querer instalar `cmake-gui` y `cmake-curses-gui` para una opción gráfica.

-    `libtool`, herramientas esenciales para producir bibliotecas compartidas.

-    `lsb-release`, la utilidad estándar de informes de base normalmente ya está instalada en un sistema Debian, y le permite distinguir mediante programación entre una instalación Debian pura o una variante, como Ubuntu o Linux Mint. No elimine este paquete, ya que muchos otros paquetes del sistema pueden depender de él.

La compilación de FreeCAD utiliza el lenguaje Python, y también se utiliza en tiempo de ejecución como lenguaje de scripting. Si estás usando una distribución basada en Debian el intérprete de Python normalmente ya está instalado.

-    `python3`
    

-    `swig`, la herramienta que crea interfaces entre el código C++ y Python.

Por favor, comprueba que tienes instalado Python 3. Python 2 quedó obsoleto en 2019, por lo que los nuevos desarrollos en FreeCAD no se prueban con esta versión del lenguaje.

Es necesario instalar las bibliotecas Boost:

-    `libboost-dev`
    

-    `libboost-date-time-dev`
    

-    `libboost-filesystem-dev`
    

-    `libboost-graph-dev`
    

-    `libboost-iostreams-dev`
    

-    `libboost-program-options-dev`
    

-    `libboost-python-dev`
    

-    `libboost-regex-dev`
    

-    `libboost-serialization-dev`
    

-    `libboost-thread-dev`
    

Es necesario instalar las bibliotecas de Coin:

-    `libcoin80-dev`, para Debian Jessie, Stretch, Ubuntu 16.04 a 18.10, o

-    `libcoin-dev`, para Debian Buster, Ubuntu 19.04 y más recientes, así como para Ubuntu 18.04/18.10 con los PPAs [freecad-stable/freecad-daily](Installing_on_Linux#Official_Ubuntu_repository.md) añadidos a sus fuentes de software.

Varias bibliotecas que se ocupan de las matemáticas, las superficies trianguladas, la ordenación, las mallas, la visión por ordenador, las proyecciones cartográficas, la visualización 3D, el sistema de ventanas X11, el análisis sintáctico de XML y la lectura de archivos Zip:

-    `libeigen3-dev`
    

-    `libgts-bin`
    

-    `libgts-dev`
    

-    `libkdtree++-dev`
    

-    `libmedc-dev`
    

-    `libopencv-dev`or `libcv-dev`

-    `libproj-dev`
    

-    `libvtk7-dev`or `libvtk6-dev`

-    `libx11-dev`
    

-    `libxerces-c-dev`
    

-    `libzipios++-dev`
    


<div class="mw-collapsible mw-collapsed" style="background-color:#e0e0e0">

#### Python 2 y Qt4 

Esto no se recomienda para las instalaciones más recientes, ya que tanto Python 2 como Qt4 están obsoletos. A partir de la versión 0.20, FreeCAD ya no los soporta.


<div class="mw-collapsible-content">

Para compilar FreeCAD para Debian Jessie, Stretch, Ubuntu 16.04, usando Python 2 y Qt4, instala las siguientes dependencias.

-    `qt4-dev-tools`
    

-    `libqt4-dev`
    

-    `libqt4-opengl-dev`
    

-    `libqtwebkit-dev`
    

-    `libshiboken-dev`
    

-    `libpyside-dev`
    

-    `pyside-tools`
    

-    `python-dev`
    

-    `python-matplotlib`
    

-    `python-pivy`
    

-    `python-ply`
    

-    `python-pyside`
    


</div>


</div>

#### Python 3 y Qt5 

Para compilar FreeCAD para Debian Buster, Ubuntu 19.04 y posteriores, así como Ubuntu 18.04/18.10 con el [freecad-stable/freecad-daily PPAs](Installing_on_Linux/es#Repositorio_Oficial_Ubuntu.md) añadido a sus fuentes de software, instale las siguientes dependencias.

-    `qtbase5-dev`
    

-    `qttools5-dev`
    

-    `qt5-default`(if compiling 0.20 on a machine that still has Qt4)

-    `libqt5opengl5-dev`
    

-    `libqt5svg5-dev`
    

-    `qtwebengine5-dev`
    

-    `libqt5xmlpatterns5-dev`
    

-    `libqt5x11extras5-dev`
    

-    `libpyside2-dev`
    

-    `libshiboken2-dev`
    

-    `pyside2-tools`
    

-    `pyqt5-dev-tools`
    

-    `python3-dev`
    

-    `python3-matplotlib`
    

-    `python3-packaging`
    

-    `python3-pivy`
    

-    `python3-ply`
    

-    `python3-pyside2.qtcore`
    

-    `python3-pyside2.qtgui`
    

-    `python3-pyside2.qtsvg`
    

-    `python3-pyside2.qtwidgets`
    

-    `python3-pyside2.qtnetwork`
    

-    `python3-pyside2.qtwebengine`
    

-    `python3-pyside2.qtwebenginecore`
    

-    `python3-pyside2.qtwebenginewidgets`
    

-    `python3-pyside2.qtwebchannel`
    

-    `python3-pyside2uic`
    

#### Núcleo OpenCascade 

El núcleo de OpenCascade es el núcleo de la biblioteca de gráficos para crear formas 3D. Existe una versión oficial OCCT, y una versión comunitaria OCE. La versión de la comunidad ya no se recomienda, ya que está obsoleta.

Para Debian Buster y Ubuntu 18.10 y posteriores, así como para Ubuntu 18.04 con el [freecad-stable/freecad-daily PPAs](Installing_on_Linux#Repositorio_Oficial_Ubuntu.md) añadido a sus fuentes de software, instale los paquetes oficiales.

-    `libocct*-dev`-   
        `libocct-data-exchange-dev`
        

    -   
        `libocct-draw-dev`
        

    -   
        `libocct-foundation-dev`
        

    -   
        `libocct-modeling-algorithms-dev`
        

    -   
        `libocct-modeling-data-dev`
        

    -   
        `libocct-ocaf-dev`
        

    -   
        `libocct-visualization-dev`
        

-    `occt-draw`
    

Para Debian Jessie, Stretch, Ubuntu 16.04 y posteriores, instale los paquetes de la edición comunitaria.

-    `liboce*-dev`-   
        `liboce-foundation-dev`
        

    -   
        `liboce-modeling-dev`
        

    -   
        `liboce-ocaf-dev`
        

    -   
        `liboce-ocaf-lite-dev`
        

    -   
        `liboce-visualization-dev`
        

-    `oce-draw`
    

Puede instalar las bibliotecas individualmente, o utilizando la expansión de asterisco. Cambie `occ` por `oce` si desea instalar las bibliotecas comunitarias.


```python
sudo apt install libocct*-dev
```

#### Paquetes opcionales 


<div class="mw-translate-fuzzy">

Opcionalmente, también puede instalar estos paquetes adicionales:

-    `libsimage-dev`, para que Coin soporte formatos de archivo de imagen adicionales.

-    `doxygen`y `libcoin-doc` (o `libcoin80-doc` para los sistemas más antiguos), si quieres generar documentación del código fuente.

-    `libspnav-dev`, para soporte de [Dispositivos de entrada 3D](3D_input_devices/es.md), como el \"Space Navigator\" o el \"Space Pilot\" de 3Dconnexion.

-    `checkinstall`, si pretende registrar los archivos instalados en el gestor de paquetes de su sistema, para poder desinstalarlo más tarde.


</div>

#### Comando único para Python 3 y Qt5 

Requiere Pyside2 disponible en Debian buster y el [freecad-stable/freecad-daily PPAs](Installing_on_Linux/es#Repositorio_Oficial_Ubuntu.md).


{{Code|lang=bash|code=
sudo apt install cmake cmake-gui libboost-date-time-dev libboost-dev libboost-filesystem-dev libboost-graph-dev libboost-iostreams-dev libboost-program-options-dev libboost-python-dev libboost-regex-dev libboost-serialization-dev libboost-thread-dev libcoin-dev libeigen3-dev libgts-bin libgts-dev libkdtree++-dev libmedc-dev libocct-data-exchange-dev libocct-ocaf-dev libocct-visualization-dev libopencv-dev libproj-dev libpyside2-dev libqt5opengl5-dev libqt5svg5-dev qtwebengine5-dev libqt5x11extras5-dev libqt5xmlpatterns5-dev libshiboken2-dev libspnav-dev libvtk7-dev libx11-dev libxerces-c-dev libzipios++-dev occt-draw pyside2-tools python3-dev python3-matplotlib python3-packaging python3-pivy python3-ply python3-pyside2.qtcore python3-pyside2.qtgui python3-pyside2.qtsvg python3-pyside2.qtwidgets python3-pyside2.qtnetwork python3-pyside2.qtwebengine python3-pyside2.qtwebenginecore python3-pyside2.qtwebenginewidgets python3-pyside2.qtwebchannel python3-markdown python3-git python3-pyside2uic qtbase5-dev qttools5-dev swig
}}

NOTA: En algunas versiones de Ubuntu y algunas versiones de Qt, obtendrá un error de que no se puede encontrar python3-pyside2uic - en esos sistemas puede omitirlo con seguridad. En Ubuntu 20.04 tendrá que añadir `pyqt5-dev-tools`. Puede encontrar más información en [esta discusión del foro](https://forum.freecadweb.org/viewtopic.php?t=51324).


<div class="mw-collapsible mw-collapsed" style="background-color:#e0e0e0">

#### Comando único para Python 2 y Qt4 

Esto no se recomienda para las instalaciones más recientes, ya que tanto Python 2 como Qt4 están obsoletos.


<div class="mw-collapsible-content">


{{Code|lang=bash|code=
sudo apt install cmake debhelper dh-exec dh-python libboost-date-time-dev libboost-dev libboost-filesystem-dev libboost-graph-dev libboost-iostreams-dev libboost-program-options-dev libboost-python-dev libboost-regex-dev libboost-serialization-dev libboost-thread-dev libcoin80-dev libeigen3-dev libgts-bin libgts-dev libkdtree++-dev libmedc-dev libocct-data-exchange-dev libocct-ocaf-dev libocct-visualization-dev libopencv-dev libproj-dev libpyside-dev libqt4-dev libqt4-opengl-dev libqtwebkit-dev libshiboken-dev libspnav-dev libvtk6-dev libx11-dev libxerces-c-dev libzipios++-dev lsb-release occt-draw pyside-tools python-dev python-matplotlib python-pivy python-ply swig
}}

Los usuarios de Ubuntu 16.04 por favor vean también la discusión de compilación en el foro: [Compilación en Linux (Kubuntu): CMake no puede encontrar VTK](http://forum.freecadweb.org/viewtopic.php?f=4&t=16292).


</div>


</div>


</div>


</div>


<div class="mw-collapsible mw-collapsed toccolours">

### Raspberry Pi 


<div class="mw-collapsible-content">

Siga los mismos pasos que en Debian y Ubuntu.


<div class="mw-translate-fuzzy">

Hay problemas reportados cuando se intenta compilar en Raspbian con Python 3 y Qt5, pero la combinación Python 3 y Qt4 parece funcionar para versiones antiguas de FreeCAD.


</div>


<div class="mw-translate-fuzzy">

Para las nuevas versiones de FreeCAD la compilación con Py3/Qt5 tiene éxito si el sistema operativo instalado es Ubuntu 20.04.


</div>


<div class="mw-translate-fuzzy">

Debido a diferentes problemas con Qt, en esta versión no se encontrarán las herramientas normales de PySide.


</div>


{{Code|lang=bash|code=
E: Unable to locate package python3-pyside2uic
}}

En este caso, podemos instalar los paquetes desde PyQt y crear enlaces simbólicos a las herramientas necesarias. {{Code|lang=bash|code=
sudo apt-get install pyqt5-dev
sudo apt-get install pyqt5-dev-tools
cd /usr/bin/
ln -s pyrcc5 pyside2-rcc
ln -s pyuic5 pyside2-uic
}}

Ahora la compilación puede continuar. {{Code|lang=bash|code=
cd freecad-build/
cmake ../freecad-source -DBUILD_QT5=ON -DPYTHON_EXECUTABLE=/usr/bin/python3 -DUSE_PYBIND11=ON
make -j2
}}

La opción `-j` de `make` no debe ser más de 3 porque la Raspberry Pi tiene memoria limitada. Tardará varias horas en compilar, por lo que es mejor hacerlo durante la noche.

Más información, [FreeCAD y Raspberry Pi 4](https://forum.freecadweb.org/viewtopic.php?f=42&t=37458&start=160#p396652).


</div>


</div>


<div class="mw-collapsible mw-collapsed toccolours">

### Fedora


<div class="mw-collapsible-content">

There is a bug in cmake distributed by Fedora 34/35 which results in cmake failing to find the opencascade libraries. This can easily be fixed by making one minor change to the top level cmake file of opencascade installed on Fedora. Details here: <https://bugzilla.redhat.com/show_bug.cgi?id=2083568>.

Near the top of the file **OpenCASCADEConfig.cmake**, change the following line to use {{Incode|REAL_PATH()}}. This fixes a bug introduced by the use of a symlink from {{Incode|/lib}} to {{Incode|/usr/lib}} of Fedora, which causes cmake to fail.

This file is usually installed in **/usr/lib64/cmake/opencascade/OpenCASCADEConfig.cmake**.


{{Code|lang=bash|code=
get_filename_component (OpenCASCADE_INSTALL_PREFIX "${OpenCASCADE_INSTALL_PREFIX}" PATH)
}}

change this to:


{{Code|lang=bash|code=
file (REAL_PATH ${OpenCASCADE_INSTALL_PREFIX} OpenCASCADE_INSTALL_PREFIX)
}}

This trivial change needs to be made inside the build directory once cmake has been run and failed. Re-running cmake will then correctly detect the OCCT libraries in the normal way.


<div class="mw-translate-fuzzy">

Necesita los siguientes paquetes :


</div>

-   gcc-c++ (or possibly another C++ compiler?)
-   cmake
-   doxygen
-   swig
-   gettext
-   dos2unix
-   desktop-file-utils
-   libXmu-devel
-   freeimage-devel
-   mesa-libGLU-devel
-   opencascade-devel
-   openmpi-devel
-   python3
-   python3-devel
-   python3-pyside2
-   python3-pyside2-devel
-   pyside2-tools
-   boost-devel
-   tbb-devel
-   eigen3-devel
-   qt-devel
-   qt5-qtwebengine-devel
-   qt5-qtxmlpatterns
-   qt5-qtxmlpatterns-devel
-   qt5-qtsvg-devel
-   qt5-qttools-static
-   ode-devel
-   xerces-c
-   xerces-c-devel
-   opencv-devel
-   smesh-devel
-   Coin3
-   Coin3-devel

(Abril 2021, Coin4 y Coin4-devel están disponibles ) (si coin2 es el último disponible para su versión de Fedora, utilice los paquetes de <http://www.zultron.com/rpm-repo/>)

-   SoQt-devel
-   freetype
-   freetype-devel
-   vtk
-   vtk-devel
-   med
-   med-devel


<div class="mw-translate-fuzzy">

Y opcionalmente:


</div>


<div class="mw-translate-fuzzy">

-   libspnav-devel (para el soporte de dispositivos 3Dconnexion como el Space Navigator o el Space Pilot)
-   python3-pivy ( <https://bugzilla.redhat.com/show_bug.cgi?id=458975> Pivy no es obligatorio pero es necesario para el módulo Borrador)


</div>

To install all dependencies at once (tested on fedora 36):


{{Code|lang=bash|code=
sudo dnf install gcc-c++ cmake doxygen swig gettext dos2unix desktop-file-utils libXmu-devel freeimage-devel mesa-libGLU-devel opencascade-devel openmpi-devel python3 python3-devel python3-pyside2 python3-pyside2-devel pyside2-tools boost-devel tbb-devel eigen3-devel qt-devel qt5-qtwebengine-devel qt5-qtxmlpatterns qt5-qtxmlpatterns-devel qt5-qtsvg-devel qt5-qttools-static ode-devel xerces-c xerces-c-devel opencv-devel smesh-devel Coin3 Coin3-devel SoQt-devel freetype freetype-devel vtk vtk-devel med med-devel libspnav-devel python3-pivy python3-markdown python3-GitPython
}}


</div>


</div>


<div class="mw-collapsible mw-collapsed toccolours">

### Gentoo


<div class="mw-collapsible-content">

La forma más fácil de comprobar qué paquetes son necesarios para compilar FreeCAD es comprobarlo a través de portage:

emerge -pv freecad

Esto debería dar una buena lista de paquetes adicionales que necesitas instalar en tu sistema.

Si FreeCAD no está disponible en Portage, está disponible en [waebbl overlay](https://github.com/waebbl/waebbl-gentoo). El rastreador de problemas en el Github de la superposición waebbl puede ayudar a guiar a través de algunos problemas que puede encontrar. El overlay proporciona freecad-9999, que puedes elegir para compilar, o simplemente usar para obtener las dependencias.

layman -a waebbl


</div>


</div>


<div class="mw-collapsible mw-collapsed toccolours">

### openSUSE


<div class="mw-collapsible-content">

#### Tumbleweed

Los siguientes comandos instalarán los paquetes necesarios para construir FreeCAD con Qt5 y Python 3.


```python
zypper in --no-recommends -t pattern devel_C_C++ devel_qt5

zypper in libqt5-qtbase-devel libqt5-qtsvg-devel libqt5-qttools-devel boost-devel swig libboost_program_options-devel libboost_mpi_python3-devel libboost_system-devel libboost_program_options-devel libboost_regex-devel libboost_python3-devel libboost_thread-devel libboost_system-devel libboost_headers-devel libboost_graph-devel python3 python3-devel python3-matplotlib python3-matplotlib-qt5 python3-pyside2 python3-pyside2-devel python3-pivy gcc gcc-fortran cmake occt-devel libXi-devel opencv-devel libxerces-c-devel Coin-devel SoQt-devel freetype2-devel eigen3-devel libode6 vtk-devel libmed-devel hdf5-openmpi-devel openmpi2-devel netgen-devel freeglut-devel libspnav-devel f2c doxygen dos2unix glew-devel
```

El siguiente comando instalará Qt Creator y el depurador de proyectos GNU.


```pythonzypper in libqt5-creator gdb```

Si falta algún paquete, puedes comprobar el archivo Tumbleweed [\"FreeCAD.spec\"](https://build.opensuse.org/package/view_file/openSUSE:Factory/FreeCAD/FreeCAD.spec) en el [Open Build Service](https://build.opensuse.org/package/show/openSUSE:Factory/FreeCAD).

Además, compruebe si hay algún parche que deba aplicar (como [0001-find-openmpi2-include-files.patch](https://build.opensuse.org/package/view_file/openSUSE:Factory/FreeCAD/0001-find-openmpi2-include-files.patch)).

#### Leap

Si hay una diferencia entre los paquetes disponibles en Tumbleweed y Leap, entonces puedes leer el archivo Leap [\"FreeCAD.spec\"](https://build.opensuse.org/package/view_file/openSUSE:Leap:15.0/FreeCAD/FreeCAD.spec) en el [Open Build Service](https://build.opensuse.org/) para determinar los paquetes necesarios.

Ver [piano_jonas guía no oficial \"Compilar en openSUSE\"](https://forum.freecadweb.org/viewtopic.php?f=4&t=49726).


</div>


</div>


<div class="mw-collapsible mw-collapsed toccolours">

### Arch Linux 


<div class="mw-collapsible-content">

Necesitará las siguientes bibliotecas de los depósitos oficiales:

-   boost
-   curl
-   desktop-file-utils
-   glew
-   hicolor-icon-theme
-   jsoncpp
-   libspnav
-   opencascade
-   shiboken2
-   xerces-c
-   pyside2
-   python-matplotlib
-   python-netcdf4
-   python-packaging
-   qt5-svg
-   qt5-webengine
-   cmake
-   eigen
-   git
-   gcc-fortran
-   pyside2-tools
-   swig
-   qt5-tools
-   shared-mime-info
-   coin
-   python-pivy
-   med


```python
sudo pacman -S boost curl desktop-file-utils glew hicolor-icon-theme jsoncpp libspnav opencascade shiboken2 xerces-c pyside2 python-matplotlib python-netcdf4 python-packaging qt5-svg qt5-webengine cmake eigen git gcc-fortran pyside2-tools swig qt5-tools shared-mime-info coin python-pivy med
```


</div>


</div>


<div class="mw-collapsible mw-collapsed toccolours">

### Distribuciones antiguas y no convencionales 


<div class="mw-collapsible-content">

En otras distribuciones, tenemos muy pocos comentarios de los usuarios, por lo que podría ser más difícil encontrar los paquetes necesarios.

Intente primero localizar las bibliotecas necesarias mencionadas en [bibliotecas de terceros](Third_Party_Libraries/es.md) en su gestor de paquetes. Tenga en cuenta que algunas de ellas pueden tener un nombre de paquete ligeramente diferente; busque `nombre`, pero también `libname`, `nombre-dev`, `nombre-devel`, y similares. Si no es posible, intente compilar esas bibliotecas usted mismo.

FreeCAD requiere una versión del compilador GNU g++ igual o superior a la 3.0.0, ya que FreeCAD está escrito principalmente en C++. Durante la compilación se ejecutan algunos scripts de Python, por lo que el intérprete de Python tiene que funcionar correctamente. Para evitar cualquier problema con el enlazador también es una buena idea tener las rutas de las bibliotecas en la variable `LD_LIBRARY_PATH` o en el archivo `ld.so.conf`. Esto ya se hace en las distribuciones modernas de Linux, pero puede ser necesario configurarlo en las más antiguas.


</div>


</div>

### Pivy


<div class="mw-translate-fuzzy">

[Pivy](Pivy/es.md) (envoltorios de Python para Coin3d) no es necesario para construir FreeCAD o para iniciarlo, pero es necesario como una dependencia en tiempo de ejecución por el [Ambiente de Trabajo Borrador](Draft_Workbench/es.md). Si no vas a utilizar este ambiente de trabajo, no necesitarás Pivy. Sin embargo, ten en cuenta que el Ambiente de Trabajo Borrador es utilizado internamente por otros ambientes de trabajo, como [Arquitectura](Arch_Workbench/es.md) y [BIM](BIM_Workbench/es.md), por lo que Pivy necesita ser instalado para utilizar estos ambientes de trabajo también.


</div>

En noviembre de 2015 la versión obsoleta de Pivy incluida con el código fuente de FreeCAD ya no compilará en muchos sistemas. Esto no es un gran problema ya que normalmente deberías obtener Pivy desde el gestor de paquetes de tu distribución; si no puedes encontrar Pivy, puede que tengas que compilarlo tú mismo, ver [Instrucciones de compilación de Pivy](Extra_python_modules/es#Pivy.md).

### Símbolos de depuración 

Para solucionar los fallos en FreeCAD, es útil tener los símbolos de depuración de las bibliotecas de dependencia importantes como Qt. Para ello, intenta instalar los paquetes de dependencia que terminan con `-dbg`, `-dbgsym`, `-debuginfo` o similares, dependiendo de tu distribución de Linux.

Para Ubuntu, es posible que tenga que habilitar repositorios especiales para poder ver e instalar estos paquetes de depuración con el gestor de paquetes. Consulte [Debug Symbol Packages](https://wiki.ubuntu.com/Debug_Symbol_Packages) para obtener más información.

## Compila FreeCAD 


**Compilación contra Python 2 y Qt4 ya no está bien soportada, y a partir de la versión 0.20 ya no está soportada en absoluto. Debería compilar contra Python 3 y Qt5. 0.20 requiere al menos Python3.6 y Qt 5.9.**

FreeCAD utiliza CMake como su principal sistema de compilación, ya que está disponible en los principales sistemas operativos. La compilación con CMake es normalmente muy simple y ocurre en dos pasos.

1.  CMake comprueba que todos los programas y bibliotecas necesarios están presentes en tu sistema, y genera un `Makefile` que se configura para el segundo paso. FreeCAD tiene varias opciones de configuración entre las que elegir, pero viene con unos valores por defecto razonables. Algunas alternativas se detallan a continuación.
2.  La compilación propiamente dicha, que se realiza con el programa `make`, que genera los ejecutables de FreeCAD.

Dado que FreeCAD es una aplicación de gran tamaño, la compilación de todo el código fuente puede tardar entre 10 minutos y una hora, dependiendo de tu CPU y del número de núcleos de la CPU utilizados para la compilación.

Puedes construir el código dentro o fuera del directorio de origen. La construcción fuera de la fuente es generalmente la mejor opción.

### Creación fuera-fuente 

Construir en una carpeta separada es más conveniente que construir en el mismo directorio donde se encuentra el código fuente, ya que cada vez que se actualiza el código fuente CMake puede determinar inteligentemente qué archivos han cambiado, y recompilar sólo lo que se necesita. Esto es muy útil cuando se prueban diferentes ramas de Git, ya que no se confunde el sistema de construcción.

Para construir fuera-fuente, simplemente crea un directorio de construcción, `freecad-build`, distinto de tu carpeta de fuentes de FreeCAD, `freecad-source`; entonces desde este directorio de construcción apunta `cmake` a la carpeta de fuentes correcta. Puedes usar `cmake-gui` o `ccmake` en lugar de `cmake` en las instrucciones de abajo también. Una vez que `cmake` termine de configurar el entorno, utilice `make` para iniciar la compilación real.


{{Code|lang=bash|code=
mkdir freecad-build
cd freecad-build
cmake ../freecad-source
make -j$(nproc --ignore=2)
}}

Nota: si está compilando la rama de lanzamiento 0.19, debe especificar explícitamente que está compilando con Qt5 y Python 3 \-- sustituya el comando cMake anterior por: {{Code|lang=bash|code=
cmake ../freecad-source -DBUILD_QT5=ON -DPYTHON_EXECUTABLE=/usr/bin/python3
}}

La opción `-j` de `make` controla cuántos trabajos (archivos) se compilan en paralelo. El programa `nproc` imprime el número de núcleos de la CPU en su sistema; usándolo junto con la opción `-j` puede elegir procesar tantos archivos como núcleos tenga, para acelerar la compilación general del programa. En el ejemplo anterior, utilizará todos los núcleos de tu sistema excepto dos; esto mantendrá a tu ordenador respondiendo para otros usos mientras la compilación se realiza en segundo plano. El ejecutable de FreeCAD aparecerá finalmente en el directorio `freecad-build/bin`. Ver también [Compilación (aceleración)](Compiling_(Speeding_up)/es.md) para mejorar la velocidad de compilación.

### Resolving cmake issues 

If you have done an out-of-source build before and get stuck on a dependency that is not recognized or can\'t seem to be resolved, try the following:

-   Delete the contents of the build directory before running cmake again. FreeCAD is a rapidly moving target, you may be tripping over cached cmake information that points at an older version than the new repository head can use. Clearing the cache may allow cmake to recover and recognize the version you actually need.

-   If cmake complains about missing a specific file, use a tool such as \"apt-file search\", or its equivalent in other package systems, to discover what package that file belongs to and install it. Bear in mind that you are likely to need the -dev version of the package that carries header or config files files required for FreeCAD to use the package.

### Compiling against GNU libc 2.34 and later 

GNU libc 2.34 introduces a change to the library that can cause builds on some Linux systems to fail with an error like:


{{Code|lang=bash|code=
No rule to make target '/usr/lib/x86_64-linux-gnu/libdl.so
}}

To resolve this, a symbolic link must be manually created from the (now empty) system-installed libdl.so.\* to the location your compiler says it is looking for the file. For example (if the actual installed copy of libdl.so on your system is /usr/lib/x86_64-linux-gnu/libdl.so.2):


{{Code|lang=bash|code=
sudo ln -s /usr/lib/x86_64-linux-gnu/libdl.so.2 /usr/lib/x86_64-linux-gnu/libdl.so
}}

Adapt the command for the structure of your system by searching for libdl.so\* and linking it to the appropriate location.

### Creación interna fuentes 

Las composiciones en fuente están bien si quieres compilar una versión de FreeCAD rápidamente, y no tienes intención de actualizar el código fuente a menudo. En este caso, puedes eliminar el programa compilado y el código fuente simplemente borrando una sola carpeta.

Cambie al directorio fuente, y apunte `cmake` al directorio actual (denotado por un solo punto):


{{Code|lang=bash|code=
cd freecad-source
cmake . -DPYTHON_EXECUTABLE=/usr/bin/python3
make -j$(nproc --ignore=2)
}}

El ejecutable de FreeCAD residirá entonces en el directorio `freecad-source/bin`.

### Cómo reparar su directorio de código fuente 

Si accidentalmente realizaste una compilación dentro del directorio de código fuente, o agregaste archivos extraños, y quisieras restaurar el contenido a sólo el código fuente original, puedes realizar los siguientes pasos.


{{Code|lang=bash|code=
> .gitignore
git clean -df
git reset --hard HEAD
}}

La primera línea borra el archivo `.gitignore`. Esto asegura que los siguientes comandos de limpieza y reinicio afectarán a todo el directorio y no ignorarán los elementos que coincidan con las expresiones en `.gitignore`. La segunda línea borra todos los archivos y directorios que no son rastreados por el repositorio git; luego el último comando restablecerá cualquier cambio en los archivos rastreados, incluyendo el primer comando que borró el archivo `.gitignore`.

Si no borra el directorio de fuentes, las siguientes ejecuciones de `cmake` pueden no capturar las nuevas opciones del sistema si el código cambia.

### Configuración

Pasando diferentes opciones a `cmake`, puedes cambiar cómo se compila FreeCAD. La sintaxis es la siguiente.


```python
cmake -D <var>:<type>=<value> $SOURCE_DIR
```

Donde `$SOURCE_DIR` es el directorio que contiene el código fuente. El `<tipo>` puede omitirse en la mayoría de los casos. El espacio después de la opción `-D` también puede omitirse.

Por ejemplo, para evitar construir el [Ambiente de trabajo MEF](FEM_Workbench/es.md):


{{Code|lang=bash|code=
cmake -D BUILD_FEM:BOOL=OFF ../freecad-source
cmake -DBUILD_FEM=OFF ../freecad-source
}}

Todas las variables posibles están listadas en el archivo `InitializeFreeCADBuildOptions.cmake`, ubicado en el directorio `cMake/FreeCAD_Helpers`. En este archivo, busque la palabra `option` para llegar a las variables que se pueden establecer, y ver sus valores por defecto.

    # ==============================================================================
    # =================   All the options for the build process    =================
    # ==============================================================================

    option(BUILD_FORCE_DIRECTORY "The build directory must be different to the source directory." OFF)
    option(BUILD_GUI "Build FreeCAD Gui. Otherwise you have only the command line and the Python import module." ON)
    option(FREECAD_USE_EXTERNAL_ZIPIOS "Use system installed zipios++ instead of the bundled." OFF)
    option(FREECAD_USE_EXTERNAL_SMESH "Use system installed smesh instead of the bundled." OFF)
    ...

Alternativamente, utilice el comando `cmake -LH` para listar la configuración actual, y por tanto todas las variables que pueden ser modificadas. También puede instalar y utilizar `cmake-gui` para lanzar una interfaz gráfica que muestra todas las variables que pueden ser modificadas. En las siguientes secciones enumeramos algunas de las opciones más relevantes que puede querer utilizar.

#### Para una creación de depuración 

Crea una compilación `Debug` para solucionar fallos en FreeCAD. Ten en cuenta que con esta compilación el [Croquizador](Sketcher_Workbench/es.md) se vuelve muy lento con croquis complejos.


{{Code|lang=bash|code=
cmake -DPYTHON_EXECUTABLE=/usr/bin/python3 -DCMAKE_BUILD_TYPE=Debug ../freecad-source
}}

#### Para una creación de versión 

Crea una compilación `Release` para probar el código que no se bloquea. Una compilación `Release` se ejecutará mucho más rápido que una compilación `Debug`.


{{Code|lang=bash|code=
cmake -DPYTHON_EXECUTABLE=/usr/bin/python3 -DCMAKE_BUILD_TYPE=Release ../freecad-source
}}

#### Creación contra Python 3 y Qt5 


<div class="mw-translate-fuzzy">

Por defecto, FreeCAD 0.19 y anteriores construyen para Python 2 y Qt4. Dado que estos dos paquetes son obsoletos, es mejor construir para Python 3 y Qt5. El soporte para Python 2 y Qt4 se ha eliminado en FreeCAD 0.20 y no es necesario activar explícitamente Qt5 y Python 3 si se compilan las últimas versiones de desarrollo.


</div>


<div class="mw-translate-fuzzy">

Por 0.20_dev:


</div>


{{Code|lang=bash|code=
cmake ../freecad-source
}}


<div class="mw-translate-fuzzy">

Tenga en cuenta que al cambiar entre las compilaciones 0.19 y 0.20, puede ser necesario borrar CMakeCache.txt antes de ejecutar cmake.


</div>

#### Creación para una versión específica de Python 


<div class="mw-translate-fuzzy">

Si el ejecutable `python` por defecto en tu sistema es un enlace simbólico a Python 2, `cmake` intentará configurar FreeCAD para esta versión. Puedes elegir otra versión de Python dando la ruta a un ejecutable específico:


</div>


{{Code|lang=bash|code=
cmake -DPYTHON_EXECUTABLE=/usr/bin/python3 ../freecad-source
}}

Si eso no funciona, es posible que tenga que definir variables adicionales que apunten a las bibliotecas de Python deseadas y a los directorios de inclusión:


{{Code|lang=bash|code=
cmake -DPYTHON_EXECUTABLE=/usr/bin/python3.6 \
    -DPYTHON_INCLUDE_DIR=/usr/include/python3.6m \
    -DPYTHON_LIBRARY=/usr/lib/x86_64-linux-gnu/libpython3.6m.so \
    -DPYTHON_PACKAGES_PATH=/usr/lib/python3.6/site-packages/ \
    ../freecad-source
}}

Es posible tener varias versiones independientes de Python en el mismo sistema, por lo que las ubicaciones y números de versión de sus archivos de Python dependerán de su distribución particular de Linux. Utilice `python3 -V` para mostrar la versión de Python que está utilizando actualmente; sólo son necesarios los dos primeros números; por ejemplo, si el resultado es `Python 3.6.8`, necesita especificar los directorios que se refieren a la versión 3.6. Si no conoce los directorios correctos, intente buscarlos con el comando `locate`.


```python
locate python3.6
```

Puede utilizar `python3 -m site` en un terminal para determinar el directorio `site-packages`, o `dist-packages` para los sistemas Debian.

Some components of FreeCAD, such as PySide, try to autodetect the most recent Python version installed on your system, which might fail if it is different from what you entered above. Adding the following cMake option might solve the issue:


{{Code|lang=bash|code=
-DPython3_FIND_STRATEGY=LOCATION
}}

#### Creación con Qt Creator contra Python 3 y Qt5 

1\. Inicie Qt Creator.

2\. Haga clic en **Abierto Proyecto**.

3\. Navega hasta el directorio donde está el código fuente, `freecad-source/`, y elige el archivo `CMakeLists.txt` más alto.

4\. Al seleccionar el archivo, se ejecutará automáticamente `cmake` en él, pero puede fallar si las opciones apropiadas no están correctamente configuradas.

5\. Vaya a **Projects → Build & Run → Imported Kit → Build → Build Settings → CMake**. Establezca el directorio de compilación adecuado, `freecad-build/`.

6\. Establezca las variables apropiadas en el diálogo Clave-Valor, de tipos `String` y `Bool`. 
```python
PYTHON_EXECUTABLE=/usr/bin/python3
```

7\. Si las variables no cargan el proyecto correctamente, puede que tenga que ir a **Projects → Manage Kits → Kits → Default (o Kit importado o similar) → CMake Configuration**. A continuación, pulse **Cambiar**, y añada la configuración adecuada como se ha descrito anteriormente. Puede que tenga que añadir más variables sobre las rutas de Python, si no se encuentra el Python del sistema. 
```python
PYTHON_EXECUTABLE:STRING=/usr/bin/python3.7
PYTHON_INCLUDE_DIR:STRING=/usr/include/python3.7m
PYTHON_LIBRARY:STRING=/usr/lib/x86_64-linux-gnu/libpython3.7m.so
PYTHON_PACKAGES_PATH:STRING=/usr/lib/python3.7/site-packages
```

7.1. Pulse **Aplicar** y luego **Aceptar**.

7.2. Asegúrese de que el resto de las opciones están correctamente configuradas, por ejemplo, **Versión de Qt** debe ser una versión presente instalada en el sistema, como `Qt 5.9.5 en PATH (qt5)`.

Pulse **Aplicar** y luego **Aceptar** para cerrar la configuración.

El programa `cmake` debería ejecutarse automáticamente de nuevo, y debería rellenar todo el diálogo Clave-Valor con todas las variables configurables.

8\. Vaya a **Projects → Build & Run → Imported Kit → Run → Run Settings → Run Configuration** y elija `FreeCADMain` para compilar la versión gráfica de FreeCAD, o `FreeCADMainCMD` para compilar sólo la versión de línea de comandos.

9\. Finalmente, vaya al menú **Build → Build Project "FreeCAD"**. Si se trata de una nueva compilación, debería tardar varios minutos, incluso horas, dependiendo del número de procesadores que tengas disponibles.

#### Qt designer complemento 

Si quieres desarrollar código Qt para FreeCAD, necesitarás el plugin Qt Designer que proporciona todos los widgets personalizados de FreeCAD.

Entra en un directorio auxiliar del código fuente, ejecuta `qmake` con el archivo de proyecto indicado para crear un `Makefile`; luego ejecuta `make` para compilar el plugin.


{{Code|lang=bash|code=
cd freecad-source/src/Tools/plugins/widget
qmake plugin.pro
make
}}

Si estás compilando para Qt5, asegúrate de que el binario `qmake` es el correspondiente a esta versión, para que el `Makefile` resultante contenga la información necesaria para Qt5.


{{Code|lang=bash|code=
cd freecad-source/src/Tools/plugins/widget
$QT_DIR/bin/qmake plugin.pro
make
}}

donde `$QT_DIR` es el directorio que almacena las bibliotecas binarias de Qt, por ejemplo, `/usr/lib/x86_64-linux-gnu/qt5`.

La biblioteca creada es `libFreeCAD_widgets.so`, que debe copiarse en `$QT_DIR/plugins/designer`.


{{Code|lang=bash|code=
sudo cp libFreeCAD_widgets.so $QT_DIR/plugins/designer
}}

#### Pivy externo o interno 

Anteriormente, una versión de Pivy estaba incluida en el código fuente de FreeCAD (interno). Si querías usar la copia de Pivy de tu sistema (externo), necesitabas usar -DFREECAD_USE_EXTERNAL_PIVY=1.

El uso de Pivy externo se convirtió en el valor por defecto durante el desarrollo de FreeCAD 0.16, por lo que ya no es necesario configurar esta opción manualmente.

#### Documentación de Doxygen 

Si tienes Doxygen instalado puedes construir la documentación del código fuente. Consulte [documentación de origen](source_documentation/es.md) para obtener instrucciones.

### Documentación adicional 

El código fuente de FreeCAD es muy extenso, y con CMake es posible configurar muchas opciones. Aprender a usar CMake completamente puede ser útil para elegir las opciones adecuadas para tus necesidades particulares.

-   [CMake Documentación de referencia](https://cmake.org/documentation/) de Kitware.
-   [Cómo construir un proyecto basado en CMake](https://preshing.com/20170511/how-to-build-a-cmake-based-project/) (blog) por Preshing sobre programación.
-   [Aprende el lenguaje de scripting de CMake en 15 minutos](https://preshing.com/20170522/learn-cmakes-scripting-language-in-15-minutes/) (blog) por Preshing sobre programación.

### Hacer un paquete debian 

Si planea construir un paquete Debian a partir de las fuentes, necesita instalar primero ciertos paquetes:


{{Code|lang=bash|code=
sudo apt install dh-make devscripts lintian
}}

Vaya al directorio de FreeCAD y llame a


{{Code|lang=bash|code=
debuild
}}

Una vez construido el paquete, puede utilizar `lintian` para comprobar si el paquete contiene errores


{{Code|lang=bash|code=
lintian freecad-package.deb
}}

#### \*.deb package with checkinstall 

The Debian script `checkinstall` allows to create a \*.deb package that can be installed and removed with the standard `dpkg` commands. It may need to be installed first (on Ubuntu use `sudo apt install checkinstall`). It\'s interactive and asks for the required information providing helpful defaults. During the process the package is installed and a \*.deb file and a backup archive are created.

It\'s a good idea to define a name and a short description for the package. The name must be entered to uninstall it again and the desription will be listed by `dpkg -l`. The default name \"build\" is not very informative.

Example:


{{Code|lang=bash|code=
cd freecad-source/freecad-build
cmake ..
make
sudo checkinstall                                  # e.g. name=freecad-test1
}}

The result is a \*.deb file in the freecad-build folder. `checkinstall` will install the build by default. This is how you can install or uninstall it:


{{Code|lang=bash|code=
cd freecad-source/freecad-build
 ls <nowiki>|</nowiki>grep freecad
        freecad-test1_20220814-1_amd64.deb
 sudo dpkg -i freecad-test1_20220814-1_amd64.deb   # install
 dkpg -l <nowiki>|</nowiki>grep freecad                             # find by name
 sudo dpkg -r freecad-test1                        # uninstall by name
}}

## Actualización del código fuente 

El sistema CMake permite actualizar de forma inteligente el código fuente, y sólo recompilar lo que ha cambiado, haciendo que las compilaciones posteriores sean más rápidas.

Muévete a la ubicación donde el código fuente de FreeCAD fue descargado por primera vez, y saca el nuevo código:


{{Code|lang=bash|code=
cd freecad-source
git pull
}}

A continuación, muévete al directorio de compilación donde el código fue compilado inicialmente, y ejecuta `cmake` especificando el directorio actual (denotado por un punto); luego activa la re-compilación con `make`.


{{Code|lang=bash|code=
cd ../freecad-build
cmake .
make -j$(nproc --ignore=2)
}}

## Uninstalling the source code 

In case the compiled source code was installed with `sudo make install` (for Debian) the files were copied to the **/usr/local** folder into several subfolders. For uninstallation the file **install_manifest.txt** can be used. It has been created into the build folder during compilation and contains all installed files. As long as this file exists, the installation can be uninstalled.


{{Code|lang=bash|code=
cd freecad-source/freecad-build
xargs sudo rm < install_manifest.txt
}}

## Solución de problemas 

### Para sistemas de 64 bits 

Cuando se compone FreeCAD para 64 bits hay un problema conocido con el paquete OpenCASCADE (OCCT) de 64 bits. Para que FreeCAD funcione correctamente puede ser necesario ejecutar el script `configure` y establecer `CXXFLAGS` adicionales:


{{Code|lang=bash|code=
./configure CXXFLAGS="-D_OCC64"
}}

Para los sistemas basados en Debian, esta opción no es necesaria cuando se utilizan los paquetes precompilados de OpenCASCADE porque éstos establecen el `CXXFLAGS` adecuado internamente.

## Scripts de creación automática 

Aquí está todo lo que necesitas para una construcción completa de FreeCAD. Es un enfoque de un solo script y funciona en una distribución de Linux recién instalada. Los comandos pedirán la contraseña de root para la instalación de paquetes y nuevos repositorios online. Estos scripts deberían funcionar en versiones de 32 y 64 bits. Están escritos para diferentes versiones, pero también es probable que funcionen en una versión posterior con o sin cambios importantes.

Si tienes un script de este tipo para tu distribución preferida, por favor discútelo en el [foro de FreeCAD](https://forum.freecadweb.org/viewforum.php?f=21&sid=e3c22dca9da076fefb56b1d5c5fb3134) para que podamos incorporarlo.


<div class="mw-collapsible mw-collapsed toccolours">

### Ubuntu


<div class="mw-collapsible-content">

Estos scripts proporcionan una forma fiable de instalar el conjunto correcto de dependencias necesarias para construir y ejecutar FreeCAD en Ubuntu. Hacen uso de los archivos de paquetes personales de Ubuntu (PPA), y deberían funcionar en cualquier versión de Ubuntu a la que se dirija el PPA. El [freecad-daily](https://launchpad.net/~freecad-maintainers/+archive/ubuntu/freecad-daily) PPA se dirige a versiones recientes de Ubuntu, mientras que el [freecad-stable](https://launchpad.net/~freecad-maintainers/+archive/ubuntu/freecad-stable) PPA se dirige a las versiones oficialmente soportadas de Ubuntu.

Este script instala la instantánea diaria compilada de FreeCAD y sus dependencias. Añade el repositorio diario, obtiene las dependencias para construir esta versión, e instala los paquetes necesarios. Después procede a sacar el código fuente en un directorio particular, crea un directorio de compilación y cambia en él, configura el entorno de compilación con `cmake`, y finalmente construye el programa completo con `make`. Guarda el script en un archivo, hazlo ejecutable y ejecútalo, pero no utilices `sudo`; se pedirán privilegios de superusuario sólo para los comandos seleccionados. Pulsa \"CTRL-ENTER\" para cambiar de canal, \"ALT-SHIFT-D\" para subir, \"ALT-SHIFT-B\" para hacer un resumen, o pulsa \"ALT\" para hacer otros comandos.


{{Code|lang=bash|code=
#!/bin/sh
sudo add-apt-repository --enable-source ppa:freecad-maintainers/freecad-daily && sudo apt-get update
sudo apt-get build-dep freecad-daily
sudo apt-get install freecad-daily

git clone https://github.com/FreeCAD/FreeCAD.git freecad-source
mkdir freecad-build
cd freecad-build
cmake -DPYTHON_EXECUTABLE=/usr/bin/python3 -DFREECAD_USE_PYBIND11=ON ../freecad-source
make -j$(nproc --ignore=2)
}}

Si lo deseas, puedes desinstalar la versión precompilada de FreeCAD (`freecad-daily`) dejando las dependencias en su lugar, sin embargo, dejar este paquete instalado permitirá al gestor de paquetes mantener sus dependencias actualizadas también; esto es sobre todo útil si tienes la intención de seguir el desarrollo de FreeCAD, y actualizar y compilar constantemente las fuentes desde el repositorio Git.

El script anterior asume que quieres compilar la última versión de FreeCAD, por lo que estás usando el repositorio \"diario\" para obtener las dependencias. Sin embargo, puedes obtener las dependencias de la versión \"estable\" de tu versión actual de Ubuntu. Si este es el caso, reemplace la parte superior del script anterior con las siguientes instrucciones. Para Ubuntu 12.04, omita `--enable-source` del comando.


{{Code|lang=bash|code=
#!/bin/sh
sudo add-apt-repository --enable-source ppa:freecad-maintainers/freecad-stable && sudo apt-get update
sudo apt-get build-dep freecad
sudo apt-get install libqt5xmlpatterns5-dev   # Needed for 0.20; should go away on next packaging update 
sudo apt-get install freecad
}}

Una vez que instales el paquete `freecad` desde el repositorio `freecad-stable`, sustituirá al ejecutable de FreeCAD que está disponible en el repositorio de Universe Ubuntu. El ejecutable se llamará simplemente `freecad`, y no `freecad-stable`.


</div>


</div>


<div class="mw-collapsible mw-collapsed toccolours">

### openSUSE 


<div class="mw-collapsible-content">


<div class="mw-translate-fuzzy">

No se necesitan repositorios externos para compilar FreeCAD. Sin embargo, hay una incompatibilidad con python3-devel que debe ser eliminada. FreeCAD puede ser compilado desde GIT


</div>


{{Code|lang=bash|code=
# install needed packages for development
sudo zypper install gcc cmake OpenCASCADE-devel libXerces-c-devel \
python-devel libqt4-devel python-qt4 Coin-devel SoQt-devel boost-devel \
libode-devel libQtWebKit-devel libeigen3-devel gcc-fortran git swig
 
# create new dir, and go into it
mkdir FreeCAD-Compiled 
cd FreeCAD-Compiled
 
# get the source
git clone https://github.com/FreeCAD/FreeCAD.git free-cad
 
# Now you will have a subfolder in this location called free-cad. It contains the source
 
# make another dir for compilation, and go into it
mkdir FreeCAD-Build1
cd FreeCAD-Build1 
 
# build configuration 
cmake ../free-cad
 
# build FreeCAD
make
 
# test FreeCAD
cd bin
./FreeCAD -t 0
}}

Como estás usando git, la próxima vez que desees compilar no tienes que clonar todo, simplemente tira de git y compila una vez más


{{Code|lang=bash|code=
# go into free-cad dir created earlier
cd free-cad
 
# pull
git pull
 
# get back to previous dir
cd ..
 
# Now repeat last few steps from before.
 
# make another dir for compilation, and go into it
mkdir FreeCAD-Build2
cd FreeCAD-Build2
 
# build configuration 
cmake ../free-cad
 
# build FreeCAD
# Note: to speed up build use all CPU cores: make -j$(nproc)
make
 
# test FreeCAD
cd bin
./FreeCAD -t 0
}}


</div>


</div>


<div class="mw-collapsible mw-collapsed toccolours">

### Debian Squeeze 


<div class="mw-collapsible-content">


{{Code|lang=bash|code=
# get the needed tools and libs
sudo apt-get install build-essential python libcoin60-dev libsoqt4-dev \
libxerces-c2-dev libboost-dev libboost-date-time-dev libboost-filesystem-dev \
libboost-graph-dev libboost-iostreams-dev libboost-program-options-dev \
libboost-serialization-dev libboost-signals-dev libboost-regex-dev \
libqt4-dev qt4-dev-tools python2.5-dev \
libsimage-dev libopencascade-dev \
libsoqt4-dev libode-dev subversion cmake libeigen2-dev python-pivy \
libtool autotools-dev automake gfortran
 
# checkout the latest source
git clone https://github.com/FreeCAD/FreeCAD.git freecad
 
# go to source dir
cd freecad
 
# build configuration 
cmake .
 
# build FreeCAD
# Note: to speed up build use all CPU cores: make -j$(nproc)
make
 
# test FreeCAD
cd bin
./FreeCAD -t 0
}}


</div>


</div>


<div class="mw-collapsible mw-collapsed toccolours">

### Fedora 27/28/29 


<div class="mw-collapsible-content">

Enviado por el usuario [http://forum.freecadweb.org/memberlist.php?mode=viewprofile&u=3666 PrzemoF](http://forum.freecadweb.org/memberlist.php?mode=viewprofile&u=3666_PrzemoF.md) en el foro.


{{Code|lang=bash|code=
#!/bin/bash

ARCH=$(arch)

MAIN_DIR=FreeCAD
BUILD_DIR=build

#FEDORA_VERSION=27
#FEDORA_VERSION=28
FEDORA_VERSION=29

PACKAGES="gcc cmake gcc-c++ boost-devel zlib-devel swig eigen3 qt-devel \
shiboken shiboken-devel pyside-tools python-pyside python-pyside-devel xerces-c \
xerces-c-devel OCE-devel smesh graphviz python-pivy python-matplotlib tbb-devel \
 freeimage-devel Coin3 Coin3-devel med-devel vtk-devel"

FEDORA_29_PACKAGES="boost-python2 boost-python3 boost-python2-devel boost-python3-devel"

if [ "$FEDORA_VERSION" = "29" ]; then
    PACKAGES="$PACKAGES $FEDORA_29_PACKAGES"
fi

echo "Installing packages required to build FreeCAD"
sudo dnf -y install $PACKAGES
cd ~
mkdir $MAIN_DIR <nowiki>||</nowiki> { echo "~/$MAIN_DIR already exist. Quitting.."; exit; }
cd $MAIN_DIR
git clone https://github.com/FreeCAD/FreeCAD.git
mkdir $BUILD_DIR <nowiki>||</nowiki> { echo "~/$BUILD_DIR already exist. Quitting.."; exit; }
cd $BUILD_DIR
cmake ../FreeCAD 
make -j$(nproc)
}}


</div>


</div>


<div class="mw-collapsible mw-collapsed toccolours">

### Arch usando AUR 


<div class="mw-collapsible-content">

[Repositorio de usuarios Arch (AUR)](https://aur.archlinux.org/) es una colección de recetas hechas por el usuario para construir paquetes que no están oficialmente soportados por los mantenedores de la distribución / comunidad. Por lo general, son seguros. Puedes ver quién mantiene el paquete y durante cuánto tiempo lo ha hecho. Se recomienda comprobar los archivos de construcción. También hay software que no es de código abierto disponible en esta área, incluso si es mantenido por la compañía oficial propietaria.

Requisito previo : git


<div class="mw-translate-fuzzy">

Pasos :

1.  Abrir un terminal. Opcionalmente, crear un directorio, por ejemplo, {{incode | mkdir git}}. Opcionalmente, cambiar de directorio, por ejemplo, `cd git`.
2.  Clonar el repositorio AUR : `git clone http://aur.archlinux.org/packages/freecad-git`
3.  Entrar en la carpeta del repositorio AUR : `cd freecad-git`
4.  Compilar usando [Arch makepkg](https://wiki.archlinux.org/index.php/Makepkg) : `makepkg -s`. La bandera -s o \--syncdeps también instalará las dependencias necesarias.
5.  Instalar el paquete creado : `makepkg --install` o hacer doble clic en el pkgname-pkgver.pkg.tar.xz dentro de su navegador de archivos.


</div>


<div class="mw-translate-fuzzy">

Para actualizar FreeCAD a la última compilación simplemente repite el paso 3.Actualiza el repo de AUR cuando haya algún cambio de ruptura en la receta o nuevas características usando `git checkout -f` dentro de la carpeta.


</div>



---
![](images/Right_arrow.png) [documentation index](../README.md) > [Developer_Documentation](Category_Developer_Documentation.md) > [Developer](Category_Developer.md) > Compile on Linux/es
