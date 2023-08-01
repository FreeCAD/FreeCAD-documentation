# Draft Rectangle/cs
---
- GuiCommand:/cs   Name:Draft Rectangle   Name/cs:Draft Rectangle   Workbenches:[Architecture](Draft_Workbench/cs___Kreslení]],_[[Arch_Workbench/cs.md)|MenuLocation:Draft -> Rectangle   Shortcut:R E   SeeAlso:[Part Box](Part_Box/cs.md)---


</div>

## Description


<div class="mw-translate-fuzzy">

## Popis

Nástroj Obdélník vytváří obdélník zadáním dvou protějších bodů. Použije se [tloušťka čáry a barva](Draft_Linestyle/cs.md) předem zadaná v záložce Nástrojů.


</div>

The corners of a Draft Rectangle can be filleted (rounded) or chamfered by changing its **Fillet Radius** or **Chamfer Size** respectively. It is also possible to subdivide a Draft Rectangle by changing its **Columns** and/or **Rows** property.

<img alt="" src=images/Draft_Rectangle_example.jpg  style="width:400px;">


<div class="mw-translate-fuzzy">

<img alt="" src=images/Draft_Rectangle_example.jpg  style="width:400px;">


</div>

## Usage

See also: [Draft Tray](Draft_Tray.md), [Draft Snap](Draft_Snap.md) and [Draft Constrain](Draft_Constrain.md).


<div class="mw-translate-fuzzy">

## Použití

1.  Stiskněte tlačítko **<img src="images/Draft_Rectangle.png" width=16px> [Obdélník](Draft_Rectangle/cs.md)
** nebo klávesy **R** a potom **E**
2.  Klikněte na první roh ve 3D pohledu nebo zadejte souřadnice
3.  Klikněte na protější bod ve 3D pohledu nebo zadejte souřadnice. Obdélník je také povrchem, i když se jeví jako drátový model.


</div>

## Options

The single character keyboard shortcuts available in the task panel can be changed. See [Draft Preferences](Draft_Preferences.md). The shortcuts mentioned here are the default shortcuts.


<div class="mw-translate-fuzzy">

## Volby

-   Stiskněte **X**, **Y** nebo **Z** po prvním bodu pro určení osy, ve které bude následuící bod.
-   Pro zadání souřadnic ručně, jednoduše zadejte číslo a stiskněte **ENTER** mezi každou z komponent X, Y a Z.
-   Stiskněte klávesu **R** nebo klikněte/odklikněte zaklikávací políčko **'''Relativní'''**. Je-li nastaven relativní mód jsou souřadnice následujícího bodu relativní k předchozímu bodu. Je-li mód absolutní souřadnice jsou vztaženy k počátečnímu bodu (0,0,0).
-   Stiskněte klávesu **T** nebo klikněte/odklikněte zaklikávací políčko **'''Pokračovat'''**. Je-li nastaven pokračovací mód, nástroj Obdélník bude po ukončení obdélníku restartován a připraven ke kreslení dalšího obdélníku bez nutnosti znovu jej spouštět klikáním na tlačítko Obdélník.
-   Stiskněte při kreslení klávesu **CTRL** pro [přichycení](Draft_Snap/cs.md) Vašeho bodu k nejbližšímu uchopovacímu místu, nezávisle na vzdálenosti od něho.
-   Stiskněte při kreslení klávesu **SHIFT** pro nastavení [vazby](Draft_Constrain/cs.md) Vašeho dalšího bodu vodorovně nebo svisle v relaci k předchozímu bodu.
-   Stiskněte klávesu **I** nebo tlačítko **'''Filled'''** aby se obdélník zobrazoval jako plocha. To jednoduše nastavuje Pohled-\>Vlastnost Obdélníku na \"Otevřené čáry\" nebo \"Drátový model\", toto také může být snadno změněno později.
-   Stiskněte klávesu **ESC** nebo tlačítko **'''Cancel'''** pro ukončení aktuálního příkazu Obdélník.


</div>

## Notes

-   A Draft Rectangle can be edited with the [Draft Edit](Draft_Edit.md) command.

## Preferences

See also: [Preferences Editor](Preferences_Editor.md) and [Draft Preferences](Draft_Preferences.md).

-   To change the number of decimals used for the input of coordinates: **Edit → Preferences... → General → Units → Units settings → Number of decimals**.
-   To change the initial value of filled mode: **Edit → Preferences... → Draft → General settings → Draft tools options → Fill objects with faces whenever possible**. Changing the filled mode in a task panel will override this preference for the current FreeCAD session.
-   If the **Edit → Preferences... → Draft → General settings → Draft tools options → Use Part Primitives when available** option is checked, the command will create a [Part Plane](Part_Plane.md) instead of a Draft Rectangle.


<div class="mw-translate-fuzzy">

## Vlastnosti

-    **Délka**: Specifikuje délku obdélníku

-    **Šířka**: Specifikuje šířku obdélníku

-    **Poloměr zaoblení**: Specifikuje poloměr zaoblení rohů obdélníku

-    **Textura obrázku**: Umožňuje zadat adresu souboru s obrázkem, který bude zobrazen na obdélníku. Je na Vás jestli dáte obdélníku stejné proporce jako má obrázek abyste se vyhnuli jeho zkreslení. Nevyplnění této vlastnosti obrázek odebere.


</div>

See also: [Property editor](Property_editor.md).

A Draft Rectangle object is derived from a [Part Part2DObject](Part_Part2DObject.md) and inherits all its properties. It also has the following additional properties:

### Data


{{TitleProperty|Draft}}

-    **Area|Area**: (read-only) specifies the area of the face of the rectangle. The value will be {{value|0.0}} if **Make Face** if `False`.

-    **Chamfer Size|Length**: specifies the length of the chamfers at the corners of the rectangle.

-    **Columns|Integer**: specifies the number of equal-sized columns in which the rectangle is divided.

-    **Fillet Radius|Length**: specifies the radius of the fillets at the corners of the rectangle.

-    **Height|Distance**: specifies the height of the rectangle.

-    **Length|Distance**: specifies the length of the rectangle.

-    **Make Face|Bool**: specifies if the rectangle makes a face or not. If it is `True` a face is created, otherwise only the perimeter is considered part of the object.

-    **Rows|Integer**: specifies the number of equal-sized rows in which the rectangle is divided.

### View


{{TitleProperty|Draft}}

-    **Pattern|Enumeration**: specifies the [Draft Pattern](Draft_Pattern.md) with which to fill the face of the rectangle. This property only works if **Make Face** is `True` and if **Display Mode** is {{value|Flat Lines}}.

-    **Pattern Size|Float**: specifies the size of the [Draft Pattern](Draft_Pattern.md).

-    **Texture Image|File**: specifies the path of the image file to be mapped onto the face of the rectangle. Blanking this property will remove the image. The rectangle should have the same proportions as the image to avoid distortions.

## Scripting


<div class="mw-translate-fuzzy">

## Skriptování

Nástroj Obdélník může být využit v [makrech](macros/cs.md) a z konzoly Pythonu použitím následující funkce:


</div>

To create a Draft Rectangle use the `make_rectangle` method (<small>(v0.19)</small> ) of the Draft module. This method replaces the deprecated `makeRectangle` method.


```python
rectangle = make_rectangle(length, height, placement=None, face=None, support=None)
```


<div class="mw-translate-fuzzy">

-   Vytvoří objekt obdélník s délkou v ose X a výškou v ose Y.
-   Je-li zadáno placement (umístění), je použito.
-   Je-li facemode False, obdélník je zobrazen jako povrch, jinak jako drátový model.
-   Je použita tloušťka čáry a barva čáry podle aktuálního nastavení.
-   Výstupem je nově vytvořený objekt.


</div>

Příklad: 
```python
import FreeCAD as App
import Draft

doc = App.newDocument()

rectangle1 = Draft.make_rectangle(4000, 1000)
rectangle2 = Draft.make_rectangle(1000, 4000)

zaxis = App.Vector(0, 0, 1)
p3 = App.Vector(1000, 1000, 0)
place3 = App.Placement(p3, App.Rotation(zaxis, 45))

rectangle3 = Draft.make_rectangle(3500, 250, placement=place3)

doc.recompute()
```



---
![](images/Button_right.svg) [documentation index](../README.md) > [Draft](Draft_Workbench.md) > Draft Rectangle/cs
