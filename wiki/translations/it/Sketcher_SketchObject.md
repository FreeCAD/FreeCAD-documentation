# Sketcher SketchObject/it
{{TOCright}}

## Introduzione

<img alt="" src=images/Sketcher_Sketch.svg  style="width:32px;">

Un [Sketcher SketchObject](Sketcher_SketchObject/it.md), o formalmente un `Sketcher::SketchObject`, è l\'elemento base per creare oggetti 2D con l\'ambiente [Sketcher](Sketcher_Workbench/it.md).


<div class="mw-translate-fuzzy">


{{Incode|Sketcher::SketchObject}}

deriva da [Part Part2DObject](Part_Part2DObject/it.md), il che significa che è un oggetto [Part Feature](Part_Feature/it.md) specializzato per la geometria 2D. Come Part2DObject, anche SketchObject può essere collegato a piani e facce. Inoltre, SketchObject è in grado di gestire i vincoli geometrici delle linee e delle curve disegnate al suo interno.


</div>

<img alt="" src=images/FreeCAD_core_objects.svg  style="width:800px;">


<div class="mw-translate-fuzzy">



*Diagramma semplificato delle relazioni tra gli oggetti principali in FreeCAD. La classe `Sketcher::SketchObject* è specializzata per le forme 2D e inoltre può gestire i vincoli.`


</div>

## Utilizzo

1.  Passare all\'ambiente [Sketcher](Sketcher_Workbench/it.md).
2.  Premere **[<img src=images/Sketcher_NewSketch.svg style="width:16px"> [Nuovo schizzo](Sketcher_NewSketch/it.md)**.
3.  Selezionare un **orientamento**: piano XY, piano XZ o piano YZ. Opzionalmente scegliere anche **Direzione inversa**, e assegnare un valore di **Offset**.
4.  Premere **OK**.


<div class="mw-translate-fuzzy">

Sebbene SketchObject possa essere utilizzato da solo per disegnare su un piano, viene comunemente utilizzato insieme a [PartDesign](PartDesign_Workbench/it.md) per creare solidi estrusi.


</div>


<div class="mw-translate-fuzzy">

1.  Passare in [PartDesign](PartDesign_Workbench/it.md).

2.  Premere **[<img src=images/PartDesign_Body.svg style="width:16px"> [Crea un corpo](PartDesign_Body/it.md)**.

3.  Premere **[<img src=images/PartDesign_NewSketch.svg style="width:16px"> [Crea uno schizzo](PartDesign_NewSketch/it.md)**.

4.  
    **Selezione della funzione**: piano XY (piano base), piano XZ (piano base) o piano YZ (piano base).

5.  Premere **OK**.


</div>

## Proprietà

Vedere [Proprietà](Property/it.md) per tutti i tipi di proprietà che possono avere gli oggetti con script.


<div class="mw-translate-fuzzy">

Un [Sketcher SketchObject](Sketcher_SketchObject.md) (classe `Sketcher::SketchObject`) deriva da un [Part Part2DObject](Part_Part2DObject.md) (`Part::Part2DObject`), quindi condivide tutte le proprietà di quest\'ultimo.


</div>


<div class="mw-translate-fuzzy">

Oltre alle proprietà descritte in [Part Part2DObject](Part_Part2DObject/it.md), il corpo di PartDesign ha le seguenti proprietà nell\'[editor delle proprietà](property_editor/it.md).


</div>

### Dati


{{TitleProperty|Sketch}}

-    **Geometry|GeometryList|Hidden**: a list of Part geometries that exist inside the sketch.

-    **Constraints|**: named constraints, if they exist; otherwise it is an empty list `[]`.

-    **External Geometry|LinkSubList**: a list of Part geometries outside this Sketch that are used for reference.

-    **Fully Constrained|Bool|Hidden**: (read-only) if `True` the sketch is fully constrained.

### Vista


<div class="mw-translate-fuzzy">


{{TitleProperty|Auto Constraints}}

-    **Autoconstraints**: se è `True` prova ad impostare i vincoli quando viene disegnata la geometria.


</div>

-    **Autoconstraints|Bool**: if `True` constraints are automatically added when geometry is drawn.

-    **Avoid Redundant|Bool**: if `True` redundant auto-constraints are avoided.


{{TitleProperty|Grid}}

-    **Grid Auto Size|Bool|Hidden**: if `True` the grid is resized based on the boundingbox of the geometry of the sketch.

-    **Grid Size|Length**: the size of the spacing of the local grid lines in the [3D view](3D_view.md); it defaults to {{value|10 mm}}.

-    **Grid Snap|Bool**: if `True` the grid can be used to snap points.

-    **Grid Style|Enumeration**: the style of the grid lines; {{value|Dashed}} (default) or {{value|Light}}.

-    **Show Grid|Bool**: if `True` a grid local to the object will be displayed in the [3D view](3D_view.md). This grid is independent of the [Draft Grid](Draft_ToggleGrid.md).

-    **Show Only In Edit Mode|Bool**: if `True` the grid is only displayed while the sketch is being edited.

-    **Tight Grid|Bool**: if `True` the local grid will be localized around the origin of the shape, otherwise it will extend itself more.

-    **max Number Of Lines|Integer**: the maximum number of lines in the grid.


{{TitleProperty|Visibility automation}}


<div class="mw-translate-fuzzy">


{{TitleProperty|Visibility automation}}

-    **Editing Workbench**: normalmente `SketcherWorkbench`, è il nome dell\'ambiente da attivare durante la modifica dello schizzo.

-    **Hide Dependent**: se è `True` tutti gli oggetti che dipendono dallo schizzo vengono nascosti quando si apre lo schizzo.

-    **Restore Camera**: se è `True` la posizione della telecamera viene salvata prima di aprire lo schizzo e viene ripristinata quando lo si chiude.

-    **Show Links**: se è `True` tutti gli oggetti utilizzati nei collegamenti alla geometria esterna vengono visualizzati quando si apre lo schizzo.

-    **Show Support**: se è `True` tutti gli oggetti a cui è associato questo schizzo vengono mostrati quando si apre lo schizzo.


</div>

## Script


<div class="mw-translate-fuzzy">


**Vedere anche:**

[Script di base per FreeCAD](FreeCAD_Scripting_Basics/it.md), e [script di oggetti](scripted_objects/it.md).


</div>


<div class="mw-translate-fuzzy">

Vedere [Part Feature](Part_Feature/it.md) per le informazioni generali.


</div>


<div class="mw-translate-fuzzy">

Un oggetto Sketcher SketchObject viene creato con il metodo `addObject()` del documento.


</div>


```python
import FreeCAD as App

doc = App.newDocument()
obj = App.ActiveDocument.addObject("Sketcher::SketchObject", "Sketch")
obj.Label = "Custom label"
```

For [Python](Python.md) subclassing you should create the `Sketcher::SketchObjectPython` object.


```python
import FreeCAD as App

doc = App.newDocument()
obj = App.ActiveDocument.addObject("Sketcher::SketchObjectPython", "CustomSketch")
obj.Label = "Custom label"
```


{{Sketcher_Tools_navi

}} {{Document_objects_navi}}



---
![](images/Button_right.svg) [documentation index](../README.md) > [Sketcher](Sketcher_Workbench.md) > Sketcher SketchObject/it
