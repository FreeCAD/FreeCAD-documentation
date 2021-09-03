 {{TOCright}}

## Introduzione


<div class="mw-translate-fuzzy">

La [vista ad albero](tree_view/it.md) appare nella scheda **Modello** della [vista combinata](combo_view/it.md); mostra tutti gli oggetti definiti dall\'utente che fanno parte di un documento di FreeCAD. La vista ad albero è una rappresentazione della [struttura del documento](document_structure/it.md) e indica quali informazioni vengono salvate sul disco.


</div>


<div class="mw-translate-fuzzy">

Questi oggetti non devono necessariamente essere forme geometriche visibili nella [vista 3D](3D_view/it.md), ma possono anche oggetti dati di supporto creati con qualsiasi [ambiente](workbenches/it.md).


</div>

![](images/FreeCAD_Tree_view.png )


*La vista ad albero che mostra vari elementi nel documento.*

## Lavorare con la vista ad albero 


<div class="mw-translate-fuzzy">

Per impostazione predefinita, ogni volta che viene creato un nuovo oggetto, questo viene aggiunto alla fine dell\'elenco nella vista ad albero. La vista ad albero consente di gestire gli oggetti per mantenerli organizzati; consente di creare dei [gruppi](Std_Group/it.md), spostare gli oggetti all\'interno dei gruppi, spostare dei gruppi all\'interno di altri gruppi, rinominare oggetti, copiare oggetti, eliminare oggetti e altre operazioni del menu contestuale che dipende anche dall\'ambiente attualmente attivo.


</div>

Molte operazioni creano oggetti che dipendono da un oggetto precedentemente esistente. In questo caso, la vista ad albero mostra questa relazione assorbendo l\'oggetto più vecchio all\'interno del nuovo oggetto. L\'espansione e la compressione degli oggetti nella vista ad albero mostra la cronologia parametrica di quell\'oggetto. Gli oggetti più profondi all\'interno degli altri sono quelli più vecchi, mentre gli oggetti all\'esterno sono i più recenti e sono derivati dagli oggetti più vecchi. Modificando gli oggetti interni, le operazioni parametriche si propagano fino in cima, generando un nuovo risultato.

<img alt="" src=images/FreeCAD_Tree_view_parametric_history_1.png  style="width:" height="304px;"> <img alt="" src=images/FreeCAD_Tree_view_parametric_history_2.png  style="width:" height="304px;">

<img alt="" src=images/FreeCAD_Tree_view_parametric_history_3.png  style="width:" height="304px;">


*L'oggetto di livello più alto viene creato eseguendo operazioni parametriche su oggetti che sono stati creati da operazioni precedenti. L'espansione dell'albero di molti livelli rivela gli elementi originali che sono stati usati per creare i solidi parziali.*

## Azioni


**Nota:**

le espressioni e le azioni link sono state aggiunte nella versione 0.19.


<div class="mw-translate-fuzzy">

Poiché la vista ad albero elenca oggetti che possono essere visibili nella [vista 3D](3D_view/it.md), molte delle azioni sono uguali a quelle che possono essere eseguite nella [vista 3D](3D_view/it.md).


</div>


<div class="mw-translate-fuzzy">

All\'avvio dell\'applicazione, per impostazione predefinita è attivo l\'ambiente [Start](Start_Workbench/it.md) e non viene stato creato alcun documento, facendo clic con il tasto destro del mouse sulla [vista ad albero](tree_view/it.md) appare solo un comando:

-    **Expression actions**: [Copia selezionati](Std_Expressions/it.md), [Copia il documentoattivo](Std_Expressions/it.md), [Copia tutti i documenti](Std_Expressions/it.md), Incolla. Questi comandi consentono di lavorare con vari documenti, ma sono disabilitati se non è presente alcun documento.


</div>

Una volta creato un nuovo documento, diventano attivi i seguenti elementi:

-    **Expression actions**: [Copia il documento attivo](Std_Expressions/it.md), [Copia tutti i documenti](Std_Expressions/it.md).


<div class="mw-translate-fuzzy">

Inoltre, sono disponibili le azioni [Link](Std_LinkMake/it.md).

-    **Link actions**: [Crea Link](Std_LinkMake/it.md).

    -   
        **Make Link group**
        
        : [Gruppo semplice](Std_LinkMakeGroup/it.md), [Gruppo con link](Std_LinkMakeGroup/it.md), [Gruppo con link di trasformazione](Std_LinkMakeGroup/it.md).


</div>

### Selezione del documento 


<div class="mw-translate-fuzzy">

Se si seleziona il documento attivo e si fa clic con il tasto destro, oltre a **Expression actions** and **Azioni link**, vengono visualizzati i seguenti comandi:

-    **Mostra gli elementi nascosti**: se attivo, la vista ad albero mostra gli oggetti nascosti.

-    **Cerca**: mostra un campo di input per cercare oggetti all\'interno del documento selezionato.

-    **Chiudi il documento**: chiude il documento selezionato chiamando il metodo `closeDocument()` dell\'applicazione.

-    **Salta il ricalcolo**: se attivo, gli oggetti del documento non vengono più [ricalcolati](recompute/it.md) automaticamente.

    -   
        **Consenti il ricalcolo parziale**
        
        : se attivo, il documento consente il [ricalcolo](recompute/it.md) solo di alcuni oggetti.

-    **Segna da ricalcolare**: contrassegna tutti gli oggetti del documento come toccati e pronti per il [ricalcolo](recompute/it.md).

-    **[Crea un gruppo](Std_Group/it.md)**: crea un [gruppo](Std_Group/it.md) nel documento selezionato usando il metodo `addObject()` del documento.


</div>

### Selezione degli oggetti 

Una volta aggiunti gli oggetti al documento, oltre alle azioni precedenti, facendo clic con il tasto destro su una parte vuota della vista ad albero vengono mostrati dei comandi aggiuntivi; questi dipendono dal tipo di oggetto e dall\'ambiente attivo.


<div class="mw-translate-fuzzy">

Ad esempio, con [Draft](Draft_Workbench/it.md) attivo, selezionare prima un oggetto, quindi fare clic con il tasto destro su un posto vuoto nella vista ad albero:

-    **[Attiva/disattiva la visibilità](Std_ToggleVisibility/it.md)**: rende l\'oggetto visibile o invisibile nella [vista 3D](3D_view/it.md).

-    **[Mostra la selezione](Std_ShowSelection/it.md)**: rende visibili gli oggetti selezionati.

-    **[Nascondi la selezione](Std_HideSelection/it.md)**: nasconde gli oggetti selezionati.

-    **[Attiva/disattiva la selezionabilità](Std_ToggleSelectability/it.md)**: rende l\'oggetto non più selezionabile nella [Vista 3D](3D_view/it.md); usare di nuovo questo comando per annullarne l\'effetto. Imposta l\'attributo `Selectable` dell\'oggetto su `True` o `False`. Modificare la proprietà attivando **Selectable** nell\'[editor delle proprietà](property_editor/it.md).

-    **[Seleziona tutte le istanze](Std_TreeSelectAllInstances/it.md)**: seleziona tutte le istanze di questo oggetto nella vista ad albero.

-    **[Aspetto](Std_SetAppearance/it.md)**: avvia la finestra di dialogo per modificare il colore e le dimensioni di linee e vertici e il colore delle facce.

-    **[Colore casuale](Std_RandomColor/it.md)**: assegna un colore casuale all\'oggetto. Imposta l\'attributo `ShapeColor` dell\'oggetto su una tupla `(r, g, b)` con un valore casuale compreso tra 0 e 1. Cambia la proprietà modificando **Shape Color** nell\'[editor delle proprietà](property_editor/it.md).

-    **[Taglia](Std_Cut/it.md)**: disabilitato se il cli con il tasto destro non si avviene sull\'oggetto.

-    **[Copia](Std_Copy/it.md)**: copia un oggetto in memoria.

-    **[Incolla](Std_Paste/it.md)**: incolla l\'oggetto copiato nel documento; la copia viene aggiunta alla fine della vista ad albero.

-    **[Elimina](Std_Delete/it.md)**: rimuove l\'oggetto dal documento e dalla vista ad albero chiamando il metodo `removeObject()` del documento.

-    **Utilità**: **(opzionale)** comandi contestuali aggiuntivi forniti da [Draft](Draft_Workbench/it.md).


</div>


<div class="mw-translate-fuzzy">

Se si seleziona un oggetto, ad esempio una [ linea di Draft](Draft_Line/it.md) e si fa clic con il tasto destro nello stesso oggetto, possono essere disponibili comandi aggiuntivi:

-    **Trasforma**: avvia il widget di trasformazione per spostare o ruotare l\'oggetto.

-    **Imposta i colori**: imposta i colori dell\'oggetto.

-    **Appiattisci questo profilo**: **(Draft)** comando specifico per una [linea di Draft](Draft_Line/it.md).

-    **Nascondi l'elemento**: se attivo, l\'oggetto selezionato viene impostato come nascosto.

-    **Segna da ricalcolare**: contrassegna l\'oggetto selezionato come toccato e pronto per il [ricalcolo](recompute/it.md).

-    **Ricalcola**: ricalcola l\'oggetto selezionato.

-    **Rinomina**: avvia la modifica del nome dell\'oggetto selezionato. Ciò consente di modificare l\'attributo `Label`, ma non l\'attributo `Name`, poiché quest\'ultimo è di sola lettura.


</div>

## Overlay icons 

One or more smaller overlay icons can be displayed on top of an object\'s default icon in the tree view. The available overlay icons and their meaning are listed below. <small>(v0.19)</small> 

### ![](images/FreeCAD_Tree_view_recompute.png ) White check mark on blue background 

This indicates that the object has to be [recomputed](Std_Refresh.md), due to changes made to the model or because the user marked the object in the tree view context menu to be recomputed. In most cases recomputes are triggered automatically, but sometimes they are delayed for performance reasons.

### ![](images/FreeCAD_Tree_view_tip.png ) White arrow on green background 

This indicates the so called [Tip](PartDesign_Body#Tip.md) of a body. It is usually the last feature in a [PartDesign Body](PartDesign_Body.md) and represents the whole body to the world outside of the body, e.g. when the body is exported or used in [Part boolean](Part_Boolean.md) operations. The tip can be changed by the user.

### ![](images/FreeCAD_Tree_view_unattached.png ) Purple chain link on white background 

This is typically shown for [sketches](Sketch.md), geometric primitives, such as box, cylinder, etc. and [Datum](Datum.md) geometry. It indicates that the object is not attached to anything. It has no Attachment Offset and gets its position and alignment solely from its [Placement](Placement.md) property.

There is a [Basic Attachment Tutorial](Basic_Attachment_Tutorial.md) explaining how to handle such objects.

### ![](images/FreeCAD_Tree_view_notfullyconstrained.png ) Yellow X 

This is only used for [sketches](Sketch.md) and indicates that the sketch is not fully constrained. Inside of [Sketcher](Sketcher_Workbench.md) the number of remaining degrees of freedom is shown in the solver messages.

### ![](images/FreeCAD_Tree_view_error.png ) White exclamation mark on red background 

This indicates that the object has an error that needs to be fixed. After recomputing the whole document a tooltip describing the error is shown when you hover the mouse over the object in the tree view. Note: All other objects depending on an object in such an error state will not be properly recomputed, thus they may still show some old state.


{{Interface navi

}} {{Std Base navi}} 
