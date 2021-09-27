# Part Part2DObject/it
## Introduzione

<img alt="" src=images/Tree_Part2D.svg  style="width:32px;">

Un _ che può essere visualizzato nella [Vista 3D](3D_view/it.md).


{{Incode|Part::Part2DObject}}

è derivato da una [Part Feature](Part_Feature/it.md), ma è specializzato nella geometria 2D, dato che la sua forma è posizionata su un piano. Il piano è definito dalla sua proprietà **Placement** (posizione, normale e rotazione). Tuttavia, il piano può anche essere definito supportando elementi geometrici, come il piano creato da tre vertici arbitrari o una faccia di un corpo solido.

<img alt="" src=images/FreeCAD_core_objects.svg  style="width:800px;">


*Diagramma semplificato delle relazioni tra gli oggetti principali in FreeCAD. La classe `Part::Part2DObject* è specializzata per le forme 2D, quindi è la classe di base per gli oggetti planari creati con gli ambienti Draft e Sketcher. Include un'estensione che consente di collegarla a facce e piani`

## Utilizzo

[Part Part2DObject](Part_Part2DObject.md) è un oggetto interno, quindi non può essere creato dall\'interfaccia grafica, ma solo dalla [console Python](Python_console/it.md) come descritto nel paragrafo [Script](Part_Part2DObject/it#Script.md).


{{Incode|Part::Part2DObject}}

è definito nell\'ambiente [Part](Part_Workbench/it.md) ma può essere usato come classe base per gli [oggetti da script](scripted_objects/it.md) in tutti gli \[\[Workbenches/it\|ambienti\] \] che producono forme geometriche 2D. Ad esempio, è l\'oggetto base per gli ([Sketcher SketchObject](Sketcher_SketchObject/it.md)) degli schizzi e per la maggior parte degli oggetti creati con [Draft](Draft_Workbench/it.md).

I workbench possono aggiungere diverse proprietà a questo elemento di base per produrre un oggetto con comportamento complesso.

## Proprietà

Vedere [Proprietà](Property/it.md) per tutti i tipi di proprietà che possono avere gli oggetti con script.

Un _ (classe `Part::Feature`), pertanto condivide tutte le proprietà di quest\'ultimo.

Oltre alle proprietà descritte in [Part Feature](Part_Feature/it.md), Part Part2DObject ha le seguenti proprietà nell\'[editor delle proprietà](property_editor/it.md). Le proprietà nascoste possono essere mostrate usando il comando **Mostra tutto** nel menu contestuale dell\'[editor delle proprietà](property_editor/it.md).

### Dati


<div class="mw-translate-fuzzy">


{{TitleProperty|Attachment}}

-    **Map Mode|Enumeration**: {{value|Deactivated}} di default. Questa proprietà definisce il piano che l\'oggetto utilizza come riferimento per la geometria 2D. Facendo clic sui puntini di sospensione **...** (tre puntini), a destra del campo di immissione si apre il pannello [Part Attachment](Part_Attachment/it.md) della [scheda azioni](task_panel/it.md) che consente di selezionare il piano di supporto selezionando diversi elementi nella [vista 3D](3D_view/it.md). Le diverse modalità sono: {{value|Deactivated}}, {{value|Translate origin}}, {{value|Object's XY}}, {{value|Object's XZ}}, {{value|Object's YZ}}, {{value|Plane face}}, {{value|Tangent to surface}}, {{value|Normal to edge}}, {{value|Frenet NB}}, {{value|Frenet TN}}, {{value|Frenet TB}}, {{value|Concentric}}, {{value|Revolution section}}, {{value|Plane by 3 points}}, {{value|Normal to 3 points}}, {{value|Folding}}, {{value|Inertia 2-3}}, {{value|Align O-N-X}}, {{value|Align O-N-Y}}, {{value|Align O-X-Y}}, {{value|Align O-X-N}}, {{value|Align O-Y-N}}, {{value|Align O-Y-X}}.


</div>


<div class="mw-translate-fuzzy">

Vedere [Part Attachment](Part_Attachment/it.md) per ulteriori informazioni su tutte le modalità di associazione.


</div>

Le seguenti due proprietà sono normalmente nascoste. Diventano visibili una volta che **Map Mode** è qualcosa di diverso da {{value|Deactivated}}.

-    **Map Reversed|Bool**: il valore predefinito è `False`; se è `True` la direzione Z sarà invertita. Ad esempio, uno [schizzo](sketch/it.md) verrà capovolto.

-    **Attachment Offset|Placement**: la posizione dell\'oggetto nella [vista 3D](3D_view/it.md), rispetto al posizionamento dell\'oggetto associato. Il posizionamento è definito da un punto `Base` (vettore), e una `Rotation` (asse e angolo). Vedere [Posizionamento](Placement/it.md).

#### Proprietà dati nascoste 


{{TitleProperty|Base}}

-    **Proxy|PythonObject**: una classe personalizzata associata a questo oggetto. Questo esiste solo per la versione [Python](Python/it.md). Vedere [Script](Part_Part2DObject/it#Script.md).


{{TitleProperty|Attachment}}

-    **Attacher Type|String**: nome della classe dell\'oggetto motore dell\'associazione che guida l\'associazione. L\'impostazione predefinita è `Attacher::AttachEnginePlane`.

-    **Support|LinkSubList**: è il piano o la faccia che supporta la geometria 2D. L\'impostazione predefinita è un elenco vuoto `[]`.

-    **Map Path Parameter|Float**: imposta il punto della curva su cui mappare uno [schizzo](sketch/it.md). Va da {{value|0}} a {{value|1}}, che corrispondono a {{value|start}} e {{value|end}}. L\'impostazione predefinita è {{value|0}}.

### Vista


{{TitleProperty|Grid}}

-    **Grid Size|Length**: un valore che determina la dimensione della spaziatura delle linee della griglia locale nella [vista 3D](3D_view/it.md). Il valore predefinito è {{value|10 mm}}.

-    **Grid Snap|Bool**: Il valore predefinito è `False`; se è `True` la griglia può essere utilizzata per agganciare i punti.

-    **Grid Style|Enumeration**: lo stile delle linee della griglia; {{value|Dashed}} (default) o {{value|Light}}.

-    **Show Grid|Bool**: Il valore predefinito è `False`; se è `True` nella [vista 3D](3D_view/it.md) viene visualizzata una griglia locale all\'oggetto. Questa griglia è indipendente dalla [griglia di Draft](Draft_ToggleGrid/it.md).

-    **Tight Grid|Bool**: se è `True` (default) la griglia locale è localizzata attorno all\'origine della forma, altrimenti si estende oltre.

#### Proprietà vista nascoste 


{{TitleProperty|Base}}

-    **Proxy|PythonObject**: una classe del provider di visualizzazione personalizzata associata a questo oggetto. Questo esiste solo per la versione [Python](Python/it.md). Vedere [Script](Part_Part2DObject/it#Script.md).

Tutte le altre proprietà della vista, comprese le proprietà nascoste, sono quelle dell\'oggetto base [Part Feature](Part_Feature/it.md).

## Script


**Vedere anche:**

[Script di base per FreeCAD](FreeCAD_Scripting_Basics/it.md), e [script di oggetti](scripted_objects/it.md).

Vedere [Part Feature](Part_Feature/it.md) per le informazioni generali sull\'aggiunta di oggetti al documento..

Un Part2DObject viene creato con il metodo `addObject()` del documento. 
```python
import FreeCAD as App

doc = App.newDocument()
obj = App.ActiveDocument.addObject("Part::Part2DObject", "Name")
obj.Label = "Custom label"
```

Questo `Part::Part2DObject` di base non ha un oggetto Proxy, quindi non può essere utilizzato completamente per la sottoclassificazione.

Pertanto, per la sottoclasse [Python](Python/it.md), è necessario creare l\'oggetto `Part::Part2DObjectPython`.


```python
import FreeCAD as App

doc = App.newDocument()
obj = App.ActiveDocument.addObject("Part::Part2DObjectPython", "Name")
obj.Label = "Custom label"
```

Ad esempio, la maggior parte degli strumenti di [Draft](Draft_Workbench/it.md), come [Linea](Draft_Line/it.md), [Rettangolo](Draft_Rectangle/it.md), [Poligono](Draft_Polygon/it.md), ecc., sono oggetti `Part::Part2DObjectPython` con un\'icona personalizzata e proprietà aggiuntive.

---
[documentation index](../README.md) > [Part](Part_Workbench.md) > Part Part2DObject/it
