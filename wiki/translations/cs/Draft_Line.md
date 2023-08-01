# Draft Line/cs
---
- GuiCommand:   Name:Draft Line   Name/cs:Kreslení Přímka   Workbenches:[Architektura](Draft_Workbench/cs___Kreslení]],_[[Arch_Workbench/cs.md)|MenuLocation:Kreslení - Přímka   Shortcut:L I   SeeAlso:[Kreslení drát](Draft_Wire/cs.md)---


</div>

## Description


<div class="mw-translate-fuzzy">

## Popis

Nástroj Přímka vytváří rovnou dvoubodovou přímku v aktuální [pracovní rovině](Draft_SelectPlane/cs.md). Použije se [tloušťka čáry a barva](Draft_Linestyle/cs.md) předem zadaná v záložce Nástrojů. Nástroj Přímka se chová přesně stejně jako nástroj [Drát (lomená čára)](Draft_Wire/cs.md) kromě toho že končí po zadání dvou bodů.


</div>

A Draft Line is in fact a [Draft Wire](Draft_Wire.md) with only two points.

<img alt="" src=images/Draft_Line_example.jpg  style="width:400px;">


<div class="mw-translate-fuzzy">

<img alt="" src=images/Draft_Line_example.jpg  style="width:400px;">


</div>

## Usage

See also: [Draft Tray](Draft_Tray.md), [Draft Snap](Draft_Snap.md) and [Draft Constrain](Draft_Constrain.md).


<div class="mw-translate-fuzzy">

## Použití

1.  Stiskněte tlačítko **<img src="images/Draft_Line.png" width=16px> [Přímka](Draft_Line.md)
** nebo klávesy **L** pak **I**
2.  Klikněte na první bod ve 3D pohledu nebo zadejte souřadnice
3.  Klikněte na druhý bod ve 3D pohledu nebo zadejte souřadnice.


</div>

## Options

The single character keyboard shortcuts available in the task panel can be changed. See [Draft Preferences](Draft_Preferences.md). The shortcuts mentioned here are the default shortcuts.


<div class="mw-translate-fuzzy">

## Volby

-   Po zadání prvního bodu stiskněte **X**, **Y** nebo **Z** pro určení osy druhého bodu.
-   Pro zadání souřadnic ručně, jednoduše zadejte číslo a stiskněte **ENTER** mezi každou z komponent X, Y a Z.
-   Stiskněte klávesu **R** nebo klikněte/odklikněte zaklikávací políčko **'''Relativní'''**. Je-li nastaven relativní mód jsou souřadnice následujícího bodu relativní k předchozímu bodu. Je-li mód absolutní souřadnice jsou vztaženy k počátečnímu bodu (0,0,0).
-   Stiskněte klávesu **T** nebo klikněte/odklikněte zaklikávací políčko **'''Pokračovat'''**. Je-li nastaven pokračovací mód, nástroj Přímka bude po ukončení křivky restartován a připraven ke kreslení další přímky bez nutnosti znovu jej spouštět klikáním na tlačítko Přímka.
-   Stiskněte při kreslení klávesu **CTRL** pro [přichycení](Draft_Snap.md) Vašeho bodu k nejbližšímu uchopovacímu místu, nezávisle na vzdálenosti od něho.
-   Stiskněte při kreslení klávesu **SHIFT** pro nastavení [vazby](Draft_Constrain.md) Vašeho dalšího bodu vodorovně nebo svisle v relaci k předchozímu bodu.
-   Stiskněte klávesy **CTRL**+**Z** nebo tlačítko **<img src="images/Draft_UndoLine.png" width=12px> '''Undo'''** ke zrušení posledního bodu.
-   Stiskněte klávesu **ESC** nebo tlačítko **'''Cancel'''** pro ukončení aktuálního příkazu Přímka.


</div>

## Notes

-   A Draft Line can be edited with the [Draft Edit](Draft_Edit.md) command.
-   Draft Lines and [Draft Wires](Draft_Wire.md) can be joined with the [Draft Wire](Draft_Wire.md) command, the [Draft Join](Draft_Join.md) command or the [Draft Upgrade](Draft_Upgrade.md) command.

## Preferences

See also: [Preferences Editor](Preferences_Editor.md) and [Draft Preferences](Draft_Preferences.md).

-   To change the number of decimals used for the input of coordinates, lengths and angles: **Edit → Preferences... → General → Units → Units settings → Number of decimals**.
-   To change the initial focus of the task panel to the **Length** input box: **Edit → Preferences... → Draft → General settings → Draft tools options → Set focus on Length instead of X coordinate**. Note that you must move the pointer in the [3D view](3D_view.md) for the change to take effect.
-   If the **Edit → Preferences... → Draft → General settings → Draft tools options → Use Part Primitives when available** option is checked, the command will create a [Part Line](Part_Line.md) instead of a Draft Line.

## Properties


<div class="mw-translate-fuzzy">

## Vlastnosti

-    {{PropertyData/cs|Počátek}}: Počáteční bod

-    {{PropertyData/cs|Konec}}: Koncový bod

-    {{PropertyData/cs|Subdivisions}}: Divides the line with the given number of subdivisions <small>(v0.16)</small> 


</div>

## Scripting


<div class="mw-translate-fuzzy">

## Skriptování

Nástroj Přímka může být využit v [makrech](macros.md) a z konzoly Pythonu použitím následující funkce:


</div>

To create a Draft Line use the `make_line` method (<small>(v0.19)</small> ) of the Draft module. This method replaces the deprecated `makeLine` method.


```python
line = make_line(p1, p2)
line = make_line(LineSegment)
line = make_line(Shape)
```


<div class="mw-translate-fuzzy">

-   Vytvoří přímku mezi dvěma zadanými vektory. Pro kreslení je použita aktuálně nastavená šířka a barva čáry.
-   Vrací nově vytvořený objekt.


</div>

Příklad:


```python
import FreeCAD as App
import Draft

doc = App.newDocument()

p1 = App.Vector(0, 0, 0)
p2 = App.Vector(1000, 500, 0)
p3 = App.Vector(-250, -500, 0)
p4 = App.Vector(500, 1000, 0)

line1 = Draft.make_line(p1, p2)
line2 = Draft.make_line(p3, p4)

doc.recompute()
```



---
![](images/Button_right.svg) [documentation index](../README.md) > [Draft](Draft_Workbench.md) > Draft Line/cs
