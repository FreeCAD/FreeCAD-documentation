# Part Part2DObject/it
{{TOCright}}

## Introduzione

<img alt="" src=images/Tree_Part2D.svg  style="width   *32px;">


<div class="mw-translate-fuzzy">

Un [Part Part2DObject](Part_Part2DObject/it.md), o formalmente un `Part   *   *Part2DObject`, è un elemento semplice a cui è associata una [forma topologica](Part_TopoShape/it.md) che può essere visualizzato nella [Vista 3D](3D_view/it.md).


</div>


<div class="mw-translate-fuzzy">


{{Incode|Part   *   *Part2DObject}}

è derivato da una [Part Feature](Part_Feature/it.md), ma è specializzato nella geometria 2D, dato che la sua forma è posizionata su un piano. Il piano è definito dalla sua proprietà **Placement** (posizione, normale e rotazione). Tuttavia, il piano può anche essere definito supportando elementi geometrici, come il piano creato da tre vertici arbitrari o una faccia di un corpo solido.


</div>

<img alt="" src=images/FreeCAD_core_objects.svg  style="width   *800px;">


<div class="mw-translate-fuzzy">



*Diagramma semplificato delle relazioni tra gli oggetti principali in FreeCAD. La classe `Part   *   *Part2DObject* è specializzata per le forme 2D, quindi è la classe di base per gli oggetti planari creati con gli ambienti Draft e Sketcher. Include un'estensione che consente di collegarla a facce e piani`


</div>

## Utilizzo


<div class="mw-translate-fuzzy">

[Part Part2DObject](Part_Part2DObject.md) è un oggetto interno, quindi non può essere creato dall\'interfaccia grafica, ma solo dalla [console Python](Python_console/it.md) come descritto nel paragrafo [Script](Part_Part2DObject/it#Script.md).


</div>


<div class="mw-translate-fuzzy">


{{Incode|Part   *   *Part2DObject}}

è definito nell\'ambiente [Part](Part_Workbench/it.md) ma può essere usato come classe base per gli [oggetti da script](scripted_objects/it.md) in tutti gli \[\[Workbenches/it\|ambienti\] \] che producono forme geometriche 2D. Ad esempio, è l\'oggetto base per gli ([Sketcher SketchObject](Sketcher_SketchObject/it.md)) degli schizzi e per la maggior parte degli oggetti creati con [Draft](Draft_Workbench/it.md).


</div>

I workbench possono aggiungere diverse proprietà a questo elemento di base per produrre un oggetto con comportamento complesso.

## Proprietà

Vedere [Proprietà](Property/it.md) per tutti i tipi di proprietà che possono avere gli oggetti con script.


<div class="mw-translate-fuzzy">

Un [Part Part2DObject](Part_Part2DObject/it.md) (classe `Part   *   *Part2DObject`) è derivato da una [Part Feature](Part_Feature/it.md) (classe `Part   *   *Feature`), pertanto condivide tutte le proprietà di quest\'ultimo.


</div>


<div class="mw-translate-fuzzy">

Oltre alle proprietà descritte in [Part Feature](Part_Feature/it.md), Part Part2DObject ha le seguenti proprietà nell\'[editor delle proprietà](property_editor/it.md). Le proprietà nascoste possono essere mostrate usando il comando **Mostra tutto** nel menu contestuale dell\'[editor delle proprietà](property_editor/it.md).


</div>

### Dati


{{TitleProperty|Attachment}}


<div class="mw-translate-fuzzy">


{{TitleProperty|Attachment}}

-    **Map Mode|Enumeration**   * {{value|Deactivated}} di default. Questa proprietà definisce il piano che l\'oggetto utilizza come riferimento per la geometria 2D. Facendo clic sui puntini di sospensione **...** (tre puntini), a destra del campo di immissione si apre il pannello [Part EditAttachment](Part_EditAttachment/it.md) della [scheda azioni](task_panel/it.md) che consente di selezionare il piano di supporto selezionando diversi elementi nella [vista 3D](3D_view/it.md). Le diverse modalità sono   * {{value|Deactivated}}, {{value|Translate origin}}, {{value|Object's XY}}, {{value|Object's XZ}}, {{value|Object's YZ}}, {{value|Plane face}}, {{value|Tangent to surface}}, {{value|Normal to edge}}, {{value|Frenet NB}}, {{value|Frenet TN}}, {{value|Frenet TB}}, {{value|Concentric}}, {{value|Revolution section}}, {{value|Plane by 3 points}}, {{value|Normal to 3 points}}, {{value|Folding}}, {{value|Inertia 2-3}}, {{value|Align O-N-X}}, {{value|Align O-N-Y}}, {{value|Align O-X-Y}}, {{value|Align O-X-N}}, {{value|Align O-Y-N}}, {{value|Align O-Y-X}}.


</div>

## Script


<div class="mw-translate-fuzzy">


**Vedere anche   ***

[Script di base per FreeCAD](FreeCAD_Scripting_Basics/it.md), e [script di oggetti](scripted_objects/it.md).


</div>

Vedere [Part Feature](Part_Feature/it.md) per le informazioni generali sull\'aggiunta di oggetti al documento..

Un Part2DObject viene creato con il metodo `addObject()` del documento.


```python
import FreeCAD as App

doc = App.newDocument()
obj = App.ActiveDocument.addObject("Part   *   *Part2DObject", "Name")
obj.Label = "Custom label"
```


<div class="mw-translate-fuzzy">

Pertanto, per la sottoclasse [Python](Python/it.md), è necessario creare l\'oggetto `Part   *   *Part2DObjectPython`.


</div>


```python
import FreeCAD as App

doc = App.newDocument()
obj = App.ActiveDocument.addObject("Part   *   *Part2DObjectPython", "Name")
obj.Label = "Custom label"
```


{{Document_objects_navi

}}



---
![](images/Right_arrow.png) [documentation index](../README.md) > [Part](Part_Workbench.md) > Part Part2DObject/it
