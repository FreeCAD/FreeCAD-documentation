# Compile on MacOS/tr
**There is an experimental FreeCAD Docker container that is being tested for FreeCAD development. Read more about it at [[Compile on Docker]]**


{{TOCright}}

## Overview

This page describes how to compile the FreeCAD source code on MacOS X. For other platforms, see [Compiling](Compiling.md).

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

FreeCAD maintains a Homebrew \'tap\' which installs the required formulas and dependencies. Issue the following brew commands in your terminal.


```python
brew tap freecad/freecad
brew install eigen
brew install --only-dependencies freecad --with-packaging-utils
```

Notes:

1.  \'brew install\' may take quite a while, so you may want go grab a beverage. :-).
2.  Homebrew is currently shipping with Boost 1.73, which contains a bug to compile FreeCAD please edit the file /usr/local/opt/boost/include/boost/geometry/index/detail/rtree/visitors/insert.hpp and on line 265 declare MembersHolder::visitor as being a Public value by replacing : MembersHolder::visitor with : public MembersHolder::visitor

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

  Name                          Value                                    Notes
  ----------------------------- ---------------------------------------- --------------------------------------------------------------------------------------------------------------------------------------------
  CMAKE\_BUILD\_TYPE            Release (STRING)                         Release or Debug. Debug is generally used for developer-level testing but may also be required for user-level testing and troubleshooting.
  BUILD\_QT5                    1 (BOOL)                                 Required to build with Qt5.
  CMAKE\_PREFIX\_PATH           \"/usr/local/opt/qt5152;\" \... (PATH)   Required to build with Qt5. See note below. You also need to add path to VTK libraries and NGLIB libraries cmake configuration file.
  FREECAD\_CREATE\_MAC\_APP     1 (BOOL)                                 Create a FreeCAD.app bundle at the location specified in CMAKE\_INSTALL\_PREFIX, when the \'make install\' command issued.
  CMAKE\_INSTALL\_PREFIX        \"./..\" (PATH)                          Path where you want to generate the FreeCAD.app bundle.
  FREECAD\_USE\_EXTERNAL\_KDL   1 (BOOL)                                 Required.
  BUILD\_FEM\_NETGEN            1 (BOOL)                                 Required if choosing to build the FEM tools.

Note: Command line to generate CMAKE\_PREFIX\_PATH:

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

If Qt4 was previously installed via brew, and you then build with Qt5, you may get a EXC\_BAD\_ACCESS (SEGSEGV) exception when launching the new Qt5 build. The fix for this is to manually uninstall Qt4.


```python
brew uninstall --ignore-dependencies --force cartr/qt4/shiboken@1.2 cartr/qt4/pyside@1.2 cartr/qt4/pyside-tools@1.2 cartr/qt4/qt-legacy-formula
```

### Fortran

*\"No CMAKE\_Fortran\_COMPILER could be found.\"* during configuration - Older versions of FreeCAD will need a fortran compiler installed. With Homebrew, do \"brew install gcc\" and try configuring again, giving cmake the path to Fortran ie -DCMAKE\_Fortran\_COMPILER=/opt/local/bin/gfortran-mp-4.9 . Or, preferably use a more current version of FreeCAD source!

### OpenGL

See [OpenGL on MacOS](OpenGL_on_MacOS.md) for OpenGL issues when Qt 4.8 and earlier are used on MacOS.

### FreeType

When using CMake versions older than 3.1.0, it\'s necessary to set CMake variable FREETYPE\_INCLUDE\_DIR\_freetype2 manually, eg /usr/local/include/freetype2

### Additional Build Instructions 

FreeCAD can be built against the latest git master hosted on github, and launched from a CLI using libraries provided by the homebrew-freecad tap. For a complete list of build instructions see [here](https://github.com/ipatch/homebrew-us-05/tree/dev/freecad#building-freecad-for-macos-by-macos).







[Category:Developer\_Documentation](Category:Developer_Documentation.md) [Category:Developer](Category:Developer.md)

---
[documentation index](../README.md) > [Developer_Documentation](Category:Developer_Documentation.md) > Compile on MacOS/tr
