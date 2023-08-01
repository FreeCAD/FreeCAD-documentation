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

## Naming


<div class="mw-translate-fuzzy">

### Nome del comando 

Il Comando Gui è denominato nel modo: *ModuleName_CommandName*. Ad esempio, \"Base_Open\" nell\'interfaccia grafica è il comando *Open* nel sistema *Base*. I comandi della Gui specifici di un modulo sono denominati con il nome del modulo come prefissso. Ad esempio: \"Part_Cylinder\".


</div>


<div class="mw-translate-fuzzy">

Se la sua documentazione non è completa usare la maschera [Template:UnfinishedDocu](Template_UnfinishedDocu.md) (en) - [Documentazione incompleta](Template:UnfinishedDocu/it.md) (it).


</div>

## Help page 


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

<img alt="" src=images/Tango-Palette.png  style="width:400px;">


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



---
⏵ [documentation index](../README.md) > Gui Command/it
