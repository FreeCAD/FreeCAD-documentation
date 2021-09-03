---
- GuiCommand:   Name:Draft Extension   Workbenches:[Arch](Draft_Workbench___Draft]],_[[Arch_Workbench.md)|MenuLocation:Draft → [[Draft Snap   Snap]] → Extension|Shortcut:   SeeAlso:---


</div>

## Descripción

Este método se ajusta a un punto en una línea imaginaria que se extiende más allá de los puntos finales de los segmentos de línea.

<img alt="" src=images/Draft_Snap_Extension.png  style="width:400px;">


*Snapping the second point of a line to the extension of another line*

## Utilización

1.  Asegúrese de que {{Button | <img src="images/_Snap_Lock.svg_" width= 16px> [ Draft ToggleSnap](Draft_ToggleSnap_.md)}} y **<img src="images/Snap_Extension.svg" width=16px> [Snap Extension](Draft_Extension.md)** está activada.
2.  Elija una herramienta de borrador para dibujar una forma.
3.  Coloque el cursor cerca de los puntos finales del segmento de línea que desea extender.
4.  Al alejar el puntero del segmento de línea, pero manteniendo la misma pendiente, la línea discontinua indica la extensión de la línea original.
5.  Haga clic para adjuntar su nuevo punto.










The <img alt="" src=images/Draft_Snap_Extension.svg  style="width:24px;"> **Draft Snap Extension** option snaps to an imaginary line that extends beyond the endpoints of straight edges. The edges can belong to [Draft](Draft_Workbench.md) or [Arch](Arch_Workbench.md) objects but also to objects created with other [workbenches](Workbenches.md).

Up to two edged can be referenced by this snap option and [Draft Snap Parallel](Draft_Snap_Parallel.md), making it possible to snap to virtual intersections. Both snap options can also be combined with other snap options.

![](images/Draft_Snap_Extension_example.png ) *Snapping the second point of a line to the extension of an edge*

## Usage

For general information about snapping see [Draft Snap](Draft_Snap.md).

1.  Make sure snapping is enabled. See <img alt="" src=images/Draft_Snap_Lock.svg  style="width:16px;"> [Draft Snap Lock](Draft_Snap_Lock.md).
2.  If **Draft Snap Extension** is not active do one of the following:
    -   Press the **<img src="images/Draft_Snap_Extension.svg" width=16px>** button in the Draft Snap toolbar.
    -   Press the **<img src="images/Draft_Snap_Lock.svg" width=16px><img src="images/Toolbar_flyout_arrow.svg" width=8px>** button in the [Draft snap widget](Draft_snap_widget.md) and in the menu select the **<img src="images/Draft_Snap_Extension.svg" width=16px> Snap Extension** option.
3.  Choose a [Draft](Draft_Workbench.md) or [Arch](Arch_Workbench.md) command to create your geometry.
4.  Note that you can also change snap options while a command is active.
5.  Move the cursor over a straight edge.
6.  The edge is highlighted.
7.  If you now move the cursor beyond the endpoints of the edge, you will see a dashed line appear when the cursor is on the extended edge.
8.  The point is marked and the <img alt="" src=images/Draft_Snap_Extension.svg  style="width:16px;"> icon is displayed near the cursor.
9.  Click to confirm the point.

## Preferences

See [Draft Snap](Draft_Snap#Preferences.md).





 
