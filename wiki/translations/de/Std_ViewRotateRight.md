---
- GuiCommand:/de
   Name:Std ViewRotateRight
   Name/de:Std_DrehenRechts
   MenuLocation:{{StdMenu|[Ansicht](Std_View_Menu/de.md)}}→ Standardansichten → Rechtsherum rotieren
   Shortcut:**Umschalten** + **Rechts**
   Workbenches:Alle
   SeeAlso:[Std AnsichtLinksDrehen](Std_ViewRotateLeft/de.md)
---

# Std ViewRotateRight/de

## Beschreibung

Der **Std AnsichtRechtsDrehen** Befehl dreht die Kamera in die aktive [3D Ansicht](3D_view.md) um die Ansichtsrichtung in 90-Grad Schritten nach rechts (im Uhrzeigersinn).

## Anwendung

1.  Es gibt verschiedene Wege, den Befehl umzusetzen:
    -   Wähle die **Ansicht → Standardansichten → <img src="images/Std_ViewRotateRight.svg" width=16px> Rechts drehen** Option aus dem Menü.
    -   Wähle die **Standardansichten → <img src="images/Std_ViewRotateRight.svg" width=16px> Rechts drehen** aus dem Menü.
    -   Wähle die **Standardansichten → <img src="images/Std_ViewRotateRight.svg" width=16px> Rechts drehen** aus dem [3D Ansicht](3D_view/de.md) Kontextmenü.
    -   Verwende das Tastaturkürzel: **Shift**+**Rechts**.

## Skripten


**Siehe auch:**

[FreeCAD Grundlagen Skripten](FreeCAD_Scripting_Basics/de.md).

Um die Ansicht nach rechts zu drehen verwende die `viewRotateRight` Methode des aktiven Ansichtobjekts. Diese Methode ist nicht verfügbar, wenn FreeCAD im Konsolenmodus nicht.


```python
import FreeCADGui

FreeCADGui.ActiveDocument.ActiveView.viewRotateRight()
FreeCADGui.ActiveDocument.ActiveView.getCameraOrientation()
```





{{Std Base navi

}}



---
![](images/Right_arrow.png) [documentation index](../README.md) > Std ViewRotateRight/de
