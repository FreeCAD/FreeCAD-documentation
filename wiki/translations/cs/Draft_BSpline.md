# Draft BSpline/cs
---
- GuiCommand   */cs   Name   *Draft BSpline   Name/cs   *Draft BSpline   Workbenches   *[Architektura](Draft_Workbench/cs___Kreslení]],_[[Arch_Workbench/cs.md)|MenuLocation   *Draft → BSpline   Shortcut   *B S   SeeAlso   *[Drát](Draft_Wire/cs.md)---


</div>

## Description


<div class="mw-translate-fuzzy">

## Popis

Nástroj B-křivka vytváří [B-křivku](http   *//en.wikipedia.org/wiki/B-spline) z několika bodů v aktuální [pracovní rovině](Draft_SelectPlane/cs.md). Přebírá [tloušťku čáry a barvu](Draft_Linestyle/cs.md) předtím nastavenou v záložce nástrojů. Nástroj B-křivka se chová přesně stejně jako nástroj [Drát](Draft_Wire/cs.md).


</div>

The Draft BSpline command specifies the **exact points** through which the curve will pass. The [Draft BezCurve](Draft_BezCurve.md) and the [Draft CubicBezCurve](Draft_CubicBezCurve.md) commands, on the other hand, use **control points** to define the position and curvature of the spline.

<img alt="" src=images/Draft_bspline_example.jpg  style="width   *400px;">


<div class="mw-translate-fuzzy">

<img alt="" src=images/Draft_bspline_example.jpg  style="width   *400px;">


</div>

## Usage

See also   * [Draft Tray](Draft_Tray.md), [Draft Snap](Draft_Snap.md) and [Draft Constrain](Draft_Constrain.md).


<div class="mw-translate-fuzzy">

## Použití

1.  Stiskněte tlačítko **<img src="images/Draft_BSpline.png" width=16px> [B-křivka](Draft_BSpline.md)
** nebo klávesy **B** potom **S**
2.  Klikněte na první bod ve 3D pohledu nebo zadejte jeho souřadnice
3.  Klikněte na další bod ve 3D pohledu nebo zadejte jeho souřadnice
4.  Stiskněte klávesu **F** nebo **C** nebo dvojklikněte na poslední bod pro ukončení nebo uzavření křivky. Je-li křivka uzavřena, bude zároveň i povrchem i když se jeví jako drátový model.


</div>

## Options

The single character keyboard shortcuts available in the task panel can be changed. See [Draft Preferences](Draft_Preferences.md). The shortcuts mentioned here are the default shortcuts.


<div class="mw-translate-fuzzy">

## Volby

-   Stiskněte klávesu **F** nebo tlačítko **<img src="images/Draft_FinishLine.png" width=12px> '''Ukončení'''** pro ukončení křivky bez jejího uzavření
-   Stiskněte klávesu **C** nebo tlačítko **<img src="images/Draft_CloseLine.png" width=12px> '''Uzavření'''** nebo klikněte na počáteční bod. Tím ukončíte zadávání, ale zároveň se doplní poslední segment křivky, který poslední bod spojí s počátečním bodem.
-   Stisknutím klávesy **X**, **Y** nebo **Z** po zadání bodu zajistíte, že následující bod bude ležet na dané ose.
-   Pro ruční zadávání souřadnic jednoduše zadávejte čísla a mezi každou komponentou X, Y a Z stiskněte **ENTER**.
-   Stiskněte klávesu **R** nebo klikněte/odklikněte zaklikávací políčko **'''Relativní'''**. Je-li nastaven relativní mód jsou souřadnice následujícího bodu relativní k předchozímu bodu. Je-li mód absolutní souřadnice jsou vztaženy k počátečnímu bodu (0,0,0).
-   Stiskněte klávesu **T** nebo klikněte/odklikněte zaklikávací políčko **'''Pokračovat'''**. Je-li nastaven pokračovací mód, nástroj B-křivka bude po ukončení křivky restartován a připraven ke kreslení další křivky bez nutnosti znovu jej spouštět klikáním na tlačítko B-křivka.
-   Stiskněte při kreslení klávesu **CTRL** pro [přichycení](Draft_Snap.md) Vašeho bodu k nejbližšímu uchopovacímu místu, nezávisle na vzdálenosti od něho.
-   Stiskněte při kreslení klávesu **SHIFT** pro nastavení [vazby](Draft_Constrain.md) Vašeho dalšího bodu vodorovně nebo svisle v relaci k předchozímu bodu.
-   Stiskněte klávesu **W** nebo stiskněte tlačítko **<img src="images/Draft_Wipe.png" width=12px> '''Smaž'''** pro odstranění existujících segmentů a začněte křivku z posledního bodu.
-   Stiskněte klávesy **CTRL**+**Z** nebo tlačítko **<img src="images/Draft_UndoLine.png" width=12px> '''Undo'''** k návratu na poslední bod.
-   Stiskněte klávesu **I** nebo tlačítko **'''Filled'''** aby se křivka po jejím uzavření zobrazovala jako plocha. To jednoduše nastavuje Pohled-\>Vlastnost Drát na \"Otevřené čáry\" nebo \"Drátový model\", toto také může být snadno změněno později.
-   Stiskněte klávesu **ESC** nebo tlačítko **'''Cancel'''** pro ukončení aktuálního příkazu B-křivka.
-   B-křivky mohou v zobrazovacím módu \"Jednoduché čáry\" zobrazovat šrafovací vzory nastavením vlastnosti \"Vzor\" dole.


</div>

## Notes

-   A Draft BSpline can be edited with the [Draft Edit](Draft_Edit.md) command.
-   A Draft BSpline can be converted to a [Draft Wire](Draft_Wire.md) with the [Draft WireToBSpline](Draft_WireToBSpline.md) command.

## Preferences

See also   * [Preferences Editor](Preferences_Editor.md) and [Draft Preferences](Draft_Preferences.md).

-   To change the number of decimals used for the input of coordinates   * **Edit → Preferences... → General → Units → Units settings → Number of decimals**.
-   To change the initial value of filled mode   * **Edit → Preferences... → Draft → General settings → Draft tools options → Fill objects with faces whenever possible**. Changing the filled mode in a task panel will override this preference for the current FreeCAD session.


<div class="mw-translate-fuzzy">

## Vlastnosti

-    **Uzavřená**   * Specifikuje zda je křivka uzavřená nebo ne

-    **Koncová šipka**   * Ukazuje sumbol šipky na koncovém bodě křivky, takže ten může být použit jako linka pro vysvělivku

-    **Vzor**   * Specifikuje šrafovací vzor pro vyplnění drátu

-    **Rozměr vzoru**   * Specifikuje rozměr šrafovacího vzoru


</div>

See also   * [Property editor](Property_editor.md).

A Draft BSpline object is derived from a [Part Part2DObject](Part_Part2DObject.md) and inherits all its properties. It also has the following additional properties   *

### Data


{{TitleProperty|Draft}}

-    **Area|Area**   * (read-only) specifies the area of the face of the spline. The value will be {{value|0.0}} if **Make Face** if `False` or the face cannot be created.

-    **Closed|Bool**   * specifies if the spline is closed or not. If the spline is initially open this value is `False`, setting it to `True` will draw a curve segment to close the spline. If the spline is initially closed this value is `True`, setting it to `False` will remove the last curve segment and make the spline open.

-    **Make Face|Bool**   * specifies if the spline makes a face or not. If it is `True` a face is created, otherwise only the perimeter is considered part of the object. This property only works if **Closed** is `True` and if the spline does not self-intersect.

-    **Parameterization|Float**   * affects the shape of the spline.

-    **Points|VectorList**   * specifies the points of the spline in its local coordinate system.

### View


{{TitleProperty|Draft}}

-    **Arrow Size|Length**   * specifies the size of the symbol displayed at the end of the spline.

-    **Arrow Type|Enumeration**   * specifies the type of symbol displayed at the end of the spline, which can be {{value|Dot}}, {{value|Circle}}, {{value|Arrow}}, {{value|Tick}} or {{value|Tick-2}}.

-    **End Arrow|Bool**   * specifies whether to show a symbol at the end of the spline, so it can be used as an annotation line.

-    **Pattern|Enumeration**   * specifies the [Draft Pattern](Draft_Pattern.md) with which to fill the face of the closed spline. This property only works if **Make Face** is `True` and if **Display Mode** is {{value|Flat Lines}}.

-    **Pattern Size|Float**   * specifies the size of the [Draft Pattern](Draft_Pattern.md).

## Scripting


<div class="mw-translate-fuzzy">

## Skriptování

Nástroj B-křivka může být využit v [makrech](macros.md) a z konzoly Pythonu použitím následující funkce   *


</div>

To create a Draft BSpline use the `make_bspline` method (<small>(v0.19)</small> ) of the Draft module. This method replaces the deprecated `makeBSpline` method.


```python
bspline = make_bspline(pointslist, closed=False, placement=None, face=None, support=None)
bspline = make_bspline(Part.Wire, closed=False, placement=None, face=None, support=None)
```


<div class="mw-translate-fuzzy">

-   Vytváří objekt B-křivka podle daného seznamu vektorů (pointslist).
-   Je-li closed True nebo jsou-li první a poslední bod identické, drát je uzavřen.
-   Je-li face (plocha) True (a křivka je uzavřena), bude se křivka jevit jako vyplněná plocha.
-   Místo seznamu bodů můžete vložit Drát (Part Wire) (lomená čára).
-   Vrací nově vytvořený objekt.


</div>


<div class="mw-translate-fuzzy">

Příklad   *


</div>


```python
import FreeCAD as App
import Draft

doc = App.newDocument()

p1 = App.Vector(0, 0, 0)
p2 = App.Vector(1000, 1000, 0)
p3 = App.Vector(2000, 0, 0)

spline1 = Draft.make_bspline([p1, p2, p3], closed=False)
spline2 = Draft.make_bspline([p1, 2*p3, 1.3*p2], closed=False)
spline3 = Draft.make_bspline([1.3*p3, p1, -1.7*p2], closed=False)

doc.recompute()
```



---
![](images/Right_arrow.png) [documentation index](../README.md) > [Draft](Draft_Workbench.md) > Draft BSpline/cs
