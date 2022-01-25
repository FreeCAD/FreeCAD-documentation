---
- GuiCommand:/it
   Name:Std LinkMake
   Name/it:Crea link
   MenuLocation:None
   Workbenches:Tutti
   Version:0.19
   SeeAlso:[Parte](Std_Part/it.md), [Gruppo](Std_Group/it.md), [Corpo di PartDesign](PartDesign_Body/it.md)
---

# Std LinkMake/it

## Descrizione


**<img src="images/Std_LinkMake.svg" width=16px> [Crea link](Std_LinkMake/it.md)
**

crea un [App Link](App_Link/it.md) (classe `App::Link`), che è un tipo di oggetto che fa riferimento o collega ad un altro oggetto, nello stesso documento o in un altro documento. È appositamente progettato per duplicare in modo efficiente un singolo oggetto più volte, il che aiuta nella creazione di [assemblaggi](assembly/it.md) complessi da sottoassiemi più piccoli e da più componenti riutilizzabili come viti, dadi e dispositivi di fissaggio simili.

L\'oggetto [App Link](App_Link/it.md) è stato introdotto di recente nella versione 0.19; in passato, si poteva ottenere una semplice duplicazione di oggetti con **[<img src=images/Draft_Clone.svg style="width:16px"> [Clona](Draft_Clone/it.md)** di Draft, ma questa è una soluzione meno efficiente a causa della sua implementazione che essenzialmente crea una copia della [Forma (Shape)](Part_TopoShape/it.md) interna dell\'oggetto sorgente. Invece, un link fa riferimento direttamente alla forma originale, quindi è più efficiente in termini di memoria.


<div class="mw-translate-fuzzy">

Di per sé l\'oggetto [Link](App_Link/it.md) può comportarsi come un array, duplicando più volte il suo oggetto base; questo può essere fatto impostando la sua proprietà **Element Count** su {{Value|1}} o più grande. Questo oggetto \"[Link\_Array](Std_LinkMake/it#Link_Array.md)\" può essere creato anche con i diversi strumenti dell\'array <img alt="" src=images/Workbench_Draft.svg  style="width:24px;"> [Ambiente Draft](Draft_Workbench/it.md), per esempio, **[<img src=images/Draft_OrthoArray.svg style="width:16px"> [Draft Serie ortogonale](Draft_OrthoArray/it.md)**, **[<img src=images/Draft_PolarArray.svg style="width:16px"> [Draft Serie polare](Draft_PolarArray/it.md)**, and **[<img src=images/Draft_CircularArray.svg style="width:16px"> [Draft Serie circolare](Draft_CircularArray/it.md)**.


</div>

Quando si lavora con l\'<img alt="" src=images/Workbench_PartDesign.svg  style="width:24px;"> [Ambiente Part Design](PartDesign_Workbench/it.md), i link sono destinati ad essere utilizzati con i **[<img src=images/PartDesign_Body.svg style="width:16px"> [Corpo di Part Design](PartDesign_Body/it.md)**, quindi si consiglia di impostare la modalità {{PropertyView/it|Display Mode Body}} su {{Value|Tip}} per selezionare le caratteristiche dell\'intero corpo, e non le singole caratteristiche. Per creare array di elementi interni [Funzioni di PartDesign](PartDesign_Feature/it.md), utilizzare **[<img src=images/PartDesign_LinearPattern.svg style="width:16px"> [PartDesign Serie lineare](PartDesign_LinearPattern/it.md)**, **[<img src=images/PartDesign_PolarPattern.svg style="width:16px"> [PartDesign Serie polare](PartDesign_PolarPattern/it.md)**, e **[<img src=images/PartDesign_MultiTransform.svg style="width:16px"> [PartDesign Multitransformazione](PartDesign_MultiTransform/it.md)**.

Lo strumento **[<img src=images/Std_LinkMake.svg style="width:16px"> [Crea link](Std_LinkMake/it.md)** non è definito da un particolare banco di lavoro, ma dal sistema di base, quindi si trova nella **Struttura della barra degli strumenti** che è disponibile in tutti gli [ambienti di lavoro](Workbenches/it.md). L\'oggetto Link, usato insieme a **[<img src=images/Std_Part.svg style="width:16px"> [Parte](Std_Part/it.md)** per raggruppare vari oggetti, costituisce la base di <img alt="" src=images/Assembly3_workbench_icon.svg  style="width:24px;"> [Assembly3](Assembly3_Workbench/it.md) e <img alt="" src=images/Assembly4_workbench_icon.svg  style="width:24px;"> [Assembly4 Workbenches](Assembly4_Workbench/it.md).

## Utilizzo

Con selezione:

1.  Selezionare un oggetto nella [vista ad albero](tree_view/it.md) o nella [vista 3D](3D_view/it.md) per il quale si desidera creare un link.
2.  Premere il pulsante **[<img src=images/Std_LinkMake.svg style="width:16px"> [Crea link](Std_LinkMake/it.md)**. L\'oggetto prodotto ha la stessa icona dell\'oggetto originale, ma ha una freccia sovrapposta che indica che è un collegamento.

Senza selezione:

1.  Se non viene selezionato alcun oggetto, premere il pulsante<img alt="" src=images/Link.svg  style="width:24px;"> **[<img src=images/Std_LinkMake.svg style="width:16px"> [Crea link](Std_LinkMake/it.md)** per creare un link vuoto .
2.  Vai all\'[editor delle proprietà](property_editor/it.md), quindi clicca sulla proprietà {{PropertyData/it|Linked Object}} per aprire [metodi di selezione](Selection_methods/it.md) e scegliere un oggetto, poi premi **OK**.
3.  Invece di scegliere un intero oggetto nella [vista ad albero](tree_view/it.md), è anche possibile scegliere i sottoelementi (vertici, bordi o facce) di un singolo oggetto nella [vista 3D](3D_view/it.md). In questo caso, il Link duplicherà solo questi sottoelementi, e la sovrapposizione delle frecce sarà diversa. Questo può essere fatto anche con **[<img src=images/Std_LinkMakeRelative.svg style="width:16px"> [crea un link relativo](Std_LinkMakeRelative/it.md)**.

![](images/Std_Link_tree_example.png ) ![](images/Std_Link_example.png )



*(1) Un oggetto, (2) Un Link vuoto, (3) un Link completo del primo oggetto (con materiale di rivestimento), (4) un collegamento solo ad alcuni sottoelementi dell'oggetto. Il Link vuoto non è legato all'oggetto reale, quindi non viene visualizzato nella [vista 3D](3D_view/it.md).*

## Utilizzo: documenti esterni 

1.  Iniziare con un documento che ha almeno un oggetto che sarà la fonte del Link.
2.  Aprire un nuovo documento o un documento esistente. Per una più facile gestione, usare **[<img src=images/Std_TreeMultiDocument.svg style="width:16px"> [Visualizza Multi documento](Std_TreeMultiDocument/it.md)** per mostrare entrambi i documenti nella [vista ad albero](tree_view/it.md). Prima di procedere, [salva](Std_Save/it.md) entrambi i documenti. Il Link non sarà in grado di trovare la sua fonte e la sua destinazione a meno che entrambi i documenti non siano salvati su disco.
3.  Nel primo documento, selezionare l\'oggetto che si desidera collegare; poi passare alle schede nell\'[area della vista principale](main_view_area/it.md) per passare al secondo documento.
4.  Premere **[<img src=images/Std_LinkMake.svg style="width:16px"> [Crea link](Std_LinkMake/it.md)**. L\'oggetto prodotto ha la stessa icona dell\'oggetto originale, ma ha una freccia aggiuntiva che indica che si tratta di un link proveniente da un documento esterno.


**Notes:**

-   Quando si salva il documento con il Link, verrà anche chiesto di [salvare](Std_Save/it.md) il documento di origine che contiene l\'oggetto originale.

-   Per includere l\'oggetto originale nel documento con il Link, utilizzare **[<img src=images/Std_LinkImport.svg style="width:16px"> [Importa un link](Std_LinkImport/it.md)** oppure **[<img src=images/Std_LinkImportAll.svg style="width:16px"> [Importa tutti i link](Std_LinkImportAll/it.md)**.

-    **[<img src=images/Std_LinkMake.svg style="width:16px"> [Crea link](Std_LinkMake/it.md)**può essere utilizzato su un oggetto Link esistente, al fine di creare un Link ad un Link che si risolve in definitiva con l\'oggetto originale nel documento di origine. Questo può essere utlizato con **[<img src=images/Std_LinkMakeRelative.svg style="width:16px"> [Crea un link relativo](Std_LinkMakeRelative/it.md)** per scegliere anche solo alcuni sotto elementi.

![](images/Std_Link_tree_documents_example.png ) ![](images/Std_Link_documents_example.png )



*(1, 2) Due oggetti di un documento sorgente collegati in un documento di destinazione, (3) un Link al secondo Link (con materiale di sovrascrittura), e (4) un Link ai sotto elementi del secondo Link.*

### Drag and drop 

Invece di passare da una scheda all\'altra del documento, è possibile creare dei Links eseguendo un\'operazione di drag and drop nella [vista ad albero](tree_view/it.md): selezionare l\'oggetto sorgente dal primo documento, trascinarlo, quindi rilasciarlo nel nome del secondo documento tenendo premuto il tasto **Alt** della tastiera.

Il trascinamento porta ad azioni diverse a seconda della tasto di modifica che si sta utilizzando.

-   Senza il tasto di modifica si sposta semplicemente l\'oggetto da un documento all\'altro; una freccia inclinata viene mostrata nel cursore.
-   Tenendo premuto il tasto **Ctrl** si copia l\'oggetto; nel cursore viene mostrato un segno più.
-   Tenendo premuto il tasto **Alt** si crea un collegamento; una coppia di maglie di catena viene mostrata nel cursore.

Per i modificatori **Ctrl** e **Alt**, il trascinamento può essere fatto anche con un singolo documento. Ovvero, trascinando un oggetto e rilasciandolo nel nome dello stesso documento si possono creare più copie o più link ad esso.

## Gruppi


**[<img src=images/Std_LinkMake.svg style="width:16px"> [Crea link](Std_LinkMake/it.md)**

può essere usato su **[<img src=images/Std_Part.svg style="width:16px"> [Parte](Std_Part/it.md)** al fine di duplicare rapidamente gruppi di oggetti posizionati nello spazio, cioè [assemblaggi](assembly/it.md).

![](images/Std_Link_tree_Std_Part_example.png )



*Link creato da una [Parte](Std_Part/it.md); gli oggetti non sono duplicati, ma sono elencati sotto il contenitore originale e sotto il Link contenitore.*

Un regolare **[<img src=images/Std_Group.svg style="width:16px"> [Gruppo](Std_Group/it.md)** non possiede una proprietà {{PropertyData/it|Placement}}, quindi non può controllare la posizione degli oggetti al suo interno. Tuttavia, quando **[<img src=images/Std_LinkMake.svg style="width:16px"> [Crea link](Std_LinkMake/it.md)** è usato con **[<img src=images/Std_Group.svg style="width:16px"> [Gruppo](Std_Group/it.md)**, il Link risultante si comporta essenzialmente come una **[<img src=images/Std_Part.svg style="width:16px"> [Parte](Std_Part/it.md)** e può anche essere spostata nello spazio.

![](images/Std_Link_tree_Std_Group_example.png ) ![](images/Std_Link_Std_Group_example.png )



*Link creato da un [Gruppo](Std_Group/it.md); gli oggetti non sono duplicati ma sono elencati sotto il contenitore originale e sotto il contenitore Link. Il Link (con materiale di sovrascrittura) può essere spostato nello spazio, proprio come una [Parte](Std_Part.md).*

Un collegamento a una **[<img src=images/Std_Part.svg style="width:16px"> [Parte](Std_Part/it.md)** manterrà la visibilità degli oggetti sincronizzati con la Parte originale; quindi se si nasconde un oggetto in un Link, esso sarà nascosto in tutti i Link e nell\'oggetto originale. Invece un Link ad un **[<img src=images/Std_Group.svg style="width:16px"> [Gruppo](Std_Group/it.md)** consentirà il controllo indipendente delle visibilità.

![](images/Std_Link_tree_Std_Part_visibility.png ) ![](images/Std_Link_tree_Std_Group_visibility.png )



*Sinistra: [Parte](Std_Part/it.md) con due oggetti, e due Links alla Parte; la visibilità degli oggetti è sincronizzata. Destra: [Gruppo](Std_Group/it.md) con due oggetti, e due Links al Gruppo; la visibilità degli oggetti è controllata indipendentemente in ogni gruppo.*

## Aspetto dominante 

Quando viene creato un Link, di default la {{PropertyView/it|Override Material}} è `False`, quindi il Link avrà lo stesso aspetto dell\'originale {{PropertyData/it|Linked Object}}.

Quando la {{PropertyView/it|Override Material}} è impostato su `True`, la proprietà {{PropertyView/it|Shape Material}} controllerà l\'aspetto del Link.

Indipendentemente dallo stato della {{PropertyView/it|Override Material}}, è possibile impostare individualmente l\'aspetto dei sottoelementi (vertici, bordi, facce) di un Link.

1.  Selezionare il Link nella [vista ad albero](tree_view/it.md). Aprire il menu contestuale (tasto destro del mouse) e scegliere **Override colors**.
2.  Ora scegliere i singoli sottoelementi che si desidera nella [vista 3D](3D_view/it.md), premere **Edit**, e modificare le proprietà, inclusa la trasparenza.
3.  Per rimuovere gli attributi personalizzati, selezionare gli elementi nella lista, e premere **Remove**.
4.  Quando si è soddisfatti del risultato, premere **OK** per chiudere la finestra di dialogo.


**Nota:**

A partire dalla v0.19, la colorazione dei sottoelementi è soggetta al [problema di denominazione topologica](topological_naming_problem/it.md), quindi dovrebbe essere fatta come ultima fase di modellazione, quando il modello non è più soggetto a modifiche.

<img alt="" src=images/Std_Link_override_color_example.png  style="width:500px;">



*(1) Un oggetto originale, (2) un Link con materiale di sovrascrittura e (3) un secondo Link con singoli sottoelementi modificati.*

## Link Array 


**Vedi anche:**

[Draft: Serie ortogonale](Draft_OrthoArray/it.md).

Quando viene creato un Link, di default il suo {{PropertyData/it|Element Count}} è {{Value|0}}, quindi solo un singolo oggetto Link sarà visibile nella [vista ad albero](tree_view/it.md).

Dato che {{PropertyData/it|Show Element}} è `True` di default, quando {{PropertyData/it|Element Count}} è impostato su {{Value|1}} o più, automaticamente verranno creati più Link sotto il primo; ogni nuovo Link può essere posizionato nella posizione desiderata cambiando la proprietà {{PropertyData/it|Placement}}.

In modo simile, ogni elemento dell\'array può avere il proprio aspetto modificato, sia con le proprietà {{PropertyView/it|Override Material}} e {{PropertyView/it|Shape Material}}, sia usando il menu **Override colors** sull\'intero array e quindi selezionando le singole facce; questo è descritto in [Aspetto dominante](#Aspetto_dominante.md).

<img alt="" src=images/Std_Link_tree_array_example.png ) ![](images/Std_Link_array_example.png  style="width:500px;">



*(1) Oggetto di origine, e (2, 3, 4) un Link array con tre elementi, ciascuno in una posizione diversa. Il primo Link ha il materiale sovrascritto e le facce trasparenti, gli altri due hanno colori personalizzati per le facce.*

Una volta che si è soddisfatti del posizionamento e delle proprietà degli elementi di collegamento nell\'array, si può cambiare {{PropertyData/it|Show Element}} in `False` per nascondere i singoli collegamenti nella [vista ad albero](tree_view/it.md); questo ha il vantaggio di rendere il sistema più reattivo, soprattutto se si hanno molti oggetti nel documento.


<div class="mw-translate-fuzzy">

Quando si crea questo tipo di array Link, è necessario posizionare manualmente ciascuno degli elementi; tuttavia, se si desidera utilizzare modelli specifici per posizionare le copie, è possibile utilizzare gli strumenti di array del <img alt="" src=images/Workbench_Draft.svg  style="width:24px;"> [Ambiente Draft](Draft_Workbench/it.md), come **[<img src=images/Draft_OrthoArray.svg style="width:16px"> [Draft: Serie ortogonale](Draft_OrthoArray/it.md)**, **[<img src=images/Draft_PolarArray.svg style="width:16px"> [Draft: Serie Polare](Draft_PolarArray/it.md)**, e **[<img src=images/Draft_CircularArray.svg style="width:16px"> [Draft: Serie circolare](Draft_CircularArray/it.md)**; questi comandi possono creare copie normali o copie Link a seconda delle opzioni al momento della creazione.


</div>

## Visibilità

Quando {{PropertyData/it|Show Element}} è `True` e i singoli elementi sono elencati nella [vista ad albero](Tree_view/it.md) in un [Link Array](#Link_Array.md), ogni Link può essere mostrato o nascosto premendo la barra **Space** della tastiera.

Un altro modo per nascondere i singoli elementi è usare il menu **Override colors**.

1.  Selezionare l\'array, aprire il menu **Override colors** (click destro).
2.  Nella [vista 3D](3D_view/it.md), scegliere qualsiasi sottoelemento da qualsiasi Link dell\'array.
3.  Premere **Nascondi**. Dovrebbe apparire l\'icona di un occhio <img alt="" src=images/Invisible.svg  style="width:24px;">, ad indicare che questo elemento è stato nascosto dalla [vista 3D](3D_view/it.md). L\'oggetto si mostrerà temporaneamente quando il cursore si posiziona sopra l\'icona <img alt="" src=images/Invisible.svg  style="width:24px;">.
4.  Si può cliccare **OK** per confermare l\'operazione e chiudere la finestra di dialogo. Il collegamento rimarrà nascosto anche se viene mostrato come visibile nella [vista ad albero](tree_view/it.md).

![](images/Std_Link_array_visibility_example.png )



*Finestra di dialogo colore dell'elemento disponibile quando si apre il menu contestuale di un oggetto Link nella vista ad albero.*

Se si desidera ripristinare la visibilità di questo elemento array, entrare di nuovo nella finestra di dialogo, scegliere l\'icona occhio, quindi cliccare su **Remove** per rimuovere lo stato nascosto, e cliccare **OK** per confermare e chiudere la finestra di dialogo. L\'elemento sarà di nuovo visibile nella [vista 3D](3D_view/it.md).

Quando il Link è per una **[<img src=images/Std_Part.svg style="width:16px"> [Parte](Std_Part/it.md)** o un **[<img src=images/Std_Group.svg style="width:16px"> [Gruppo](Std_Group/it.md)**, il menu funziona in modo simile a quello degli array; permette di controllare il colore della faccia, il colore dell\'intero oggetto e la visibilità degli oggetti del gruppo.

![](images/Std_Link_Std_Part_visibility_example.png ) ![](images/Std_Link_Std_Part_visibility_example_3D.png )



*Una [Parte](Std_Part/it.md) contenente tre oggetti e un Link a quella Parte; nel Link, (1) il primo oggetto è reso invisibile, (2) il secondo oggetto ha alcuni sotto-elementi con colori diversi, (3) l'intero terzo oggetto ha un diverso colore e livello di trasparenza.*

## Proprietà

Un [App Link](App_Link/it.md) (`App::Link` class) è derivato dall\'[App DocumentObject](App_DocumentObject/it.md) (`App::DocumentObject` class) di base quindi ha le proprietà di base di quest\'ultimo come {{PropertyData/it|Label}} e {{PropertyData/it|Label2}}.

Di seguito sono riportate le proprietà specifiche disponibili nell\'[editor delle proprietà](Property_editor/it.md). Le proprietà nascoste possono essere mostrate utilizzando il comando **Show all** nel menu contestuale dell\'[editor delle proprietà](Property_editor/it.md).

### Dati


{{TitleProperty| Link}}

-    {{PropertyData/it|Linked Object|XLink}}: indica l\'oggetto sorgente dell\'[App Link](App_Link/it.md); questo può essere un oggetto intero o un sottoelemento dello stesso (vertice, bordo o faccia).

-    {{PropertyData/it|Link Transform|Bool}}: è impostato su `False`, in questo caso il Link sovrascriverà il posizionamento del {{PropertyData/it|Linked Object}}. Se è impostato su `True`, il Link sarà posizionato nella stessa posizione del {{PropertyData/it|Linked Object}}, e il suo posizionamento sarà relativo al posizionamento del {{PropertyData/it|Linked Object}}. Questo può essere ottenuto anche con **[<img src=images/Std_LinkMakeRelative.svg style="width:16px">. [Crea un link relativo](Std_LinkMakeRelative/it.md)**.

-    {{PropertyData/it|Placement|Placement}}: il posizionamento del Link in coordinate assolute.

-    {{PropertyData/it|Link Placement|Placement|Hidden}}: è un offset applicato in aggiunta al {{PropertyData/it|Placement}} dell\'{{PropertyData/it|Linked Object}}. Questa proprietà è normalmente nascosta, ma appare se {{PropertyData/it|Link Transform}} è impostato su `True`; in questo caso, {{PropertyData/it|Placement}} diventa ora nascosto.

-    {{PropertyData/it|Show Element|Bool}}: è impostato di default su `True`, nel qual caso la [vista ad albero](tree_view/it.md) mostrerà le singole copie del Link, a condizione che {{PropertyData/it|Element Count}} sia {{Value|1}} o più grande.

-    {{PropertyData/it|Element Count|IntegerConstraint}}: è impostato su {{Value|0}}. Se è {{Value|1}} o più grande, il [App Link](App_Link/it.md) si comporterà come un array, e duplicherà lo stesso **Linked Object** molte volte. Se **Show Elements** è `True`, ogni elemento dell\'array sarà visualizzato nella [vista ad albero](tree_view/it.md), e ognuno può avere il proprio {{PropertyData/it|Placement}} modificato. Ogni copia del Link avrà un nome basato sul Link [Nome](Object_name/it.md), incrementato da `_iN`, dove `N` è un numero che inizia con `0`. Per esempio, con un singolo `Link`, le copie saranno denominate `Link_i0`, `Link_i1`, `Link_i2`, ecc.

-    {{PropertyData/it|Link Execute|String}}:nome della funzione di esecuzione che verrà eseguita per questo particolare oggetto Link. Il suo valore predefinito è {{Value|'appLinkExecute'}}. Impostarlo su {{Value|'None'}} per disabilitarlo.

-    {{PropertyData/it|Colored Elements|LinkSubHidden|Hidden}}: elenco di link che hanno subito la sovrascrittura del loro colore.

-    {{PropertyData/it|Scale|Float}}: è impostato su {{Value|1.0}}. È un fattore per una scalabilità uniforme in ogni direzione `X`, `Y`, e `Z`. Per esempio, un cubo di {{Value|2 mm}} x {{Value|2 mm}} x {{Value|2 mm}}, che viene scalato da {{Value|2.0}}, risulterà in una forma con dimensioni {{Value|4 mm}} x {{Value|4 mm}} x {{Value|4 mm}}.

-    {{PropertyData/it|Scale Vector|Vector|Hidden}}: il fattore di scala per ogni componente `(X, Y, Z)` per tutti gli elementi Link quando {{PropertyData/it|Element Count}} è {{Value|1}} o più grande. Se **Scale** è diverso da {{Value|1.0}}, lo stesso valore sarà utilizzato nei tre componenti.

-    {{PropertyData/it|Scale List|VectorList}}: il fattore di scala per ogni elemento Link.

-    {{PropertyData/it|Visibility List|BoolList|Hidden}}: {{emphasis|(read-only)}} lo stato di visibilità di ogni elemento Link, o `True` o `False`.

-    {{PropertyData/it|Placement List|PlacementList|Hidden}}: {{emphasis|(read-only)}} il posizionamento per ogni elemento Link.

-    {{PropertyData/it|Element List|LinkList|Hidden}}: l\'elenco degli elementi Link.

-    {{PropertyData/it|_LinkTouched|Bool|Hidden}}:

-    {{PropertyData/it|_ChildCache|LinkList|Hidden}}:


{{TitleProperty|Base}}

-    {{PropertyData/it|Proxy|PythonObject|Hidden}}: una classe personalizzata associata a questo oggetto. Questa esiste solo per la versione [Python](Python/it.md). Vedi [Scripting](Std_LinkMake/it#Scripting.md).

L\'oggetto [App Link](App_Link/it.md) mostra inoltre le proprietà del **Linked Object** originale, quindi l\'[editor delle proprietà](property_editor/it.md) può avere gruppi di proprietà come {{TitleProperty|Attachment}} , {{TitleProperty|Box}}, {{TitleProperty|Draft}} e così via.

### Vista


{{TitleProperty| Link}}

-    **Draw Style|Enumeration**: è predefinito a {{Value|None}}; può essere {{value|Solid}}, {{value|Dashed}}, {{value|Dotted}}, {{value|Dashdot}}; definisce lo stile dei bordi nella [vista 3D](3D_view/it.md).

-    **Line Width|FloatConstraint**: un float che determina la larghezza in pixel dei bordi nella [vista 3d](3D_view/it.md). E\' predefinito a {{value|2.0}}.

-    **Override Material|Bool**: è predefinito a `False`; se impostato su `True` sovrascriverà il materiale dell\'**Linked Object**, e visualizzerà i colori definiti in **Shape Material**.

-    **Point Size|FloatConstraint**: simile a **Line Width**, definisce la dimensione dei vertici.

-    **Selectable|Bool**: se è `True`, l\'oggetto può essere scelto con il puntatore nella [vista 3D](3D_view/it.md). Altrimenti, l\'oggetto non può essere selezionato finché questa opzione non è impostata su `True`.

-    **Shape Material|Material**: questa proprietà include sottoproprietà che descrivono l\'aspetto dell\'oggetto.

    -   
        **Diffuse Color**
        
        , è predefinito a  light blue .

    -   
        **Ambient Color**
        
        , è predefinito a  dark gray .

    -   
        **Specular Color**
        
        , è predefinito a  black .

    -   
        **Emissive Color**
        
        , è predefinito a  black .

    -   
        **Shininess**
        
        , è predefinito a {{Value|0.2}}

    -   
        **Transparency**
        
        , è predefinito a {{Value|0.0}}.


{{TitleProperty|Base}}

-    **Child View Provider|PersistentObject|Hidden**:

-    **Material List|MaterialList|Hidden**: **(read-only)** se sono stati aggiunti materiali individuali, saranno elencati qui.

-    **Override Color List|ColorList|Hidden**: **(read-only)** se le singole facce o i bordi del collegamento sono stati sovrascritti saranno elencati qui.

-    **Override Material List|BoolList|Hidden**: **(read-only)** se i singoli materiali del link sono stati sovrascritti saranno elencati qui.


{{TitleProperty|Opzioni di visualizzazione}}

-    **Display Mode|Enumeration**: {{Value|'Link'}} or {{Value|'ChildView'}}.

-    **Show In Tree|Bool**: vedere le informazioni in [App FeaturePython](App_FeaturePython/it.md).

-    **Visibility|Bool**: vedere le informazioni in [App FeaturePython](App_FeaturePython/it.md).


{{TitleProperty|Selezione}}

-    **On Top When Selected|Enumeration**: vedere le informazioni in [App FeaturePython](App_FeaturePython/it.md).

-    **Selection Style|Enumeration**: vedere le informazioni in [App FeaturePython](App_FeaturePython/it.md).

Mostra inoltre le proprietà Vista dell\'originale **Linked Object**.

## Eredità

Un [App Link](App_Link/it.md) è formalmente un\'istanza della classe `App::Link`, il cui genitore è il genitore di base [App DocumentObject](App_DocumentObject/it.md). (`App::DocumentObject` class). È un oggetto di livello molto basso, che può essere usato con la maggior parte degli altri oggetti documento.

<img alt="" src=images/FreeCAD_core_objects.svg  style="width:800px;">



*Diagramma semplificato delle relazioni tra gli oggetti principali del programma. L'oggetto `App::Link* è un componente principale del sistema, non dipende da alcun ambiente, ma può essere utilizzato con la maggior parte degli oggetti creati in tutti gli ambienti.`

## Script


**See also:**

[Script di base per FreeCAD](FreeCAD_Scripting_Basics/it.md), e [script di oggetti](scripted_objects/it.md).

Vedere [Funzione Part](Part_Feature/it.md) per le informazioni generali.

Un App Link viene creato con il metodo `addObject()` del documento. Questo può definire il suo **Linked Object** sovrascrivendo il suo attributo `LinkedObject`, o usando il suo metodo `setLink`. 
```python
import FreeCAD as App

doc = App.newDocument()
bod1 = App.ActiveDocument.addObject("Part::Box", "Box")
bod2 = App.ActiveDocument.addObject("Part::Cylinder", "Cylinder")
bod1.Placement.Base = App.Vector(10, 0, 0)
bod2.Placement.Base = App.Vector(0, 10, 0)

obj1 = App.ActiveDocument.addObject("App::Link", "Link")
obj2 = App.ActiveDocument.addObject("App::Link", "Link")

obj1.LinkedObject = bod1
obj2.setLink(bod2)
obj1.Placement.Base = App.Vector(-10, -10, 0)
obj2.Placement.Base = App.Vector(10, -10, 0)
obj1.ViewObject.OverrideMaterial = True
App.ActiveDocument.recompute()
```

Questo `App::Link` non ha un oggetto Proxy, quindi non può essere pienamente utilizzato per la sotto-classe.

Pertanto, per la sottoclasse [Python](Python/it.md), è necessario creare l\'oggetto `App::LinkPython`.


```python
import FreeCAD as App

doc = App.newDocument()
obj = App.ActiveDocument.addObject("App::LinkPython", "Link")
obj.Label = "Custom label"
```

## Ulteriori letture 

L\'oggetto [App Link](App_Link/it.md) è stato introdotto dopo 2 anni di sviluppo e prototipazione. Questo componente è stato pensato e sviluppato quasi da solo dall\'utente **realthunder**. Le motivazioni e le implementazioni progettuali alla base di questo progetto sono descritte nella sua pagina GitHub, [Link](https://github.com/realthunder/FreeCAD_assembly3/wiki/Link). Per realizzare questa funzione, sono state apportate diverse modifiche fondamentali a FreeCAD; anche queste sono state ampiamente documentati in [Core-Changes](https://github.com/realthunder/FreeCAD_assembly3/wiki/Core-Changes).

Il progetto App Link è iniziato dopo la riprogettazione del [Ambiente PartDesign](PartDesign_Workbench/it.md) è stato completato nella v0.17. La storia di App Link può essere rintracciata in alcuni thread essenziali del forum:

-   [Why an object can only be inside one App::Part?](https://forum.freecadweb.org/viewtopic.php?f=19&t=21505) (Marzo 2017)
-   [Introducing App::Link/XLink](https://forum.freecadweb.org/viewtopic.php?f=10&t=21586) (Marzo 2017)
-   [Links](https://forum.freecadweb.org/viewtopic.php?f=20&t=22216) (Maggio 2017)
-   [Realthunder Link implementation: Architecture discussion](https://forum.freecadweb.org/viewtopic.php?f=20&t=23015) (Giugno 2017)
-   [PR \#876: Link, stage one, context aware selection](https://forum.freecadweb.org/viewtopic.php?f=17&t=23419) (Luglio 2017)
-   [Preview: Link, stage two, API groundwork](https://forum.freecadweb.org/viewtopic.php?f=17&t=23626) (Luglio 2017)
-   [Assembly3 preview](https://forum.freecadweb.org/viewtopic.php?f=20&t=25712) (Deicembre 2017)
-   [Merging of my Link branch](https://forum.freecadweb.org/viewtopic.php?f=10&t=29542) (Giugno 2018)

Infine, la richiesta di pull e il merge sono avvenuti:

-   [App::Link: the big merge](https://forum.freecadweb.org/viewtopic.php?f=27&t=38621), vecchio thread (Luglio 2019), [pull request \#2350](https://github.com/FreeCAD/FreeCAD/pull/2350) (la GRANDE fusione), [LinkMerge branch](https://github.com/realthunder/FreeCAD/tree/LinkMerge).
-   [App::Link: the big merge](https://forum.freecadweb.org/viewtopic.php?f=8&t=37757), thread principale (Luglio 2019)
-   [A simple path description of Link, 019, Link stage, Asm3, merge?](https://forum.freecadweb.org/viewtopic.php?p=329054#p329054) (Agosto 2019)
-   [PR\#2559: expose link and navigation actions](https://forum.freecadweb.org/viewtopic.php?f=17&t=39672), un\'introduzione alla funzione Link in 0.19 (Settembre 2019).

Other miscellaneous \"links\" about Link include:

-   [Dynamic linked object](Dynamic_linked_object.md) - A pattern with Link and assemblies that aims to reduce duplication of assembly related logic such as orientation, positioning, or number of instances.





{{Std Base navi

}}



---
![](images/Right_arrow.png) [documentation index](../README.md) > Std LinkMake/it
