# Drawing templates/it



**The [Drawing Workbench](Drawing_Workbench.md) became obsolete in v0.17. Consider using the [TechDraw Workbench](TechDraw_Workbench.md) instead.**


{{TOCright}}

## Creare modelli SVG 


<div class="mw-translate-fuzzy">

Creare dei nuovi modelli di fogli per il modulo di disegno di proiezione [Drawing](Drawing_Workbench/it.md) è molto semplice. Oltre a questa pagina consultare anche il tutorial [Creare dei modelli](Drawing_Template_HowTo/it.md). I modelli sono dei file SVG creati con qualsiasi applicazione in grado di esportare file SVG, ad esempio [Inkscape](http://www.inkscape.org). Si devono seguire solo due regole:


</div>

### Base rules 


<div class="mw-translate-fuzzy">

### Regole di base 

-   Un pixel = un millimetro. Si può avere il formato pagina specificato all\'interno del tag di apertura<svg>, sia senza unità che con \"mm\". Ad esempio, queste sono due forme sono valide:


</div>

 {.html}
width="1067mm"
height="762mm"


oppure

 {.html}
width="1067"
height = "762"


Anche se svg supporta i pollici (\"42 in\"), questi non sono attualmente supportati da FreeCAD, quindi è sempre meglio avere le dimensioni della pagina SVG specificata in millimetri. L\'attributo \"viewBox\" deve avere lo stesso valore, ad esempio:

 {.html}
viewBox="0 0 1067 762"


-   È necessario inserire, da qualche parte all\'interno del proprio codice svg, dove si desidera che appaia il contenuto del disegno (per esempio alla fine del file, appena prima dell\'ultimo tag</svg>), la seguente riga:

 {.html}



Questo testo sopra (che è in realtà un commento XML) deve essere su una riga separata, e non incorporato nel mezzo di altri pezzi di testo. Attenzione che se si riapre e si salva il modello in Inkscape, dopo aver aggiunto la riga sopra, Inkscape mantiene la riga, ma aggiunge altri elementi XML sulla stessa riga, e di coseguenza il modello non funziona più. È necessario modificarlo con un editor di testo e isolare di nuovo il commento di cui sopra sulla propria riga.

### Namespace


<div class="mw-translate-fuzzy">

### Namespace 

-   Diversi oggetti (in particolare quelli creati con il comando [Draft\_Drawing](Draft_Drawing/it.md), e se il modello ha dei testi modificabili) utilizzano uno speciale [Svg Namespace](Svg_Namespace.md) specifico per FreeCAD. Questo rende FreeCAD in grado di rilevare gli elementi specifici all\'interno di file SVG, che altre applicazioni semplicemente ignorano. Se si prevede di utilizzare uno di questi, è necessario aggiungere questa linea all\'interno del tag di apertura<svg>, ad esempio insieme alle altre righe xml aggiunte da inkscape:


</div>

xmlns:freecad=\"<http://www.freecadweb.org/wiki/index.php?title=Svg_Namespace>\"

### Title block 


<div class="mw-translate-fuzzy">

### Cartiglio

Oltre a queste due regole, a partire da FreeCAD 0.14, al modello possono essere aggiunte le informazioni sul bordo e sul cartiglio. Esse sono usate dallo strumento di proiezione ortogonale e definiscono dove FreeCAD può, e non può effettuare le proiezioni.


</div>

Per definire il bordo dell\'area utilizzata, prima del tag \<metadata nel file svg, deve apparire la seguente riga:

 {.html}



Dove X1, Y1, X2, Y2 sono definiti in questo modo:

-   X1 è la distanza dell\'asse X dal lato sinistro della pagina al lato sinistro del bordo.
-   Y1 è la distanza dell\'asse Y dal lato superiore della pagina al lato superiore del bordo.
-   X2 è la distanza dell\'asse X dal lato sinistro della pagina al lato destro del bordo.
-   Y2 è la distanza dell\'asse Y dal lato superiore della pagina al lato inferiore del bordo.

![](images/XY_Working_v2.svg )

Per definire l\'area della tabella, prima del tag \<metadata e dopo il tag dell\'area di lavoro, si deve inserire la seguente riga:

 {.html}



Dove X1a, Y1a, X2a, Y2a sono definiti come:

-   X1a è la distanza dell\'asse X dal bordo sinistro della pagina al lato sinistro del blocco del titolo.
-   Y1a è la distanza dell\'asse Y dal bordo superiore della pagina al lato superiore del blocco del titolo.
-   X2a è la distanza dell\'asse X dal bordo sinistro della pagina al lato destro del blocco del titolo.
-   Y2a è la distanza dell\'asse Y dal bordo superiore della pagina al lato inferiore del blocco del titolo.
-   X1a \<= X1 oppure X2a \>= X2
-   Y1a \<= Y1 oppure Y2a \>= Y2

![](images/XY_Title_v2.svg )

Il seguente è un esempio del codice che deve essere inserito prima del tag \<metadata per definire l\'area di lavoro e l\'area della tabella. Non è obbligatorio definire una tabella, ma quando si fa la tabella deve essere definita nella riga successiva a quella della definizione dello spazio di lavoro:

 {.html}




Per scalare la stampa, la dimensione effettiva deve essere data negli attributi width e height del tag SVG. Le dimensioni del documento, nelle unità utilizzate (px), deve essere fornita nell\'attributo Viewbox.

In questo caso deve essere formattato come nell\'esempio sottostante dove:

-   xxx = pixel width larghezza
-   yyy = pixel height altezza

 {.html}
width="xxxmm"
height="yyymm"
viewBox="0 0 xxx yyy"



<div class="mw-translate-fuzzy">

-   Nelle squadrature si possono posizionare diversi attributi personalizzati. L\'elenco degli attributi attualmente supportati sono disponibili nella pagina [Svg Namespace](Svg_Namespace/it.md).

-   Di default, i modelli di squadrature, nei sistemi Windows si trovano in *C:/Program Files/FreeCAD0.13/data/Mod/Drawing/Templates/A3\_Landscape.svg*, e nei sistemi Linux in */usr/share/freecad/Mod/Drawing/Templates/A3\_Landscape.svg*.


</div>

## Modelli DXF 


<div class="mw-translate-fuzzy">

Dalla versione 0.15, FreeCAD può esportare in modo affidabile una pagina [Drawing](Drawing_Workbench/it.md) nel formato DXF. Questo sistema utilizza anche i modelli. Se nella stessa cartella del modello SVG utilizzata per una pagina si trova anche un file dxf con lo stesso nome, esso viene utilizzato per l\'esportazione. In caso contrario, viene creato al volo un modello vuoto predefinito.


</div>

Di conseguenza, se si crea i propri modelli SVG, e si vuole essere in grado di esportare in DXF le pagine create con Drawing, è sufficiente creare un modello DXF corrispondente, e salvarlo con lo stesso nome nella stessa cartella.

I modelli DXF possono essere creati con qualsiasi applicazione che produce dei file DXF, come LibreCAD. È quindi necessario modificarli con un editor di testo, e aggiungere due ulteriori righe, una all\'inizio o alla fine della sezione BLOCKS, e un\'altra all\'inizio o alla fine della sezione ENTITIES, che sono il posto dove FreeCAD aggiungerà i propri blocchi e entità.

Un modello molto semplice si presenta così:

    999
    FreeCAD DXF exporter v0.15
    0
    SECTION
    2
    HEADER
    9
    $ACADVER
    1
    AC1009
    0
    ENDSEC
    0
    SECTION
    2
    BLOCKS
    $blocks
    0
    ENDSEC
    0
    SECTION
    2
    ENTITIES
    $entities
    0
    ENDSEC
    0
    EOF

Il modello precedente non contiene alcuna entità. Se si crea il file DXF con un\'applicazione CAD, ci sarà probabilmente molto più contenuto all\'interno delle sezioni HEADER, BLOCKS e ENTITIES.

Le due righe cercate da FreeCAD sono \"\$blocks\" e \"\$entities\". Esse devono essere esistenti nel modello, e devono essere posizionate sulla loro riga. Si può scegliere di metterle subito dopo le righe BLOCKS o ENTITIES, che è più facile (basta utilizzare la funzione \"cerca\" del vostro editor di testo per trovarle), o alla fine, prima delle righe \"0 ENDSEC\" (fate attenzione che ce n\'è una per ogni sezione, assicurarsi di usare quella relativa a BLOCKS e ENTITIES). Quest\'ultimo metodo mette gli oggetti di FreeCAD dopo gli oggetti definiti nel modello, che potrebbe essere più logico.

## Modelli A3 


<div class="mw-translate-fuzzy">

### A3 Classic: 

<img alt="" src=images/A3_Classic.svg  style="width:800px;">


</div>

<img alt="" src=images/A3_Classic.svg  style="width:800px;">


<div class="mw-translate-fuzzy">

### A3 Clean: 

<img alt="" src=images/A3_Clean.svg  style="width:800px;">


</div>

<img alt="" src=images/A3_Clean.svg  style="width:800px;">


<div class="mw-translate-fuzzy">

### A3 Modern: 

<img alt="" src=images/A3_Modern.svg  style="width:800px;">


</div>

<img alt="" src=images/A3_Modern.svg  style="width:800px;">


<div class="mw-translate-fuzzy">

### A3 Showcase: 

<img alt="" src=images/A3_Showcase.svg  style="width:800px;">


</div>

<img alt="" src=images/A3_Showcase.svg  style="width:800px;">


<div class="mw-translate-fuzzy">

### A3 Landscape english: 

<img alt="" src=images/A3_Landscape_english.svg  style="width:800px;">


</div>

<img alt="" src=images/A3_Landscape_english.svg  style="width:800px;">

## Modelli A4 

### A4 Landscape english: 

<img alt="" src=images/A4_Landscape_english.svg  style="width:800px;">

### A4 Portrait 1 english: 

<img alt="" src=images/A4_Portrait_1_english.svg  style="width:400px;">

## Modelli US Letter 

### US Letter landscape: 

<img alt="" src=images/US_Letter_landscape.svg  style="width:800px;">

### US Letter portrait: 

<img alt="" src=images/US_Letter_portrait.svg  style="width:400px;">

### US Letter ds Landscape: 

<img alt="" src=images/US_Letter_ds_Landscape.svg  style="width:800px;">

### US Legal ds Landscape: 

<img alt="" src=images/US_Legal_ds_Landscape.svg  style="width:800px;">

### US Ledger ds Landscape: 

<img alt="" src=images/US_Ledger_ds_Landscape.svg  style="width:800px;">

### Altri standard disponibili 

-   [Modelli ANSI](ANSI_templates/it.md): conformi allo standard [ANSI](http://en.wikipedia.org/wiki/American_National_Standards_Institute) del American National Standards Institute
-   [Modelli Arch](Arch_templates/it.md): conformi allo standard [Arch](http://en.wikipedia.org/wiki/American_National_Standards_Institute) del American National Standards Institute
-   [Modelli misti](Misc_templates/it.md)


{{Drawing Tools navi

}} 

[Category:Developer Documentation](Category:Developer_Documentation.md) [Category:Documentation](Category:Documentation.md)
