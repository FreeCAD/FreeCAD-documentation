---
- GuiCommand:/de
   Name:TechDraw  ActiveView
   Name/de:TechDraw AktiveAnsicht
   MenuLocation:TechDraw → Aktive Ansicht einfügen (3D Ansicht)
   Workbenches:[TechDraw](TechDraw_Workbench/de.md)
   Version:0.19
   SeeAlso:[TechDraw Symbol](TechDraw_Symbol/de.md)
---

# TechDraw ActiveView/de

## Beschreibung

Das Werkzeug AktiveAnsicht fügt eine Kopie eines 3D Fensters in eine Zeichnungsseite ein.

![](images/TechDraw_ActiveView_example.png ) 
*Eine einfache Ansicht aus dem 3D Modell, die keine komplexen Berechnungen ausführt.*

## Anwendung


<div class="mw-translate-fuzzy">

1.  Gehe zu dem 3D Fenster, das du kopieren möchtest.
2.  Wenn du mehrere Zeichnungsseiten in deinem Dokument hast, musst du auch die gewünschte Seite im Baum auswählen.
3.  Drücke die **<img src="images/TechDraw_ActiveView.svg" width=16px> [Aktive Ansicht einfügen](TechDraw_ActiveView/de.md)** Schaltfläche
4.  Ein Dialogfeld wird geöffnet, in dem du die Größe, den Rahmen und die Hintergrundfarbe der Kopie festlegen kannst.


</div>

## Options

The following can be specified:

-    **Width**: The width of the generated view.

-    **Height**: The height of the generated view.

-    **Border**: The amount of empty space to be left around the view (but within Width x Height).

-    **Background**: If checked a background with the specified color is added.

-    **Line Width**: The thickness of the lines in the view.

-    **Render Mode**: The available modes are:

    -   
        {{Value|As is}}
        
        : Render primitives as they are.

    -   
        {{Value|Wireframe}}
        
        : Render polygons as wireframe.

    -   
        {{Value|Points}}
        
        : Render only the vertices of the polygons and lines.

    -   
        {{Value|Wireframe overlay}}
        
        : Render a wireframe overlay in addition to the {{Value|As is}} mode.

    -   
        {{Value|Hidden Line}}
        
        : As {{Value|Wireframe}}, but culls lines which would otherwise not be shown due to geometric culling.

    -   
        {{Value|Bounding box}}
        
        : Only show the bounding box of each object.

## Hinweise


<div class="mw-translate-fuzzy">

-   Aktive Ansichten sind nach der Erzeugung statisch, sie werden nie mit Änderungen am 3D Modell aktualisiert.
-   AktiveAnsicht hinter den Kulissen ist ein <img alt="" src=images/TechDraw_Symbol.svg  style="width:24px;"> [Symbolansicht](TechDraw_Symbol/de.md). Sein **Maßstabstyp** wird daher immer als *Angepasst* gekennzeichnet.

* Dieses Werkzeug ist noch etwas **experimentell**.


</div>

## Eigenschaften


<div class="mw-translate-fuzzy">

See <img alt="" src=images/TechDraw_Symbol.svg  style="width:16px;"> [Symbol](TechDraw_Symbol/de.md)


</div>

## Skripten


**Siehe auch:**

[TechDraw API](TechDraw_API/de.md) und [FreeCAD Grundlagen Skripten](FreeCAD_Scripting_Basics/de.md).

Das Werkzeug AktiveAnsicht kann in [Makros](Macros/de.md) und aus der [Python](Python/de.md) Konsole heraus mittels folgender Funktionen verwendet werden:


```python
import TechDrawGui
TechDrawGui.copyActiveViewToSvgFile(Gui.ActiveDocument.ActiveView,"myFile.svg")
```





{{TechDraw Tools navi

}}



---
![](images/Right_arrow.png) [documentation index](../README.md) > [TechDraw](TechDraw_Workbench.md) > TechDraw ActiveView/de
