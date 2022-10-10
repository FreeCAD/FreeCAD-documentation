# FEM Install/ro
{{TOCright}}


<div class="mw-translate-fuzzy">

## Introducere

Pentru a putea face o analiză a elementelor finite (FEA) utilizând [FEM Worbench](FEM_Workbench.md) FreeCAD folosește două programe externe. Una este folosită pentru generarea FEM-Mesh, iar cealaltă pentru rezolvarea sistemului de ecuații. Dacă FreeCAD este configurat pentru a face analiza elementului mecanic finit, ar putea fi ușor verificată prin încărcarea și analizarea unui fișier exemplu. Vedeți [FEM_CalculiX_Cantilever_3D](FEM_CalculiX_Cantilever_3D.md)


</div>

To be able to perform finite element analysis (FEA) within the **<img src="images/Workbench_FEM.svg" width=24px> [FEM Workbench](FEM_Workbench.md)**, FreeCAD makes use of two external programs   * one is used for generating the [FEM Mesh](FEM_Mesh.md), and the other for numerically solving the actual analysis. You can test if your FreeCAD installation is ready for FEA by running the [FEM CalculiX Cantilever 3D](FEM_CalculiX_Cantilever_3D.md) example which is included with every installation of FreeCAD since v0.17.

<img alt="" src=images/FEM_Workbench_workflow.svg  style="width   *600px;"> 
*Workflow of the FEM Workbench; the workbench calls two external programs to perform meshing of a solid object, and perform the actual solution of the finite element problem*


<div class="mw-translate-fuzzy">

##### Rezolvitor FEM 

Acesta este utilizat pentru rezolvarea sistemului de ecuații CalculiX. Vezi <http   *//www.calculix.de/> FreeCAD scrie un fișier de intrare CalculiX pornește CalculiX și citește ieșirea CalculiX. Aceasta înseamnă că calculiX binar este independent și independent de FreeCAD. Din acest motiv și din moment ce există mai multe posibilități de obținere a unui FEM Mesh valid, se recomandă să instalați mai întâi Solver. Până în prezent (mijlocul anului 2015) CalculiX este singurul Solver suportat al modulului FEM.


</div>

The default solver to perform finite element calculations is [CalculiX](FEM_CalculiX.md), a simple solver for analysis of structures. FreeCAD writes a CalculiX input file, starts the solver, and reads the output, which can then be presented visually in the viewport; this means the CalculiX binary is standalone and independent from FreeCAD. Given that there are many programs that can generate a mesh, **it is recommended to install the solver, and make sure it\'s working first**.

If the solver is correctly installed, you may run the single command `ccx` in the terminal to obtain a simple response   *


{{SystemInput|User@PC   *~$ ccx}}


```python
Usage   * CalculiX.exe -i jobname
```

If the solver is installed, make sure the FEM Workbench is able to find the binary; go to **Edit → Preferences → FEM → CalculiX → Search in known binary directories**. If you compiled the solver yourself, untick the option, and give the correct path to the binary. For other solvers that could be used with FreeCAD, see [FEM Solver](FEM_Solver.md).

### FEM mesh generator 

In order to create a [FEM Mesh](FEM_Mesh.md), FreeCAD uses [Gmsh](http   *//gmsh.info/) as the default mesher. Depending or your operating system and your FreeCAD installation Gmsh is bundled with the FreeCAD installation binaries or not. If it is not bundled you can install it separately from FreeCAD and then use the menu **Edit → Preferences → FEM → Gmsh** to set the path to the *gmsh.exe*.

If the program is correctly installed, you may run the command `gmsh` in the terminal to launch the graphical interface of the program. This interface is not used by FreeCAD but demonstrates that the program is installed.


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

If the mesher is installed, make sure the FEM Workbench is able to find the binary; go to **Edit → Preferences → FEM → Gmsh → Search in known binary directories**. If you compiled the mesher yourself, untick the option, and give the correct path to the binary. See [FEM Mesh](FEM_Mesh.md) for various possibilities of obtaining a valid mesh for analysis.

### Netgen


**Note   * The Netgen mesher was disabled in March 2017, when FreeCAD transitioned to using OCCT 7.1. Please edit this information if Netgen is usable again with the stable release of FreeCAD.**

In previous versions of FreeCAD, [Netgen](https   *//sourceforge.net/projects/netgen-mesher/) was the default mesher. For it to work with the FEM Workbench, FreeCAD had to be linked against the Netgen libraries at compile time. As FreeCAD transitioned from OCE 0.17 to OCCT 7.1, Netgen 4.9.13 failed to link against this version of OCCT, so it was decided to drop Netgen support in the [FEM Workbench](FEM_Workbench.md) (the [Netgen button](FEM_MeshNetgenFromShape.md) was removed). Nevertheless, shortly afterwards some users reported success in patching Netgen 5.3.1, so that it worked with OCCT 7.x and FreeCAD.

For historical reference, see the threads   *

-   [(Ubuntu Daily PPA) Transitioning to OCCT7, VTK7\...](https   *//forum.freecadweb.org/viewtopic.php?f=4&t=17501)
-   [Ubuntu Daily Builds PPA now using OCC 7.1.0](https   *//forum.freecadweb.org/viewtopic.php?t=21246)
-   [patching Netgen 5.3.1](https   *//forum.freecadweb.org/viewtopic.php?f=4&t=17501&start=200#p165769) to work with OCCT 7.1
-   [Troubles with gmsh in FEM wb (netgen nostalgy)](https   *//forum.freecadweb.org/viewtopic.php?t=28368)

Despite Netgen not being available from within the [FEM Workbench](FEM_Workbench.md), it can still be used by itself to produce meshes that can then be imported.

If the program is correctly installed, you may run the command `netgen` in the terminal to launch the graphical interface of the program.


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

## Installing on Windows 

The FreeCAD packages available from the [download](Download.md) page already include Netgen and CalculiX, so no additional software needs to be installed. Some links where to get a better Calculix executable than included in FreeCAD can be found here [alternative ccx executables](https   *//forum.freecadweb.org/viewtopic.php?f=18&t=58792&start=10#p506164)


<div class="mw-collapsible mw-collapsed toccolours">

## Installing on Linux 

Linux distributions have different ways of installing software. Many distributions have software repositories and package managers; before compiling source code, look in your package manager for `netgen`, `gmsh`, `calculix-ccx` or `ccx`, and install them following the instructions of your own distribution.


<div class="mw-collapsible-content">

### Ubuntu PPA 

The [freecad-stable](https   *//launchpad.net/~freecad-maintainers/+archive/ubuntu/freecad-stable) and [freecad-daily](https   *//launchpad.net/~freecad-maintainers/+archive/ubuntu/freecad-daily) personal package archives (PPA) provide a more recent version of FreeCAD than is available in the official Ubuntu repositories. These PPAs include the most recent `netgen`, `gmsh`, and `calculix-ccx` packages as well. See [Installing on Linux](Installing_on_Linux.md) for more information on setting up the repositories.

If a PPA is already added to your system, install the packages as follows


```python
sudo apt-get install netgen
sudo apt-get install gmsh
sudo apt-get install calculix-ccx
```

The [freecad-community](https   *//launchpad.net/~freecad-community/+archive/ubuntu/ppa) PPA also provides `netgen`, `gmsh`, and `calculix-ccx` packages for testing. If they are stable enough, they may be added to the daily or stable repositories. The binaries for ccx 2.14 work on Debian Stretch, but not on Debian Buster due to dependency problems.


**Note   ***

the thread [Ubuntu Repository](http   *//forum.freecadweb.org/viewtopic.php?f=18&t=10393) discusses the creation of the Ubuntu PPA packages. At the time it was written, CalculiX was not included in the Debian repositories, so there were several personal packages in Launchpad. Only one package should be installed.

### Arch Linux 

Get the CalculiX package from the [AUR repository](https   *//aur.archlinux.org/packages/calculix/).

### Debian

-   Debian 9 Buster   * the packages in the [repository](https   *//packages.debian.org/buster/calculix-ccx) are outdated, but you can use the packages from the Ubuntu PPA (`freecad-community`). See [Gmsh 4 package available for testing in Community Extras PPA](https   *//forum.freecadweb.org/viewtopic.php?f=18&t=31360&start=10#p279925) (forum post).
-   Debian 8 Stretch   * the packages in the [repository](https   *//packages.debian.org/stretch/calculix-ccx) are outdated, but you can use the packages from the Ubuntu PPA (`freecad-community`). See [Gmsh 4 package available for testing in Community Extras PPA](https   *//forum.freecadweb.org/viewtopic.php?f=18&t=31360&p=279925#p260872) (forum post).
-   Debian 7 Jessie   * install the packages from Debian 8 Stretch using `dpkg`. See [Debian source package for Calculix](http   *//forum.freecadweb.org/viewtopic.php?f=4&t=5975&p=110597#p110597) (forum post).

### openSUSE

-   [openSUSE   *Science Math](https   *//en.opensuse.org/openSUSE   *Science_Math#Mesh_Generation_and_Related_Tools)
-   [netgen Automatic 3D tetrahedral mesh generator](https   *//software.opensuse.org/package/netgen)
-   [gmsh A three-dimensional finite element mesh generator](https   *//software.opensuse.org/package/gmsh)
-   [ccx An open source finite element package](https   *//software.opensuse.org/package/ccx)

Additional packages are typically installed with YAST (abbr. Yet another Setup Tool) the Linux operating system setup and configuration tool, or in any terminal/console (root rights required) with   *

   *   
    
```python
    zypper install netgen
    zypper install gmsh
    zypper install ccx
    
```
    

### CalculiX binary 

The CalculiX authors provide a pre-compiled Linux binary of the solver; it can be downloaded from the [authors\' website](http   *//www.dhondt.de/). However, since different Linux distributions have different library paths, most likely this binary will not work without making some adjustments.

To use the binary with Fedora 21, see the thread [Making FEM run on linux fedora 21](http   *//forum.freecadweb.org/viewtopic.php?f=18&t=10140). For newer Fedora versions, you should compile CalculiX yourself.

If you use this binary, check that the binary is executable, that it is in the executable `$PATH` of your system, and that you have the necessary version of the libraries (`libgfortran`, `liblapack`, `libblas`, etc.) against which it was compiled. This is mentioned in the forum post [FEM WB](http   *//forum.freecadweb.org/viewtopic.php?f=3&t=11830&start=20#p95741).

Use the command `ldd` to see the libraries that are linked by the binary. Install any missing dependency.


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

### Compile CalculiX 

Since CalculiX is a standalone application, you can either install a binary packaged for your distribution, or compile it yourself. Any CalculiX version from 2.7.x onwards should work with FreeCAD, and since the code hasn\'t changed much in years, lower versions than 2.7.x may work as well.

Compiling CalculiX is a task for experienced users, requiring editing the Makefiles and build options in different platforms. See the following information   *

-   Debian   * [Debian source package for Calculix](http   *//forum.freecadweb.org/viewtopic.php?f=4&t=5975&start=10), [Gmsh 4 package available for testing in Community Extras PPA](https   *//forum.freecadweb.org/viewtopic.php?f=18&t=31360&start=10#p260506), [Compiling CalculiX ccx on fedora, ubuntu and debian](https   *//forum.freecadweb.org/viewtopic.php?f=18&t=34024).
-   Fedora 27, 28, 29   * [Compiling CalculiX ccx on fedora, ubuntu and debian](https   *//forum.freecadweb.org/viewtopic.php?f=18&t=34024).
-   There is a CMake version of the source package in a [github repository](https   *//github.com/ricortiz/CalculiX-cmake), but at the FreeCAD forums no one has reported if this package works.

### Compile Netgen 

Netgen was originally linked by FreeCAD when FreeCAD used OCE, the community fork of OpenCascade (OCCT). As OCE lagged in development behind OCCT, FreeCAD switched back to OCCT. This broke the linking of Netgen, which could only link against OCCT 6.9 or OCE 0.18 and below. As OCCT 7.x versions improved the core funcitonality of FreeCAD, it was decided to drop Netgen support in favor of Gmsh.

Since then some success has been achieved patching and linking newer versions of Netgen against OCCT 7.x. Nevertheless, the inclusion of Netgen with FreeCAD is still problematic.


</div>


</div>

## Installing on MacOSX 


**This information may be out of date. If you are an OSX user, please test and clean up this section**

The OSX [development packages](https   *//github.com/FreeCAD/FreeCAD/releases) of FreeCAD may include Netgen but may not include CalculiX.


<div class="mw-translate-fuzzy">

#### CalculiX

A se vedea acest forum post [FreeCAD Fem on OSX](https   *//forum.freecadweb.org/viewtopic.php?f=18&t=10979&p=198652#p198642) cum se instalează CalculiX pe OSX Următoarele informații pot fi depășite   *

-   [forum](http   *//forum.freecadweb.org/viewtopic.php?f=18&t=10979)
-   [forum](http   *//forum.freecadweb.org/viewtopic.php?f=8&t=14497)


</div>

CalculiX   *

-   [install CalculiX with brew](https   *//forum.freecadweb.org/viewtopic.php?f=18&t=10979&start=90#p508724)

The following posts may be outdated   *

-   [FEM on Mac OSX, post 1](http   *//forum.freecadweb.org/viewtopic.php?f=18&t=10979)
-   [MacPorts users   * CalculiX port test request](http   *//forum.freecadweb.org/viewtopic.php?f=8&t=14497)

## Further information 

The [FEM Workbench](FEM_Workbench.md) is under constant development. The most recent information is found in the [FreeCAD forum](http   *//www.forum.freecadweb.org/).

If you have problems installing Netgen, Gmsh, or CalculiX, or another external tool, please search the forum first   *

-   [netgen site   *forum.freecadweb.org](https   *//www.google.ch/search?q=sys.append.path+site%3Aforum.freecadweb.org#q=netgen+site   *forum.freecadweb.org)
-   [gmsh site   *forum.freecadweb.org](https   *//www.google.ch/search?q=sys.append.path+site%3Aforum.freecadweb.org#q=gmsh+site   *forum.freecadweb.org)
-   [calculix site   *forum.freecadweb.org](https   *//www.google.ch/search?q=sys.append.path+site%3Aforum.freecadweb.org#q=calculix+site   *forum.freecadweb.org)


{{FEM Tools navi

}}



---
![](images/Right_arrow.png) [documentation index](../README.md) > [FEM](Category_FEM.md) > FEM Install/ro
