# Draft Polygon/cs
---
 GuiCommand:   Name: Draft Polygon   Name/cs: Draft Polygon   Workbenches: Draft_Workbench/cs   Kreslení, Arch_Workbench/cs|MenuLocation: Draft -> Polygon   Shortcut: P G---


</div>

## Description


<div class="mw-translate-fuzzy">

## Popis

Nástroj Mnohoúhelník vytváří pravidelný mnohoúhelník zadáním 2 bodů, střed a druhý bod definující poloměr. Použije se [tloušťka čáry a barva](Draft_Linestyle/cs.md) předem zadaná v záložce Nástrojů.


</div>

A Draft Polygon can be switched from inscribed to circumscribed by changing its **Draw Mode** property. The corners of a Draft Polygon can be filleted (rounded) or chamfered by changing its **Fillet Radius** or **Chamfer Size** respectively.

<img alt="" src=images/Draft_polygon_example.jpg  style="width:400px;">


<div class="mw-translate-fuzzy">

<img alt="" src=images/Draft_polygon_example.jpg  style="width:400px;">


</div>

## Usage

See also: [Draft Tray](Draft_Tray.md), [Draft Snap](Draft_Snap.md) and [Draft Constrain](Draft_Constrain.md).


<div class="mw-translate-fuzzy">

## Použití

1.  Stiskněte tlačítko **<img src="images/Draft_Polygon.png" width=16px> [Mnohoúhelník](Draft_Polygon/cs.md)
** nebo klávesy **P** a potom **G**
2.  Klikněte na první bod ve 3D pohledu nebo zadejte jeho souřadnice pro určení středu
3.  V dialogovém okně voleb zadejte počet stran,
4.  Klikněte na další bod ve 3D pohledu nebo zadejte hodnotu definující poloměr mnohoúhelníku. Mnohoúhelník je také povrchem, i když se jeví jako drátový model.


</div>

## Options

The single character keyboard shortcuts available in the task panel can be changed. See [Draft Preferences](Draft_Preferences.md). The shortcuts mentioned here are the default shortcuts (for version 1.0).


<div class="mw-translate-fuzzy">

## Volby

-   Pro zadání souřadnic ručně, jednoduše zadejte číslo a stiskněte **ENTER** mezi každou z komponent X, Y a Z.
-   Stiskněte klávesu **T** nebo klikněte/odklikněte zaklikávací políčko **'''Pokračovat'''**. Je-li nastaven pokračovací mód, nástroj Mnohoúhelník bude po ukončení mnohoúhelníka restartován a připraven ke kreslení dalšího mnohoúhelníka bez nutnosti znovu jej spouštět klikáním na tlačítko Mnohoúhelník.
-   Stiskněte při kreslení klávesu **CTRL** pro [přichycení](Draft_Snap/cs.md) Vašeho bodu k nejbližšímu uchopovacímu místu, nezávisle na vzdálenosti od něho.
-   Stiskněte při kreslení klávesu **SHIFT** pro nastavení [vazby](Draft_Constrain/cs.md) Vašeho dalšího bodu vodorovně nebo svisle v relaci k předchozímu bodu.
-   Stisknutím klávesy **I** nebo tlačítka **'''Filled'''** zajistíte, že se mnohoúhelník tváří jako plocha (musí být uzavřená). Jednoduše se to nastavuje Pohled-\>Vlastnost Mnohoúhelník na \"Otevřené čáry\" nebo \"Drátový model\", toto také může být snadno změněno později.
-   Stiskněte klávesu **ESC** nebo tlačítko **'''Cancel'''** pro ukončení aktuálního příkazu.


</div>

## Notes

-   A Draft Polygon can be edited with the [Draft Edit](Draft_Edit.md) command.

## Preferences

See also: [Preferences Editor](Preferences_Editor.md) and [Draft Preferences](Draft_Preferences.md).

-   If the **Edit → Preferences... → Draft → General → Create Part primitives if possible** option is checked, the command will create a [Part RegularPolygon](Part_RegularPolygon.md) instead of a Draft Polygon.




<div class="mw-translate-fuzzy">

## Vlastnosti

-    **Poloměr**: Poloměr definiční kružnice

-    **Kreslicí mód**: Specifikuje jestli je mnohoúhelník vepsaný nebo opsaný definiční kruřnici

-    **Počet stran**: Počet stran mnohoúhelníka

-    **Poloměr zaoblení**: Specifikuje poloměr zaoblení v rozích mnohoúhelníka


</div>

See also: [Property editor](Property_editor.md).

A Draft Polygon object is derived from a [Part Part2DObject](Part_Part2DObject.md) and inherits all its properties. It also has the following additional properties:

### Data


{{TitleProperty|Draft}}

-    **Area|Area**: (read-only) specifies the area of the face of the polygon. The value will be {{value|0.0}} if **Make Face** if `False`.

-    **Chamfer Size|Length**: specifies the length of the chamfers at the corners of the polygon.

-    **Draw Mode|Enumeration**: specifies if the polygon is {{value|inscribed}} in a circle or {{value|circumscribed}} around a circle.

-    **Faces Number|Integer**: specifies the number of sides of the polygon.

-    **Fillet Radius|Length**: specifies the radius of the fillets at the corners of the polygon.

-    **Make Face|Bool**: specifies if the polygon makes a face or not. If it is `True` a face is created, otherwise only the perimeter is considered part of the object.

-    **Radius|Length**: specifies the radius of the circle that defines the polygon.

### View


{{TitleProperty|Draft}}

-    **Pattern|Enumeration**: specifies the [Draft Pattern](Draft_Pattern.md) with which to fill the face of the polygon. This property only works if **Make Face** is `True` and if **Display Mode** is {{value|Flat Lines}}.

-    **Pattern Size|Float**: specifies the size of the [Draft Pattern](Draft_Pattern.md).

## Scripting


<div class="mw-translate-fuzzy">

## Skriptování

Nástroj Mnohoúhelník může být využit v [makrech](macros/cs.md) a z konzoly Pythonu použitím následující funkce:


</div>

To create a Draft Polygon use the `make_polygon` method (<small>(v0.19)</small> ) of the Draft module. This method replaces the deprecated `makePolygon` method.


```python
polygon = make_polygon(nfaces, radius=1, inscribed=True, placement=None, face=None, support=None)
```


<div class="mw-translate-fuzzy">

-   Vytvoří objekt mnohoúhelník se zadaným počtem stran a poloměrem.
-   Je-li inscribed False, mnohoúhelník je opsán kolem kružnice s daným poloměrem. Jinak je vepsán dovnitř kružnice.
-   Je-li face True, výsledný tvar je zobrazen jako povrch, jinak jako drátový model.
-   Výstupem je nově vytvořený objekt.


</div>

Příklad: 
```python
import FreeCAD as App
import Draft

doc = App.newDocument()

polygon1 = Draft.make_polygon(4, radius=500)
polygon2 = Draft.make_polygon(5, radius=750)

zaxis = App.Vector(0, 0, 1)
p3 = App.Vector(1000, 1000, 0)
place3 = App.Placement(p3, App.Rotation(zaxis, 90))

Polygon3 = Draft.make_polygon(6, radius=1450, placement=place3)

doc.recompute()
```



---
⏵ [documentation index](../README.md) > [Draft](Draft_Workbench.md) > Draft Polygon/cs
