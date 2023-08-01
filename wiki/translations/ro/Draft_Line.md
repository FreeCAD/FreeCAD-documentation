---
- GuiCommand:
   Name:Draft Line
   Name/ro:Draft Line
   MenuLocation:Draft - Line
   Workbenches:[Draft](Draft_Workbench/ro.md), [Arch](Arch_Workbench/ro.md)
   Shortcut:**L** **I**
   SeeAlso:[Draft Wire](Draft_Wire/ro.md)
---

# Draft Line/ro


</div>

## Description


<div class="mw-translate-fuzzy">

## Descriere

Instrumentul Linie creează o linie dreaptă, definită prin două puncte. Ea utilizează [Draft Linestyle](Draft_Linestyle.md) definită în bara de instrumente Draft. Instrumentul Linie se comportă exact ca instrumentul [Draft Wire](Draft_Wire/ro.md) , cu excepția faptului că se oprește după două puncte.


</div>

A Draft Line is in fact a [Draft Wire](Draft_Wire.md) with only two points.

<img alt="" src=images/Draft_Line_example.jpg  style="width:400px;">


<div class="mw-translate-fuzzy">

<img alt="" src=images/Draft_Line_example.jpg  style="width:400px;">


</div>

## Usage

See also: [Draft Tray](Draft_Tray.md), [Draft Snap](Draft_Snap.md) and [Draft Constrain](Draft_Constrain.md).


<div class="mw-translate-fuzzy">

## Cum se utilizează 

1.  Apăsați butonul **<img src="images/Draft_Line.png" width=16px> [Draft Line](Draft_Line/ro.md)
** sau apăsați tastele **L** apoi **I**
2.  Faceți clic pe un prim punct din vizualizarea 3D sau tastați un coordinate
3.  Faceți clic pe un al doilea punct din vizualizarea 3D sau tastați un coordinate


</div>

## Options

The single character keyboard shortcuts available in the task panel can be changed. See [Draft Preferences](Draft_Preferences.md). The shortcuts mentioned here are the default shortcuts.


<div class="mw-translate-fuzzy">

## Opțiuni

-   Apăsați **X**, **Y** sau **Z** după primul punct pentru a restrânge al doilea punct de pe axa dată.
-   Pentru a introduce manual coordonatele, pur și simplu introduceți numerele, apoi apăsați **ENTER** între fiecare componentă X, Y și Z.
-   Apăsați tasta **R** sau faceți clic pe caseta de selectare pentru a bifa/debifa butonul **'''Relativ'''**. Dacă modul relativ este activ, coordonatele celui de-al doilea punct sunt relative la prima. Dacă nu, ele sunt absolute, luate din punctul de origine (0,0,0).
-   Apăsați tasta **T** sau faceți clic pe caseta de selectare pentru a bifa/debifa butonul **'''Continue'''**. Dacă modul continuat este activat, instrumentul Linie se va reporni după ce dați cel de-al doilea punct, permițându-vă să desenați un alt segment de linie fără a apăsa din nou butonul Linie.
-   Apăsați **CTRL** în timp ce desenați pentru a forța ancorarea [snapping](Draft_Snap.md) punctul dvs. către cea mai apropiată locație, independent de distanța.
-   Apăsați **SHIFT** în timp ce desenați [constrain](Draft_Constrain.md) al doilea punct pe orizontală sau pe verticală în raport cu primul punct.
-   Apăsați tasta **CTRL** + **Z** sau apăsați pe **['Image: Draft UndoLine.png|12px] ** pentru a anula ultimul punct.
-   Apăsați butonul **ESC** sau butonul **'''Anulare'''** pentru a întrerupe comanda curentă.
-   Dacă sunt selectate mai multe linii [Draft Lines](Draft_Line/ro.md), ele pot fi transformate într-un filament prin apăsarea butonului **Upgrade Draft**.


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

## Proprietăți

-    {{PropertyData/ro|Start}}: Punctul de pornire

-    {{PropertyData/ro|End}}: Punctul final

-    {{PropertyData/ro|Subdivisions}}: Împărțirea liniei cu numărul de subdiviziuni dat <small>(v0.16/ro)</small> 


</div>

## Scripting


<div class="mw-translate-fuzzy">

## Script-Programare 

Instrumentul Linie poate fi utilizat în [macros](macros/ro.md) și din consola [Python](Python/ro.md) utilizând următoarea funcție:


</div>

To create a Draft Line use the `make_line` method (<small>(v0.19)</small> ) of the Draft module. This method replaces the deprecated `makeLine` method.


```python
line = make_line(p1, p2)
line = make_line(LineSegment)
line = make_line(Shape)
```


<div class="mw-translate-fuzzy">

-   Creează un obiect Line între cei două puncte punctele p1 și p2, fiecare definit ca FreeCAD.Vector
-   Creează un obiect Line dintr-un Part.LineSegment
-   Creează un obiect Line de la primul vârf la ultimul vârf al Shape dată
-   Se va folosi versiunea curentă [Draft Linestyle](Draft_Linestyle/ro.md)


</div>

Exempluː


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
![](images/Button_right.svg) [documentation index](../README.md) > [Draft](Draft_Workbench.md) > Draft Line/ro
