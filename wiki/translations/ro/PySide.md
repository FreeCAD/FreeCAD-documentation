


{{TOCright}}


<div class="mw-translate-fuzzy">


<H2>

PySide


</H2>


</div>


<div class="mw-translate-fuzzy">

[PySide](http://en.wikipedia.org/wiki/PySide) este un instrument Python multiplatformă obligatoriu pentru a crea GUI în QT. FreeCAD utilizează PySide pentru toate GUI (Graphic User Interface) în interiorul Python. PySide este o alternativă la pachetul PyQt folosit anterior de FreeCAD pentru GUI. PySide are o licență mai permisivă. A se vedea [Differences Between PySide and PyQt](http://qt-project.org/wiki/Differences_Between_PySide_and_PyQt) for more information on the differences.


</div>

When you install FreeCAD, you should get both Qt and PySide as part of the package. If you are [compiling](Compiling.md) yourself then you must verify that these two libraries are installed in order for FreeCAD to run correctly. Of course, PySide will only work if Qt is present.

In the past, FreeCAD used PyQt, another Qt binding for Python, but in 2013 ([1dc122dc9a](https://github.com/FreeCAD/FreeCAD/commit/1dc122dc9a)) the project migrated to PySide because it has a more permissible [license](licence.md).

For more information see:

-   [Wikipedia:PySide](http://en.wikipedia.org/wiki/PySide)
-   [Differences Between PySide and PyQt](http://qt-project.org/wiki/Differences_Between_PySide_and_PyQt)

![](images/PySideScreenSnapshot1.jpg ) ![](images/PySideScreenSnapshot2.jpg ) *Examples created with PySide. Left: a simple dialog. Right: a more complex dialog with graphs.*

## PySide in FreeCAD with Qt5 {#pyside_in_freecad_with_qt5}

FreeCAD was developed to be used with Python 2 and Qt4. As these two libraries became obsolete, FreeCAD transitioned to Python 3 and Qt5. In most cases this transition was done without needing to break backwards compatibility.

Normally, the `PySide` module provides support for Qt4, while `PySide2` provides support for Qt5. However, in FreeCAD there is no need to use `PySide2` directly, as a special `PySide` module is included to handle Qt5.

This `PySide` module is located in the `Ext/` directory of an installation of FreeCAD compiled for Qt5. 
```python
/usr/share/freecad/Ext/PySide
```

This module just imports the necessary classes from `PySide2`, and places them in the `PySide` namespace. This means that in most cases the same code can be used with both Qt4 and Qt5, as long as we use the single `PySide` module. 
```python
PySide2.QtCore -> PySide.QtCore
PySide2.QtGui -> PySide.QtGui
PySide2.QtSvg -> PySide.QtSvg
PySide2.QtUiTools -> PySide.QtUiTools
```

The only unusual aspect is that the `PySide2.QtWidgets` classes are placed in the `PySide.QtGui` namespace. 
```python
PySide2.QtWidgets.QCheckBox -> PySide.QtGui.QCheckBox
```

[top](#top.md)

## Examples of PySide use {#examples_of_pyside_use}


<div class="mw-translate-fuzzy">

-   [Beginner PySide Examples](PySide_Beginner_Examples.md) (Hello World, anunțuri, introducerea textului, intgroducerea numerului)
-   [Medium PySide Examples](PySide_Medium_Examples.md) (mărimea ferestrei, ascunderea widgets, meniuri popup, poziția mouse , evenimentele mouse-ului)
-   [Advanced PySide Examples](PySide_Advanced_Examples.md) (widgets etc.)


</div>


<div class="mw-translate-fuzzy">

Acestea împart subiectul în 3 părți, diferențiate după nivelul de cunoaștere a PySide, Python și FreeCAD. Prima pagină are o imagine de ansamblu și un material de referință care oferă o descriere a PySide și modul în care sunt setate împreună, în timp ce a doua și a treia pagină sunt în mare parte exemple de cod la diferite niveluri.


</div>


<div class="mw-translate-fuzzy">

Intenția este ca paginile asociate să furnizeze un cod Python simplu pentru a rula PySide, astfel încât utilizatorul care lucrează la o problemă să poată copia cu ușurință codul, să-l lipsească în munca proprie, să-l adapteze după cum este necesar și să se întoarcă la rezolvarea problemelor cu FreeCAD. Sperăm că nu trebuie să meargă pe Internet în căutarea răspunsurilor la problemele PySide. În același timp, această pagină nu are intenția de a înlocui diferitele tutoriale și site-uri de referință PySide disponibile pe web.


</div>

[top](#top.md)

## Documentation

There are some differences in handling of widgets in Qt4 (PySide) and Qt5 (PySide2). The programmer should be aware of these incompatibilities, and should consult the official documentation if something doesn\'t seem to work as expected on a given platform. Nevertheless, Qt4 is considered obsolete, so most development should target Qt5 and Python 3.

The PySide documentation refers to the Python-style classes; however, since Qt is originally a C++ library, the same information should be available in the corresponding C++ reference.

-   [Qt Modules](https://doc.qt.io/qtforpython/modules.html) available from PySide2 (Qt5).
-   [All Qt classes by module](https://doc.qt.io/qt-5/modules-cpp.html) in Qt5 for C++.
-   [Qt Modules](https://deptinfo-ensip.univ-poitiers.fr/ENS/pyside-docs/index.html) available from PySide (Qt4).

[top](#top.md)


{{Powerdocnavi

}} 

[Category:Developer Documentation{{\#translation:}}](Category:Developer_Documentation.md) [Category:Python Code{{\#translation:}}](Category:Python_Code.md)
