---
- GuiCommand:/it   Name:TechDraw Dimension Radius   Name/it:Raggio   Workbenches:[MenuLocation:TechDraw → Raggio   Shortcut:   SeeAlso:[[TechDraw Dimension Diameter/it|Diametro](TechDraw_Workbench/it___TechDraw]].md)---


</div>

## Descrizione

Lo strumento Raggio aggiunge una dimensione di diametro a una vista. La dimensione può essere applicata a qualsiasi bordo circolare del disegno. Inizialmente viene indicato il valore della distanza proiettata (vale a dire, come mostrato nel disegno), ma questo valore può essere sostituito con quello dell\'effettiva distanza 3D utilizzando lo strumento **<img src="images/TechDraw_Dimension_Link.svg" width=16px>  [Link alla dimensione](TechDraw_Dimension_Link/it.md)**.

<img alt="" src=images/TechDraw_Dimension_Radius_example.png  style="width:130px;"> 
*Misurare un cerchio, indicando il raggio*

## Uso


<div class="mw-translate-fuzzy">

1.  Selezionare un cerchio o arco di cerchio nel disegno. (Notare che alcuni archi che sembrano essere circolari sono in realtà ellissi o B spline. In questi casi non si può creare una dimensione di raggio)
2.  Premere il pulsante **<img src="images/TechDraw_Dimension_Radius.svg" width=16px> [Raggio](TechDraw_Dimension_Radius/it.md)
**
3.  Alla Vista viene aggiunta una dimensione. La dimensione può essere trascinata nella posizione desiderata.


</div>

To change the properties of a dimension object either double-clicking it in the drawing or in the [Tree view](Tree_view.md). This will open the [dimension dialog](TechDraw_Dimension_Length#Dimension_dialog.md).

## Limitazioni


<div class="mw-translate-fuzzy">

Gli oggetti dimensione sono vulnerabili ai problemi di \"denominazione topologica\". Per maggiori informazioni vedere le informazioni nello strumento [Lunghezza](TechDraw_Dimension_Length/it.md).


</div>

## Proprietà


<div class="mw-translate-fuzzy">

Questo oggetto ha le stesse proprietà dello strumento [Lunghezza](TechDraw_Dimension_Length/it.md)


</div>

## Script


<div class="mw-translate-fuzzy">


**Vedere anche:**

[API TechDraw](TechDraw_API/it.md) e [Nozioni di base sugli script di FreeCAD](FreeCAD_Scripting_Basics/it.md).


</div>


<div class="mw-translate-fuzzy">

Lo strumento Raggio può essere utilizzato nelle [macro](macros/it.md) e dalla console [Python](Python/it.md) tramite la seguente funzione:


</div>


```python
dim1 = FreeCAD.ActiveDocument.addObject('TechDraw::DrawViewDimension','Dimension')
dim1.Type = "Radius"
dim1.References2D=[(view1, 'Edge1')]
rc = page.addView(dim1)
```


<div class="mw-translate-fuzzy">





</div>


{{TechDraw Tools navi

}}  
