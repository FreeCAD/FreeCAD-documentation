---
 GuiCommand:
   Name: TechDraw RadiusDimension
   Name/it: TechDraw Quota raggio
   MenuLocation: TechDraw , Quotatura , Inserisci Quota raggio
   Workbenches: TechDraw_Workbench/it
   SeeAlso: TechDraw_DiameterDimension/it
---

# TechDraw RadiusDimension/it



## Descrizione

Lo strumento **TechDraw Quota raggio** aggiunge una quota del raggio ad una Vista. La quota può essere applicata a qualsiasi bordo che sia un cerchio o un arco circolare.

<img alt="" src=images/TechDraw_Dimension_Radius_example.png  style="width:130px;"> 
*Quotatura di un cerchio, indicando il raggio*



## Uso

1.  Selezionare un cerchio o un arco circolare. La geometria può essere selezionata nella [Vista 3D](3D_view/it.md) o nel disegno. Notare che alcuni archi che sembrano circolari sono in realtà ellissi o B-spline. In questi casi non è possibile creare una Quota raggio.
2.  Se si ha selezionato la geometria nella vista 3D: aggiungere la Vista TechDraw corretta alla selezione selezionandola nella [Vista ad albero](Tree_view/it.md).
3.  Esistono diversi modi per richiamare lo strumento:
    -   
        {{Version/it|1.0}}
        
        : Se la [preferenza](TechDraw_Preferences/it#Dimensions.md) degli **Strumenti di quotatura** è impostata su {{Value|Strumento singolo}} (predefinito): premere la freccia giù a destra del pulsante **<img src="images/TechDraw_Dimension.svg" width=|x16px><img src="images/Toolbar_flyout_arrow.svg" width=x16px>** e selezionare il pulsante **<img src="images/TechDraw_RadiusDimension.svg" width=16px> Inserisci Quota Raggio** dal menu a discesa.

    -   Se questa preferenza ha un valore diverso (e in {{VersionMinus/it|0.21}}): premere il pulsante **<img src="images/TechDraw_RadiusDimension.svg" width=16px> [Inserisci Quota Raggio](TechDraw_RadiusDimension/it.md)** .

    -   Selezionare l\'opzione **TechDraw → Quotatura → <img src="images/TechDraw_RadiusDimension.svg" width=16px> Inserisci Quota raggio** dal menu.
4.  Una quota viene aggiunta alla Vista.
5.  La quota può essere trascinata nella posizione desiderata.
6.  Se necessario, aggiungere tolleranze come descritto in [questa pagina](TechDraw_Geometric_dimensioning_and_tolerancing/it#Tolleranze.md).



### Visualizzazione quotatura 3D 

Vedere [TechDraw LengthDimension](TechDraw_LengthDimension/it#Display_3D_measurement.md).



### Cambiare le proprietà 

Per modificare le proprietà di un oggetto quota, fare doppio clic su di esso nel disegno o nella [Vista ad albero](Tree_view/it.md). Si aprirà la [Finestra di dialogo Quota](TechDraw_LengthDimension/it#Finestra_di_dialogo_Quota.md).



## Limitazioni

Gli oggetti Quota sono vulnerabili al \"[problema di denominazione topologica](Topological_naming_problem/it.md)\". Vedere [TechDraw Quota allineata](TechDraw_LengthDimension/it.md).



## Note

Vedere [TechDraw Quota allineata](TechDraw_LengthDimension/it#Note.md).



## Proprietà

Vedere [TechDraw Quota allineata](TechDraw_LengthDimension/it#Proprietà.md).



## Script

Vedere anche: [Autogenerated API documentation](https://freecad.github.io/SourceDoc/) e [Script di base per FreeCAD](FreeCAD_Scripting_Basics/it.md).

Lo strumento Quota raggio può essere utilizzato nelle [macro](Macros/it.md) e dalla console [Python](Python/it.md) tramite la seguente funzione:


```python
dim1 = FreeCAD.ActiveDocument.addObject("TechDraw::DrawViewDimension", "Dimension")
dim1.Type = "Radius"
dim1.References2D=[(view1, "Edge1")]
page.addView(dim1)
```





{{TechDraw Tools navi

}}



---
⏵ [documentation index](../README.md) > [TechDraw](TechDraw_Workbench.md) > TechDraw RadiusDimension/it
