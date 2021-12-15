---
- GuiCommand:/it
   Name:TechDraw Dimension Angle3Pt
   Name/it:Angolo da 3 punti
   Workbenches:[TechDraw](TechDraw_Workbench/it.md)
   MenuLocation:TechDraw → Angolo da 3 punti
   Shortcut:
   SeeAlso:[Angolo](TechDraw_AngleDimension/it.md)
---

# TechDraw 3PtAngleDimension/it


</div>

## Descrizione


<div class="mw-translate-fuzzy">

Lo strumento <img alt="" src=images/TechDraw_3PtAngleDimension.svg  style="width:24px;"> Angolo da 3 punti aggiunge una dimensione angolare a una vista. La dimensione può essere specificata selezionando tre vertici su una vista. 
**Notare che il secondo dei tre vertici è l\'apice dell\'angolo**. Inizialmente viene indicato il valore dell\'angolo proiettato (vale a dire, come mostrato nel disegno), ma questo valore può essere sostituito con quello dell\'angolo 3D effettivo utilizzando lo strumento **<img src="images/TechDraw_LinkDimension.svg" width=16px> [Link alla dimensione](TechDraw_LinkDimension/it.md)**


</div>

<img alt="" src=images/TechDraw_Dimension_Angle3Pt_example.png  style="width:200px;"> 
*Misurare l'angolo tra due linee rette usando tre vertici; il secondo vertice è l'apice dell'angolo*

## Utilizzo


<div class="mw-translate-fuzzy">

1.  Selezionare i punti o bordi che definiscono la misura.
2.  Premere il pulsante **<img src="images/TechDraw_3PtAngleDimension.svg" width=16px> [Angolo da 3 punti](TechDraw_3PtAngleDimension/it.md)
**
3.  Alla Vista viene aggiunta una dimensione. La dimensione può essere trascinata nella posizione desiderata.


</div>

To change the properties of a dimension object either double-clicking it in the drawing or in the [Tree view](Tree_view.md). This will open the [dimension dialog](TechDraw_LengthDimension#Dimension_dialog.md).

## Limitazioni


<div class="mw-translate-fuzzy">

Gli oggetti dimensione sono vulnerabili ai problemi di \"denominazione topologica\". Per maggiori informazioni vedere le informazioni nello strumento <img alt="" src=images/TechDraw_LengthDimension.svg  style="width:16px;"> [Lunghezza](TechDraw_LengthDimension/it.md).


</div>

## Proprietà


<div class="mw-translate-fuzzy">

Questo oggetto ha le stesse proprietà dello strumento [Lunghezza](TechDraw_LengthDimension/it.md)


</div>

## Script


**Vedere anche:**

[TechDraw API](TechDraw_API/it.md) e [Nozioni di base sugli script di FreeCAD](FreeCAD_Scripting_Basics/it.md).


<div class="mw-translate-fuzzy">

Lo strumento Dimension Angle3Pt può essere utilizzato nelle [macro](macros/it.md) e dalla [console di Python](FreeCAD_Scripting_Basics/it.md) tramite la seguente funzione:


</div>


```python
dim1 = FreeCAD.ActiveDocument.addObject('TechDraw::DrawViewDimension','Dimension')
dim1.Type = "Angle3Pt"
dim1.References2D=[(view1, 'Vertex1',(view1, 'Vertex4'),(view1, 'Vertex2'))]
rc = page.addView(dim1)
```


<div class="mw-translate-fuzzy">





</div>


{{TechDraw Tools navi

}}

---
[documentation index](../README.md) > [TechDraw](TechDraw_Workbench.md) > TechDraw 3PtAngleDimension/it
