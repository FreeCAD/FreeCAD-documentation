---
- GuiCommand:/it
   Name:Std ViewZoomOut
   Name/it:Riduci
   MenuLocation:Visualizza → Zoom → Riduci
   Workbenches:Tutti
   Shortcut:**Ctrl**+**-**
   SeeAlso:[Ingrandisci](Std_ViewZoomIn/it.md), [Finestra di ingrandimento](Std_ViewBoxZoom/it.md)
---

## Descrizione

Il comando **Std ViewZoomOut** riduce la [vista 3D](3D_view/it.md) attiva.

## Utilizzo


<div class="mw-translate-fuzzy">

## Uso

-   Andare in **Visualizza → Zoom‏‎ → <img src=images/Zoom-out.svg style="width:24px"> Zoom Out** o premere **Ctrl** + **-**.
-   La vista può anche essere rimpicciolita con la rotellina del mouse.


</div>

## Note

-   It is also possible to zoom with the mouse scroll wheel.

## Preferenze

-   The zoom factor can be changed in the preferences: **Edit → Preferences... → Display → Navigation → Zoom step**. This setting also affects scroll wheel zoom. See [Preferences Editor](Preferences_Editor#Navigation.md).

## Script


**Vedere anche:**

[Script di base per FreeCAD](FreeCAD_Scripting_Basics/it.md)

To zoom out use the `zoomOut` method of the ActiveView object. This method is not available if FreeCAD is in console mode.


```python
import FreeCADGui

FreeCADGui.ActiveDocument.ActiveView.zoomOut()
```


<div class="mw-translate-fuzzy">





</div>


{{Std Base navi

}}  
