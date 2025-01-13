---
 GuiCommand:
   Name: Std AxisCross
   Name/de: Std Achsenkreuz
   MenuLocation: Ansicht , Achsenkreuz ein-/ausblenden
   Workbenches: Alle
   Shortcut: **A** **C**
---

# Std AxisCross/de



## Beschreibung

Der **Std AxisCross**-Befehl schaltet das Achsenkreuz in der aktiven [3D-Ansicht](3D_view/de.md) ein/aus.

Das Achsenkreuz besteht aus drei Pfeilen, die positiven X-, Y- und Z-Achsen des globalen Koordinatensystems darstellen. Ihr gemeinsamer Startpunkt ist der Ursprung des globalen Koordinatensystems.

![](images/Std_AxisCross_example.svg ) 
*Das Achsenkreuz (die Buchstaben sind nicht Teil des Achsenkreuzes)*



## Anwendung

1.  Es gibt mehrere Möglichkeiten, den Befehl aufzurufen:
    -   Wähle die Option **Ansicht → <img src="images/Std_AxisCross.svg" width=16px> Achsenkreuz ein/ausblenden** aus dem Menü.
    -   Verwende das Tastaturkürzel: **A** dann **C**.



## Hinweise

-   FreeCAD kann einen kleineren Koordinatensystemindikator in der unteren rechten Ecke von 3D-Ansichten anzeigen: : **Bearbeiten → Einstellungen... → Anzeige → 3D Viewer → Koordinatensystem in Ecke anzeigen**. Siehe [Voreinstellungseditor](Preferences_Editor/de#3D_View.md).
-   Der [Navigationswürfel](Navigation_Cube/de.md) enthält ebenfalls einen Koordinatensystemindikator.



## Einstellungen

Siehe auch: [Voreinstellungseditor](Preferences_Editor/de.md).

-   Die Standardeinstellung für das Achsenkreuz kann geändert werden: **Bearbeiten → Einstellungen... → Anzeige → 3D-Ansicht → Achsenkreuz standardmäßig anzeigen**.



## Skripten

Siehe auch: [Autogenerierte API-Dokumentation](https://freecad.github.io/SourceDoc/) und [Grundlagen der Skripterstellung in FreeCAD](FreeCAD_Scripting_Basics/de.md).

Die Methode `setAxisCross` des View-Objekts wird verwendet, um das Achsenkreuz ein- bzw. auszuschalten.


```python
import FreeCADGui

view = FreeCADGui.ActiveDocument.ActiveView
view.setAxisCross(True)
view.hasAxisCross()
```





{{Std_Base_navi

}}



---
⏵ [documentation index](../README.md) > Std AxisCross/de
