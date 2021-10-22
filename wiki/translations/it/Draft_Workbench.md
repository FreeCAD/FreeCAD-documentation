# <img alt="L\'icona di Draft" src=images/Workbench_Draft.svg  style="width:64px;"> Draft Workbench/it


{{TOCright}}

## Introduzione


<div class="mw-translate-fuzzy">

L\'[Ambiente Draft](Draft_Workbench/it.md) <img alt="" src=images/Workbench_Draft.svg  style="width:24px;"> consente di disegnare semplici oggetti 2D e offre diversi strumenti per modificarli in seguito. Fornisce inoltre strumenti per definire un piano di lavoro, una griglia e un sistema di snap per controllare con precisione la posizione della geometria.


</div>


<div class="mw-translate-fuzzy">

Gli oggetti 2D creati possono essere utilizzati per il disegno in modo simile a Inkscape o Autocad. Queste forme 2D possono anche essere utilizzate come componenti di base di oggetti 3D creati con altri ambienti di lavoro, ad esempio con <img alt="" src=images/Workbench_Part.svg  style="width:32px;"> _. È anche possibile convertire gli oggetti Draft in <img alt="" src=images/Workbench_Sketcher.svg  style="width:32px;"> _ per creare dei corpi solidi.


</div>

The Draft Workbench also provides tools to define a [working plane](Draft_SelectPlane.md), a [grid](Draft_Snap_Grid.md), and a [snapping system](Draft_Snap.md) to precisely control the position of geometry.


<div class="mw-translate-fuzzy">

FreeCAD è principalmente un\'applicazione di modellazione 3D, quindi i suoi strumenti 2D non sono così avanzati come in altri programmi di disegno. Se l\'obiettivo principale è la produzione di disegni 2D complessi e di file [DXF](DXF/it.md), e non si ha bisogno di modelli 3D, si può prendere in considerazione un programma software dedicato al disegno tecnico come [LibreCAD](https://en.wikipedia.org/wiki/LibreCAD), [QCad](https://en.wikipedia.org/wiki/QCad), e altri.


</div>

![](images/Draft_Workbench_Example.png ) 
*The image shows the [grid](Draft_Snap_Grid.md) aligned with the XY plane.<br>
On the left, in white, several planar objects.<br>
On the right a non-planar [Draft Wire](Draft_Wire.md) used as the Path Object of a [Draft PathArray](Draft_PathArray.md).*

## Drafting

-   <img alt="" src=images/Draft_Line.svg  style="width:32px;"> [Line](Draft_Line.md): creates a straight line.

-   <img alt="" src=images/Draft_Wire.svg  style="width:32px;"> [Polyline](Draft_Wire.md): creates a polyline, a sequence of several connected line segments.

-   <img alt="" src=images/Draft_Fillet.svg  style="width:32px;"> _. <small>(v0.19)</small> 

-   <img alt="" src=images/Draft_Arc.svg  style="width:32px;"> Arc tools

:\* <img alt="" src=images/Draft_Arc.svg  style="width:32px;"> [Arc](Draft_Arc.md): creates a circular arc from a center, a radius, a start angle and an aperture angle.

:\* <img alt="" src=images/Draft_Arc_3Points.svg  style="width:32px;"> [Arc by 3 points](Draft_Arc_3Points.md): creates a circular arc from three points that define its circumference. <small>(v0.19)</small> 

-   <img alt="" src=images/Draft_Circle.svg  style="width:32px;"> [Circle](Draft_Circle.md): creates a circle from a center and a radius.

-   <img alt="" src=images/Draft_Ellipse.svg  style="width:32px;"> [Ellipse](Draft_Ellipse.md): creates an ellipse from two points defining a rectangle in which the ellipse will fit.

-   <img alt="" src=images/Draft_Rectangle.svg  style="width:32px;"> [Rectangle](Draft_Rectangle.md): creates a rectangle from two points.

-   <img alt="" src=images/Draft_Polygon.svg  style="width:32px;"> [Polygon](Draft_Polygon.md): creates a regular polygon from a center and a radius.

-   <img alt="" src=images/Draft_BSpline.svg  style="width:32px;"> [B-spline](Draft_BSpline.md): creates a B-spline curve from several points.

-   <img alt="" src=images/Draft_CubicBezCurve.svg  style="width:32px;"> Bézier tools

:\* <img alt="" src=images/Draft_CubicBezCurve.svg  style="width:32px;"> [Cubic Bézier curve](Draft_CubicBezCurve.md): creates a Bézier curve of the third degree. <small>(v0.19)</small> 

:\* <img alt="" src=images/Draft_BezCurve.svg  style="width:32px;"> [Bézier curve](Draft_BezCurve.md): creates a Bézier curve from several points.

-   <img alt="" src=images/Draft_Point.svg  style="width:32px;"> [Point](Draft_Point.md): creates a simple point.

-   <img alt="" src=images/Draft_Facebinder.svg  style="width:32px;"> [Facebinder](Draft_Facebinder.md): creates a surface object from selected faces.

-   <img alt="" src=images/Draft_ShapeString.svg  style="width:32px;"> [ShapeString](Draft_ShapeString.md): creates a compound shape that represents a text string.

-   <img alt="" src=images/Draft_Hatch.svg  style="width:32px;"> [Hatch](Draft_Hatch.md): creates hatches on the faces of a selected object. <small>(v0.20)</small> 

## Annotation

-   <img alt="" src=images/Draft_Text.svg  style="width:32px;"> [Text](Draft_Text.md): creates a multi-line text at a given point.

-   <img alt="" src=images/Draft_Dimension.svg  style="width:32px;"> [Dimension](Draft_Dimension.md): creates a linear dimension, a radial dimension or an angular dimension.

-   <img alt="" src=images/Draft_Label.svg  style="width:32px;"> [Label](Draft_Label.md): creates a multi-line text with a 2-segment leader line and an arrow.

-   <img alt="" src=images/Draft_AnnotationStyleEditor.svg  style="width:32px;"> [Annotation styles\...](Draft_AnnotationStyleEditor.md): allows you to define styles that affect the visual properties of annotation-like objects. <small>(v0.19)</small> 

## Modification

-   <img alt="" src=images/Draft_Move.svg  style="width:32px;"> [Move](Draft_Move.md): moves or copies selected objects from one point to another.

-   <img alt="" src=images/Draft_Rotate.svg  style="width:32px;"> [Rotate](Draft_Rotate.md): rotates or copies selected objects around a center point by a given angle.

-   <img alt="" src=images/Draft_Scale.svg  style="width:32px;"> [Scale](Draft_Scale.md): scales or copies selected objects around a base point.

-   <img alt="" src=images/Draft_Mirror.svg  style="width:32px;"> [Mirror](Draft_Mirror.md): creates mirrored copies from selected objects.

-   <img alt="" src=images/Draft_Offset.svg  style="width:32px;"> [Offset](Draft_Offset.md): offsets each segment of a selected object over a given distance, or creates an offset copy of the selected object.

-   <img alt="" src=images/Draft_Trimex.svg  style="width:32px;"> [Trimex](Draft_Trimex.md): trims or extends a selected object.

-   <img alt="" src=images/Draft_Stretch.svg  style="width:32px;"> [Stretch](Draft_Stretch.md): stretches objects by moving selected points.

-   <img alt="" src=images/Draft_Clone.svg  style="width:32px;"> [Clone](Draft_Clone.md): creates linked copies, clones, of selected objects.

-   <img alt="" src=images/Draft_OrthoArray.svg  style="width:32px;"> Array tools

:\* <img alt="" src=images/Draft_OrthoArray.svg  style="width:32px;"> _ array. <small>(v0.19)</small> 

:\* <img alt="" src=images/Draft_PolarArray.svg  style="width:32px;"> _ array. <small>(v0.19)</small> 

:\* <img alt="" src=images/Draft_CircularArray.svg  style="width:32px;"> _ array. <small>(v0.19)</small> 

:\* <img alt="" src=images/Draft_PathArray.svg  style="width:32px;"> [Path array](Draft_PathArray.md): creates an array from a selected object by placing copies along a path.

:\* <img alt="" src=images/Draft_PathLinkArray.svg  style="width:32px;"> _ array instead of a regular array. <small>(v0.19)</small> 

:\* <img alt="" src=images/Draft_PointArray.svg  style="width:32px;"> [Point Array](Draft_PointArray.md): creates an array from a selected object by placing copies at the points from a point compound.

:\* <img alt="" src=images/Draft_PointLinkArray.svg  style="width:32px;"> _ array instead of a regular array. <small>(v0.19)</small> 

-   <img alt="" src=images/Draft_Edit.svg  style="width:32px;"> [Edit](Draft_Edit.md): puts selected objects in Draft Edit mode. In this mode the properties of objects can be edited graphically.

-   <img alt="" src=images/Draft_SubelementHighlight.svg  style="width:32px;"> [Subelement highlight](Draft_SubelementHighlight.md): temporarily highlights selected objects, or the base objects of selected objects.

-   <img alt="" src=images/Draft_Join.svg  style="width:32px;"> _ and [Draft Wires](Draft_Wire.md) into a single wire.

-   <img alt="" src=images/Draft_Split.svg  style="width:32px;"> _ or [Draft Wire](Draft_Wire.md) at a specified point or edge.

-   <img alt="" src=images/Draft_Upgrade.svg  style="width:32px;"> [Upgrade](Draft_Upgrade.md): upgrades selected objects.

-   <img alt="" src=images/Draft_Downgrade.svg  style="width:32px;"> [Downgrade](Draft_Downgrade.md): downgrades selected objects.

-   <img alt="" src=images/Draft_WireToBSpline.svg  style="width:32px;"> _ to [Draft BSplines](Draft_BSpline.md) and vice versa.

-   <img alt="" src=images/Draft_Draft2Sketch.svg  style="width:32px;"> _ objects to [Sketcher Sketches](Sketcher_NewSketch.md) and vice versa.

-   <img alt="" src=images/Draft_Slope.svg  style="width:32px;"> _ or [Draft Wires](Draft_Wire.md) by increasing, or decreasing, the Z coordinate of all points after the first one.

-   <img alt="" src=images/Draft_FlipDimension.svg  style="width:32px;"> _ 180° around the dimension line.

-   <img alt="" src=images/Draft_Shape2DView.svg  style="width:32px;"> [Shape 2D view](Draft_Shape2DView.md): creates 2D projections from selected objects.

## Barra degli strumenti del vassoio di Draft 

La barra degli strumenti del vassoio di Draft viene visualizzata all\'avvio dell\'ambiiente e consente di selezionare il piano di lavoro, insieme ad alcune proprietà visive come il colore della linea, il colore della forma, la dimensione del testo, la larghezza della linea e il gruppo automatico.

![](images/Draft_tray_default.png )


<div class="mw-translate-fuzzy">

-   <img alt="" src=images/Draft_SelectPlane.svg  style="width:32px;"> [Piano di lavoro](Draft_SelectPlane/it.md): consente di impostare un piano di lavoro da una vista standard o da una faccia selezionata..
-   <img alt="" src=images/Draft_ToggleConstructionMode.svg  style="width:32px;"> [Modalità costruzione](Draft_ToggleConstructionMode/it.md): attiva o disattiva la modalità costruzione.
-   <img alt="" src=images/Draft_ApplyStyle.svg  style="width:32px;"> [Imposta Stile](Draft_Apply/it.md): imposta lo stile di default per i nuovi oggetti e applica lo stile e il colore correnti agli oggetti selezionati.
-   <img alt="" src=images/Draft_AutoGroup.svg  style="width:32px;"> _, <img alt="" src=images/Draft_Layer.svg  style="width:32px;"> _. {{Version/it|0.17}}


</div>

-   ![](images/Draft_tray_button_style.png ) [Set style](Draft_SetStyle.md): sets the default style for new objects. Also available in the menu: **Draft → Utilities → <img src="images/Draft_SetStyle.svg" width=16px> Set style**. <small>(v0.19)</small> 

-   ![](images/Draft_tray_button_construction.png ) [Toggle construction mode](Draft_ToggleConstructionMode.md): switches Draft construction mode on or off. Also available in the menu: **Draft → Utilities → <img src="images/Draft_ToggleConstructionMode.svg" width=16px> Toggle construction mode**.

-   !_ or, optionally, the active [Std Group](Std_Group.md) or group-like [Arch](Arch_Workbench.md) object.

## Draft annotation scale widget 

With the [Draft annotation scale widget](Draft_annotation_scale_widget.md) the Draft annotation scale can be specified. <small>(v0.19)</small> 

![](images/Draft_annotation_scale_widget_button.png )

## Draft snap widget 

The [Draft snap widget](Draft_snap_widget.md) can be used as an alternative for the [Draft Snap toolbar](#Draft_Snap_toolbar.md). <small>(v0.19)</small> 

![](images/Draft_snap_widget_button.png )

## Barra degli strumenti di aggancio 

La barra degli strumenti di [Aggancio](Draft_Snap/it.md) consente di selezionare la modalità di aggancio corrente. Il suo pulsante rimane premuto quando una modalità è attiva.

-   <img alt="" src=images/Draft_Snap_Lock.svg  style="width:32px;"> [Snap Lock](Draft_Snap_Lock.md): enables or disables snapping globally.

-   <img alt="" src=images/Draft_Snap_Endpoint.svg  style="width:32px;"> [Snap Endpoint](Draft_Snap_Endpoint.md): snaps to the endpoints of edges.

-   <img alt="" src=images/Draft_Snap_Midpoint.svg  style="width:32px;"> [Snap Midpoint](Draft_Snap_Midpoint.md): snaps to the midpoint of straight and circular edges.

-   <img alt="" src=images/Draft_Snap_Center.svg  style="width:32px;"> _ and [Arch BuildingParts](Arch_BuildingPart.md).

-   <img alt="" src=images/Draft_Snap_Angle.svg  style="width:32px;"> [Snap Angle](Draft_Snap_Angle.md): snaps to the special cardinal points on circular edges, at multiples of 30° and 45°.

-   <img alt="" src=images/Draft_Snap_Intersection.svg  style="width:32px;"> [Snap Intersection](Draft_Snap_Intersection.md): snaps to the intersection of two edges.

-   <img alt="" src=images/Draft_Snap_Perpendicular.svg  style="width:32px;"> [Snap Perpendicular](Draft_Snap_Perpendicular.md): snaps to the perpendicular point on edges.

-   <img alt="" src=images/Draft_Snap_Extension.svg  style="width:32px;"> [Snap Extension](Draft_Snap_Extension.md): snaps to an imaginary line that extends beyond the endpoints of straight edges.

-   <img alt="" src=images/Draft_Snap_Parallel.svg  style="width:32px;"> [Snap Parallel](Draft_Snap_Parallel.md): snaps to an imaginary line parallel to straight edges.

-   <img alt="" src=images/Draft_Snap_Special.svg  style="width:32px;"> [Snap Special](Draft_Snap_Special.md): snaps to special points defined by the object.

-   <img alt="" src=images/Draft_Snap_Near.svg  style="width:32px;"> [Snap Near](Draft_Snap_Near.md): snaps to the nearest point on faces or edges.

-   <img alt="" src=images/Draft_Snap_Ortho.svg  style="width:32px;"> [Snap Ortho](Draft_Snap_Ortho.md): snaps to imaginary lines that cross the previous point at 0°, 45°, 90° and 135°.

-   <img alt="" src=images/Draft_Snap_Grid.svg  style="width:32px;"> [Snap Grid](Draft_Snap_Grid.md): snaps to the intersections of grid lines.

-   <img alt="" src=images/Draft_Snap_WorkingPlane.svg  style="width:32px;"> _.

-   <img alt="" src=images/Draft_Snap_Dimensions.svg  style="width:32px;"> [Snap Dimensions](Draft_Snap_Dimensions.md): shows temporary X and Y dimensions.

-   <img alt="" src=images/Draft_ToggleGrid.svg  style="width:32px;"> [Toggle Grid](Draft_ToggleGrid.md): switches the grid on or off.

## Strumenti di utilità 

-   <img alt="" src=images/Draft_Layer.svg  style="width:32px;"> _. <small>(v0.19)</small> 

-   <img alt="" src=images/Draft_AddNamedGroup.svg  style="width:32px;"> _ and moves selected objects to that group. <small>(v0.20)</small> 

-   <img alt="" src=images/Draft_AddToGroup.svg  style="width:32px;"> _. It can also ungroup objects.

-   <img alt="" src=images/Draft_SelectGroup.svg  style="width:32px;"> _, [Std Groups](Std_Group.md) or group-like [Arch](Arch_Workbench.md) objects.

-   <img alt="" src=images/Draft_AddConstruction.svg  style="width:32px;"> _.

-   <img alt="" src=images/Draft_ToggleDisplayMode.svg  style="width:32px;"> [Toggle normal/wireframe display](Draft_ToggleDisplayMode.md): switches the **Display Mode** property of selected objects between {{Value|Flat Lines}} and {{Value|Wireframe}}.

-   <img alt="" src=images/Draft_WorkingPlaneProxy.svg  style="width:32px;"> _.

## Menu di utilità 

Strumenti aggiuntivi disponibili dal menu **Draft → Utilità** o tramite il menu di scelta rapida visualizzato facendo clic con il pulsante destro del mouse, a seconda dell\'oggetto selezionato.

-   <img alt="" src=images/Draft_ApplyStyle.svg  style="width:32px;"> [Apply current style](Draft_ApplyStyle.md): applies the current style settings to selected objects.

-   <img alt="" src=images/Draft_Heal.svg  style="width:32px;"> [Heal](Draft_Heal.md): heals problematic Draft objects found in very old files.

-   <img alt="" src=images/Draft_ToggleContinueMode.svg  style="width:32px;"> [Toggle continue mode](Draft_ToggleContinueMode.md): switches continue mode on or off.

-   <img alt="" src=images/Draft_ShowSnapBar.svg  style="width:32px;"> _.

## Ulteriori funzioni 


<div class="mw-translate-fuzzy">

-   [Digitare le coordinate](Draft_Coordinates/it.md): permette di inserire le coordinate invece di fare clic sulla vista 3D per definire un nuovo punto.
-   [Vincolare](Draft_Constrain/it.md): limita il puntatore nei movimenti orizzontali o verticali rispetto a un punto precedente.
-   [Ancorare (Snap)](Draft_Snap/it.md): posiziona nuovi punti su posti speciali su oggetti esistenti o sulla griglia.
-   [Modalità copia](Draft_Copying/it.md): Tutti gli strumenti di modifica possono modificare gli oggetti selezionati o crearne una copia modificata. Tenendo premuto **Alt** durante la modifica dell\'oggetto, ad es. spostato o ruotato, crea una copia quando si rilascia il tasto.
-   [Modalità costruzione](Draft_ToggleConstructionMode/it.md): Permette di creare geometrie separate dalle altre semplicemente attivandola o disattivandola.
-   [Piano di lavoro](Draft_SelectPlane/it.md): consente di selezionare una superficie nello spazio 3D su cui lavorare.


</div>

## Tree view context menu 

The following additional options are available in the [Tree view](Tree_view.md) context menu:

### Default options 

If there is an active document the context menu contains one additional sub-menu:

-    **Utilities**: a subset of the tools available in the main Draft Utilities menu.

### Wire options 

For a [Draft Wire](Draft_Wire.md), [Draft BSpline](Draft_BSpline.md), [Draft CubicBezCurve](Draft_CubicBezCurve.md) and [Draft BezCurve](Draft_BezCurve.md) this additional option is available:

-   <img alt="" src=images/Draft_Edit.svg  style="width:32px;"> Flatten this wire: flattens the wire based on its internal geometry. This option currently does not work properly.

### Layer container options 

For a [Draft LayerContainer](Draft_Layer.md) these additional options are available:

-   <img alt="" src=images/Draft_Layer.svg  style="width:32px;"> Merge layer duplicates: this option currently does not work.

-   <img alt="" src=images/Draft_NewLayer.svg  style="width:32px;"> [Add new layer](Draft_Layer.md): adds a new layer to the current document.

### Layer options 

For a [Draft Layer](Draft_Layer.md) these additional options are available:

-   <img alt="" src=images/button_right.svg  style="width:32px;"> [Activate this layer](Draft_AutoGroup.md): activates the selected layer.

-   <img alt="" src=images/Draft_SelectGroup.svg  style="width:32px;"> [Select layer contents](Draft_SelectGroup.md): selects the objects inside the selected layer.

### Working plane proxy options 

For a [Draft WorkingPlaneProxy](Draft_WorkingPlaneProxy.md) these additional options are available:

-   <img alt="" src=images/Draft_SelectPlane.svg  style="width:32px;"> _ camera settings.

-   <img alt="" src=images/Draft_SelectPlane.svg  style="width:32px;"> [Write objects state](Draft_WorkingPlaneProxy#Context_menu.md): updates the **Visibility Map** property of the working plane proxy with the current visibility state of objects in the document.

## 3D view context menu 

The following additional options are available in the [3D view](3D_view.md) context menu:

### Default options 

If there is an active document the context menu contains one additional sub-menu:

-    **Utilities**: a subset of the tools available in the main Draft Utilities menu.

### Obsoleti

Questi strumenti sono stati rimossi dall\'interfaccia in v0.19 perché non avevano più alcuno scopo.


<div class="mw-translate-fuzzy">

-   <img alt="" src=images/Draft_VisGroup.svg  style="width:32px;"> [VisGruppo](Draft_VisGroup/it.md): crea nel documento corrente un gruppo di elementi con le stesse proprietà Vista. {{Obsolete/it|0.19}}
-   <img alt="" src=images/Draft_FinishLine.svg  style="width:32px;"> _ o [BSpline](Draft_BSpline/it.md), senza chiuderla. {{Obsolete/it|0.19}}
-   <img alt="" src=images/Draft_CloseLine.svg  style="width:32px;"> _ o [BSpline](Draft_BSpline/it.md), e la chiude. {{Obsolete/it|0.19}}
-   <img alt="" src=images/Draft_UndoLine.svg  style="width:32px;"> _. {{Obsolete/it|0.19}}


</div>

-   <img alt="" src=images/Draft_Drawing.svg  style="width:32px;"> _ page. {{Obsolete|0.17}}

## Preferenze


<div class="mw-translate-fuzzy">

-   <img alt="" src=images/Preferences-draft.svg  style="width:32px;"> [Preferenze](Draft_Preferences/it.md): preferenze generali per il piano di lavoro e gli strumenti di disegno.
-   <img alt="" src=images/Preferences-import-export.svg  style="width:32px;"> [Preferenze Import-Export](Import_Export_Preferences/it.md): preferenze disponibili per l\'importazione e l\'esportazione in diversi formati di file.


</div>

-   <img alt="" src=images/Preferences-import-export.svg  style="width:32px;"> [Import Export Preferences](Import_Export_Preferences.md): preferences available for importing from and exporting to different file formats.

## Formato dei file 


<div class="mw-translate-fuzzy">

Queste sono le funzioni per l\'apertura, l\'importazione o l\'esportazione di altri formati di file. Il comando Apri apre un nuovo documento con i contenuti del file, mentre Importa aggiunge i contenuti del file al documento corrente. Esporta salva gli oggetti selezionati in un file. Se non viene selezionato nulla, vengono esportati tutti gli oggetti. Ricordare che lo scopo di Draft è di lavorare con oggetti 2D, quindi le procedure di importazione si concentrano solo su oggetti 2D e sebbene i formati DXF e OCA supportino anche le definizioni di oggetti nello spazio 3D (gli oggetti non sono necessariamente piatti), non importa oggetti volumetrici come mesh, superfici 3D, ecc., ma solo linee, cerchi, testi o forme piatte. I formati di file attualmente supportati sono:


</div>


<div class="mw-translate-fuzzy">

-   _.
-   _. Vedere anche la pagina [Importare i file DWG in FreeCAD](FreeCAD_and_DWG_Import/it.md).
-   [SVG](Draft_SVG/it.md): importa ed esporta i file [Scalable Vector Graphics](http://en.wikipedia.org/wiki/Scalable_Vector_Graphics) creato con applicazioni di disegno vettoriale.
-   [Open Cad format .OCA](Draft_OCA/it.md): importa ed esporta file OCA/GCAD, potenzialmente un nuovo [formato di file open CAD](http://groups.google.com/group/open_cad_format).
-   [Airfoil Data Format .DAT](Draft_DAT/it.md): importa file DAT che descrivono [profili aerodinamici](http://www.ae.illinois.edu/m-selig/ads/coord_database.html) portanti.


</div>

## Test unitari 


<div class="mw-translate-fuzzy">


**Vedere anche:**

[Ambiente Test](Test_Workbench/it.md).


</div>


<div class="mw-translate-fuzzy">

Per eseguire i test unitari dell\'ambiente, eseguire quanto segue dal terminale del sistema operativo.


</div>


```python
freecad -t TestDraft
```

## Script


<div class="mw-translate-fuzzy">

Gli strumenti di Draft possono essere utilizzati nelle [macro](macros/it.md) e dalla console [Python](Python/it.md) utilizzando le [API Draft](Draft_API/it.md).


</div>

L\'ambiente include un modulo per creare dei campioni di tutti gli oggetti in un nuovo documento. {{Version/it|0.19}}


<div class="mw-translate-fuzzy">

Utilizzare questo per verificare che tutti gli oggetti siano prodotti correttamente.


</div>


```python
import drafttests.draft_test_objects as dto
doc = dto.create_test_file()
```


<div class="mw-translate-fuzzy">

Ispezionare il codice di questo modulo è utile per capire come utilizzare l\'interfaccia di programmazione.


</div>

## Tutorials


<div class="mw-translate-fuzzy">

## Tutorial

-   [Draft tutorial](Draft_tutorial/it.md)
-   [Draft tutorial obsoleto](Draft_tutorial_Outdated/it.md)
-   [Draft ShapeString tutorial](Draft_ShapeString_tutorial/it.md)


</div>





 

_

---
[documentation index](../README.md) > [Workbenches](Category_Workbenches.md) > Draft Workbench/it
