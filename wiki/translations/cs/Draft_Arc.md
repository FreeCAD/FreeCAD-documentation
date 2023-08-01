# Draft Arc/cs
---
- GuiCommand:/cs   Name:Draft_Arc   Name/cs:Kreslení oblouk   Workbenches:[Architektura](Draft_Workbench/cs___Kreslení]],_[[Arch_Workbench/cs.md)|MenuLocation:Kreslení → Oblouk   Shortcut:A R   SeeAlso:[Kreslení kružnice](Draft_Circle/cs.md)---


</div>


<div class="mw-translate-fuzzy">

## Popis

Nástroj Oblouk vytváří oblouk v aktuální [pracovní rovině](Draft_SelectPlane/cs.md) zadáním čtyř bodů: střed, poloměr, počáteční a koncový bod nebo zadáním tečen nebo kombinací obou způsobů. Použije se [tloušťka čáry a barva](Draft_Linestyle/cs.md) předem zadaná v záložce Nástrojů. Tento nástroj pracuje stejně jako nástroj [Kružnice](Draft_Circle/cs.md), ale přidává počáteční a koncový úhel.


</div>

The <img alt="" src=images/Draft_Arc.svg  style="width:24px;"> **Draft Arc** command creates a circular arc in the current [working plane](Draft_SelectPlane.md) from a center, a radius, a start angle and an aperture angle. The radius and the angles can be defined by picking points.

A Draft Arc is in fact a [Draft Circle](Draft_Circle.md) with a **First Angle** that is not the same as its **Last Angle**.

<img alt="" src=images/Draft_Arc_example.jpg  style="width:400px;"> 
*Arc defined by four points, center, radius, initial point of arc and final point of arc*

## Usage

See also: [Draft Tray](Draft_Tray.md), [Draft Snap](Draft_Snap.md) and [Draft Constrain](Draft_Constrain.md).


<div class="mw-translate-fuzzy">

## Použití

1.  Stiskněte tlačítko **<img src="images/Draft_Arc.png" width=16px> [Oblouk](Draft_Arc.md)
** nebo stiskněte klávesy **A** a potom **R**
2.  Klikněte na první bod ve 3D pohledu nebo zadejte souřadnice
3.  Klikněte na druhý bod ve 3D pohledu nebo zadejte poloměr
4.  Klikněte na třetí bod ve 3D pohledu nebo zadejte počáteční úhel
5.  Klikněte na čtvrtý bod ve 3D pohledu nebo zadejte koncový úhel


</div>

## Options

The single character keyboard shortcuts available in the task panel can be changed. See [Draft Preferences](Draft_Preferences.md). The shortcuts mentioned here are the default shortcuts.


<div class="mw-translate-fuzzy">

## Volby

-   Základní použití nástroje Oblouk je zadání čtyř bodů: střed, bod na obvodu, který definuje poloměr, třetí bod definující začátek oblouku a čtvrtý bod definující jeho konec.
-   Stisknutím **ALT** můžete vybrat tečnu místo zadávání bodu čímž definujete základní kružnici oblouku. Tím můžete zkonstruovat několik typů kružnic výběrem jedné, dvou nebo tří tečen.
-   Směr oblouku závisí na pohybu myši. Jestli s ní po zadání třetího bodu začnete pohybovat ve směru hodinových ručiček, Váš oblouk bude vytvořen ve stejném směru. Chcete-li oblouk v opačném směru, jednoduše se myší vracejte přes třetí bod proti směru hodinových ručiček tak dlouho až se oblouk začne kreslit v opačném směru.
-   Chcete-li zadat souřadnice ručně jednoduše zadejte číslo a potom stiskněte **ENTER** mezi každou z komponent X, Y a Z.
-   Stiskněte klávesu **T** nebo klikněte na zaklikávací políčko pro zatrhnutí nebo odtrhnutí tlačítka **'''Pokračovat'''**. Je-li nastaven pokračovací mód, bude nástroj Oblouk hned po zadání čtvrtého bodu připraven ke kreslení dalšího oblouku bez nutnosti stisknout znovu tlačítko Oblouk..
-   Stisknutím klávesy **CTRL** během kreslení vynutíte [přichycení](Draft_Snap.md) vašeho bodu k nejbližšímu uchopovacímu místu nezávisle na vzálenosti od něho.
-   Stisknutím klávesy **SHIFT** během kreslení [nastavíte vazbu](Draft_Constrain.md) vašeho bodu svisle nebo vodorovně v relaci ke středu.
-   Stisknutím tlačítka **ESC** nebo **'''Cancel'''** zrušíte právě probíhající příkaz.
-   Oblouk může být po vytvoření změněn na kružnici nastavením stejné hodnoty pro počáteční i koncový úhel ve vlastnostech.


</div>

## Notes

-   A Draft Arc can be edited with the [Draft Edit](Draft_Edit.md) command.

## Preferences

See also: [Preferences Editor](Preferences_Editor.md) and [Draft Preferences](Draft_Preferences.md).

-   To change the number of decimals used for the input of coordinates, radii and angles: **Edit → Preferences... → General → Units → Units settings → Number of decimals**.
-   If the **Edit → Preferences... → Draft → General settings → Draft tools options → Use Part Primitives when available** option is checked, the command will create a [Part Circle](Part_Circle.md) instead of a Draft Circle.

## Properties


<div class="mw-translate-fuzzy">

## Vlastnosti

-    **Poloměr**: Poloměr oblouku

-    **Počáteční úhel**: Úhel počátečního bodu oblouku

-    **Koncový úhel**: Úhel koncového bodu oblouku


</div>

## Scripting


<div class="mw-translate-fuzzy">

## Skriptování

Nástroj Kružnice může být použít i pro vytváření oblouků v [makrech](macros.md) a z konzoly Pythonu použitím následující funkce, přidáním dodatečných argumentů:


</div>

To create a Draft Arc use the `make_circle` method (<small>(v0.19)</small> ) of the Draft module. This method replaces the deprecated `makeCircle` method.

Example:


```python
import FreeCAD as App
import Draft

doc = App.newDocument()

arc1 = Draft.make_circle(200, startangle=0, endangle=90)
arc2 = Draft.make_circle(500, startangle=20, endangle=160)
arc3 = Draft.make_circle(750, startangle=-30, endangle=-150)

doc.recompute()
```



---
![](images/Button_right.svg) [documentation index](../README.md) > [Draft](Draft_Workbench.md) > Draft Arc/cs
