 {{TOCright}}

## Introduzione

Una [Part TopoShape](Part_TopoShape.md), o formalmente una `Part::TopoShape`, è una classe che definisce una \"forma topologica\" parametrica nel software. Gli oggetti del documento che mostrano qualcosa nella [vista 3D](3D_view/it.md) normalmente hanno una TopoShape.


<div class="mw-translate-fuzzy">

Le forme topologiche, così come i loro metodi, sono definiti dal kernel OpenCASCADE Technology (OCCT). FreeCAD usa queste forme e crea dei [App DocumentObjects](App_DocumentObject/it.md) attorno ad esse.


</div>

Another type of class is that of [meshes](Mesh.md); this class is not very parametric because it can\'t be redefined easily except by specifying individual vertices and triangular surfaces.

![](images/Shape_and_mesh.svg )


*Left: parametric [Part TopoShape](Part_TopoShape.md) defined by properties. Right: non-parametric [mesh](Mesh.md), defined by vertices and triangular surfaces.*

<img alt="" src=images/FreeCAD_core_objects.svg  style="width:800px;">


*Diagramma semplificato delle relazioni tra gli oggetti principali del programma. La classe `Part::TopoShape* è incorporata nell'oggetto {{incode|Part::Feature` e da lì viene propagata a tutti gli oggetti che ne derivano.}}

## Utilizzo

TopoShape è un oggetto assegnato ad alcuni [App DocumentObjects](App_DocumentObject/it.md).

In particolare, l\'oggetto base che gestisce questi tipi di forme è la [Part Feature](Part_Feature/it.md) (classe `Part::Feature`). Tutti gli oggetti derivati da questa classe avranno accesso a una Part TopoShape.

Alcuni degli oggetti più importanti con Part TopoShape sono i seguenti:

-   Qualsiasi solido primitivo creato con [Part](Part_Workbench/it.md).
-   Qualsiasi [Corpo di PartDesign](PartDesign_Body/it.md) e [PartDesign Feature](PartDesign_Feature/it.md) creati con [PartDesign](PartDesign_Workbench/it.md).
-   Qualsiasi oggetto derivato da [Part Part2DObject](Part_Part2DObject/it.md), come la maggior parte degli oggetti creati con [Draft](Draft_Workbench/it.md).
-   Qualsiasi [schizzo](Sketch/it.md), cioè, [Sketcher SketchObject](Sketcher_SketchObject/it.md), creato con [Sketcher](Sketcher_Workbench/it.md).
-   Qualsiasi oggetto creato importando uno STEP, BREP e file simili in formato solido.

## Script


**Vedere anche:**

[Script di base per FreeCAD](FreeCAD_Scripting_Basics/it.md), e [script di oggetti](scripted_objects/it.md).

Tutti gli oggetti derivati da `Part::Feature` avranno un [Part TopoShape](Part_TopoShape/it.md), che è normalmente accessibile dal suo attributo `Shape`. 
```python
import FreeCAD as App

doc = App.newDocument()
obj = App.ActiveDocument.addObject("Part::Box", "Box")
print(obj.Shape)
```

Un TopoShape ha molti attributi (variabili) e metodi che contengono informazioni su di esso e che consentono di eseguire operazioni con esso. Queste variabili e metodi possono essere testati nella [console Python](Python_console/it.md). 
```python
print(obj.Shape.Area)
print(obj.Shape.BoundBox)
print(obj.Shape.CenterOfMass)
print(obj.Shape.ShapeType)

obj.Shape.check()
obj.Shape.copy()
obj.Shape.exportStep("my_file.step")
obj.Shape.exportStl("my_file.stl")
```


<div class="mw-translate-fuzzy">

Per un elenco completo di attributi e metodi, consultare [documentazione del codice sorgente](Source_documentation/it.md) e lo strumento di [documentazione dei moduli Python](Std_PythonHelp/it.md).


</div>

You can obtain a quick summary of all methods using Python\'s built-in `help()` function. 
```python
help(obj.Shape)
```


 {{Document objects navi}} 
