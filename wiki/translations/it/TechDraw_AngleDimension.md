---
- GuiCommand   */it
   Name   *TechDraw Dimension Angle
   Name/it   *Angolo
   Workbenches   *[TechDraw](TechDraw_Workbench/it.md)
   MenuLocation   *TechDraw → Angolo
   Shortcut   *
   SeeAlso   *[Angolo da tre punti](TechDraw_3PtAngleDimension.md)
---

# TechDraw AngleDimension/it


</div>

## Descrizione


<div class="mw-translate-fuzzy">

Lo strumento Angolo aggiunge una dimensione angolare ad una Vista. La dimensione può essere l\'angolo interno tra due bordi rettilinei. Inizialmente viene indicato il valore dell\'angolo proiettato (vale a dire, come mostrato nel disegno), ma questo valore può essere sostituito con quello dell\'angolo 3D effettivo utilizzando lo strumento **<img src="images/TechDraw_LinkDimension.svg" width=16px> [Link alla dimensione](TechDraw_LinkDimension/it.md)**.


</div>

<img alt="" src=images/TechDraw_Dimension_Angle_example.png  style="width   *200px;"> 
*Misurazione dell'angolo tra due linee rette*

## Utilizzo


<div class="mw-translate-fuzzy">

1.  Selezionare i punti o bordi che definiscono la misura.
2.  Premere il pulsante **<img src="images/TechDraw_AngleDimension.svg" width=24px> [Angolo](TechDraw_AngleDimension/it.md)
**
3.  Alla Vista viene aggiunta una dimensione. La dimensione può essere trascinata nella posizione desiderata.


</div>

To change the properties of a dimension object either double-clicking it in the drawing or in the [Tree view](Tree_view.md). This will open the [dimension dialog](TechDraw_LengthDimension#Dimension_dialog.md).

## Limitazioni


<div class="mw-translate-fuzzy">

Gli oggetti dimensione sono vulnerabili ai problemi di \"denominazione topologica\". Per maggiori informazioni vedere le informazioni nello strumento <img alt="" src=images/TechDraw_LengthDimension.svg  style="width   *16px;"> [Lunghezza](TechDraw_LengthDimension/it.md).


</div>

## Proprietà


<div class="mw-translate-fuzzy">

Questo oggetto ha le stesse proprietà dello strumento [Lunghezza](TechDraw_LengthDimension/it.md)


</div>

## Script


**Vedere anche   ***

[TechDraw API](TechDraw_API/it.md) e [Nozioni di base sugli script di FreeCAD](FreeCAD_Scripting_Basics/it.md).


<div class="mw-translate-fuzzy">

Lo strumento Dimension Angle può essere utilizzato nelle [macro](macros/it.md) e dalla [console di Python](FreeCAD_Scripting_Basics/it.md) tramite la seguente funzione   *


</div>


```python
dim1 = FreeCAD.ActiveDocument.addObject('TechDraw   *   *DrawViewDimension','Dimension')
dim1.Type = "Angle"
dim1.References2D=[(view1, 'Edge1')]
rc = page.addView(dim1)
```


<div class="mw-translate-fuzzy">





</div>


{{TechDraw Tools navi

}}



---
![](images/Right_arrow.png) [documentation index](../README.md) > [TechDraw](TechDraw_Workbench.md) > TechDraw AngleDimension/it
