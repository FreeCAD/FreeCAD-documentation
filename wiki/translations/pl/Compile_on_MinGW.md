# Compile on MinGW/pl
{{TOCright}}

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
    git checkout tags/1.0 -b releases/FreeCAD-1-0

Or a specific pull request (in this example, PR 1234):

    cd FreeCAD
    git fetch origin pull/1234/head:pr/1234
    git checkout pr/1234

Note that not all versions can be compiled on MSYS2, several changes were required to enable it and these were not present in the 0.19 or earlier versions. For example, the 0.19.3 tag will not be compilable.

### Install required libraries 

FreeCAD depends on many 3rd-party libraries for its functionality. They may be installed individually, or as a single unified command.

Now, install the following required dependencies using pacman:

-   mingw-w64-x86\_64-opencascade
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
-   mingw-w64-x86\_64-python-markdown
-   mingw-w64-x86\_64-python-pygit2

The following is a single command to install everything in the list above:

    pacman -S mingw-w64-x86_64-opencascade mingw-w64-x86_64-xerces-c mingw-w64-x86_64-qt5 mingw-w64-x86_64-med mingw-w64-x86_64-swig mingw-w64-x86_64-qtwebkit mingw-w64-x86_64-coin mingw-w64-x86_64-python-pivy mingw-w64-x86_64-pyside2-qt5 mingw-w64-x86_64-python-ply mingw-w64-x86_64-python-six mingw-w64-x86_64-python-yaml mingw-w64-x86_64-python-numpy mingw-w64-x86_64-python-matplotlib mingw-w64-x86_64-python-markdown mingw-w64-x86_64-python-pygit2

### Build FreeCAD 

Make a directory for the build: note this is typically not a subdirectory of the source directory (it is often useful to be able to delete either the source or the build directory independently).

    mkdir FreeCAD-build
    cd FreeCAD-build

Run cMake:

    cmake ../FreeCAD

And finally:

    cmake --build ./



---
![](images/Right_arrow.png) [documentation index](../README.md) > [Developer_Documentation](Category_Developer_Documentation.md) > [Developer](Category_Developer.md) > Compile on MinGW/pl
