# Draft Snap/it
<div class="mw-translate-fuzzy">





</div>


{{TOCright}}

## Descrizione


<div class="mw-translate-fuzzy">

Gli <img alt="" src=images/Workbench_Draft.svg  style="width:24px;"> [Ambiente Bozza](Draft_Workbench/it.md) strumenti consentono di scegliere punti e distanze cliccando sulla [vista 3D](3D_view/it.md) con il puntatore, o inserendo le coordinate nel [pannelo azioni](Task_panel/it.md) dello strumento.


</div>

Snapping is available with most [Draft](Draft_Workbench.md) and [Arch](Arch_Workbench.md) commands.

![](images/Draft_Snap_Endpoint_example.png )


<div class="mw-translate-fuzzy">



*Linea agganciata perpendicolarmente su un'altra linea*


</div>

## Snap tools 

These tools are available in the Draft snap toolbar and in the [Draft snap widget](Draft_snap_widget.md).

Note that circular edges do not have to be full circles.

-   <img alt="" src=images/Draft_Snap_Lock.svg  style="width:32px;"> [Snap Lock](Draft_Snap_Lock.md): enables or disables snapping globally.

-   <img alt="" src=images/Draft_Snap_Endpoint.svg  style="width:32px;"> [Snap Endpoint](Draft_Snap_Endpoint.md): snaps to the endpoints of edges.

-   <img alt="" src=images/Draft_Snap_Midpoint.svg  style="width:32px;"> [Snap Midpoint](Draft_Snap_Midpoint.md): snaps to the midpoint of edges.

-   <img alt="" src=images/Draft_Snap_Center.svg  style="width:32px;"> [Snap Center](Draft_Snap_Center.md): snaps to the center point of faces and circular edges, and to the **Placement** point of [Draft WorkingPlaneProxies](Draft_WorkingPlaneProxy.md) and [Arch BuildingParts](Arch_BuildingPart.md).

-   <img alt="" src=images/Draft_Snap_Angle.svg  style="width:32px;"> [Snap Angle](Draft_Snap_Angle.md): snaps to the special cardinal points on circular edges, at multiples of 30° and 45°.

-   <img alt="" src=images/Draft_Snap_Intersection.svg  style="width:32px;"> [Snap Intersection](Draft_Snap_Intersection.md): snaps to the intersection of two edges.

-   <img alt="" src=images/Draft_Snap_Perpendicular.svg  style="width:32px;"> [Snap Perpendicular](Draft_Snap_Perpendicular.md): snaps to the perpendicular points on faces (<small>(v1.0)</small> ) and edges.

-   <img alt="" src=images/Draft_Snap_Extension.svg  style="width:32px;"> [Snap Extension](Draft_Snap_Extension.md): snaps to an imaginary line that extends beyond the endpoints of straight edges.

-   <img alt="" src=images/Draft_Snap_Parallel.svg  style="width:32px;"> [Snap Parallel](Draft_Snap_Parallel.md): snaps to an imaginary line parallel to straight edges.

-   <img alt="" src=images/Draft_Snap_Special.svg  style="width:32px;"> [Snap Special](Draft_Snap_Special.md): snaps to special points defined by the object.

-   <img alt="" src=images/Draft_Snap_Near.svg  style="width:32px;"> [Snap Near](Draft_Snap_Near.md): snaps to the nearest point on faces and edges.

-   <img alt="" src=images/Draft_Snap_Ortho.svg  style="width:32px;"> [Snap Ortho](Draft_Snap_Ortho.md): snaps to imaginary lines that cross the previous point at multiples of 45°.

-   <img alt="" src=images/Draft_Snap_Grid.svg  style="width:32px;"> [Snap Grid](Draft_Snap_Grid.md): snaps to the intersections of grid lines.

-   <img alt="" src=images/Draft_Snap_WorkingPlane.svg  style="width:32px;"> [Snap WorkingPlane](Draft_Snap_WorkingPlane.md): projects snap points onto the current [working plane](Draft_SelectPlane.md).

-   <img alt="" src=images/Draft_Snap_Dimensions.svg  style="width:32px;"> [Snap Dimensions](Draft_Snap_Dimensions.md): shows temporary X and Y dimensions.

-   <img alt="" src=images/Draft_ToggleGrid.svg  style="width:32px;"> [Toggle Grid](Draft_ToggleGrid.md): switches the grid on or off.


<div class="mw-translate-fuzzy">

### Aggancio avanzato 


</div>


<div class="mw-translate-fuzzy">

-   Ulteriori posizioni di aggancio possono essere ottenute combinando due metodi di snap, come [Ortogonale](Draft_Snap_Ortho/it.md) e [Estensione](Draft_Snap_Extension/it.md), che danno un punto di snap all\'intersezione delle loro linee immaginarie.
-   Altre posizioni di snap possono essere ottenute usando i [Vincoli](Draft_Constrain/it.md), tenendo premuto **Maiusc** o premendo **X**, **Y** o **Z** mentre si disegna.
-   Premere **Q** mentre si disegna per inserire un \"punto di attesa\" nella posizione corrente del cursore. Dopo è possibile agganciarsi ortogonalmente a questi punti di attesa e alle intersezioni dei loro assi ortogonali. Se lo snap [Punto medio](Draft_Snap_Midpoint/it.md) è abilitato, è anche possibile agganciarsi al punto medio tra due punti di attesa. {{Version/it|0.17}}


</div>

![](images/Draft_Snap_example_cycling_1.png ) 
*Snap cycling 1: The red rectangle was created first therefore it has snap priority. Without snap cycling you cannot snap to the green rectangle where it is overlapped by the red rectangle.*

![](images/Draft_Snap_example_cycling_2.png ) 
*Snap cycling 2: After using the snap cycle key once the green rectangle receives snap priority. Snapping to the midpoint of the overlapped green edge is now possible.*

## Notes


<div class="mw-translate-fuzzy">

Anche se l\'utilizzo di molti metodi di snap allo stesso tempo può essere utile per disegnare gli oggetti nelle posizioni desiderate, può anche essere problematico se il cursore si collega costantemente ai punti sbagliati. In tal caso, provare a utilizzare solo un metodo di snap alla volta.


</div>


<div class="mw-translate-fuzzy">

## Opzioni


</div>

See also: [Preferences Editor](Preferences_Editor.md) and [Draft Preferences](Draft_Preferences.md).

Note that after changing some preferences you must restart FreeCAD.


<div class="mw-translate-fuzzy">

-   La distanza massima a cui un punto è considerato un punto di snap è specificata nelle [Preferenze di Draft](Draft_Preferences/it.md), e può anche essere cambiato al volo premendo i tasti **<nowiki>[</nowiki>** (aumenta) o **<nowiki>]</nowiki>** (diminuisci).
-   Premendo **A** mentre si disegna si blocca l\'angolo corrente del segmento di linea disegnato.


</div>


<div class="mw-translate-fuzzy">





</div>



---
![](images/Right_arrow.png) [documentation index](../README.md) > [Draft](Draft_Workbench.md) > Draft Snap/it
