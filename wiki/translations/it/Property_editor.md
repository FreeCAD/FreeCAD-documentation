# Property editor/it
{{TOCright}}



## Descrizione

L\'[editor delle proprietà](property_editor/it.md) appare quando è attiva la scheda **Modello** della [vista combinata](combo_view/it.md) nell\'[interfaciia](interface/it.md); consente di gestire le proprietà degli oggetti nel documento.

Generalmente, l\'editor delle proprietà è destinato a gestire solo un oggetto alla volta. I valori mostrati nell\'editor appartengono all\'oggetto selezionato nel documento attivo. Nonostante questo, alcune proprietà come i colori, possono essere impostate per più oggetti selezionati. Se non ci sono elementi selezionati, l\'editor delle proprietà è vuoto.

Non tutte le proprietà possono sempre essere modificate; a seconda dello stato specifico della proprietà, alcune di esse possono essere invisibili (non elencate) o di sola lettura (non modificabili).


{{TOCright}}

![](images/FreeCAD_Property_editor_empty.png )



*Editore delle proprietà vuoto, quando nessun oggetto è selezionato.*



## Tipi di proprietà 

Una proprietà è un\'informazione come un numero o una stringa di testo allegata a un documento di FreeCAD o ad un oggetto del documento.

Gli oggetti creati con [script personalizzati](scripted_objects/it.md) possono utilizzare qualsiasi tipo di proprietà definita nel sistema di base. Vedere l\'elenco completo in [Proprietà degli oggetti](Property/it.md).

Alcuni dei tipi di proprietà più comunemente usati sono:


```python
App::PropertyBool
App::PropertyFloat
App::PropertyAngle
App::PropertyDistance
App::PropertyInteger
App::PropertyString
App::PropertyMatrix
App::PropertyVector
App::PropertyPlacement
```

Oggetti diversi possono avere tipi di proprietà diverse. Tuttavia, molti oggetti hanno gli stessi tipi perché sono derivati dalla stessa classe interna. Ad esempio, la maggior parte degli oggetti che descrivono le forme geometriche (linee, cerchi, rettangoli, corpi solidi, parti importate, ecc.) hanno la proprietà \"Posizionamento\" che definisce la loro posizione nella [Vista 3D](3D_view/it.md).



## Proprietà Vista e Dati 

Ci sono due classi di proprietà delle funzioni accessibili tramite le schede nell\'editore delle proprietà:

-   Proprietà **Vista** relative all\'aspetto \"visivo\" dell\'oggetto. Le proprietà **Vista** sono legate all\'attributo **ViewProvider** (`ViewObject`) dell\'oggetto e sono accessibili solo quando viene caricata l\'interfaccia utente grafica (GUI). Non sono accessibili quando si utilizza FreeCAD in modalità console o come libreria senza testa.
-   Proprietà **Dati** relative ai parametri \"fisici\" dell\'oggetto. Le proprietà **Dati** definiscono le caratteristiche essenziali dell\'oggetto; esistono sempre, anche quando FreeCAD viene utilizzato in modalità console o come libreria. Ciò significa che se si carica un documento in modalità console, è possibile modificare il raggio di un cerchio o la lunghezza di una linea, anche se non è possibile visualizzare il risultato sullo schermo.

Per questo motivo, le proprietà **Dati** sono considerate più \"reali\", in quanto definiscono veramente la geometria di una forma. Invece le proprietà **Vista** sono meno importanti perché influenzano solo l\'aspetto supericiale della geometria. Ad esempio, un cerchio di raggio di 10 mm è diverso da un cerchio di raggio di 5 mm; il colore del cerchio (proprietà vista) non influisce sulla sua forma, ma il raggio (proprietà dati) sì. In molti casi in questa documentazione, si intende che la parola \"proprietà\" si riferisce a una \"proprietà dati\" e non ad una \"proprietà vista\".



### Proprietà di base 


**Vedere anche: [Nome dell'oggetto](Object_name/it.md)**

L\'oggetto [script](scripted_objects/it.md) più semplice non mostra alcuna proprietà **Dati** nell\'editor delle proprietà, ad eccezione dell\'attributo `Label`. {{Incode|Label}} è una stringa modificabile dall\'utente che identifica l\'oggetto nella [vista ad albero](tree_view/it.md). Invece, l\'attributo `Name` di un oggetto viene assegnato al momento della sua creazione e non può essere modificato; questo attributo è di sola lettura e non viene nemmeno visualizzato nell\'editor delle proprietà.

Un oggetto parametrico di base viene creato nel modo seguente:


```python
obj = App.ActiveDocument.addObject("App::FeaturePython", "App__FeaturePython")
obj.Label = "Plain_object"
print(obj.Name)
print(obj.Label)
```

<img alt="" src=images/FreeCAD_Property_editor_View_basic.png  style="width:" height="264px;"> <img alt="" src=images/FreeCAD_Property_editor_Data_basic.png  style="width:" height="264px;">



*Schede Vista e Dati dell'editor delle proprietà, per un oggetto script di base "App::FeaturePython".*

La maggior parte degli oggetti geometrici che possono essere creati e visualizzati nella [vista 3D](3D_view/it.md) sono derivati da una `Part::Feature`. Vedere [Part Feature](Part_Feature/it.md) per le proprietà più basilari di questi oggetti.

Per la geometria 2D, la maggior parte degli oggetti deriva da `Part::Part2DObject` (essi stessi derivati da `Part::Feature`) che sono la base di [Schizzi](Sketch/it.md), e di molti elementi di [Draft](Draft_Workbench/it.md). Vedere [Part Part2DObject](Part_Part2DObject/it.md) per le proprietà più basilari di questi oggetti.



## Azioni


{{Version/it|0.19}}

Facendo clic con il tasto destro in uno spazio vuoto della vista o con una proprietà selezionata, viene visualizzato solo un comando:

-    **Mostra tutto**: se attivo, oltre alle proprietà standard che appaiono già, mostra tutti i dati nascosti e visualizza le proprietà nelle rispettive schede.

    -   Dati: \"Proxy\", \"Label2\", \"Expression Engine\", and \"Visibility\".
    -   Vista: \"Proxy\".

Quando l\'opzione **Mostra tutto** è attiva e viene selezionata una proprietà, facendo un secondo clic con il tasto destro sono disponibili altre azioni:

-    **Mostra tutto**: disattiva il comando **Mostra tutto** e nasconde le proprietà aggiuntive di Dati e Vista.

-    **Aggiungi proprietà**: aggiunge una proprietà dinamica all\'oggetto; funziona con oggetti definiti in [script](scripted_objects/it.md) C++ e Python.

-    **Espressione**: visualizza l\'editor delle formule, che consente di utilizzare le [espressioni](Expressions/it.md) nel valore della proprietà.

-    **Hidden**: se attivo, imposta la proprietà come nascosta, il che significa che verrà visualizzata nell\'editor delle proprietà solo se **Mostra tutto** è attivo.

-    **Output**: se attivo, imposta la proprietà come output.

-    **NoRecompute**: se attivo, imposta la proprietà come non ricalcolata quandi il documento viene ricalcolato; è utile quando una proprietà non deve essere influenzata da altri aggiornamenti.

-    **ReadOnly**: se attivo, imposta la proprietà in sola lettura; non sarà più modificabile nell\'editor delle proprietà fino a quando questo interruttore non viene disattivato.La voce di menu **Expression...** non è più disponibile. **Nota:** Potrebbe essere ancora possibile modificare la proprietà tramite una finestra di dialogo che aggiorna la proprietà.

-    **Transient**: se attivo, imposta la proprietà come transitoria. Il valore di una proprietà transitoria non viene salvato su file. Quando si apre un file, viene istanziata con il suo valore predefinito.

-    **Touched**: se attivo, viene toccato e pronto per il ricalcolo.

-    **EvalOnRestore**: se attivo, viene valutato al ripristino del documento.



## Esempio di proprietà di un oggetto PartDesign 

In questa sezione mostriamo alcune proprietà comuni che sono visibili per un [Corpo PartDesign](Corpo_PartDesign.md) e una [Funzione PartDesign](Funzione_PartDesign.md). Le proprietà specifiche di un oggetto possono essere trovate nella pagina della documentazione specifica di quell\'oggetto.



### Vista

La maggior parte di queste proprietà viene ereditata dall\'oggetto di base [Funzione Part](Part_Feature/it.md).

<img alt="" src=images/FreeCAD_Property_editor_View.png  style="width:490px;">


{{TitleProperty|Base}}

-    **Angular Deflection**: è un altro modo per specificare quanto finemente generare la mesh per il rendering sullo schermo o durante l\'esportazione. Il valore predefinito è 28,5 gradi o 0,5 radianti. Più piccolo è il valore, più uniforme sarà l\'aspetto in [Vista 3D](3D_view/it.md) e più fine sarà la mesh che verrà esportata.

-    **Bounding Box**: Indica se deve essere visualizzata una casella che mostra l\'ingombro complessivo dell\'oggetto.

-    **Deviation**: imposta la precisione della rappresentazione poligonale del modello nella vista 3D (tassellatura). Valori più bassi indicano una migliore qualità. Il valore è in percentuale della dimensione dell\'oggetto.

-    **Display Mode**: modalità di visualizzazione dell\'intero corpo,{{Value|Flat lines}} (default), {{Value|Shaded}}, {{Value|Wireframe}}, {{Value|Points}}.

-    **Display Mode Body**: modalità di visualizzazione della punta del corpo, {{Value|Through}} (default), {{Value|Tip}}.

-    **Draw Style**: {{Value|Solid}}, {{Value|Dashed}}, {{Value|Dotted}}, {{Value|Dashdot}}; definisce lo stile dei bordi nella [vista 3D](3D_view/it.md).

-    **Lighting**: {{Value|One side}}, {{Value|Two side}} (default).

-    **Line Color**: il colore RGB dei bordi, di default {{value|(25, 25, 25)}}.

-    **Line Width**: lo spessore dei bordi, di default {{value|2}} pixels.

-    **On Top When Selected**: {{value|Disabled}}, {{value|Enabled}}, {{value|Object}}, {{value|Element}}.

-    **Point Color**: il colore RGB dei vertici, di default {{value|(25, 25, 25)}}.

-    **Point Size**: la dimensione dei vertici, di default {{value|2}} pixels.

-    **Selectable**: se l\'oggetto è selezionabile o meno.

-    **Selection Style**: {{value|Shape}}, {{value|BoundBox}}.

-    **Shape Color**: il colore RGB della forma, di default {{value|(204, 204, 204)}}.

-    **Show In Tree**: se è `True`, l\'oggetto appare nella vista ad albero. Altrimenti, è impostato come invisibile.

-    **Transparency**: imposta il grado di trasparenza nella funzione da **0** a **100** (Default, **0**).

-    **Visibility**: se l\'oggetto è visibile o no nella [vista 3D](3D_view/it.md). Commuta con la barra **Space** della tastiera.









### Dati

In questo caso osserviamo le proprietà dello strumento [Rivoluzione di PartDesign](PartDesign_Revolution/it.md).

<img alt="" src=images/FreeCAD_Property_editor_Data.png  style="width:490px;">


{{TitleProperty|Base}}

-    {{ProprietaDati|Label}}: il nome definito dall\'utente assegnato all\'oggetto, questo può essere modificato a piacere.


{{TitleProperty|Part Design}}

-    **Refine**: se affinare la fusione fatta con altri oggetti.


{{TitleProperty|Rivoluzione}}

-    **Base**: il punto nello spazio che specifica dove avviene la rivoluzione. Non può essere modificato direttamente, solo durante la modifica della funzione.

-    **Asse**: l\'asse attorno al quale verrà eseguita la rivoluzione. Non può essere modificato direttamente, solo durante la modifica della funzione.

-    **Angolo**: l\'angolo che specifica quanto dell\'elemento base viene ruotato. Per impostazione predefinita è {{value|360 gradi}}, ma può essere qualsiasi sua frazione.


{{TitleProperty|Sketch Based}}

-    **Midplane**: se l\'oggetto di base è uno [Sketch](Sketch.md), quando questa proprietà è `True`, eseguirà la rivoluzione con lo schizzo che funge da piano di simmetria. Questo è evidente se l\' **Angolo** è diverso da {{value|360 gradi}}.

-    **Reversed**: di default è `True`. Indica se eseguire la rivoluzione in una direzione o nell\'altra.




## Scripting


**See also:**

[Script di base per FreeCAD](FreeCAD_Scripting_Basics/it.md).

Vedere [script di oggetti](scripted_objects/it.md) per le informazioni complete sull\'aggiunta di proprietà agli oggetti definiti tramite [Python](Python/it.md).

È possibile accedere alla maggior parte delle proprietà visibili nell\'editor delle proprietà dalla [console Python](Python_console/it.md). Queste proprietà sono solo attributi della classe che definisce l\'oggetto selezionato. Ad esempio, se l\'editor delle proprietà mostra la proprietà **Group**, significa che l\'oggetto ha l\'attributo `Group`.


```python
print(obj.Group)
```

Questi attributi (proprietà) vengono aggiunti con il metodo `addProperty` dell\'oggetto base. È necessario specificare almeno il tipo di [proprietà](proprietà.md), e il suo nome.


```python
obj.addProperty("App::PropertyFloat", "Custom")
print(obj.Custom)
```

Le proprietà seguono la convenzione `CapitalCamelCase` o `PascalCase`, il che significa che ogni parola inizia con una lettera maiuscola e non ci sono trattini bassi. Quando l\'editor di proprietà visualizza tali nomi, lascia uno spazio tra ogni lettera maiuscola, facilitandone la lettura.


```python
obj.addProperty("App::PropertyDistance", "CustomCamelProperty")
obj.CustomCamelProperty = 1000
print(obj.CustomCamelProperty)
```

![](images/FreeCAD_Property_editor_Custom.png ) 
*Editor di proprietà che mostra le proprietà dei dati di un [Corpo PartDesign](PartDesign_Body/it.md), con due proprietà aggiuntive, "Personalizzato" e "Proprietà Camel personalizzata".*

In modo simile vengono aggiunte le proprietà **View**, non all\'oggetto base, ma al suo `ViewObject`. Quindi, ne consegue che proprietà come **Angular Deflection**, **Bounding Box**, **Display Mode**, **Display Mode Body**, **Line Color**, e altri, possono essere esaminati e modificati dalla [console Python](Python_console/it.md).


```python
print(obj.ViewObject.AngularDeflection)
print(obj.ViewObject.BoundingBox)
print(obj.ViewObject.DisplayMode)
print(obj.ViewObject.DisplayModeBody)
print(obj.ViewObject.LineColor)
```

Tutte le proprietà pubbliche dell\'oggetto e del relativo provider di visualizzazione sono contenute nell\'attributo `PropertiesList` corrispondente.


```python
print(obj.PropertiesList)
print(obj.ViewObject.PropertiesList)
```


{{docnav/it
|[Struttura del documento](Document_structure/it.md)
|[Ambienti di lavoro](Workbenches/it.md)
}}


{{Interface navi

}} {{Std Base navi}}



---
![](images/Right_arrow.png) [documentation index](../README.md) > Property editor/it
