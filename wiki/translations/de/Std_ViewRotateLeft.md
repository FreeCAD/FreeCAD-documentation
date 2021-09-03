---
- GuiCommand:/de
   Name:Std ViewRotateLeft
   Name/de:Std AnsichtLinksDrehen
   MenuLocation:Ansicht → Standardansichten → Links drehen
   Workbenches:Alle
   Shortcut:**Umschalten** + **Links**
   SeeAlso:[Std AnsichtRechtsDrehen](Std_ViewRotateRight/de.md)
---

## Beschreibung

Der Befehl **Std AnsichtLinksDrehen** dreht die Kamera in der aktiven [3D Ansicht](3D_view/de.md) um die Blickrichtung in 90-Grad Schritten nach links (entgegen dem Uhrzeigersinn).

## Anwendung

1.  Es gibt verschiedene Wege, den Befehl aufzurufen:
    -   Wähle die **Ansicht → Standardansichten → <img src="images/Std_ViewRotateLeft.svg" width=16px> Links drehen** Option aus dem Menü.
    -   Wähle die **Standardansichten → <img src="images/Std_ViewRotateLeft.svg" width=16px> Links drehen** Option aus dem Menü.
    -   Wähle die **Standardansichten → <img src="images/Std_ViewRotateLeft.svg" width=16px> Links drehen** aus dem [3D Ansicht](3D_view/de.md) Kontextmenü.
    -   Verwende den Tastenkürzel: **Umschalten**+**Links**.

## Skripten


**Siehe auch:**

[FreeCAD Grundlagen Skripten](FreeCAD_Scripting_Basics/de.md).

Um die Ansicht nach links zu drehen verwende die `viewRotateLinks` Methode des aktiven Ansichtobjekts. Diese Methode ist nicht verfügbar, wenn FreeCAD im Konsolenmodus ist.


```python
import FreeCADGui

FreeCADGui.ActiveDocument.ActiveView.viewRotateLeft()
FreeCADGui.ActiveDocument.ActiveView.getCameraOrientation()
```





{{Std Base navi

}}  
