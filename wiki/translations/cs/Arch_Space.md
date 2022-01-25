---
- GuiCommand:/cs
   Name:Arch_Space
   Name/cs:Arch Space
   MenuLocation:Architecture → Space
   Workbenches:[Architektura](Arch_Workbench/cs.md)
   Shortcut:**S** **P**
   SeeAlso:[[Arch Wall/cs]], [[Arch Structure/cs]]
   Version:0.14
---

# Arch Space/cs


</div>


<div class="mw-translate-fuzzy">

## Popis

Nástroj Prostor umožňuje definovat prázdný objem, který je buď založen na tělese nebo definován svými hranicemi nebo mixem obou postupů. Je-li založen výhradně na tělese, je objem počítán od ohraničujícího boxu ze všech daných hranic a odečtem prostoru za každou hranicí. Objekt Prostor vždy definuje objem tělesa. Podlahová plocha objektu Prostor, počítaná z průsečíku vodorovné roviny ve středu objemu prostoru, také může být zobrazen, nastavením zobrazovacího módu objektu prostoru na \"detailní\".


</div>

<img alt="" src=images/Arch_Space_example.jpg  style="width:640px;">


<div class="mw-translate-fuzzy">

*Na obrázku výše je objekt prostoru vytvořen z existujícího tělesa, potom jsou přidány dvě plochy zdi jako hranice a mód zobrazení je nasatven na \"detailní\", aby zobrazoval podlahovou plochu.*


</div>


<div class="mw-translate-fuzzy">

## Použití


</div>


<div class="mw-translate-fuzzy">

-   Vyberte existující těleso nebo plochy na hraničním objektu
-   Stiskněte tlačítko **<img src="images/Arch_Space.png" width=32px> Prostor
** nebo klávesy **S** a **P**


</div>


<div class="mw-translate-fuzzy">

## Omezení


</div>

-   The boundaries properties is currently not editable via GUI.
-   See the [forum announcement](http://forum.freecadweb.org/viewtopic.php?f=9&t=4275).

## Vlastnosti


<div class="mw-translate-fuzzy">

-    **Základ**: Základový objekt, pokud existuje (musí to být těleso)

-    **Hranice**: Seznam volitelných prvků hranic


</div>

-    **Text**: The text to show. Use \$area, \$label, \$tag, \$floor, \$walls, \$ceiling to insert the respective data

-    **FontName**: The name of the font

-    **TextColor**: The color of the text

-    **FontSize**: The size of the text

-    **FirstLine**: The size of the first line of text (multiplies the font size. 1 = same size, 2 = double size, etc..)

-    **LineSpacing**: The space between the lines of text

-    **TextPosition**: The position of the text. Leave (0,0,0) for automatic position

-    **TextAlign**: The justification of the text

-    **Decimals**: The number of decimals to use for calculated texts

-    **ShowUnit**: Show the unit suffix or not

## Options

-   To create zones that group several spaces, use a [Arch BuildingPart](Arch_BuildingPart.md) and set its IFC type to \"Spatial Zone\"
-   The space object has the same display modes as other Arch and Part objects, with one more, called **Footprint**, that displays only the bottom face of the space. <small>(v0.19)</small> 


<div class="mw-translate-fuzzy">

## Skriptování


</div>


<div class="mw-translate-fuzzy">

Nástroj Prostor může být použit ve skriptech Pythonu a v [makrech](macros/cs.md) použitím následující funkce:


</div>


```python
Space = makeSpace(objects=None, baseobj=None, name="Space")
```


<div class="mw-translate-fuzzy">

-   Vytvoří objekt prostoru ze zadaných objektů.
-   Objekty mohou být jeden dokument objektu, v tomto případě se objekt stane základovým objektem prostoru nebo seznam vvybraných objektů jako návratová hodnota funkce FreeCADGui.Selection.getSelectionEx(), nebo seznam dvojic (objekt, jméno subobjektu).
-   Vrací nově vytvořený objekt prostoru.


</div>

Příklad: 
```python
import FreeCAD, Arch

Box = FreeCAD.ActiveDocument.addObject("Part::Box", "Box")
Box.Length = 1000
Box.Width = 1000
Box.Height = 1000

Space = Arch.makeSpace(Box)
Space.ViewObject.LineWidth = 2
FreeCAD.ActiveDocument.recompute()
```

After a space object is created, selected faces can be added to it with the following code: 
```python
import FreeCAD, FreeCADGui, Draft, Arch

points = [FreeCAD.Vector(-500, 0, 0), FreeCAD.Vector(1000, 1000, 0)]
Line = Draft.makeWire(points)
Wall = Arch.makeWall(Line, width=150, height=2000)
FreeCAD.ActiveDocument.recompute()

# Select a face of the wall
selection = FreeCADGui.Selection.getSelectionEx()
Arch.addSpaceBoundaries(Space, selection)
```

Boundaries can also be removed, again by selecting the indicated faces: 
```python
selection = FreeCADGui.Selection.getSelectionEx()
Arch.removeSpaceBoundaries(Space, selection)
```


<div class="mw-translate-fuzzy">


{{docnav/cs|[Roof](Arch_Roof/cs.md)|[Stairs](Arch_Stairs/cs.md)|[Arch](Arch_Workbench/cs.md)|IconL=Arch_Roof.svg |IconC=Workbench_Arch.svg |IconR=Arch_Stairs.svg}}


</div>



---
![](images/Right_arrow.png) [documentation index](../README.md) > [Arch](Arch_Workbench.md) > Arch Space/cs
