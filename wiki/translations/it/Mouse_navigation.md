# Mouse navigation/it
{{docnav/it
|[Per iniziare](Getting_started/it.md)
|[Metodi di selezione](Selection_methods/it.md)
}}


{{TOCright}}

## Panoramica


<div class="mw-translate-fuzzy">

La funzione **Navigare col mouse** di FreeCAD comprende i comandi utilizzati per navigare visivamente lo spazio 3D e per interagire con gli oggetti visualizzati. FreeCAD offre diversi stili di navigazione con il mouse. Lo stile di navigazione predefinito, denominato \"Navigazione CAD​​\", è molto semplice e pratico, ma FreeCAD fornisce anche stili di navigazione alternativi che puoi scegliere in base alle tue preferenze.


</div>

For more information about selecting objects see [Selection methods](Selection_methods.md).

For more information about manipulating objects see [Std TransformManip](Std_TransformManip.md).


<div class="mw-translate-fuzzy">

## Navigare


</div>


<div class="mw-translate-fuzzy">

-   In [Preferenze](Preferences_Editor/it#Navigazione.md), **Modifica → Preferenze → Visualizzazione → Navigazione 3D**.
-   Cliccare col tasto destro nello spazio vuoto dell\'area della vista 3D, quindi selezionare **Stile di navigazione** nel menu contestuale.


</div>

## Available navigation styles 

### Navigazione Blender 

The Blender navigation style was modeled after [Blender](https://www.blender.org).


<div class="mw-translate-fuzzy">

Lo stile di navigazione Blender segue il modello di [Blender](https://www.blender.org). In precedenza non c\'era la traslazione con il solo mouse, ed era richiesto l\'uso del tasto **Shift** per spostare la vista. Questo è cambiato nel 2016 con l\'introduzione di una funzione aggiuntiva. Per eseguire una panoramica della vista, ora è possibile premere i pulsanti sinistro e destro del mouse per spostare la vista.


{{Blender Navigation/it
|Select_name=Selezione
|Pan_name=Traslazione
|Zoom_name=Zoom
|Rotate_view_name=Rotazione vista
|Shift=**Shift**
|Select_text=Premere il tasto sinistro del mouse su un oggetto che si desidera selezionare.
|Pan_text=Tenere premuto **Shift** e il pulsante centrale del mouse, quindi spostare il puntatore.
</div>

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

<div class="mw-translate-fuzzy">
Tenendo premuto **Ctrl** consente la selezione di più oggetti.
|Pan_text=Tenere premuto il pulsante centrale del mouse, quindi spostare il puntatore.
|Pan_mode_text=Modalità Traslazione: tenere premuto il tasto **Ctrl**, preme il tasto destro del mouse una volta, quindi muovere il puntatore. {{Version/it|0.17}}
|Zoom_text=Usare la rotellina del mouse per zoommare avanti e indietro.
</div>

<div class="mw-translate-fuzzy">
Facendo clic sul pulsante centrale del mouse, la vista viene nuovamente centrata sulla posizione del cursore.
|Zoom_mode_text=Modalità zoom: tenere premuti i tasti **Ctrl** e **Shift**, premere il pulsante destro del mouse una volta, quindi spostare il puntatore. {{Version/it|0.17}}
|Rotate_view_text=Tenere premuto il pulsante centrale del mouse, quindi premere e tenere premuto il pulsante sinistro del mouse, quindi spostare il puntatore.
</div>

<div class="mw-translate-fuzzy">
La posizione del cursore quando viene premuto il pulsante centrale del mouse determina il centro di rotazione. La rotazione funziona come una palla che ruota attorno al suo centro. Se i pulsanti vengono rilasciati prima di interrompere il movimento del mouse, la visualizzazione continua la [rotazione](spinning/it.md), se l'azione è abilitata.
</div>

<div class="mw-translate-fuzzy">
Un doppio clic con il pulsante centrale del mouse imposta un nuovo centro di rotazione.
|Rotate_view_mode_text=Modalità rotazione: tenere premuto il tasto **Shift**, premere il tasto destro del mouse una volta, quindi spostare il puntatore. {{Version/it|0.17}}
|Rotate_view_alt_text=Tenere premuto il pulsante centrale del mouse, e tenere premuto il pulsante destro del mouse, quindi spostare il puntatore.
</div>

Con questo metodo il pulsante centrale del mouse può essere rilasciato dopo aver tenuto premuto il pulsante destro del mouse.

Gli utenti che utilizzano il mouse con la mano destra potrebbero trovare questo metodo più semplice del primo metodo.
}}

### Navigazione Gesture 

This style was tailored for use with a touchscreen and pen. Nevertheless, it can also be used with a mouse, and is recommended for use when using a Mac with a trackpad.


<div class="mw-translate-fuzzy">

Questo stile di navigazione è stato introdotto nella versione 0.16, è fatto su misura per essere usato con il touchscreen o con la penna, ma è usabile anche con il mouse ed è consigliato per l\'uso quando si utilizza un Mac con un trackpad. {{Gesture Navigation
|Select_name=Selezione
|Pan_name=Traslazione
|Zoom_name=Zoom
|Rotate_view_name=Rotazione vista
|Tilt_view_name=Inclinazione vista
|Select_text=Premere il tasto sinistro del mouse su un oggetto che si desidera selezionare.
|Select_gesture_text=Toccare per selezionare.
|Pan_text=Tenere premuto il tasto destro del mouse, quindi spostare il puntatore.
|Pan_gesture_text=Trascinare con due dita.
</div>

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

In Maya-Gesture Navigation, panning, zooming, and rotating the view require the **Alt** key together with a mouse button; therefore, a three-button mouse is required. It\'s also possible to use gestures as this mode was developed over the [Gesture navigation](#Gesture_navigation.md) mode.


<div class="mw-translate-fuzzy">

Nella navigazione Maya-Gesture, traslazione, zoom e rotazione della vista richiedono il tasto **Alt** insieme al pulsante del mouse; pertanto, è richiesto un mouse a tre pulsanti. È anche possibile usare i gesti poiché questa modalità è stata sviluppata sulla modalità [Navigazione Gesture](#Navigazione_Gesture.md). {{MayaGesture Navigation
|Select_name=Selezione
|Pan_name=Traslazione
|Zoom_name=Zoom
|Rotate_view_name=Rotazione vista
|Alt=**Alt**
|Select_text=Premere il tasto sinistro del mouse su un oggetto che si desidera selezionare.
|Pan_text=Tenere premuto **Alt** e il pulsante centrale del mouse, quindi spostare il puntatore.
|Zoom_text=Tenere premuto **Alt** e il tasto destro del mouse, quindi spostare il puntatore.
</div>

In alternativa, utilizzare la rotellina del mouse per ingrandire e ridurre.
|Rotate_view_text=Tenere premuto **Alt** e il tasto sinistro del mouse, quindi spostare il puntatore.
}}

### Navigazione OpenCascade 

The OpenCascade navigation style was modeled after [OpenCascade](https://www.opencascade.com/).


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

### OpenSCAD navigation 

The OpenSCAD navigation style was modeled after [OpenSCAD](https://openscad.org/).


<small>(v0.20)</small> 


{{OpenSCAD_Navigation
|Select_name=Select
|Pan_name=Pan
|Zoom_name=Zoom
|Rotate_view_name=Rotate view
|Shift=**Shift**
|Select_text=Press the left mouse button over an object you want to select.
|Pan_text=Hold the right mouse button, then move the pointer.
|Zoom_text=Hold the middle mouse button, then move the pointer.
Alternatively, hold **Shift** and the right mouse button, then move the pointer.
|Rotate_view_text=Hold the left mouse button, then move the pointer.
}}

### Navigazione Revit 

The Revit navigation style was modeled after [Revit](https://en.wikipedia.org/wiki/Autodesk_Revit).


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

### TinkerCAD navigation 

The TinkerCAD navigation style was modeled after [TinkerCAD](https://en.wikipedia.org/wiki/Tinkercad).


<small>(v0.20)</small> 


{{TinkerCAD Navigation
|Select_name=Select
|Pan_name=Pan
|Zoom_name=Zoom
|Rotate_view_name=Rotate view
|Select_text=Press the left mouse button over an object you want to select.
|Pan_text=Hold the middle mouse button, then move the pointer.
|Zoom_text=Use the mouse wheel to zoom in and out.
|Rotate_view_text=Press the right mouse button, then move the pointer.
}}

### Navigazione Touchpad 

In Touchpad Navigation, panning, zooming, and rotating the view require a modifier key together with the touchpad.


<div class="mw-translate-fuzzy">

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


</div>

## Supporto Hardware 


<div class="mw-translate-fuzzy">

FreeCAD supporta anche i [dispositivi di input 3D](3D_input_devices/it.md).


</div>

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
