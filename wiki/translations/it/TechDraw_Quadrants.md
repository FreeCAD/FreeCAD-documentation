---
 GuiCommand:
   Name: TechDraw Quadrants
   Name/it: TechDraw Quadranti
   MenuLocation: TechDraw , Aggiungi Vertici , Aggiungi Vertici sul quadrante
   Workbenches: TechDraw_Workbench/it
   Version: 0.19
   SeeAlso: TechDraw CosmeticVertex/it, TechDraw Midpoints/it

---

# TechDraw Quadrants/it



## Descrizione

Lo strumento **TechDraw Quadranti** aggiunge tre [vertici cosmetici](TechDraw_CosmeticVertex/it.md) lungo la lunghezza di uno o più bordi selezionati. I vertici sono posizionati al 25%, 50% e 75% della lunghezza dei bordi. Per un bordo circolare ciò si traduce in vertici cosmetici a 90°, 180° e 270°, oltre al vertice geometrico a 0°.

<img alt="" src=images/TechDraw_CosmeticQuadrant_Sample.png  style="width:250px;"> 
*Vertici cosmetici nei punti del quadrante di un cerchio
*



## Utilizzo

1.  Selezionare uno o più bordi in una vista. È possibile selezionare qualsiasi bordo, non solo i cerchi.
2.  Esistono diversi modi per richiamare lo strumento:
    -   Premere il pulsante **<img src="images/TechDraw_Quadrants.svg" width=16px> [Aggiungi Vertici sul quadrante](TechDraw_Quadrants/it.md)**.
    -   Selezionare l\'opzione **TechDraw → Aggiungi Vertici → <img src="images/TechDraw_Quadrants.svg" width=16px> Aggiungi vertici sul quadrante** dal menu.



## Note

-   I vertici cosmetici creati non sono collegati parametricamente ai bordi selezionati.
-   Per eliminare un vertice cosmetico selezionarlo e premere **Delete**. {{Version/it|1.0}}



## Proprietà

I vertici cosmetici non hanno proprietà proprie, in quanto non sono dei Document Objects. Condividono le impostazioni di colore e dimensione con i normali vertici della geometria.



## Script

Vedere anche: [Autogenerated API documentation](https://freecad.github.io/SourceDoc/) e [Script di base per FreeCAD](FreeCAD_Scripting_Basics/it.md).

In questo momento i vertici cosmetici non sono accessibili dalle [macro](Macros/it.md) o dalla console [Python](Python/it.md). Questo snippet rimuoverà tutti i vertici cosmetici dalla vista.


```python
v = App.ActiveDocument.View
v.clearCV()
App.ActiveDocument.recompute()
```





{{TechDraw Tools navi

}}



---
⏵ [documentation index](../README.md) > [TechDraw](TechDraw_Workbench.md) > TechDraw Quadrants/it
