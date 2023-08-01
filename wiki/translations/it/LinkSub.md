# LinkSub/it
## Descrizione

Un [LinkSub](LinkSub/it.md) è una struttura dati che viene utilizzata come input per varie funzioni e oggetti; il suo scopo è passare un sottooggetto o sottoelemento (vertice, bordo o faccia) da un oggetto a un altro oggetto che utilizzerà o trasformerà quella geometria.

Un LinkSub è composto da un elenco di due argomenti. 
```python
sub = [argument1, argument2]
```

Il primo argomento è un riferimento a un [oggetto documento](App_DocumentObject/it.md) e il secondo argomento è una stringa di testo che indica il nome interno del sottoelemento. Questo nome ha un numero che inizia con uno e va fino al numero totale di tali sottoelementi. 
```python
sub = [obj1, "Vertex1"]
sub = [obj2, "Face1"]
sub = [obj3, "Edge1"]
```

Il secondo argomento può essere a sua volta un elenco di stringhe, che indica vari sottoelementi dello stesso oggetto documento. 
```python
sub1 = [obj1, ["Vertex1", "Vertex2"]]
sub2 = [obj2, ["Face1", "Face3", "Face5"]]
sub3 = [obj3, ["Vertex1", "Face5", "Edge1", "Edge2"]]
```

È possibile vedere che un [LinkSubList](LinkSubList/it.md) è un elenco di strutture [LinkSub](LinkSub/it.md).

## Script


**Vedere anche:**

[Script di base per FreeCAD](FreeCAD_Scripting_Basics/it.md), [LinkSubList](LinkSubList/it.md).

Un nuovo [oggetto da script](scripted_objects/it.md) può accettare un LinkSub aggiungendo la [proprietà](property/it.md) corrispondente.

È importante ricalcolare gli oggetti prima che i loro sottoelementi vengano utilizzati come input per altri oggetti, altrimenti potrebbe essere prodotto un errore in quanto la geometria potrebbe non contenere una [Shape](Part_TopoShape/it.md) valida.


```python
doc = App.newDocument()

cube = doc.addObject("Part::Box", "Cube")
cyl = doc.addObject("Part::Cylinder", "Cylinder")
doc.recompute()

new_obj = doc.addObject("App::FeaturePython", "New")
new_obj.addProperty("App::PropertyLinkSub", "Geometry")
new_obj.Geometry = [cube, ["Vertex1", "Vertex2"]]

new_obj2 = doc.addObject("App::FeaturePython", "New")
new_obj2.addProperty("App::PropertyLinkSub", "Geometry")
new_obj2.Geometry = [cyl, "Edge1"]

doc.recompute()
```

Il sottoelemento può quindi essere estratto dalla proprietà assegnata e può essere manipolato per fare qualcosa. 
```python
>>> new_obj.Geometry
(<Part::PartFeature>, ['Vertex1', 'Vertex2'])

>>> new_obj.Geometry[1]
['Vertex1', 'Vertex2']

>>> new_obj.Geometry[1][1]
'Vertex2'

>>> new_obj.Geometry[1][1].strip("Vertex")
'2'

>>> int(new_obj.Geometry[1][1].strip("Vertex"))
2
```



---
⏵ [documentation index](../README.md) > LinkSub/it
