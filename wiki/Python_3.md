# Python 3
**
This roadmap is probably obsolete. For more information see [Development roadmap](Development_roadmap.md).<br>
If you are not involved with the development discussed here:<br>
!!! PLEASE DO NOT EDIT OR TRANSLATE !!!
**

 

The port of FreeCAD to Python 3 support is currently underway and progress is being tracked in [this forum thread](https://forum.freecadweb.org/viewtopic.php?f=10&t=12534). The master branch of FreeCAD is already usable with python3. Tests are passing, but there are still many little incompatibilities. TESTERS WANTED!

This document is a placeholder for various platforms\' build instructions and a checklist to monitor progress.

## Building FreeCAD w/ Python 3 

### Ubuntu

The first step in building FreeCAD for Python 3 is ensuring you can build normally. **Tip**: It\'s also helpful to have a cmake GUI tool like **cmake-qt-gui** or **cmake-curses-gui**.

The following instructions are adapted from a post by looo in the Python 3 porting thread: Note: tested only with linux/ubuntu.

Download the current master of FreeCAD

 git clone [https://github.com/FreeCAD/FreeCAD](https://github.com/FreeCAD/FreeCAD)

If python3 is your default python then there shouldn\'t be much to do. If not I think the easiest is to do: Set the python relevant cmake variables with cmake-gui which are: 


```python
- PYTHON_EXECUTABLE
- PYTHON_INCLUDE_DIR
- PYTHON_LIBRARY
- PYTHON_BASENAME (=PySideConfigPYTHON_SUFFIX.cmake) -> for me on ubuntu this would be this: .cpython-35m-x86_64-linux-gnu
- PYTHON_SUFFIX (=ShibokenConfigPYTHON_SUFFIX.cmake) -> eg.: .cpython-35m-x86_64-linux-gnu
```



#### Pivy

python3 builds for freecad are available with this [ppa](https://launchpad.net/~sppedflyer/+archive/ubuntu/mytestppa1) 


```python
sudo add-apt-repository ppa:sppedflyer/mytestppa1
sudo apt-get update
sudo apt-get install python3-pivy
```



#### PySide

PySide for python3.5 isn\'t officially available, but I think ubuntu provides a build. 


```python
sudo apt-get install python3-pyside
```



## Test builds on anaconda (linux64) 




```python
wget -c http://repo.continuum.io/miniconda/Miniconda-latest-Linux-x86_64.sh
bash Miniconda-latest-Linux-x86_64.sh
```

 and follow the instructions

once miniconda is installed we have to configure conda to have access to the freecad-builds: 


```python
conda config --add channels conda-forge
conda config --add channels freecad
```

 now we create a new enviroment and install freecad 


```python
conda create --name freecad_py3 python=3.6 freecad
```

 this will download all the necessary packages. When done activate the enviroment and start FreeCAD 


```python
source activate freecad_py3
FreeCAD
```

 the first time you launch freecad, matplotlib loads some modules, and therefore FreeCAD will need some time to show up.

### Alternate Install 

#### Conda




```python
Install miniconda: http://conda.pydata.org/miniconda.html 
```

 Install conda-build: 


```python
conda install conda_build
```

 Add channels: 


```python
conda config --add channels freecad
conda config --add channels conda-forge
```

 Clone the current Python 3 port of FreeCAD 


```python
git clone https://github.com/looooo/FreeCAD/tree/py3-27
```

 Clone the conda-recipes for FreeCAD 


```python
git clone https://github.com/looooo/FreeCAD_Conda
```

 - go to FreeCAD\_Conda/.FreeCAD\_debug

\- set the variables on top of the script (the path to FreeCAD, and if you want to build with calling cmake) 


```python
conda build . --python=3.6 --dirty
```

 (the dirty flag isn\'t necessary if you build the first time. If it isn\'t set conda does a full build all the time. The python option is not necessary if you have installed python3.6 miniconda version. But then you have to set this flag to build with python2.7\....)

## Links

-   Follow latest Pyside developments:

:\* Progress Notes: <https://wiki.qt.io/PySide2#Pyside_Development_Progress_Notes>

:\* Git commits: <http://code.qt.io/cgit/pyside/pyside.git/log/>



---
![](images/Right_arrow.png) [documentation index](../README.md) > [User Documentation](Category_User Documentation.md) > [Administration](Category_Administration.md) > Python 3
