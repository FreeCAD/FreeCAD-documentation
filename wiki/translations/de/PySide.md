# PySide/de
## Einführung

Die [PySide](PySide.md) Bibliothek ermöglicht den Zugriff auf das plattformübergreifende GUI Werkzeugsatz Qt von [Python](Python/de.md). Qt ist eine Sammlung von C++ Bibliotheken, aber mit Hilfe von PySide können die gleichen Komponenten von [Python](Python/de.md) aus verwendet werden. Jede grafische Oberfläche, die in C++ erstellt werden kann, kann auch in Python erstellt und modifiziert werden. Ein Vorteil der Verwendung von Python ist, dass Qt Oberflächen entwickelt und live getestet werden können, da wir die Quelldateien nicht kompilieren müssen.

Wenn du FreeCAD installierst, solltest du sowohl Qt als auch PySide als Teil des Pakets erhalten. Wenn du selbst [Kompilierst](Compiling/de.md), dann musst du überprüfen, ob diese beiden Bibliotheken installiert sind, damit FreeCAD korrekt läuft. Natürlich wird PySide nur funktionieren, wenn Qt vorhanden ist.

In der Vergangenheit benutzte FreeCAD PyQt, eine weitere Qt-Einbindung für Python, aber 2013 ([commit 1dc122dc9a](https://github.com/FreeCAD/FreeCAD/commit/1dc122dc9a)) migrierte das Projekt zu PySide, weil es eine umfassendere [Lizenz](License/de.md) hat.

Für weitere Informationen siehe:

-   [Wikipedia:PySide](https://en.wikipedia.org/wiki/PySide)
-   [Differences Between PySide and PyQt](https://wiki.qt.io/Differences_Between_PySide_and_PyQt)

![](images/PySideScreenSnapshot1.jpg ) ![](images/PySideScreenSnapshot2.jpg ) 
*Mit PySide erstellte Beispiele. Links: ein einfacher Dialog. Rechts: ein komplexerer Dialog mit Diagrammen.*



## PySide in FreeCAD mit Qt5 

FreeCAD wurde für die Verwendung mit Python 2 und Qt4 entwickelt. Als diese beiden Bibliotheken veraltet waren, wurde FreeCAD auf Python 3 und Qt5 umgestellt. In den meisten Fällen erfolgte dieser Übergang, ohne dass die Rückwärtskompatibilität unterbrochen werden musste.

Normalerweise bietet das `PySide` Modul Unterstützung für Qt4, während `PySide2` Unterstützung für Qt5 bietet. In FreeCAD ist es jedoch nicht notwendig, `PySide2` direkt zu verwenden, da ein spezielles `PySide` Modul enthalten ist, um Qt5 zu behandeln.

Dieses `PySide` Modul befindet sich im `Ext/` Verzeichnis einer für Qt5 kompilierten FreeCAD Installation. 
```python
/usr/share/freecad/Ext/PySide
```

Dieses Modul importiert einfach die erforderlichen Klassen aus `PySide2`, platziert sie aber im `PySide` Namensraum. Das bedeutet, dass in den meisten Fällen derselbe Code sowohl mit Qt4 als auch mit Qt5 verwendet werden kann, solange wir das einzelne `PySide` Modul verwenden. 
```python
PySide2.QtCore -> PySide.QtCore
PySide2.QtGui -> PySide.QtGui
PySide2.QtSvg -> PySide.QtSvg
PySide2.QtUiTools -> PySide.QtUiTools
```

Der einzige ungewöhnliche Aspekt ist, dass die `PySide2.QtWidgets` Klassen im `PySide.QtGui` Namensraum platziert werden. 
```python
PySide2.QtWidgets.QCheckBox -> PySide.QtGui.QCheckBox
```

## Beispiele für PySide Verwendung 

-   [PySide Anfänger Beispiele](PySide_Beginner_Examples/de.md), Hallo Welt, Ankündigungen, Text eingeben, Nummer eingeben.
-   [PySide Beispiele für Fortgeschrittene](PySide_Intermediate_Examples/de.md), Fenstergröße, Widgets ausblenden, Aufklappmenüs, Mausposition, Mausereignisse.
-   [PySide Zwischenbeispiele](PySide_Advanced_Examples/de.md), viele Widgets.

Die Beispiele von PySide sind in 3 Teile unterteilt, die sich nach dem Grad der Exposition gegenüber PySide, Python und den FreeCAD Interna unterscheiden. Die erste Seite gibt einen Überblick über PySide; die zweite und dritte Seite sind meist Code Beispiele auf verschiedenen Niveaus.

Es wird erwartet, dass diese Beispiele für den Anfang nützlich sind, und danach kann der Benutzer andere Ressourcen online oder die offizielle Dokumentation hinzuziehen. 

## Dokumentation

Es gibt einige Unterschiede in der Behandlung von Widgets in Qt4 (PySide) und Qt5 (PySide2). Der Programmierer sollte sich dieser Inkompatibilitäten bewusst sein und die offizielle Dokumentation konsultieren, wenn etwas auf einer bestimmten Plattform nicht wie erwartet zu funktionieren scheint. Nichtsdestotrotz wird Qt4 als veraltet angesehen, so dass die meiste Entwicklung auf Qt5 und Python 3 abzielen sollte.

Die PySide Dokumentation bezieht sich auf die Klassen im Python Stil; da Qt jedoch ursprünglich eine C++ Bibliothek ist, sollten dieselben Informationen auch in der entsprechenden C++ Referenz verfügbar sein.

-   [Qt Module](https://doc.qt.io/qtforpython/modules.html) verfügbar von PySide2 (Qt5).
-   [Alle Qt Klassen nach Modulen](https://doc.qt.io/qt-5/modules-cpp.html) in Qt5 für C++.
-   [Qt-Module](https://deptinfo-ensip.univ-poitiers.fr/ENS/pyside-docs/index.html) verfügbar von PySide (Qt4).


{{Top}}



---
⏵ [documentation index](../README.md) > [Developer Documentation](Category_Developer%20Documentation.md) > [Python Code](Category_Python%20Code.md) > PySide/de
