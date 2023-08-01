# PySide/it
{{docnav/it
|[Pivy](Pivy/it.md)
|[Creare l'interfaccia](Interface_creation/it.md)
}}




## Introduzione

La libreria [PySide](PySide/it.md) dà accesso al toolkit Qt dell\'interfaccia utente grafica multipiattaforma (GUI) di [Python](Python/it.md). Qt è una raccolta di librerie C++, ma con l\'aiuto di PySide, gli stessi componenti possono essere usati da [Python](Python/it.md). Ogni interfaccia grafica che può essere creata in C++, può anche essere creata e modificata in Python. Un vantaggio dell\'utilizzo di Python è che le interfacce Qt possono essere sviluppate e testate dal vivo, poiché non è necessario compilare i file sorgente.

Quando si installa FreeCAD, si dovrebbe ottenere sia Qt che PySide come parte del pacchetto. Se si sta [compilando](Compiling/it.md), si deve verificare che queste due librerie siano installate affinché FreeCAD funzioni correttamente. Naturalmente, PySide funzionerà solo se è presente Qt.

In passato, FreeCAD utilizzava PyQt, un\'altra associazione Qt per Python, ma nel 2013 ([commit 1dc122dc9a](https://github.com/FreeCAD/FreeCAD/commit/1dc122dc9a)) il progetto è migrato a PySide perché ha una [licenza](licence/it.md) più permissiva.

Per ulteriori informazioni, vedere:

-   [Wikipedia:PySide](https://it.wikipedia.org/wiki/PySide)
-   [Differenze tra PySide e PyQt](https://wiki.qt.io/Differences_Between_PySide_and_PyQt)

![](images/PySideScreenSnapshot1.jpg ) ![](images/PySideScreenSnapshot2.jpg ) 
*Esempi creati con PySide. A sinistra: una semplice finestra di dialogo. A destra: una finestra di dialogo più complessa con grafici.*

## PySide in FreeCAD con Qt5 

FreeCAD è stato sviluppato per essere utilizzato con Python 2 e Qt4. Poiché queste due librerie sono diventate obsolete, FreeCAD è passato a Python 3 e Qt5. Nella maggior parte dei casi questa transizione è stata eseguita senza la necessità di interrompere la compatibilità con le versioni precedenti.

Normalmente, il modulo `PySide` fornisce il supporto per Qt4, mentre `PySide2` fornisce il supporto per Qt5. Tuttavia, in FreeCAD non è necessario utilizzare `PySide2` direttamente, poiché è incluso uno speciale modulo `PySide` per gestire Qt5.

Questo modulo `PySide` si trova nella directory `Ext/` di un\'installazione di FreeCAD compilata per Qt5. 
```python
/usr/share/freecad/Ext/PySide
```

Questo modulo importa solo le classi necessarie da `PySide2` e le inserisce nel namespace `PySide`. Ciò significa che nella maggior parte dei casi lo stesso codice può essere utilizzato sia con Qt4 che con Qt5, purché utilizziamo il singolo modulo `PySide`. 
```python
PySide2.QtCore -> PySide.QtCore
PySide2.QtGui -> PySide.QtGui
PySide2.QtSvg -> PySide.QtSvg
PySide2.QtUiTools -> PySide.QtUiTools
```

L\'unico aspetto insolito è che le classi `PySide2.QtWidgets` sono posizionate nel namespace `PySide.QtGui`. 
```python
PySide2.QtWidgets.QCheckBox -> PySide.QtGui.QCheckBox
``` {{Top}}

## Esempi di utilizzo di PySide 

-   [Esempi di livello base di PySide](PySide_Beginner_Examples/it.md), Hello World, avvisi, inserire un testo, inserire un numero.
-   [Esempi di livello medio di PySide](PySide_Intermediate_Examples/it.md), dimensionare le finestre, nascondere i widget, i menu popup, la posizione del mouse, gli eventi del mouse.
-   [Esempi di livello avanzato di PySide](PySide_Advanced_Examples/it.md), widget etc.

Gli esempi di PySide sono divisi in 3 parti, differenziate per livello di esposizione a PySide, Python e alle parti incorporate in FreeCAD. La prima pagina contiene una panoramica e le basi della materia, fornisce una descrizione di PySide e di come è organizzato, mentre la seconda e la terza pagina contengono soprattutto degli esempi di codice di diversi livelli.

Si ritiene che questi esempi siano utili per iniziare, dopodiché l\'utente potrà consultare altre risorse online o la documentazione ufficiale. {{Top}}

## Documentazione

Ci sono alcune differenze nella gestione dei widget in Qt4 (PySide) e Qt5 (PySide2). Il programmatore dovrebbe essere consapevole di queste incompatibilità e dovrebbe consultare la documentazione ufficiale se qualcosa non sembra funzionare come previsto su una data piattaforma. Tuttavia, Qt4 è considerato obsoleto, quindi la maggior parte dello sviluppo dovrebbe mirare a Qt5 e Python 3.

La documentazione di PySide fa riferimento alle classi in stile Python; tuttavia, poiché Qt è originariamente una libreria C++, le stesse informazioni dovrebbero essere disponibili nel riferimento C++ corrispondente.

-   [Moduli Qt](https://doc.qt.io/qtforpython/modules.html) disponibile da PySide2 (Qt5).
-   [Tutte le classi Qt per modulo](https://doc.qt.io/qt-5/modules-cpp.html) in Qt5 per C++.
-   [Moduli Qt](https://deptinfo-ensip.univ-poitiers.fr/ENS/pyside-docs/index.html) disponibile da PySide (Qt4).


{{Top}}


{{docnav/it
|[Pivy](Pivy/it.md)
|[Creare l'interfaccia](Interface_creation/it.md)
}}



---
⏵ [documentation index](../README.md) > [Developer Documentation](Category_Developer Documentation.md) > [Python Code](Category_Python Code.md) > PySide/it
