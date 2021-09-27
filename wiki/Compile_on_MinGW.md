# Compile on MinGW
**(2021) The re-write of this page is an early draft, and work is still in progress. Please help us to finish it!<br>Meanwhile, try other [compilation options](Compiling.md).**

 

This guide will walk through the steps necessary to build FreeCAD on Windows using the MSYS2/MinGW environment. Basic familiarity with Bash shell commands will be useful for understanding what each step does, but following the guide by rote should result in a working build even if you don\'t understand exactly what you did to get it.

### Before you start 

Download and install [MSYS2](https://www.msys2.org) if you have not already. When launching MSYS2, use the \"MSYS2 MinGW 64-bit\" runtime unless you know what you are doing and have a specific reason not to. If you use the UCRT console, make sure to adapt your installation to use the UCRT packages instead.



    pacman -Syu



and then relaunching and running



    pacman -Su



before proceeding.

### Install basic development tools 

In all of the following steps, when prompted by MSYS2\'s shell, accept the default installations of everything by pressing \"Enter\" when asked.

First, install the mingw-w64 GCC toolchain:



    pacman -S --needed base-devel mingw-w64-x86_64-toolchain mingw-w64-x86_64-cmake mingw-w64-x86_64-ninja



This will probably take several minutes to complete, as the compiler toolchain is quite large.

Install git:



    pacman -S git



Close your current console window and relaunch the MSYS2 MinGW 64 console (in a standard installation this will be in your Start menu in the MSYS2 folder).

### Check out the FreeCAD sources 

To get the FreeCAD source code, clone it from the main git repository:



    git clone https://github.com/FreeCAD/FreeCAD



If you do not want to compile the latest HEAD, once you have the source you can check out a specific tag:



    cd FreeCAD
    git checkout tags/0.19.2 -b releases/FreeCAD-0-19



Or a specific pull request (in this example, PR 1234):



    cd FreeCAD
    git fetch origin pull/1234/head:pr/1234
    git checkout pr/1234



### Install required libraries 

FreeCAD depends on many 3rd-party libraries for its functionality. They may be installed individually, or as a single unified command. Updating this list is the current ongoing work of this documentation: to help, repeatedly run the cmake command from the next section, and install whatever the next package is that it errors on. As of this writing there is a problem with the pacman-installed OpenCASCADE package.

-   mingw-w64-x86\_64-opencascade

To resolve the current (9/11/2021) problem with the OpenCASCADE installation, it is necessary to modify the installed cMake configuration files for the library. In the files /mingw64/lib/cmake/opencascade/\*-release.cmake, remove all occurrences of the string



    \${OCCT_INSTALL_BIN_LETTER}



(Note the leading backslash \-- that character must be removed along with the variable reference).

Now, install the following required dependencies using pacman:

-   mingw-w64-x86\_64-xerces-c
-   mingw-w64-x86\_64-qt5
-   mingw-w64-x86\_64-med
-   mingw-w64-x86\_64-swig
-   mingw-w64-x86\_64-qtwebkit
-   mingw-w64-x86\_64-coin
-   mingw-w64-x86\_64-python-pivy
-   mingw-w64-x86\_64-python-ply
-   mingw-w64-x86\_64-python-six
-   mingw-w64-x86\_64-python-yaml
-   mingw-w64-x86\_64-python-numpy
-   mingw-w64-x86\_64-python-matplotlib
-   mingw-w64-x86\_64-pyside2-qt5

The following is a single command to install everything but OpenCASCADE:



    pacman -S mingw-w64-x86_64-xerces-c mingw-w64-x86_64-qt5 mingw-w64-x86_64-med mingw-w64-x86_64-swig mingw-w64-x86_64-qtwebkit mingw-w64-x86_64-coin mingw-w64-x86_64-python-pivy mingw-w64-x86_64-pyside2-qt5 mingw-w64-x86_64-python-python-ply mingw-w64-x86_64-python-six mingw-w64-x86_64-python-yaml mingw-w64-x86_64-python-numpy mingw-w64-x86_64-python-matplotlib



### Build FreeCAD 

Make a directory for the build: note this is typically not a subdirectory of the source directory (it is often useful to be able to delete either the source or the build directory independently).



    mkdir FreeCAD-build
    cd FreeCAD-build



Run cMake:



    cmake ../FreeCAD



And finally:



    cmake --build ./



 

_ _

---
[documentation index](../README.md) > [Developer_Documentation](Category_Developer_Documentation.md) > Compile on MinGW
