# Draft Wire/cs
---
- GuiCommand:   Name:Draft_Wire   Name/cs:Kreslení Drát   Workbenches:[Architektura](Draft_Workbench/cs___Kreslení]],_[[Arch_Workbench/cs.md)|Shortcut:W I   MenuLocation:Kreslení -> Drát   SeeAlso:[Kreslení Přímka](Draft_Line/cs.md), [Kreslení B-křivka](Draft_BSpline/cs.md)---


</div>

## Description


<div class="mw-translate-fuzzy">

## Popis

Nástroj Drát vytváří lomenou čáru (sekvenci přímek z několika segmentů) v aktuální [pracovní rovině](Draft_SelectPlane/cs.md). Použije se [tloušťka čáry a barva](Draft_Linestyle/cs.md) předem zadaná v záložce Nástrojů. Nástroj Drát se chová přesně stejně jako nástroj [Přímka](Draft_Line/cs.md) kromě toho, že nekončí po zadání dvou bodů.


</div>

The corners of a Draft Wire can be filleted (rounded) or chamfered by changing its **Fillet Radius** or **Chamfer Size** respectively. It is also possible to subdivide the edges of a Draft Wire by changing its **Subdivisions** property.

<img alt="" src=images/Draft_Polyline_example.jpg  style="width:400px;"> 
*Wire defined by multiple points*

## Create

### Usage

See also: [Draft Tray](Draft_Tray.md), [Draft Snap](Draft_Snap.md) and [Draft Constrain](Draft_Constrain.md).


<div class="mw-translate-fuzzy">

## Použití

1.  Stiskněte tlačítko **<img src="images/Draft_Wire.png" width=16px> [Drát](Draft_Wire.md)
** nebo klávesy **W** potom **I**
2.  Klikněte na první bod ve 3D pohledu nebo zadejte jeho souřadnice
3.  Klikněte na další bod ve 3D pohledu nebo zadejte jeho souřadnice
4.  Stiskněte klávesu **F** nebo **C** nebo dvojklikněte na poslední bod pro ukončení nebo uzavření drátu. Je-li drát uzavřen, bude zároveň i povrchem i když se jeví jako drátový model.


</div>

### Options

The single character keyboard shortcuts available in the task panel can be changed. See [Draft Preferences](Draft_Preferences.md). The shortcuts mentioned here are the default shortcuts.


<div class="mw-translate-fuzzy">

## Volby

-   Stiskněte klávesu **F** nebo tlačítko **<img src="images/Draft_FinishLine.png" width=12px> '''UkončitČáru'''** pro ukončení drátu a ponechání jej otevřený
-   Stiskněte klávesu **C** nebo tlačítko **<img src="images/Draft_CloseLine.png" width=12px> '''UzavřítČáru'''** nebo klikněte na první bod drátu. Tím se drát ukončí a uzavře se doplněním posledního (uzavíracího) segmentu mezi posledním a počátečním bodem.
-   Stisknutím klávesy **X**, **Y** nebo **Z** po zadání bodu zajistíte, že následující bod bude ležet na dané ose.
-   Pro ruční zadávání souřadnic jednoduše zadávejte čísla a mezi každou komponentou X, Y a Z stiskněte **ENTER**
-   Stiskněte klávesu **R** nebo klikněte/odklikněte zaklikávací políčko **'''Relativní'''**. Je-li nastaven relativní mód jsou souřadnice následujícího bodu relativní k předchozímu bodu. Je-li mód absolutní souřadnice jsou vztaženy k počátečnímu bodu (0,0,0).
-   Stiskněte klávesu **T** nebo klikněte/odklikněte zaklikávací políčko **'''Pokračovat'''**. Je-li nastaven pokračovací mód, nástroj Drát bude po ukončení drátu restartován a připraven ke kreslení dalšího drátu bez nutnosti znovu jej spouštět klikáním na tlačítko Drát.
-   Stiskněte při kreslení klávesu **CTRL** pro [přichycení](Draft_Snap.md) Vašeho bodu k nejbližšímu uchopovacímu místu, nezávisle na vzdálenosti od něho.
-   Stiskněte při kreslení klávesu **SHIFT** pro nastavení [vazby](Draft_Constrain.md) Vašeho dalšího bodu vodorovně nebo svisle v relaci k předchozímu bodu.
-   Stiskněte klávesu **W** nebo stiskněte tlačítko **<img src="images/Draft_Wipe.png" width=12px> '''Smaž'''** pro odstranění existujících segmentů a začněte křivku z posledního bodu.
-   Stiskněte klávesy **CTRL**+**Z** nebo tlačítko **<img src="images/Draft_UndoLine.png" width=12px> '''Undo'''** k návratu na poslední bod.
-   Stiskněte klávesu **I** nebo tlačítko **'''Filled'''** aby se drát po jeho uzavření zobrazoval jako plocha. To jednoduše nastavuje Pohled-\>Vlastnost Drát na \"Otevřené čáry\" nebo \"Drátový model\", toto také může být snadno změněno později.
-   Stiskněte klávesu **ESC** nebo tlačítko **'''Cancel'''** pro ukončení aktuálního příkazu Drát.


</div>

## Join

### Usage 

1.  The end points of the [Draft Lines](Draft_Line.md) and/or Draft Wires to be joined must be exactly coincident. If required first adjust points to ensure that this is the case.
2.  Select two or more [Draft Lines](Draft_Line.md) and/or Draft Wires.
3.  There are several ways to invoke the command:
    -   Press the **<img src="images/Draft_Wire.svg" width=16px> [Draft Wire](Draft_Wire.md)** button.
    -   Select the **Drafting → <img src="images/Draft_Wire.svg" width=16px> Polyline** option from the menu.
    -   Use the keyboard shortcut: **P** then **L**.

## Notes

-   A Draft Wire can be edited with the [Draft Edit](Draft_Edit.md) command.
-   A Draft Wire can be converted to a [Draft BSpline](Draft_BSpline.md) with the [Draft WireToBSpline](Draft_WireToBSpline.md) command.
-   [Draft Lines](Draft_Line.md) and Draft Wires can also be joined with the [Draft Join](Draft_Join.md) command or the [Draft Upgrade](Draft_Upgrade.md) command.

## Preferences

See also: [Preferences Editor](Preferences_Editor.md) and [Draft Preferences](Draft_Preferences.md).

-   To change the number of decimals used for the input of coordinates: **Edit → Preferences... → General → Units → Units settings → Number of decimals**.
-   To change the initial value of filled mode: **Edit → Preferences... → Draft → General settings → Draft tools options → Fill objects with faces whenever possible**. Changing the filled mode in a task panel will override this preference for the current FreeCAD session.

## Properties

See also: [Property editor](Property_editor.md).

A Draft Wire object is derived from a [Part Part2DObject](Part_Part2DObject.md) and inherits all its properties. It also has the following additional properties:

### Data


{{TitleProperty|Draft}}

-    **Area|Area**: (read-only) specifies the area of the face of the wire. The value will be {{value|0.0}} if **Make Face** if `False` or the face cannot be created.

-    **Base|Link**
    

-    **Chamfer Size|Length**: specifies the length of the chamfers at the corners of the wire.

-    **Closed|Bool**: specifies if the wire is closed or not. If the wire is initially open this value is `False`, setting it to `True` will draw a line segment to close the wire. If the wire is initially closed this value is `True`, setting it to `False` will remove the last line segment and make the wire open.

-    **End|VectorDistance**: specifies the end point of the wire.

-    **Fillet Radius|Length**: specifies the radius of the fillets at the corners of the wire.

-    **Length|Length**: (read-only) specifies the total length of the wire.

-    **Make Face|Bool**: specifies if the wire makes a face or not. If it is `True` a face is created, otherwise only the edges are considered part of the object. This property only works if **Closed** is `True` and if the wire does not self-intersect.

-    **Points|VectorList**: specifies the points of the wire in its local coordinate system.

-    **Start|VectorDistance**: specifies the start point of the wire.

-    **Subdivisions|Integer**: specifies the number of subdivisions for each edge of the wire. If it is {{value|1}} each edge will be divided into {{value|2}} equal segments. Subdivisions are applied before chamfers and fillets.

-    **Tool|Link**
    

### View


{{TitleProperty|Draft}}

-    **Arrow Size|Length**: specifies the size of the symbol displayed at the end of the wire.

-    **Arrow Type|Enumeration**: specifies the type of symbol displayed at the end of the wire, which can be {{value|Dot}}, {{value|Circle}}, {{value|Arrow}}, {{value|Tick}} or {{value|Tick-2}}.

-    **End Arrow|Bool**: specifies whether to show a symbol at the end of the wire, so it can be used as an annotation line.

-    **Pattern|Enumeration**: specifies the [Draft Pattern](Draft_Pattern.md) with which to fill the face of the closed wire. This property only works if **Make Face** is `True` and if **Display Mode** is {{value|Flat Lines}}.

-    **Pattern Size|Float**: specifies the size of the [Draft Pattern](Draft_Pattern.md).




<div class="mw-translate-fuzzy">

## Skriptování

Nástroj Drát může být využit v [makrech](macros.md) a z konzoly Pythonu použitím následující funkce:


</div>

See also: [Autogenerated API documentation](https://freecad.github.io/SourceDoc/) and [FreeCAD Scripting Basics](FreeCAD_Scripting_Basics.md).

To create a Draft Wire use the `make_wire` method (<small>(v0.19)</small> ) of the Draft module. This method replaces the deprecated `makeWire` method.


```python
wire = make_wire(pointslist, closed=False, placement=None, face=None, support=None)
wire = make_wire(Part.Wire, closed=False, placement=None, face=None, support=None)
```


<div class="mw-translate-fuzzy">

-   Vytvoří objekt Drát podle zadaného seznamu vektorů bodů nebo podle Drát (Part Wire).
-   Je-li closed True nebo jsou-li první a poslední bod identické, drát je uzavřen.
-   Je-li face (plocha) True (a drát je uzavřen), bude se drát jevit jako vyplněná plocha.
-   Je použita aktuálně nastavená tloušťka čáry a barva čáry.
-   Vrací nově vytvořený objekt.


</div>

Příklad:


```python
import FreeCAD as App
import Draft

doc = App.newDocument()

p1 = App.Vector(0, 0, 0)
p2 = App.Vector(1000, 1000, 0)
p3 = App.Vector(2000, 0, 0)

wire1 = Draft.make_wire([p1, p2, p3], closed=True)
wire2 = Draft.make_wire([p1, 2*p3, 1.3*p2], closed=True)
wire3 = Draft.make_wire([1.3*p3, p1, -1.7*p2], closed=True)

doc.recompute()
```



---
![](images/Button_right.svg) [documentation index](../README.md) > [Draft](Draft_Workbench.md) > Draft Wire/cs
