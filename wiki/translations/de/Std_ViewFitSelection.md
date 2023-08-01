---
- GuiCommand:
   Name:Std ViewFitSelection
   Name/de:Std AnsichtAuswahlEinpassen
   MenuLocation:Ansicht → Standardansichten → Auswahl einpassen
   Workbenches:Alle
   Shortcut:**V****S**
   SeeAlso:[Std AnsichtAllesEinpassen](Std_ViewFitAll/de.md)
---

# Std ViewFitSelection/de



## Beschreibung

Der Befehl **Std AnsichtAuswahlEinpassen** zoomt und schwenkt die Kamera, so dass alle ausgewählten Objekte in die aktive [3D-Ansicht](3D_view/de.md) passen. Dieser Befehl ist nützlich, falls sich Objekte außerhalb (der Ränder) der aktuellen 3D-Ansicht befinden oder sich nicht problemlos per [3D-Navigation](Mouse_navigation/de.md) finden lassen.



## Anwendung

1.  Ein oder mehrere Objekte auswählen.
2.  Es gibt mehrere Möglichkeiten, den Befehl aufzurufen:
    -   Die Schaltfläche **<img src="images/Std_ViewFitSelection.svg" width=16px> [Einpassen](Std_ViewFitSelection/de.md)** drücken.
    -   Den Menüeintrag **Ansicht → Standardansichten → <img src="images/Std_ViewFitSelection.png" width=16px> Einpassen** auswählen.
    -   Den Menüeintrag **<img src="images/Std_ViewFitSelection.svg" width=16px> Auswahl einpassen** aus dem Kontextmenü der [3D-Ansicht](3D_view/de.md) auswählen.
    -   Das Tastaturkürzel **V**, dann **S**.



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
![](images/Button_right.svg) [documentation index](../README.md) > Std ViewFitSelection/de
