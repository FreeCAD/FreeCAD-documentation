---
- GuiCommand:/de
   Name:Draft Array
   Name/de:Entwurf Anordnung
   MenuLocation:Entwurf → Anordnung
   Workbenches:[Draft](Draft_Workbench/de.md), [Arch](Arch_Workbench/de.md)
   SeeAlso:[PfadDatenfeld](Draft_PathArray/de.md), [Draft PointArray](Draft_PointArray/de.md), [Draft Klonen](Draft_Clone/de.md)
---

# Draft Array/de


</div>

## Beschreibung


<div class="mw-translate-fuzzy">

Das **<img src="images/Draft_Array.svg" width=16px>[Entwurf Anordnung](Draft_Array/de.md)** Werkzeug erzeugt eine orthogonales (3-Achsen), polare oder kreisförmige Anordnung aus einem ausgewählten Objekt.


</div>


<div class="mw-translate-fuzzy">

Dieses Werkzeug kann für 2D Formen verwendet werden, die mit der [Entwurf Arbeitsbereich](Draft_Workbench/de.md) erstellt wurden, aber auch für viele Arten von 3D Objekten, wie sie mit der [Part Arbeitsbereich](Part_Workbench/de.md) oder [PartDesign Arbeitsbereich](PartDesign_Workbench/de.md) erstellt wurden.


</div>

This command is now obsolete. Use the [Draft OrthoArray](Draft_OrthoArray.md), [Draft PolarArray](Draft_PolarArray.md) or [Draft CircularArray](Draft_CircularArray.md) command instead.

## Usage


<div class="mw-translate-fuzzy">

## Verwendung

1.  Wähle ein Objekt aus, mit dem Du ein Array erstellen möchtest.
2.  Drücke den **<img src="images/Draft_Array.svg" width=16px> [Entwurf Anordnung](Draft_Array/de.md)** Schaltfläche . Wenn kein Objekt gewählt ist, wirst Du aufgefordert, eines auszuwählen.
3.  Das Anordnungsobjekt wird sofort erstellt. Du musst die Eigenschaften der Anordnung ändern, um die Anzahl und Richtung der erstellten Kopien zu ändern.


</div>

## Properties


<div class="mw-translate-fuzzy">

## Eigenschaften

-    {{PropertyData/de|Base}}: beschreibt das zu duplizierende Objekt in der Anordnung.

-    {{PropertyData/de|Array Type|Aufzählung}}: gibt den Typ der zu erstellenden Anordnung an, {{value|"ortho"}}, {{value|"polar"}}, oder {{value|"circular"}}.

-    {{PropertyData/de|Verschmelzen}}: wenn es `True` ist und die Kopien sich überschneiden, werden sie zu einer einzigen Form zusammengefügt.


</div>

## Scripting


<div class="mw-translate-fuzzy">

## Skripten


**Siehe auch:**

[Draft API](Draft_API/de.md) und [FreeCAD Skripten Gundlagen](FreeCAD_Scripting_Basics/de.md).


</div>


<div class="mw-translate-fuzzy">





</div>

---
[documentation index](../README.md) > [Draft](Draft_Workbench.md) > Draft Array/de
