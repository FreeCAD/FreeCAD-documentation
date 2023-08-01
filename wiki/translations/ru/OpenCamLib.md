# OpenCamLib/ru
{{TOCright}}



## Описание

OpenCamLib (OCL) is an open source library aiming to provide computer aided manufacturing (CAM) algorithms. FreeCAD uses OCL in the experimental **<img src="images/Path_Surface.svg" width=24px> [3D Surface](Path_Surface.md)** path operations and other experimental features.

Github: <https://github.com/aewallin/opencamlib>

Website: <http://www.anderswallin.net/CAM/>



## Установка

### Windows

**Note:** Beginning with FreeCAD version 0.19, OCL should be included with all Windows distribution packages.

To install OCL on Windows, follow these instructions.

1.  Obtain the Python version of OpenCamLib (OCL).
    -   Build from [source](https://github.com/aewallin/opencamlib) using the Python version used by your FreeCAD version. Peter Lama\'s [fork of the same](https://github.com/peterlama/opencamlib) source has project files for a MSVC build.
    -   Download the Python 2.7 x86/x64 [binary](https://github.com/sgrogan/opencamlib/releases) by sgrogan on GitHub.
    -   Download the Python 3.6 x64 [binary](https://github.com/sgrogan/opencamlib/releases) by sgrogan on GitHub.
2.  Navigate to your OCL build *or* binary folder
3.  Copy the **ocl.pyd** library file
4.  Proceed with one of the following four(4) options:
    -   Navigate to your **FreeCAD\\lib** folder, and paste the **ocl.pyd** file there. {{ColoredText||red|(''This is the preferred option.'')}}
    -   Navigate to your **FreeCAD\\bin** folder, and paste the **ocl.pyd** file there.
    -   Navigate to your **FreeCAD\\Mod** folder. Create a new folder, **OCL**. Enter the **OCL** folder and paste the **ocl.pyd** file.
    -   Navigate to your **%USERPROFILE%\\AppData\\Roaming\\FreeCAD** folder. Create a new folder, **Mod**. Enter the **Mod** folder. Create a new **OCL** folder. Enter the **OCL** folder and paste the **ocl.pyd** file. {{ColoredText||red|(''This is the least preferred option.'')}}
5.  Restart FreeCAD
6.  Verify proper installation
    1.  Click **View** → **Panels** → **Python console**.
    2.  Type \"**import ocl**\" into the Python console and press the **enter** key.
    3.  If no error appears, you have correctly installed OCL
        -   If you receive an error:
            -   Check the placement and name of the **ocl.pyd** file as instructed above
            -   Verify the correct architecture type of the OCL library you installed - x86 or x64
            -   Verify the Python version used to build the OCL library is the same as that of your FreeCAD software - 2.7 or 3.6 currently

### Linux

The repository is [here](https://github.com/aewallin/opencamlib) and contains basic installation instructions.

Before beginning installation, or during the installation process, you will probably find you need to install some additional packages:

#### Ubuntu/Debian

For example: {{Code|lang=bash|code=
sudo apt install cmake
sudo apt install libboost-program-options-dev
# Optional, for documentation:
sudo apt-get install doxygen
sudo apt-get install texlive-full
}}

Note: the \"libboost-program-options-dev\" may be substituted with \"libboost-all-dev\".

If you are struggling, carefully review any error messages you get during the cmake and make phases as you may need to install additional packages.

#### Archlinux

1.  Install OpenCamLib from the [AUR package](https://aur.archlinux.org/packages/opencamlib-git).
2.  Then run the following code snippet inside FreeCAD\'s [Python console](Python_console.md)


{{Code|lang=bash|code=
import sys
sys.path.append('/usr/opencamlib/')
import ocl
}}

#### Python 3 

Identify the version of cmake you have installed with cmake --version

For cmake \>= 3.12, add these flags:


{{Code|lang=bash|code=
cmake -DBUILD_PY_LIB=ON -DUSE_PY_3=ON -DCMAKE_BUILD_TYPE=Release ../src -Wno-dev
}}

For cmake \< 3.12 (like in Ubuntu 18.04, which has 3.10), first you\'ll need to edit src/pythonlib/pythonlib.cmake, and apply this patch:

Index: opencamlib-2019.07/src/pythonlib/pythonlib.cmake
===================================================================
--- opencamlib-2019.07.orig/src/pythonlib/pythonlib.cmake
+++ opencamlib-2019.07/src/pythonlib/pythonlib.cmake
@@ -48,13 +48,13 @@ if(${CMAKE_VERSION} VERSION_LESS "3.12.0
     message("Python not found")
   endif()
   execute_process(
-    COMMAND ${PYTHON_EXECUTABLE} -c "from distutils.sysconfig import get_python_lib; print get_python_lib(0,0,\"/usr/local\")"
+    COMMAND ${PYTHON_EXECUTABLE} -c "import site; print(site.getsitepackages()[-1])"
     OUTPUT_VARIABLE PYTHON_SITE_PACKAGES
     OUTPUT_STRIP_TRAILING_WHITESPACE
   ) # on Ubuntu 11.10 this outputs: /usr/local/lib/python2.7/dist-packages
 
   execute_process(
-    COMMAND ${PYTHON_EXECUTABLE} -c "from distutils.sysconfig import get_python_lib; print get_python_lib(plat_specific=1,standard_lib=0,prefix=\"/usr/local\")"
+    COMMAND ${PYTHON_EXECUTABLE} -c "import site; print(site.getsitepackages()[-1])"
     OUTPUT_VARIABLE PYTHON_ARCH_PACKAGES
     OUTPUT_STRIP_TRAILING_WHITESPACE
   )

Then, in order for Python 3 to be detected correctly you\'ll need to add 2 more flags to the cmake line:


{{Code|lang=bash|code=
cmake -DBUILD_PY_LIB=ON -DUSE_PY_3=ON -DPYTHON_EXECUTABLE="$(which python3)" -DPYTHON_VERSION_SUFFIX=3 -DCMAKE_BUILD_TYPE=Release ../src -Wno-dev
}}

See the FreeCAD forum at [Re: How to activate openCamLib after compiling it](https://forum.freecadweb.org/viewtopic.php?p=316970#p316988), and a few posts following.

### Mac


{{Code|lang=bash|code=
git clone https://github.com/aewallin/opencamlib
cd opencamlib
mkdir build
cd build
cmake -DBUILD_PY_LIB=ON -DUSE_PY_3=ON -DCMAKE_BUILD_TYPE=Release .. -Wno-dev
make -j4
make install
}}

To test the build enter the following in the [Python console](Python_console.md):


```python
import area
import ocl
dir(ocl)
```

The return value should be:


```python
['AdaptivePathDropCutter', 'AdaptivePathDropCutter_base', 'AdaptiveWaterline', 'AdaptiveWaterline_base', 'Arc', 'ArcSpanType', 'BallConeCutter', 'BallCutter', 'BatchDropCutter', 'BatchDropCutter_base', 'BatchPushCutter', 'BatchPushCutter_base', 'Bbox', 'BullConeCutter', 'BullCutter', 'CCPoint', 'CCType', 'CLPoint', 'CompBallCutter', 'CompCylCutter', 'ConeConeCutter', 'ConeCutter', 'CutterLocationSurface', 'CylConeCutter', 'CylCutter', 'Ellipse', 'EllipsePosition', 'Fiber', 'Fiber_base', 'Interval', 'Line', 'LineCLFilter', 'LineCLFilter_base', 'LineSpanType', 'MillingCutter', 'Path', 'PathDropCutter', 'PathDropCutter_base', 'Path_base', 'Point', 'STLReader', 'STLSurf', 'STLSurf_base', 'SpanType', 'Triangle', 'Triangle_base', 'Waterline', 'Waterline_base', 'WeaveVertexType', 'ZigZag', 'ZigZag_base', '__doc__', '__file__', '__loader__', '__name__', '__package__', '__spec__', 'eps', 'epsD', 'epsF', 'version']
```

In case of an error the return value will be:


```python
['__doc__', '__file__', '__loader__', '__name__', '__package__', '__path__', '__spec__']
```

For cmake the Release option is very important, when using Debug area and ocl will collide and either library will not load (depending on what what was loaded first).

## More help 

In case you run into difficulties, you may find additional help at these forum posts:

-   [Windows](https://forum.freecadweb.org/viewtopic.php?t=19205)
-   [Linux](https://forum.freecadweb.org/viewtopic.php?t=18017)

## Acknowledgments

Thank you to [Dr. Anders Wallin](http://www.anderswallin.net/about/) for providing OCL to the public.



---
![](images/Button_right.svg) [documentation index](../README.md) > [User Documentation](Category_User Documentation.md) > [3rd Party](Category_3rd Party.md) > OpenCamLib/ru
