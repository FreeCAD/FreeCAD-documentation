# Release notes 0.13/it

 Questo è un riassunto dei cambiamenti più interessanti avvenuti in FreeCAD con la versione più recente. Vedere [qui](http://www.freecadweb.org/tracker/changelog_page.php) per la lista completa delle modifiche.


<div class="mw-translate-fuzzy">

Versioni precedenti: ([0.11 en](Release_notes_0.11.md)) - [0.12](Release_notes_0.12/it.md)


</div>

![800px](images/FreeCAD013.jpg)

*modellato in FreeCAD da psicofil*

## Generale

-   **Preferenze di colore**: siete stufi del tradizionale aspetto predefinito (forme-grige-con-linee-nere) di FreeCAD? Ora è modificabile nelle preferenze utente (menu **Modifica → Preferenze → Visualizzazione → Colori**), insieme a diversi altri colori predefiniti.
-   **Allineamento**: con questo nuovo strumento disponibile nel menu Modifica si possono allineare tra loro due forme utilizzando fino a tre punti.

## Modulo Drawing - Disegno in Proiezione 

-   **Operazione Ritaglio**: Un nuovo oggetto di [Ritaglio](Drawing_Clip/it.md) consente di posizionare le viste di oggetti all\'interno di rettangoli ritagliati nelle pagine di disegno.
-   **Blocchi di titoli editabili**: Durante la progettazione dei [Modelli di squadrature](Drawing_templates/it.md), ora è possibile marcare i testi modificabili. Tali testi diventano quindi direttamente modificabili in FreeCAD.
-   **Operazione Annotazione**: Un nuovo oggetto [Annotazione](Drawing_Annotation/it.md), una semplice funzione per posizionare rapidamente i blocchi di testo in una pagina di disegno.
-   **Viste ortografiche**: Un nuovo strumento [Viste ortogonali](Drawing_Orthoviews/it.md) facilita la creazione di viste multiple tutte allineate tra di loro, secondo la proiezione del primo o del terzo quadrante.
-   **Anteprima Browser**: Dato che il visualizzatore interno SVG di Qt non supporta sempre tutte le funzionalità SVG, questo pulsante consente di controllare come appare una pagina nel browser Webkit il quale supporta pienamente il formato SVG. Questo è provvisorio, fino a quando non viene sostituito definitivamente l\'attuale viewer SVG con Webkit \...
-   **Esportazione DXF**: ora è possibile esportare una vista di una pagina direttamente in un file DXF.
-   Alcune correzioni di bug permettono ora di stampare le pagine in scala.

## Modulo Schizzo 

-   **Creare dei punti**

![](images/Release-0.13-PointTool.png )

I punti possono essere aggiunti e utilizzati come un elemento dello schizzo

-   **Origine dello schizzo**

![](images/Release-0.13-Origin.png )

Ora si può utilizzare sia l\'origine che gli assi dello schizzo per definire la geometria.

-   **Vincoli di tangenza e perpendicolarità per archi e cerchi.**
-   **Vincoli rispetto a una geometria esterna (proiettati).**
-   **Migliorato il conteggio dei gradi di libertà dello schizzo.**
-   **Vincolo di simmetria rispetto ad un punto di simmetria** (vincolo di punto medio).

-   **Migliorie nella visualizzazione delle Etichette dei Dati e dei Vincoli:**

![](images/Release-0.13-SketcherDimensions.png )

-   -   Ogni etichetta di vincolo (comprese le frecce) è scalata correttamente e automaticamente alla dimensione della scena grafica 3D.
    -   Le etichette di testo per Distanza, Distanza X, Distanza Y e Raggio ora possono essere posizionate liberamente e con migliore controllo.
    -   Piccoli miglioramenti per la sovrapposizione delle icone dei vincoli e dei blocchi.
    -   La direzione del testo nelle etichette dei Dati viene invertita quando la vista viene orientata dalla parte opposta.

-   **Gli schizzi completamente vincolati ora vengono evidenziati:**

![](images/Release-0.13-SketcherFullyConstrained.png )

-   -   **Selezione Rubber band:**

![](images/Release-0.13-RubberBandSelection.png )

Le geometrie (punti, linee e curve) possono essere selezionate trascinando il mouse sullo sfondo per creare un rettangolo di selezione.

-   **Ampliamento di funzioni dello strumento polilinea:** con il tasto m si può passare dalla modalità arco alla modalità linea e scegliere tra libero, tangente o perpendicolare rispetto al segmento precedente.

-   **Mappa schizzo su faccia** è un nuovo strumento per mappare (o rimappare) uno schizzo esistente sulla faccia selezionata di un solido. Questo consente l\'uso dello schizzo per funzioni quali Pad e Scavo.

-   **Piccoli miglioramenti:**
    -   Quando si costruisce la geometria, accanto al cursore viene visualizzata la punta dell\'utensile con le relative informazioni.
    -   **Sketch view** which sets the 3D view perpendicular to the sketch plane has now an icon in the Sketcher toolbar.

## Modulo Draft - Disegno 2D 

-   **Modo di lavoro**: Ora, di default, nel modulo Draft è attiva la modalità Vista delle attività (Finestra attività). Se si preferisce la modalità Barra degli strumenti, essa è ancora disponibile nelle impostazioni delle preferenze di Draft (Modifica → Preferenze → Draft → Modalità interfaccia →).
-   **Importatore DXF**: L\'importatore di file .DXF ora supporta i punti (tradotti come [punti di Draft](Draft_Point/it.md)) e le linee (tradotte come [spezzate di Draft](Draft_Wire/it.md))
-   **Nuovo sistema di ancoraggio**: Il [sistema di aggancio](Draft_Snap/it.md) del modulo Draft è stato riscritto quasi completamente. Ora è molto più facile estenderlo e utilizzarlo in altri script o moduli, ora ha nuove icone e nuovi cursori, e dispone di una barra degli strumenti che consente di attivare o disattivare le singole posizioni di blocco o l\'intero sistema di snap.

![800px](images/013-draft-snap.jpg)

-   **Miglioramenti nei vincoli**: Quando si inseriscono i punti 3D, oltre alla funzione **Maiuscola-vincolo** esistente, è possibile limitare il movimento in direzione X, Y o Z premendo i tasti **X**, **Y** o **Z**. Premendoli una seconda volta si disattiva il vincolo.
-   **Conversione Draft \<-\> Schizzo**: L\'ambiente Draft ora offre il nuovo strumento di conversione [Draft2Sketch](Draft_Draft2Sketch/it.md), che converte gli oggetti Draft selezionati (o qualsiasi forma piana) in Schizzi, e viceversa.
-   **Strumento Clona**: Questo pratico strumento serve per creare copie degli oggetti selezionati. Quando l\'originale viene modificato, i cloni vengono automaticamente aggiornati. Il clone può essere spostato, ruotato, e dispone inoltre di una **proprietà scala** che consente di modificare le dimensioni della copia.
-   **Importatore SVG**: L\'importatore SVG ora ha un migliore supporto per le curve di Bezier. La definizione globale del sistema di unità dell\'utente è ora rispettato e la geomtria è scalata correttamente in millimetri. E\' stato aggiunto un supporto per nuovi elementi come ellissi e rettangoli arrotondati. L\'analizzatore è stato rielaborato e ora gestisce i percorsi di Adobe Illustrator.
-   **Angoli arrotondati**: Diversi oggetti di Draft ([Contorni](Draft_Wire/it.md), [Rettangoli](Draft_Rectangle/it.md) e [Poligoni](Draft_Polygon/it.md)) ora hanno la proprietà **Raggio di raccordo** (Fillet Radius), che arrotonda i loro angoli con il valore del raggio di raccordo indicato.

![800px](images/013-draft-fillet.jpg)

-   **Vista 2D dell\'oggetto**: Il nuovo strumento [Shape2DView](Draft_Shape2DView/it.md) permette di posizionare rapidamente nel documento una vista 2D di un oggetto selezionato. È possibile specificare il vettore della proiezione.

![800px](images/013-draft-shape2dview.jpg)

## Modulo Architettura 

-   **Integrazione con Draft**: I moduli **Architettura** e **Draft** ora sono strettamente integrati. Gli strumenti di Arch utilizzano il sistema di [ancoraggio](Draft_Snap/it.md) di Draft, e tutti gli strumenti di Draft sono presenti nell\'ambiente Architettura. Infatti, se si desidera, è possibile disattivare completamente il modulo Draft (Modifica → Preferenze → Draft → Nascondi l\'ambiente Draft).
-   **Nuovo strumento Muro**: Lo strumento [Muro](Arch_Wall/it.md) è stato notevolmente migliorato. Ora dispone di una modalità di disegno diretta, che si attiva quando si preme il pulsante Muro senza alcun oggetto selezionato, questo consente di disegnare i muri come si disegnano semplici linee. Inoltre, ora, quando si aggancia un muro esistente, la connessione tra le pareti è automatica.

![800px](images/013-arch-wall.jpg)

-   **Nuovo strumento Tetto**: Ora nel modulo Architettura è disponibile un nuovo strumento [Tetto](Arch_Roof/it.md) che consente di creare rapidamente tetti inclinati partendo da una faccia selezionata.
-   **Nuovo strumento Finestra**: Le [Finestre](Arch_Window/it.md) ora vengono create direttamente sopra una forma piana che contiene uno o più contorni, come, ad esempio, su un rettangolo o uno schizzo. Se tale forma è stata disegnata direttamente su una faccia di una parete, la finestra taglia la parete e produce automaticamente un\'apertura nel muro.
-   **Nuovo metodo di sezione**: Ora è molto semplice creare piani 2D, sezioni e prospetti del modello. Basta inserire un oggetto [Piano di sezione](Arch_SectionPlane/it.md), orientarlo nel modo desiderato, modificarlo per includere gli oggetti che si devono vedere, ed è fatto!
-   **Nuovo renderizzatore solido**: Oltre al render di contorni 2D basato su OpenCasCADe, utilizzato attualmente dal modulo [Drawing](Drawing_Workbench/it.md), il modulo **Arch** offre ora un nuovo renderer 2D, che è in grado di rendere le facce piene su un foglio di disegno in formato .SVG, producendo delle viste 2D più gradevoli.

![800px](images/013-arch-vrm.jpg)

-   **Importazione IFC con [IfcOpenShell](http://www.ifcopenshell.org)**: Ora il modulo Arch può utilizzare [IfcOpenShell](http://www.ifcopenshell.org) se è installato sul sistema. Questo permette di importare il formato IFC per renderlo molto più potente, e l\'importazione di tutti i contenuti del file IFC è garantita.
-   **Nuovi oggetti di Piano e Costruzione**: Piani e Costruzione ora sono dei gruppi quindi gli oggetti possono essere aggiunti e rimossi con un semplice drag & drop dalla struttura ad albero.
-   **Nuovo sistema di assi**: E\' stato aggiunto un nuovo [Sistema di assi](Arch_Axis/it.md) che permette la disposizione in modo rapido di sistemi di assi complessi. Questi assi possono essere aggiunti agli oggetti [Struttura](Arch_Structure/it.md) e, in questo modo, si propagano automaticamente sui nodi della griglia.

![800px](images/013-arch-axes.jpg)

-   **Oggetti Architettura da oggetti Meshes**: Ora [Muri](Arch_Wall/it.md) e [Strutture](Arch_Structure/it.md) possono essere creati direttamente da oggetti maglia, purché questi siano ​​chiusi, solidi e tutti i bordi siano [manifold](http://doc.spatial.com/index.php/Manifold_and_Non-manifold_Objects). Questo consente di trasformare molto rapidamente le geometrie importate da altre applicazioni, quali [Blender](http://www.blender.org), in oggetti Arch validi.

## Modulo Parte 

-   **Affina la forma** è una nuova utility che pulisce le facce dopo l\'esecuzione di alcune operazioni su una forma. Può essere impostata per essere eseguita automaticamente dopo le operazioni booleane nelle Preferenze.
-   **Nuovo strumento Loft** estrusione modellata, può estrudere un complesso insieme di superfici o una forma solida attraverso una serie di schizzi o oggetti Draft.
-   **Nuovo strumento Sweep** estrusione lungo un percorso, può estrudere un complesso insieme di superfici o una forma solida attraverso una serie di schizzi o di oggetti Draft lungo una traiettoria costituita da uno schizzo, un bordo o un oggetto Draft.
-   **Nuovo strumento Offset** può creare un offset di una superficie o di una forma.
-   **Nuovo strumento Thickness** può produrre una forma solida impostando uno spessore e creare aperture in una o più facce.
-   **Costruzione di forme** e **Creazione di primitive** ora fanno parte della barra degli strumenti e sono rapidamente accessibili.

## Modulo Progettazione Parte 

-   **Estrusione** e **Scavo** ora sono più potenti grazie alla disponibilità di maggiori parametri, come ad esempio estrusione fino al primo, fino all\'ultimo, fino alla faccia, 2 dimensioni, simmetrica al piano.
-   **Smusso** e **Raccordo** sono stati aggiornati: ora è possibile selezionare una faccia e tutti i bordi esterni e interni della faccia vengono elaborati.
-   **Rivoluzione**: ora è possibile usare una linea di costruzione come asse di rivoluzione.
-   **Nuovo strumento Groove**: (scanalatura) asporta del materiale dal solido rivoluzionando uno schizzo.
-   **Linear pattern**, **Polar pattern** e **Multipattern** sono dei nuovi strumenti che consentono di creare e distribuire schiere di estrusioni o di scavi su una forma.
-   **Shaft Wizard** che fornisce asssistenza nella progettazione di alberi.

## Modulo Navale (Ship module) 

-   Nuovo modulo navale ([tutorial](FreeCAD-Ship_s60_tutorial/it.md))

## Mouse 3D 

-   Alla versione per Windows è stato aggiunto il supporto per i mouse 3D (Spaceball, Space Navigator).
-   Nella finestra di dialogo per la personalizzazione la nuova scheda **Motion Spaceball** permette di regolare la precisione del mouse 3D ai parametri che si desidera, direttamente da FreeCAD.

!!FUZZY!!== Modulo OpenSCAD ==

-   Questo nuovo modulo (sperimentale) fornisce la capacità di importare file OpenSCAD in FreeCAD. Questo formato di file è molto popolare nella comunità RepRap e sul sito Thingiverse per condividere disegni digitali.

-   Gli script di OpenSCAD possono essere eseguiti all\'interno di FreeCAD, da OpenSCAD (se è installato), e il risultato appare nel documento FreeCAD.
-   Per ulteriori informazioni consultare la pagina [OpenSCAD](OpenSCAD_Workbench/it.md) nel wiki di FreeCAD.

[Category:News](Category:News.md) [Category:Documentation](Category:Documentation.md) [Category:Releases](Category:Releases.md)
