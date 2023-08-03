---
 GuiCommand:
   Name: Draft Snap WorkingPlane
   Workbenches: Draft Workbench, Arch Workbench
   MenuLocation: Draft , Draft Snap , WorkingPlane
   Shortcut: 
   SeeAlso: 
---

# Draft Snap WorkingPlane/ro


</div>

## Descriere


<div class="mw-translate-fuzzy">

Modul Snap care pune întotdeauna punctul de ancorare pe planul curent [working plane](Draft_SelectPlane.md), chiar dacă faceți ancorarea pe un punct în afara planului de lucru.


</div>

![](images/Draft_Snap_WorkingPlane_example.png ) 
*Snapping the second point of a line to the projected endpoint of an edge*

## Utilizare

For general information about snapping see [Draft Snap](Draft_Snap.md).

1.  Optionally change the [working plane](Draft_SelectPlane.md).
2.  Make sure snapping is enabled. See <img alt="" src=images/Draft_Snap_Lock.svg  style="width:16px;"> [Draft Snap Lock](Draft_Snap_Lock.md).
3.  If **Draft Snap WorkingPlane** is not active do one of the following:
    -   Press the **<img src="images/Draft_Snap_WorkingPlane.svg" width=16px>** button in the Draft snap toolbar.
    -   Press the **<img src="images/Draft_Snap_WorkingPlane.svg" width=16px>** button in the [Draft snap widget](Draft_snap_widget.md).
4.  Make sure at least one other snap option is active.
5.  Choose a [Draft](Draft_Workbench.md) or [Arch](Arch_Workbench.md) command to create your geometry.
6.  Note that you can also change snap options while a command is active.
7.  Move the cursor over the object you want to snap to.
8.  The object is highlighted.
9.  If a snap point is found it is projected onto the [working plane](Draft_SelectPlane.md) where it is marked.
10. Click to confirm the point.

## Preferences

See [Draft Snap](Draft_Snap#Preferences.md).



---
⏵ [documentation index](../README.md) > [Draft](Draft_Workbench.md) > Draft Snap WorkingPlane/ro
