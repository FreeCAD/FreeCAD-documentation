---
- GuiCommand   */it
   Name   *Std ViewZoomIn
   Name/it   *Ingrandisci
   MenuLocation   *Visualizza → Zoom‏‎ → Ingrandisci
   Workbenches   *Tutti
   Shortcut   ***Ctrl**+**+**
   SeeAlso   *[Riduci](Std_ViewZoomOut/it.md), [Finestra di ingrandimento](Std_ViewBoxZoom/it.md)
---

# Std ViewZoomIn/it

## Descrizione

Il comando **Std ViewZoomIn** ingrandisce la [vista 3D](3D_view/it.md) attiva.

## Utilizzo


<div class="mw-translate-fuzzy">

## Uso

-   Andare in **Visualizza → Zoom‏‎ → [<img src=images/Zoom-in.svg style="width   *16px"> Zoom In** o premere **Ctrl** + **+**.
-   La vista può anche essere ingrandita con la rotellina del mouse.


</div>

## Note

-   It is also possible to zoom with the mouse scroll wheel.

## Preferenze

-   The zoom factor can be changed in the preferences   * **Edit → Preferences... → Display → Navigation → Zoom step**. This setting also affects scroll wheel zoom. See [Preferences Editor](Preferences_Editor#Navigation.md).

## Script


**Vedere anche   ***

[Script di base per FreeCAD](FreeCAD_Scripting_Basics/it.md)

To zoom in use the `zoomIn` method of the ActiveView object. This method is not available if FreeCAD is in console mode.


```python
import FreeCADGui

FreeCADGui.ActiveDocument.ActiveView.zoomIn()
```


<div class="mw-translate-fuzzy">





</div>


{{Std Base navi

}}



---
![](images/Right_arrow.png) [documentation index](../README.md) > Std ViewZoomIn/it
