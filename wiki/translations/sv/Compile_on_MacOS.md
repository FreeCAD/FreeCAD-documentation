# Compile on MacOS/sv
**There is an experimental FreeCAD Docker container that is being tested for FreeCAD development. Read more about it at [[Compile on Docker]]**


{{TOCright}}

## Overview

This page describes how to compile the FreeCAD source code on macOS. For other platforms, see [Compiling](Compiling.md).

These instructions have been tested on macOS Catalina with standard XCode 11.6. It is known to work on macOS BigSur Beta with XCode 12.0 beta. If you plan to use XCode Beta, please be sure to download Command Line Tools add on through a dmg package to workaround some libz dependency issues.

This page serves as a quick start, and is not intended to be comprehensive with regard to describing all the available build options.

If you just want to evaluate the latest pre-release build of FreeCAD, you can download pre-built binaries [from here](https://github.com/FreeCAD/FreeCAD/releases).

## Install Prerequisites 

The following software must be installed to support the build process.

### Homebrew Package Manager 

Homebrew is a command line based package manager for macOS. The [Homebrew main page](https://brew.sh/) provides an installation command line that you simply paste into a terminal window.

### CMake

CMake is a build tool that generates a build configuration based on variables you specify. You then issue the \'make\' command to actually build that configuration. The command-line version of CMake is automatically installed as part of the Homebrew installation, above. If you prefer to use a GUI version of CMake, you can download it from [here](https://www.cmake.org/downloadDownload).

## Install Dependencies 

FreeCAD maintains a Homebrew \'cask\' which installs the required formulas and dependencies. Issue the following brew commands in your terminal.


```python
brew tap freecad/freecad
brew install eigen
brew install --only-dependencies freecad
```


{{Incode|brew install}}

may take quite a while, so you may want go grab a beverage. :-).

Alternately, you can install the individual dependencies manually by installing the following packages using {{Incode|brew install ...}}:

-    `cmake`
    

-    `swig`
    

-    `boost`
    

-    `boost-python3`
    

-    `eigen`
    

-    `gts`
    

-    `vtk`
    

-    `xerces-c`
    

-    `qt@5`\- Only Qt5 is currently supported, support for Qt6 is a work-in-progress

-    `opencascade`
    

-    `doxygen`
    

-    `pkgconfig`
    

-    `coin3d`\- Note that as of this writing (Nov. 2022) this will install an unusable version of pyside@2 as a dependency.

There are several packages that are only available when you have tapped the freecad cask: you must do that (`brew tap freecad/freecad`). Due to some historical bug workarounds, at the time of this writing (Nov. 2022) the versions of PySide2 and Shiboken2 installed by Homebrew are not usable because they force the use of Py_Limited_API, which FreeCAD does not support. It is expected that this workaround will be removed in the coming months, but in the meantime you must use the FreeCAD cask versions of PySide and Shiboken. Use `brew install ...`, install the following packages:

-    `freecad/freecad/pyside2@5.15.5`
    

-    `freecad/freecad/shiboken2@5.15.5`
    

-    `freecad/freecad/med-file`
    

-    `freecad/freecad/netgen`
    

You will also need to \"link\" PySide and Shiboken:


```python
brew link freecad/freecad/pyside2@5.15.5 freecad/freecad/shiboken2@5.15.5
```

In some cases the packages installed by Homebrew do not use the same Python version: for example, at the time of this writing PySide2 uses Python 3.10, but boost-python3 uses Python 3.11. While it is possible to \"roll back\" the more advanced version (so that in this case boost-python3 uses Python 3.10) this is an advanced operation, and in many cases it is best to wait for an update to the other package. If you want to pursue that path anyway, look at the \"brew extract\" command, which you can use to extract a formula into a new cask (typically freecad/freecad). You can then edit that formula as needed.

You will need to set the path to Qt: Qt5 is currently supported, while support for Qt6 is a work-in-progress. Set FREECAD_QT_VERSION to \"Auto\" or \"5\" to select Qt5 (the default). On the command line, use something like:


```python
cmake \
  -DCMAKE_BUILD_TYPE="Release" \
  -DPYTHON_EXECUTABLE="/usr/local/bin/python3" \
  -DQt5_DIR="/usr/local/Cellar/qt@5/5.15.7/lib/cmake/Qt5" \
  -DPySide2_DIR="/usr/local/Cellar/pyside2@5.15.5/5.15.5/lib/cmake/PySide2-5.15.5" \
  -DShiboken2_DIR="/usr/local/Cellar/shiboken2@5.15.5/5.15.5_1/lib/cmake/Shiboken2-5.15.5" \
  ../freecad-source
```

## Get the source 

In the following instructions, the source and build folders are created side-by-side under


```python
/Users/username/FreeCAD
```

but you can use whatever folders you want.


```python
mkdir ~/FreeCAD
cd ~/FreeCAD
```

The following command will clone the FreeCAD git repository into a directory called FreeCAD-git.


```python
git clone https://github.com/FreeCAD/FreeCAD FreeCAD-git
```

Create the build folder.


```python
mkdir ~/FreeCAD/build
```

## Run CMake 

Next, we will run CMake to generate the build configuration. Several options must be passed to CMake. The following table describes the options and gives some background.

### CMake Options 

  Name                       Value                                    Notes
    
  CMAKE_BUILD_TYPE           Release (STRING)                         Release or Debug. Debug is generally used for developer-level testing but may also be required for user-level testing and troubleshooting.
  CMAKE_PREFIX_PATH          \"/usr/local/opt/qt5152;\" \... (PATH)   Required to build with Qt5. See note below. You also need to add path to VTK libraries and NGLIB libraries cmake configuration file.
  FREECAD_CREATE_MAC_APP     1 (BOOL)                                 Create a FreeCAD.app bundle at the location specified in CMAKE_INSTALL_PREFIX, when the \'make install\' command issued.
  CMAKE_INSTALL_PREFIX       \"./..\" (PATH)                          Path where you want to generate the FreeCAD.app bundle.
  FREECAD_USE_EXTERNAL_KDL   1 (BOOL)                                 Required.
  BUILD_FEM_NETGEN           1 (BOOL)                                 Required if choosing to build the FEM tools.

Note: Command line to generate CMAKE_PREFIX_PATH:

ls -d $(brew list -1 | grep qt | tail -1 | xargs brew --cellar)/*/lib/cmake

### CMake GUI 

Open the CMake app, and fill in the source and build folder fields. In this example, it would be **/Users/username/FreeCAD/FreeCAD-git** for the source, and **/Users/username/FreeCAD/build** for the build folder.

Next, click the **Configure** button to populate the list of configuration options. This will display a dialog asking you to specify what generator to use. Leave it at the default **Unix Makefiles.** Configuring will fail the first time because there are some options that need to be changed. Note: You will need to check the **Advanced** checkbox to get all of the options.

Set options from the table above, then click **Configure** again and then **Generate**.

### CMake command line 

Enter the following in the terminal.


```python
export PREFIX_PATH="/usr/local/opt/qt5152;\
/usr/local/Cellar/nglib/v6.2.2007/Contents/Resources;\
/usr/local/Cellar/vtk@8.2/8.2.0_1/lib/cmake;"
```


```python
$cd ~/FreeCAD/build
$cmake \
  -DCMAKE_BUILD_TYPE="Release"   \
  -DBUILD_QT5=1                  \
  -DWITH_PYTHON3=1               \
  -DCMAKE_PREFIX_PATH="$PREFIX_PATH" \
  -DPYTHON_EXECUTABLE="/usr/local/bin/python3" \
  -DFREECAD_USE_EXTERNAL_KDL=1   \
  -DCMAKE_CXX_FLAGS='-std=c++14' \
  -DBUILD_FEM_NETGEN=1           \
  -DFREECAD_CREATE_MAC_APP=1     \
  -DCMAKE_INSTALL_PREFIX="./.."  \
  ../FreeCAD-git/

```

## Run make 

Finally, from a terminal run **make** to compile and link FreeCAD, and generate the app bundle.


```python
cd ~/FreeCAD/build
make -j5 install
```

The -j option specifies how many make processes to run at once. One plus the number of CPU cores is usually a good number to use. However, if compiling fails for some reason, it is useful to rerun make without the -j option, so that you can see exactly where the error occurred.

See also [Compiling - Speeding up](Compiling_(Speeding_up).md).

If make finishes without any errors, you can now launch FreeCAD by double clicking the executable in the Finder.

## Updating from Github 

FreeCAD development happens fast; every day or so there are bug fixes or new features. To get the latest changes, use git to update the source directory (see [Source code management](Source_code_management.md)), then re-run the CMake and make steps above. It is not usually necessary to start with a clean build directory in this case, and subsequent compiles will generally go much faster than the first one.

## Building with Qt4 and Python 2.7 

FreeCAD has transitioned from Qt 4 to Qt 5 as well as homebrew. Qt 4 is no longer available as an option for new build on macOS following Qt 5 transition. Python 2.7 has been deprecated within homebrew and upcoming macOS and we do not support it anymore for macOS build either.

## Troubleshooting

### Segfault on Qt5 launch 

If Qt4 was previously installed via brew, and you then build with Qt5, you may get a EXC_BAD_ACCESS (SEGSEGV) exception when launching the new Qt5 build. The fix for this is to manually uninstall Qt4.


```python
brew uninstall --ignore-dependencies --force cartr/qt4/shiboken@1.2 cartr/qt4/pyside@1.2 cartr/qt4/pyside-tools@1.2 cartr/qt4/qt-legacy-formula
```

### Fortran

*\"No CMAKE_Fortran_COMPILER could be found.\"* during configuration - Older versions of FreeCAD will need a fortran compiler installed. With Homebrew, do \"brew install gcc\" and try configuring again, giving cmake the path to Fortran ie -DCMAKE_Fortran_COMPILER=/opt/local/bin/gfortran-mp-4.9 . Or, preferably use a more current version of FreeCAD source!

### FreeType

When using CMake versions older than 3.1.0, it\'s necessary to set CMake variable FREETYPE_INCLUDE_DIR_freetype2 manually, eg /usr/local/include/freetype2

### Additional Build Instructions 

FreeCAD can be built against the latest git master hosted on github, and launched from a CLI using libraries provided by the homebrew-freecad tap. For a complete list of build instructions see [here](https://github.com/ipatch/homebrew-us-05/tree/dev/freecad#building-freecad-for-macos-by-macos).



---
![](images/Right_arrow.png) [documentation index](../README.md) > [Developer_Documentation](Category_Developer_Documentation.md) > [Developer](Category_Developer.md) > Compile on MacOS/sv
