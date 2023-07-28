---
- GuiCommand:/it
   Name:TechDraw Dimension Radius
   Name/it:Raggio
   Workbenches:[TechDraw](TechDraw_Workbench/it.md)
   MenuLocation:TechDraw → Raggio
   Shortcut:
   SeeAlso:[Diametro](TechDraw_DiameterDimension/it.md)
---

# TechDraw RadiusDimension/it


</div>



## Descrizione


<div class="mw-translate-fuzzy">

Lo strumento Raggio aggiunge una dimensione di diametro a una vista. La dimensione può essere applicata a qualsiasi bordo circolare del disegno. Inizialmente viene indicato il valore della distanza proiettata (vale a dire, come mostrato nel disegno), ma questo valore può essere sostituito con quello dell\'effettiva distanza 3D utilizzando lo strumento **<img src="images/TechDraw_LinkDimension.svg" width=16px>  [Link alla dimensione](TechDraw_LinkDimension/it.md)**.


</div>

<img alt="" src=images/TechDraw_Dimension_Radius_example.png  style="width:130px;"> 
*Misurare un cerchio, indicando il raggio*



## Uso


<div class="mw-translate-fuzzy">

1.  Selezionare un cerchio o arco di cerchio nel disegno. (Notare che alcuni archi che sembrano essere circolari sono in realtà ellissi o B spline. In questi casi non si può creare una dimensione di raggio)
2.  Premere il pulsante **<img src="images/TechDraw_RadiusDimension.svg" width=16px> [Raggio](TechDraw_RadiusDimension/it.md)
**
3.  Alla Vista viene aggiunta una dimensione. La dimensione può essere trascinata nella posizione desiderata.


</div>

### Display 3D measurement 

See [TechDraw LengthDimension](TechDraw_LengthDimension#Display_3D_measurement.md).

### Change properties 

To change the properties of a dimension object either double-click it in the drawing or in the [Tree view](Tree_view.md). This will open the [Dimension dialog](TechDraw_LengthDimension#Dimension_dialog.md).



## Limitazioni


<div class="mw-translate-fuzzy">

Gli oggetti dimensione sono vulnerabili ai problemi di \"denominazione topologica\". Per maggiori informazioni vedere le informazioni nello strumento [Lunghezza](TechDraw_LengthDimension/it.md).


</div>

## Notes

See [TechDraw LengthDimension](TechDraw_LengthDimension#Notes.md).



## Proprietà


<div class="mw-translate-fuzzy">

Questo oggetto ha le stesse proprietà dello strumento [Lunghezza](TechDraw_LengthDimension/it.md)


</div>



## Script


**Vedere anche:**

[API TechDraw](TechDraw_API/it.md) e [Nozioni di base sugli script di FreeCAD](FreeCAD_Scripting_Basics/it.md).


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



---
![](images/Right_arrow.png) [documentation index](../README.md) > [TechDraw](TechDraw_Workbench.md) > TechDraw RadiusDimension/it
