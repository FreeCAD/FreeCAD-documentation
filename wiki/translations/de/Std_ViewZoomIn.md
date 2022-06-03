---
- GuiCommand   */de
   Name/de   *Std ViewZoomIn
   MenuLocation   *Ansicht → Zoom‏‎ → Vergrößern
   Workbenches   *Alle
   Shortcut   ***Strg** + **+**
   SeeAlso   *[Szd Verkleinern](Std_ViewZoomOut/de.md), [Zoomen mit Rechteck](Std_ViewBoxZoom/de.md)
---

# Std ViewZoomIn/de

## Beschreibung

Der **Std Vergrößern**-Befehl vergrößert die Objekte in der aktiven [3D-Ansicht](3D_view.md).

## Anwendung

1.  Es gibt mehrere Möglichkeiten, den Befehl aufzurufen   *
    -   Wähle die Option **Ansicht → Zoom‏‎ → <img src="images/Std_ViewZoomIn.svg" width=16px> Vergrößern** aus dem Menü
    -   Benutze den Tastaturkurzbefehl **Strg** + **+**.

## Hinweise

-   Die Ansicht kann auch mit dem Mausrad vergrößert werden.

## Einstellungen

-   Der Zoomfaktor kann in den Einstellungen geändert werden   * **Bearbeiten → Einstellungen... → Anzeigen → Navigation → Zoom-Schritt**. Diese Einstellung beeinflusst auch den Mausrad-Zoom. Siehe [Voreinstellungseditor](Preferences_Editor/de#Navigation.md).

## Skripten


**Siehe auch   ***

[FreeCAD Grundlagen Skripten](FreeCAD_Scripting_Basics/de.md).

Zum Vergrößern benutze die `zoomIn`-Methode des ActiveView-Objekts. Diese Methode gibt es im FreeCAD-Konsolenmodus nicht.


```python
import FreeCADGui

FreeCADGui.ActiveDocument.ActiveView.zoomIn()
```





{{Std Base navi

}}



---
![](images/Right_arrow.png) [documentation index](../README.md) > Std ViewZoomIn/de
