---
- GuiCommand:/de
   Icon:Zoom-out.svg
   Name/de:Std ViewZoomOut
   MenuLocation:Ansicht → Zoom‏‎ → Verkleinern
   Workbenches:Alle
   Shortcut:**Strg** + **-**
   SeeAlso:[Vergrößern](Std_ViewZoomIn/de.md), [Zoomen mit Rechteck](Std_ViewBoxZoom/de.md)
---

# Std ViewZoomOut/de

## Beschreibung

Der **Std Verkleinern**-Befehl verkleinert die Objekte in der aktiven [3D-Ansicht](3D_view.md).

## Anwendung

1.  Es gibt mehrere Möglichkeiten, den Befehl aufzurufen:
    -   Wähle die Option **Ansicht → Zoom‏‎ → <img src="images/Std_ViewZoomOut.svg" width=16px> Verkleinern** aus dem Menü
    -   Benutze den Tastaturkurzbefehl **Strg** + **-**.

## Hinweise

-   Die Ansicht kann auch mit dem Mausrad verkleinert werden.

## Einstellungen

-   Der Zoomfaktor kann in den Einstellungen geändert werden: **Bearbeiten → Einstellungen... → Anzeigen → Navigation → Zoom-Schritt**. Diese Einstellung beeinflusst auch den Mausrad-Zoom. Siehe [Voreinstellungseditor](Preferences_Editor/de#Navigation.md).

## Skripten


**Siehe auch:**

[FreeCAD Grundlagen Skripten](FreeCAD_Scripting_Basics/de.md).

Zum Verkleinern benutze die `zoomOut`-Methode des ActiveView-Objekts. Diese Methode gibt es im FreeCAD-Konsolenmodus nicht.


```python
import FreeCADGui

FreeCADGui.ActiveDocument.ActiveView.zoomOut()
```





{{Std Base navi

}}

---
[documentation index](../README.md) > Std ViewZoomOut/de
