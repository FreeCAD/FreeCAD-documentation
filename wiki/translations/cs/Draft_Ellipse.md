# Draft Ellipse/cs
---
- GuiCommand:/cs   Name:Draft_Ellipse   Name/cs:Kreslení Elipsa   Workbenches:[Architektura](Draft_Workbench/cs___Kreslení]],_[[Arch_Workbench/cs.md)|MenuLocation:Kreslení -> Elipsa   Shortcut:E L   SeeAlso:[Kreslení Kružnice](Draft_Circle/cs.md)---


</div>

## Popis


<div class="mw-translate-fuzzy">

Nástroj Elipsa vytvoří elipsu v aktuální [pracovní rovině](Draft_SelectPlane/cs.md) vložením dvou bodů definujících roh obdélníku, kterému je elipsa vepsána. Elipsa přebírá [barvu a tloušťku čáry](Draft_Linestyle/cs.md) předem nastavenou v záložce úloh.


</div>

A Draft Ellipse can be turned into an elliptical arc by setting its **First Angle** and **Last Angle** properties to different values.

<img alt="" src=images/Draft_ellipse_example.jpg  style="width:400px;">


<div class="mw-translate-fuzzy">

<img alt="" src=images/Draft_ellipse_example.jpg  style="width:400px;">


</div>

## Usage

See also: [Draft Tray](Draft_Tray.md), [Draft Snap](Draft_Snap.md) and [Draft Constrain](Draft_Constrain.md).


<div class="mw-translate-fuzzy">

## Použití

1.  Stiskněte tlačítko **<img src="images/Draft_Ellipse.png" width=16px> [Elipsa](Draft_Ellipse.md)
** nebo klávesy **E** pak **L**
2.  Klikněte na první bod ve 3D pohledu nebo zadejte souřadnice
3.  Klikněte na druhý bod ve 3D pohledu nebo zadejte souřadnice.


</div>

## Volby

The single character keyboard shortcuts available in the task panel can be changed. See [Draft Preferences](Draft_Preferences.md). The shortcuts mentioned here are the default shortcuts.


<div class="mw-translate-fuzzy">

-   Chcete-li zadat souřadnice ručně jednoduše zadejte číslo a potom stiskněte **ENTER** mezi každou z komponent X, Y a Z.
-   Stiskněte klávesu **T** nebo klikněte na zaklikávací políčko pro zatrhnutí nebo odtrhnutí tlačítka **'''Pokračovat'''**. Je-li nastaven pokračovací mód, bude nástroj Elipsa hned po zadání druhého bodu připraven ke kreslení další elipsy bez nutnosti stisknout znovu tlačítko Elipsa.
-   Stisknutím klávesy **CTRL** během kreslení vynutíte [přichycení](Draft_Snap.md) vašeho bodu k nejbližšímu uchopovacímu místu nezávisle na vzálenosti od něho.
-   Stisknutím klávesy **SHIFT** během kreslení [nastavíte vazbu](Draft_Constrain.md) vašeho bodu svisle nebo vodorovně v relaci k předchozímu bodu.
-   Stisknutím klávesy **I** nebo tlačítka **'''Vyplnit'''** bude se elipsa po uzavření jevit jako povrch (vyplněná). Tak se jednoduše nastaví Pohled-\>Vlastnosti elipsy na \"Flat přímky\" nebo \"Drátový model\", což může být nastaveno i později.
-   Stisknutím tlačítka **ESC** nebo **'''Cancel'''** zrušíte právě probíhající příkaz.
-   Elipsy v zobrazovacím módu \"Flat přímky\" mohou mít šrafování podle nastavení jejich vlastnosti \"Vzor\" níže.


</div>

## Notes

-   A Draft Ellipse can be edited with the [Draft Edit](Draft_Edit.md) command.

## Preferences

See also: [Preferences Editor](Preferences_Editor.md) and [Draft Preferences](Draft_Preferences.md).

-   To change the number of decimals used for the input of coordinates: **Edit → Preferences... → General → Units → Units settings → Number of decimals**.
-   To change the initial value of filled mode: **Edit → Preferences... → Draft → General settings → Draft tools options → Fill objects with faces whenever possible**. Changing the filled mode in a task panel will override this preference for the current FreeCAD session.
-   If the **Edit → Preferences... → Draft → General settings → Draft tools options → Use Part Primitives when available** option is checked, the command will create a [Part Ellipse](Part_Ellipse.md) instead of a Draft Ellipse.

## Vlastnosti

See also: [Property editor](Property_editor.md).

A Draft Ellipse object is derived from a [Part Part2DObject](Part_Part2DObject.md) and inherits all its properties. It also has the following additional properties:

### Data


{{TitleProperty|Draft}}


<div class="mw-translate-fuzzy">

-    **Velký poloměr**: Velký poloměr elipsy

-    **Malý poloměr**: Malý poloměr elipsy

-    **Vzor**: Určuje šrafovací vzor, kterým má elipsa být vyplněna

-    **Rozměr vzoru**: Určuje velikost šrafovacího vzoru


</div>

### View


{{TitleProperty|Draft}}

-    **Pattern|Enumeration**: specifies the [Draft Pattern](Draft_Pattern.md) with which to fill the face of the ellipse. This property only works if **Make Face** is `True` and if **Display Mode** is {{value|Flat Lines}}.

-    **Pattern Size|Float**: specifies the size of the [Draft Pattern](Draft_Pattern.md).

## Scripting


<div class="mw-translate-fuzzy">

## Skriptování

Nástroj Elipsa může být využit v [makrech](macros.md) a z konzoly Pythonu použitím následující funkce:


</div>

To create a Draft Ellipse use the `make_ellipse` method (<small>(v0.19)</small> ) of the Draft module. This method replaces the deprecated `makeEllipse` method.


```python
ellipse = make_ellipse(majradius, minradius, placement=None, face=True, support=None)
```


<div class="mw-translate-fuzzy">

-   Vytvoří elipsu s daným velkým (majorradius) a malým(minorradius) poloměrem.
-   Je-li zadán placement (umístění), bude využito.
-   Je-li facemode False, bude se elipsa zobrazovat jako drátový model, jinak jako plocha.
-   Vrací nově vytvořený pohled.


</div>

Příklad:


```python
import FreeCAD as App
import Draft

doc = App.newDocument()

ellipse1 = Draft.make_ellipse(3000, 200)
ellipse2 = Draft.make_ellipse(700, 1000)

zaxis = App.Vector(0, 0, 1)
p3 = App.Vector(1000, 1000, 0)
place3 = App.Placement(p3, App.Rotation(zaxis, 90))

ellipse3 = Draft.make_ellipse(700, 1000, placement=place3)

doc.recompute()
```



---
![](images/Right_arrow.png) [documentation index](../README.md) > [Draft](Draft_Workbench.md) > Draft Ellipse/cs
