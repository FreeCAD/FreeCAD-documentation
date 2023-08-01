---
- GuiCommand:/de
   Name:Std ViewRotateLeft
   Name/de:Std AnsichtNachLinksDrehen
   MenuLocation:Ansicht → Standardansichten → Nach links drehen
   Workbenches:Alle
   Shortcut:**Umschalten** + **Links**
   SeeAlso:[Std AnsichtNachRechtsDrehen](Std_ViewRotateRight/de.md)
---

# Std ViewRotateLeft/de

## Beschreibung

Der Befehl **Std AnsichtNachLinksDrehen** dreht die Kamera in der aktiven [3D-Ansicht](3D_view/de.md) in 90-Grad Schritten nach links (gegen den Uhrzeigersinn) um die Blickrichtung.

## Anwendung

1.  Es gibt mehrere Möglichkeiten den Befehl aufzurufen:
    -   Den Menüeintrag **Ansicht → Standardansichten → <img src="images/Std_ViewRotateLeft.svg" width=16px> Nach links drehen** auswählen.
    -   Die Option **Standardansichten → <img src="images/Std_ViewRotateLeft.svg" width=16px> Nach links drehen** aus dem Kontextmenü der [3D-Ansicht](3D_view/de.md) auswählen.
    -   Das Tastaturkürzel: **Shift**+**Links**.

## Skripten


**Siehe auch:**

[FreeCAD Grundlagen Skripten](FreeCAD_Scripting_Basics/de.md).

Um die Ansicht nach links zu drehen, wird die Methode `viewRotateLeft` des ActiveView-Objekts verwendet. Diese Methode ist nicht verfügbar, wenn sich FreeCAD im Konsolenmodus befindet.


```python
import FreeCADGui

FreeCADGui.ActiveDocument.ActiveView.viewRotateLeft()
FreeCADGui.ActiveDocument.ActiveView.getCameraOrientation()
```





{{Std Base navi

}}



---
![](images/Button_right.svg) [documentation index](../README.md) > Std ViewRotateLeft/de
