# Mouse navigation/it
{{docnav/it
|[Per iniziare](Getting_started/it.md)
|[Metodi di selezione](Selection_methods/it.md)
}}


{{TOCright}}

## Panoramica

La funzione **Navigare col mouse** di FreeCAD comprende i comandi utilizzati per navigare visivamente lo spazio 3D e per interagire con gli oggetti visualizzati. FreeCAD offre diversi stili di navigazione con il mouse. Lo stile di navigazione predefinito, denominato [\"Navigazione CAD​​\"](#Navigazione_CAD.md), è molto semplice e pratico, ma FreeCAD fornisce anche diversi stili di navigazione alternativi tra cui puoi scegliere. Lo stile selezionato sarà utilizzato per tutti gli ambienti di lavoro.

Per ulteriori informazione riguardo la selezione degli oggetti vedere [modi di selezione](Selection_methods/it.md)

Per ulteriori informazioni riguardo la manipolazione degli oggetti vedere [Std TransformManip](Std_TransformManip/it.md)

## Selezionare uno stile di navigazione 

1.  Effettuare una delle seguenti operazioni:
    -   Premere il bottone **[<img src=images/NavigationCAD_dark.svg style="width:16px">** sulla [barra di stato](Status_bar/it.md).
    -   Cliccare su un area vuota della [vista 3D](3D_view/it.md), e selezionare **Stile di navigazione** dal menu contestuale.
    -   Utilizzare l\'[Editor delle preferenze](Preferences_Editor/it#Navigation.md). Dal menu selezionare **Modifica → Preferenze** e poi **Visualizzazione → Navigazione → Navigazione 3D**.
2.  Seleziona uno stile dalla lista.
3.  Facoltativamente cambiare lo **Stile Orbita**: premere il bottone **[<img src=images/NavigationCAD_dark.svg style="width:16px">** sulla [barra di Stato](Status_bar/it.md) e poi scegliere **Impostazioni → Stile Orbita**. Vedere l\'[Editor delle Preferenze](Preferences_Editor/it#Navigazione.md).

## Stili di navigazione disponibili 

### Navigazione Blender 

La navigazione Blender si basa sul modello [Blender](https://www.blender.org).


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

### Navigazione CAD 

Questo è lo stile di navigazione predefinito. Consente all\'utente un semplice controllo della vista, e non richiede l\'uso dei tasti della tastiera se non per effettuare selezioni multiple.


{{CAD Navigation
|Select_name=Selezione
|Pan_name=Traslazione
|Zoom_name=Zoom
|Rotate_view_name=Rotazione vista<br>Primo metodo
|Rotate_view_alt_name=Rotazione vista<br>Metodo alternativo
|Ctrl=**Ctrl**
|Shift=**Shift**
|Select_text=Premere il tasto sinistro del mouse su un oggetto che si desidera selezionare.

Tenere premuto **Ctrl** per selezionare più oggetti.
|Pan_text=Tenere premuto il pulsante centrale del mouse, quindi spostare il puntatore.
|Pan_mode_text=Modalità Traslazione: tenere premuto il tasto **Ctrl**, premere il tasto destro del mouse una volta, quindi muovere il puntatore.
|Zoom_text=Usare la rotellina del mouse per zoommare avanti e indietro.

Facendo clic sul pulsante centrale del mouse, la vista viene nuovamente centrata sulla posizione del cursore.
|Zoom_mode_text=Modalità zoom: tenere premuti i tasti **Ctrl** e **Shift**, premere il pulsante destro del mouse una volta, quindi spostare il puntatore.
|Rotate_view_text=Tenere premuto il pulsante centrale del mouse, quindi premere e tenere premuto il pulsante sinistro del mouse, quindi spostare il puntatore.

Se i pulsanti vengono rilasciati prima di interrompere il movimento del mouse, la visualizzazione continua la [rotazione](spinning/it.md), se l'azione è abilitata.

Un doppio clic con il pulsante centrale del mouse imposta un nuovo centro di rotazione.
|Rotate_view_mode_text=Modalità rotazione: tenere premuto il tasto **Shift**, premere il tasto destro del mouse una volta, quindi spostare il puntatore.
|Rotate_view_alt_text=Tenere premuto il pulsante centrale del mouse, e tenere premuto il pulsante destro del mouse, quindi spostare il puntatore.

Con questo metodo il pulsante centrale del mouse può essere rilasciato dopo aver tenuto premuto il pulsante destro del mouse.

Gli utenti che utilizzano il mouse con la mano destra potrebbero trovare questo metodo più semplice del primo metodo.
}}

### Navigazione Gesture 

Questo stile è stato pensato per l\'uso con un touchscreen e una penna. Tuttavia, può essere utilizzato anche con un mouse ed è consigliato quando si utilizza un Mac con trackpad.


{{Gesture Navigation
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

Nella navigazione Maya-Gesture, lo spostamento, lo zoom e la rotazione della vista richiedono il tasto **Alt** insieme a un pulsante del mouse; pertanto, è necessario un mouse a tre pulsanti. È anche possibile utilizzare le gesture poiché questo stile è stato sviluppato sullo stile della [Navigazione Gesture](#Navigazione_Gesture.md).


{{MayaGesture Navigation
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

### Navigazione OpenCascade 

La navigazione OpenCascade si basa sul modello [OpenCascade](https://www.opencascade.com/).


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

### Navigazione OpenInventor 

La Navigazione OpenInventor (formalmente Inventor) si basa sul modello [Open Inventor](http://en.wikipedia.org/wiki/Open_Inventor). Per selezionare gli oggetti, è necessario tenere premuto il tasto **Shift** o **Ctrl**.

Questo stile non è basato su Autodesk Inventor.


{{OpenInventor Navigation
|Select_name=Selezione
|Pan_name=Traslazione
|Zoom_name=Zoom
|Rotate_view_name=Rotazione vista
|Shift=**Shift**
|Select_text=Tenere premuto **Shift**, quindi premere il tasto sinistro del mouse sopra un oggetto che si desidera selezionare.

Invece tenere premuto **Ctrl** per selezionare più oggetti.
|Pan_text=Tenere premuto il pulsante centrale del mouse, quindi spostare il puntatore.
|Zoom_text=Usare la rotellina del mouse per ingrandire e rimpicciolire.

In alternativa, tenere premuto il pulsante centrale del mouse, quindi premere e tenere premuto il pulsante sinistro del mouse, quindi spostare il puntatore. 
|Rotate_view_text=Tenere premuto il pulsante sinistro del mouse, quindi spostare il puntatore.
}}

### Navigazione OpenSCAD 

La Navigazione OpenSCAD si basa sul modello [OpenSCAD](https://openscad.org/).


{{Version/it|0.20}}


{{OpenSCAD_Navigation
|Select_name=Selezione
|Pan_name=Traslazione
|Zoom_name=Zoom
|Rotate_view_name=Rotazione vista
|Shift=**Shift**
|Select_text=Premere il pulsante sinistro del mouse su un oggetto che si desidera selezionare.
|Pan_text=Tenere premuto il tasto destro del mouse, quindi spostare il puntatore.
|Zoom_text=Tenere premuto il pulsante centrale del mouse, quindi spostare il puntatore. In alternativa, tenere premuto **Shift** e il pulsante destro del mouse, quindi spostare il puntatore.
|Rotate_view_text=Tenere premuto il pulsante sinistro del mouse, quindi spostare il puntatore.
}}

### Navigazione Revit 

La Navigazione Revit si basa sul modello [Revit](https://en.wikipedia.org/wiki/Autodesk_Revit).


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

### Navigazione TinkerCAD 

La Navigazione TinkerCAD si basa sul modello [TinkerCAD](https://en.wikipedia.org/wiki/Tinkercad).


{{Version/it|0.20}}


{{TinkerCAD Navigation
|Select_name=Selezione
|Pan_name=Traslazione
|Zoom_name=Zoom
|Rotate_view_name=Rotazione vista
|Select_text=Premre il pulsante sinistro del mouse su un oggetto che si desidera selezionare.
|Pan_text=Tenere premuto il pulsante centrale del mouse, quindi spostare il puntatore.
|Zoom_text=Usare la rotellina del mouse per zoommare avanti e indietro.
|Rotate_view_text=Premere il tasto destro del mouse, quindi spostare il puntatore.
}}

### Navigazione Touchpad 

Nella Navigazione touchpad, lo spostamento, lo zoom e la rotazione della vista richiedono un tasto modificatore insieme al touchpad.


{{Touchpad Navigation
|Select_name=Selezione
|Pan_name=Traslazione
|Zoom_name=Zoom
|Rotate_view_name=Rotazione vista Ctrl=**Ctrl**
|Shift=**Shift**
|Alt=**Alt**
|PageUp=**PagSù**
|PageDown=**PagGiù**
|Select_text=Premere il tasto sinistro del mouse su un oggetto che si desidera selezionare.
|Pan_text=Premere **Shift**, quindi spostare il puntatore.
|Zoom_text=Usare **PagSù** e **PagGiù** per ingrandire e ridurre.
|Zoom_alt_text=In alternativa, tenere premuto **Ctrl** e **Shift**, quindi spostare il puntatore.
|Rotate_view_text=Tenere premuto **Alt**, quindi spostare il puntatore.
|Rotate_view_alt_text=In alternativa, tenere premuto **Shift** e il pulsante sinistro, quindi spostare il puntatore.
}}

## Supporto Hardware 

FreeCAD supporta anche i [dispositivi di input 3D](3D_input_devices/it.md).

## Navigazione consigliata per macOS 

Sui MacBook con trackpad la navigazione gestuale funziona molto bene, ma i gesti hanno un significato speciale:

-   Zoom: trascina con due dita.
-   Ruota: trascina con tre dita.
-   Panoramica: **Ctrl** + tre dita.

## Sviluppo di una navigazione personalizzata 

Il tutorial [Aggiunta di una nuova opzione di navigazione del mouse a FreeCAD](Adding_a_new_mouse_navigation_option_to_FreeCAD/it.md) orienta gli sviluppatori che desiderano sviluppare un\'opzione di navigazione del mouse personalizzata. È richiesta la familiarità con la sintassi C++.


{{docnav/it
|[Per iniziare](Getting_started/it.md)
|[Metodi di selezione](Selection_methods/it.md)
}}



---
![](images/Right_arrow.png) [documentation index](../README.md) > Mouse navigation/it
