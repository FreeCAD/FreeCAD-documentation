---
- GuiCommand:   Name:Part Box   MenuLocation:Part → Primitives → Cube   |Workbenches:[SeeAlso:[[Part_CreatePrimitives|Part CreatePrimitives](Part_Workbench___Part]],_Complete.md)---


</div>

## Descriere

Comanda Box din Atelierul [Part Workbench](Part_Workbench.md) inserează o casetă parametrică, [rectangular cuboid](http://en.wikipedia.org/wiki/Cuboid#Rectangular_cuboid), o primitivă geometrică în documentul activ. Implicit, comanda Box va insera un cub de 10x10x10 mm, poziționaat în origine, cu denumirea/eticheta \"cube\". Acești parametri pot fi modificați după adăugarea obiectului.

<img alt="Part\_Box" src=images/Part_Box.jpg  style="width:400px;">


<div class="mw-translate-fuzzy">

## Cum se folosește {#cum_se_folosește}

-   Click the cube icon **<img src="images/Part_Box.png" width=30px>** from the Part Workbench.
-   Alternatively, you can select {{MenuCommand|Part → Primitives → Cube}} from the menu bar.


</div>

**Result:** The default result is a box with an equal length, width and height of 10 mm. It is attached to the global xy-plane and one edge is coincident with the global z-axis.

The box properties can later be edited, either in the property editor or by double-clicking on the box in the model tree.


<div class="mw-translate-fuzzy">

## Proprietăți


{{Properties_Title|Base}}

-    **Placement**: Determină orientarea și poziția casetei în spațiul 3D. Vedeți [ Placement](Placement.md). Punctul de referință este colțul frontal din stânga al cutiei.

-    **Label**: Etichetă dată obiectului Casetă. Modificați pentru a vi se potrivi nevoilor.


</div>


{{Properties_Title|Box}}

-    **Length**:Parametrul lungime este dimensiunea Box în direcția x.

-    **Width**: Parametrul lățime este dimensiunea Box în direcția y.

-    **Height**: Parametrul înălțime este dimensiunea Box în direcția z.

![Part\_Box-Properties](images/Part_Box-Properties.jpg )


<div class="mw-translate-fuzzy">

## Scripting

Comanda Box poate fi utilizat în [macros](macros.md) și din consola python utilizând următoarea funcție:


</div>


```python
FreeCAD.ActiveDocument.addObject("Part::Box", "myBox")
```

-   Unde \"myBox\" este o denumire/etichetă pentru obiectul Box.
-   Are ca rezulta obiectul nou creat de tip Box.

Puteți accesa și modifica atributele obiectului Box. De exemplu, ați putea dori să modificați parametrii de lungime, lățime și înălțime. 
```python
FreeCAD.ActiveDocument.myBox.Length = 25
FreeCAD.ActiveDocument.myBox.Width = 15
FreeCAD.ActiveDocument.myBox.Height = 30
```

Puteți schimba amplasamentul cu: 
```python
FreeCAD.ActiveDocument.myBox.Placement = FreeCAD.Placement(FreeCAD.Vector(4, 6, 3), FreeCAD.Rotation(30, 45, 10))
```





 
