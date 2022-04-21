---
- GuiCommand:/it
   Name:TechDraw_ActiveView
   Name/it:Vista attiva
   Icon:TechDraw_ActiveView.svg
   MenuLocation:TechDraw → Vista attiva
   Workbenches:[TechDraw](TechDraw_Workbench/it.md)
   SeeAlso:[Simbolo](TechDraw_Symbol/it.md)
   Version:0.19
---

# TechDraw ActiveView/it


</div>

## Descrizione

Lo strumento Vista attiva inserisce una copia di una finestra 3D in una pagina di disegno.

![](images/TechDraw_ActiveView_example.png ) 
*Una vista semplice dal modello 3D.*

## Utilizzo


<div class="mw-translate-fuzzy">

1.  Passare alla finestra 3D che si desidera copiare.
2.  Se nel documento sono presenti più pagine di disegno, è necessario selezionare nella struttura ad albero anche la pagina desiderata.
3.  Premere il pulsante **<img src="images/TechDraw_ActiveView.svg" width=16px> [Vista attiva](TechDraw_ActiveView/it.md)**.
4.  Si apre una finestra di dialogo che consente di specificare le dimensioni, il colore del bordo e dello sfondo della copia.


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

## Note


<div class="mw-translate-fuzzy">

-   Le viste attive sono statiche, una volta generate non vengono mai aggiornate con le modifiche al modello 3D.
-   Vista attiva in realtà è un <img alt="" src=images/TechDraw_Symbol.svg  style="width:24px;"> [Simbolo](TechDraw_Symbol/it.md). La sua proprietà **Scale Type** viene quindi sempre inizializzata come *Personalizzata*.
-   Questo strumento è ancora in qualche modo **sperimentale**.


</div>

## Proprietà


<div class="mw-translate-fuzzy">

Vedere <img alt="" src=images/TechDraw_Symbol.svg  style="width:16px;"> [Simbolo](TechDraw_Symbol/it.md)


</div>

## Script


<div class="mw-translate-fuzzy">


**Vedere anche:**

[TechDraw API](TechDraw_API/it.md) e [Nozioni di base sugli script di FreeCAD](FreeCAD_Scripting_Basics/it.md).


</div>


<div class="mw-translate-fuzzy">

Lo strumento Vista attiva può essere utilizzato nelle [macro](macros/it.md) e dalla console [Python](Python/it.md) utilizzando la seguente funzione:


</div>


```python
import TechDrawGui
TechDrawGui.copyActiveViewToSvgFile(Gui.ActiveDocument.ActiveView,"myFile.svg")
```


<div class="mw-translate-fuzzy">





</div>


{{TechDraw Tools navi

}}



---
![](images/Right_arrow.png) [documentation index](../README.md) > [TechDraw](TechDraw_Workbench.md) > TechDraw ActiveView/it
