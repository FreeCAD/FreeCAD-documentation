# TechDraw Preferences/it
<div class="mw-translate-fuzzy">





</div>






## Introduzione


<div class="mw-translate-fuzzy">

Le preferenze per l\'ambiente [TechDraw](TechDraw_Workbench/it.md) si trovano nel [Editor delle preferenze](Preferences_Editor/it.md), nel menu **Modifica → Preferenze → TechDraw**.


</div>

There are seven pages: [General](#General.md), [Scale](#Scale.md), [Dimensions](#Dimensions.md), [Annotation](#Annotation.md), [Colors](#Colors.md), [HLR](#HLR.md) and [Advanced](#Advanced.md).


<div class="mw-translate-fuzzy">

Tutte le impostazioni delle preferenze con etichette in *corsivo* sono valori predefiniti per i nuovi oggetti inseriti nel disegno. Non hanno alcun effetto sugli oggetti esistenti.


</div>

This page has been updated for version 1.0.



## Generale


<div class="mw-translate-fuzzy">

<img alt="Preferenze generali" src=images/TechDraw_PreferencesGeneral.png  style="width:350px;">


</div>



### Aggiornamento del disegno 


<div class="mw-translate-fuzzy">


{{Version/it|0.19}}

-   **Aggiorna con il 3D**: controlla se le pagine vengono aggiornate o meno ogni volta che si cambia il modello 3D. Questa è un\'impostazione di gestione globale.
-   **Consenti sostituzione pagina**: Controlla se la proprietà **[Keep Update](TechDraw_PageDefault/it#Proprietà.md)** di una pagina può o meno sostituire il parametro **Aggiorna con il 3D** a livello di sistema. Questa è un\'impostazione di gestione globale.
-   **Mantieni aggiornate le pagine**: mantiene le pagine di disegno sincronizzate con i cambiamenti del modello 3D in tempo reale. Può rallentare i tempi di risposta.
-   **Viste secondarie distribuite automaticamente**: distribuisce automaticamente le viste secondarie per i [Gruppi di proiezioni](TechDraw_ProjectionGroup/it.md).


</div>



### Etichette


<div class="mw-translate-fuzzy">

-   **Carattere etichetta**: il nome del carattere predefinito per le etichette.
-   **Dimensioni etichetta**: dimensione predefinita per il testo dell\'etichetta.


</div>



### Convenzioni


<div class="mw-translate-fuzzy">

-   **Angolo di proiezione del gruppo**: stabilisce se il [gruppo di proiezioni](TechDraw_ProjectionGroup/it.md) deve utilizzare la proiezione di primo o terzo angolo. Per la descrizione vedere [multiview projection](https://en.wikipedia.org/wiki/Multiview_projection#Multiviews).
-   **Stile delle linee nascoste**: lo stile da utilizzare per le linee nascoste.


</div>



### File


<div class="mw-translate-fuzzy">

-   **Modello predefinito**: file del [modello](TechDraw_Templates.md) predefinito per le nuove pagine.
-   **Directory del modello**: la directory di partenza per il pulsante **<img src="images/TechDraw_PageTemplate.svg" width=16px> [Nuovo disegno da modello](TechDraw_PageTemplate.md)**.
-   **File del modello di tratteggio**: file di default [SVG](SVG/it.md) o [bitmap](bitmap/it.md) per il [tratteggio da modello](TechDraw_Hatch/it.md).
-   **File del gruppo di linee**: file alternativo per le definizioni personali del [gruppo di linee](TechDraw_LineGroup/it.md).
-   **Directory di saldatura**: la directory di default per il pulsante **[<img src=images/TechDraw_WeldSymbol.svg style="width:16px"> [Informazioni di saldatura](TechDraw_WeldSymbol/it.md)**. {{Version/it|0.19}}.
-   **File PAT**: file di default per il modello PAT predefinito per il [tratteggio geometrico](TechDraw_GeometricHatch/it.md).
-   **Nome del modello**: il nome del motivo PAT predefinito.


</div>

### Grid

-   **Show Grid**: Default Show Grid setting for new pages.
-   **Grid Spacing**: Default distance between grid lines for new pages.

### Selection

-   **Enable Multiselection Mode**: If enabled, clicking without **Ctrl** does not clear the existing selection. <small>(v1.0)</small> 

### View Defaults 

-   **Use 3d Camera Direction**: If checked, the 3d camera direction (or normal of a selected face) will be used as the view direction. If not checked, Views will be created as Front Views. <small>(v1.0)</small> 
-   **Always Show Label**: If checked, view labels will be displayed even when frames are suppressed. <small>(v1.0)</small> 

### Snapping

-   **Snap View Alignment**: If checked, Views will be snapped into alignment when dragged. <small>(v1.0)</small> 
-   **View Snapping Factor**: Tolerance for snapping of Views - if a View is within this fraction of View size of perfect alignment, it will snap into alignment. <small>(v1.0)</small> 




<div class="mw-translate-fuzzy">

## Scale


</div>


<div class="mw-translate-fuzzy">

<img alt="Preferenze di Scala" src=images/TechDraw_PreferencesScale.png  style="width:350px;">


</div>



### Scala

-   **Scala della pagina**: Scala predefinita per le nuove pagine.
-   **Scala delle viste**: Scala predefinita per le nuove viste.
-   **Scala personalizzata delle viste**: Scala predefinita per le viste se **Scala delle viste** è *Personalizzata*.



### Regolazioni delle dimensioni 


<div class="mw-translate-fuzzy">

-   **Scala del vertice**: Scala dei punti [vertici](Glossary#V.md). Moltiplicatore della larghezza della linea.
-   **Scala del segno di centro**: Dimensione dei segni di centro. Moltiplicatore delle dimensioni del vertice.
-   **Scala per il testo della tolleranza**: Regolazione della dimensione del carattere per la tolleranza. Moltiplicatore della dimensione di **[Font Size](TechDraw_Preferences#Dimensions_2.md)**.
-   **Dimensione del marcatore di testo modificabile**: dimensione in mm dell\'indicatore di testo modificabile nei [modelli](TechDraw_Templates/it.md) (punti verdi).
-   **Scala del simbolo saldatura**: Moltiplicatore per dimensioni dei [simboli di saldatura](TechDraw_WeldSymbol/it.md). {{Version/it|0.19}}


</div>



## Quotatura

<img alt="Preferenze quoattura" src=images/Preferences_TechDraw_Page_Dimensions.png  style="width:350px;">



### Quotatura 


<div class="mw-translate-fuzzy">

-   **Standard e Stile**: lo standard da utilizzare per la quotatura. La differenza tra gli standard è mostrata nell\'immagine: ![\|500px\|Differenze tra gli standard supportati](images/TechDraw_Dimension_standardization.png )
-   **Usa i decimali globali**: usa il numero di decimali delle [preferenze generali](Preferences_Editor/it#Unità.md).
-   **Mostra le unità di misura**: aggiunge l\'unità (mm, in, ecc.) al valore delle quota.
-   **Decimali alternativi**: numero di decimali se **Usa i decimali globali** non è usato.
-   **Formato di default**: formato personalizzato per il testo della quota. Usa il [printf format specifier](https://en.wikipedia.org/wiki/Printf_format_string).
-   **Dimensione del carattere**: dimensione del carattere per il testo della quota.
-   **Simbolo di diametro**: carattere utilizzato per indicare la dimensione del diametro.
-   **Stile delle frecce**: stile delle frecce per le quote.
-   **Dimensione delle frecce**: dimensione delle frecce per le quote.


</div>

### Tools

-   **Dimensioning tools**: Select the type of dimensioning tools for the toolbar. Whichever you choose, all tools are always available in the menu and through shortcuts. The options are: <small>(v1.0)</small> 
    -   *Single tool*: A [single tool](TechDraw_Dimension.md) for all dimensioning in the toolbar: Distance, Distance X / Y, Angle, Radius. Others in dropdown.
    -   *Separated tools*: Individual tools for each dimensioning tool.
    -   *Both*: You will have both the \'Single tool\' and the separated tools.
-   **Dimension tool diameter/radius mode**: While using the [Dimension](TechDraw_Dimension.md) tool you may choose how to handle circles and arcs: <small>(v1.0)</small> 
    -   *Auto*: The tool will apply radius to arcs and diameter to circles.
    -   *Diameter*: The tool will apply diameter to all.
    -   *Radius*: The tool will apply radius to all.



## Annotazioni


<div class="mw-translate-fuzzy">

<img alt="Preferenze per le annotazioni" src=images/TechDraw_PreferencesAnnotation.png  style="width:350px;">


</div>

### Annotation


<div class="mw-translate-fuzzy">

-   **Standard della linea di sezione**: standard da utilizzare per tracciare le linee di sezione nelle [viste di sezioni](TechDraw_SectionView/it.md).
-   **Stile della linea di sezione**: stile per le linee di sezione.
-   **Superficie della sezione tagliata**: stile per la superficie tagliata nella sezione. Le opzioni sono: {{Version/it|0.19}}
    -   *Nascosta*: la superficie non è visibile.
    -   *Tinta unita*: la superficie ottiene il colore impostato nella scheda Colori per **Faccia di sezione**
    -   *Tratteggio SVG*: la superficie viene [tratteggiata con un modello SVG o bitmap](TechDraw_Hatch/it.md).
    -   *Tratteggio PAT*: la superficie viene [tratteggiata in modo geometrico](TechDraw_GeometricHatch/it.md).
-   **Nome del gruppo di linee**: nome di default per specificare un [gruppo di linee](TechDraw_LineGroup/it.md).
-   **Contorno della vista in dettaglio**: forma del contorno per le [viste di dettaglio](TechDraw_DetailView/it.md).
-   **Stile del contorno del dettaglio**: stile di linea della forma del contorno delle [viste di dettaglio](TechDraw_DetailView/it.md). {{Version/it|0.19}}
-   **Stile della linea centrale**: stile predefinito per le [linee centrali](TechDraw_FaceCenterLine/it.md).
-   **Forma della bolla**: forma delle bolle per la [pallinatura](TechDraw_Balloon/it.md).
-   **Finale delle linee guida della pallinatura**: stile predefinito per le estremità della linea guida della pallinatura.
-   **Lunghezza di piega della linea guida**: lunghezza del nodo della linea guida della pallinatura.
-   **Bolla con triangolo in ortogonale**: se il **Finale delle linee guida della pallinatura** è *Triangolo pieno*, il triangolo può avere solo una direzione verticale o orizzontale quando la bolla viene spostata.
-   **Linea guida auto orizzontale**: forza l\'ultimo segmento della [linea guida](TechDraw_LeaderLine/it.md) ad essere orizzontale.
-   **Mostra i centri**: mostra i segni del centro dell\'arco nelle viste.
-   **Stampa i centri**: mostra i segni del centro dell\'arco nella stampa.


</div>

### Lines

-   **Line Standard**: Standard to be used to draw section lines in [section views](TechDraw_SectionView.md).
-   **Line Width Group**: A [LineGroup](TechDraw_LineGroup.md) to set the default line widths.
-   **Hidden Line Style**: Style of hidden lines. <small>(v1.0)</small> 
-   **Section Line Style**: Style for section lines.
-   **Detail Highlight Style**: Line style of the outline shape for [detail views](TechDraw_DetailView.md).
-   **Center Line Style**: Default style for [centerlines](TechDraw_FaceCenterLine.md).
-   **Break Line Style**: Default style for lines used to indicate [BrokenViews](TechDraw_BrokenView.md). <small>(v1.0)</small> 
-   **Line End Cap Shape**: The default (round) should almost always be the right choice. Flat or square caps are useful if you are planning to use a drawing as a 1:1 cutting guide.



## Colori


<div class="mw-translate-fuzzy">

<img alt="Preferenze per i colori" src=images/TechDraw_Preferences_Colors.PNG  style="width:350px;">


</div>

Impostazione dei colori predefiniti per le nuove pagine.


<div class="mw-translate-fuzzy">

-   **Normale**: colore della linea normale.
-   **Preselezione**: colore della preselezione. Il colore utilizzato per evidenziare gli oggetti quando ci si passa sopra con il mouse.
-   **Selezionato**: colore per gli oggetti selezionati.
-   **Sfondo**: colore di sfondo attorno alle pagine.
-   **Dimensione**: colore delle linee di quota e del testo.
-   **Linea centrale**: colore per le [linee centrali](TechDraw_FaceCenterLine/it.md).
-   **Contorno del dettaglio**: colore della linea per la forma del contorno delle [viste di dettagli](TechDraw_DetailView/it.md). {{Version/it|0.19}}
-   **Facce trasparenti**: se selezionato, le facce degli oggetti saranno trasparenti. In caso contrario, per le facce verrà utilizzato il colore impostato. {{Version/it|0.19}}
-   **Linee nascoste**: colore della linea nascosta. Questo colore verrà utilizzato per tutti i tipi di [linee nascoste](#HLR_Parameters.md).
-   **Faccia di sezione**: colore della superficie tagliata nelle [viste di sezione](TechDraw_SectionView/it.md). Utilizzato solo se l\'impostazione **Superficie della sezione tagliata** della scheda Annotazione è impostata su *Tinta unita*.
-   **Linea di sezione**: colore della linea di taglio della [vista di sezione](TechDraw_SectionView/it.md).
-   **Tratteggio**: colore dell\'immagine del [tratteggio](TechDraw_Hatch/it.md).
-   **Tratteggio geometrico**: colore del [tratteggio geometrico](TechDraw_GeometricHatch/it.md).
-   **Vertice**: colore dei [vertici](Glossary#V.md) selezionabili nelle viste.
-   **Linea guida**: colore per le nuove [linee guida](TechDraw_LeaderLine/it.md).


</div>



## HLR


<div class="mw-translate-fuzzy">

<img alt="Preferenze per HLR" src=images/TechDraw_PreferencesHLR.png  style="width:350px;">


</div>

HLR sta per *hidden line removal* (rimozione della linea nascosta).

-   **Usa l\'approssimazione poligonale**: utilizza un\'approssimazione per trovare le linee nascoste. Questo sistema è veloce, ma il risultato è un insieme di brevi linee rette.
-   **Mostra i bordi ed i contorni**: mostra i bordi duri e i contorni (le linee visibili sono sempre mostrate)
-   **Mostra le linee di tangenza**: mostra linee morbide. Una linea morbida è una linea che indica un cambiamento tra le superfici tangenti, come nella transizione da una superficie piana a un [raccordo](https://en.wikipedia.org/wiki/Fillet_(mechanics)).
-   **Mostra le linee di giunzione**: mostra le linee di giunzione. Una linee di giunzione è un confine tra le facce.
-   **Mostra le linee iso U, V**: mostra le linee isoparametriche. Iso sta per *isoparametriche*. [Ecco una descrizione](https://knowledge.autodesk.com/support/alias-products/learn-explore/caas/CloudHelp/cloudhelp/2014/ENU/Alias/files/GUID-4CCDF144-DB4F-4BEB-BA5A-E69CED27F4B9-htm.html) di quali sono le linee isoparametriche (in realtà le curve).
-   **Numero di isoparametriche**: il numero di linee isoparametriche per bordo della faccia.




<div class="mw-translate-fuzzy">

## Avanzate


</div>


<div class="mw-translate-fuzzy">

<img alt="Preferenze avanzate" src=images/TechDraw_PreferencesAdvanced.png  style="width:350px;">


</div>


<div class="mw-translate-fuzzy">

-   **Rileva le facce**: se selezionato, TechDraw tenterà di creare le facce utilizzando i segmenti di linea restituiti dall\'algoritmo di rimozione delle linee nascoste. Le facce devono essere rilevate per poter usare il [tratteggio](TechDraw_Hatching/it.md), ma può esserci una penalizzazione delle prestazioni in modelli complessi.
-   **Mostra i bordi delle sezioni**: evidenzia il bordo della sezione tagliata nelle [viste di sezioni](TechDraw_SectionView/it.md).
-   **Debug della sezione**: scarica i risultati intermedi durante l\'elaborazione di una vista in sezione
-   **Debug del dettaglio**: scarica i risultati intermedi durante l\'elaborazione di una vista di dettaglio
-   **Accetta gli spigoli pazzi**: include i bordi con geometria imprevista nei risultati, ad es. zero lunghezza
-   **Fondi prima della sezione**: esegue un\'operazione di fusione sulle forme di input prima di elaborare la vista in sezione.
-   **Mostra la geometria 2D dispersa**: include oggetti 2D nelle proiezioni, ad es. schizzi sciolti
-   **Forma terminale della linea**: Impostazione della forma del cappuccio terminale delle linee. Spiegazione delle opzioni in: <https://doc.qt.io/qt-5/qt.html#PenCapStyle-enum>
-   **Massimo numero di tessere di tratteggio SVG**: limite di tessere SVG 64x64 pixel utilizzate per tratteggiare una singola faccia. Per le grandi dimensioni si potrebbe ottenere un errore relativo a troppi riquadri SVG. In questo caso è necessario aumentare il limite delle tessere.
-   **Massimo numero di segmenti di tratteggio PAT**: massimo numero di segmenti di linea da utilizzare quando si tratteggia una faccia con un modello PAT.


</div>


<div class="mw-translate-fuzzy">





</div>


{{TechDraw Tools navi

}}



---
⏵ [documentation index](../README.md) > [Preferences](Category_Preferences.md) > [TechDraw](TechDraw_Workbench.md) > TechDraw Preferences/it
