---
 GuiCommand:
   Name: Arch Space   Name/ro: Arch
   MenuLocation: Arch , Space
   Workbenches: Arch_Workbench/ro
   Shortcut: **S** **P**
   SeeAlso: Arch Wall, Arch Structure
   Version: 0.14
---

# Arch Space/ro


</div>

## Description


<div class="mw-translate-fuzzy">

## Descriere

Instrumentul Spațiu vă permite să definiți un volum gol, fie bazându-l pe o formă solidă, fie prin definirea limitelor sale sau printr-un amestec de ambele. Dacă se bazează numai pe limite, volumul se calculează pornind de la caseta delimitată a tuturor limitelor date și scăzând spațiile din spatele fiecărei limite. Obiectul spațial definește întotdeauna un volum solid. Suprafața podelei unui obiect spațial, calculată prin intersecția unui plan orizontal cu centrul de masă al volumului spațiului, poate fi de asemenea afișată, prin setarea modului de afișare a obiectului spațial la \"detaliat\".


</div>

<img alt="" src=images/Arch_Space_example.jpg  style="width:640px;">


<div class="mw-translate-fuzzy">

*În imaginea de mai sus, un obiect spațial este creat dintr-un obiect solid existent, apoi două fețe de perete sunt adăugate ca granițe, iar modul de afișare este setat la \"detaliat\" pentru a afișa suprafața podelei.*


</div>




<div class="mw-translate-fuzzy">

## Cum se folosește 


</div>


<div class="mw-translate-fuzzy">

1.  Selectați un obiect solid existent sau se confruntă cu obiecte de frontieră
2.  Apăsați butonul **<img src="images/Arch_Space.png" width=16px> [[Arch Space]]
**, sau apăsați tastele **S**, **P**


</div>




<div class="mw-translate-fuzzy">

## Limite


</div>


<div class="mw-translate-fuzzy">

-   Este disponibil doar pentru versiunile mai recente decât FreeCAD version 0.14
-   Proprietățile Limitelor sunt ne-editabile via Gui, deocamdată
-   A se vedea [forum announcement](http://forum.freecadweb.org/viewtopic.php?f=9&t=4275)


</div>



## Proprietăți


<div class="mw-translate-fuzzy">

-    **Base**: Baza obiectului, dacă există una(Trebuie să fie un solid)

-    **Boundaries**: O listă a elementelor opționale de limită


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

-   To create zones that group several spaces, use an [Arch BuildingPart](Arch_BuildingPart.md) and set its IFC type to \"Spatial Zone\".
-   The Space object has the same display modes as other Arch and Part objects, with one more, called **Footprint**, that displays only the bottom face of the space.

## Scripting


<div class="mw-translate-fuzzy">

## Scrip-Programare 


</div>


<div class="mw-translate-fuzzy">

Instrumentul Space poate fi folosit în scripturile python și [macros](macros.md) utilizând următoarea funcție:


</div>


```python
Space = makeSpace(objects=None, baseobj=None, name="Space")
```


<div class="mw-translate-fuzzy">

-   Creează un obiect Spațiu din obiectele date.
-   Obiectele pot fi un obiect tip document, caz în care devine forma de bază a obiectului Spațiu sau o listă de obiecte selecate și returnate de comanda FreeCADGui.Selection.getSelectionEx () sau o listă de tuple (obiect, subobiectnume).
-   Returnează un obiect Sapțiu nou creat.


</div>

Exempluː


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


<div class="mw-translate-fuzzy">

După crearea unui obiect spațial, fațetele selectate pot fi adăugate la acesta cu următoarea funcție:


</div>


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


<div class="mw-translate-fuzzy">

De asemenea, limitele pot fi eliminate cu:


</div>


```python
selection = FreeCADGui.Selection.getSelectionEx()
Arch.removeSpaceBoundaries(Space, selection)
```


<div class="mw-translate-fuzzy">


{{docnav/ro
|[Roof/ro](Arch_Roof/ro.md)
|[Stairs/ro](Arch_Stairs/ro.md)
|[Arch/ro](Arch_Workbench/ro.md)
|IconL=Arch_Roof.svg
|IconC=Workbench_Arch.svg
|IconR=Arch_Stairs.svg
}}


</div>



---
⏵ [documentation index](../README.md) > [Arch](Arch_Workbench.md) > Arch Space/ro
