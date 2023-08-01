# Draft Circle/cs
---
- GuiCommand:/cs   Name:Draft_Circle   Name/cs:Kreslení_Kružnice   Workbenches:[Architektura](Draft_Workbench/cs___Kreslení]],_[[Arch_Workbench/cs.md)|MenuLocation:Kreslení -> Kružnice   Shortcut:C I   SeeAlso:[Kreslení oblouk](Draft_Arc/cs.md)---


</div>

## Description


<div class="mw-translate-fuzzy">

## Popis

Nástroj Kružnice vytváří kružnici v aktuální [pracovní rovině](Draft_SelectPlane/cs.md) zadáním dvou bodů: střed a poloměr nebo zadáním tečen nebo kombinací obou způsobů. Použije se [tloušťka čáry a barva](Draft_Linestyle/cs.md) předem zadaná v záložce Nástrojů. Tento nástroj pracuje stejně jako nástroj [Oblouk](Draft_Circle/cs.md), kromě toho, že se končí po zadání poloměru.


</div>

A Draft Circle can be turned into an arc by setting its **First Angle** and **Last Angle** properties to different values.

<img alt="" src=images/Draft_Circle_example.jpg  style="width:400px;">


<div class="mw-translate-fuzzy">

<img alt="" src=images/Draft_Circle_example.jpg  style="width:400px;">


</div>

## Usage

See also: [Draft Tray](Draft_Tray.md), [Draft Snap](Draft_Snap.md) and [Draft Constrain](Draft_Constrain.md).


<div class="mw-translate-fuzzy">

## Použití

1.  Stiskněte tlačítko **<img src="images/Draft_Circle.png" width=16px> [Kružnice](Draft_Circle/cs.md)
** nebo klávesy **C** pak **I**
2.  Klikněte na první bod ve 3D pohledu nebo zadejte souřadnice
3.  Klikněte na druhý bod ve 3D pohledu nebo zadejte hodnotu poloměru.


</div>

## Options

The single character keyboard shortcuts available in the task panel can be changed. See [Draft Preferences](Draft_Preferences.md). The shortcuts mentioned here are the default shortcuts.


<div class="mw-translate-fuzzy">

## Volby

-   Základní způsob použití nástrije Kružnice je zadáním dvou bodů, středu a bodu na obvodu kružnice, který definuje poloměr.
-   Stiskem **ALT** můžete vybrat tečnu místo zadání druhého bodu. Můžete tak zkonstruovat několik typů kružnic výběrem jedné dvou nebo tří tečen.
-   Chcete-li zadat souřadnice ručně, jdenoduše vkládejte čísla a stiskněte **ENTER** mezi každou z komponent X, Y a Z.
-   Stiskněte klávesu T nebo klikněte na zaklikávací políčko pro zatrhnutí nebo odtrhnutí tlačítka Pokračovat. Je-li nastaven pokračovací mód, bude nástroj Kružnice hned po zadání druhého bodu připraven ke kreslení další kružnice bez nutnosti stisknout znovu tlačítko Kružnice.
-   Stisknutím klávesy **CTRL** během kreslení vynutíte [přichycení](Draft_Snap.md) vašeho bodu k nejbližšímu uchopovacímu místu nezávisle na vzálenosti od něho.
-   Stisknutím klávesy **SHIFT** během kreslení [nastavíte vazbu](Draft_Constrain.md) vašeho bodu svisle nebo vodorovně v relaci ke středu.
-   Stisknutím klávesy **I** nebo tlačítka **'''Filled'''** zajistíte, že se kružnice tváří jako plocha (musí být uzavřená). Jednoduše se to nastavuje Pohled-\>Vlastnost Kružnice na \"Otevřené čáry\" nebo \"Drátový model\", toto také může být snadno změněno později.
-   Stiskněte klávesu **ESC** nebo tlačítko **'''Cancel'''** pro ukončení aktuálního příkazu.
-   Kružnice může být po vytvoření změněna na oblouk nastavením počátečního a koncového úhlu na jiné hodnoty.
-   Když je Kružnice v zobrazovacím módu \"Jednoduché čáry\" může zobrazovat šrafovací vzor nastavením vlastnosti \"Vzor\" dole.


</div>

## Notes

-   A Draft Circle can be edited with the [Draft Edit](Draft_Edit.md) command.

## Preferences

See also: [Preferences Editor](Preferences_Editor.md) and [Draft Preferences](Draft_Preferences.md).

-   To change the number of decimals used for the input of coordinates and radii: **Edit → Preferences... → General → Units → Units settings → Number of decimals**.
-   To change the initial value of filled mode: **Edit → Preferences... → Draft → General settings → Draft tools options → Fill objects with faces whenever possible**. Changing the filled mode in a task panel will override this preference for the current FreeCAD session.
-   If the **Edit → Preferences... → Draft → General settings → Draft tools options → Use Part Primitives when available** option is checked, the command will create a [Part Circle](Part_Circle.md) instead of a Draft Circle.

## Properties

See also: [Property editor](Property_editor.md).

A Draft Circle object is derived from a [Part Part2DObject](Part_Part2DObject.md) and inherits all its properties. It also has the following additional properties:

### Data


{{TitleProperty|Draft}}

-    **Area|Area**: (read-only) specifies the area of the face of the circle. The value will be {{value|0.0}} if **Make Face** if `False` or the face cannot be created.

-    **First Angle|Angle**: specifies the start angle of the circle, normally {{value|0&#176;}}.

-    **Last Angle|Angle**: specifies the end angle of the circle, normally {{value|0&#176;}}.

-    **Make Face|Bool**: specifies if the circle makes a face or not. If it is `True` a face is created, otherwise only the perimeter is considered part of the object. This property only works if the **First Angle** and **Last Angle** have the same value. Note that {{value|0&#176;}} and {{value|360&#176;}} are not considered the same.

-    **Radius|Length**: specifies the radius of the circle.

### View


{{TitleProperty|Draft}}

-    **Pattern|Enumeration**: specifies the [Draft Pattern](Draft_Pattern.md) with which to fill the face of the circle. This property only works if **Make Face** is `True` and if **Display Mode** is {{value|Flat Lines}}.

-    **Pattern Size|Float**: specifies the size of the [Draft Pattern](Draft_Pattern.md).

## Scripting


<div class="mw-translate-fuzzy">

## Skriptování

Nástroj Kružnice může být využit v [makrech](macros.md) a z konzoly Pythonu použitím následující funkce:


</div>

To create a Draft Circle use the `make_circle` method (<small>(v0.19)</small> ) of the Draft module. This method replaces the deprecated `makeCircle` method.


```python
circle = make_circle(radius, placement=None, face=None, startangle=None, endangle=None, support=None)
circle = make_circle(Part.Edge, placement=None, face=None, startangle=None, endangle=None, support=None)
```


<div class="mw-translate-fuzzy">

-   Vytvoří objekt kružnice podle daného poloměru.
-   Je-li zadáno placement (umístění), je využito.
-   Je-li facemode (mód plochy) False, bude kružnice zobrazena jako drát, jinak jako plocha.
-   Jsou-li zadány počáteční a koncový úhel (startangle a endangle) (ve stupních), jsou využity a objekt se zobrazí jako oblouk.
-   Výstupem je nově vytvořený objekt.


</div>

Příklad: 
```python
import FreeCAD as App
import Draft

doc = App.newDocument()

circle1 = Draft.make_circle(200)

zaxis = App.Vector(0, 0, 1)
p2 = App.Vector(1000, 1000, 0)
place2 = App.Placement(p2, App.Rotation(zaxis, 0))
circle2 = Draft.make_circle(500, placement=place2)

p3 = App.Vector(-1000, -1000, 0)
place3 = App.Placement(p3, App.Rotation(zaxis, 0))
circle3 = Draft.make_circle(750, placement=place3)

doc.recompute()
```



---
![](images/Button_right.svg) [documentation index](../README.md) > [Draft](Draft_Workbench.md) > Draft Circle/cs
