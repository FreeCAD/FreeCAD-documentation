---
- GuiCommand   */it
   Name   *TechDraw  Dimension Diameter
   Name/it   *Diametro
   Workbenches   *[TechDraw](TechDraw_Workbench/it.md)
   MenuLocation   *TechDraw → Diametro
   Shortcut   *
   SeeAlso   *[Raggio](TechDraw_RadiusDimension/it.md)
---

# TechDraw DiameterDimension/it


</div>

## Descrizione


<div class="mw-translate-fuzzy">

Lo strumento Diametro aggiunge una dimensione di diametro a una vista.

La dimensione può essere applicata a qualsiasi parte circolare del disegno. Inizialmente viene indicato il valore della distanza proiettata (vale a dire, come mostrato nel disegno), ma questo valore può essere sostituito con quello dell\'effettiva distanza 3D utilizzando lo strumento **<img src="images/TechDraw_LinkDimension.svg" width=16px> [Link alla dimensione](TechDraw_LinkDimension/it.md)**.


</div>

<img alt="" src=images/TechDraw_Dimension_Diameter_example.png  style="width   *130px;"> 
*Misurazione di un cerchio, indicando il diametro*

## Utilizzo


<div class="mw-translate-fuzzy">

1.  Selezionare un bordo circolare nel disegno. (Notare che alcuni archi che sembrano essere circolari sono in realtà ellissi o bspline. In questi casi non si può creare una dimensione di diametro)
2.  Premere il pulsante **<img src="images/TechDraw_DiameterDimension.svg" width=24px> [Diametro](TechDraw_DiameterDimension/it.md)
**
3.  Alla Vista viene aggiunta una dimensione. La dimensione può essere trascinata nella posizione desiderata.


</div>

To change the properties of a dimension object either double-clicking it in the drawing or in the [Tree view](Tree_view.md). This will open the [dimension dialog](TechDraw_LengthDimension#Dimension_dialog.md).

## Limitazioni


<div class="mw-translate-fuzzy">

Gli oggetti dimensione sono vulnerabili ai problemi di \"denominazione topologica\". Per maggiori informazioni vedere le informazioni nello strumento [Lunghezza](TechDraw_LengthDimension/it.md).


</div>

## Proprietà


<div class="mw-translate-fuzzy">

Questo oggetto ha le stesse proprietà dello strumento [Lunghezza](TechDraw_LengthDimension/it.md)


</div>

## Script


**Vedere anche   ***

[TechDraw API](TechDraw_API/it.md) e [Nozioni di base sugli script di FreeCAD](FreeCAD_Scripting_Basics/it.md).


<div class="mw-translate-fuzzy">

Lo strumento Dimension Diameter può essere utilizzato nelle [macro](macros/it.md) e dalla [console di Python](FreeCAD_Scripting_Basics/it.md) tramite la seguente funzione   *


</div>


```python
dim1 = FreeCAD.ActiveDocument.addObject('TechDraw   *   *DrawViewDimension','Dimension')
dim1.Type = "Diameter"
dim1.References2D=[(view1, 'Edge1')]
rc = page.addView(dim1)
```


<div class="mw-translate-fuzzy">





</div>


{{TechDraw Tools navi

}}



---
![](images/Right_arrow.png) [documentation index](../README.md) > [TechDraw](TechDraw_Workbench.md) > TechDraw DiameterDimension/it
