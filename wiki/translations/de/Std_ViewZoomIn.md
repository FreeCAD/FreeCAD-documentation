---
 GuiCommand:
   Name/de: Std ViewZoomIn
   MenuLocation: Ansicht , Zoom‏‎ , Vergrößern
   Workbenches: Alle
   Shortcut: **Strg** + **+**
   SeeAlso: Std_ViewZoomOut/de, Std_ViewBoxZoom/de
---

# Std ViewZoomIn/de



## Beschreibung

Der **Std Vergrößern**-Befehl vergrößert die Objekte in der aktiven [3D-Ansicht](3D_view.md).



## Anwendung

1.  Es gibt mehrere Möglichkeiten, den Befehl aufzurufen:
    -   Wähle die Option **Ansicht → Zoom‏‎ → <img src="images/Std_ViewZoomIn.svg" width=16px> Vergrößern** aus dem Menü
    -   Benutze den Tastaturkurzbefehl **Strg** + **+**.



## Hinweise

-   In fast allen Stilen der [Mausnavigation](Mouse_navigation/de.md) ist es auch möglich, durch Drehen am Mausrad die Ansicht zu skalieren (zoom).



## Einstellungen

Siehe auch: [Voreinstellungseditor](Preferences_Editor/de.md).

-   Der Zoomfaktor kann geändert werden: **Bearbeiten → Einstellungen... → Anzeigen → Navigation → Zoom-Schritt**. Diese Einstellung beeinflusst auch den Mausrad-Zoom.



## Skripten

Siehe auch: [Autogenerierte API-Dokumentation](https://freecad.github.io/SourceDoc/) und [Grundlagen der Skripterstellung in FreeCAD](FreeCAD_Scripting_Basics/de.md).

Die Methode `zoomIn` des View-Objekts wird zum Vergrößern verwendet. Die Methode `zoomOut` steht auch zur Verfügung.


```python
import FreeCADGui

view = FreeCADGui.ActiveDocument.ActiveView
view.zoomIn()
```



---
⏵ [documentation index](../README.md) > Std ViewZoomIn/de
