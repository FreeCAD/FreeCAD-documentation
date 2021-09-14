# Mouse navigation/it




{{docnav/it
|[Per iniziare](Getting_started/it.md)
|[Metodi di selezione](Selection_methods/it.md)
}}


{{TOCright}}

## Introduzione

La funzione **Navigare col mouse** di FreeCAD comprende i comandi utilizzati per navigare visivamente lo spazio 3D e per interagire con gli oggetti visualizzati. Attualmente FreeCAD offre diversi stili di navigazione con il mouse. Lo stile di navigazione predefinito, denominato \"Navigazione CAD​​\", è molto semplice e pratico, ma si può anche usare uno stile alternativo, secondo le proprie preferenze.

## Navigazione

I gesti del mouse utilizzati per la manipolazione dell\'oggetto variano in base allo stile di navigazione selezionato; lo stile attivo, attualmente selezionato, viene utilizzato in tutti gli ambienti.

Ci sono due modi per modificare lo stile di navigazione:

-   In [Preferenze](Preferences_Editor/it#Navigazione.md), **Modifica → Preferenze → Visualizzazione → Navigazione 3D**.
-   Cliccare col tasto destro nello spazio vuoto dell\'area della vista 3D, quindi selezionare **Stile di navigazione** nel menu contestuale.

### Navigazione CAD 

Questo è lo stile di navigazione predefinito. Permette all\'utente un semplice controllo della vista. Richiede l\'uso della tastiera solo per eseguire multi-selezioni.


{{CAD Navigation
|Select_name=Selezione
|Pan_name=Traslazione
|Zoom_name=Zoom
|Rotate_view_name=Rotazione vista<br>Primo metodo
|Rotate_view_alt_name=Rotazione vista<br>Metodo alternativo
|Ctrl=**Ctrl**
|Shift=**Shift**
|Select_text=Premere il tasto sinistro del mouse su un oggetto che si desidera selezionare.

Tenendo premuto **Ctrl** consente la selezione di più oggetti.
|Pan_text=Tenere premuto il pulsante centrale del mouse, quindi spostare il puntatore.
|Pan_mode_text=Modalità Traslazione: tenere premuto il tasto **Ctrl**, preme il tasto destro del mouse una volta, quindi muovere il puntatore. {{Version/it|0.17}}
|Zoom_text=Usare la rotellina del mouse per zoommare avanti e indietro.

Facendo clic sul pulsante centrale del mouse, la vista viene nuovamente centrata sulla posizione del cursore.
|Zoom_mode_text=Modalità zoom: tenere premuti i tasti **Ctrl** e **Shift**, premere il pulsante destro del mouse una volta, quindi spostare il puntatore. {{Version/it|0.17}}
|Rotate_view_text=Tenere premuto il pulsante centrale del mouse, quindi premere e tenere premuto il pulsante sinistro del mouse, quindi spostare il puntatore.

La posizione del cursore quando viene premuto il pulsante centrale del mouse determina il centro di rotazione. La rotazione funziona come una palla che ruota attorno al suo centro. Se i pulsanti vengono rilasciati prima di interrompere il movimento del mouse, la visualizzazione continua la [rotazione](spinning/it.md), se l'azione è abilitata.

Un doppio clic con il pulsante centrale del mouse imposta un nuovo centro di rotazione.
|Rotate_view_mode_text=Modalità rotazione: tenere premuto il tasto **Shift**, premere il tasto destro del mouse una volta, quindi spostare il puntatore. {{Version/it|0.17}}
|Rotate_view_alt_text=Tenere premuto il pulsante centrale del mouse, e tenere premuto il pulsante destro del mouse, quindi spostare il puntatore.

Con questo metodo il pulsante centrale del mouse può essere rilasciato dopo aver tenuto premuto il pulsante destro del mouse.

Gli utenti che utilizzano il mouse con la mano destra potrebbero trovare questo metodo più semplice del primo metodo.
}}

### Navigazione OpenInventor 

La Navigazione OpenInventor (formalmente Inventor), si basa sul modello [Open Inventor](http://en.wikipedia.org/wiki/Open_Inventor). Per selezionare gli oggetti, è necessario tenere premuto il tasto **Ctrl**.

Questa modalità non è basata su Autodesk Inventor.


{{OpenInventor Navigation
|Select_name=Selezione
|Pan_name=Traslazione
|Zoom_name=Zoom
|Rotate_view_name=Rotazione vista
|Ctrl=**Ctrl**
|Select_text=Tenere premuto **Ctrl**, quindi premere il tasto sinistro del mouse sopra un oggetto che si desidera selezionare.
|Pan_text=Tenere premuto il pulsante centrale del mouse, quindi spostare il puntatore.
|Zoom_text=Usare la rotellina del mouse per zoommare avanti e indietro.

In alternativa, tenere premuto il pulsante centrale del mouse, quindi premere e tenere premuto il pulsante sinistro del mouse, quindi spostare il puntatore. 
|Rotate_view_text=Tenere premuto il pulsante sinistro del mouse, quindi spostare il puntatore.
}}

### Navigazione Blender 

Lo stile di navigazione Blender segue il modello di [Blender](https://www.blender.org). In precedenza non c\'era la traslazione con il solo mouse, ed era richiesto l\'uso del tasto **Shift** per spostare la vista. Questo è cambiato nel 2016 con l\'introduzione di una funzione aggiuntiva. Per eseguire una panoramica della vista, ora è possibile premere i pulsanti sinistro e destro del mouse per spostare la vista.


{{Blender Navigation/it
|Select_name=Selezione
|Pan_name=Traslazione
|Zoom_name=Zoom
|Rotate_view_name=Rotazione vista
|Shift=**Shift**
|Select_text=Premere il tasto sinistro del mouse su un oggetto che si desidera selezionare.
|Pan_text=Tenere premuto **Shift** e il pulsante centrale del mouse, quindi spostare il puntatore.

In alternativa, tenere premuti i pulsanti sinistro e destro del mouse, quindi spostare il puntatore.
|Zoom_text=Usare la rotellina del mouse per zoommare avanti e indietro.
|Rotate_view_text=Tenere premuto il pulsante centrale del mouse, quindi spostare il puntatore.
}}

### Navigazione Touchpad 

Nella navigazione Touchpad, traslazione, zoom e rotazione della vista richiedono un tasto modificatore insieme al touchpad. {{Touchpad Navigation
|Select_name=Selezione
|Pan_name=Traslazione
|Zoom_name=Zoom
|Rotate_view_name=Rotazione vista
|Shift=**Shift**
|Ctrl=**Ctrl**
|Alt=**Alt**
|PageUp=**PagSù**
|PageDown=**PagGiù**
|Select_text=Premere il tasto sinistro del mouse su un oggetto che si desidera selezionare.
|Pan_text=Hold **Shift**, quindi spostare il puntatore.
|Zoom_text=Use **PagSù** e **PagGiù** per ingrandire e ridurre.
|Zoom_alt_text=In alternativa, tenere premuto **Shift** e **Ctrl**, quindi spostare il puntatore.
|Rotate_view_text=Tenere premuto **Alt**, quindi spostare il puntatore.
|Rotate_view_alt_text=In alternativa, tenere premuto **Shift** e il pulsante sinistro, quindi spostare il puntatore.
}}

### Navigazione Gesture 

Questo stile di navigazione è stato introdotto nella versione 0.16, è fatto su misura per essere usato con il touchscreen o con la penna, ma è usabile anche con il mouse. {{Gesture Navigation
|Select_name=Selezione
|Pan_name=Traslazione
|Zoom_name=Zoom
|Rotate_view_name=Rotazione vista
|Tilt_view_name=Inclinazione vista
|Select_text=Premere il tasto sinistro del mouse su un oggetto che si desidera selezionare.
|Select_gesture_text=Toccare per selezionare.
|Pan_text=Tenere premuto il tasto destro del mouse, quindi spostare il puntatore.
|Pan_gesture_text=Trascinare con due dita.

In alternativa, toccare e tenere premuto, quindi trascinare. Questo simula la traslazione con il tasto destro del mouse.
|Zoom_text=Usare la rotellina del mouse per zoommare avanti e indietro.
|Zoom_gesture_text=Trascinare due dita (pizzicare) più vicino o più lontano.
|Rotate_view_text=Tenere premuto il pulsante sinistro del mouse, quindi spostare il puntatore.
In [Sketcher](Sketcher_Workbench/it.md) e altre modalità di modifica, questo comportamento è disabilitato. Tenere premuto **Alt** quando si preme il pulsante del mouse per accedere alla modalità di rotazione.

Per impostare il punto di messa a fuoco della fotocamera per la rotazione, fare clic su un punto con il pulsante centrale del mouse. In alternativa, puntare il cursore su un punto e premere **H** sulla tastiera.
|Rotate_view_gesture_text=Trascinare con un dito per ruotare.

Tenere premuto **Alt** quando ci si trova in [Sketcher](Sketcher_Workbench/it.md).
|Tilt_view_text=Tenere premuti i pulsanti sinistro e destro del mouse, quindi spostare il puntatore di lato. 
|Tilt_view_gesture_text=Ruota la linea immaginaria formata da due punti di contatto.

In v0.18 questo metodo è disabilitato per impostazione predefinita. Per abilitarlo, andare in ** Modifica → Preferenze → Visualizzazione** e deselezionare la casella di controllo "Disabilita l'inclinazione touchscreen".
}}

### Navigazione Maya-Gesture 

Nella navigazione Maya-Gesture, traslazione, zoom e rotazione della vista richiedono il tasto **Alt** insieme al pulsante del mouse; pertanto, è richiesto un mouse a tre pulsanti. È anche possibile usare i gesti poiché questa modalità è stata sviluppata sulla modalità [Navigazione Gesture](#Navigazione_Gesture.md). {{MayaGesture Navigation
|Select_name=Selezione
|Pan_name=Traslazione
|Zoom_name=Zoom
|Rotate_view_name=Rotazione vista
|Alt=**Alt**
|Select_text=Premere il tasto sinistro del mouse su un oggetto che si desidera selezionare.
|Pan_text=Tenere premuto **Alt** e il pulsante centrale del mouse, quindi spostare il puntatore.
|Zoom_text=Tenere premuto **Alt** e il tasto destro del mouse, quindi spostare il puntatore.

In alternativa, utilizzare la rotellina del mouse per ingrandire e ridurre.
|Rotate_view_text=Tenere premuto **Alt** e il tasto sinistro del mouse, quindi spostare il puntatore.
}}

### Navigazione Revit 

Questo stile è stato introdotto nella versione 0.18.


{{Revit Navigation
|Select_name=Selezione
|Pan_name=Traslazione
|Zoom_name=Zoom
|Rotate_view_name=Rotazione vista
|Shift=**Shift**
|Select_text=Premere il tasto sinistro del mouse su un oggetto che si desidera selezionare.
|Pan_text=Tenere premuto il pulsante centrale del mouse, quindi spostare il puntatore.

In alternativa, tenere premuti i pulsanti sinistro e destro del mouse, quindi spostare il puntatore.

|Zoom_text=Usa la rotellina del mouse per zoommare avanti e indietro.
|Rotate_view_text=Tenere premuto **Shift** e il pulsante centrale del mouse, quindi spostare il puntatore.

In alternativa, tenere premuto il pulsante centrale del mouse, e tenere premuto il pulsante destro del mouse, quindi spostare il puntatore.
}}

### OpenCascade

Questo stile è stato introdotto nella versione 0.18.


{{OpenCascade Navigation
|Select_name=Selezione
|Pan_name=Traslazione
|Zoom_name=Zoom
|Rotate_view_name=Rotazione vista
|Ctrl=**Ctrl**
|Select_text=Premere il tasto sinistro del mouse su un oggetto che si desidera selezionare.
|Pan_text=Tenere premuto il pulsante centrale del mouse, quindi spostare il puntatore.
|Zoom_text=Usare la rotellina del mouse per zoommare avanti e indietro.

In alternativa, tenere premuto **Ctrl** e il tasto sinistro del mouse, quindi spostare il puntatore.
|Rotate_view_text=Tenere premuto **Ctrl** e il tasto destro del mouse, quindi spostare il puntatore.
}}

## La selezione degli oggetti 

### Selezione semplice 

Gli oggetti si possono selezionare con un click del tasto sinistro del mouse o facendo clic sull\'oggetto nella [vista 3D](3D_view/it.md) o selezionandoli nella [vista ad albero](tree_view/it.md).

### Preselezione

Passando con il mouse sugli oggetti, una funzione di Preselezione li evidenzia e visualizza le relative informazioni prima della loro selezione. Se questo comportamento non è gradito o si dispone di una macchina lenta, è possibile disattivare la funzione nel dialogo delle preferenze.

## La manipolazione degli oggetti 

FreeCAD offre strumenti [Manipolatori](manipulator/it.md) utilizzabili per modificare un oggetto o il suo aspetto visivo.

## Supporto Hardware 

FreeCAD supporta anche i [dispositivi di input 3D](3D_input_devices/it.md).

## Problemi con Mac OS X 

Recentemente abbiamo ricevuto segnalazioni [nel forum](http://forum.freecadweb.org/viewtopic.php?f=3&t=3592&start=0) da utenti Mac che questi pulsanti del mouse e le combinazioni di tasti non funzionano come previsto. Purtroppo, nessuno degli sviluppatori possiede un Mac e neppure gli altri collaboratori regolari. Abbiamo bisogno del vostro aiuto per determinare quali pulsanti del mouse e quali combinazioni di tasti funzionano e poter aggiornare questo wiki.


{{docnav/it
|[Per iniziare](Getting_started/it.md)
|[Metodi di selezione](Selection_methods/it.md)
}}



