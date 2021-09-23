# Gui Command/it
<div class="mw-translate-fuzzy">

I comandi dell\'interfaccia grafica dell\'utente (GuiCommand) sono una delle funzioni più importanti di FreeCAD e sono il punto principale di interazione dell\'utente. Ogni volta che l\'utente seleziona una voce del menu o preme un pulsante si attiva un comando Gui. Alcuni degli attributi di un comando grafico sono:

-   Definisce un nome
-   Contiene una icona
-   Definisce la possibilità di annullare/ripetere
-   Ha una pagina di aiuto
-   Apre e controlla le finestre di dialogo
-   Registra macro
-   etc\...


</div>


<div class="mw-translate-fuzzy">

### Nome del comando 

Il Comando Gui è denominato nel modo: *ModuleName\_CommandName*. Ad esempio, \"Base\_Open\" nell\'interfaccia grafica è il comando *Open* nel sistema *Base*. I comandi della Gui specifici di un modulo sono denominati con il nome del modulo come prefissso. Ad esempio: \"Part\_Cylinder\".


</div>


<div class="mw-translate-fuzzy">

Se la sua documentazione non è completa usare la maschera [Template:UnfinishedDocu](Template:UnfinishedDocu.md) (en) - [Documentazione incompleta](Template:UnfinishedDocu/it.md) (it).


</div>


<div class="mw-translate-fuzzy">

### Pagina di aiuto 

Ogni GuiCommand deve avere una pagina di aiuto. La pagina di aiuto è ospitata sul wiki della documentazione di FreeCAD. L\'articolo ha lo stesso nome del GuiCommand. Per esempio [Draft ShapeString](Draft_ShapeString.md) (in inglese) - [Draft ShapeString](Draft_ShapeString/it.md) (in it).


</div>


<div class="mw-translate-fuzzy">

Per creare le proprie pagine di aiuto si può utilizzare il modello: [GuiCommand model](GuiCommand_model.md) (en) - [Modello di comando Gui](GuiCommand_model/it.md) (it)


</div>


<div class="mw-translate-fuzzy">

Esempi in italiano:

-   [Draft ShapeString](Draft_ShapeString/it.md)
-   [Draft Linea](Draft_Line/it.md)

Esempi in inglese:

-   [Draft ShapeString](Draft_ShapeString.md)
-   [Draft Line](Draft_Line.md)


</div>


<div class="mw-translate-fuzzy">

### Icone

<img alt="" src=images/Tango-Palette.png  style="width:400px;">


</div>


<div class="mw-translate-fuzzy">

Ogni comando dell\'interfaccia grafica deve avere un\'icona. Utilizziamo il [Set di icone Tango](http://tango.freedesktop.org/Tango_Desktop_Project) e le sue linee guida. Sul lato destro si vede la tavolozza dei colori Tango.


</div>


<div class="mw-translate-fuzzy">

Produrre preferiblemente tutte le icone in formato Grafico Vettoriale Scalabile (SVG) per esempio con [Inkscape](http://inkscape.org). Questo rende più facile applicare le modifiche e ricavare ulteriori icone nell\'ambito della stessa applicazione.


</div>


<div class="mw-translate-fuzzy">

**tabella del codice colore delle icone**


</div>

<img alt="" src=images/Colorchart.png  style="width:200px;">

Cerchiamo di rispettare quanto più possibile questo schema, in modo che il colore delle icone abbia un preciso significato.


<div class="mw-translate-fuzzy">

## Requisiti di qualità 

In FreeCAD esistono diversi comandi dell\'interfaccia grafica (Funzioni) che sono sperimentali o utilizzati raramente in attesa di implementazione. Questi comandi Gui si trovano per lo più negli ambienti specifici quali Parte, Mesh o Cam. Per consentire all\'utente una sperimentazione efficace si è creato un ambiente di lavoro definito *Completo*. Questo ambiente di lavoro incorpora tutti i comandi Gui che soddisfano determinati **requisiti di qualità** che sono descritti qui:


</div>

There are a lot of GuiCommands (tools) in FreeCAD which are experimental or used for a short time to test implementation of new features. These GuiCommands are mostly in the dedicated workbenches like Part, Mesh or Cam. To ensure a good user experience the workbench *Complete* was created. This workbench incorporates all GuiCommands which meet certain quality requirements which are described here:


<div class="mw-translate-fuzzy">

-   Il comando o funzione è **finito**. Non ci sono lavori in corso!
-   Ha una **pagina di aiuto** come [Draft ShapeString](Draft_ShapeString/it.md)
    -   Tutti i campi del modello [Template:GuiCommand](Template:GuiCommand.md) - [Maschera di GuiCommand](Template:GuiCommand/it.md) sono compilati
    -   È visualizzata l\'eventuale finestra di dialogo del comando
    -   C\'è la descrizione dettagliata del comando, di tutti i suoi parametri e delle impostazioni
    -   Le interfacce e classi Python correlate sono descritte con codici di esempio
-   È definita una icona appropriata e una posizione nel menu


</div>


<div class="mw-translate-fuzzy">

Si spera che questo sia vero per tutti i comandi Gui della [List of Commands](List_of_Commands.md) - [Lista dei comandi](List_of_Commands/it.md).


</div>


{{Powerdocnavi

}}

---
[documentation index](../README.md) > Gui Command/it
