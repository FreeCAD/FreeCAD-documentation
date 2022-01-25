---
- GuiCommand:/it
   Name:TechDraw Dimension Horizontal Extent
   Name/it:Estensione orizzontale
   MenuLocation:TechDraw → Estensione orizzontale
   Workbenches:[TechDraw](TechDraw_Workbench/it.md)
   SeeAlso:[Lunghezza](TechDraw_LengthDimension/it.md), [Estensione verticale](TechDraw_VerticalExtentDimension/it.md)
---

# TechDraw HorizontalExtentDimension/it


</div>

## Descrizione


<div class="mw-translate-fuzzy">

Lo strumento Estensione orizzontale aggiunge una quota lineare a una vista. La dimensione si estende dal punto più a sinistra degli oggetti selezionati al punto più a destra. Viene posizionato un vertice cosmetico nei punti estremi.


</div>

<img alt="" src=images/TechDraw_Dimension_Horizontal_Extent_example.png  style="width:400px;"> 
*Estensione orizzontale della faccia BSpline*

## Utilizzo


<div class="mw-translate-fuzzy">

1.  Selezionare una vista o una serie di bordi in una vista.
2.  Premere il pulsante **<img src="images/TechDraw_HorizontalExtentDimension.svg" width=16px> [Estensione orizzontale](TechDraw_HorizontalExtentDimension/it.md)**.
3.  Viene aggiunta dimensione alla vista. La dimensione può essere trascinata nella posizione desiderata.


</div>

## Limitazioni


<div class="mw-translate-fuzzy">

Gli oggetti dimensione sono vulnerabili ai problemi di \"[denominazione topologica](topological_naming_problem/it.md)\". Per maggiori informazioni vedere le informazioni nello strumento **<img src="images/TechDraw_LengthDimension.svg" width=16px> [Lunghezza](TechDraw_LengthDimension/it.md)**.


</div>

## Proprietà


<div class="mw-translate-fuzzy">

Questo oggetto ha le stesse proprietà dello strumento [Lunghezza](TechDraw_LengthDimension/it.md). Eccezioni rilevate.


</div>

### Dati

-    **MeasureType**: `True` - basata sulla geometria 3D o \"Projected\" - basata sul disegno. Normalmente non manipolato direttamente dall\'utente finale. Non ancora implementata per Estensione orizzontale.

## Script


**Vedere anche:**

[API TechDraw](TechDraw_API/it.md) e [Nozioni di base sugli script di FreeCAD](FreeCAD_Scripting_Basics/it.md).


<div class="mw-translate-fuzzy">

Lo strumento Estensione orizzontale può essere utilizzato nelle [macro](macros/it.md) e dalla [console di Python](FreeCAD_Scripting_Basics/it.md) tramite la seguente funzione:


</div>


```python
selection = [(view1, 'Edge1'), (view1, 'Edge2')]  #or [] for all
hExtentDim = TechDraw.Dimension.makeExtentDim(selection, HORIZONTAL)
rc = page.addView(hExtentDim)
```





{{TechDraw Tools navi

}}



---
![](images/Right_arrow.png) [documentation index](../README.md) > [TechDraw](TechDraw_Workbench.md) > TechDraw HorizontalExtentDimension/it
