---
- GuiCommand:/it
   Name:TechDraw Dimension Vertical
   Name/it:Dimensione verticale
   Workbenches:[TechDraw](TechDraw_Workbench/it.md)
   MenuLocation:TechDraw → Dimensione verticale
   Shortcut:
   SeeAlso:[Lunghezza](TechDraw_LengthDimension/it.md), [Orizzontale](TechDraw_HorizontalDimension/it.md)
---

# TechDraw VerticalDimension/it


</div>

## Descrizione


<div class="mw-translate-fuzzy">

Lo strumento Dimensione verticale aggiunge una dimensione verticale ad una Vista. La dimensione può essere la distanza tra due vertici, la lunghezza di uno spigolo o la distanza verticale tra 2 spigoli. La distanza indicata all\'inizio è la distanza proiettata (vale a dire, come mostrata nel disegno), ma utilizzando lo strumento **<img src="images/TechDraw_LinkDimension.svg" width=16px> [Link alla dimensione](TechDraw_LinkDimension/it.md)** essa può essere modificata con la distanza 3D effettiva.


</div>

<img alt="" src=images/TechDraw_Dimension_Vertical_example.png  style="width:220px;"> 
*Dimensione della lunghezza presa da due nodi arbitrari della vista; la distanza è misurata verticalmente*

## Utilizzo


<div class="mw-translate-fuzzy">

1.  Selezionare i punti o i bordi che definiscono la misura.
2.  Premere il pulsante **<img src="images/TechDraw_VerticalDimension.svg" width=24px> [Dimensione verticale](TechDraw_VerticalDimension/it.md)
**
3.  Viene aggiunta una dimensione alla vista. La dimensione può essere trascinata nella posizione desiderata.


</div>

To change the properties of a dimension object either double-clicking it in the drawing or in the [Tree view](Tree_view.md). This will open the [dimension dialog](TechDraw_LengthDimension#Dimension_dialog.md).

## Limitazioni


<div class="mw-translate-fuzzy">

Gli oggetti dimensione sono vulnerabili ai problemi di \"[denominazione topologica](Topological_naming_problem/it.md)\". Per maggiori informazioni vedere le informazioni nello strumento [Lunghezza](TechDraw_LengthDimension/it.md).


</div>

## Proprietà


<div class="mw-translate-fuzzy">

Questo oggetto ha le stesse proprietà dello strumento [Lunghezza](TechDraw_LengthDimension/it.md)


</div>

## Script


**Vedere anche:**

[TechDraw API](TechDraw_API/it.md) e [Nozioni di base sugli script di FreeCAD](FreeCAD_Scripting_Basics/it.md).


<div class="mw-translate-fuzzy">

Lo strumento Dimension Vertical può essere utilizzato nelle [macro](macros/it.md) e dalla [console di Python](FreeCAD_Scripting_Basics/it.md) tramite la seguente funzione:


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

---
[documentation index](../README.md) > [TechDraw](TechDraw_Workbench.md) > TechDraw VerticalDimension/it
