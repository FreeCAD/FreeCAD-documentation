---
- GuiCommand:/de
   Name:Std ViewFitSelection
   Name/de:Std ViewFitSelection
   MenuLocation:Ansicht → Standardansichten → Auswahl einpassen
   Workbenches:Alle
   Shortcut:**V****S**
   SeeAlso:[Std AnsichtAlleseinpassen](Std_ViewFitAll/de.md)
---

# Std ViewFitSelection/de

## Beschreibung

Der **Std AnsichtEinpassenAuswahl**-Befehl zoomt und schwenkt, so dass alle ausgewählten Objekte in die aktive [3D-Ansicht](3D_view/de.md) passen.

## Anwendung

1.  Wähle ein oder mehrere Objekte.
2.  Es gibt mehrere Wege, den Befehl aufzurufen:
    -   Drücke die **<img src="images/Std_ViewFitSelection.svg" width=16px> [Std AnsichtEinpassenAuswahl](Std_ViewFitSelection/de.md)**-Schaltfläche.
    -   Wähle die **Ansicht → Standardansichten → <img src="images/Std_ViewFitSelection.png" width=16px>-Option einpassen** aus dem Menü.
    -   Wähle die **<img src="images/Std_ViewFitSelection.svg" width=16px> Auswahl einpassen**-Option aus dem [3D-Ansicht](3D_view/de.md)-Kontextmenü.
    -   Benutze den Tastaturkurzbefehl **V**, dann **S**.

## Skripten


**Siehe auch:**

[FreeCAD Grundlagen Skripten](FreeCAD_Scripting_Basics/de.md).

Um die Ansicht in \'Auswahl einpassen\' zu ändern, kann die `SendMsgToActiveView`-Methode des FreeCADGui-Objekts benutzt werden. Diese Methode ist im FreeCAD-Konsolenmodus nicht verfügbar.


```python
import FreeCADGui

FreeCADGui.SendMsgToActiveView('ViewSelection')
```





{{Std Base navi

}}



---
![](images/Right_arrow.png) [documentation index](../README.md) > Std ViewFitSelection/de
