# Note di rilascio della versione 0.12 

Questo è un riassunto dei cambiamenti più interessanti avvenuti in FreeCAD rispetto alla versione precedente. Vedere [qui](http://www.freecadweb.org/tracker/changelog_page.php) per avere l\'elenco completo delle modifiche.

Versione precedente: [0.11](Release_notes_011/it.md)

\_\_\_TOC\_\_\_

### Benvenuti!

-   Quando si apre FreeCAD per la prima volta, ora si viene accolti da un nuovo fiammante Start Center, che raccoglie le azioni più comuni che si può desiderare di eseguire, come ad esempio aprire un particolare ambiente di lavoro, caricare uno dei file recenti sui quali si è lavorato, leggere le ultime notizie sullo sviluppo di FreeCAD, o guardare uno dei tanti nuovi tutorial video che la operosa comunità di FreeCAD ha prodotto recentemente.

![](images/FreeCAD_start_center.jpg )
=== Schizzo & Progettazione Parti ===

<img alt="" src=images/Rim_bling.png  style="width:800px;">

-   L\'ambiente [Schizzo](Sketcher_Workbench/it.md) - Sketcher è stato notevolmente migliorato con una grande quantità di lavoro rispetto alla versione precedente, ed è ora basato su un nuovo risolutore riprogettato da zero per questo compito. L\'operatore Schizzo è ora in grado di eseguire quasi tutte le operazioni di [Disegno 2D](Draft_Module/it.md) del modulo Draft, e di inserire una vasta gamma di vincoli sugli elementi di schizzo.

-   Inoltre, l\'ambiente [Progettazione Parte](PartDesign_Workbench/it.md) - PartDesign si è molto evoluto e offre diversi strumenti comuni (e totalmente parametrici), per lavorare sugli schizzi, come l\'estrusione, il lofting (estrusione che si avvia su un profilo 2D e si conclude su un diverso profilo 2D, una specie di raccordo tra due profili diversi) o la rivoluzione.

=== Architettura ===

-   Un nuovo modulo di [Architettura](Arch_Module/it.md) fa ora parte di FreeCAD. E\' ancora in fase di sviluppo, ma presenta già alcuni pratici oggetti di utilità, quali i muri e gli elementi strutturali (pilastri e travi). Questi oggetti possono essere costruiti su una geometria 2D esistente, quali linee, contorni e schizzi, specificando una larghezza e un\'altezza, o, in caso di elementi strutturali, partendo da profili 2D. Possono anche essere basati su solidi, o anche includere altre forme solide, sotto forma di aggiunte o anche di sottrazioni, consentendo praticamente qualsiasi geometria possibile.

![](images/Arch_screenshot.jpg )

-   Il modulo Architettura dispone anche di un importatore id [IFC](http://en.wikipedia.org/wiki/Industry_Foundation_Classes), di un importatore ed esportatore di [DAE (collada)](http://en.wikipedia.org/wiki/Collada), e di un esportatore speciale di [OBJ](http://en.wikipedia.org/wiki/Wavefront_.obj_file) più adatto di quelli standard ai modelli di architettura.

-   Incluso nel modulo Architettura vi è anche una collezione crescente di strumenti per facilitare il processo di lavoro con gli oggetti Mesh di altre applicazioni come ad esempio [Blender](http://www.blender.org). Gli oggetti Mesh, se sono ben modellati, possono essere facilmente e automaticamente trasformati in forme semplici (pulite), e poi in oggetti parametrici dell\'ambiente di Architettura.

===Draft - Disegno 2D ===

![](images/Draft_taskview.jpg )

-   Recupera dello spazio di lavoro! Il modulo [Disegno 2D (Draft)](Draft_Module/it.md) dispone ora di una nuova interfaccia utente che utilizza il pannello *finestra delle attività di FreeCAD*, è una finestra che riunisce tutte le interazione con l\'utente in un unico pannello, recuperando lo spazio prezioso occupato dalla barra degli strumenti di Draft. Per attivarla, andare nelle preferenze di Draft e selezionare la modalità **finestra delle attività**.

-   Lo strumento Riduci/Estendi di Draft è ora in grado di estrudere singole facce degli oggetti esistenti.

-   Sono state aggiunte diverse nuove modalità di [ancoraggio](Draft_Snap/it.md) (snap), ora sono possibili agganci perpendicolari e paralleli alle linee esistenti, e agganci a posizioni che sono allineate con altri segmenti di linea.

-   Il modulo Draft dispone anche di un nuovo strumento che produce, all\'interno del documento stesso, una vista in proiezione in 2D di qualsiasi forma 3D.

-   Gli oggetti di Draft ora possono essere disegnati direttamente sopra facce esistenti. Se non si specifica un piano di lavoro, sono adattati temporaneamente alla faccia sottostante.

-   Il modulo Draft è ora in grado di importare le curve di Bézier da file SVG.


{{languages/it | {{en|Release_notes_012}} {{es|Release_notes_012/es}} {{fr|Release_notes_012/fr}} {{pl|Release_notes_012/pl}} {{ru|Release_notes_012/ru}} }}

[Category:News{{\#translation:}}](Category:News.md) [Category:Documentation{{\#translation:}}](Category:Documentation.md) [Category:Releases{{\#translation:}}](Category:Releases.md)
