# Draft Snap/ro







{{TOCright}}

## Description


<div class="mw-translate-fuzzy">

Ancorarea(Snapping) înseamnă \"lipirea\" următorului punct 3D pe un punct existent. Snapping este disponibil cu majoritatea instrumentelor [Draft Workbench](Draft_Workbench.md) and [Arch Workbench](Arch_Workbench.md) și poate fi activat și dezactivat la nivel global cu <img alt="" src=images/Snap_Lock.png  style="width:32px;"> [Draft ToggleSnap](#Options.md) . Fiecare locație de tip snap de mai jos poate fi activată sau dezactivată individual făcând clic pe butonul corespunzător din bara de instrumente snap. 
**View → Toolbars → Draft Snap**


</div>

Snapping is available with most [Draft](Draft_Workbench.md) and [Arch](Arch_Workbench.md) commands.

![](images/Draft_Snap_Endpoint_example.png )


<div class="mw-translate-fuzzy">

![](images/Draft_Snap_example.jpg )


</div>

## Snap tools 

These tools are available in the Draft Snap toolbar and in the [Draft snap widget](Draft_snap_widget.md).

Note that circular edges do not have to be full circles.

-   <img alt="" src=images/Draft_Snap_Lock.svg  style="width:32px;"> [Snap Lock](Draft_Snap_Lock.md): enables or disables snapping globally.

-   <img alt="" src=images/Draft_Snap_Endpoint.svg  style="width:32px;"> [Snap Endpoint](Draft_Snap_Endpoint.md): snaps to the endpoints of edges.

-   <img alt="" src=images/Draft_Snap_Midpoint.svg  style="width:32px;"> [Snap Midpoint](Draft_Snap_Midpoint.md): snaps to the midpoint of straight and circular edges.

-   <img alt="" src=images/Draft_Snap_Center.svg  style="width:32px;"> [Snap Center](Draft_Snap_Center.md): snaps to the center point of faces and circular edges, and to the **Placement** point of [Draft WorkingPlaneProxies](Draft_WorkingPlaneProxy.md) and [Arch BuildingParts](Arch_BuildingPart.md).

-   <img alt="" src=images/Draft_Snap_Angle.svg  style="width:32px;"> [Snap Angle](Draft_Snap_Angle.md): snaps to the special cardinal points on circular edges, at multiples of 30° and 45°.

-   <img alt="" src=images/Draft_Snap_Intersection.svg  style="width:32px;"> [Snap Intersection](Draft_Snap_Intersection.md): snaps to the intersection of two edges.

-   <img alt="" src=images/Draft_Snap_Perpendicular.svg  style="width:32px;"> [Snap Perpendicular](Draft_Snap_Perpendicular.md): snaps to the perpendicular point on edges.

-   <img alt="" src=images/Draft_Snap_Extension.svg  style="width:32px;"> [Snap Extension](Draft_Snap_Extension.md): snaps to an imaginary line that extends beyond the endpoints of straight edges.

-   <img alt="" src=images/Draft_Snap_Parallel.svg  style="width:32px;"> [Snap Parallel](Draft_Snap_Parallel.md): snaps to an imaginary line parallel to straight edges.

-   <img alt="" src=images/Draft_Snap_Special.svg  style="width:32px;"> [Snap Special](Draft_Snap_Special.md): snaps to special points defined by the object.

-   <img alt="" src=images/Draft_Snap_Near.svg  style="width:32px;"> [Snap Near](Draft_Snap_Near.md): snaps to the nearest point on faces or edges.

-   <img alt="" src=images/Draft_Snap_Ortho.svg  style="width:32px;"> [Snap Ortho](Draft_Snap_Ortho.md): snaps to imaginary lines that cross the previous point at 0°, 45°, 90° and 135°.

-   <img alt="" src=images/Draft_Snap_Grid.svg  style="width:32px;"> [Snap Grid](Draft_Snap_Grid.md): snaps to the intersections of grid lines.

-   <img alt="" src=images/Draft_Snap_WorkingPlane.svg  style="width:32px;"> [Snap Working Plane](Draft_Snap_WorkingPlane.md): projects the snap point onto the current [working plane](Draft_SelectPlane.md).

-   <img alt="" src=images/Draft_Snap_Dimensions.svg  style="width:32px;"> [Snap Dimensions](Draft_Snap_Dimensions.md): shows temporary X and Y dimensions.

-   <img alt="" src=images/Draft_ToggleGrid.svg  style="width:32px;"> [Toggle Grid](Draft_ToggleGrid.md): switches the grid on or off.

## Advanced snapping 

-   Additional snap points can be obtained by combining two snap options. For example combining [Draft Snap Ortho](Draft_Snap_Ortho.md) and [Draft Snap Extension](Draft_Snap_Extension.md) will give you a snap point at the intersection of their imaginary lines.
-   Snapping can be combined with [constraining](Draft_Constrain.md).
-   Press **Q** to insert a \"hold point\" at the current location of the cursor. You can snap to the orthogonal axes of hold points, and to the intersections of these axes. If the [Draft Snap Midpoint](Draft_Snap_Midpoint.md) option is active, you can also snap to the midpoint between two hold points.
-   Press **** one or more times to snap to an object that is obscured by other geometry. This is called \"snap cycling\". Note that you must move the cursor by a small amount in the [3D view](3D_view.md) after pressing the key.

![](images/Draft_Snap_example_cycling_1.png ) *Snap cycling 1: The red rectangle was created first therefore it has snap priority. Without snap cycling you cannot snap to the green rectangle where it is overlapped by the red rectangle.*

![](images/Draft_Snap_example_cycling_2.png ) *Snap cycling 2: After using the snap cycle key once the green rectangle receives snap priority. Snapping to the midpoint of the overlapped green edge is now possible.*

## Notes

-   Multiple snap options can be active at the same time, but it is advisable to only activate the snap options you really need. Activating too many can slow things down.
-   It is not a good idea to have [Draft Snap Near](Draft_Snap_Near.md) permanently active as it takes precedence over many other snap options.

## Preferences

See also: [Preferences Editor](Preferences_Editor.md) and [Draft Preferences](Draft_Preferences.md).

Note that after changing some preferences you must restart FreeCAD.


<div class="mw-translate-fuzzy">

## Opțiuni

-   <img alt="" src=images/Snap_Lock.png  style="width:32px;"> [Lock](Draft_ToggleSnap.md): activează global ancorarea on/off
-   Anumite locații de fixare suplimentare pot fi obținute prin combinarea a două locații snap, cum ar fi extensia orto +, care vă va oferi un punct de fixare la intersecția liniilor lor imaginare.
-   Alte locații, mai complexe, pot fi obținute prin utilizarea [constraining](Draft_Constrain.md) (by pressing **SHIFT** or **X** or **Y** or **Z** while drawing).
-   apăsarea tastei **L** în timpul desenării, blochează unghiul curent al segmentului de linie care este desenat.
-   Distanta maxima la care un punct este capturat

și un amplasament de captură este specificat în [preferences](Draft_Preferences.md), și poate de altfel să fie schimbat din zbor apăsând tastele **<nowiki>[</nowiki>** or **<nowiki>]</nowiki>**.

-   Apăsând **Q** în timpul desenării, introduce un punct de întrerupere la poziția curentă a cursorului. Veți putea apoi să vă aliniați ortogonal acestor puncte de atașare și intersecții ale axelor lor ortogonale. Dacă este activată ancorarea la punctul median, puteți ancora, de asemenea, la jumătatea distanței dintre două puncte de întrerupere. <small>(v0.17)</small> 


</div>


<div class="mw-translate-fuzzy">


</div>


 

[Category:User Documentation/ro](Category:User_Documentation/ro.md)
