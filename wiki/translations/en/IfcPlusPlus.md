# IfcPlusPlus/en
## Description




[IFC++](IfcPlusPlus.md) or [IfcPlusPlus](IfcPlusPlus.md) is a C++ open source (MIT license) library from the [IfcQuery](IfcPlusPlus.md) project for reading, writing, and viewing [IFC](Arch_IFC.md) files.

The IFC++ library can be used for general purpose, and it also includes a sample IFC visualization application. This viewer is based on Qt 5 and OpenSceneGraph (OSG), and can load big IFC files very fast, and thus can be used to compare the performance of other IFC viewers, like Blender and FreeCAD, which internally use the [IfcOpenShell](IfcOpenShell.md) library.

<img alt="" src=images/IfcQuery_viewer_example.png  style="width:600px;">



*The sample IFC viewer included in the source distribution of the IfcQuery/IFC++ libraries.*


**Note:**

in common usage, the names \"IfcQuery\", \"IFC++\", and \"IfcPlusPlus\" may be used interchangeably to refer to the same thing, the C++ library, or more specifically the free IFC viewer.

## Installing

The IFC++ distribution is provided as source code, so to use the library and the viewer, the code must be compiled.

IFC++ is developed mostly on a Windows platform, so it includes solution (`.snl`) and project (`.vcxproj`) files to compile the `IfcPlusPlus.dll` dynamic library using Visual Studio. A static library `libIfcPlusPlus.a` can also be produced for Linux using CMake.


**Note:**

there is a more complete viewer that uses pre-compiled IFC++ libraries intended for Windows. This viewer is free for use but is not open source. It is available by downloading the `SimpleViewerExampleQt.zip` package from {{URL|http://www.ifcquery.com/}}, and running `SimpleViewerExampleQt.exe`. This viewer is self-contained, everything that it requires to run is included in the `.zip` archive.

## Compiling in Windows 

Follow the instructions in the official [ifcplusplus](https://github.com/ifcquery/ifcplusplus) repository.

## Compiling in Linux 

The general instructions are as follows:

1.  Get the source code of IFC++ from its main repository.
2.  Gather all dependencies for compiling, including a C++ compiler, CMake, and Make, and the development files for Boost, Qt 5, as well as the OpenSceneGraph (OSG) library for visualization.
3.  Run `cmake` to generate a `Makefile`, then start the compilation by running `make`.
4.  Install the `libIfcPlusPlus.a` and `libcarve.so` libraries to the appropriate library path so that they are found by the IFC++ sample viewer.

### Prerequisites

In a Debian/Ubuntu based distribution, getting the required development files is usually simple. 
```python
sudo apt install git cmake gcc g++ libboost-all-dev
sudo apt install qt5-qmake qtbase5-dev qttools5-dev libqt5widgets5 libqt5opengl5-dev
```

Get the source code of the project and place it in a custom directory to which you have full write access. 
```python
git clone https://github.com/ifcquery/ifcplusplus ifcplusplus-source
```

### OpenSceneGraph

[OpenSceneGraph](http://www.openscenegraph.org/) (OSG) is a collection of C++ libraries that uses OpenGL for 3D visualization; it can be used in games, virtual reality, scientific visualization and modelling.


```python
sudo apt install libopenscenegraph-3.4-dev
```

If the files are too old in your distribution, you may also compile the libraries yourself. The procedure is outlined in the main repository, [openscenegraph/OpenSceneGraph](https://github.com/openscenegraph/OpenSceneGraph). Compiling is straight forward, although you may need various dependencies like Qt 5, Freetype, Inventor, OpenEXR, COLLADA, ZLIB, GDAL, FFmpeg, Gstreamer, SDL, Cairo, and Poppler.


```python
git clone https://github.com/openscenegraph/OpenSceneGraph OpenSceneGraph-source

mkdir -p OpenSceneGraph-build
cd OpenSceneGraph-build
cmake ../OpenSceneGraph-source

make -j 3
sudo make install
```

### Carve

Carve is a [constructive solid geometry](constructive_solid_geometry.md) (CSG) C++ library designed to perform boolean operations between two arbitrary polygonal meshes. Together with the IFC++ library, `libIfcPlusPlus.a`, Carve is used by the IFC++ sample viewer to open and display IFC files.

-   Original repository: [carve](https://code.google.com/archive/p/carve/), GPL2, from 2009 to 2011.
-   New repository: [folded/carve](https://github.com/folded/carve), from 2011 onwards; the project changed to the MIT License starting on October, 2015.

As the project is now MIT licensed, copies of the Carve source files are now included in the IFC++ repository. This means that when compiling IFC++, `libcarve.so` will be compiled as well. This library must be available in the system for the IFC++ sample viewer to work properly.

### CMake configuration 

It is recommended to perform the configuration and compilation in a specific build directory separate from the source directory.


```python
mkdir -p ifcplusplus-build
cd ifcplusplus-build

cmake ../ifcplusplus-source/
```

By default the type of build is `Release` but it can also be set to `Debug`. 
```python
cmake -DCMAKE_BUILD_TYPE=Debug ../ifcplusplus-source/
```

### Actual compilation 

If there were no error messages during configuration with CMake, a `Makefile` should have been created in the build directory, so you can proceed to compile the libraries by running `make`.


```python
make -j N
```


`N`

is the number of processors that you assign to the compilation process; choose at least one fewer than the total number of CPU cores that you have.

### Testing the compilation in the build directory 

If the build was successful you should have a `Release/` subdirectory with the newly compiled libraries. 
```python
Release/libcarve.so
Release/libIfcPlusPlus.a
Release/SimpleViewerExample
```

You can launch the `SimpleViewerExample` executable with an [IFC](Arch_IFC.md) file as input. 
```python
Release/SimpleViewerExample IfcOpenHouse.ifc
```

If the build type was set to `Debug`, then the compiled libraries will appear in the `Debug/` subdirectory instead.

### Installation of the compiled libraries 

If the compilation doesn\'t report any errors, you may run `make install` to copy the headers, compiled libraries, and binaries to their corresponding installation directories. 
```python
sudo make install
```

By default, the `CMAKE_INSTALL_PREFIX` is `/usr/local/`, so all compiled files will be placed under this directory, which normally requires elevated privileges. {{Code|lang=sh|code=
/usr/local/bin/SimpleViewerExample
/usr/local/lib/libcarve.so
/usr/local/lib/libIfcPlusPlus.a
/usr/local/include/carve/*.{h, hpp}
/usr/local/include/ifcpp/geometry/*.h
/usr/local/include/ifcpp/geometry/Carve/*.h
/usr/local/include/ifcpp/geometry/OCC/*.h
/usr/local/include/ifcpp/IFC4/*.h
/usr/local/include/ifcpp/IFC4/include/*.h
/usr/local/include/ifcpp/model/*.h
/usr/local/include/ifcpp/reader/*.h
/usr/local/include/ifcpp/writer/*.h
/usr/local/share/IFCPP/cmake/*.cmake
}}

### Library path 

Once `SimpleViewerExample` is placed in `/usr/local/bin`, the executable will be available in the entire system. However, in certain platforms `libcarve.so` may not be found if it is installed in the default `/usr/local/lib` directory. {{Code|lang=md|code=
SimpleViewerExample: error while loading shared libraries: libcarve.so: cannot open shared object file: No such file or directory
}}

If this is the case, it may be enough to update the cache of the `ld.so` library loader by calling `ldconfig`: 
```python
sudo ldconfig
```

Or you may have to move the library to the correct directory first: 
```python
sudo mkdir -p /usr/local/lib/x86_64-linux-gnu/
sudo mv /usr/local/lib/libcarve.so /usr/local/lib/x86_64-linux-gnu/libcarve.so
sudo ldconfig
```

Alternatively, you may set the `LD_LIBRARY_PATH` variable to the directory containing `libcarve.so`, before launching the executable: 
```python
LD_LIBRARY_PATH=/usr/local/lib SimpleViewerExample
```

To make this effect persistent, this environmental variable can be set in the shell resource file, for example, `.bashrc`, so that it is propagated to all terminal instances on startup: 
```python
export LD_LIBRARY_PATH=/usr/local/lib:$LD_LIBRARY_PATH
```

### Removing the compiled libraries 

To remove the installed libraries, just remove the corresponding files that were installed. {{Code|lang=sh|code=
sudo rm -rf /usr/local/bin/SimpleViewerExample
sudo rm -rf /usr/local/lib/libcarve.so
sudo rm -rf /usr/local/lib/libIfcPlusPlus.a
sudo rm -rf /usr/local/include/carve
sudo rm -rf /usr/local/include/ifcpp
sudo rm -rf /usr/local/share/IFCPP/cmake/
}}

## Fixes for Linux 

The IFC++ library is developed by its author on a Windows system. This means that even if the code depends on multiplatform libraries like Boost, Qt, and OpenSceneGraph, the code is mostly tested to compile and run on Windows. Nevertheless, over the years other developers have provided fixes to the project so that IFC++ can be compiled and run on Linux distributions.

In particular, a fork of the main project is maintained with small fixes to compile and run better in Debian.

-   [berndhahnebach/ifcplusplus](https://github.com/berndhahnebach/ifcplusplus/)

If the code of the official repository does not work or seems to have issues in Linux, try following the same compilation instructions but using the sources from this alternative repository. This repository is often some commits behind the main distribution, but it aims to remain up to date, and at the same time provide some Linux specific fixes. These improvements are normally submitted back to the main repository in order to make the official branch compile on Linux without issues.

The main developer of IFC++ does not support Linux directly, so Linux developers should be prepared to troubleshoot problems, fix them, and submit patches when using IFC++ in Linux.

### Invisible icons 

For the `SimpleViewerExample`, there are two buttons in the main interface which are invisible if the custom style sheet is not found. {{Code|lang=cpp|code=
QIODevice::read (QFile, ":styles.css"): device not open
}}

The style must be included in the CMake configuration in the section devoted to the Qt libraries: {{Code|lang=cmake|code=
# ifcplusplus-source/examples/SimpleViewerExampleQt/CMakeLists.txt
...
ADD_DEFINITIONS(${Qt5Widgets_DEFINITIONS})

SET(viewer_dir ${IFCPP_SOURCE_DIR}/examples/SimpleViewerExampleQt)
SET(RESOURCES ${viewer_dir}/Resources/ifcplusplus.qrc)
QT5_ADD_RESOURCES(SimpleViewerExample_RESOURCES_RCC ${RESOURCES})
}}

## More information 

-   [IFC++ project page](https://www.ifcquery.com/)
-   [ifcquery/ifcplusplus](https://github.com/ifcquery/ifcplusplus) repository
-   Alternative repository, especially for Debian: [berndhahnebach/ifcplusplus](https://github.com/berndhahnebach/ifcplusplus/)
-   Forum thread: [IFC Viewer ifcplusplus](https://forum.freecadweb.org/viewtopic.php?f=39&t=5101) (2013 to 2020)
-   [IfcPlusPlus compiled on Gentoo - questions and alternatives?](https://forum.freecadweb.org/viewtopic.php?f=39&t=33254)
-   German thread: [IfcQuery / IfcPlusPlus selber kompilieren](https://forum.freecadweb.org/viewtopic.php?f=13&t=48648)


 {{FEM Tools navi}}



---
⏵ [documentation index](../README.md) > [Arch](Category_Arch.md) > [FEM](Category_FEM.md) > IfcPlusPlus/en
