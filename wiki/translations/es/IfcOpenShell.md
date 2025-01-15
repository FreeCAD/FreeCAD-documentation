# IfcOpenShell/es
## Descripción




[IfcOpenShell](IfcOpenShell/es.md) es una biblioteca de software de código abierto (LGPL 3) que ayuda a los desarrolladores a trabajar con el formato de archivo [industry foundation classes](http://www.buildingsmart-tech.org/specifications/ifc-overview) ([IFC](Arch_IFC/es.md)). El formato de archivo IFC puede utilizarse para describir datos de construcción y edificación. El formato se utiliza habitualmente para [building information modelling](https://en.wikipedia.org/wiki/Building_information_modeling) (BIM), por ejemplo, para el análisis de cargas mecánicas y para los estudios de eficiencia térmica y energética. IfcOpenShell es principalmente una colección de librerías C++, sin embargo, como tiene enlaces [Python](Python/es.md), puede integrarse con programas como FreeCAD y Blender.

IfcOpenShell utiliza [OpenCASCADE](OpenCASCADE/es.md) internamente para convertir la geometría implícita de los archivos IFC en geometría explícita que otros paquetes CAD pueden entender, por ejemplo, STEP, [OBJ](Arch_OBJ/es.md), y [DAE](Arch_DAE/es.md).


<div class="mw-translate-fuzzy">

A partir de la v0.19, FreeCAD es capaz de importar archivos IFC siempre que el módulo `ifcopenshell` [Python](Python/es.md) esté disponible en el sistema. Asimismo, los [Arquitectura](Arch_Workbench/es.md) y [BIM ambientes de trabajo](BIM_Workbench/es.md) pueden exportar un modelo de edificio al formato IFC para que pueda ser utilizado en otras aplicaciones.


</div>

Para verificar que IfcOpenShell está instalado en su sistema, intente importarlo desde la [Consola de Python](Python_console/es.md); la biblioteca está correctamente instalada si no se devuelve ningún mensaje de error.


```python
import ifcopenshell
```



## Instalación

IfcOpenShell puede instalarse de varias maneras, dependiendo de su sistema operativo y del entorno de Python. En el pasado, IfcOpenShell era un poco difícil de instalar, ya que tenía que ser compilado para su sistema específico; sin embargo, a partir de este escrito (2020) es más fácil empezar a usarlo, ya que ahora se incluye junto con FreeCAD en muchas distribuciones de FreeCAD. En general, es aconsejable utilizar una de estas distribuciones precompiladas, y sólo compilarlo tú mismo si eres un usuario avanzado.

### From BlenderBIM 

[BlenderBIM](https://blenderbim.org) is another project that uses IfcOpenShell. They provide up-to-date IfcOpenShell packages for several platforms. This is the best way to make sure you have a recent version of IfcOpenShell.

BlenderBIM IfcOpenShell install page: <https://blenderbim.org/docs-python/ifcopenshell-python/installation.html>

### Pip

The easiest way to install IfcOpenShell is using [pip](https://pypi.org/project/pip/). Once pip is installed on your system, you can [install](https://datatofish.com/install-package-python-using-pip/) IfcOpenShell easily by issuing from a terminal window:


```python
pip install ifcopenshell
```

### Conda

Para los sistemas Windows y MacOS, las distribuciones de FreeCAD que se han creado con el gestor de paquetes [Conda](Conda/es.md) suelen incluir ya IfcOpenShell, por lo que no es necesaria ninguna instalación adicional. Obtén la distribución apropiada desde la página [Download](Download/es.md).

La [AppImage](AppImage/es.md) para Linux también se basa en [Conda](Conda/es.md), y también incluye IfcOpenShell.

### Linux

Si está disponible, puede instalar IfcOpenShell utilizando el gestor de paquetes de su distribución.


```python
sudo apt install ifcopenshell
```

Sin embargo, tenga en cuenta que los paquetes proporcionados por muchos repositorios de Linux tienden a ser antiguos, y pueden no contener los últimos desarrollos del software. Si quieres estar seguro de que estás utilizando el software más reciente, utiliza una distribución de FreeCAD basada en [Conda](Conda/es.md), una distribución precompilada de IfcOpenShell, o compila tú mismo IfcOpenShell.



### Utilizar un paquete IfcOpenShell precompilado 

Hay un repositorio especial del proyecto IfcOpenShell que compila regularmente las bibliotecas de IfcOpenShell para varios sistemas (Linux, Windows, MacOS), arquitecturas (32 y 64 bits), y versiones de Python (2.7, 3.x). Para utilizar estas librerías precompiladas, debes elegir la versión correcta que coincida con tu sistema operativo, arquitectura, y los números mayor y menor del [Python](Python/es.md) que se utiliza con FreeCAD. Esto significa que los dos primeros números deben coincidir (Python 3.6 y 3.7 se consideran versiones distintas) mientras que el tercero (micro) no importa (Python 3.6.5 y 3.6.12 se consideran iguales a efectos de compatibilidad).

1.  Dirígete al repositorio de construcción [IfcOpenBot/IfcOpenShell](https://github.com/IfcOpenBot/IfcOpenShell). Este repositorio no es para desarrollo, sólo contiene una copia del repositorio principal así como paquetes precompilados.
2.  En el momento de escribir este artículo (2020), la rama maestra del proyecto IfcOpenShell no contiene el último código, por lo que debemos seleccionar la rama deseada, por ejemplo, `v0.6.0`.
3.  Haga clic en el número de commit, que le llevará a la lista de commits de la rama, por ejemplo, `IfcOpenBot/IfcOpenShell/commits/v0.6.0`.
4.  Retrocede en el historial hasta encontrar un commit que tenga un comentario. Esto indicará el momento en que las bibliotecas precompiladas fueron liberadas.
5.  Haga clic en el commit. Verás un comentario de IfcOpenBot que muestra una tabla de combinaciones de sistema operativo, arquitectura y versión de Python. Elige el enlace correcto para \"Python\" que coincida con tu [versión de FreeCAD](Std_About/es.md). Los paquetes \"Blender\", \"IfcConvert\" e \"IfcGeomServer\" no son necesarios para el uso de FreeCAD.
6.  El paquete descargado necesita ser extraído, y el directorio extraído necesita ser colocado en la ruta de búsqueda de Python para encontrar los nuevos módulos.


**Nota:**

los siguientes ejemplos suponen un sistema basado en Debian/Ubuntu, pero el procedimiento general debería funcionar para otros sistemas operativos.

  - Al descomprimir el paquete descargado se crea una carpeta `ifcopenshell/`. 
```python
unzip ifcopenshell-python-36-v0.6.0-4baec57-linux64.zip
```

  - La ruta de búsqueda se puede encontrar inspeccionando la variable `sys.path` en la [consola de Python](Python_console/es.md). 
```python
import sys
print(sys.path)
```

  - Si quieres instalar la librería IfcOpenShell sólo para tu usuario, y que no afecte a los directorios del sistema, debes colocar la carpeta extraída `ifcopenshell/` en el directorio principal de tu propio usuario. 
```python
mv -t $HOME/.local/lib/python3.6/site-packages/ ifcopenshell/
```

Si desea instalar la biblioteca IfcOpenShell en todo el sistema, normalmente necesitará privilegios de superusuario para escribir en los directorios del sistema; normalmente se trata de un directorio `site-packages/`, o un directorio `dist-packages/` para las distribuciones Debian/Ubuntu. 
```python
sudo mv -t /usr/local/lib/python3.6/dist-packages/ ifcopenshell/
```

Si el directorio se ha movido correctamente, comprueba que el módulo `ifcopenshell` es accesible desde la [Consola de Python](Python_console/es.md). 
```python
>>> import ifcopenshell
>>> print(ifcopenshell.version)
0.6.0b0
>>> print(ifcopenshell.__path__)
['/home/user/.local/lib/python3.6/site-packages/ifcopenshell']
```

Para eliminar la biblioteca instalada, basta con eliminar el directorio correspondiente con todos los módulos dentro. 
```python
rm -rf $HOME/.local/lib/python3.6/site-packages/ifcopenshell/
sudo rm -rf /usr/local/lib/python3.6/dist-packages/ifcopenshell/
```



## Compilación

Compiling IfcOpenShell is recommended only for advanced users. The process is similar to [compiling FreeCAD on Linux](Compile_on_Linux.md), so if you have done this already, then you may already have the necessary requisites like the [OpenCASCADE\'s](OpenCASCADE.md) development files. The process uses the CMake configuration tool to produce a custom `Makefile` for use with the Make tool.

The general instructions are outlined in the [IfcOpenShell repository](https://github.com/IfcOpenShell/IfcOpenShell), and are as follows:

1.  Get the source code of IfcOpenShell from its main repository.
2.  Gather all dependencies for compiling, including a C++ compiler, CMake, and Make, and the development files for Boost, libxml2, [OpenCASCADE](OpenCASCADE.md), SWIG, Python, and OpenCOLLADA (optional). Most of these components are strictly optional, however, for use with FreeCAD they should all be installed. OpenCOLLADA is optional as it only provides [DAE](Arch_DAE.md) support for the `IfcConvert` binary.
3.  Run `cmake` to generate a `Makefile`, then start the compilation by running `make`.
4.  Install the `ifcopenshell` [Python](Python.md) module in the appropriate `site-packages/` directory so that it is found by FreeCAD.


**Note:**

the following examples assume a Debian/Ubuntu based system, but the general procedure should work for other operating systems. For example, in Debian shared libraries are normally located in `/usr/lib/x86_64-linux-gnu/` while in other distributions this may be `/usr/lib64/` so the paths should be adjusted accordingly.



### Prerequisitos

Instale las herramientas básicas de compilación. 
```python
sudo apt install git cmake gcc g++ libboost-all-dev
```

Obtenga el código fuente del proyecto y colóquelo en un directorio personalizado al que tenga acceso total de escritura.

As of this writing (2020), the master branch of the IfcOpenShell project does not contain the latest code, so we need to clone a specific branch. 
```python
git clone https://github.com/IfcOpenShell/IfcOpenShell -b v0.6.0 IfcOpenShell-source
```

### OpenCASCADE

Install the development files of [OpenCASCADE](OpenCASCADE.md). 
```python
sudo apt install libocct*-dev
```

Which expands to 
```python
sudo apt install libocct-data-exchange-dev libocct-draw-dev libocct-foundation-dev libocct-modeling-algorithms-dev libocct-modeling-data-dev libocct-ocaf-dev libocct-visualization-dev
```

You may use the community edition (OCE) of OpenCASCADE as well, however, please notice that this version is old and no longer recommended by FreeCAD as of 2020.

### OpenCOLLADA

Install the development files of OpenCOLLADA. 
```python
sudo apt install opencollada-dev
```

If the files are too old in your distribution, you may also compile the libraries yourself. The procedure is outlined in the main repository, [KhronosGroup/OpenCOLLADA](https://github.com/KhronosGroup/OpenCOLLADA), and it\'s very straight forward as it only requires the `libpcre3` and `libxml2` development files.


```python
sudo apt install libpcre3-dev libxml2-dev
git clone https://github.com/KhronosGroup/OpenCOLLADA OpenCOLLADA-source

mkdir -p OpenCOLLADA-build
cd OpenCOLLADA-build
cmake ../OpenCOLLADA-source

make -j 3
sudo make install
```

### Python wrapper 

For usage with FreeCAD you need the [Python](Python.md) wrapper which uses SWIG to generate the proper interfaces from the C++ classes.


```python
sudo apt-get install python-all-dev swig
```



### CMake configuración 

It is recommended to perform the configuration and compilation in a specific build directory separate from the source directory.


```python
mkdir -p IfcOpenShell-build
cd IfcOpenShell-build

cmake ../IfcOpenShell-source/cmake/
```

Notice that the `CMakeLists.txt` file that drives CMake is inside the `cmake/` subdirectory in the source directory.

Depending on your Linux distribution, and the way you installed the dependencies, you may have to define some CMake variables so that the libraries are found properly.



#### Especificación de las bibliotecas OpenCASCADE 

If you manually compiled OpenCASCADE, or if the libraries are not in a standard directory, you may have to set the proper variables.


```python
cmake \
    -DOCC_INCLUDE_DIR=/usr/include/opencascade \
    -DOCC_LIBRARY_DIR=/usr/lib/x86_64-linux-gnu \
    ../IfcOpenShell-source/cmake/
```

By default the build system expects the community edition (OCE) of OpenCASCADE (`/usr/include/oce/`), however, please notice that this version is old and no longer recommended by FreeCAD as of 2020. For this reason installing the development files of the main version of [OpenCASCADE](OpenCASCADE.md) (OCCT) is recommended.



#### Sin OpenCOLLADA 

If you don\'t need OpenCOLLADA support ([DAE](Arch_DAE.md) files) you need to turn it off explicitly with the `COLLADA_SUPPORT` variable.


```python
cmake \
    ...
    -DCOLLADA_SUPPORT=FALSE \
    ../IfcOpenShell-source/cmake/
```



#### Con OpenCOLLADA 

If you manually compiled OpenCOLLADA, or if the libraries are not in a standard directory, you may have to set the proper variables for OpenCOLLADA and for the `libpcre` library.


```python
cmake \
    ...
    -DOPENCOLLADA_INCLUDE_DIR=/usr/include/opencollada \
    -DOPENCOLLADA_LIBRARY_DIR=/usr/lib/opencollada \
    -DPCRE_LIBRARY_DIR=/usr/lib/x86_64-linux-gnu \
    ../IfcOpenShell-source/cmake/
```



#### Especificación de las bibliotecas libxml2 

If the `libxml2` libraries are not found during compilation and linking, or if the libraries are not in a standard directory, you may have to set the proper variables.


```python
cmake \
    ...
    -DLIBXML2_INCLUDE_DIR=/usr/include/libxml2 \
    -DLIBXML2_LIBRARIES=/usr/lib/x86_64-linux-gnu/libxml2.so \
    ../IfcOpenShell-source/cmake/
```



#### Especificando la instalación en el directorio personal del usuario 

By default, the Python module `ifcopenshell` will be installed in a system `site-packages/` directory, so it requires superuser privileges. By setting the `USERSPACE_PYTHON_PREFIX` variable, the installation of the Python module will be done to the user\'s home directory.


```python
cmake \
    ...
    -DUSERSPACE_PYTHON_PREFIX=ON \
    ../IfcOpenShell-source/cmake/
```



#### Especificando la versión de Python 

If you want to generate a binding for a particular Python version, set the `PYTHON_EXECUTABLE` variable to the specific executable. Remember that this version must be the same Python version against which FreeCAD was compiled. 
```python
cmake \
    ...
    -DPYTHON_EXECUTABLE=/usr/bin/python3.6 \
    ../IfcOpenShell-source/cmake/
```



#### Línea de configuración única 

In a typical Debian/Ubuntu system you may use this line to configure the compilation. Adjust it as necessary. 
```python
cmake -DOCC_INCLUDE_DIR=/usr/include/opencascade -DOCC_LIBRARY_DIR=/usr/lib/x86_64-linux-gnu -DLIBXML2_INCLUDE_DIR=/usr/include/libxml2 -DLIBXML2_LIBRARIES=/usr/lib/x86_64-linux-gnu/libxml2.so -DUSERSPACE_PYTHON_PREFIX=ON ../IfcOpenShell-source/cmake/
```

Without OpenCOLLADA: 
```python
cmake -DOCC_INCLUDE_DIR=/usr/include/opencascade -DOCC_LIBRARY_DIR=/usr/lib/x86_64-linux-gnu -DCOLLADA_SUPPORT=FALSE -DLIBXML2_INCLUDE_DIR=/usr/include/libxml2 -DLIBXML2_LIBRARIES=/usr/lib/x86_64-linux-gnu/libxml2.so -DUSERSPACE_PYTHON_PREFIX=ON ../IfcOpenShell-source/cmake/
```



### Compilación actual 

If there were no error messages during configuration with CMake, a `Makefile` should have been created in the build directory, so you can proceed to compile the libraries by running `make`. 
```python
make -j N
```


`N`

is the number of processors that you assign to the compilation process; choose at least one fewer than the total number of CPU cores that you have.



### Solución de problemas y otras opciones 

All configuration options are available in the `CMakeLists.txt` file located inside the `IfcOpenShell-source/cmake/` directory. If there are problems when running CMake or Make, look here for other options that may need to be set.

In all instructions above, instead of `cmake`, the graphical interface `cmake-gui` can be used. This will quickly show the available options in the configuration.


```python
cmake-gui ../IfcOpenShell-source/cmake/
```



### Probar la compilación en el directorio de construcción 

If the build was successful you should have an `examples/` subdirectory with the newly compiled `IfcOpenHouse` executable. Run this utility from the build directory to generate a sample IFC file. 
```python
example/IfcOpenHouse
```

The sample [IFC](Arch_IFC.md) file should appear in the build directory, and can be used as input to the also newly compiled `IfcConvert` executable. This utility takes as input an IFC file, and produces as output a different format including [OBJ](Arch_OBJ.md), [DAE](Arch_DAE.md) if OpenCOLLADA support was enabled, STEP, IGS, XML, [SVG](Draft_SVG.md), or another [IFC](Arch_IFC.md). 
```python
./IfcConvert IfcOpenHouse.ifc
```

If no output file is specified, by default it will create an [OBJ](Arch_OBJ.md) file and its accompanying material table (MTL).



### Instalación de las bibliotecas compiladas 

If the compilation doesn\'t report any errors, you may run `make install` to copy the headers, compiled libraries, and binaries to their corresponding installation directories.


```python
sudo make install
```

By default, the `CMAKE_INSTALL_PREFIX` is `/usr/local/`, so all compiled files will be placed under this directory, which normally requires elevated privileges. 
```python
/usr/local/bin/IfcConvert
/usr/local/bin/IfcGeomServer
/usr/local/include/ifcparse/*.h
/usr/local/include/ifcgeom/*.h
/usr/local/include/ifcgeom_schema_agnostic/*.h
/usr/local/include/serializers/{*.h,*.cpp}
/usr/local/include/serializers/schema_dependent/{*.h,*.cpp}
/usr/local/lib/libIfcGeom*.a
/usr/local/lib/libIfcParse.a
/usr/local/lib/libSerializers*.a
```

The `ifcopenshell` Python module that is required for FreeCAD is not actually present in the build directory; this package is created only when `make install` is run. The resulting package is placed in a `site-packages/` directory, or a `dist-packages/` directory for Debian/Ubuntu distributions. 
```python
/usr/lib/python3/dist-packages/ifcopenshell/
```

If the `USERSPACE_PYTHON_PREFIX` variable was set during the CMake configuration step, `ifcopenshell` will be placed in the user\'s `site-packages/` directory. 
```python
$HOME/.local/lib/python3.6/site-packages/ifcopenshell/
```



### Eliminar las bibliotecas compiladas 

To remove the installed libraries, just remove the corresponding files that were installed, and the `ifcopenshell/` directory with all modules inside. 
```python
sudo rm -rf /usr/local/bin/IfcConvert
sudo rm -rf /usr/local/bin/IfcGeomServer
sudo rm -rf /usr/local/include/ifcparse/
sudo rm -rf /usr/local/include/ifcgeom/
sudo rm -rf /usr/local/include/ifcgeom_schema_agnostic/
sudo rm -rf /usr/local/lib/libIfcGeom*
sudo rm -rf /usr/local/lib/libIfcParse*
sudo rm -rf /usr/local/lib/libSerializers*
```


```python
sudo rm -rf /usr/lib/python3/dist-packages/ifcopenshell/
```

Or if the `USERSPACE_PYTHON_PREFIX` variable was set. 
```python
sudo rm -rf $HOME/.local/lib/python3.6/site-packages/ifcopenshell/
```



### Instalación manual 

Compilation of the entire IfcOpenShell distribution produces binaries like `IfcConvert` and `IfcGeomServer`, as well as many static libraries (`lib*.a`) in the build directory. However, for FreeCAD we only need the `ifcopenshell` Python module. This module is not a single file, but a \"package\", that is, a directory with various files. This `ifcopenshell` package is put together from the Python wrappers built inside `IfcOpenShell-build/ifcwrap/`, and from the Python modules in the original source directory `IfcOpenShell-source/src/ifcopenshell-python/ifcopenshell/`.

-   Produced by the compilation process:


```python
../IfcOpenShell-build/ifcwrap/ifcopenshell_wrapper.py
../IfcOpenShell-build/ifcwrap/_ifcopenshell_wrapper.so
```

-   Existing in the source directory:


```python
../IfcOpenShell-source/src/ifcopenshell-python/ifcopenshell/
```

The `ifcopenshell` module is created by copying the original source directory, and adding the two `*ifcopenshell_wrapper*` files to it.


```python
cp -rt . ../IfcOpenShell-source/src/ifcopenshell-python/ifcopenshell/
cp -t ifcopenshell/ ifcwrap/ifcopenshell_wrapper.py ifcwrap/_ifcopenshell_wrapper.so
```

Now this directory can be moved to the user-specific or system `site-packages/` (`dist-packages/` for Debian/Ubuntu) to make it available for all Python applications. 
```python
mv -t $HOME/.local/lib/python3.6/site-packages/ ifcopenshell/
```

Or for system-wide installation: 
```python
sudo mv -t /usr/lib/python3/dist-packages/ ifcopenshell/
```

Now the `ifcopenshell` module should be available to be imported from a [Python console](Python_console.md). 
```python
>>> import ifcopenshell
>>> print(ifcopenshell.version)
0.6.0b0
>>> print(ifcopenshell.__path__)
['/home/user/.local/lib/python3.6/site-packages/ifcopenshell']
```



## Aplicación del visor IFC 

The IfcOpenShell library actually includes a small graphical viewer for IFC files that uses PyQt5 and PythonOCC.

To launch this viewer from the Python console, the `application` class needs to be instantiated and started: 
```python
from ifcopenshell.geom.app import application
application().start()
```

If the library is already installed, the entire module can also be run from the terminal: 
```python
python3 /home/user/.local/lib/python3.6/site-packages/ifcopenshell/geom/app.py
```

At the time of writing (2020), only the [PythonOCC](PythonOCC.md) version compiled for the [OpenCASCADE](OpenCASCADE.md) community edition (OCE) was supported.



## Visor en línea del IFC 

The IfcOpenShell project has also developed \"IFC Pipeline\", a self-hosted IFC processing and visualization program. It also provides a small web application that accepts file uploads, which anybody can use. This means that to visualize IFC data you don\'t need to have IfcOpenShell, or other viewers, installed locally; you can just load your IFC file into this system to see the result.

-   Online viewer: <https://view.ifcopenshell.org/>
-   Repository: [AECgeeks/ifc-pipeline](https://github.com/AECgeeks/ifc-pipeline)



## Más información 

-   Página web: [ifcopenshell.org](http://ifcopenshell.org/)
-   Repositorio de código: [IfcOpenShell/IfcOpenShell](https://github.com/IfcOpenShell/IfcOpenShell)
-   Academia con ejemplos y artículos: [academy.ifcopenshell.org](http://academy.ifcopenshell.org/)
-   [Visor en línea de IfcOpenShell](https://view.ifcopenshell.org/)
-   Comunidad OSArch con recursos para la arquitectura de código abierto: [wiki.OSArch.org](https://wiki.osarch.org/index.php?title=Main_Page)
-   [Instalación de IfcOpenShell](https://forum.freecadweb.org/viewtopic.php?f=39&t=48971); discusión principal en el foro.
-   [Instalación de IFC](https://forum.freecadweb.org/viewtopic.php?f=39&t=12368&start=10#p117883); discusión antigua en el foro.
-   [IfcPlusPlus compilado en Gentoo - ¿preguntas y alternativas?](https://forum.freecadweb.org/viewtopic.php?f=39&t=33254)
-   [Compilación de IfcOpenShell para MacOS](Import/Export_IFC_-_compiling_IfcOpenShell/es.md); una guía antigua que describe el proceso general. Puede que ya no sea necesaria ya que IfcOpenShell se distribuye ahora junto con FreeCAD gracias a [Conda](Conda/es.md).
-   Qué páginas enlazan con [esta página](Special:WhatLinksHere/IfcOpenShell/es.md).


 {{FEM_Tools_navi}}



---
⏵ [documentation index](../README.md) > [3rd_Party](Category_3rd_Party.md) > [BIM](Category_BIM.md) > [FEM](Category_FEM.md) > IfcOpenShell/es
