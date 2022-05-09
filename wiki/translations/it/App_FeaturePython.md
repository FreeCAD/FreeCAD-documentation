# App FeaturePython/it
{{TOCright}}

## Introduzione


<div class="mw-translate-fuzzy">

Un oggetto <img alt="" src=images/Feature.svg  style="width   *32px;"> [App FeaturePython](App_FeaturePython/it.md), o formalmente un `App   *   *FeaturePython`, è una semplice istanza di [App DocumentObject](App_DocumentObject/it.md) in [Python](Python/it.md).


</div>


<div class="mw-translate-fuzzy">

Questo è un oggetto semplice che per impostazione predefinita non ha molte proprietà, ad esempio nessun [posizionamento](Placement/it.md) né [forma topologica](Part_TopoShape/it.md). Questo oggetto è per uso generale e, fornendolo di proprietà, può essere utilizzato per gestire diversi tipi di dati.


</div>

<img alt="" src=images/FreeCAD_core_objects.svg  style="width   *800px;">


<div class="mw-translate-fuzzy">



*Diagramma semplificato delle relazioni tra gli oggetti principali del programma. La classe `App   *   *FeaturePython* è una semplice implementazione di {{incode|App   *   *DocumentObject` che può essere utilizzata per qualsiasi scopo, poiché di default non ha una [forma topologica](Part_TopoShape/it.md).}}


</div>

## Utilizzo

Un [App FeaturePython](App_FeaturePython/it.md) è un oggetto interno, quindi non può essere creato dall\'interfaccia grafica. È pensato per essere sottoclassato da classi che gestiranno diversi tipi di dati.


<div class="mw-translate-fuzzy">

Per esempio, gli elemnti [Testo](Draft_Text/it.md), [Dimensione](Draft_Dimension/it.md), e [Piano di lavoro proxy](Draft_SetWorkingPlaneProxy/it.md) di [Draft](Draft_Workbench/it.md) sono oggetti `App   *   *FeaturePython` oggetti con un\'icona personalizzata e proprietà aggiuntive. Conservano i dati ma non sono in effetti [Part TopoShape](Part_TopoShape/it.md).


</div>


<div class="mw-translate-fuzzy">

Se l\'oggetto desiderato deve avere un posizionamento, una forma, un allegato o altre proprietà complesse, è meglio creare una delle classi più complesse, ad esempio, [App GeoFeature](App_GeoFeature/it.md), [Part Feature](Part_Feature/it.md), o [Part Part2DObject](Part_Part2DObject/it.md).


</div>

## Proprietà

Vedere [Proprietà](Property/it.md) per tutti i tipi di proprietà che possono avere gli oggetti con script.


<div class="mw-translate-fuzzy">

Un oggetto [App FeaturePython](App_FeaturePython/it.md) (classe `App   *   *FeaturePython`) è derivato dall\'oggetto base [App DocumentObject](App_DocumentObject.md) (classe `App   *   *DocumentObject`), pertanto condivide tutte le proprietà di quest\'ultimo.


</div>


<div class="mw-translate-fuzzy">

Queste sono le proprietà disponibili nell\'[editor delle proprietà](property_editor/it.md). Le proprietà nascoste possono essere mostrate usando il comando **Mostra tutto** nel menu contestuale dell\'[editor delle proprietà](property_editor/it.md).


</div>

### Dati


{{TitleProperty|Base}}

-    **Proxy|PythonObject|Hidden**   * una classe personalizzata associata a questo oggetto.

-    **Label|String**   * il nome modificabile dall\'utente di questo oggetto, è una stringa UTF8 arbitraria.

-    **Label2|String|Hidden**   * una descrizione più lunga e modificabile dall\'utente di questo oggetto, è una stringa UTF8 arbitraria che può includere nuove righe. Per impostazione predefinita, è una stringa vuota {{value|""}}.

-    **Expression Engine|ExpressionEngine|Hidden**   * un elenco di espressioni. Per impostazione predefinita, è vuota {{value|[]}}.

-    **Visibility|Bool|Hidden**   * se visualizzare o no l\'oggetto.

### Vista


{{TitleProperty|Base}}


<div class="mw-translate-fuzzy">

-    **Proxy|PythonObject|Hidden**   * una classe di provider di visualizzazione personalizzata associata a questo oggetto. Questa proprietà esiste solo per quelle classi che sono in grado di assegnare una classe personalizzata.


</div>


<div class="mw-translate-fuzzy">


{{TitleProperty|Display Options}}

-    **Display Mode|Enumeration**   * di default è vuota.

-    **Show In Tree|Bool**   * il valore predefinito è `True`, nel qual caso l\'oggetto appare nella [vista ad albero](tree_view/it.md); in caso contrario, l\'oggetto è nascosto nella vista struttura. Quando un oggetto nell\'albero è invisibile, si può di nuovo enderlo visibile aprendo il menu contestuale sul nome del documento (clic destro) e selezionando {{CheckBox|TRUE|Mostra elementi nascosti}}. Quindi l\'elemento nascosto può essere selezionato e e la sua proprietà **Mostra nell'albero** può essere riportata a `True`.

-    **Visibility|Bool**   * il valore predefinito è `True`, nel qual caso l\'oggetto è visibile nella [vista 3D](3D_view/it.md) se ha una [Forma](Part_TopoShape/it.md), altrimenti è invisibile. Per impostazione predefinita, questa proprietà può essere attivata e disattivata selezionando l\'oggetto e premendo la barra **Spazio** sulla tastiera.


</div>


{{TitleProperty|Selection}}


<div class="mw-translate-fuzzy">

-    **On Top When Selected|Enumeration**   * controlla il modo in cui avviene la selezione nella [vista 3D](3D_view/it.md) se l\'oggetto ha una [Forma](Part_TopoShape/it.md) e ci sono oggetti parzialmente coperti da altri. Il valore predefinito è {{value|Disabled}}, il che significa che non si verifica alcuna evidenziazione speciale; {{value|Enabled}} significa che l\'oggetto appare sopra qualsiasi altro oggetto quando selezionato; {{value|Object}} significa che l\'oggetto appare in primo piano solo se l\'intero oggetto è selezionato nella [vista ad albero](tree_view/it.md); {{value|Element}} significa che l\'oggetto appare in primo piano solo se un sottoelemento (vertice, bordo, faccia) è selezionato in [vista 3D](3D_view/it.md).

-    **Selection Style|Enumeration**   * controlla il modo in cui l\'oggetto è evidenziato se ha una [Forma](Part_TopoShape/it.md). Se è {{value|Shape}}, l\'intera forma (vertici, bordi e facce) è evidenziata nella [vista 3D](3D_view/it.md); se è {{value|BoundBox}} viene evidenziato un riquadro di delimitazione che circonda l\'oggetto.


</div>

## Script


<div class="mw-translate-fuzzy">


**Vedere anche   ***

[Script di base per FreeCAD](FreeCAD_Scripting_Basics/it.md), e [script di oggetti](scripted_objects/it.md).


</div>


<div class="mw-translate-fuzzy">

Vedere [Part Feature](Part_Feature/it.md) per le informazioni generali sull\'aggiunta di oggetti al programma.


</div>

Una App FeaturePython viene creata con il metodo `addObject()` del documento


```python
import FreeCAD as App

doc = App.newDocument()
obj = App.ActiveDocument.addObject("App   *   *FeaturePython", "Name")
obj.Label = "Custom label"
```


{{Document_objects_navi

}}



---
![](images/Right_arrow.png) [documentation index](../README.md) > App FeaturePython/it
