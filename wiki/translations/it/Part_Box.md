---
- GuiCommand:/it
   Name:Part Box   Name/it:Cubo
   Icon:Part Box.svg
   MenuLocation:Parte → Primitive → Cubo
   Workbenches:[Parte](Part_Workbench/it.md)
   SeeAlso:[Crea primitive...](Part_CreatePrimitives/it.md)
   Version:?
---


</div>

## Descrizione

Il comando Cubo dell\'ambiente [Part](Part_Workbench/it.md) inserisce nel documento attivo un [parallelepipedo](http://en.wikipedia.org/wiki/Cuboid#Rectangular_cuboid) parametrico. Di default, inserisce un cubo con i lati di 10 mm, posizionato nell\'origine, e con l\'etichetta \"Cubo\". Questi parametri possono essere modificati dopo aver aggiunto l\'oggetto.

<img alt="Part\_Box" src=images/Part_Box.jpg  style="width:400px;">


<div class="mw-translate-fuzzy">

## Uso

1.  Passare nell\'ambiente <img alt="" src=images/Workbench_Part.svg  style="width:24px;"> [Parte](Part_Workbench/it.md)
2.  Si può invocare il comando in diversi modi:
    -   Premere il pulsante **<img src="images/Part_Box.svg" width=24px>** sulla barra degli strumenti
    -   Selezionare {{MenuCommand|Parte → Primitive → Cubo}} nella barra dei menù.


</div>

**Result:** The default result is a box with an equal length, width and height of 10 mm. It is attached to the global xy-plane and one edge is coincident with the global z-axis.

The box properties can later be edited, either in the property editor or by double-clicking on the box in the model tree.


<div class="mw-translate-fuzzy">

## Proprietà


{{Properties_Title|Base}}

-    **Placement**: Specifica l\'orientamento e la posizione del Cubo nello spazio 3D. Vedere [ Posizionamento](Placement/it.md). Il punto di riferimento è l\'angolo anteriore in basso a sinistra del cubo.

-    **Label**: L\'etichetta è il nome assegnato all\'operazione. Questo nome può essere modificato a piacimento.


</div>


{{Properties_Title|Box}}

-    **Length**: Il parametro di lunghezza è la dimensione del Cubo nella direzione x.

-    **Width**: Il parametro di larghezza è la dimensione del Cubo nella direzione y.

-    **Height**: Il parametro di altezza è la dimensione del Cubo nella direzione z.

![Part\_Box-Properties](images/Part_Box-Properties.jpg )


<div class="mw-translate-fuzzy">

## Script

Lo strumento Cubo può essere utilizzato nelle [macro](macros/it.md) e dalla [console di Python](FreeCAD_Scripting_Basics/it.md) utilizzando la seguente funzione:


</div>


```python
FreeCAD.ActiveDocument.addObject("Part::Box", "myBox")
```

-   Dove \"myBox\" è l\'etichetta per l\'oggetto Box.
-   Restituisce un oggetto di tipo Box di nuova creazione.

È possibile accedere e modificare gli attributi dell\'oggetto Box. Ad esempio, si potrebbe desiderare di modificare i parametri di lunghezza, larghezza e altezza. 
```python
FreeCAD.ActiveDocument.myBox.Length = 25
FreeCAD.ActiveDocument.myBox.Width = 15
FreeCAD.ActiveDocument.myBox.Height = 30
```

È possibile modificare la sua posizione con: 
```python
FreeCAD.ActiveDocument.myBox.Placement = FreeCAD.Placement(FreeCAD.Vector(4, 6, 3), FreeCAD.Rotation(30, 45, 10))
```


<div class="mw-translate-fuzzy">





</div>


 
