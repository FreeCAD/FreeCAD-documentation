---
- GuiCommand:/it
   Name:TechDraw CosmeticVertex
   Name/it:Vertice cosmetico
   Icon:techdraw-point.svg
   MenuLocation:TechDraw → Aggiuge Vertici → Vertice cosmetico
   Workbenches:[TechDraw](TechDraw_Workbench/it.md)
   SeeAlso:[Punti mediani](TechDraw_Midpoints/it.md), [Quadrante](TechDraw_Quadrants/it.md)
   Version:0.19
---

# TechDraw CosmeticVertex/it


</div>

## Descrizione

Lo strumento Vertice cosmetico aggiunge ad una vista un [vertice](Glossary#V.md) che non fa parte della geometria di origine. Questo vertice si comporta come qualsiasi altro vertice e può essere utilizzato per il dimensionamento.

<img alt="" src=images/TechDraw_CosmeticVertex_Sample.png  style="width:300px;"> 
*Vertice cosmetico utilizzato per creare una dimensione altrimenti impossibile*

## Utilizzo

1.  Selezionare una vista nel disegno.
2.  Premere il pulsante **<img src="images/TechDraw_CosmeticVertex.svg" width=16px> Vertice cosmetico**.
3.  Si apre una finestra di dialogo delle azioni che permette di impostare la posizione del vertice cosmetico selezionando un punto o inserendo un offset x, y dal centro della vista selezionata.
4.  Per selezionare una posizione, premere il pulsante **Selettore del punto**. Fare clic su una posizione nella vista e successivamente premere **OK** per creare il punto. Per uscire dalla selezione dei punti senza creare un vertice cosmetico, premere il pulsante **Escape picking** nella finestra di dialogo.

Per eliminare un vertice cosmetico, selezionarlo e utilizzare il pulsante della barra degli strumenti **<img src="images/TechDraw_CosmeticEraser.svg" width=16px> [Rimuovi oggetto cosmetico](TechDraw_CosmeticEraser/it.md)**.

**Nota:** Non è possibile modificare la posizione del vertice cosmetico dopo che è stato creato. Al momento bisogna eliminarlo e crearne uno nuovo.

## Proprietà

I vertici cosmetici non hanno proprietà proprie, in quanto non sono dei Document Objects. Condividono le impostazioni di colore e dimensione con i normali vertici della geometria.

## Script


<div class="mw-translate-fuzzy">


**Vedere anche:**

[API TechDraw](TechDraw_API/it.md) e [Nozioni di base sugli script di FreeCAD](FreeCAD_Scripting_Basics/it.md).


</div>


<div class="mw-translate-fuzzy">

I vertici cosmetici sono accessibili dalle [macro](macros/it.md) o dalla console [Python](Python/it.md).


</div>


```python
dvp = App.ActiveDocument.View
org = App.Vector(0.0, 0.0, 0.0)
dvp.makeCosmeticVertex(org);

#lines too!
start = FreeCAD.Vector (1.0, 5.0, 0.0)
end = FreeCAD.Vector(1.0, -5.0, 0.0)
style = 2
weight = 0.75
pyGreen = (0.0, 0.0, 1.0, 0.0)
dvp.makeCosmeticLine(start,end,style, weight, pyGreen)
```


<div class="mw-translate-fuzzy">





</div>


{{TechDraw Tools navi

}}



---
![](images/Right_arrow.png) [documentation index](../README.md) > [TechDraw](TechDraw_Workbench.md) > TechDraw CosmeticVertex/it
