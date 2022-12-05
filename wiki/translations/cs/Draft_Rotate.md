# Draft Rotate/cs
---
- GuiCommand:/cs   Name:Draft Rotate   Name/cs:Kreslení Otočit   Workbenches:[Architektura](Draft_Workbench/cs___Kreslení]],_[[Arch_Workbench/cs.md)|MenuLocation:Kreslení → Otočit   Shortcut:R O---


</div>

## Popis


<div class="mw-translate-fuzzy">

Nástroj Otočit otáčí nebo kopíruje vybrané objekty o zadaný úhel kolem bodu v aktuální [pracovní rovině](Draft_SelectPlane/cs.md). Není-li vybrán žádný objekt, budete vyzváni k výběru objektu.


</div>

The command can be used on 2D objects created with the [Draft Workbench](Draft_Workbench.md) or [Sketcher Workbench](Sketcher_Workbench.md), but also on many 3D objects such as those created with the [Part Workbench](Part_Workbench.md), [PartDesign Workbench](PartDesign_Workbench.md) or [Arch Workbench](Arch_Workbench.md).

<img alt="" src=images/Draft_Rotate_example.jpg  style="width:400px;"> 
*Rotating an object around a center point*


<div class="mw-translate-fuzzy">

## Použití


</div>

See also: [Draft Snap](Draft_Snap.md) and [Draft Constrain](Draft_Constrain.md).


<div class="mw-translate-fuzzy">

1.  Vyberte objekt, který chcete otočit nebo zkopírovat
2.  Stiskněte tlačítko **<img src="images/Draft_Rotate.png" width=16px> [Kreslení Otočit](Draft_Rotate/cs.md)
** nebo klávesy **R** potom **O**
3.  Klikněte na střed ve 3D pohledu nebo zadejte souřadnice
4.  Klikněte na druhý bod ve 3D pohledu nebo zadejte referenční úhel
5.  Klikněte na třetí bod ve 3D pohledu nebo zadejte úhel otočení


</div>

## Volby

The single character keyboard shortcuts and the modifier key mentioned here can be changed. See [Draft Preferences](Draft_Preferences.md).


<div class="mw-translate-fuzzy">

-   Stiskněte klávesu **X**, **Y** nebo **Z** po prvním bodu pokud chcete uplatnit vazbu dalšího bodu v příslušné ose.
-   Chcete-li zadat souřadnice ručně jednoduše zadejte číslo a potom stiskněte **ENTER** mezi každou z komponent X, Y a Z.
-   Stiskněte klávesu **T** nebo zaklikněte/odklikněte políčko **'''Pokračovat'''**. Je-li nastaven pokračovací mód, bude nástroj Otočit hned po ukončení připraven k otočení nebo kopírování bez nutnosti stisknout znovu tlačítko Otočit.
-   Stisknutí klávesy **ALT** nebo **C** nebo kliknutí na tlačítko **'''Kopie'''** vytvoří kopii objektu místo jeho otočení. Podržíte-li stisknutou klávesu **ALT** po kliknutí na druhý bod, budete moci umístit několik kopií, až dokud neuvolníte klávesu **ALT**.
-   Stisknutím klávesy **CTRL** během kreslení vynutíte [přichycení](Draft_Snap/cs.md) vašeho bodu k nejbližšímu uchopovacímu místu nezávisle na vzálenosti od něho.
-   Stisknutím klávesy **SHIFT** během kreslení [nastavíte vazbu](Draft_Constrain/cs.md) vašeho bodu svisle nebo vodorovně v relaci předchozímu bodu.
-   Stisknutím tlačítka **ESC** nebo **'''Zrušit'''** zrušíte právě probíhající příkaz.


</div>

## Notes

-   An Object that is [attached](Part_EditAttachment.md) cannot be rotated with the Draft Rotate command. To rotate it either its **Support** object has to be rotated, or its **Attachment Offset** has to be changed.

## Preferences

See also: [Preferences Editor](Preferences_Editor.md) and [Draft Preferences](Draft_Preferences.md).

-   To change the number of decimals used for the input of coordinates and angles: **Edit → Preferences... → General → Units → Units settings → Number of decimals**.
-   To store and reuse the same copy mode setting across commands: **Edit → Preferences... → Draft → General settings → Draft tools options → Global copy mode**.
-   To reselect the base objects after copying objects: **Edit → Preferences... → Draft → General settings → Draft tools options → Select base objects after copying**.

## Scripting


<div class="mw-translate-fuzzy">

## Skriptování


</div>


<div class="mw-translate-fuzzy">

Nástroj Otočit může být využit v [makrech](macros/cs.md) a z konzoly Pythonu použitím následující funkce:


</div>


```python
rotated_list = rotate(objectslist, angle, center=Vector(0,0,0), axis=Vector(0,0,1), copy=False)
```


<div class="mw-translate-fuzzy">

-   Otočí zadaný objekt nebo objekty obsažené v zadaném seznamum (list) o daný úhel (angle) kolem středu (je-li zadán) s použitím osy jako osy rotace.
-   Chybí-li osa (axis), bude otočení provedeno podle svislé osy Z.
-   Je-li copymode True, aktuální objekty se nepohnou, ale místo toho jsou vytvořeny jejich kopie.
-   Vrací objekty (nebo jejich kopie, pokud bylo copymode True).


</div>

Příklad:


```python
import FreeCAD as App
import Draft

doc = App.newDocument()

polygon1 = Draft.make_polygon(3, radius=300)
Draft.move(polygon1, App.Vector(1000, 0, 0))

# Rotation around the origin
angle1 = 45
rot2 = Draft.rotate(polygon1, angle1, copy=True)
rot3 = Draft.rotate(polygon1, 2*angle1, copy=True)
rot4 = Draft.rotate(polygon1, 4*angle1, copy=True)

polygon2 = Draft.make_polygon(3, radius=1000)
polygon3 = Draft.make_polygon(5, radius=500)
Draft.move(polygon2, App.Vector(2000, 0, 0))
Draft.move(polygon3, App.Vector(2000, 0, 0))

# Rotation around another point
angle2 = 60
cen = App.Vector(3100, 0, 0)
list2 = [polygon2, polygon3]
rot_list2 = Draft.rotate(list2, angle2, center=cen, copy=True)
rot_list3 = Draft.rotate(list2, 2*angle2, center=cen, copy=True)
rot_list4 = Draft.rotate(list2, 4*angle2, center=cen, copy=True)

doc.recompute()
```



---
![](images/Right_arrow.png) [documentation index](../README.md) > [Draft](Draft_Workbench.md) > Draft Rotate/cs
