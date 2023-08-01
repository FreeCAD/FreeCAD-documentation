# WebTools Sketchfab/it
---
- GuiCommand:   Name:WebTools Sketchfab   Name/it:WebTools Sketchfab   MenuLocation:WebTools - Sketchfab   |Workbenches:[[WebTools Workbench/it   WebTools]]|Shortcut:   SeeAlso:---


</div>

## Descrizione

Questo strumento consente di esportare e caricare gli oggetti in un proprio account [SketchFab](http://www.sketchfab.com){{Version/it|0.17}}

![](images/Sketchfab_exporter.jpg )


<div class="mw-translate-fuzzy">

## Uso

1.  Creare un proprio un account su [SketchFab](http://www.sketchfab.com), se non esiste ancora. Gli account gratuiti vanno bene, gli account a pagamento aggiungono ulteriori funzionalità, come la possibilità di avere modelli privati e grandi dimensioni massime di upload
2.  Preparare un modello che si desidera caricare
3.  Cliccare su <img alt="" src=images/WebTools_Sketchfab.png  style="width:32px;"> dalla barra degli strumenti principale nel [WebTools Workbench](WebTools_Workbench/it.md)
4.  Compilare i campi. Nome e chiave API sono obbligatori
5.  Cliccare sul pulsante \"Upload\"


</div>

1.  Make yourself an account on [SketchFab](http://www.sketchfab.com) if you don\'t have one yet. Free accounts are just fine, paid accounts add more features like the possibility to have private models and bigger maximum upload sizes
2.  Prepare a model you wish to upload
3.  Click on <img alt="" src=images/WebTools_Sketchfab.svg  style="width:32px;"> from the main toolbar in the [WebTools Workbench](WebTools_Workbench.md)
4.  Fill in the fields. Name and API key are mandatory
5.  Click the \"Upload\" button

## Opzioni

-   Affinché questo esportatore sia in grado di connettersi al proprio account sketchfab serve una chiave API Sketchfab. Premendo il tasto \"Obtain\", si viene indirizzati alla pagina delle impostazioni di Sketchfab, dove viene fornita una chiave API (che è unica per il proprio account). Copiare la chiave e incollarla nel campo \"API key\" dell\'esportatore. Questo valore viene memorizzato da FreeCAD, quindi basta inserirlo una volta sola.
-   Il campo nome è obbligatorio, gli altri possono essere lasciati vuoti.
-   L\'esportatore propone numerosi formati diversi di esportazione. Il migliore per voi dipende dal tipo di modello e dal risultato che volete ottenere, si raccomanda di verificare quale funziona meglio. Generalmente, OBJ + MTL dà un migliore controllo sui materiali, mentre IV (OpenInventor) dà un risultato che è maggiormente simile a quello che si vede nella vista 3D di FreeCAD.
-   Quando il modello è caricato, Sketchfab offre un\'interfaccia piuttosto avanzata in cui è possibile configurare ulteriormente i materiali, l\'illuminazione e l\'ambiente.
-   Quando si preme \"Upload button\", dopo aver completato il caricamento, se tutto è andato bene, il pulsante si trasforma in \"View your model online\", che, se cliccato, porta direttamente alla pagina del modello su Sketchfab.
-   Alcuni formati, come OBJ, sono interpretati in modo diverso da Sketchfab e da FreeCAD. FreeCAD considera l\'asse Z rivolto verso l\'alto, mentre Sketchfab considera che punti verso la persona che sta davanti allo schermo. Per rimediare a questo, dopo aver terminato l\'upload, l\'esportatore utilizza la API Sketchfab per ruotare il modello nella sua posizione corretta. Se questa operazione non riesce, si viene avvertiti, e comunque il vostro modello rimane caricato correttamente. È possibile ruotarlo manualmente nell\'interfaccia di Sketchfab, premendo la freccia destra oltre l\'asse \"X\" nella scheda di orientamento del modello.



---
![](images/Button_right.svg) [documentation index](../README.md) > WebTools Sketchfab/it
