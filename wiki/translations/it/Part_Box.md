---
- GuiCommand:/it
   Name:Part Box   Name/it:Cubo
   Icon:Part Box.svg
   MenuLocation:Parte → Primitive → Cubo
   Workbenches:[Parte](Part_Workbench/it.md)
   SeeAlso:[Crea primitive...](Part_CreatePrimitives/it.md)
   Version:?
---

# Part Box/it


</div>

## Description


<div class="mw-translate-fuzzy">

## Descrizione

Il comando Cubo dell\'ambiente [Part](Part_Workbench/it.md) inserisce nel documento attivo un [parallelepipedo](http://en.wikipedia.org/wiki/Cuboid#Rectangular_cuboid) parametrico. Di default, inserisce un cubo con i lati di 10 mm, posizionato nell\'origine, e con l\'etichetta \"Cubo\". Questi parametri possono essere modificati dopo aver aggiunto l\'oggetto.


</div>

<img alt="Part\_Box" src=images/Part_Box.jpg  style="width:400px;">

## Usage


<div class="mw-translate-fuzzy">

## Uso

1.  Passare nell\'ambiente <img alt="" src=images/Workbench_Part.svg  style="width:24px;"> [Parte](Part_Workbench/it.md)
2.  Si può invocare il comando in diversi modi:
    -   Premere il pulsante **<img src="images/Part_Box.svg" width=24px>** sulla barra degli strumenti
    -   Selezionare **Parte → Primitive → Cubo** nella barra dei menù.


</div>

**Result:** The default result is a box with an equal length, width and height of 10 mm. It is attached to the global xy-plane and one edge is coincident with the global z-axis.

The box properties can later be edited, either in the property editor or by double-clicking on the box in the model tree.

## Properties


{{Properties_Title|Box}}


<div class="mw-translate-fuzzy">


{{Properties_Title|Box}}

-    **Length**: Il parametro di lunghezza è la dimensione del Cubo nella direzione x.

-    **Width**: Il parametro di larghezza è la dimensione del Cubo nella direzione y.

-    **Height**: Il parametro di altezza è la dimensione del Cubo nella direzione z.


</div>

## Scripting


<div class="mw-translate-fuzzy">

## Script

Lo strumento Cubo può essere utilizzato nelle [macro](macros/it.md) e dalla [console di Python](FreeCAD_Scripting_Basics/it.md) utilizzando la seguente funzione:


</div>


```python
box = FreeCAD.ActiveDocument.addObject("Part::Box", "myBox")
```


<div class="mw-translate-fuzzy">

-   Dove \"myBox\" è l\'etichetta per l\'oggetto Box.
-   Restituisce un oggetto di tipo Box di nuova creazione.


</div>


<div class="mw-translate-fuzzy">

È possibile accedere e modificare gli attributi dell\'oggetto Box. Ad esempio, si potrebbe desiderare di modificare i parametri di lunghezza, larghezza e altezza.


</div>


```python
box.Length = 25
box.Width = 15
box.Height = 30
```

È possibile modificare la sua posizione con:


```python
box.Placement = FreeCAD.Placement(FreeCAD.Vector(4, 6, 3), FreeCAD.Rotation(30, 45, 10))
```


<div class="mw-translate-fuzzy">





</div>

---
[documentation index](../README.md) > [Part](Part_Workbench.md) > Part Box/it
