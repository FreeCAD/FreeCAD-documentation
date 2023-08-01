---
- GuiCommand:
   Name: TechDraw Dimension Horizontal Extent
   Name/it: Estensione orizzontale
   MenuLocation: TechDraw - Estensione orizzontale
   Workbenches: [TechDraw](TechDraw_Workbench/it.md)
   SeeAlso: [Lunghezza](TechDraw_LengthDimension/it.md), [Estensione verticale](TechDraw_VerticalExtentDimension/it.md)
---

# TechDraw HorizontalExtentDimension/it


</div>



## Descrizione


<div class="mw-translate-fuzzy">

Lo strumento Estensione orizzontale aggiunge una quota lineare a una vista. La dimensione si estende dal punto più a sinistra degli oggetti selezionati al punto più a destra. Viene posizionato un vertice cosmetico nei punti estremi.


</div>

<img alt="" src=images/TechDraw_Dimension_Horizontal_Extent_example.png  style="width:400px;">


<div class="mw-translate-fuzzy">



*Estensione orizzontale della faccia BSpline*


</div>



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
selection = ['Edge1', 'Edge2']                      # or [] for all

TechDraw.makeExtentDim(view1, selection, 0)         # view1 is a DrawViewPart; 0 for horizontal
App.ActiveDocument.DimExtent.Y = -60                # offset dimension line from dimensioned edges in Y direction
App.ActiveDocument.DimExtent.X = 10                 # offset dimension text along dimension line in X direction
App.ActiveDocument.DimExtent.FormatSpec = '%.0f'    # Dimension format

TechDraw.makeExtentDim(view1, selection, 1)         # view1 is a DrawViewPart; 1 for vertical
App.ActiveDocument.DimExtent001.X = -130            # offset dimension line from dimensioned edges in X direction
App.ActiveDocument.DimExtent001.Y = 10              # offset dimension text along dimension line in Y direction
App.ActiveDocument.DimExtent001.FormatSpec = '%.0f'

# Note the dimension names are 'DimExtent', 'DimExtent001' etc in the order created.
```





{{TechDraw Tools navi

}}



---
⏵ [documentation index](../README.md) > [TechDraw](TechDraw_Workbench.md) > TechDraw HorizontalExtentDimension/it
