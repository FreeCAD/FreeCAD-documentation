# Mouse navigation/it
{{docnav/it
|[Per iniziare](Getting_started/it.md)
|[Metodi di selezione](Selection_methods/it.md)
}}






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

Con tutti gli stili di navigazione, a meno che non si selezionino oggetti da uno schizzo in modalità di modifica, è necessario tenere premuto **Ctrl** per selezionare più oggetti.

The following keyboard options are available for all styles:

-    **Ctrl**\+ {{ASCII|43}} and **Ctrl** + {{ASCII|22}} or **PgUp** and **PgDn** to zoom in and out, respectively.

-   The arrow keys, {{ASCII|17}}{{ASCII|16}}{{ASCII|30}}{{ASCII|31}}, to pan the view left/right and up/down.

-    **Shift**\+ {{ASCII|17}} and **Shift** + {{ASCII|16}} to rotate the view by 90 degrees.



### Navigazione Blender 

La navigazione Blender si basa sul modello [Blender](https://www.blender.org).


<div class="mw-translate-fuzzy">


{{Blender Navigation/it
|Select_name=Selezione
|Pan_name=Traslazione
|Zoom_name=Zoom
|Rotate_view_name=Rotazione vista
|Shift=**Shift**
|Select_text=Premere il tasto sinistro del mouse su un oggetto che si desidera selezionare.
|Pan_text=Tenere premuto **Shift** e il pulsante centrale del mouse, quindi spostare il puntatore.
</div>

|Shift=**Shift**

|Select_text=Press the left mouse button over an object you want to select.

|Zoom_text=Use the mouse wheel to zoom in and out.

|Rotate_view_text=Hold the middle mouse button, then move the pointer.

|Pan_text=Hold **Shift** and the middle mouse button, then move the pointer.

Alternatively, hold both left and right mouse buttons, and then move the pointer.
}}



### Navigazione CAD 

Questo è lo stile di navigazione predefinito. Consente all\'utente un semplice controllo della vista, e non richiede l\'uso dei tasti della tastiera se non per effettuare selezioni multiple.


<div class="mw-translate-fuzzy">


{{CAD Navigation
|Select_name=Selezione
|Pan_name=Traslazione
|Zoom_name=Zoom
|Rotate_view_name=Rotazione vista<br>Primo metodo
|Rotate_view_alt_name=Rotazione vista<br>Metodo alternativo
|Ctrl=**Ctrl**
|Shift=**Shift**
|Select_text=Premere il tasto sinistro del mouse su un oggetto che si desidera selezionare.
|Pan_text=Tenere premuto il pulsante centrale del mouse, quindi sposta il puntatore.
|Pan_mode_text=Modalità Pan: tenere premuto il tasto **Ctrl**, premere una volta il pulsante destro del mouse, quindi spostare il puntatore.
|Zoom_text=Utilizzare la rotellina del mouse per ingrandire e rimpicciolire.
</div>

|Ctrl=**Ctrl**
|Shift=**Shift**

|Select_text=Press the left mouse button over an object you want to select.

|Zoom_text=Use the mouse wheel to zoom in and out.

Clicking the middle mouse button re-centers the view on the location of the cursor.

|Rotate_view_text=Hold the middle mouse button, then press and hold the left mouse button, then move the pointer.

Se i pulsanti vengono rilasciati prima di interrompere il movimento del mouse, la visualizzazione continua la [rotazione](spinning/it.md), se l'azione è abilitata.

<div class="mw-translate-fuzzy">
Un doppio clic con il pulsante centrale del mouse imposta un nuovo centro di rotazione.
|Rotate_view_mode_text=Modalità rotazione: tenere premuto il tasto **Shift**, premere il tasto destro del mouse una volta, quindi spostare il puntatore.
|Rotate_view_alt_text=Tenere premuto il pulsante centrale del mouse, e tenere premuto il pulsante destro del mouse, quindi spostare il puntatore.
</div>

|Rotate_view_alt_text=Hold the middle mouse button, then press and hold the right mouse button, then move the pointer.

Con questo metodo il pulsante centrale del mouse può essere rilasciato dopo aver tenuto premuto il pulsante destro del mouse.

<div class="mw-translate-fuzzy">
Gli utenti che utilizzano il mouse con la mano destra potrebbero trovare questo metodo più semplice del primo metodo.
}}


</div>

\|Pan_text=Hold the middle mouse button, then move the pointer.

\|Zoom_mode_text=Zoom mode: hold the **Ctrl** and **Shift** keys, press the right mouse button once, then move the pointer.

\|Rotate_view_mode_text=Rotate mode: hold the **Shift** key, press the right mouse button once, then move the pointer.

\|Pan_mode_text=Pan mode: hold the **Ctrl** key, press the right mouse button once, then move the pointer. }}



### Navigazione Gesture 

Questo stile è stato pensato per l\'uso con un touchscreen e una penna. Tuttavia, può essere utilizzato anche con un mouse ed è consigliato quando si utilizza un Mac con trackpad.


<div class="mw-translate-fuzzy">


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
</div>

|Select_text=Press the left mouse button over an object you want to select.

|Zoom_text=Use the mouse wheel to zoom in and out.

|Rotate_view_text=Hold the left mouse button, then move the pointer.
In [Sketcher](Sketcher_Workbench.md) and other edit modes, this behavior is disabled. Hold **Alt** when pressing the mouse button to enter rotation mode.

<div class="mw-translate-fuzzy">
Per impostare il punto di messa a fuoco della fotocamera per la rotazione, fare clic su un punto con il pulsante centrale del mouse. In alternativa, puntare il cursore su un punto e premere **H** sulla tastiera.
|Rotate_view_gesture_text=Trascinare con un dito per ruotare.
</div>

|Pan_text=Hold the right mouse button, then move the pointer.

|Tilt_view_text=Hold both left and right mouse buttons, then move the pointer sideways.

|Select_gesture_text=Tap to select.

|Zoom_gesture_text=Drag two fingers (pinch) closer or farther apart.

|Rotate_view_gesture_text=Drag with one finger to rotate.

<div class="mw-translate-fuzzy">
Tenere premuto **Alt** quando ci si trova in [Sketcher](Sketcher_Workbench/it.md).
|Tilt_view_text=Tenere premuti i pulsanti sinistro e destro del mouse, quindi spostare il puntatore di lato. 
|Tilt_view_gesture_text=Ruota la linea immaginaria formata da due punti di contatto.
</div>

|Pan_gesture_text=Drag with two fingers.

<div class="mw-translate-fuzzy">
In alternativa, toccare e tenere premuto, quindi trascinare. Questo simula la traslazione con il tasto destro del mouse.
|Zoom_text=Usare la rotellina del mouse per zoommare avanti e indietro.
|Zoom_gesture_text=Trascinare due dita (pizzicare) più vicino o più lontano.
|Rotate_view_text=Tenere premuto il pulsante sinistro del mouse, quindi spostare il puntatore.
In [Sketcher](Sketcher_Workbench/it.md) e altre modalità di modifica, questo comportamento è disabilitato. Tenere premuto **Alt** quando si preme il pulsante del mouse per accedere alla modalità di rotazione.
</div>

|Tilt_view_gesture_text=Rotate the imaginary line formed by two touch points.

Questo metodo è disabilitato per impostazione predefinita. Per abilitarlo, andare in ** Modifica → Preferenze → Visualizzazione → Navigazione** e deselezionare la casella di controllo "Disabilita l'inclinazione touchscreen".
}}



### Navigazione Maya-Gesture 

Nella navigazione Maya-Gesture, lo spostamento, lo zoom e la rotazione della vista richiedono il tasto **Alt** insieme a un pulsante del mouse; pertanto, è necessario un mouse a tre pulsanti. È anche possibile utilizzare le gesture poiché questo stile è stato sviluppato sullo stile della [Navigazione Gesture](#Navigazione_Gesture.md).


<div class="mw-translate-fuzzy">


{{MayaGesture Navigation
|Select_name=Selezione
|Pan_name=Traslazione
|Zoom_name=Zoom
|Rotate_view_name=Rotazione vista
|Alt=**Alt**
|Select_text=Premere il tasto sinistro del mouse su un oggetto che si desidera selezionare.
|Pan_text=Tenere premuto **Alt** e il pulsante centrale del mouse, quindi spostare il puntatore.
|Zoom_text=Tenere premuto **Alt** e il tasto destro del mouse, quindi spostare il puntatore.
</div>

|Alt=**Alt**

|Select_text=Press the left mouse button over an object you want to select.

|Zoom_text=Use the mouse wheel to zoom in and out.

Alternatively, hold **Alt** and the right mouse button, then move the pointer.

|Rotate_view_text=Hold **Alt** and the left mouse button, then move the pointer.

|Pan_text=Hold **Alt** and the middle mouse button, then move the pointer.

|Tilt_view_text=Hold **Alt** and both left and right mouse buttons, and then move the pointer sideways.
}}



### Navigazione OpenCascade 

La navigazione OpenCascade si basa sul modello [OpenCascade](https://www.opencascade.com/).


<div class="mw-translate-fuzzy">


{{OpenCascade Navigation
|Select_name=Selezione
|Pan_name=Traslazione
|Zoom_name=Zoom
|Rotate_view_name=Rotazione vista
|Ctrl=**Ctrl**
|Select_text=Premere il tasto sinistro del mouse su un oggetto che si desidera selezionare.
|Pan_text=Tenere premuto il pulsante centrale del mouse, quindi spostare il puntatore.
|Zoom_text=Usare la rotellina del mouse per zoommare avanti e indietro.
</div>

|Ctrl=**Ctrl**

|Select_text=Press the left mouse button over an object you want to select.

|Zoom_text=Use the mouse wheel to zoom in and out.

<div class="mw-translate-fuzzy">
In alternativa, tenere premuto **Ctrl** e il tasto sinistro del mouse, quindi spostare il puntatore.
|Rotate_view_text=Tenere premuto **Ctrl** e il tasto destro del mouse, quindi spostare il puntatore.
}}


</div>

\|Rotate_view_text=Hold the middle mouse button, then press and hold the right mouse button, then move the pointer.

Alternatively, hold **Ctrl** and the right mouse button, then move the pointer.

\|Pan_text=Hold the middle mouse button, then move the pointer. It is possible to hold **Ctrl**. }}



### Navigazione OpenInventor 

La Navigazione OpenInventor (formalmente Inventor) si basa sul modello [Open Inventor](http://en.wikipedia.org/wiki/Open_Inventor). Per selezionare gli oggetti, è necessario tenere premuto il tasto **Shift** o **Ctrl**.

Questo stile non è basato su Autodesk Inventor.


<div class="mw-translate-fuzzy">


{{OpenInventor Navigation
|Select_name=Selezione
|Pan_name=Traslazione
|Zoom_name=Zoom
|Rotate_view_name=Rotazione vista
|Shift=**Shift**
|Select_text=Tenere premuto **Shift**, quindi premere il tasto sinistro del mouse sopra un oggetto che si desidera selezionare.
</div>

|Shift=**Shift**

|Select_text=Hold **Shift**, then press the left mouse button over an object you want to select.

<div class="mw-translate-fuzzy">
Invece tenere premuto **Ctrl** per selezionare più oggetti.
|Pan_text=Tenere premuto il pulsante centrale del mouse, quindi spostare il puntatore.
|Zoom_text=Usare la rotellina del mouse per ingrandire e rimpicciolire.
</div>

|Zoom_text=Use the mouse wheel to zoom in and out.

<div class="mw-translate-fuzzy">
In alternativa, tenere premuto il pulsante centrale del mouse, quindi premere e tenere premuto il pulsante sinistro del mouse, quindi spostare il puntatore. 
|Rotate_view_text=Tenere premuto il pulsante sinistro del mouse, quindi spostare il puntatore.
}}


</div>

\|Rotate_view_text=Hold the left mouse button, then move the pointer.

\|Pan_text=Hold the middle mouse button, then move the pointer. }}



### Navigazione OpenSCAD 

La Navigazione OpenSCAD si basa sul modello [OpenSCAD](https://openscad.org/).


<div class="mw-translate-fuzzy">


{{OpenSCAD_Navigation
|Select_name=Selezione
|Pan_name=Traslazione
|Zoom_name=Zoom
|Rotate_view_name=Rotazione vista
|Shift=**Shift**
|Select_text=Premere il pulsante sinistro del mouse su un oggetto che si desidera selezionare.
</div>

|Shift=**Shift**

|Select_text=Press the left mouse button over an object you want to select.

<div class="mw-translate-fuzzy">
{{VersionMinus/it|0.21}} Tenere premuto **Ctrl** e **Shift** quando si preme il pulsante del mouse per trascinare un oggetto in uno schizzo in modalità di modifica.
|Pan_text=Tenere premuto il pulsante destro del mouse, quindi spostare il puntatore.
|Zoom_text=Tenere premuto il pulsante centrale del mouse, quindi spostare il puntatore.
In alternativa, tenere premuto **Shift** e il pulsante destro del mouse, quindi spostare il puntatore.
|Rotate_view_text=Tenere premuto il pulsante sinistro del mouse, quindi spostare il puntatore.
</div>

|Zoom_text=Use the mouse wheel to zoom in and out.

Alternatively, hold the middle mouse button, then move the pointer.

Or hold **Shift** and the right mouse button, then move the pointer.

|Rotate_view_text=Hold the left mouse button, then move the pointer.

<div class="mw-translate-fuzzy">
In alternativa, e quando uno schizzo è in modalità di modifica, tenere premuto il pulsante centrale del mouse, quindi tenere premuto il pulsante destro del mouse, quindi spostare il puntatore.
</div>

|Pan_text=Hold the right mouse button, then move the pointer.
}}



### Navigazione Revit 

La Navigazione Revit si basa sul modello [Revit](https://en.wikipedia.org/wiki/Autodesk_Revit).


<div class="mw-translate-fuzzy">


{{Revit Navigation
|Select_name=Selezione
|Pan_name=Traslazione
|Zoom_name=Zoom
|Rotate_view_name=Rotazione vista
|Shift=**Shift**
|Select_text=Premere il tasto sinistro del mouse su un oggetto che si desidera selezionare.
|Pan_text=Tenere premuto il pulsante centrale del mouse, quindi spostare il puntatore.
</div>

|Shift=**Shift**

|Select_text=Press the left mouse button over an object you want to select.

<div class="mw-translate-fuzzy">
|Zoom_text=Usa la rotellina del mouse per zoommare avanti e indietro.
|Rotate_view_text=Tenere premuto **Shift** e il pulsante centrale del mouse, quindi spostare il puntatore.
</div>

|Rotate_view_text=Hold **Shift** and the middle mouse button, then move the pointer.

<div class="mw-translate-fuzzy">
In alternativa, tenere premuto il pulsante centrale del mouse, e tenere premuto il pulsante destro del mouse, quindi spostare il puntatore.
}}


</div>

\|Pan_text=Hold the middle mouse button, then move the pointer.


<div class="mw-translate-fuzzy">

In alternativa, tenere premuti i pulsanti sinistro e destro del mouse, quindi spostare il puntatore.


</div>



### Navigazione TinkerCAD 

La Navigazione TinkerCAD si basa sul modello [TinkerCAD](https://en.wikipedia.org/wiki/Tinkercad).


<div class="mw-translate-fuzzy">


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


</div>

\|Select_text=Press the left mouse button over an object you want to select.

\|Zoom_text=Use the mouse wheel to zoom in and out.

\|Rotate_view_text=Press the right mouse button, then move the pointer.

\|Pan_text=Hold the middle mouse button, then move the pointer. }}



### Navigazione Touchpad 

Con la Navigazione touchpad, lo spostamento, lo zoom e la rotazione della vista richiedono un tasto modificatore insieme al touchpad. Questo stile può essere utilizzato anche con il mouse.


<div class="mw-translate-fuzzy">


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


</div>

\|Ctrl=**Ctrl** \|Shift=**Shift** \|Alt=**Alt**

\|Select_text=Press the left mouse button over an object you want to select.

\|Zoom_text=Hold **Ctrl** and **Shift**, then move the pointer.

\|Rotate_view_text=Hold **Alt**, then move the pointer.

Alternatively, hold **Shift** and the left button, then move the pointer.

\|Pan_text=Hold **Shift**, then move the pointer. }}



## Supporto Hardware 

FreeCAD supporta anche i [dispositivi di input 3D](3D_input_devices/it.md).



## Navigazione consigliata per macOS 

Sui MacBook con trackpad la navigazione gestuale funziona molto bene, ma i gesti hanno un significato speciale:

-   Zoom: trascina con due dita.
-   Ruota: trascina con tre dita.
-   Panoramica: **Ctrl** + tre dita.


{{docnav/it
|[Per iniziare](Getting_started/it.md)
|[Metodi di selezione](Selection_methods/it.md)
}}



---
⏵ [documentation index](../README.md) > Mouse navigation/it
