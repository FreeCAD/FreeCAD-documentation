---
- GuiCommand:/it
   Name:TechDraw Midpoints
   Name/it:Punti mediani
   MenuLocation:TechDraw → Aggiungi vertici → Punti mediani
   Workbenches:[TechDraw](TechDraw_Workbench/it.md)
   SeeAlso:[Vertice cosmetico](TechDraw_CosmeticVertex/it.md), [Quadrante](TechDraw_Quadrants/it.md)
   Version:0.19
---

# TechDraw Midpoints/it


</div>

## Descrizione

Lo strumento Punti mediani aggiunge dei [vertici](Glossary#V.md) cosmetici nei punti medi di uno o più bordi.

<img alt="" src=images/TechDraw_CosmeticMidpoint_Sample.png  style="width:250px;"> 
*Vertici cosmetici nei punti mediani dei bordi*

## Utilizzo

1.  Selezionare uno o più bordi in una vista.
2.  Premere il pulsante **<img src="images/TechDraw_Midpoints.svg" width=16px> Punti mediani
**
3.  I vertici cosmetici vengono aggiunti nei punti medi dei bordi.

Per eliminare un punto mediano, selezionarlo e utilizzare il pulsante della barra degli strumenti **<img src="images/TechDraw_CosmeticEraser.svg" width=16px> [Rimuovi oggetto cosmetico](TechDraw_CosmeticEraser/it.md)**.

## Proprietà

I vertici cosmetici non hanno proprietà proprie, in quanto non sono dei Document Objects. Condividono le impostazioni di colore e dimensione con i normali vertici della geometria.

## Script


<div class="mw-translate-fuzzy">


**Vedere anche:**

[API TechDraw](TechDraw_API/it.md) e [Nozioni di base sugli script di FreeCAD](FreeCAD_Scripting_Basics/it.md).


</div>


<div class="mw-translate-fuzzy">

In questo momento i vertici cosmetici non sono accessibili dalle [macro](macros/it.md) o dalla console [Python](Python/it.md). Questo snippet rimuoverà tutti i vertici cosmetici dalla vista.


</div>


```python
>>> v = App.ActiveDocument.View
>>> v.clearCV()
>>> App.activeDocument().recompute()
```


<div class="mw-translate-fuzzy">





</div>


{{TechDraw Tools navi

}}



---
![](images/Right_arrow.png) [documentation index](../README.md) > [TechDraw](TechDraw_Workbench.md) > TechDraw Midpoints/it
