# Compile on Linux/ro
**There is an experimental FreeCAD Docker container that is being tested for FreeCAD development. Read more about it at [[Compile on Docker]]**


{{TOCright}}

## Overview

On recent linux distributions, FreeCAD is generally easy to build, since all dependencies are usually provided by the package manager. It basically involves 3 steps   *

1.  Getting the FreeCAD source code
2.  Getting the dependencies or packages that FreeCAD depends on
3.  Configure with `cmake` and compile with `make`

Below, you\'ll find detailed explanations of the whole process, some [build scripts](#Automatic_build_scripts.md), and particularities you might encounter. If you find anything wrong or out of date in the text below (Linux distributions change often), or if you use a distribution which is not listed, discuss the issue in the [forum](https   *//forum.freecadweb.org/index.php), and help us correct it.

<img alt="" src=images/FreeCAD_source_compilation_workflow.svg  style="width   *800px;">



*General workflow to compile FreeCAD from source. The third party dependencies must be in the system, as well as the FreeCAD source code itself. CMake configures the system so that with a single make instruction the entire project is compiled.*

## Getting the source 

### Git

The best way to get the code is to clone the read-only [Git repository](https   *//github.com/FreeCAD/FreeCAD). For this you need the `git` program which can be easily installed in most Linux distributions. It can also be obtained from the [official website](http   *//git-scm.com/).

Git can be installed via the following command   *


{{Code|lang=bash|code=
sudo apt install git
}}

The following command will place a copy of the latest version of the FreeCAD source code in a new directory called `freecad-source`.


{{Code|lang=bash|code=
git clone https   *//github.com/FreeCAD/FreeCAD.git freecad-source
}}

For more information on using Git and contributing code to the project, see [Source code management](Source_code_management.md).

### Source archive 

Alternatively you can download the source as an [archive](https   *//github.com/FreeCAD/FreeCAD/releases/latest), a `.zip` or `.tar.gz` file, and unpack it in the desired directory.

## Getting the dependencies 

To compile FreeCAD you have to install the requisite dependencies mentioned in [Third Party Libraries](Third_Party_Libraries.md); the packages that contain these dependencies are listed below for different Linux distributions. Please note that the names and availability of the libraries will depend on your particular distribution; if your distribution is old, some packages may be unavailable of have a different name. In this case, look in the [older and non-conventional distributions](#Older_and_non-conventional_distributions.md) section below.

Once you have all the dependencies installed, proceed to [compile FreeCAD](#Compile_FreeCAD.md).

Please note that FreeCAD\'s source code is around 500 MB in size; it may be three times as big if you clone the Git repository with its entire modification history. Getting all dependencies may require downloading 500 MB or more of new files; when these files are unpacked they may require 1500 MB or more in space. Also beware that the compilation process may generate up to 1500 MB of additional files as the system copies and modifies the entire source code. Therefore, be sure you have enough free space in your hard drive, at least 4 GB, when attempting compilation.


<div class="mw-collapsible mw-collapsed toccolours">

### Debian and Ubuntu 


<div class="mw-collapsible-content">

On Debian-based systems (Debian, Ubuntu, Mint, etc.) it is quite easy to get all needed dependencies installed. Most of the libraries are available via `apt` or the Synaptic package manager.

If you already installed FreeCAD from the official repositories, you can install its build dependencies with this single line of code in a terminal   *


```python
sudo apt build-dep freecad
```

However, if the version of FreeCAD in the repositories is old, the dependencies may be the wrong ones to compile a recent version of FreeCAD. Therefore, please verify that you have installed the following packages.

These packages are essential for any sort of compilation to succeed   *

-    `build-essential`, installs the C and C++ compilers, the C development libraries, and the `make` program.

-    `cmake`, essential tool to configure the source of FreeCAD. You may also wish to install `cmake-gui` and `cmake-curses-gui` for a graphical option.

-    `libtool`, essential tools to produce shared libraries.

-    `lsb-release`, the standard base reporting utility is normally already installed in a Debian system, and allows you to programmatically distinguish between a pure Debian installation or a variant, such as Ubuntu or Linux Mint. Do not remove this package, as many other system packages may depend on it.

Compilation of FreeCAD uses the Python language, and it\'s also used at runtime as a scripting language. If you are using a Debian based distribution the Python interpreter is normally already installed.

-    `python3`
    

-    `swig`, the tool that creates interfaces between C++ code and Python.

Please check that you have Python 3 installed. Python 2 was obsoleted in 2019, so new development in FreeCAD is not tested with this version of the language.

The Boost libraries need to be installed   *

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
    

The Coin libraries need to be installed   *

-    `libcoin80-dev`, for Debian Jessie, Stretch, Ubuntu 16.04 to 18.10, or

-    `libcoin-dev`, for Debian Buster, Ubuntu 19.04 and newer, as well as for Ubuntu 18.04/18.10 with the [freecad-stable/freecad-daily PPAs](Installing_on_Linux#Official_Ubuntu_repository.md) added to your software sources.

Several libraries that deal with mathematics, triangulated surfaces, sorting, meshes, computer vision, cartographic projections, 3D visualization, the X11 Window system, XML parsing, and Zip file reading   *

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
    


<div class="mw-collapsible mw-collapsed" style="background-color   *#e0e0e0">

#### Python 2 and Qt4 

This is not recommended for newer installations as both Python 2 and Qt4 are obsolete. As of version 0.20, FreeCAD no longer supports them.


<div class="mw-collapsible-content">

To compile FreeCAD for Debian Jessie, Stretch, Ubuntu 16.04, using Python 2 and Qt4, install the following dependencies.

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

#### Python 3 and Qt5 

To compile FreeCAD for Debian Buster, Ubuntu 19.04 and newer, as well as Ubuntu 18.04/18.10 with the [freecad-stable/freecad-daily PPAs](Installing_on_Linux#Official_Ubuntu_repository.md) added to your software sources, install the following dependencies.

-    `qtbase5-dev`
    

-    `qttools5-dev`
    

-    `qt5-default`(if compiling 0.20 on a machine that still has Qt4)

-    `libqt5opengl5-dev`
    

-    `libqt5svg5-dev`
    

-    `libqt5webkit5-dev`or `qtwebengine5-dev`

-    `libqt5xmlpatterns5-dev`
    

-    `libqt5x11extras5-dev`
    

-    `libpyside2-dev`
    

-    `libshiboken2-dev`
    

-    `pyside2-tools`
    

-    `pyqt5-dev-tools`
    

-    `python3-dev`
    

-    `python3-matplotlib`
    

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
    

#### OpenCascade kernel 

The OpenCascade kernel is the core graphics library to create 3D shapes. It exists in an official version OCCT, and a community version OCE. The community version is no longer recommended, as it\'s outdated.

For Debian Buster and Ubuntu 18.10 and newer, as well as Ubuntu 18.04 with the [freecad-stable/freecad-daily PPAs](Installing_on_Linux#Official_Ubuntu_repository.md) added to your software sources, install the official packages.

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
    

For Debian Jessie, Stretch, Ubuntu 16.04 and newer, install the community edition packages.

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
    

You may install the libraries individually, or using asterisk expansion. Change `occ` for `oce` if you want to install the community libraries.


```python
sudo apt install libocct*-dev
```

#### Optional packages 

Optionally you can also install these extra packages   *

-    `libsimage-dev`, to make Coin support additional image file formats.

-    `doxygen`and `libcoin-doc` (or `libcoin80-doc` for older systems), if you intend to generate source code documentation.

-    `libspnav-dev`, for [3D input devices](3D_input_devices.md) support, like the 3Dconnexion \"Space Navigator\" or \"Space Pilot\".

-    `checkinstall`, if you intend to register your installed files into your system\'s package manager, so you can uninstall it later.

-    `python3-markdown`, for Addon Manager to display Markdown-formatted README.md files natively.

-    `python3-git`, for Addon Manager to use git to fetch and update workbenches and macros.

#### Single command for Python 3 and Qt5 

Requires Pyside2 available in Debian buster and the [freecad-stable/freecad-daily PPAs](Installing_on_Linux#Official_Ubuntu_repository.md).


```python
sudo apt install cmake cmake-gui libboost-date-time-dev libboost-dev libboost-filesystem-dev libboost-graph-dev libboost-iostreams-dev libboost-program-options-dev libboost-python-dev libboost-regex-dev libboost-serialization-dev libboost-thread-dev libcoin-dev libeigen3-dev libgts-bin libgts-dev libkdtree++-dev libmedc-dev libocct-data-exchange-dev libocct-ocaf-dev libocct-visualization-dev libopencv-dev libproj-dev libpyside2-dev libqt5opengl5-dev libqt5svg5-dev libqt5webkit5-dev libqt5x11extras5-dev libqt5xmlpatterns5-dev libshiboken2-dev libspnav-dev libvtk7-dev libx11-dev libxerces-c-dev libzipios++-dev occt-draw pyside2-tools python3-dev python3-matplotlib python3-pivy python3-ply python3-pyside2.qtcore python3-pyside2.qtgui python3-pyside2.qtsvg python3-pyside2.qtwidgets python3-pyside2.qtnetwork python3-pyside2.qtwebengine python3-pyside2.qtwebenginecore python3-pyside2.qtwebenginewidgets python3-pyside2.qtwebchannel python3-markdown python3-git python3-pyside2uic qtbase5-dev qttools5-dev swig
```

NOTE   * On some versions of Ubuntu and some versions of Qt, you will get an error that python3-pyside2uic cannot be found \-- on those systems you can safely omit it. On Ubuntu 20.04 you will need to add `pyqt5-dev-tools`. More information can be found in [this forum discussion](https   *//forum.freecadweb.org/viewtopic.php?t=51324).


<div class="mw-collapsible mw-collapsed" style="background-color   *#e0e0e0">

#### Single command for Python 2 and Qt4 

This is not recommended for newer installations as both Python 2 and Qt4 are obsolete.


<div class="mw-collapsible-content">


```python
sudo apt install cmake debhelper dh-exec dh-python libboost-date-time-dev libboost-dev libboost-filesystem-dev libboost-graph-dev libboost-iostreams-dev libboost-program-options-dev libboost-python-dev libboost-regex-dev libboost-serialization-dev libboost-thread-dev libcoin80-dev libeigen3-dev libgts-bin libgts-dev libkdtree++-dev libmedc-dev libocct-data-exchange-dev libocct-ocaf-dev libocct-visualization-dev libopencv-dev libproj-dev libpyside-dev libqt4-dev libqt4-opengl-dev libqtwebkit-dev libshiboken-dev libspnav-dev libvtk6-dev libx11-dev libxerces-c-dev libzipios++-dev lsb-release occt-draw pyside-tools python-dev python-matplotlib python-pivy python-ply swig
```

Ubuntu 16.04 users please see also the compilation discussion in the forum   * [Compile on Linux (Kubuntu)   * CMake can\'t find VTK](http   *//forum.freecadweb.org/viewtopic.php?f=4&t=16292).


</div>


</div>


</div>


</div>


<div class="mw-collapsible mw-collapsed toccolours">

### Raspberry Pi 


<div class="mw-collapsible-content">

Follow the same steps as in Debian and Ubuntu.

There are problems reported when trying to compile in Raspbian with Python 3 and Qt5, but the combination Python 3 and Qt4 seems to work for older versions of FreeCAD.

For newer versions of FreeCAD the compilation with Py3/Qt5 is successful if the operating system installed is Ubuntu 20.04.

Due to different issues with Qt, in this version the normal PySide tools won\'t be found. {{Code|lang=bash|code=
E   * Unable to locate package python3-pyside2uic
}}

In this case, we can install the packages from PyQt and create symbolic links to the needed tools. {{Code|lang=bash|code=
sudo apt-get install pyqt5-dev
sudo apt-get install pyqt5-dev-tools
cd /usr/bin/
ln -s pyrcc5 pyside2-rcc
ln -s pyuic5 pyside2-uic
}}

Now compilation may proceed. {{Code|lang=bash|code=
cd freecad-build/
cmake ../freecad-source -DBUILD_QT5=ON -DPYTHON_EXECUTABLE=/usr/bin/python3 -DUSE_PYBIND11=ON
make -j2
}}

The `-j` option to `make` should not be more than 3 because the Raspberry Pi has limited memory. It will take several hours to compile, so it is better to do it overnight.

More information, [FreeCAD and Raspberry Pi 4](https   *//forum.freecadweb.org/viewtopic.php?f=42&t=37458&start=160#p396652).


</div>


</div>


<div class="mw-collapsible mw-collapsed toccolours">

### Fedora


<div class="mw-collapsible-content">

You need the following packages    *

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
-   OCE-devel
-   python
-   python-devel
-   python-pyside-devel
-   pyside-tools
-   boost-devel
-   tbb-devel
-   eigen3-devel
-   qt-devel
-   qt-webkit-devel
-   qt5-qtxmlpatterns
-   qt5-qttools-static
-   ode-devel
-   xerces-c
-   xerces-c-devel
-   opencv-devel
-   smesh-devel
-   Coin3
-   Coin3-devel

(April 2021, Coin4 and Coin4-devel are available) (if coin2 is the latest available for your version of Fedora, use packages from <http   *//www.zultron.com/rpm-repo/>)

-   SoQt-devel
-   freetype
-   freetype-devel
-   vtk
-   med
-   med-devel

And optionally    *

-   libspnav-devel (for 3Dconnexion devices support like the Space Navigator or Space Pilot)
-   python3-pivy ( <https   *//bugzilla.redhat.com/show_bug.cgi?id=458975> Pivy is not mandatory but needed for the Draft Workbench)
-   python3-markdown (for the Addon Manager to display native markdown)
-   python3-git (for the Addon Manager to use git to checkout and update workbenches and macros)

There is a bug in cmake distributed by Fedora 34/35 which fails to find the opencascade libraries on Fedora. This can be easily be fixed by adding one line to the top level cmake file of opencascade installed on Fedora. Details here   * <https   *//bugzilla.redhat.com/show_bug.cgi?id=2083568>


</div>


</div>


<div class="mw-collapsible mw-collapsed toccolours">

### Gentoo


<div class="mw-collapsible-content">

Easiest way to check which packages are needed to compile FreeCAD is to check via portage   *

emerge -pv freecad

This should give a nice list of extra packages that you need installed on your system.

If FreeCAD is not available on portage, it is available on the [waebbl overlay](https   *//github.com/waebbl/waebbl-gentoo). The issue tracker on the waebbl overlay Github may help guide through some issues you may come across. The overlay provides freecad-9999, which you can choose to compile, or simply use to get the dependencies.

layman -a waebbl


</div>


</div>


<div class="mw-collapsible mw-collapsed toccolours">

### openSUSE


<div class="mw-collapsible-content">

#### Tumbleweed

The following commands will install the packages required for building FreeCAD with Qt5 and Python 3.


```python
zypper in --no-recommends -t pattern devel_C_C++ devel_qt5

zypper in libqt5-qtbase-devel libqt5-qtsvg-devel libqt5-qttools-devel boost-devel swig libboost_program_options-devel libboost_mpi_python3-devel libboost_system-devel libboost_program_options-devel libboost_regex-devel libboost_python3-devel libboost_thread-devel libboost_system-devel libboost_headers-devel libboost_graph-devel python3 python3-devel python3-matplotlib python3-matplotlib-qt5 python3-pyside2 python3-pyside2-devel python3-pivy gcc gcc-fortran cmake occt-devel libXi-devel opencv-devel libxerces-c-devel Coin-devel SoQt-devel freetype2-devel eigen3-devel libode6 vtk-devel libmed-devel hdf5-openmpi-devel openmpi2-devel netgen-devel freeglut-devel libspnav-devel f2c doxygen dos2unix glew-devel
```

The following command will install Qt Creator and the GNU Project Debugger.


```pythonzypper in libqt5-creator gdb```

If any packages are missing, then you can check the Tumbleweed [\"FreeCAD.spec\"](https   *//build.opensuse.org/package/view_file/openSUSE   *Factory/FreeCAD/FreeCAD.spec) file on the [Open Build Service](https   *//build.opensuse.org/package/show/openSUSE   *Factory/FreeCAD).

Also, check to see if there are any patches you need to apply (such as [0001-find-openmpi2-include-files.patch](https   *//build.opensuse.org/package/view_file/openSUSE   *Factory/FreeCAD/0001-find-openmpi2-include-files.patch)).

#### Leap

If there is a difference between the available packages on Tumbleweed and Leap, then you can read the Leap [\"FreeCAD.spec\"](https   *//build.opensuse.org/package/view_file/openSUSE   *Leap   *15.0/FreeCAD/FreeCAD.spec) file on the [Open Build Service](https   *//build.opensuse.org/) to determine the required packages.

See [piano\_jonas unofficial \"Compile On openSUSE\" guide](https   *//forum.freecadweb.org/viewtopic.php?f=4&t=49726).


</div>


</div>


<div class="mw-collapsible mw-collapsed toccolours">

### Arch Linux 


<div class="mw-collapsible-content">

You will need the following libraries from the official repositories   *

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
-   qt5-svg
-   qt5-webkit
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
sudo pacman -S boost curl desktop-file-utils glew hicolor-icon-theme jsoncpp libspnav opencascade shiboken2 xerces-c pyside2 python-matplotlib python-netcdf4 qt5-svg qt5-webkit qt5-webengine cmake eigen git gcc-fortran pyside2-tools swig qt5-tools shared-mime-info coin python-pivy med
```


</div>


</div>


<div class="mw-collapsible mw-collapsed toccolours">

### Older and non-conventional distributions 


<div class="mw-collapsible-content">

On other distributions, we have very few feedback from users, so it might be harder to find the required packages.

Try first locating the required libraries mentioned in [third party libraries](Third_Party_Libraries.md) in your package manager. Beware that some of them might have a slightly different package name; search for `name`, but also `libname`, `name-dev`, `name-devel`, and similar. If that is not possible try compiling those libraries yourself.

FreeCAD requires the GNU g++ compiler version equal or above 3.0.0, as FreeCAD is mostly written in C++. During the compilation some Python scripts are executed, so the Python interpreter has to work properly. To avoid any linker problems it is also a good idea to have the library paths in the `LD_LIBRARY_PATH` variable or in the `ld.so.conf` file. This is already done in modern Linux distributions, but may need to be set in older ones.


</div>


</div>

### Pivy

[Pivy](Pivy.md) (Python wrappers to Coin3d) is not needed to build FreeCAD or to start it, but it is needed as a runtime dependency by the [Draft Workbench](Draft_Workbench.md). If you are not going to use this workbench, you won\'t need Pivy. However, do notice that the Draft Workbench is used internally by other workbenches, like [Arch](Arch_Workbench.md) and [BIM](BIM_Workbench.md), so Pivy needs to be installed to use these workbenches as well.

By November 2015 the obsolete version of Pivy included with the FreeCAD source code will no longer compile on many systems. This isn\'t a big problem as normally you should get Pivy from your distribution\'s package manager; if you cannot find Pivy, you may have to compile it yourself, see [Pivy compilation instructions](Extra_python_modules#Pivy.md).

### Debug symbols 

In order to troubleshoot crashes in FreeCAD, it is useful to have the debug symbols of important dependency libraries such as Qt. For this, try installing the dependency packages that end with `-dbg`, `-dbgsym`, `-debuginfo` or similar, depending on your Linux distribution.

For Ubuntu, you may have to enable special repositories to be able to see and install these debug packages with the package manager. See [Debug Symbol Packages](https   *//wiki.ubuntu.com/Debug_Symbol_Packages) for more information.

## Compile FreeCAD 


**Compiling against Python 2 and Qt4 is no longer well supported, and as of 0.20 is no longer supported at all. You should compile against Python 3 and Qt5. 0.20 requires at least Python3.6 and Qt 5.9.**

FreeCAD uses CMake as its main build system, as it\'s available on all major operating systems. Compiling with CMake is usually very simple and happens in two steps.

1.  CMake checks that every needed program and library is present on your system, and generates a `Makefile` that is configured for the second step. FreeCAD has several configuration options to choose from, but it comes with sensible defaults. Some alternatives are detailed below.
2.  The compilation itself, which is done with the program `make`, which generates the FreeCAD executables.

Since FreeCAD is a large application, compiling the entire source code can take anywhere from 10 minutes to one hour, depending on your CPU and the number of CPU cores used for compilation.

You can build the code either in or out of the source directory. Out-of-source building is generally the best option.

### Out-of-source build 

Building in a separate folder is more convenient than building in the same directory where the source code is located as every time you update the source code CMake can intelligently determine which files have changed, and recompile only what is needed. This is very useful when testing different Git branches as you don\'t confuse the build system.

To build out-of-source, simply create a build directory, `freecad-build`, distinct from your FreeCAD source folder, `freecad-source`; then from this build directory point `cmake` to the right source folder. You can use `cmake-gui` or `ccmake` instead of `cmake` in the instructions below as well. Once `cmake` finishes configuring the environment, use `make` to start the actual compilation.


{{Code|lang=bash|code=
mkdir freecad-build
cd freecad-build
cmake ../freecad-source
make -j$(nproc --ignore=2)
}}

Note   * if you are compiling the 0.19 release branch, you must explicitly specify that you are compiling with Qt5 and Python 3 \-- replace the cMake command above with   * {{Code|lang=bash|code=
cmake ../freecad-source -DBUILD_QT5=ON -DPYTHON_EXECUTABLE=/usr/bin/python3
}}

The `-j` option of `make` controls how many jobs (files) are compiled in parallel. The `nproc` program prints the number of CPU cores in your system; by using it together with the `-j` option you can choose to process as many files as you have cores, in order to speed up overall compilation of the program. In the example above, it will use all cores in your system except two; this will keep your computer responsive for other uses while compilation proceeds in the background. The FreeCAD executable will eventually appear in the `freecad-build/bin` directory. See also [Compiling (speeding up)](Compiling_(Speeding_up).md) to improve compilation speed.

### Resolving cmake issues 

If you have done an out-of-source build before and get stuck on a dependency that is not recognized or can\'t seem to be resolved, try the following   *

-   Delete the contents of the build directory before running cmake again. FreeCAD is a rapidly moving target, you may be tripping over cached cmake information that points at an older version than the new repository head can use. Clearing the cache may allow cmake to recover and recognize the version you actually need.

-   If cmake complains about missing a specific file, use a tool such as \"apt-file search\", or its equivalent in other package systems, to discover what package that file belongs to and install it. Bear in mind that you are likely to need the -dev version of the package that carries header or config files files required for FreeCAD to use the package.

### Compiling against GNU libc 2.34 and later 

GNU libc 2.34 introduces a change to the library that can cause builds on some Linux systems to fail with an error like   *


{{Code|lang=bash|code=
No rule to make target '/usr/lib/x86_64-linux-gnu/libdl.so
}}

To resolve this, a symbolic link must be manually created from the (now empty) system-installed libdl.so.\* to the location your compiler says it is looking for the file. For example (if the actual installed copy of libdl.so on your system is /usr/lib/x86\_64-linux-gnu/libdl.so.2)   *


{{Code|lang=bash|code=
sudo ln -s /usr/lib/x86_64-linux-gnu/libdl.so.2 /usr/lib/x86_64-linux-gnu/libdl.so
}}

Adapt the command for the structure of your system by searching for libdl.so\* and linking it to the appropriate location.

### In-source building 

In-source builds are fine if you want to compile a version of FreeCAD quickly, and don\'t intend to update the source code often. In this case, you can remove the compiled program and the source just by deleting a single folder.

Change to the source directory, and point `cmake` to the present directory (denoted by a single point)   *


{{Code|lang=bash|code=
cd freecad-source
cmake . -DBUILD_QT5=ON -DPYTHON_EXECUTABLE=/usr/bin/python3
make -j$(nproc --ignore=2)
}}

The FreeCAD executable will then reside in the `freecad-source/bin` directory.

### How to repair your source code directory 

If you accidentally performed a compilation inside the source code directory, or added strange files, and would like to restore the contents to only the original source code, you can perform the following steps.


{{Code|lang=bash|code=
> .gitignore
git clean -df
git reset --hard HEAD
}}

The first line clears the `.gitignore` file. This ensures that the following clean and reset commands will affect everything in the directory and will not ignore items matching the expressions in `.gitignore`. The second line deletes all files and directories that are not tracked by the git repository; then the last command will reset any changes to tracked files, including the first command which cleared the `.gitignore` file.

If you do not clear the source directory, subsequent runs of `cmake` may not capture new options to the system if the code changes.

### Configuration

By passing different options to `cmake`, you can change how FreeCAD is compiled. The syntax is as follows.


```python
cmake -D <var>   *<type>=<value> $SOURCE_DIR
```

Where `$SOURCE_DIR` is the directory that contains the source code. The `<type>` may be omitted in most cases. The space after the `-D` option may also be omitted.

For example, to avoid building the [FEM Workbench](FEM_Workbench.md)   *


{{Code|lang=bash|code=
cmake -D BUILD_FEM   *BOOL=OFF ../freecad-source
cmake -DBUILD_FEM=OFF ../freecad-source
}}

All possible variables are listed in the `InitializeFreeCADBuildOptions.cmake` file, located in the `cMake/FreeCAD_Helpers` directory. In this file, search for the word `option` to get to the variables that can be set, and see their default values.

    # ==============================================================================
    # =================   All the options for the build process    =================
    # ==============================================================================

    option(BUILD_FORCE_DIRECTORY "The build directory must be different to the source directory." OFF)
    option(BUILD_GUI "Build FreeCAD Gui. Otherwise you have only the command line and the Python import module." ON)
    option(FREECAD_USE_EXTERNAL_ZIPIOS "Use system installed zipios++ instead of the bundled." OFF)
    option(FREECAD_USE_EXTERNAL_SMESH "Use system installed smesh instead of the bundled." OFF)
    ...

Alternatively, use the command `cmake -LH` to list the current configuration, and thus all variables that can be changed. You may also install and use `cmake-gui` to launch a graphical interface showing all the variables that can be modified. In the next sections we list some of the more relevant options that you may want to use.

#### For a Debug build 

Create a `Debug` build to troubleshoot crashes in FreeCAD. Beware that with this build the [Sketcher](Sketcher_Workbench.md) becomes very slow with complex sketches.


{{Code|lang=bash|code=
cmake -DBUILD_QT5=ON -DPYTHON_EXECUTABLE=/usr/bin/python3 -DCMAKE_BUILD_TYPE=Debug ../freecad-source
}}

#### For a Release build 

Create a `Release` build to test code that doesn\'t crash. A `Release` build will run much faster than a `Debug` build.


{{Code|lang=bash|code=
cmake -DBUILD_QT5=ON -DPYTHON_EXECUTABLE=/usr/bin/python3 -DCMAKE_BUILD_TYPE=Release ../freecad-source
}}

#### Building against Python 3 and Qt5 

By default, FreeCAD 0.19 and earlier build for Python 2 and Qt4. Since these two packages are obsolete, it is better to build for Python 3 and Qt5. Support for Python 2 and Qt4 has been removed in FreeCAD 0.20 and it is not necessary to explicitly enable Qt5 and Python 3 if compiling the latest development versions.

In a modern Linux distribution you only need to provide two variables specifying the use of Qt5, and the path to the Python interpreter.

For 0.19   * {{Code|lang=bash|code=
cmake -DBUILD_QT5=ON -DPYTHON_EXECUTABLE=/usr/bin/python3 ../freecad-source
}}

For 0.20\_dev   * {{Code|lang=bash|code=
cmake ../freecad-source
}}

Note that when switching between 0.19 and the 0.20 builds, it may be necessary to delete CMakeCache.txt prior to running cmake.

#### Building for a specific Python version 

If the default `python` executable in your system is a symbolic link to Python 2, `cmake` will try to configure FreeCAD for this version. You can choose another version of Python by giving the path to a specific executable   *


{{Code|lang=bash|code=
cmake -DPYTHON_EXECUTABLE=/usr/bin/python3 ../freecad-source
}}

If that doesn\'t work, you may have to define additional variables pointing to the desired Python libraries and include directories   *


{{Code|lang=bash|code=
cmake -DPYTHON_EXECUTABLE=/usr/bin/python3.6 \
    -DPYTHON_INCLUDE_DIR=/usr/include/python3.6m \
    -DPYTHON_LIBRARY=/usr/lib/x86_64-linux-gnu/libpython3.6m.so \
    -DPYTHON_PACKAGES_PATH=/usr/lib/python3.6/site-packages/ \
    ../freecad-source
}}

It is possible to have several independent versions of Python in the same system, so the locations and version numbers of your Python files will depend on your particular Linux distribution. Use `python3 -V` to display the version of Python that you are using currently; only the first two numbers are necessary; for example, if the result is `Python 3.6.8`, you need to specify the directories that relate to the 3.6 version. If you don\'t know the right directories, try searching for them with the `locate` command.


```python
locate python3.6
```

You may use `python3 -m site` in a terminal to determine the `site-packages` directory, or `dist-packages` for Debian systems.

#### Building with Qt Creator against Python 3 and Qt5 

1\. Launch Qt Creator.

2\. Click on **Open Project**.

3\. Navigate to the directory where the source code is, `freecad-source/`, and choose the topmost `CMakeLists.txt` file.

4\. By selecting the file, it will automatically run `cmake` on it, but it may fail if the appropriate options aren\'t correctly set.

5\. Go to **Projects → Build & Run → Imported Kit → Build → Build Settings → CMake**. Set the appropriate build directory, `freecad-build/`.

6\. Set the appropriate variables in the Key-Value dialog, of types `String` and `Bool`. 
```python
PYTHON_EXECUTABLE=/usr/bin/python3
BUILD_QT5=ON
```

7\. If the variables do not load the project correctly, you may have to go to **Projects → Manage Kits → Kits → Default (or Imported Kit or similar) → CMake Configuration**. Then press **Change**, and add the appropriate configuration as described above. You may have to add more variables about the Python paths, if the system Python is not found. 
```python
PYTHON_EXECUTABLE   *STRING=/usr/bin/python3.7
PYTHON_INCLUDE_DIR   *STRING=/usr/include/python3.7m
PYTHON_LIBRARY   *STRING=/usr/lib/x86_64-linux-gnu/libpython3.7m.so
PYTHON_PACKAGES_PATH   *STRING=/usr/lib/python3.7/site-packages
BUILD_QT5   *BOOL=ON
```

7.1. Press **Apply**, then **OK**.

7.2. Make sure the rest of the options are correctly set, for example, **Qt version** should be a present version installed in the system, like `Qt 5.9.5 in PATH (qt5)`.

Press **Apply**, then **OK** to close the configuration.

The `cmake` program should run automatically again, and it should fill the entire Key-Value dialog with all the variables that can be configured.

8\. Go to **Projects → Build & Run → Imported Kit → Run → Run Settings → Run → Run Configuration** and choose `FreeCADMain` to compile the graphical version of FreeCAD, or `FreeCADMainCMD` to compile only the command line version.

9\. Finally, go to the menu **Build → Build Project "FreeCAD"**. If this is a new compilation, it should take several minutes, inclusive hours, depending on the number of processors that you have available.

#### Qt designer plugin 

If you want to develop Qt code for FreeCAD, you\'ll need the Qt Designer plugin that provides all custom widgets of FreeCAD.

Go into an auxiliary directory of the source code, the run `qmake` with the indicated project file to create a `Makefile`; then run `make` to compile the plugin.


{{Code|lang=bash|code=
cd freecad-source/src/Tools/plugins/widget
qmake plugin.pro
make
}}

If you are compiling for Qt5, make sure the `qmake` binary is the one for this version, so that the resulting `Makefile` contains the necessary information for Qt5.


{{Code|lang=bash|code=
cd freecad-source/src/Tools/plugins/widget
$QT_DIR/bin/qmake plugin.pro
make
}}

where `$QT_DIR` is the directory that stores Qt binary libraries, for example, `/usr/lib/x86_64-linux-gnu/qt5`.

The library created is `libFreeCAD_widgets.so`, which needs to be copied to `$QT_DIR/plugins/designer`.


{{Code|lang=bash|code=
sudo cp libFreeCAD_widgets.so $QT_DIR/plugins/designer
}}

#### External or internal Pivy 

Previously, a version of Pivy was included in the source code of FreeCAD (internal). If you wanted to use your system\'s copy of Pivy (external), you needed to use -DFREECAD_USE_EXTERNAL_PIVY=1.

Using external Pivy became the default during development of FreeCAD 0.16, therefore this option does not need to be set manually anymore.

#### Doxygen documentation 

If you have Doxygen installed you can build the source code documentation. See [source documentation](source_documentation.md) for instructions.

### Additional documentation 

The source code of FreeCAD is very extensive, and with CMake it\'s possible to configure many options. Learning to use CMake fully may be useful to choose the right options for your particular needs.

-   [CMake Reference Documentation](https   *//cmake.org/documentation/) by Kitware.
-   [How to Build a CMake-Based Project](https   *//preshing.com/20170511/how-to-build-a-cmake-based-project/) (blog) by Preshing on programming.
-   [Learn CMake\'s Scripting Language in 15 Minutes](https   *//preshing.com/20170522/learn-cmakes-scripting-language-in-15-minutes/) (blog) by Preshing on programming.

### Making a debian package 

If you plan to build a Debian package out of the sources you need to install certain packages first   *


{{Code|lang=bash|code=
sudo apt install dh-make devscripts lintian
}}

Go to the FreeCAD directory and call


{{Code|lang=bash|code=
debuild
}}

Once the package is built, you can use `lintian` to check if the package contains errors


{{Code|lang=bash|code=
lintian freecad-package.deb
}}

## Updating the source code 

The CMake system allows you to intelligently update the source code, and only recompile what has changed, making subsequent compilations faster.

Move to the location where the FreeCAD source code was first downloaded, and pull the new code   *


{{Code|lang=bash|code=
cd freecad-source
git pull
}}

Then move into the build directory where the code was compiled initially, and run `cmake` specifying the present directory (denoted by a dot); then trigger the re-compilation with `make`.


{{Code|lang=bash|code=
cd ../freecad-build
cmake .
make -j$(nproc --ignore=2)
}}

## Troubleshooting

### For 64 bit systems 

When building FreeCAD for 64-bit there is a known issue with the OpenCASCADE (OCCT) 64-bit package. To get FreeCAD running properly you might need to run the `configure` script and set additional `CXXFLAGS`   *


{{Code|lang=bash|code=
./configure CXXFLAGS="-D_OCC64"
}}

For Debian based systems this option is not needed when using the pre-built OpenCASCADE packages because these ones set the proper `CXXFLAGS` internally.

## Automatic build scripts 

Here is all what you need for a complete build of FreeCAD. It\'s a one-script-approach and works on a freshly installed Linux distribution. The commands will ask for the root password for installation of packages and new online repositories. These scripts should run on 32 and 64 bit versions. They are written for different versions, but are also likely to run on a later version with or without major changes.

If you have such a script for your preferred distribution, please discuss it on the [FreeCAD forum](https   *//forum.freecadweb.org/viewforum.php?f=21&sid=e3c22dca9da076fefb56b1d5c5fb3134) so we can incorporate it.


<div class="mw-collapsible mw-collapsed toccolours">

### Ubuntu


<div class="mw-collapsible-content">

These scripts provide a reliable way to install the correct set of dependencies required to build and run FreeCAD on Ubuntu. They make use of the Ubuntu personal package archives (PPA), and should work on any version of Ubuntu targeted by the PPA. The [freecad-daily](https   *//launchpad.net/~freecad-maintainers/+archive/ubuntu/freecad-daily) PPA targets recent versions of Ubuntu, while the [freecad-stable](https   *//launchpad.net/~freecad-maintainers/+archive/ubuntu/freecad-stable) PPA targets officially supported versions of Ubuntu.

This script installs the daily compiled snapshot of FreeCAD and its dependencies. It adds the daily repository, gets the dependencies to build this version, and installs the required packages. Afterwards it proceeds to pull the source code into a particular directory, creates a build directory and changes into it, configures the compilation environment with `cmake`, and finally builds the entire program with `make`. Save the script to a file, make it executable, and run it, but don\'t use `sudo`; superuser privileges will be asked only for selected commands.


{{Code|lang=bash|code=
#!/bin/sh
sudo add-apt-repository --enable-source ppa   *freecad-maintainers/freecad-daily && sudo apt-get update
sudo apt-get build-dep freecad-daily
sudo apt-get install freecad-daily

git clone https   *//github.com/FreeCAD/FreeCAD.git freecad-source
mkdir freecad-build
cd freecad-build
cmake -DBUILD_QT5=ON -DPYTHON_EXECUTABLE=/usr/bin/python3 -DFREECAD_USE_PYBIND11=ON ../freecad-source
make -j$(nproc --ignore=2)
}}

If you wish, you can uninstall the pre-compiled version of FreeCAD (`freecad-daily`) while leaving the dependencies in place, however, leaving this package installed will allow the package manager to keep its dependencies up to date as well; this is mostly useful if you intend to follow the development of FreeCAD, and constantly update and compile the sources from the Git repository.

The previous script assumes that you want to compile the latest version of FreeCAD, so you are using the \"daily\" repository to get the dependencies. However, you can instead get the build dependencies of the \"stable\" version for your current Ubuntu release. If this is the case, replace the top part of the previous script with the following instructions. For Ubuntu 12.04, omit `--enable-source` from the command.


{{Code|lang=bash|code=
#!/bin/sh
sudo add-apt-repository --enable-source ppa   *freecad-maintainers/freecad-stable && sudo apt-get update
sudo apt-get build-dep freecad
sudo apt-get install libqt5xmlpatterns5-dev   # Needed for 0.20; should go away on next packaging update 
sudo apt-get install freecad
}}

Once you install the `freecad` package from the `freecad-stable` repository, it will supersede the FreeCAD executable that is available from the Universe Ubuntu repository. The executable will be named simply `freecad`, and not `freecad-stable`.


</div>


</div>


<div class="mw-collapsible mw-collapsed toccolours">

### openSUSE 


<div class="mw-collapsible-content">

No external Repositories are needed to compile FreeCAD. However, there is an imcompatability with python3-devel which needs to be removed. FreeCAD can be compiled from GIT


{{Code|lang=bash|code=
# install needed packages for development
sudo zypper install gcc cmake OpenCASCADE-devel libXerces-c-devel \
python-devel libqt4-devel python-qt4 Coin-devel SoQt-devel boost-devel \
libode-devel libQtWebKit-devel libeigen3-devel gcc-fortran git swig
 
# create new dir, and go into it
mkdir FreeCAD-Compiled 
cd FreeCAD-Compiled
 
# get the source
git clone https   *//github.com/FreeCAD/FreeCAD.git free-cad
 
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

Since you are using git, next time you wish to compile you do not have to clone everything, just pull from git and compile once more


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
# Note   * to speed up build use all CPU cores   * make -j$(nproc)
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
git clone https   *//github.com/FreeCAD/FreeCAD.git freecad
 
# go to source dir
cd freecad
 
# build configuration 
cmake .
 
# build FreeCAD
# Note   * to speed up build use all CPU cores   * make -j$(nproc)
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

Posted by user [http   *//forum.freecadweb.org/memberlist.php?mode=viewprofile&u=3666 PrzemoF](http   *//forum.freecadweb.org/memberlist.php?mode=viewprofile&u=3666_PrzemoF.md) in the forum.


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
git clone https   *//github.com/FreeCAD/FreeCAD.git
mkdir $BUILD_DIR <nowiki>||</nowiki> { echo "~/$BUILD_DIR already exist. Quitting.."; exit; }
cd $BUILD_DIR
cmake ../FreeCAD 
make -j$(nproc)
}}


</div>


</div>


<div class="mw-collapsible mw-collapsed toccolours">

### Arch using AUR 


<div class="mw-collapsible-content">

[Arch User Repository (AUR)](https   *//aur.archlinux.org/) is a collection user made recipes to build packages which are not officially supported by distribution maintainers / community. They are usually safe. You can see who maintain the package and for how long he did. It is recommended to check construction files. Also non open source software are available in this area even if maintained by the official owning company.

Prerequisite    * git

Steps    *

1.  Open a terminal. Optionally create a directory eg. {{incode | mkdir git}}. Optionally change directory eg. `cd git`.
2.  Clone the AUR repository    * `git clone http   *//aur.archlinux.org/packages/freecad-git`
3.  Enter AUR repository folder    * `cd freecad-git`
4.  Compile using [Arch makepkg](https   *//wiki.archlinux.org/index.php/Makepkg)    * `makepkg -s`. The -s or \--syncdeps flag will also install required dependencies.
5.  Install created package    * `makepkg --install` or double click on the pkgname-pkgver.pkg.tar.xz inside your file browser.

To update FreeCAD to latest build just repeat from step 3. Update AUR repo when there is some breaking change in the recipe or new features using `git checkout -f` inside the folder.







[Category   *Developer\_Documentation](Category_Developer_Documentation.md) [Category   *Developer](Category_Developer.md)



---
![](images/Right_arrow.png) [documentation index](../README.md) > [Developer_Documentation](Category_Developer_Documentation.md) > [Developer](Category_Developer.md) > Compile on Linux/ro
