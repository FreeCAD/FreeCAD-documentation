---
- GuiCommand:/ro
   Name:Draft Scale
   Name/ro:Draft Scale
   MenuLocation:Draft → Scale
   Workbenches:[Draft](Draft_Workbench/ro.md), [Arch](Arch_Workbench/ro.md)
   Shortcut:**S** **C**
   SeeAlso:[Draft Clone](Draft_Clone/ro.md)
---

# Draft Scale/ro


</div>

## Descriere


<div class="mw-translate-fuzzy">

Acest instrument mărește/micșorează la scară obiectele selectate în jurul unui punct de bază. Dacă nu este selectat niciun obiect, veți fi invitat să selectați unul.


</div>

The command can be used on 2D objects created with the [Draft Workbench](Draft_Workbench.md) or [Sketcher Workbench](Sketcher_Workbench.md), but also on many 3D objects such as those created with the [Part Workbench](Part_Workbench.md), [PartDesign Workbench](PartDesign_Workbench.md) or [Arch Workbench](Arch_Workbench.md).

<img alt="" src=images/Draft_Scale_example.png  style="width:400px;"> 
*Scaling an object around a base point*

## Cum se folosește 

See also: [Draft Snap](Draft_Snap.md) and [Draft Constrain](Draft_Constrain.md).


<div class="mw-translate-fuzzy">

1.  Selectați obiectele pe care doriți să le modificați
2.  Apăsați butonul **<img src="images/Draft_Scale.png" width=16px> [[Draft Scale]]
** sau apăsați {{KEY | S}} apoi tasta **C**
3.  Faceți clic pe un prim punct al vizualizării 3D sau introduceți un coordinate pentru a defini punctul de bază al scalei
4.  Se deschide un alt dialog cu opțiunile de scalare. Completați diferitele opțiuni și apăsați pe {{KEY | OK}} pentru a accepta


</div>

## Opţiuni

### First task panel 

The single character keyboard shortcuts mentioned here can be changed. See [Draft Preferences](Draft_Preferences.md).

-   To manually enter the coordinates for the base point enter the X, Y and Z component, and press **Enter** after each. Or you can press the **<img src="images/Draft_AddPoint.svg" width=16px> Enter point** button when you have the desired values. It is advisable to move the pointer out of the [3D view](3D_view.md) before entering coordinates.
-   Press **G** or click the **Global** checkbox to toggle global mode. If global mode is on, coordinates are relative to the global coordinate system, else they are relative to the [working plane](Draft_SelectPlane.md) coordinate system. <small>(v0.20)</small> 
-   The other checkboxes in this task panel, displayed in FreeCAD version 0.19 and earlier, are ignored by the command.
-   Press **S** to switch [Draft snapping](Draft_Snap.md) on or off.
-   Press the **Close** button to abort the command.

### Second task panel 


<div class="mw-translate-fuzzy">

-   Pentru a introduce manual coordonatele punctului de bază, pur și simplu introduceți numerele, apoi apăsați {{KEY | ENTER}} între fiecare componentă X, Y și Z.
-   Completați valoarea de scalare X, Y și Z pentru a defini scalarea.
-   Verificarea opțiunii \"Scalare uniformă\" va bloca X, Y și Z la aceeași valoare
-   Opțiunea \"Relativ la planul de lucru\" va lua în considerare valorile de scalare X, Y și Z de-a lungul curentului [Working Plane](Draft_SelectPlane.md). În caz contrar, se utilizează indicațiile globale X, Y și Z.
-   Rezultatul operației de scalare poate fi:
    -   A [Draft Clone](Draft_Clone.md) a obiectelor originale, care nu modifică obiectele originale, dar vă permit să modificați manual factorul de scalare mai târziu (funcționează pentru toate tipurile de obiecte)
    -   Obiectele originale au modificat dimensiunea lor (vor funcționa numai cu obiecte proiectate sau cu forme neparametrice)
    -   Se produce o copie scalată a obiectelor de bază (va funcționa pentru toate tipurile de obiecte, dar numai copii ale obiectelor Draft vor fi parametrice)


</div>

## Notes

-   The command can also scale [Image Planes](Image_CreateImagePlane.md), but not in clone mode.

## Preferences

See also: [Preferences Editor](Preferences_Editor.md) and [Draft Preferences](Draft_Preferences.md).

-   To change the number of decimals used for the input of scale factors (<small>(v0.20)</small> ) and coordinates: **Edit → Preferences... → General → Units → Units settings → Number of decimals**.
-   To change the number of decimals used for the input of scale factors ({{VersionMinus|0.19}}): **Edit → Preferences... → Draft → General settings → General Draft Settings → Internal precision level**.
-   To reselect the base objects after copying objects: **Edit → Preferences... → Draft → General settings → Draft tools options → Select base objects after copying**.

## Scripting


<div class="mw-translate-fuzzy">

## Scrip-Programare 


</div>


<div class="mw-translate-fuzzy">

Instrumentul Scale poate fi utilizat în [macros](macros.md) și de la consola python utilizând următoarele funcții:


</div>


```python
scaled_list = scale(objectslist, scale=Vector(1,1,1), center=Vector(0,0,0), copy=False)
```


<div class="mw-translate-fuzzy">

-   Scalarea obiectelor conținute în alte obiecte (care poate fi o listă de obiecte sau un obiect) a factorilor scalei date definite de vectorul dat (în direcțiile X, Y și Z) în jurul centrului dat.
-   Dacă moștenirea este adevărată, se utilizează modul direct (vechi), în caz contrar se face o copiere parametrică.
-   Dacă copia este Adevărată, obiectele reale nu sunt mutate, dar sunt create copii.
-   Obiectele (sau copiile lor) sunt returnate.


</div>

Exempluː


```python
import FreeCAD as App
import Draft

doc = App.newDocument()

pts = [App.Vector(0, 0, 0), App.Vector(500, 500, 0), App.Vector(600, 0, 0)]
wire1 = Draft.make_wire(pts, closed=True)
doc.recompute()

scale1 = App.Vector(2.3, 0.75, 0)
wire2 = Draft.scale(wire1, scale1, copy=True)
doc.recompute()

scale2 = App.Vector(-2, -1.5, 0)
wires = Draft.scale([wire1, wire2], scale2, copy=True)
doc.recompute()
```



---
![](images/Right_arrow.png) [documentation index](../README.md) > [Draft](Draft_Workbench.md) > Draft Scale/ro
