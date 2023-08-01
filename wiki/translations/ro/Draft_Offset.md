---
- GuiCommand:
   Name:Draft Offset
   Name/ro:Draft Offset
   MenuLocation:Draft - Offset
   Workbenches:[Draft](Draft_Workbench/ro.md), [Arch](Arch_Workbench/ro.md)
   Shortcut:**O** **S**
   SeeAlso:[Part 2D Offset](Part_Offset2D/ro.md)
---

# Draft Offset/ro


</div>

## Descriere


<div class="mw-translate-fuzzy">

Instrumentul Decalare deplasează obiectele selectate la o o distanță dată față de durentul paln [work plane](Draft_SelectPlane.md). Dacă nu este selectat niciun obiect, veți fi invitat să selectați unul.


</div>

<img alt="" src=images/Draft_Offset_example.jpg  style="width:400px;"> 
*Offsetting a Draft Wire*


<div class="mw-translate-fuzzy">

## Cum se folosește 


</div>

See also: [Draft Snap](Draft_Snap.md) and [Draft Constrain](Draft_Constrain.md).


<div class="mw-translate-fuzzy">

1.  Selectați obiectele pe care doriți să le compensați
2.  Apăsați butonul **<img src="images/Draft_Offset.png" width=16px> [[Draft Offset]]
** sau apăsați tasta **O** urmată apoi de tasta **S**
3.  Faceți clic pe un punct din vizualizarea 3D sau tastați o distanță.


</div>

## Opţiuni

The single character keyboard shortcuts and the modifier keys mentioned here can be changed. See [Draft Preferences](Draft_Preferences.md).


<div class="mw-translate-fuzzy">

-   Apăsați tasta **T** sau faceți clic pe caseta de selectare pentru a bifa/debifa butonul **'''Continue''''**. Dacă funcția continuă este activată, instrumentul Offset se va reporni după ce îl terminați sau închideți, permițându-vă să decalați sau să copiați obiectele altfel fără să apăsați din nou butonul Offset.
-   Apăsând butonul **ALT** sau **C** sau făcând clic pe butonul ** '''Copiere'''** va face o copie a obiectelor, în loc să le mutați. Dacă țineți apăsat **ALT** după ce faceți clic pe cel de-al doilea punct, veți putea plasa mai multe copii până când eliberați tasta {{KEY |ALT}}.
-   Apăsați **CTRL** în timp ce desenați pentru a forța ancorarea [snapping](Draft_Snap.md) punctului dvs. către cea mai apropiată locație, independent de distanța.
-   Apăsând pe **SHIFT**, [constrain](Draft_Constrain.md) vă va fi segmentul curent, în loc să-l alegeți cel mai apropiat.
-   Apăsați butonul {{KEY | ESC}} sau butonul {{KEY | '''Anulare'''}} pentru a întrerupe comanda curentă.


</div>

## Notes

-   To create an offset version of a [Draft BSpline](Draft_BSpline.md) its points are offset individually, and from the new points a new spline is calculated. This new spline is not parallel to the original spline. For an exact parallel offset of a [Draft BSpline](Draft_BSpline.md) the [Part Offset2D](Part_Offset2D.md) command should be used.
-   The Draft Offset command cannot handle [Draft BezCurves](Draft_BezCurve.md). Use the [Part Offset2D](Part_Offset2D.md) command instead.

## Preferences

See also: [Preferences Editor](Preferences_Editor.md) and [Draft Preferences](Draft_Preferences.md).

-   To change the number of decimals used for the input of the distance: **Edit → Preferences... → General → Units → Units settings → Number of decimals**.

## Scripting


<div class="mw-translate-fuzzy">

## Scrip-Programare 


</div>


<div class="mw-translate-fuzzy">

Instrumentul de Decalare poate fi folosit în [macros](macros.md) și din consola Python utilizând următoarea funcție:


</div>


```python
offset_obj = offset(obj, delta, copy=False, bind=False, sym=False, occ=False)
```


<div class="mw-translate-fuzzy">

-   Se decalează/compensează filamentul dat prin aplicarea Vectorului dat la primul său vârf.
-   Dacă copymode este True, un alt obiect este creat, altfel același obiect devine offset.
-   Dacă bind este adevărat și cu condiția ca filamentul să fie deschis, firele originale și cele compensate vor fi legate de punctele lor finale, formând o fațetă.
-   Dacă sym este True, decalajul se face pe ambele fețe, lățimea totală fiind lungimea vectorului dat.
-   Returnează obiectul offset (sau copia lui dacă copymode este True).


</div>

Exempluː


```python
import FreeCAD as App
import Draft

doc = App.newDocument()

p1 = App.Vector(0, 0, 0)
p2 = App.Vector(1500, 2000, 0)
p3 = App.Vector(4000, 0, 0)

wire = Draft.make_wire([p1, p2, p3])
doc.recompute()

vector = App.Vector(-200, 150, 0)
offset1 = Draft.offset(wire, vector, copy=True, bind=True, sym=True)
offset2 = Draft.offset(wire, 3*vector, copy=True)
offset3 = Draft.offset(wire, 6*vector, copy=True)
offset4 = Draft.offset(wire, 9*vector, copy=True)
offset5 = Draft.offset(wire, 1.5*vector, copy=True, occ=True)

doc.recompute()
```



---
![](images/Button_right.svg) [documentation index](../README.md) > [Draft](Draft_Workbench.md) > Draft Offset/ro
