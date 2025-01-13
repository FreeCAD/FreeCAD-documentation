---
 GuiCommand:
   Name: Std ViewRotateLeft
   Name/de: Std AnsichtNachLinksDrehen
   MenuLocation: Ansicht , Standardansichten , Nach links drehen
   Workbenches: Alle
   Shortcut: **Umschalten** + **Links**
   SeeAlso: Std_ViewRotateRight/de
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

Siehe auch: [Autogenerierte API-Dokumentation](https://freecad.github.io/SourceDoc/) und [Grundlagen der Skripterstellung in FreeCAD](FreeCAD_Scripting_Basics/de.md).

Die Methode `viewRotateLeft` des View-Objekts wird verwendet, um die Ansicht nach links zu drehen. Die Methode `viewRotateRight` steht ebenfalls zur Verfügung.


```python
import FreeCADGui

view = FreeCADGui.ActiveDocument.ActiveView
view.viewRotateLeft()
```





{{Std_Base_navi

}}



---
⏵ [documentation index](../README.md) > Std ViewRotateLeft/de
