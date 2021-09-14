# Sketcher SketchObject/it



## Introduzione

<img alt="" src=images/Sketcher_Sketch.svg  style="width:32px;">

Un [Sketcher SketchObject](Sketcher_SketchObject/it.md), o formalmente un `Sketcher::SketchObject`, è l\'elemento base per creare oggetti 2D con l\'ambiente [Sketcher](Sketcher_Workbench/it.md).


{{Incode|Sketcher::SketchObject}}

deriva da [Part Part2DObject](Part_Part2DObject/it.md), il che significa che è un oggetto [Part Feature](Part_Feature/it.md) specializzato per la geometria 2D. Come Part2DObject, anche SketchObject può essere collegato a piani e facce. Inoltre, SketchObject è in grado di gestire i vincoli geometrici delle linee e delle curve disegnate al suo interno.

<img alt="" src=images/FreeCAD_core_objects.svg  style="width:800px;">


<div class="mw-translate-fuzzy">


*Diagramma semplificato delle relazioni tra gli oggetti principali in FreeCAD. La classe `Sketcher::SketchObject* è specializzata per le forme 2D e inoltre può gestire i vincoli.`


</div>

## Utilizzo

1.  Passare all\'ambiente [Sketcher](Sketcher_Workbench/it.md).
2.  Premere **<img src=images/Sketcher_NewSketch.svg style="width:16px"> [Nuovo schizzo](Sketcher_NewSketch/it.md)**.
3.  Selezionare un **orientamento**: piano XY, piano XZ o piano YZ. Opzionalmente scegliere anche **Direzione inversa**, e assegnare un valore di **Offset**.
4.  Premere **OK**.

Sebbene SketchObject possa essere utilizzato da solo per disegnare su un piano, viene comunemente utilizzato insieme a [PartDesign](PartDesign_Workbench/it.md) per creare solidi estrusi.

1.  Passare in [PartDesign](PartDesign_Workbench/it.md).

2.  Premere **<img src=images/PartDesign_Body.svg style="width:16px"> [Crea un corpo](PartDesign_Body/it.md)**.

3.  Premere **<img src=images/PartDesign_NewSketch.svg style="width:16px"> [Crea uno schizzo](PartDesign_NewSketch/it.md)**.

4.  
    **Selezione della funzione**: piano XY (piano base), piano XZ (piano base) o piano YZ (piano base).

5.  Premere **OK**.

## Proprietà

Vedere [Proprietà](Property/it.md) per tutti i tipi di proprietà che possono avere gli oggetti con script.

Un [Sketcher SketchObject](Sketcher_SketchObject.md) (classe `Sketcher::SketchObject`) deriva da un [Part Part2DObject](Part_Part2DObject.md) (`Part::Part2DObject`), quindi condivide tutte le proprietà di quest\'ultimo.


<div class="mw-translate-fuzzy">

Oltre alle proprietà descritte in [Part Part2DObject](Part_Part2DObject/it.md), il corpo di PartDesign ha le seguenti proprietà nell\'[editor delle proprietà](property_editor/it.md).


</div>

### Dati


<div class="mw-translate-fuzzy">


{{TitleProperty|Attachment}}

-    **Map Mode**: vedere [Part Attachment](Part_Attachment/it.md) per ulteriori informazioni su tutte le modalità di associazione.


</div>


<div class="mw-translate-fuzzy">


{{TitleProperty|Sketch}}

-    **Constraints**: vincoli atribuiti, se esistono; altrimenti è un elenco `[]` vuoto.


</div>

#### Hidden properties Data 

See [Part Part2DObject](Part_Part2DObject.md) for the rest of the hidden properties.


{{TitleProperty|Base}}

-    **Proxy|PythonObject**: a custom class associated with this object. This only exists for the [Python](Python.md) version. See [Scripting](Sketcher_SketchObject#Scripting.md).


{{TitleProperty|Sketch}}

-    **Geometry|GeometryList**: a list of Part geometries that exist inside the sketch.

-    **External Geometry|LinkSubList**: a list of Part geometries outside this Sketch that are used for reference.

### Vista


<div class="mw-translate-fuzzy">


{{TitleProperty|Auto Constraints}}

-    **Autoconstraints**: se è `True` prova ad impostare i vincoli quando viene disegnata la geometria.


</div>


<div class="mw-translate-fuzzy">


{{TitleProperty|Visibility automation}}

-    **Editing Workbench**: normalmente `SketcherWorkbench`, è il nome dell\'ambiente da attivare durante la modifica dello schizzo.

-    **Hide Dependent**: se è `True` tutti gli oggetti che dipendono dallo schizzo vengono nascosti quando si apre lo schizzo.

-    **Restore Camera**: se è `True` la posizione della telecamera viene salvata prima di aprire lo schizzo e viene ripristinata quando lo si chiude.

-    **Show Links**: se è `True` tutti gli oggetti utilizzati nei collegamenti alla geometria esterna vengono visualizzati quando si apre lo schizzo.

-    **Show Support**: se è `True` tutti gli oggetti a cui è associato questo schizzo vengono mostrati quando si apre lo schizzo.


</div>

#### Hidden properties View 


{{TitleProperty|Base}}

-    **Proxy|PythonObject**: a custom view provider class associated with this object. This only exists for the [Python](Python.md) version. See [Scripting](Sketcher_SketchObject#Scripting.md).


{{TitleProperty|Visibility automation}}

-    **Tempo Vis|PythonObject**: a custom class associated with this object, that handles hiding and showing other objects when opening and closing the sketch.

All other view properties, including hidden properties, are those of the base [Part Feature](Part_Feature.md) object.

## Script


**Vedere anche:**

[Script di base per FreeCAD](FreeCAD_Scripting_Basics/it.md), e [script di oggetti](scripted_objects/it.md).


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

This basic `Sketcher::SketchObject` doesn\'t have a Proxy object so it can\'t be fully used for sub-classing.

Therefore, for [Python](Python.md) subclassing, you should create the `Sketcher::SketchObjectPython` object.


```python
import FreeCAD as App

doc = App.newDocument()
obj = App.ActiveDocument.addObject("Sketcher::SketchObjectPython", "CustomSketch")
obj.Label = "Custom label"
```


{{Sketcher Tools navi

}}  {{Document objects navi}} 
