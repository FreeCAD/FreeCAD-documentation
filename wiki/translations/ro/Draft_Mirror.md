---
- GuiCommand   */ro
   Name   *Draft Mirror
   Name/ro   *Draft Mirror
   MenuLocation   *Draft → Mirror
   Workbenches   *[Draft](Draft_Workbench/ro.md), [Arch](Arch_Workbench/ro.md)
   SeeAlso   *[Draft Scale](Draft_Scale/ro.md)
---

# Draft Mirror/ro


</div>

## Description


<div class="mw-translate-fuzzy">

## Descriere

Acest instrument produce o copie în oglindă a unui obiect selectat, utilizând un obiect [Mirror Object](Part_Mirror/ro.md). Copia este legată parametric de obiectul original   * dacă se modifică obiectul original, copia oglindă se modifică și ea, dar rămâne oglindită.


</div>

The command can be used on 2D objects created with the [Draft Workbench](Draft_Workbench.md) or [Sketcher Workbench](Sketcher_Workbench.md), but also on many 3D objects such as those created with the [Part Workbench](Part_Workbench.md), [PartDesign Workbench](PartDesign_Workbench.md) or [Arch Workbench](Arch_Workbench.md).

<img alt="" src=images/Draft_Mirror_example.jpg  style="width   *400px;">


<div class="mw-translate-fuzzy">

<img alt="" src=images/Draft_Mirror_example.jpg  style="width   *400px;">


</div>

## Usage

See also   * [Draft Snap](Draft_Snap.md) and [Draft Constrain](Draft_Constrain.md).


<div class="mw-translate-fuzzy">

## Cum se utilizează 

1.  Selectați obiectele pe care doriți să le reflectați
2.  Apăsați butonul **<img src="images/Draft_Mirror.png" width=16px> [[Draft Mirror]]
**
3.  Faceți clic pe primul punct al liniei de oglindă din vizualizarea 3D sau tastați un coordinate
4.  Faceți clic pe celălalt punct al liniei de simetrie/oglindire din vizualizarea 3D sau tastați un coordinate


</div>

## Options

The single character keyboard shortcuts mentioned here can be changed. See [Draft Preferences](Draft_Preferences.md).


<div class="mw-translate-fuzzy">

## Opțiuni

-   După crearea oglinzii, legarea sa cu obiectul original poate fi eliminată folosind instrumentul [ Creare parțială simplă](Part_SimpleCopy.md).
-   Oglinda unui obiect Draft poate fi de asemenea transformată într-un Wire Draft, utilizând [Draft Downgrade](Draft_Downgrade.md) apoi [Draft Upgrade](Draft_Upgrade.md).


</div>

## Notes

-   Mirrored copies of [Draft Lines](Draft_Line.md), [Draft Wires](Draft_Wire.md), [Draft Arcs](Draft_Arc.md) and [Draft Circles](Draft_Circle.md) can be turned into independent editable Draft objects by using [Draft Downgrade](Draft_Downgrade.md) and then [Draft Upgrade](Draft_Upgrade.md).
-   The [Part SimpleCopy](Part_SimpleCopy.md) command can be used to create a copy of a mirrored object that is not linked to its source object.

## Preferences

See also   * [Preferences Editor](Preferences_Editor.md) and [Draft Preferences](Draft_Preferences.md).

-   To change the number of decimals used for the input of coordinates   * **Edit → Preferences... → General → Units → Units settings → Number of decimals**.

## Properties

See also   * [Property editor](property_editor.md).

A [Part Mirror](Part_Mirror.md) object is derived from a [Part Feature](Part_Feature.md) object and inherits all its properties. It also has the following additional properties   *

### Data


{{TitleProperty|Base}}

-    **Source|Link**   * specifies the object that is mirrored.


{{TitleProperty|Plane}}


<div class="mw-translate-fuzzy">

## Proprietăți

-    **Base**   * Baza punctului planului de simetrie

-    **Normal**   * Direcția normală la planul de simetrie


</div>

## Scripting


<div class="mw-translate-fuzzy">

## Script-Programre 

Unealta Clone poate fi folosită în [macro-uri](macros/ro.md) şi de la consola Python cu ajutorul funcţiei următoare   *


</div>

To mirror objects use the `mirror` method of the Draft module.


```python
mirrored_list = mirror(objlist, p1, p2)
```


<div class="mw-translate-fuzzy">

-   Realizează oglinda (obiectelor) obiectului dat peste un plan definit de o linie de la p1 la p2 și paralel cu vizualizarea curentă
-   Rezultatul este un obiect `Part   *   *Mirroring`
-   Dacă obiectul original se modifică, obiectul final se schimbă și el, dar rămâne oglindit


</div>

Exempluː


```python
import FreeCAD as App
import Draft

doc = App.newDocument()

place = App.Placement(FreeCAD.Vector(1000, 0, 0), App.Rotation())
polygon1 = Draft.make_polygon(3, 750)
polygon2 = Draft.make_polygon(5, 750, placement=place)

p1 = App.Vector(2000, -1000, 0)
p2 = App.Vector(2000, 1000, 0)

line1 = Draft.make_line(p1, p2)
mirrored1 = Draft.mirror(polygon1, p1, p2)

Line2 = Draft.make_line(-p1, -p2)
mirrored2 = Draft.mirror([polygon1, polygon2], -p1, -p2)

doc.recompute()
```



---
![](images/Right_arrow.png) [documentation index](../README.md) > [Draft](Draft_Workbench.md) > Draft Mirror/ro
