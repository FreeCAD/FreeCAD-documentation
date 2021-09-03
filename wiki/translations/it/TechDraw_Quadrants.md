---
- GuiCommand:/it
   Name:TechDraw Quadrants
   Name/it:Quadrante
   MenuLocation:TechDraw → Aggiungi vertici → Quadrante
   Workbenches:[TechDraw](TechDraw_Workbench/it.md)
   SeeAlso:[Vertice cosmetico](TechDraw_CosmeticVertex/it.md), [Punti mediani](TechDraw_Midpoints/it.md)
   Version:0.19
---


</div>

## Descrizione

Lo strumento Quadrante aggiunge dei [vertici cosmetici](TechDraw_CosmeticVertex/it.md) nei punti a 90/180/270° di un bordo circolare. Il vertice di 0° dovrebbe già essere presente come vertice geometrico.

<img alt="" src=images/TechDraw_CosmeticQuadrant_Sample.png  style="width:250px;"> *Vertici cosmetici nei punti del quadrante di un cerchio
*

## Utilizzo

1.  Selezionare uno o più bordi circolari in una vista.
2.  Premere il pulsante **<img src="images/TechDraw_Quadrants.svg" width=16px> Quadrante**.
3.  I vertici cosmetici vengono aggiunti nei punti quarti del bordo.

**Nota:** Questo strumento può essere utilizzato su qualsiasi bordo, non solo sui cerchi.

Per eliminare un vertice di un quadrante, selezionarlo e utilizzare il pulsante della barra degli strumenti **<img src="images/TechDraw_CosmeticEraser.svg" width=16px> [Rimuovi oggetto cosmetico](TechDraw_CosmeticEraser/it.md)**.

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
