---
- GuiCommand:/de
   Name:Std ViewRotateRight
   Name/de:Std AnsichtNachRechtsDrehen
   MenuLocation:Ansicht → Standardansichten → Nach rechts drehen
   Shortcut:**Umschalten** + **Rechts**
   Workbenches:Alle
   SeeAlso:[Std AnsichtNachLinksDrehen](Std_ViewRotateLeft/de.md)
---

# Std ViewRotateRight/de

## Beschreibung

Der Befehl **Std AnsichtNachRechtsDrehen** dreht die Kamera in der aktiven [3D-Ansicht](3D_view/de.md) in 90°-Schritten nach rechts (im Uhrzeigersinn) um die Blickrichtung.

## Anwendung

1.  Es gibt mehrere Möglichkeiten den Befehl aufzurufen:
    -   Den Menüeintrag **Ansicht → Standardansichten → <img src="images/Std_ViewRotateRight.svg" width=16px> Nach rechts drehen** auswählen.
    -   Die Option **Standardansichten → <img src="images/Std_ViewRotateRight.svg" width=16px> Nach rechts drehen** aus dem Kontextmenü der [3D-Ansicht](3D_view/de.md) auswählen.
    -   Das Tastaturkürzel: **Shift**+**Rechts**.

## Skripten


**Siehe auch:**

[FreeCAD Grundlagen Skripten](FreeCAD_Scripting_Basics/de.md).

Um die Ansicht nach rechts zu drehen, wird die Methode `viewRotateRight` des ActiveView-Objekts verwendet. Diese Methode ist nicht verfügbar, wenn sich FreeCAD im Konsolenmodus befindet.


```python
import FreeCADGui

FreeCADGui.ActiveDocument.ActiveView.viewRotateRight()
FreeCADGui.ActiveDocument.ActiveView.getCameraOrientation()
```





{{Std Base navi

}}



---
![](images/Button_right.svg) [documentation index](../README.md) > Std ViewRotateRight/de
