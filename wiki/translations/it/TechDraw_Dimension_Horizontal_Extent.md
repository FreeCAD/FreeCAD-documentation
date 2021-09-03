---
- GuiCommand:/it
   Name:TechDraw Dimension Horizontal Extent
   Name/it:Estensione orizzontale
   MenuLocation:TechDraw → Estensione orizzontale
   Workbenches:[TechDraw](TechDraw_Workbench/it.md)
   SeeAlso:[Lunghezza](TechDraw_Dimension_Length/it.md), [Estensione verticale](TechDraw_Dimension_Vertical_Extent/it.md)
---


</div>

## Descrizione

Lo strumento Estensione orizzontale aggiunge una quota lineare a una vista. La dimensione si estende dal punto più a sinistra degli oggetti selezionati al punto più a destra. Viene posizionato un vertice cosmetico nei punti estremi.

<img alt="" src=images/TechDraw_Dimension_Horizontal_Extent_example.png  style="width:400px;"> 
*Estensione orizzontale della faccia BSpline*

## Utilizzo


<div class="mw-translate-fuzzy">

1.  Selezionare una vista o una serie di bordi in una vista.
2.  Premere il pulsante **<img src="images/TechDraw_Dimension_HExtent.svg" width=16px> [Estensione orizzontale](TechDraw_Dimension_Horizontal_Extent/it.md)**.
3.  Viene aggiunta dimensione alla vista. La dimensione può essere trascinata nella posizione desiderata.


</div>

## Limitazioni


<div class="mw-translate-fuzzy">

Gli oggetti dimensione sono vulnerabili ai problemi di \"[denominazione topologica](topological_naming_problem/it.md)\". Per maggiori informazioni vedere le informazioni nello strumento **<img src="images/TechDraw_Dimension_Length.svg" width=16px> [Lunghezza](TechDraw_Dimension_Length/it.md)**.


</div>

## Proprietà


<div class="mw-translate-fuzzy">

Questo oggetto ha le stesse proprietà dello strumento [Lunghezza](TechDraw_Dimension_Length/it.md). Eccezioni rilevate.


</div>

### Dati

-    **MeasureType**: `True` - basata sulla geometria 3D o \"Projected\" - basata sul disegno. Normalmente non manipolato direttamente dall\'utente finale. Non ancora implementata per Estensione orizzontale.

## Script


<div class="mw-translate-fuzzy">


**Vedere anche:**

[API TechDraw](TechDraw_API/it.md) e [Nozioni di base sugli script di FreeCAD](FreeCAD_Scripting_Basics/it.md).


</div>


<div class="mw-translate-fuzzy">

Lo strumento Estensione orizzontale può essere utilizzato nelle [macro](macros/it.md) e dalla [console di Python](FreeCAD_Scripting_Basics/it.md) tramite la seguente funzione:


</div>


```python
selection = [(view1, 'Edge1'), (view1, 'Edge2')]  #or [] for all
hExtentDim = TechDraw.Dimension.makeExtentDim(selection, HORIZONTAL)
rc = page.addView(hExtentDim)
```


<div class="mw-translate-fuzzy">





</div>


{{TechDraw Tools navi

}}  
