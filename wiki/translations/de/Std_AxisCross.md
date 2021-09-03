---
- GuiCommand:/de
   Name:Std AxisCross
   Name/de:Std Achsenkreuz
   MenuLocation:Ansicht → Achsenkreuz ein-/ausblenden
   Workbenches:Alle
   Shortcut:**A** **C**
---

## Beschreibung

Der **Std AxisCross**-Befehl schaltet das Achsenkreuz in der aktiven [3D-Ansicht](3D_view/de.md) ein/aus.

Das Achsenkreuz besteht aus drei Pfeilen, die positiven X-, Y- und Z-Achsen des globalen Koordinatensystems darstellen. Ihr gemeinsamer Startpunkt ist der Ursprung des globalen Koordinatensystems.

![](images/Std_AxisCross_example.svg ) *Das Achsenkreuz (die Buchstaben sind nicht Teil des Achsenkreuzes)*

## Anwendung

1.  Es gibt mehrere Möglichkeiten, den Befehl aufzurufen:
    -   Wähle die Option {{MenuCommand|Ansicht → <img src="images/Std_AxisCross.svg" width=16px> Achsenkreuz ein/ausblenden}} aus dem Menü.
    -   Verwende das Tastaturkürzel: **A** dann **C**.

## Hinweise

-   FreeCAD kann einen kleineren Koordinatensystemindikator in der unteren rechten Ecke von 3D-Ansichten anzeigen: : {{MenuCommand|Bearbeiten → Einstellungen... → Anzeige → 3D Viewer → Koordinatensystem in Ecke anzeigen}}. Siehe [Voreinstellungseditor](Preferences_Editor/de#3D_View.md).
-   Der [Navigationswürfel](Navigation_Cube/de.md) enthält ebenfalls einen Koordinatensystemindikator.

## Einstellungen

-   Der Standard für das Achsenkreuz kann in den Einstellungen geändert werden: {{MenuCommand|Bearbeiten → Einstellungen... → Anzeige → 3D-Ansicht → Achsenkreuz standardmäßig anzeigen}}. Siehe [Voreinstellungseditor](https://wiki.freecadweb.org/Preferences_Editor/de#3D_Ansicht.md). {{Version/de|0.19}}

## Skripten


**Siehe auch:**

[FreeCAD Grundlagen Skripten](FreeCAD_Scripting_Basics/de.md).

Um die Ansicht des Achsenkreuzes umzuschalten, verwende die Methode `viewIsometric` des AktiveAnsicht Objekts. Diese Methode ist nicht verfügbar, wenn sich FreeCAD im Konsolenmodus befindet.


```python
import FreeCADGui

FreeCADGui.ActiveDocument.ActiveView.setAxisCross(True)
FreeCADGui.ActiveDocument.ActiveView.hasAxisCross()
```





{{Std Base navi

}}  
