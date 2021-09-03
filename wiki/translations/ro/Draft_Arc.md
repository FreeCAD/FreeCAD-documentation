---
- GuiCommand:/ro   Name:Draft Arc   Name/ro:Arc de Cerc   Workbenches:[Arch](Draft_Module/ro___Draft]],_[[Arch_Module/ro.md)|MenuLocation:Draft → Arc   Shortcut:A R   SeeAlso:[Draft Circle](Draft_Circle/ro.md)---


</div>


<div class="mw-translate-fuzzy">

## Descriere

Instrumentul Arc crează un arc în planul curent [work plan](Draft_SelectPlane/ro.md) introducând patru puncte, centrul, raza, primul punct și ultimul punct sau prin alegerea de tangente sau orice combinație a acestora. Este nevoie de [linewidth and color](Draft_Linestyle/ro.md) setată anterior pe fila Activități. Acest instrument funcționează la fel ca instrumentul [Draft Circle](Draft_Circle/ro.md), dar adaugă unghiuri de început și de sfârșit.


</div>

The <img alt="" src=images/Draft_Arc.svg  style="width:24px;"> **Draft Arc** command creates a circular arc in the current [working plane](Draft_SelectPlane.md) from a center, a radius, a start angle and an aperture angle. The radius and the angles can be defined by picking points.

A Draft Arc is in fact a [Draft Circle](Draft_Circle.md) with a **First Angle** that is not the same as its **Last Angle**.

<img alt="" src=images/Draft_Arc_example.jpg  style="width:400px;">


<div class="mw-translate-fuzzy">

<img alt="" src=images/Draft_Arc_example.jpg  style="width:400px;">


</div>

## Usage

See also: [Draft Tray](Draft_Tray.md), [Draft Snap](Draft_Snap.md) and [Draft Constrain](Draft_Constrain.md).


<div class="mw-translate-fuzzy">

## Cum se folosește 

1.  Apăsați butonul **<img src="images/Draft_Arc.png" width=16px> [Draft Arc](Draft_Arc/ro.md)
** button, or press **A** sau apăsați tastele **A** apoi **R**
2.  Faceți clic pe un prim punct din vizualizarea 3D sau tastați un [coordinate](Draft_Coordinates/ro.md)
3.  Faceți clic pe un al doilea punct din vizualizarea 3D sau introduceți o valoare de rază
4.  Faceți clic pe un al treilea punct din vizualizarea 3D sau introduceți un unghi de pornire
5.  Faceți clic pe un al patrulea punct din vizualizarea 3D sau introduceți un unghi final


</div>

## Options

The single character keyboard shortcuts available in the task panel can be changed. See [Draft Preferences](Draft_Preferences.md). The shortcuts mentioned here are the default shortcuts.


<div class="mw-translate-fuzzy">

## Opțiuni

-   Utilizarea primară a instrumentului arc este prin alegerea a patru puncte: centrul, un punct pe circumferință, definind raza, un al treilea punct care definește începutul arcului, iar al patrulea definește sfârșitul.
-   Prin apăsarea tastei **ALT**, puteți selecta o tangentă în locul punctului de selectare, pentru a defini cercul de bază al arcului. Prin urmare, puteți construi mai multe tipuri de cercuri selectând una, două sau trei tangente.
-   Direcția arcului depinde de mișcarea pe care o faceți cu mouse-ul. Dacă începeți să vă mișcați în sensul acelor de ceasornic după introducerea celui de-al treilea punct, arcul va merge în sensul acelor de ceasornic. Pentru a merge în sens invers acelor de ceasornic, pur și simplu mișcați mouse-ul înapoi peste cel de-al treilea punct, până când arcul începe să tragă în cealaltă direcție.
-   Pentru a introduce manual coordonatele, pur și simplu introduceți numerele, apoi apăsați **ENTER** între fiecare componentă X, Y și Z.
-   Apăsați tasta **T** sau faceți clic pe caseta de selectare pentru a bifa/debifa butonul **'''Continue'''**. Dacă modul continuat este activat, instrumentul Arc va reporni după ce dați cel de-al patrulea punct, permițându-vă să desenați un alt arc fără să apăsați din nou butonul Arc.
-   Apăsați **CTRL** în timp ce desenați pentru a forța [snapping](Draft_Snap/ro.md) punctul dvs. către cea mai apropiată locație, independent de distanța.
-   Apăsați **SHIFT** în timp ce desenați [constrain](Draft_Constrain/ro.md) punctul dvs. orizontal sau vertical în raport cu centrul.
-   Apăsați butonul **ESC** sau butonul **'''Anulare'''** pentru a întrerupe comanda curentă.
-   Arcul poate fi transformat într-un cerc după creare, prin stabilirea aceleiași valori la propriul său unghi și proprietăți ultimul unghi.


</div>

## Notes

-   A Draft Arc can be edited with the [Draft Edit](Draft_Edit.md) command.

## Preferences

See also: [Preferences Editor](Preferences_Editor.md) and [Draft Preferences](Draft_Preferences.md).

-   To change the number of decimals used for the input of coordinates, radii and angles: **Edit → Preferences... → General → Units → Units settings → Number of decimals**.
-   If the **Edit → Preferences... → Draft → General settings → Draft tools options → Use Part Primitives when available** option is checked, the command will create a [Part Circle](Part_Circle.md) instead of a Draft Circle.

## Properties


<div class="mw-translate-fuzzy">

## Proprietăți

-    {{PropertyData/ro|Radius}}: Raza arcului de cerc

-    {{PropertyData/ro|First Angle}}: Unghiul primului punct al arcului de cerc

-    {{PropertyData/ro|Last Angle}}: Unghiul ultimului punct al arcului de cerc


</div>

## Scripting


<div class="mw-translate-fuzzy">

## Scripturi

Instrumentul Circle poate fi de asemenea utilizat pentru a crea arce în [macros](macros/ro.md) și din consola Python utilizând următoarea funcție, oferindu-i argumente suplimentare:


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





 
