# Gui Command/it
I comandi dell\'interfaccia grafica utente (GuiCommand) sono una delle funzioni più importanti di FreeCAD in quanto principale metodo di interazione dell\'utente. Ogni volta che l\'utente seleziona una voce di menu o preme un pulsante della barra degli strumenti, attiva un GuiCommand. Alcuni degli attributi della GuiCommand sonoː

-   Definisce un nome
-   Contiene una icona
-   Definisce la possibilità di annullare/ripetere
-   Ha una pagina di aiuto
-   Apre e controlla le finestre di dialogo
-   Registra macro
-   etc\...



## Nome del comando 

Il GuiCommand è denominato in modo standard: *ModuleName_CommandName* ad esempio, \"[Base_Open](Base_Open.md)\" questo è il comando Open Gui nel sistema Base. Il GuiCommand in un determinato modulo è denominato con il nome del modulo in primo piano, ad esempio \"[Part_Cylinder](Part_Cylinder/it.md)\".

Se la sua documentazione non è completa usare la maschera [Template:UnfinishedDocu](Template_UnfinishedDocu.md) (en) - [Documentazione incompleta](Template:UnfinishedDocu/it.md) (it).



## Pagina di aiuto 

Ogni GuiCommand deve avere una pagina di aiuto. La pagina di aiuto è ospitata sul wiki della documentazione di FreeCAD. L\'articolo ha lo stesso nome del GuiCommand, es. [Draft ShapeString](Draft_ShapeString.md).

Per creare le proprie pagine di aiuto si può utilizzare il modello [GuiCommand model](GuiCommand_model.md) (en) - [Modello di comando Gui](GuiCommand_model/it.md) (it)

Esempi in italiano:

-   [Draft Forma da testo](Draft_ShapeString/it.md)
-   [Draft Linea](Draft_Line/it.md)

Esempi in inglese:

-   [Draft ShapeString](Draft_ShapeString.md)
-   [Draft Line](Draft_Line.md)



## Icone

<img alt="" src=images/Tango-Palette.png  style="width:400px;">

Ogni comando dell\'interfaccia grafica deve avere un\'icona. Utilizziamo il [Set di icone Tango](http://tango-project.org/Tango_Desktop_Project/) e le sue linee guida. Sul lato destro si vede la tavolozza dei colori Tango.

Tutte le icone devono essere create in formato [SVG](SVG/it.md) con un\'applicazione per immagini vettoriali, come [Inkscape](http://inkscape.org). Ciò semplifica l\'applicazione delle modifiche e la derivazione di icone aggiuntive nello stesso spazio dell\'applicazione.



### Tabella di codifica colori delle icone 

<img alt="" src=images/Colorchart.png  style="width:200px;">

Cerchiamo di rispettare quanto più possibile questo schema, in modo che il colore delle icone abbia un preciso significato.



---
⏵ [documentation index](../README.md) > Gui Command/it
