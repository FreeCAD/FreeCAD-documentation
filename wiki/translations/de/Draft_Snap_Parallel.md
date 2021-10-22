---
- GuiCommand:/de
   Name:Draft Parallel
   Name/de:Entwurf Parallel
   Workbenches:[Entwurf](Draft_Workbench/de.md), [Arch](Arch_Workbench/de.md)
   MenuLocation:Entwurf → [Fangen](Draft_Snap/de.md) → Parallel
   Shortcut:-
   SeeAlso:[Fangen](Draft_Snap/de.md), [Fangen ein/aus](Draft_ToggleSnap/de.md)
---

# Draft Snap Parallel/de


</div>

## Beschreibung


<div class="mw-translate-fuzzy">

Diese Methode fängt einen Punkt einer imaginären Linie, die parallel zu einer anderen Linie ist.


</div>

Up to two edges can be referenced by this snap option and [Draft Snap Extension](Draft_Snap_Extension.md), making it possible to snap to virtual intersections. Both snap options can also be combined with other snap options.

This snap option currently does not work if the cursor is next to the referenced edge. You must move the cursor to an area beyond the endpoints of the edge.

![](images/Draft_Snap_Parallel_example.png )


<div class="mw-translate-fuzzy">



*Fangen des zweiten Punktes einer Linie auf einer unsichtbaren Linie, die parallel zur Referenzlinie verläuft.*


</div>

## Anwendung

For general information about snapping see [Draft Snap](Draft_Snap.md).


<div class="mw-translate-fuzzy">

1.  
    **<img src="images/Snap_Lock.svg" width=16px> [Fangen ein/aus](Draft_ToggleSnap/de.md)**und **<img src="images/Snap_Parallel.svg" width=16px> [ Parallel fangen](Draft_Parallel/de.md)** einschalten.

2.  Mit <img alt="" src=images/Draft_Line.svg  style="width:16px;"> [Entwurfslinie](Draft_Line/de.md) eine Form zeichen. Den ersten Punkt eingeben.

3.  Den Mauszeiger über die Linie führen, die als Bezug verwendet werden soll.

4.  Den Mauszeiger wegbewegen und versuchen, die gleiche Neigung wie die Referenzlinie beizubehalten, bis das Fang-Symbol erscheint.

5.  Mit einem Klick den neuen Punkt anhängen.


</div>

## Preferences

See [Draft Snap](Draft_Snap#Preferences.md).


<div class="mw-translate-fuzzy">





</div>

---
[documentation index](../README.md) > [Draft](Draft_Workbench.md) > Draft Snap Parallel/de
