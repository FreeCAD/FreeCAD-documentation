# Part Part2DObject/it
## Introduzione

<img alt="" src=images/Tree_Part2D.svg  style="width:32px;">

Un [Part Part2DObject](Part_Part2DObject/it.md), o formalmente un `Part::Part2DObject`, è un elemento semplice con una [forma topologica](Part_TopoShape/it.md) che può essere visualizzato nella [Vista 3D](3D_view/it.md).


{{Incode|Part::Part2DObject}}

è derivato dalla [Part Feature](Part_Feature/it.md), ma è specializzato nella geometria 2D, dato che la sua forma è posizionata su un piano. Il piano è definito dalla sua proprietà **Placement** (posizione, normale e rotazione). Tuttavia, il piano può anche essere definito supportando elementi geometrici, come il piano creato da tre vertici arbitrari o una faccia di un corpo solido.

<img alt="" src=images/FreeCAD_core_objects.svg  style="width:800px;">



*Diagramma semplificato delle relazioni tra gli oggetti principali in FreeCAD*



## Utilizzo

[Part Part2DObject](Part_Part2DObject.md) è un oggetto interno, quindi non può essere creato dall\'interfaccia grafica, ma solo dalla [console Python](Python_console/it.md) come descritto nel paragrafo [Scripting](#Script.md).


{{Incode|Part::Part2DObject}}

è definito nell\'ambiente [Part](Part_Workbench/it.md) ma può essere usato come classe base per gli [oggetti da script](Scripted_objects/it.md) in tutti gli \[\[Workbenches/it\|ambienti\] \] che producono forme geometriche 2D. Ad esempio, è l\'oggetto base per gli ([Sketcher SketchObject](Sketcher_SketchObject/it.md)) degli schizzi e per la maggior parte degli oggetti creati con [Draft](Draft_Workbench/it.md).

I workbench possono aggiungere diverse proprietà a questo elemento di base per produrre un oggetto con comportamento complesso.



## Proprietà

Vedere [Proprietà](Property/it.md) per tutti i tipi di proprietà che possono avere gli oggetti con script.

Il [Part Part2DObject](Part_Part2DObject/it.md) (classe `Part::Part2DObject`) è derivato da [Part Feature](Part_Feature/it.md) (classe `Part::Feature`) e ne eredita tutte le proprietà.

Il Part Part2DObject ha anche le seguenti proprietà aggiuntive nell\'[editor delle proprietà](Property_editor/it.md). Le proprietà nascoste possono essere visualizzate utilizzando il comando **Mostra tutto** nel menu contestuale dell\'[editor delle proprietà](Property_editor/it.md).



### Dati


{{TitleProperty|Attachment}}

-    <div id="Property_Attacher_Type">
    </div>
    **Attacher Type|String|Hidden**: nome della classe dell\'oggetto motore di collegamento che guida l\'allegato. Il valore predefinito è `Attacher::AttachEnginePlane`.

-    <div id="Property_Support">
    </div>
    **Support|LinkSubList**: è il piano o la faccia che supporta la geometria 2D. Il valore predefinito è un elenco vuoto `[]`.

-    <div id="Property_Map_Mode">
    </div>
    **Map Mode|Enumeration**: {{value|Deactivated}} per impostazione predefinita. Questa proprietà determina un piano che l\'oggetto utilizzerà come riferimento per la geometria 2D. Cliccando sui puntini di sospensione **...** (tre punti), a destra del campo di immissione si avvia il comando [Part EditAttachment](Part_EditAttachment/it.md) che consente di selezionare il piano di appoggio selezionando diversi elementi nella [Vista 3D](3D_view/it.md). Le diverse modalità sono: {{value|Deactivated}}, {{value|Translate origin}}, {{value|Object's XY}}, {{value|Object's XZ}}, {{value|Object's YZ}}, {{value|Plane face}}, {{value|Tangent to surface}}, {{value|Normal to edge}}, {{value|Frenet NB}}, {{value|Frenet TN}}, {{value|Frenet TB}}, {{value|Concentric}}, {{value|Revolution section}}, {{value|Plane by 3 points}}, {{value|Normal to 3 points}}, {{value|Folding}}, {{value|Inertia 2-3}}, {{value|Align O-N-X}}, {{value|Align O-N-Y}}, {{value|Align O-X-Y}}, {{value|Align O-X-N}}, {{value|Align O-Y-N}}, {{value|Align O-Y-X}}.

-    <div id="Property_Map_Reversed">
    </div>
    **Map Reversed|Bool**: il valore predefinito è `False`; se è `True` la direzione Z verrà invertita. Ad esempio, uno [schizzo](Sketch/it.md) verrà capovolto. Nascosto se **Map Mode** è {{value|Deactivated}}.

-    <div id="Property_Map_Path">
    </div>
    **Map Path Parameter|Float|Hidden**: imposta il punto della curva su cui mappare uno [schizzo](Sketch/it.md). Va da {{value|0}} a {{value|1}}, che corrisponde a {{value|start}} e {{value|end}}. Il valore predefinito è {{value|0}}.

-    <div id="Property_Attachment_Offset">
    </div>
    **Attachment Offset|Placement**: la posizione dell\'oggetto nella [vista 3D](3D_view/it.md), rispetto al posizionamento dell\'oggetto allegato. Il posizionamento è definito da un punto `Base` (vettore) e da una `Rotazione` (asse e angolo). Vedi [Posizionamento](Placement/it.md). Nascosto se **Map Mode** è {{value|Deactivated}}.



## Script


**Vedere anche:**

[Script di base per FreeCAD](FreeCAD_Scripting_Basics/it.md), e [script di oggetti](Scripted_objects/it.md).

Vedere [Part Feature](Part_Feature/it.md) per le informazioni generali sull\'aggiunta di oggetti al documento..

Un Part2DObject viene creato con il metodo `addObject()` del documento.


```python
import FreeCAD as App

doc = App.newDocument()
obj = App.ActiveDocument.addObject("Part::Part2DObject", "Name")
obj.Label = "Custom label"
```

Per la sottoclasse [Python](Python/it.md), è necessario creare un oggetto `Part::Part2DObjectPython`.


```python
import FreeCAD as App

doc = App.newDocument()
obj = App.ActiveDocument.addObject("Part::Part2DObjectPython", "Name")
obj.Label = "Custom label"
```


{{Document_objects_navi

}}



---
⏵ [documentation index](../README.md) > [Part](Part_Workbench.md) > Part Part2DObject/it
