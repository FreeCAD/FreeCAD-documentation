---
- GuiCommand:/it   Name:TechDraw_HorizontalDimension   Name/it:Dimensione orizzontale   Workbenches:[MenuLocation:TechDraw → Dimensione orizzontale   Shortcut:   SeeAlso:[[TechDraw Dimension Length/it|Lunghezza](TechDraw_Workbench/it___TechDraw]].md), [Dimensione verticale](TechDraw_Dimension_Vertical/it.md)---


</div>

## Descrizione


<div class="mw-translate-fuzzy">

Lo strumento dimensione Orizzontale aggiunge una dimensione orizzontale ad una Vista. La dimensione può essere la distanza tra due vertici, la lunghezza di uno spigolo o la distanza orizzontale tra 2 spigoli. La distanza indicata all\'inizio è la distanza proiettata (vale a dire, come mostrata nel disegno), ma utilizzando lo strumento **<img src="images/TechDraw_Dimension_Link.svg" width=16px>  [Link alla dimensione](TechDraw_Dimension_Link/it.md)** essa può essere modificata con la distanza 3D effettiva.


</div>

<img alt="" src=images/TechDraw_Dimension_Horizontal_example.png  style="width:200px;"> 
*Dimensione della lunghezza presa da due nodi arbitrari della vista; la distanza è misurata orizzontalmente*

## Uso


<div class="mw-translate-fuzzy">

1.  Selezionare i punti o i bordi che definiscono la misura.
2.  Premere il pulsante **<img src="images/TechDraw_Dimension_Horizontal.svg" width=24px> [Dimensione orizzontale](TechDraw_Dimension_Horizontal/it.md)
**
3.  Viene aggiunta una dimensione alla vista. La dimensione può essere trascinata nella posizione desiderata.


</div>

To change the properties of a dimension object either double-clicking it in the drawing or in the [Tree view](Tree_view.md). This will open the [dimension dialog](TechDraw_LengthDimension#Dimension_dialog.md).

## Limitazioni


<div class="mw-translate-fuzzy">

Gli oggetti dimensione sono vulnerabili ai problemi di \"denominazione topologica\". Per maggiori informazioni vedere le informazioni nello strumento [Lunghezza](TechDraw_Dimension_Length/it.md).


</div>

## Proprietà


<div class="mw-translate-fuzzy">

Questo oggetto ha le stesse proprietà dello strumento [Lunghezza](TechDraw_Dimension_Length/it.md)


</div>

## Script


**Vedere anche:**

[TechDraw API](TechDraw_API/it.md) e [Nozioni di base sugli script di FreeCAD](FreeCAD_Scripting_Basics/it.md).


<div class="mw-translate-fuzzy">

Lo strumento Dimension Horizontal può essere utilizzato nelle [macro](macros/it.md) e dalla [console di Python](FreeCAD_Scripting_Basics/it.md) tramite la seguente funzione:


</div>


```python
dim1 = FreeCAD.ActiveDocument.addObject('TechDraw::DrawViewDimension','Dimension')
dim1.Type = "DistanceX"
dim1.References2D=[(view1, 'Edge1')]
rc = page.addView(dim1)
```


<div class="mw-translate-fuzzy">





</div>


{{TechDraw Tools navi

}} 
