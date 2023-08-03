# Draft Move/cs
---
 GuiCommand:   Name: Draft_Move   Name/cs: Kreslení Posun   Workbenches: Draft_Workbench/cs   Kreslení, Arch_Workbench/cs|MenuLocation: Draft -> Move   Shortcut: M V---


</div>

## Popis


<div class="mw-translate-fuzzy">

Nástroj Posun posunuje nebo kopíruje vybrané objekty z jednoho bodu do druhého v aktuální [pracovní rovině](Draft_SelectPlane/cs.md). Není-li vybrán žádný objekt, budete vyzváni k výběru objektu.


</div>

The command can be used on 2D objects created with the [Draft Workbench](Draft_Workbench.md) or [Sketcher Workbench](Sketcher_Workbench.md), but also on many 3D objects such as those created with the [Part Workbench](Part_Workbench.md), [PartDesign Workbench](PartDesign_Workbench.md) or [Arch Workbench](Arch_Workbench.md).

<img alt="" src=images/Draft_Move_example.jpg  style="width:400px;"> 
*Moving an object from one point to another*

## Použití

See also: [Draft Snap](Draft_Snap.md) and [Draft Constrain](Draft_Constrain.md).


<div class="mw-translate-fuzzy">

1.  Vyberte objekty, které chcete posunout nebo zkopírovat
2.  Stiskněte tlačítko **<img src="images/Draft_Move.png" width=16px> [Posun](Draft_Move/cs.md)
** nebo klávesy **M** a potom **V**
3.  Klikněte na první bod ve 3D pohledu nebo zadejte souřadnice
4.  Klikněte na další bod ve 3D pohledu nebo zadejte souřadnice.


</div>

## Volby

The single character keyboard shortcuts mentioned here can be changed. See [Draft Preferences](Draft_Preferences.md).


<div class="mw-translate-fuzzy">

-   Stiskněte klávesu **X**, **Y** nebo **Z** po prvním bodu pokud chcete uplatnit vazbu dalšího bodu v příslušné ose.
-   Chcete-li zadat souřadnice ručně jednoduše zadejte číslo a potom stiskněte **ENTER** mezi každou z komponent X, Y a Z.
-   Stiskněte klávesu **R** nebo zaklikněte/odklikněte políčko **'''Relativně'''**. Je-li zapnut relativní mód, budou souřadnice dalšího bodu relativní k předchozímu bodu. Pokud ne, bodou souřadnice absolutní, tj. k počátečnímu bodu (0,0,0).
-   Stiskněte klávesu **T** nebo zaklikněte/odklikněte políčko **'''Pokračovat'''**. Je-li nastaven pokračovací mód, bude nástroj Posun hned po ukončení připraven k posunutí nebo kopírování bez nutnosti stisknout znovu tlačítko Posun.
-   Stisknutí klávesy **ALT** nebo **C** nebo kliknutí na tlačítko **'''Kopie'''** vytvoří kopii objektu místo jeho posunutí. Podržíte-li stisknutou klávesu **ALT** po kliknutí na druhý bod, budete moci umístit několik kopií, až dokud neuvolníte klávesu **ALT**.
-   Stisknutím klávesy **CTRL** během kreslení vynutíte [přichycení](Draft_Snap/cs.md) vašeho bodu k nejbližšímu uchopovacímu místu nezávisle na vzálenosti od něho.
-   Stisknutím klávesy **SHIFT** během kreslení [nastavíte vazbu](Draft_Constrain/cs.md) vašeho bodu svisle nebo vodorovně v relaci předchozímu bodu.
-   Stisknutím tlačítka **ESC** nebo **'''Zrušit'''** zrušíte právě probíhající příkaz.


</div>

## Notes

-   An Object that is [attached](Part_EditAttachment.md) cannot be moved with the Draft Move command. To move it either its **Support** object has to be moved, or its **Attachment Offset** has to be changed.

## Preferences

See also: [Preferences Editor](Preferences_Editor.md) and [Draft Preferences](Draft_Preferences.md).

-   To change the number of decimals used for the input of coordinates, lengths and angles: **Edit → Preferences... → General → Units → Units settings → Number of decimals**.
-   To change the initial focus of the task panel to the **Length** input box: **Edit → Preferences... → Draft → General settings → Draft tools options → Set focus on Length instead of X coordinate**. Note that you must move the pointer in the [3D view](3D_view.md) for the change to take effect.
-   To store and reuse the same copy mode setting across commands: **Edit → Preferences... → Draft → General settings → Draft tools options → Global copy mode**.
-   To reselect the base objects after copying objects: **Edit → Preferences... → Draft → General settings → Draft tools options → Select base objects after copying**.

## Scripting


<div class="mw-translate-fuzzy">

## Skriptování


</div>


<div class="mw-translate-fuzzy">

Nástroj Posun může být využit v [makrech](macros/cs.md) a z konzoly Pythonu použitím následující funkce:


</div>


```python
moved_list = move(objectslist, vector, copy=False)
```


<div class="mw-translate-fuzzy">

-   Posune objekt nebo objekty obsažené v zadaném seznamu (list) ve směru a do vzdálenosti dané parametrem Vector.
-   Je-li copymode True, nebudou vybrané objety posunuty, ale zkopírovány. Vrací objekt(y) (nebo jejich kopie, je-li copymode True).
-   Je vrácen seznam posunutých objektů (resp. zkopírovaných).


</div>

Příklad:


```python
import FreeCAD as App
import Draft

doc = App.newDocument()

polygon1 = Draft.make_polygon(5, radius=1000)
polygon2 = Draft.make_polygon(3, radius=500)
polygon3 = Draft.make_polygon(6, radius=220)

Draft.move(polygon1, App.Vector(500, 500, 0))
Draft.move(polygon1, App.Vector(500, 500, 0))
Draft.move(polygon2, App.Vector(1000, -1000, 0))
Draft.move(polygon3, App.Vector(-500, -500, 0))

list1 = [polygon1, polygon2, polygon3]

vector = App.Vector(-2000, -2000, 0)
list2 = Draft.move(list1, vector, copy=True)
list3 = Draft.move(list1, -2*vector, copy=True)

doc.recompute()
```



---
⏵ [documentation index](../README.md) > [Draft](Draft_Workbench.md) > Draft Move/cs
