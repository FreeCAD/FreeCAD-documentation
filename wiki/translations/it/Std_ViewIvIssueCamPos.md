# Std ViewIvIssueCamPos/it
---
- GuiCommand:/it   Name:Std ViewIvIssueCamPos   Name/it:Pubblica la posizione della camera   MenuLocation:Visualizza → Stereo → Pubblica la posizione della camera   Workbenches:Tutti   Shortcut:   SeeAlso:[Viste bloccate](Std_FreezeViews/it.md)---

## Descrizione


<div class="mw-translate-fuzzy">

Questo comando serve a conoscere i dati della posizione, dell\'orientamento e le altre informazioni sulla camera.

Esempio casuale dei dati di posizione della camera nel pannello Report:

![](images/CameraPosition1_it.png )


</div>


```python   OrthographicCamera {   viewportMapping ADJUST_CAMERA   position 57.73505 -57.73502 57.735027   orientation 0.74290609 0.30772209 0.59447283  1.2171158   nearDistance 81.588844   farDistance 109.60551   aspectRatio 1   focalDistance 100   height 100  } 
```


*Example output: camera settings after changing to [isometric view](Std_ViewIsometric.md) in a new document*

## Utilizzo

1.  Select the **View → Stereo → <img src="images/Std_ViewIvIssueCamPos.svg" width=16px> Issue camera position** option from the menu.

## Note

-   The camera settings can be used to add frozen views to a \*.cam file. See [Std FreezeViews](Std_FreezeViews.md).

## Script


**Vedere anche:**

[Script di base per FreeCAD](FreeCAD_Scripting_Basics/it.md)

The `getCamera` method of the ActiveView object returns the same camera settings in a single string. This method is not available if FreeCAD is in console mode.


```python
import FreeCADGui

FreeCADGui.ActiveDocument.ActiveView.getCamera()
```


<div class="mw-translate-fuzzy">





</div>


{{Std Base navi

}}

---
[documentation index](../README.md) > Std ViewIvIssueCamPos/it
