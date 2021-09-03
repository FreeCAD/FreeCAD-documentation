---
- GuiCommand:/cs   Name:Draft Offset   Name/cs:Kreslení Odsadit   Workbenches:[Architektura](Draft_Workbench/cs___Kreslení]],_[[Arch_Workbench/cs.md)|MenuLocation:Draft → Offset   Shortcut:O S   SeeAlso:[Part 2D Offset](Part_Offset2D/cs.md)---


</div>

## Popis


<div class="mw-translate-fuzzy">

Nástroj Odsadit odsadí vybrané objekty o zadanou vzdálenost v aktuální [pracovní rovině](Draft_SelectPlane/cs.md). Není-li vybrán žádný objekt, budete vyzváni k výběru objektu.


</div>

<img alt="" src=images/Draft_Offset_example.jpg  style="width:400px;"> 
*Offsetting a Draft Wire*


<div class="mw-translate-fuzzy">

## Použití


</div>

See also: [Draft Snap](Draft_Snap.md) and [Draft Constrain](Draft_Constrain.md).


<div class="mw-translate-fuzzy">

1.  Vyberte objekty, které chcete odsadit
2.  Stiskněte tlačítko **<img src="images/Draft_Offset.png" width=16px> [Kreslení Odsadit](Draft_Offset/cs.md)
** nebo klávesy **O** a potom **S**
3.  Klikněte na bod ve 3D pohledu nebo zadejte vzálenost.


</div>

## Volby

The single character keyboard shortcuts and the modifier keys mentioned here can be changed. See [Draft Preferences](Draft_Preferences.md).


<div class="mw-translate-fuzzy">

-   Stiskněte klávesu **T** nebo zaklikněte/odklikněte políčko **'''Pokračovat'''**. Je-li nastaven pokračovací mód, bude nástroj Odsadit hned po ukončení připraven k odsazení nebo kopírování bez nutnosti stisknout znovu tlačítko Odsadit.
-   Stisknutí klávesy **ALT** nebo **C** nebo kliknutí na tlačítko **'''Kopie'''** vytvoří kopii objektu místo jeho odsazení. Podržíte-li stisknutou klávesu **ALT** po kliknutí na druhý bod, budete moci umístit několik kopií, až dokud neuvolníte klávesu **ALT**.
-   Stisknutím klávesy **CTRL** během kreslení vynutíte [přichycení](Draft_Snap/cs.md) vašeho bodu k nejbližšímu uchopovacímu místu nezávisle na vzálenosti od něho.
-   Stisknutím klávesy **SHIFT** během kreslení [nastavíte vazbu](Draft_Constrain/cs.md) na aktuální segment místo výběru nejbližšího.
-   Stisknutím tlačítka **ESC** nebo **'''Cancel'''** zrušíte právě probíhající příkaz.


</div>

## Notes

-   To create an offset version of a [Draft BSpline](Draft_BSpline.md) its points are offset individually, and from the new points a new spline is calculated. This new spline is not parallel to the original spline. For an exact parallel offset of a [Draft BSpline](Draft_BSpline.md) the [Part Offset2D](Part_Offset2D.md) command should be used.
-   The Draft Offset command cannot handle [Draft BezCurves](Draft_BezCurve.md). Use the [Part Offset2D](Part_Offset2D.md) command instead.

## Preferences

See also: [Preferences Editor](Preferences_Editor.md) and [Draft Preferences](Draft_Preferences.md).

-   To change the number of decimals used for the input of the distance: **Edit → Preferences... → General → Units → Units settings → Number of decimals**.

## Scripting


<div class="mw-translate-fuzzy">

## Skriptování


</div>


<div class="mw-translate-fuzzy">

Nástroj Odsadit může být využit v [makrech](macros/cs.md) a z konzoly Pythonu použitím následující funkce:


</div>


```python
offset_obj = offset(obj, delta, copy=False, bind=False, sym=False, occ=False)
```


<div class="mw-translate-fuzzy">

-   Odsadí zadaný drát aplikací údajů z Vectoru na první vrchol drátu .
-   Je-li copymode True, je vytvořen další objekt, jinak je odsunut původní objekt.
-   Je-li bind True a zadaný drát je otevřený, původní a odsunutý drát budou spojeny koncovými body a vytvoří plochu.
-   Je-li sym True, je odsunutí provedeno symetricky na obou stranách s celkovou šířkou rovnou délce zadaného vektoru.
-   Vrací odsunutý objekt (nebo jeho kopii, je-li copymode True).


</div>

Příklad:


```python
import FreeCAD as App
import Draft

doc = App.newDocument()

p1 = App.Vector(0, 0, 0)
p2 = App.Vector(1500, 2000, 0)
p3 = App.Vector(4000, 0, 0)

wire = Draft.make_wire([p1, p2, p3])
doc.recompute()

vector = App.Vector(-200, 150, 0)
offset1 = Draft.offset(wire, vector, copy=True, bind=True, sym=True)
offset2 = Draft.offset(wire, 3*vector, copy=True)
offset3 = Draft.offset(wire, 6*vector, copy=True)
offset4 = Draft.offset(wire, 9*vector, copy=True)
offset5 = Draft.offset(wire, 1.5*vector, copy=True, occ=True)

doc.recompute()
```





 
