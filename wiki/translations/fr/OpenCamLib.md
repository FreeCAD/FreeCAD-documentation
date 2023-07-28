# OpenCamLib/fr
{{TOCright}}

## Description

OpenCamLib (OCL) est une bibliothèque open source visant à fournir des algorithmes de fabrication assistée par ordinateur (FAO). FreeCAD utilise OCL dans les opérations expérimentales de **<img src="images/Path_Surface.svg" width=24px> [Surface](Path_Surface/fr.md)** et autres fonctionnalités expérimentales.

Github : <https://github.com/aewallin/opencamlib>

Site web : <http://www.anderswallin.net/CAM/>



## Installation

### Windows

**Remarque :** à partir de la version 0.19 de FreeCAD, OCL devrait être inclus avec tous les packages de distribution Windows.

Pour installer OCL sur Windows, suivez ces instructions.

1.  Déterminez la version Python d\'OpenCamLib (OCL).
    -   Construisez à partir du fichier [source](https://github.com/aewallin/opencamlib) en utilisant la version Python utilisée par votre version de FreeCAD. Le [fork du fichier source](https://github.com/peterlama/opencamlib) de Peter Lama contient des fichiers de projet pour une construction MSVC.
    -   Téléchargez Python 2.7 x86/x64 [binary](https://github.com/sgrogan/opencamlib/releases) par sgrogan sur GitHub.
    -   Téléchargez le Python 3.6 x64 [binary](https://github.com/sgrogan/opencamlib/releases) par sgrogan sur GitHub.
2.  Naviguez vers votre build OCL *ou* dossier des binaires
3.  Copier le fichier de la bibliothèque *ocl.pyd*.
4.  Choisissez l\'une des quatre (4) options suivantes :
    -   Accédez à votre dossier **FreeCAD\\lib** et collez-y le fichier **ocl.pyd**. {{ColoredText||red|(''Option à préférer.'')}}
    -   Accédez à votre dossier **FreeCAD\\bin** et collez-y le fichier **ocl.pyd**.
    -   Accédez à votre dossier **FreeCAD\\Mod**. Créez un nouveau dossier **OCL**. Entrez dans le dossier **OCL** et collez le fichier **ocl.pyd**.
    -   Accédez à votre dossier **%USERPROFILE%\\AppData\\Roaming\\FreeCAD**. Créez un nouveau dossier, **Mod**. Entrez dans le dossier **Mod**. Créez un nouveau dossier **OCL**. Entrez dans le dossier **OCL** et collez le fichier **ocl.pyd**. {{ColoredText||red|(''Option la moins préférée.'')}}
5.  Redémarrez FreeCAD
6.  Vérifier la bonne installation
    1.  Cliquez sur **Affichage** → **Panneaux** → **Console Python**.
    2.  Tapez \"**import ocl**\" dans la console Python et appuyez sur la touche **entrée**.
    3.  Si aucune erreur n\'apparaît, vous avez correctement installé OCL
        -   Si vous avez une erreur:
            -   Vérifiez l\'emplacement et le nom du fichier **ocl.pyd** comme indiqué ci-dessus
            -   Vérifiez le type d\'architecture correct de la bibliothèque OCL que vous avez installée - x86 ou x64
            -   Vérifiez que la version Python utilisée pour construire la bibliothèque OCL est la même que celle de votre logiciel FreeCAD - 2.7 ou 3.6 actuellement

### Linux

Le dépôt est [ici](https://github.com/aewallin/opencamlib) et contient des instructions d\'installation de base.

Avant de commencer l\'installation ou pendant le processus d\'installation, vous constaterez probablement que vous devez installer des packages supplémentaires :

#### Ubuntu/Debian

Par exemple : {{Code|lang=bash|code=
sudo apt install cmake
sudo apt install libboost-program-options-dev
# Optional, for documentation:
sudo apt-get install doxygen
sudo apt-get install texlive-full
}}

Remarque: \"libboost-program-options-dev\" peut être remplacé par \"libboost-all-dev\".

Si vous avez des difficultés, examinez attentivement tous les messages d\'erreur que vous obtenez pendant les phases de cmake et de make, car vous devrez peut-être installer des paquets supplémentaires.



#### Arch Linux 

1.  Installez OpenCamLib à partir du [package AUR](https://aur.archlinux.org/packages/opencamlib-git).
2.  Exécutez ensuite le code suivant dans la [console Python](Python_console/fr.md) de FreeCAD


{{Code|lang=bash|code=
import sys
sys.path.append('/usr/opencamlib/')
import ocl
}}

#### Python 3 

Identifiez la version de cmake que vous avez installée avec cmake --version

Pour cmake \>= 3.12, ajoutez ces drapeaux :


{{Code|lang=bash|code=
cmake -DBUILD_PY_LIB=ON -DUSE_PY_3=ON -DCMAKE_BUILD_TYPE=Release ../src -Wno-dev
}}

Pour cmake \< 3.12 (comme dans Ubuntu 18.04 qui a la 3.10), vous devez d\'abord modifier src/pythonlib/pythonlib.cmake et appliquer ce patch:

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

Ensuite, pour que Python 3 soit détecté correctement, vous devrez ajouter 2 autres drapeaux à la ligne cmake :


{{Code|lang=bash|code=
cmake -DBUILD_PY_LIB=ON -DUSE_PY_3=ON -DPYTHON_EXECUTABLE="$(which python3)" -DPYTHON_VERSION_SUFFIX=3 -DCMAKE_BUILD_TYPE=Release ../src -Wno-dev
}}

Voir le forum FreeCAD sur [Re: Comment activer openCamLib après l\'avoir compilé](https://forum.freecadweb.org/viewtopic.php?p=316970#p316988) et quelques posts suivants.

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

Pour tester la compilation, entrez ce qui suit dans la [console Python](Python_console/fr.md) :


```python
import area
import ocl
dir(ocl)
```

La valeur de retour doit être :


```python
['AdaptivePathDropCutter', 'AdaptivePathDropCutter_base', 'AdaptiveWaterline', 'AdaptiveWaterline_base', 'Arc', 'ArcSpanType', 'BallConeCutter', 'BallCutter', 'BatchDropCutter', 'BatchDropCutter_base', 'BatchPushCutter', 'BatchPushCutter_base', 'Bbox', 'BullConeCutter', 'BullCutter', 'CCPoint', 'CCType', 'CLPoint', 'CompBallCutter', 'CompCylCutter', 'ConeConeCutter', 'ConeCutter', 'CutterLocationSurface', 'CylConeCutter', 'CylCutter', 'Ellipse', 'EllipsePosition', 'Fiber', 'Fiber_base', 'Interval', 'Line', 'LineCLFilter', 'LineCLFilter_base', 'LineSpanType', 'MillingCutter', 'Path', 'PathDropCutter', 'PathDropCutter_base', 'Path_base', 'Point', 'STLReader', 'STLSurf', 'STLSurf_base', 'SpanType', 'Triangle', 'Triangle_base', 'Waterline', 'Waterline_base', 'WeaveVertexType', 'ZigZag', 'ZigZag_base', '__doc__', '__file__', '__loader__', '__name__', '__package__', '__spec__', 'eps', 'epsD', 'epsF', 'version']
```

En cas d\'erreur, la valeur de retour sera :


```python
['__doc__', '__file__', '__loader__', '__name__', '__package__', '__path__', '__spec__']
```

Pour cmake, l\'option Release est très importante, lorsque vous utilisez Debug area et ocl vont entrer en collision et l\'une ou l\'autre des bibliothèques ne sera pas chargée (en fonction de ce qui a été chargé en premier).



## Plus d\'aide 

Si vous rencontrez des difficultés, vous pouvez trouver de l\'aide supplémentaire sur ces messages du forum :

-   [Windows](https://forum.freecadweb.org/viewtopic.php?t=19205)
-   [Linux](https://forum.freecadweb.org/viewtopic.php?t=18017)



## Remerciements

Merci au [Dr. Anders Wallin](http://www.anderswallin.net/about/) d\'avoir fourni OCL au public.



---
![](images/Right_arrow.png) [documentation index](../README.md) > [User Documentation](Category_User Documentation.md) > [3rd Party](Category_3rd Party.md) > OpenCamLib/fr
