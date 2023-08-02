---
- GuiCommand:
   Name: Draft Snap Extension
   Name/ro: Draft Snap Extension
   MenuLocation: Draft -> Draft Snap/ro -> Extension
   Workbenches: Draft_Workbench/ro, Arch_Workbench/ro
   SeeAlso: Draft Snap/ro, Draft_Snap_Lock/ro
---

# Draft Snap Extension/ro


</div>

## Descriere


<div class="mw-translate-fuzzy">

Această metodă ancorează un punct pe o linie imaginară care se extinde dincolo de punctele finale ale segmentelor de linie.


</div>

Up to 2 (or 8 <small>(v0.20)</small> ) edges can be referenced by this snap option and [Draft Snap Parallel](Draft_Snap_Parallel.md), making it possible to snap to virtual intersections. Both snap options can also be combined with other snap options.

![](images/Draft_Snap_Extension_example.png ) 
*Snapping the second point of a line to the extension of an edge*

## Utilizare

For general information about snapping see [Draft Snap](Draft_Snap.md).


<div class="mw-translate-fuzzy">

1.  Asigurați-vă că butoanele **<img src="images/Draft_Snap_Lock.svg" width=16px> [Draft ToggleSnap](Draft_Snap_Lock.md)** și **<img src="images/Draft_Snap_Extension.svg" width=16px> [Snap Extension](Draft_Snap_Extension.md)** sunt activate.
2.  Alegeți un instrument Draft pentru a desena forma.
3.  Glisați cursorul peste punctele finale ale liniei pe care doriți să o extindeți.
4.  Pe măsură ce deplasați cursorul departe de segmentul de linie, păstrând aceeași panta, o linie punctată indică extensia liniei originale.
5.  Faceți clic pentru a atașa noul punct.


</div>

## Preferences

See [Draft Snap](Draft_Snap#Preferences.md).



---
⏵ [documentation index](../README.md) > [Draft](Draft_Workbench.md) > Draft Snap Extension/ro
