---
- GuiCommand   */ro
   Name   *Draft Move
   Name/ro   *Draft Move
   MenuLocation   *Draft → Move
   Workbenches   *[Draft](Draft_Workbench/ro.md), [Arch](Arch_Workbench/ro.md)
   Shortcut   ***M** **V**
   Version   *0.7
   SeeAlso   *[Draft SubelementHighlight](Draft_SubelementHighlight.md)
---

# Draft Move/ro


</div>

## Descriere


<div class="mw-translate-fuzzy">

Instrumentul Mutare deplasează sau copiază obiectele selectate dintr-un punct în altul pe [work plane](Draft_SelectPlane.md). Dacă nu este selectat niciun obiect, veți fi invitat să selectați unul.


</div>

The command can be used on 2D objects created with the [Draft Workbench](Draft_Workbench.md) or [Sketcher Workbench](Sketcher_Workbench.md), but also on many 3D objects such as those created with the [Part Workbench](Part_Workbench.md), [PartDesign Workbench](PartDesign_Workbench.md) or [Arch Workbench](Arch_Workbench.md).

<img alt="" src=images/Draft_Move_example.jpg  style="width   *400px;"> 
*Moving an object from one point to another*

## Cum se folosește 

See also   * [Draft Snap](Draft_Snap.md) and [Draft Constrain](Draft_Constrain.md).


<div class="mw-translate-fuzzy">

1.  Select objects you wish to move or copy
2.  Press the **<img src="images/Draft_Move.png" width=16px> [[Draft Move]]** button, or press **M** then **V** keys
3.  Click a first point on the 3D view, or type a coordinate
4.  Click another point on the 3D view, or type a coordinate


</div>

## Opţiuni

The single character keyboard shortcuts mentioned here can be changed. See [Draft Preferences](Draft_Preferences.md).


<div class="mw-translate-fuzzy">

-   Apăsați {{KEY | X}}, {{KEY | Y}} sau {{KEY | Z}} după un punct pentru a restrânge următorul punct de pe axa dată.
-   Pentru a introduce manual coordonatele, pur și simplu introduceți numerele, apoi apăsați {{KEY | ENTER}} între fiecare componentă X, Y și Z.
-   Apăsați tasta {{KEY | R}} sau faceți clic pe caseta de selectare pentru a bifa / debifa butonul {{KEY | '' 'Relativ' ''}}. Dacă modul relativ este activ, coordonatele punctului următor sunt relativ la ultima. Dacă nu, ele sunt absolute, luate din punctul de origine (0,0,0).
-   Apăsați tasta {{KEY | T}} sau faceți clic pe caseta de selectare pentru a bifa / debifa butonul {{KEY | '' 'Continue' '}}. Dacă modul continuat este activat, instrumentul Mutare se va reporni după ce îl terminați sau îl închideți, permițându-vă să mutați sau să copiați obiectele altfel fără să apăsați din nou butonul Mutare.
-   Apăsând butonul {{KEY | ALT}} sau {{KEY | C}} sau făcând clic pe butonul {{KEY | '''Copiere'''}} va face o copie a obiectelor, în loc să le mutați. Dacă țineți apăsat {{KEY | ALT}} după ce faceți clic pe cel de-al doilea punct, veți putea plasa mai multe copii până când eliberați tasta {{KEY | ALT}}.
-   Apăsați {{KEY | CTRL}} în timp ce desenați pentru a forța ancorarea [ snapping](Draft_Snap.md) punctul dvs. către cea mai apropiată locație, independent de distanță.
-   Apăsați pe {{KEY | SHIFT}} în timp ce desenați [ constrain](Draft_Constrain.md) următorul punct pe orizontală sau pe verticală în raport cu ultimul.
-   Apăsați butonul {{KEY | ESC}} sau butonul {{KEY | '''Anulare'''}} pentru a întrerupe comanda curentă.


</div>

## Notes

-   An Object that is [attached](Part_EditAttachment.md) cannot be moved with the Draft Move command. To move it either its **Support** object has to be moved, or its **Attachment Offset** has to be changed.

## Preferences

See also   * [Preferences Editor](Preferences_Editor.md) and [Draft Preferences](Draft_Preferences.md).

-   To change the number of decimals used for the input of coordinates, lengths and angles   * **Edit → Preferences... → General → Units → Units settings → Number of decimals**.
-   To change the initial focus of the task panel to the **Length** input box   * **Edit → Preferences... → Draft → General settings → Draft tools options → Set focus on Length instead of X coordinate**. Note that you must move the pointer in the [3D view](3D_view.md) for the change to take effect.
-   To store and reuse the same copy mode setting across commands   * **Edit → Preferences... → Draft → General settings → Draft tools options → Global copy mode**.
-   To reselect the base objects after copying objects   * **Edit → Preferences... → Draft → General settings → Draft tools options → Select base objects after copying**.

## Scripting


<div class="mw-translate-fuzzy">

## Script


</div>


<div class="mw-translate-fuzzy">

Instrumentul de mutare poate fi folosit în [macros](macros.md) și din consola python utilizând următoarea funcție   *


</div>


```python
moved_list = move(objectslist, vector, copy=False)
```


<div class="mw-translate-fuzzy">

-   Mută obiectul dat sau obiectele conținute în lista dată în direcția și distanța indicată de vectorul dat.
-   Dacă copymode este True, obiectele reale nu sunt mutate, în schimb sunt create copii. Returnează obiectele (sau copiile lor dacă modelul de copiere a fost Tru)
-   Se întoarce o listă a obiectului mutat (sau a copiilor)


</div>

Exempluː


```python
import FreeCAD as App
import Draft

doc = App.newDocument()

polygon1 = Draft.make_polygon(5, radius=1000)
polygon2 = Draft.make_polygon(3, radius=500)
polygon3 = Draft.make_polygon(6, radius=220)

Draft.move(polygon1, App.Vector(500, 500, 0))
Draft.move(polygon1, App.Vector(500, 500, 0))
Draft.move(polygon2, App.Vector(1000, -1000, 0))
Draft.move(polygon3, App.Vector(-500, -500, 0))

list1 = [polygon1, polygon2, polygon3]

vector = App.Vector(-2000, -2000, 0)
list2 = Draft.move(list1, vector, copy=True)
list3 = Draft.move(list1, -2*vector, copy=True)

doc.recompute()
```



---
![](images/Right_arrow.png) [documentation index](../README.md) > [Draft](Draft_Workbench.md) > Draft Move/ro
