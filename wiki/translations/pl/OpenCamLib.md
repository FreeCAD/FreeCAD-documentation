# OpenCamLib/pl
## Opis

OpenCamLib *(OCL)* to biblioteka open source, której celem jest dostarczanie algorytmów komputerowego wspomagania wytwarzania *(CAM)*. FreeCAD wykorzystuje OCL w eksperymentalnie w narzędziu **<img src="images/Path_Surface.svg" width=24px> [Powierzchnia 3D](Path_Surface/pl.md)** i innych funkcjach.

GitHub: <https://github.com/aewallin/opencamlib>

Strona domowa: <http://www.anderswallin.net/CAM/>



## Instalacja



### Windows

**Uwaga:** Począwszy od FreeCAD w wersji 0.19, OCL powinien być dołączony do wszystkich pakietów dystrybucyjnych Windows.

Aby zainstalować OCL w systemie Windows, postępuj zgodnie z poniższymi instrukcjami.

1.  Uzyskaj wersję Python OpenCamLib (OCL).
    -   Zbuduj ze źródła [1](https://github.com/aewallin/opencamlib) używając wersji Python używanej przez twoją wersję FreeCAD. Źródło Petera Lamy [fork of the same](https://github.com/peterlama/opencamlib) zawiera pliki projektu dla kompilacji MSVC.
    -   Pobierz Python 2.7 x86/x64 [binary](https://github.com/sgrogan/opencamlib/releases) przez sgrogan na GitHub.
    -   Pobierz Python 3.6 x64 [binarny](https://github.com/sgrogan/opencamlib/releases) przez sgrogan na GitHub.
2.  Przejdź do folderu binarnego \"or\" kompilacji OCL.
3.  Skopiuj plik biblioteki **ocl.pyd**.
4.  Postępuj zgodnie z jedną z następujących czterech(4) opcji:
    -   Przejdź do folderu **FreeCAD\\lib** i wklej tam plik **ocl.pyd**, {{ColoredText||red||(''To jest preferowana opcja'')}},
    -   Przejdź do folderu **FreeCAD\\bin** i wklej tam plik **ocl.pyd**,
    -   Przejdź do folderu **FreeCAD\\Mod**. Utwórz nowy folder **OCL**. Wejdź do folderu **OCL** i wklej plik **ocl.pyd**,
    -   Przejdź do folderu *%USERPROFILE%\\AppData\\Roaming\\FreeCAD*. Utwórz nowy folder **Mod**. Wejdź do folderu \"Mod\". Utwórz nowy folder \"OCL\". Wejdź do folderu **OCL** i wklej plik **ocl.pyd**. {{ColoredText||red|''(To jest najmniej preferowana opcja)''}}
5.  Uruchom ponownie FreeCAD.
6.  Zweryfikuj poprawność instalacji.
    1.  Kliknij **Widok → Panele → Konsola Python**.
    2.  Wpisz \"**import ocl**\' w konsoli Python i naciśnij klawisz **enter**.
    3.  Jeśli nie pojawi się żaden błąd, OCL został poprawnie zainstalowany
        -   Jeśli pojawi się błąd:
            -   Sprawdź umiejscowienie i nazwę pliku **ocl.pyd** zgodnie z powyższą instrukcją,
            -   Sprawdź poprawność typu architektury zainstalowanej biblioteki OCL - x86 lub x64,
            -   Sprawdź, czy wersja Pythona użyta do zbudowania biblioteki OCL jest taka sama jak wersja oprogramowania FreeCAD - 2.7 lub 3.6.



### Linux

Repozytorium znajduje się [w serwisie GitHub](https://github.com/aewallin/opencamlib) i zawiera podstawowe instrukcje instalacji.

Przed rozpoczęciem instalacji lub w jej trakcie, prawdopodobnie konieczne będzie zainstalowanie dodatkowych pakietów:



#### Debian/Ubuntu

Dla przykładu: {{Code|lang=bash|code=
sudo apt install cmake
sudo apt install libboost-program-options-dev
# Optional, for documentation:
sudo apt-get install doxygen
sudo apt-get install texlive-full
}}

Uwaga: \"libboost-program-options-dev\" może być zastąpione przez \"libboost-all-dev\".

Jeśli masz trudności, dokładnie przejrzyj wszystkie komunikaty o błędach, które otrzymujesz podczas faz `cmake` i `make`, ponieważ może być konieczne zainstalowanie dodatkowych pakietów.



#### Arch Linux 

1.  Zainstaluj OpenCamLib z pakietu [AUR](https://aur.archlinux.org/packages/opencamlib-git).
2.  Następnie uruchom następujący fragment kodu w [konsoli Python](Python_console/pl.md) programu FreeCAD.


{{Code|lang=bash|code=
import sys
sys.path.append('/usr/opencamlib/')
import ocl
}}



#### Python 3 

Zidentyfikuj zainstalowaną wersję cmake za pomocą instrukcji cmake --version

Dla wersji cmake \>= 3.12 należy dodać te flagi:


{{Code|lang=bash|code=
cmake -DBUILD_PY_LIB=ON -DUSE_PY_3=ON -DCMAKE_BUILD_TYPE=Release ../src -Wno-dev
}}

Dla wersji cmake \< 3.12 *(jak w Ubuntu 18.04, który ma 3.10)*, najpierw musisz edytować src/pythonlib/pythonlib.cmake i zastosować tę poprawkę:

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

Następnie, aby Python 3 był poprawnie wykrywany, należy dodać 2 dodatkowe flagi do linii cmake:


{{Code|lang=bash|code=
cmake -DBUILD_PY_LIB=ON -DUSE_PY_3=ON -DPYTHON_EXECUTABLE="$(which python3)" -DPYTHON_VERSION_SUFFIX=3 -DCMAKE_BUILD_TYPE=Release ../src -Wno-dev
}}

Zobacz forum FreeCAD pod adresem [Re: Jak aktywować openCamLib po kompilacji](https://forum.freecadweb.org/viewtopic.php?p=316970#p316988) i kilka postów po nim.



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

Aby przetestować kompilację, wprowadź następujące polecenie w [konsoli Python](Python_console/pl.md):


```python
import area
import ocl
dir(ocl)
```

Wartością zwracaną powinna być:


```python
['AdaptivePathDropCutter', 'AdaptivePathDropCutter_base', 'AdaptiveWaterline', 'AdaptiveWaterline_base', 'Arc', 'ArcSpanType', 'BallConeCutter', 'BallCutter', 'BatchDropCutter', 'BatchDropCutter_base', 'BatchPushCutter', 'BatchPushCutter_base', 'Bbox', 'BullConeCutter', 'BullCutter', 'CCPoint', 'CCType', 'CLPoint', 'CompBallCutter', 'CompCylCutter', 'ConeConeCutter', 'ConeCutter', 'CutterLocationSurface', 'CylConeCutter', 'CylCutter', 'Ellipse', 'EllipsePosition', 'Fiber', 'Fiber_base', 'Interval', 'Line', 'LineCLFilter', 'LineCLFilter_base', 'LineSpanType', 'MillingCutter', 'Path', 'PathDropCutter', 'PathDropCutter_base', 'Path_base', 'Point', 'STLReader', 'STLSurf', 'STLSurf_base', 'SpanType', 'Triangle', 'Triangle_base', 'Waterline', 'Waterline_base', 'WeaveVertexType', 'ZigZag', 'ZigZag_base', '__doc__', '__file__', '__loader__', '__name__', '__package__', '__spec__', 'eps', 'epsD', 'epsF', 'version']
```

W przypadku błędu, zwracaną wartością będzie:


```python
['__doc__', '__file__', '__loader__', '__name__', '__package__', '__path__', '__spec__']
```

Dla cmake opcja Release jest bardzo ważna, gdy używasz Debug area i ocl będą kolidować i jedna z bibliotek nie zostanie załadowana *(w zależności od tego, co zostało załadowane jako pierwsze)*.



## Więcej pomocy 

Jeśli napotkasz trudności, możesz znaleźć dodatkową pomoc w tych postach na forum:

-   [Linux](https://forum.freecadweb.org/viewtopic.php?t=18017)
-   [Windows](https://forum.freecadweb.org/viewtopic.php?t=19205)



## Podziękowania

Dziękujemy [Dr Anders Wallin](http://www.anderswallin.net/about/) za udostępnienie OCL do życia publicznego.



---
⏵ [documentation index](../README.md) > [User Documentation](Category_User Documentation.md) > [3rd Party](Category_3rd Party.md) > OpenCamLib/pl
