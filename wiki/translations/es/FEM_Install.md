# FEM Install/es
{{TOCright}}

## Introducción


<div class="mw-translate-fuzzy">

Para poder realizar análisis de elementos finitos (FEA) dentro del **<img src="images/Workbench_FEM.svg" width=24px> [Ambiente de trabajo MEF](FEM_Workbench/es.md)**, FreeCAD hace uso de dos programas externos   * uno se utiliza para generar el [MEF Malla](FEM_Mesh/es.md), y el otro para resolver numéricamente el análisis real. Puedes probar si tu instalación de FreeCAD está preparada para el AEF ejecutando el ejemplo [MEF CalculiX Cantilever 3D](FEM_CalculiX_Cantilever_3D/es.md) que se incluye con cada instalación de FreeCAD desde la v0.17.


</div>

<img alt="" src=images/FEM_Workbench_workflow.svg  style="width   *600px;"> 
*Flujo de trabajo del Ambiente de trabajob MEF; el Ambiente de trabajo llama a dos programas externos para realizar el mallado de un objeto sólido, y realizar la solución real del problema de elementos finitos*

### MEF solucionador 

El solucionador por defecto para realizar los cálculos de elementos finitos es [CalculiX](FEM_CalculiX/es.md), un solucionador simple para el análisis de estructuras. FreeCAD escribe un archivo de entrada de CalculiX, inicia el solucionador, y lee la salida, que puede ser presentada visualmente en la ventana gráfica; esto significa que el binario de CalculiX es autónomo e independiente de FreeCAD. Dado que hay muchos programas que pueden generar una malla, **se recomienda instalar el solucionador, y asegurarse de que está funcionando primero**.

Si el solucionador está correctamente instalado, puede ejecutar el único comando `ccx` en el terminal para obtener una respuesta sencilla   *


{{SystemInput|User@PC   *~$ ccx}}


```python
Usage   * CalculiX.exe -i jobname
```

Si el solucionador está instalado, asegúrese de que el Ambiente de trabajo MEF es capaz de encontrar el binario; vaya a **Edición → Preferencias → MEF → CalculiX → Buscar en directorios binarios conocidos**. Si ha compilado el solucionador usted mismo, desmarque la opción, y dé la ruta correcta al binario. Para otros solucionadores que pueden usarse con FreeCAD, vea [MEF Solucionador](FEM_Solver/es.md).

### MEF Generador Malla 


<div class="mw-translate-fuzzy">

Para crear una [MEF Malla](FEM_Mesh/es.md), FreeCAD utiliza [Gmsh](http   *//gmsh.info/) como malla por defecto. Para que esto funcione, Gmsh debe ser instalado por separado de FreeCAD.


</div>

Si el programa está correctamente instalado, puedes ejecutar el comando `gmsh` en el terminal para lanzar la interfaz gráfica del programa. Esta interfaz no es utilizada por FreeCAD pero demuestra que el programa está instalado.


{{SystemInput|User@PC   *~$ gmsh -info}}


```python
Version             * 3.0.6
License             * GNU General Public License
Build OS            * Linux64
Build date          * 20171107
Build host          * lgw01-amd64-034
Build options       * 64Bit Ann Bamg Bfgs Blas(Generic) Blossom C++11 Cgns Chaco DIntegration Dlopen Fltk Gmm Jpeg Kbipack Lapack(Generic) LinuxJoystick MPI MathEx Med Mesh Mmg3d Mpeg NativeFileChooser Netgen ONELAB ONELABMetamodel OpenCASCADE OpenGL OptHom Parser Plugins Png Post Python Solver TetGen/BR Tetgen Voro3D Zlib
FLTK version        * 1.3.4
OCC version         * 6.9.1
MED version         * 3.0.6
Packaged by         * buildd
Web site            * http   *//gmsh.info
Mailing list        * gmsh@onelab.info
```

Si el mallado está instalado, asegúrese de que el Ambiente de trabajo MEF es capaz de encontrar el binario; vaya a **Edición → Preferencias → MEF → Gmsh → Buscar en directorios binarios conocidos**. Si has compilado el mesher tú mismo, desmarca la opción, y da la ruta correcta al binario. Vea [MEF Malla](FEM_Mesh/es.md) para varias posibilidades de obtener una malla válida para el análisis.

### Netgen


**Nota   * El mallado de Netgen se desactivó en marzo de 2017, cuando FreeCAD pasó a utilizar OCCT 7.1. Por favor, edite esta información si Netgen es utilizable de nuevo con la versión estable de FreeCAD.**

En versiones anteriores de FreeCAD, [Netgen](https   *//sourceforge.net/projects/netgen-mesher/) era el mallado por defecto. Para que funcione con el ambiente de trabajo MEF, FreeCAD tenía que ser enlazado con las librerías de Netgen en tiempo de compilación. Cuando FreeCAD pasó de OCE 0.17 a OCCT 7.1, Netgen 4.9.13 no pudo enlazar con esta versión de OCCT, por lo que se decidió dejar de soportar Netgen en el [Ambiente de trabajo MEF](FEM_Workbench/es.md). (se eliminó el botón [Netgen](FEM_MeshNetgenFromShape/es.md)). Sin embargo, poco después algunos usuarios informaron de que habían conseguido parchear Netgen 5.3.1 para que funcionara con OCCT 7.x y FreeCAD.

For historical reference, see the threads   *

-   [(Ubuntu Daily PPA) Transitioning to OCCT7, VTK7\...](https   *//forum.freecadweb.org/viewtopic.php?f=4&t=17501)
-   [Ubuntu Daily Builds PPA now using OCC 7.1.0](https   *//forum.freecadweb.org/viewtopic.php?t=21246)
-   [patching Netgen 5.3.1](https   *//forum.freecadweb.org/viewtopic.php?f=4&t=17501&start=200#p165769) to work with OCCT 7.1
-   [Troubles with gmsh in FEM wb (netgen nostalgy)](https   *//forum.freecadweb.org/viewtopic.php?t=28368)

Despite Netgen not being available from within the [FEM Workbench](FEM_Workbench.md), it can still be used by itself to produce meshes that can then be imported.

Si el programa está correctamente instalado, puede ejecutar el comando `netgen` en el terminal para lanzar la interfaz gráfica del programa.


{{SystemInput|User@PC   *~$ netgen -V}}


```python
NETGEN-6.2-dev
Developed by Joachim Schoeberl at
2010-xxxx Vienna University of Technology
2006-2010 RWTH Aachen University
1996-2006 Johannes Kepler University Linz
Including OpenCascade geometry kernel
Run parallel Netgen with 'mpirun -np xy netgen'
NETGENDIR = .
Tcl header version = 8.6.8
Tcl runtime version = 8.6.8 
using internal Tcl-script
optfile ./ng.opt does not exist - using default values
togl-version    * 2
OCC module loaded
```

## Instalación en Windows 

Los paquetes de FreeCAD disponibles en la página [descargar](Download/es.md) ya incluyen Netgen y CalculiX, por lo que no es necesario instalar ningún software adicional. Algunos enlaces donde conseguir un ejecutable de Calculix mejor que el incluido en FreeCAD se pueden encontrar aquí [ejecutables ccx alternativos](https   *//forum.freecadweb.org/viewtopic.php?f=18&t=58792&start=10#p506164)


<div class="mw-collapsible mw-collapsed toccolours">

## Instalación en Linux 

Las distribuciones de Linux tienen diferentes maneras de instalar el software. Muchas distribuciones tienen repositorios de software y gestores de paquetes; antes de compilar el código fuente, busque en su gestor de paquetes `netgen`, `gmsh`, `calculix-ccx` o `ccx`, e instálelos siguiendo las instrucciones de su propia distribución.


<div class="mw-collapsible-content">

### Ubuntu PPA 

Los archivos de paquetes personales (PPA) [freecad-stable](https   *//launchpad.net/~freecad-maintainers/+archive/ubuntu/freecad-stable) y [freecad-daily](https   *//launchpad.net/~freecad-maintainers/+archive/ubuntu/freecad-daily) proporcionan una versión más reciente de FreeCAD que la disponible en los repositorios oficiales de Ubuntu. Estos PPAs incluyen los paquetes más recientes `netgen`, `gmsh`, y `calculix-ccx`. Ver [Instalación en Linux](Installing_on_Linux/es.md) para más información sobre la configuración de los repositorios.

Si un PPA ya está añadido a su sistema, instale los paquetes de la siguiente manera


```python
sudo apt-get install netgen
sudo apt-get install gmsh
sudo apt-get install calculix-ccx
```

El [freecad-community](https   *//launchpad.net/~freecad-community/+archive/ubuntu/ppa) PPA también proporciona los paquetes `netgen`, `gmsh`, y `calculix-ccx` para pruebas. Si son lo suficientemente estables, pueden añadirse a los repositorios diarios o estables. Los binarios para ccx 2.14 funcionan en Debian Stretch, pero no en Debian Buster debido a problemas de dependencia.


**Nota   ***

el hilo [Ubuntu Repositorio](http   *//forum.freecadweb.org/viewtopic.php?f=18&t=10393) habla de la creación de los paquetes PPA de Ubuntu. En el momento en que se escribió, CalculiX no estaba incluido en los repositorios de Debian, por lo que había varios paquetes personales en Launchpad. Sólo debe instalarse un paquete.

### Arch Linux 

Obtenga el paquete CalculiX del [AUR repositorio](https   *//aur.archlinux.org/packages/calculix/).

### Debian

-   Debian 9 Buster   * los paquetes en el [repository](https   *//packages.debian.org/buster/calculix-ccx) están obsoletos, pero puede utilizar los paquetes del PPA de Ubuntu (`freecad-community`). Ver [Paquete Gmsh 4 disponible para probar en el PPA de Community Extras](https   *//forum.freecadweb.org/viewtopic.php?f=18&t=31360&start=10#p279925) (post del foro).
-   Debian 8 Stretch   * los paquetes del [repository](https   *//packages.debian.org/stretch/calculix-ccx) están obsoletos, pero puede utilizar los paquetes del PPA de Ubuntu (`freecad-community`). Ver [Paquete Gmsh 4 disponible para probar en el PPA de Community Extras](https   *//forum.freecadweb.org/viewtopic.php?f=18&t=31360&p=279925#p260872) (post del foro).
-   Debian 7 Jessie   * instale los paquetes de Debian 8 Stretch usando `dpkg`. Ver [paquete fuente de Debian para Calculix](http   *//forum.freecadweb.org/viewtopic.php?f=4&t=5975&p=110597#p110597) (mensaje en el foro).

### openSUSE

-   [openSUSE   *Science Math](https   *//en.opensuse.org/openSUSE   *Science_Math#Mesh_Generation_and_Related_Tools)
-   [netgen Generador automático de mallas tetraédricas 3D](https   *//software.opensuse.org/package/netgen)
-   [gmsh Un generador de mallas de elementos finitos tridimensionales](https   *//software.opensuse.org/package/gmsh)
-   [ccx Un paquete de elementos finitos de código abierto](https   *//software.opensuse.org/package/ccx)

Los paquetes adicionales suelen instalarse con YAST (abbr. Yet another Setup Tool) (Español   * Otra herramienta de configuración) la herramienta de configuración del sistema operativo Linux, o en cualquier terminal/consola (se requieren derechos de root) con   *

   *   
    
```python
    zypper install netgen
    zypper install gmsh
    zypper install ccx
    
```
    

### CalculiX binary 

Los autores de CalculiX proporcionan un binario precompilado para Linux del solucionador; puede descargarse desde el sitio web de los autores [1](http   *//www.dhondt.de/). Sin embargo, dado que las diferentes distribuciones de Linux tienen diferentes rutas de bibliotecas, lo más probable es que este binario no funcione sin hacer algunos ajustes.

Para utilizar el binario con Fedora 21, consulte el hilo [Cómo hacer que MEF funcione en linux fedora 21](http   *//forum.freecadweb.org/viewtopic.php?f=18&t=10140). Para versiones más recientes de Fedora, debes compilar CalculiX tú mismo.

Si usas este binario, comprueba que el binario es ejecutable, que está en el `$PATH` de tu sistema, y que tienes la versión necesaria de las librerías (`libgfortran`, `liblapack`, `libblas`, etc.) contra las que fue compilado. Esto se menciona en el post del foro [Ambiente de trabajo MEF](http   *//forum.freecadweb.org/viewtopic.php?f=3&t=11830&start=20#p95741).

Usar el comando `ldd` para ver las bibliotecas que están enlazadas por el binario. Instala cualquier dependencia que falte.


{{SystemInput|User@PC   *~$ ldd /usr/bin/ccx}}


```python
linux-vdso.so.1 (0x00007fffbabdc000)
 libspooles.so.2.2 => /usr/lib/x86_64-linux-gnu/libspooles.so.2.2 (0x00007fe9bd042000)
 libpthread.so.0 => /lib/x86_64-linux-gnu/libpthread.so.0 (0x00007fe9bce23000)
 libarpack.so.2 => /usr/lib/x86_64-linux-gnu/libarpack.so.2 (0x00007fe9bcbd9000)
 liblapack.so.3 => /usr/lib/x86_64-linux-gnu/liblapack.so.3 (0x00007fe9bc353000)
 libgfortran.so.4 => /usr/lib/x86_64-linux-gnu/libgfortran.so.4 (0x00007fe9bbf74000)
 libm.so.6 => /lib/x86_64-linux-gnu/libm.so.6 (0x00007fe9bbbd6000)
 libc.so.6 => /lib/x86_64-linux-gnu/libc.so.6 (0x00007fe9bb7e5000)
 libgcc_s.so.1 => /lib/x86_64-linux-gnu/libgcc_s.so.1 (0x00007fe9bb5cd000)
 libmpi.so.20 => /usr/lib/x86_64-linux-gnu/libmpi.so.20 (0x00007fe9bb2db000)
 /lib64/ld-linux-x86-64.so.2 (0x00007fe9bdaa9000)
 libblas.so.3 => /usr/lib/x86_64-linux-gnu/libblas.so.3 (0x00007fe9bb080000)
 libopenblas.so.0 => /usr/lib/x86_64-linux-gnu/libopenblas.so.0 (0x00007fe9b8dda000)
 libquadmath.so.0 => /usr/lib/x86_64-linux-gnu/libquadmath.so.0 (0x00007fe9b8b9a000)
 libopen-rte.so.20 => /usr/lib/x86_64-linux-gnu/libopen-rte.so.20 (0x00007fe9b8912000)
 libopen-pal.so.20 => /usr/lib/x86_64-linux-gnu/libopen-pal.so.20 (0x00007fe9b8660000)
 librt.so.1 => /lib/x86_64-linux-gnu/librt.so.1 (0x00007fe9b8458000)
 libhwloc.so.5 => /usr/lib/x86_64-linux-gnu/libhwloc.so.5 (0x00007fe9b821b000)
 libdl.so.2 => /lib/x86_64-linux-gnu/libdl.so.2 (0x00007fe9b8017000)
 libutil.so.1 => /lib/x86_64-linux-gnu/libutil.so.1 (0x00007fe9b7e14000)
 libnuma.so.1 => /usr/lib/x86_64-linux-gnu/libnuma.so.1 (0x00007fe9b7c09000)
 libltdl.so.7 => /usr/lib/x86_64-linux-gnu/libltdl.so.7 (0x00007fe9b79ff000)
```

### Compilar CalculiX 

Since CalculiX is a standalone application, you can either install a binary packaged for your distribution, or compile it yourself. Any CalculiX version from 2.7.x onwards should work with FreeCAD, and since the code hasn\'t changed much in years, lower versions than 2.7.x may work as well.

Compiling CalculiX is a task for experienced users, requiring editing the Makefiles and build options in different platforms. See the following information   *

-   Debian   * [Debian source package for Calculix](http   *//forum.freecadweb.org/viewtopic.php?f=4&t=5975&start=10), [Gmsh 4 package available for testing in Community Extras PPA](https   *//forum.freecadweb.org/viewtopic.php?f=18&t=31360&start=10#p260506), [Compiling CalculiX ccx on fedora, ubuntu and debian](https   *//forum.freecadweb.org/viewtopic.php?f=18&t=34024).
-   Fedora 27, 28, 29   * [Compiling CalculiX ccx on fedora, ubuntu and debian](https   *//forum.freecadweb.org/viewtopic.php?f=18&t=34024).
-   There is a CMake version of the source package in a [github repository](https   *//github.com/ricortiz/CalculiX-cmake), but at the FreeCAD forums no one has reported if this package works.

### Compilar Netgen 

Netgen was originally linked by FreeCAD when FreeCAD used OCE, the community fork of OpenCascade (OCCT). As OCE lagged in development behind OCCT, FreeCAD switched back to OCCT. This broke the linking of Netgen, which could only link against OCCT 6.9 or OCE 0.18 and below. As OCCT 7.x versions improved the core funcitonality of FreeCAD, it was decided to drop Netgen support in favor of Gmsh.

Since then some success has been achieved patching and linking newer versions of Netgen against OCCT 7.x. Nevertheless, the inclusion of Netgen with FreeCAD is still problematic.


</div>


</div>

## Instalación en MacOSX 


**This information may be out of date. If you are an OSX user, please test and clean up this section**

The OSX [development packages](https   *//github.com/FreeCAD/FreeCAD/releases) of FreeCAD may include Netgen but may not include CalculiX.

See this forum post [FEM on Mac OSX](https   *//forum.freecadweb.org/viewtopic.php?f=18&t=10979&p=198652#p198642) for information on installing CalculiX, and an [updated post](https   *//forum.freecadweb.org/viewtopic.php?f=18&t=10979&start=90#p273746) for more recent information.

CalculiX   *

-   [install CalculiX with brew](https   *//forum.freecadweb.org/viewtopic.php?f=18&t=10979&start=90#p508724)

The following posts may be outdated   *

-   [FEM on Mac OSX, post 1](http   *//forum.freecadweb.org/viewtopic.php?f=18&t=10979)
-   [MacPorts users   * CalculiX port test request](http   *//forum.freecadweb.org/viewtopic.php?f=8&t=14497)

## Más información 


<div class="mw-translate-fuzzy">

El [Ambiente de trabajo MEF](FEM_Workbench/es.md) está en constante desarrollo. La información más reciente se encuentra en el [FreeCAD foro](http   *//www.forum.freecadweb.org/).


</div>

Si tiene problemas para instalar Netgen, Gmsh, o CalculiX, u otra herramienta externa, por favor busque primero en el foro   *

-   [netgen site   *forum.freecadweb.org](https   *//www.google.ch/search?q=sys.append.path+site%3Aforum.freecadweb.org#q=netgen+site   *forum.freecadweb.org)
-   [gmsh site   *forum.freecadweb.org](https   *//www.google.ch/search?q=sys.append.path+site%3Aforum.freecadweb.org#q=gmsh+site   *forum.freecadweb.org)
-   [calculix site   *forum.freecadweb.org](https   *//www.google.ch/search?q=sys.append.path+site%3Aforum.freecadweb.org#q=calculix+site   *forum.freecadweb.org)


{{FEM Tools navi

}}



---
![](images/Right_arrow.png) [documentation index](../README.md) > [FEM](Category_FEM.md) > FEM Install/es
