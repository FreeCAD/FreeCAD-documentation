# PySide/it
<div class="mw-translate-fuzzy">


{{docnav/it|[Pivy](Pivy/it.md)|[Ogetti FeaturePython](FeaturePython_Objects/it.md)}}


</div>


{{TOCright}}


<div class="mw-translate-fuzzy">

## PySide


</div>


<div class="mw-translate-fuzzy">

[PySide](http://en.wikipedia.org/wiki/PySide) è il legame tra Python e la multi-piattaforma GUI degli strumenti di Qt. FreeCAD usa PySide all\'interno di Python per tutti gli effetti GUI (Interfaccia grafica per l\'utente). PySide è una alternativa al pacchetto PyQt che è stato utilizzato in precedenza da FreeCAD per la sua GUI. PySide ha una licenza più permissiva. Per maggiori informazioni sulla differenza vedere [Differences Between PySide and PyQt](http://qt-project.org/wiki/Differences_Between_PySide_and_PyQt).


</div>

When you install FreeCAD, you should get both Qt and PySide as part of the package. If you are [compiling](Compiling.md) yourself then you must verify that these two libraries are installed in order for FreeCAD to run correctly. Of course, PySide will only work if Qt is present.

In the past, FreeCAD used PyQt, another Qt binding for Python, but in 2013 ([commit 1dc122dc9a](https://github.com/FreeCAD/FreeCAD/commit/1dc122dc9a)) the project migrated to PySide because it has a more permissible [license](licence.md).

For more information see:

-   [Wikipedia:PySide](https://en.wikipedia.org/wiki/PySide)
-   [Differences Between PySide and PyQt](https://wiki.qt.io/Differences_Between_PySide_and_PyQt)

![](images/PySideScreenSnapshot1.jpg ) ![](images/PySideScreenSnapshot2.jpg ) 
*Examples created with PySide. Left: a simple dialog. Right: a more complex dialog with graphs.*

## PySide in FreeCAD with Qt5 

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
``` {{Top}}

## Examples of PySide use 


<div class="mw-translate-fuzzy">

**Per acquisire familiarità con alcuni esempi reali di PySide**

-   [Esempi di livello base di PySide](PySide_Beginner_Examples/it.md) (Hello World, avvisi, inserire un testo, inserire un numero)
-   [Esempi di livello medio di PySide](PySide_Intermediate_Examples/it.md) (dimensionare le finestre, nascondere i widget, i menu popup, la posizione del mouse, gli eventi del mouse)
-   [Esempi di livello avanzato di PySide](PySide_Advanced_Examples/it.md) (widget etc.)


</div>


<div class="mw-translate-fuzzy">

Esse suddividono l\'argomento in 3 parti, e si differenziano per livello di esposizione per PySide, Python e le parti incorporate in FreeCAD. La prima pagina contiene una panoramica e le basi della materia, fornisce una descrizione di PySide e di come è organizzato, mentre la seconda e la terza pagina contengono soprattutto degli esempi di codice di diversi livelli.


</div>


<div class="mw-translate-fuzzy">

Con le pagine allegate si intende fornire del semplice codice Python per eseguire PySide, in modo che l\'utente possa facilmente copiarlo, incollarlo nel proprio lavoro, adattarlo se necessario, e risolvere i suoi problemi con FreeCAD. Sperando che non abbia bisogno di andare alla ricerca di risposte alle domande su PySide attraverso internet. Allo stesso tempo, queste pagine non vogliono sostituirsi ai vari tutorial completi e ai siti di riferimento a PySide presenti nel web.


</div>


{{Top}}

## Documentation

There are some differences in handling of widgets in Qt4 (PySide) and Qt5 (PySide2). The programmer should be aware of these incompatibilities, and should consult the official documentation if something doesn\'t seem to work as expected on a given platform. Nevertheless, Qt4 is considered obsolete, so most development should target Qt5 and Python 3.

The PySide documentation refers to the Python-style classes; however, since Qt is originally a C++ library, the same information should be available in the corresponding C++ reference.

-   [Qt Modules](https://doc.qt.io/qtforpython/modules.html) available from PySide2 (Qt5).
-   [All Qt classes by module](https://doc.qt.io/qt-5/modules-cpp.html) in Qt5 for C++.
-   [Qt Modules](https://deptinfo-ensip.univ-poitiers.fr/ENS/pyside-docs/index.html) available from PySide (Qt4).


{{Top}}


<div class="mw-translate-fuzzy">


{{docnav/it|[Pivy](Pivy/it.md)|[Ogetti FeaturePython](FeaturePython_Objects/it.md)}}


</div>


{{Powerdocnavi

}}

[<img src="images/Property.png" style="width:16px"> Developer Documentation](Category_Developer_Documentation.md) [<img src="images/Property.png" style="width:16px"> Python Code](Category_Python_Code.md)

---
[documentation index](../README.md) > [Developer Documentation](Category_Developer Documentation.md) > PySide/it
