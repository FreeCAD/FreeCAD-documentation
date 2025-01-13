# Property editor/it
## Descrizione

L\'[Editor delle proprietà](Property_editor/it.md) appare nella sezione inferiore del pannello **Model** (se la [Vista combinata](Combo_view/it.md) è attiva) o come pannello autonomo chiamato **Vista proprietà**.

Generalmente, l\'Editor delle Proprietà è destinato a gestire solo un oggetto alla volta. I valori mostrati nell\'Editor appartengono all\'oggetto selezionato nel documento attivo. Nonostante questo, alcune proprietà come i colori, possono essere impostate per più oggetti selezionati. Se non ci sono elementi selezionati, l\'Editor delle Proprietà è vuoto.

Non tutte le proprietà possono essere modificate, alcune sono di sola lettura.

<img alt="" src=images/FreeCAD_Property_editor_Data.png  style="width:300px;"> 
*Le proprietà dei Dati di un [Part Cubo](Part_Box/it.md)*



## Tipi di proprietà 

Una proprietà è un\'informazione come un numero o una stringa di testo associata a un documento di FreeCAD o ad un oggetto del documento. Sono disponibili molti tipi di proprietà. Alcuni dei tipi più comuni sono:


{{Code|lang=text|code=
App::PropertyAngle
App::PropertyBool
App::PropertyDistance
App::PropertyFloat
App::PropertyInteger
App::PropertyLength
App::PropertyPlacement
App::PropertyString
App::PropertyVector
}}



## Proprietà Vista e Dati 

L\'Editor delle Proprietà dispone di due schede che danno accesso a due classi di proprietà:

-   Proprietà **Dati**, relative ai parametri \"fisici\" dell\'oggetto. Le proprietà **Dati** definiscono le caratteristiche essenziali dell\'oggetto. Esistono sempre, anche quando FreeCAD viene utilizzato in modalità console o come libreria. Ciò significa che se si carica un documento in modalità console, è possibile modificare il raggio di un cerchio o la lunghezza di una linea, anche se non si può vedere il risultato sullo schermo.
-   Proprietà **Vista**, relative all\'aspetto \"visivo\" dell\'oggetto. Le proprietà **Vista** sono legate all\'`ViewObject` dell\'oggetto e sono accessibili solo quando l\'interfaccia utente grafica (GUI) è caricata. Non sono accessibili quando si utilizza FreeCAD in modalità console o come libreria headless. Per impostazione predefinita, le modifiche alle proprietà della vista non vengono aggiunte allo stack di annullamento e non possono essere annullate e ripetute con [Annulla](Std_Undo/it.md) e [Ripristina](Std_Redo/it.md). Ma è possibile cambiare questo comportamento impostando il parametro [fine-tuning](Fine-tuning/it.md) **AutoTransactionView** su `True`.



## Proprietà di base 

Oggetti diversi possono avere proprietà diverse. Tuttavia, molti oggetti hanno le stesse proprietà perché derivano dalla stessa classe interna.

La maggior parte degli oggetti geometrici che possono essere creati e visualizzati nella [Vista 3D](3D_view/it.md) sono derivati da una `Part::Feature`. Vedere [Part Feature](Part_Feature/it.md) per le proprietà più basilari di questi oggetti.

Per la geometria 2D, la maggior parte degli oggetti deriva da un `Part::Part2DObject` (essi stessi derivati da un `Part::Feature`) che sono la base di [Schizzi](Sketch/it.md), e di molti elementi di [Draft](Draft_Workbench/it.md). Vedere [Part Part2DObject](Part_Part2DObject/it.md) per le proprietà più basilari di questi oggetti.



## Menù contestuale 

Per visualizzare il menu contestuale dell\'Editor delle Proprietà, fare clic con il pulsante destro del mouse sullo sfondo dell\'editor oppure fare clic con il pulsante destro del mouse su una proprietà.

Facendo clic con il pulsante destro del mouse sullo sfondo vengono visualizzate tre opzioni:

-    **Aggiungi proprietà**: aggiunge una proprietà dinamica all\'oggetto.

-    **Mostra nascoste**: se attivo, le proprietà nascoste dei dati e della vista vengono mostrate nell\'editor.

-    **Espansione automatica**: se attivo, tutti i nodi nell\'editor vengono espansi quando viene selezionato un oggetto.

Facendo clic con il pulsante destro del mouse su una proprietà sono disponibili le seguenti opzioni aggiuntive:

-    **Rinomina gruppo di proprietà**: rinomina il gruppo di proprietà delle proprietà selezionate. Disponibile solo per le proprietà dinamiche. Le proprietà dinamiche sono quelle aggiunte dall\'utente, così come quelle aggiunte tramite il codice Python.

-    **Rimuovi proprietà**: rimuove le proprietà selezionate. Disponibile solo per le proprietà dinamiche.

-    **Espressione...**: richiama l\'Editor delle Espressioni, che consente di utilizzare [espressioni](Expressions/it.md) nel valore della proprietà.

-    **Stato**:

:   Se un valore di stato è seguito da un asterisco (*****) è statico e non può essere modificato.

  - **Hidden**: se attivo, imposta la proprietà come nascosta, ovvero verrà visualizzata nell\'Editor delle Proprietà solo se **Mostra nascosto** è attivo.

  - **Output**: se attivo, imposta la proprietà come output.

  - **NoRecompute**: se attivo, la modifica della proprietà non tocca il suo contenitore per il ricalcolo.

  - **ReadOnly**: se attivo, imposta la proprietà come di sola lettura. La proprietà non sarà modificabile nell\'Editor delle Proprietà e l\'opzione **Expression...** non sarà più disponibile. Potrebbe tuttavia essere ancora possibile modificare la proprietà tramite una finestra di dialogo.

  - **Transient**: se attivo, imposta la proprietà come temporanea. Il valore di una proprietà temporanea non viene salvato nel file. Quando si apre un file, viene istanziata con il suo valore predefinito.

  - **Touched**: se attivo, l\'oggetto diventa toccato e pronto per il ricalcolo.

  - **EvalOnRestore**: se attivo, la proprietà viene valutata al ripristino del documento.

  - **CopyOnChange**: se attivo, la proprietà viene copiata quando modificata in un Link. Affinché funzioni, la proprietà **Link Copy on Change** del collegamento deve essere impostata su {{Value|Tracking}} o {{Value|Enabled}}. Questo è correlato a [Variant Links](https://forum.freecad.org/viewtopic.php?p=738833#p738833).

## Scripting

Vedere [Proprietà personalizzate FeaturePython](FeaturePython_Custom_Properties/it.md).



## Preferenze

Vedere [Vista combinata](Combo_view/it#Preferenze.md).





{{Interface_navi

}} {{Std_Base_navi}}



---
⏵ [documentation index](../README.md) > Property editor/it
