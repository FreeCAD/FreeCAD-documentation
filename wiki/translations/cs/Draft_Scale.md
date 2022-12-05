# Draft Scale/cs
---
- GuiCommand:/cs   Name:Draft Scale   Name/cs:Kreslení Roztáhnout   Workbenches:[Architektura](Draft_Workbench/cs___Kreslení]],_[[Arch_Workbench/cs.md)|MenuLocation:Kreslení → Roztáhnout   Shortcut:S C   SeeAlso:[Kreslení Klon](Draft_Clone/cs.md)---


</div>

## Popis


<div class="mw-translate-fuzzy">

Tento nástroj roztáhne rozměry objektů vzhledem k základnímu bodu. Není-li vybrán žádný objekt, budete vyzváni k jeho výběru. Nástroj také může být využit k zrcadlení objektů.


</div>

The command can be used on 2D objects created with the [Draft Workbench](Draft_Workbench.md) or [Sketcher Workbench](Sketcher_Workbench.md), but also on many 3D objects such as those created with the [Part Workbench](Part_Workbench.md), [PartDesign Workbench](PartDesign_Workbench.md) or [Arch Workbench](Arch_Workbench.md).

<img alt="" src=images/Draft_Scale_example.png  style="width:400px;"> 
*Scaling an object around a base point*

## Použití

See also: [Draft Snap](Draft_Snap.md) and [Draft Constrain](Draft_Constrain.md).


<div class="mw-translate-fuzzy">

1.  Vyberte objekt, který chcete roztáhnout
2.  Stiskněte tlačítko **<img src="images/Draft_Scale.png" width=16px> [Kreslení Roztáhnout](Draft_Scale/cs.md)
** nebo klávesy **S** potom **C**
3.  Klikněte na první bod ve 3D pohledu nebo zadejte souřadnice
4.  Klikněte na druhý bod ve 3D pohledu nebo zadejte souřadnice


</div>

## Volby

### First task panel 

The single character keyboard shortcuts mentioned here can be changed. See [Draft Preferences](Draft_Preferences.md).

-   To manually enter the coordinates for the base point enter the X, Y and Z component, and press **Enter** after each. Or you can press the **<img src="images/Draft_AddPoint.svg" width=16px> Enter point** button when you have the desired values. It is advisable to move the pointer out of the [3D view](3D_view.md) before entering coordinates.
-   Press **G** or click the **Global** checkbox to toggle global mode. If global mode is on, coordinates are relative to the global coordinate system, else they are relative to the [working plane](Draft_SelectPlane.md) coordinate system. <small>(v0.20)</small> 
-   Press **S** to switch [Draft snapping](Draft_Snap.md) on or off.
-   Press the **Close** button to abort the command.

### Second task panel 


<div class="mw-translate-fuzzy">

-   Chcete-li zadat souřadnice ručně jednoduše zadejte číslo a potom stiskněte **ENTER** mezi každou z komponent X, Y a Z.
-   Komponenty x, y and z druhého bodu definují faktor roztažení. Například, (1,1,1) neudělá nic, (2,2,2) roztáhne objekt 2x ve všech směrech, (-1,1,1) zrcadlí objekt ve směru x.
-   Stisknutí klávesy **ALT** nebo **C** nebo kliknutí na tlačítko **'''Kopie'''** vytvoří kopii objektu místo jeho roztažení. Podržíte-li stisknutou klávesu **ALT** po kliknutí na druhý bod, budete moci umístit několik kopií, až dokud neuvolníte klávesu **ALT**.
-   Stisknutím klávesy **CTRL** během kreslení vynutíte [přichycení](Draft_Snap/cs.md) vašeho bodu k nejbližšímu uchopovacímu místu nezávisle na vzálenosti od něho.
-   Stisknutí klávesy **SHIFT** uzamkne společně hodnoty x a y, takže tvar není deformován.
-   Stisknutím tlačítka **ESC** nebo **'''Zrušit'''** zrušíte právě probíhající příkaz.
-   Výsledný objekt je [klon](Draft_Clone/cs.md), což umožňuje měnit hodnotu roztažení po tom co byl objekt vytvořen.
-   Zrcadlení objektů je založeno na otočení znaménka v jednom ze směrů. Například, (-1,1,1) zrcadlí vodorovně (podle osy X) a (1,-1,1) svisle (podle osy Y).


</div>

## Notes

-   The command can also scale [Image Planes](Image_CreateImagePlane.md), but not in clone mode.

## Preferences

See also: [Preferences Editor](Preferences_Editor.md) and [Draft Preferences](Draft_Preferences.md).

-   To change the number of decimals used for the input of scale factors (<small>(v0.20)</small> ) and coordinates: **Edit → Preferences... → General → Units → Units settings → Number of decimals**.
-   To reselect the base objects after copying objects: **Edit → Preferences... → Draft → General settings → Draft tools options → Select base objects after copying**.

## Scripting


<div class="mw-translate-fuzzy">

## Skriptování


</div>


<div class="mw-translate-fuzzy">

Nástroj Roztáhnout může být využit v [makrech](macros/cs.md) a z konzoly Pythonu použitím následující funkce:


</div>


```python
scaled_list = scale(objectslist, scale=Vector(1,1,1), center=Vector(0,0,0), copy=False)
```


<div class="mw-translate-fuzzy">

-   Roztáhne objekty obsažené v objects (může to být objekt nebo seznam objektů) podle zadaného faktoru roztažení definovaného vektorem (ve směrech X, Y a Z) kolem zadaného středu.
-   Je-li legacy True, je použit (zastaralý) mód direct, jinak je provedena parametrická kopie.
-   Je-li copy True, aktuální objekty se nepohnou, ale místo toho jsou vytvořeny nové kopie.
-   Jsou vráceny objekty (nebo jejich kopie).


</div>

Příklad:


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
![](images/Right_arrow.png) [documentation index](../README.md) > [Draft](Draft_Workbench.md) > Draft Scale/cs
