


{{UnfinishedDocu

}} <img alt="Icona dell\'ambiente esterno SheetMetal" src=images/Sheetmetal_workbench_icon.svg  style="width:128px;">

## Descrizione


{{TOCright}}

<img alt="" src=images/Sheetmetal_workbench_icon.svg  style="width:32px;"> **Sheet Metal** è un [ambiente aggiuntivo](external_workbenches/it.md) per progettare e dispiegare parti di lamiera. Non fa parte dell\'installazione standard di FreeCAD.

<img alt="" src=images/SheetMetal_Example.png  style="width:600px;"> 
*Il modello in lamiera costruito con l'addon Sheet Metal; di fronte ad esso, il solido dispiegato; in primo piano, lo schizzo aperto con linee di piegatura per l'esportazione in DXF.*

Se l\'esportazione in DXF viene utilizzata per controllare una macchina (ad esempio Lasercut), è necessario modificare il DXF per rimuovere le linee che mostrano le pieghe, pèrché queste linee potrebbero essere utilizzate come linee di taglio dalla macchina.

## Installazione

Questo ambiente di lavoro può essere installato da [Addon Manager](Std_AddonMgr/it.md). Per l\'installazione manuale vedi [Installare ulteriori ambienti di lavoro](Installing_more_workbenches/it.md).

## Strumenti

È possibile trovare una descrizione dettagliata degli strumenti [sul blog dell\'autore](http://theseger.com/projects/2015/06/sheet-metal-addon-for-freecad/).

-   <img alt="" src=images/SheetMetal_AddBase.svg  style="width:32px;"> [Make Base Wall](SheetMetal_AddBase/it.md): Crea un foglio di lamiera da uno schizzo.

-   <img alt="" src=images/SheetMetal_AddWall.svg  style="width:32px;"> [Make Wall](SheetMetal_AddWall/it.md): Estende una faccia del foglio di lamiera.

-   <img alt="" src=images/SheetMetal_Extrude.svg  style="width:32px;"> [Extend Face](SheetMetal_Extrude/it.md): Estende una faccia lungo la normale.

-   <img alt="" src=images/SheetMetal_AddFoldWall.svg  style="width:32px;"> [Fold a Wall](SheetMetal_AddFoldWall/it.md): Piega una faccia sulla linea scelta con il raggio di curvatura specificato.


<div class="mw-translate-fuzzy">

-   <img alt="" src=images/SheetMetal_Unfold.svg  style="width:32px;"> [Unfold](SheetMetal_Unfold/it.md): Appiattisce l\'oggetto in lamiera piegata e genera un solido e uno schizzo.


</div>

-   <img alt="" src=images/SheetMetal_UnattendedUnfold.svg  style="width:32px;"> [Unattended Unfold](SheetMetal_UnattendedUnfold.md): Flattens folded sheet metal object and generates a solid and a sketch (if parameters have already been set).

-   <img alt="" src=images/SheetMetal_AddCornerRelief.svg  style="width:32px;"> [Add Corner Relief](SheetMetal_AddCornerRelief/it.md): Aggiunge rilievo ad un angolo.

-   <img alt="" src=images/SheetMetal_AddRelief.svg  style="width:32px;"> [Make Relief](SheetMetal_AddRelief/it.md): Aggiunge rilievo a un angolo.

-   <img alt="" src=images/SheetMetal_AddJunction.svg  style="width:32px;"> [Make Junction](SheetMetal_AddJunction/it.md): Crea un vuoto nell\'angolo tra due lati.

-   <img alt="" src=images/SheetMetal_AddBend.svg  style="width:32px;"> [Make Bend](SheetMetal_AddBend/it.md): Piega una faccia sulla linea scelta.

-   <img alt="" src=images/SheetMetal_SketchOnSheet.svg  style="width:32px;"> [Sketch On Sheet metal](SheetMetal_SketchOnSheet/it.md): Crea un foro nella lamiera sulla base di uno schizzo.

-   <img alt="" src=images/SheetMetal_Forming.svg  style="width:32px;"> [Make Forming in Wall](SheetMetal_Forming/it.md): Crea lo strumento di formatura.

## Due strumenti complementari {#due_strumenti_complementari}

### Crea un profilo di base {#crea_un_profilo_di_base}

Strumento a forma di omega: permette di realizzare una parte da una semplice multilinea creata in Sketcher o Draf, dargli altezza e spessore centrati, a sinistra o a destra di questa linea, fare attenzione a non creare autointersezione in pieghe chiuse di spazio minore dello spessore del materiale.

### Piega lungo una linea {#piega_lungo_una_linea}

Piega una piastra di base \"piatta\" lungo una linea (icona formata da un rettangolo barrato da una linea): selezionare la faccia, poi la linea e lo strumento, scegliere l\'angolo, il raggio, il lato; notare che la posizione della piega rispetto alla linea è non molto ben definita; sembra che la linea sia il bordo di intersezione all\'estensione delle 2 facce.

## Limitazioni

-   Il workbench è influenzato dal problema della [denominazione topologica](Glossary#Topological_Naming.md) inerente a FreeCAD. Se una modifica di una piega precedente nella cronologia della parte rinomina le facce, le piegature successive potrebbero essere influenzate e cambiare le facce. Se le funzioni di piegatura non si interrompono, si può fare doppio clic su di esse per ottenere una finestra di dialogo in cui è possibile selezionare la faccia corretta nella vista 3D e aggiornare la Piegatura.
-   Lo strumento Unfold ha alcune limitazioni e fallisce in alcune situazioni complesse. Quando fallisce, provare a selezionare una faccia diversa.
-   Caso frequente di crash: prendere tutte le precauzioni per non tagliare le cerniere (le pieghe) né lungo le facce o negli angoli e per non fare fori o tacche negli angoli.

## Tutorial


<div class="mw-collapsible mw-collapsed toccolours" style="width:800px">

### Sheet Metal Tutorial by meme2704 {#sheet_metal_tutorial_by_meme2704}

Il seguente tutorial è riprodotto dal tutorial in PDF menzionato nei [Link](SheetMetal_Workbench/it#Link.md).


<div class="mw-collapsible-content">

#### Presentazione dell\'ambiente di lavoro {#presentazione_dellambiente_di_lavoro}

Dopo aver scaricato e installato l\'estensione, aprirla. ![](images/sm1.png )

#### Prima operazione {#prima_operazione}

-   Creare la base: usare gli ambienti \"Part\" o \"Draft\", creare uno schizzo che contenga tutti i fori e qualsiasi taglio, estrudere questa base allo spessore corrispondente allo spessore del foglio di lamiera.
-   Tenere presente che i bordi saranno sempre delle aggiunte, così come i raggi di piegatura.

![](images/sm2.png )

#### Seconda operazione {#seconda_operazione}

-   Aprire l\'ambiente Sheet Metal.
-   Selezionare uno spessore del bordo (un bordo) della piastra di base e fare clic sullo strumento \"Piegatura\" (Bend). L\'angolo di piegatura predefinito è di 90°, ma può essere modificato da 0° a 90°.
-   L\'altezza del bordo (lembo piegato) di default è 10 mm, modificabile da 0,1 a xxx mm.
-   Il raggio di curvatura di default è uguale allo spessore della lamiera, ma è modificabile da 0,1 a xx mm (non usare mai 0).
-   Gap1, gap2 sono la distanza del bordo piegato dall\'angolo della base (0 è accettato).
-   Invert default: false piega a Z+, true a ZReliefd taglia l\'angolo tra la piega e la base (inattivo se gap = 0).
-   Reliefw aggiunge una gola di scarico tra la base e il bordo (inattivo se reliefd = 0).

![](images/sm3.png ) Ripetere tante volte quanti sono i lati da piegare.
Piegare un ritorno con l\'uso di \"extend\".
![](images/sm4a.png ) Per aggiungere una piega di ritorno, ripetere la stessa operazione selezionando il bordo dello spessore interessato.
Per ridurre lo spazio tra i 2 bordi, usare \"estends\".
Selezionare lo spessore e specificare la lunghezza da aggiungere.
Notare che se l\'estensione del primo bordo viene effettuata prima della piega di ritorno, essa non viene presa in considerazione; se una piega identica viene aggiunta all\'estensione, essa appare corretta ma il suo dispiegamento non viene eseguito.
Piegatura di un secondo bordo:
Ora bisogna separare i due bordi altrimenti si fondono e il dispiegamento è impossibile.
\* Primo metodo: ritrarre, arretrare, un bordo.

-   -   Dare un valore leggermente maggiore a gap1 (o gap2), a zero c\'è ancora fusione.

-   Secondo metodo, effettuare un taglio a 45°, vedere più avanti la descrizione di come utilizzare questo strumento.

![](images/sm5a.png )

#### Dispiegatura

Scegliere una faccia di riferimento (qui la faccia arancione) e fare clic sul pulsante nella barra degli strumenti.
Si ottiene la parte blu in cui è sufficiente modificare i valori X, Y o Z per vederla completamente.
![](images/sm6.png )

#### Tagliare i lembi a 45° {#tagliare_i_lembi_a_45}

Dopo aver piegato i lembi senza averne ritratto nessuno, la forma appare così. ![](images/sm7a.png ) Per poter fare ciò, si deve dividere i lembi a 45° (o seguendo le bisettrici per larghezze non uguali).
\* Creare un nuovo schizzo correlato alla parte comune dei due lembi.

-   Creare un arresto collegato selezionando il bordo esterno della \"cerniera\".
-   Disegnare un triangolo la cui cima è vincolata all\'arresto, orientare un lato a 45°, dare al lato corto una larghezza minima (0,1 mm è sufficiente) e creare una tasca.

Fare attenzione a non graffiare la \"cerniera\" dove la nudità lega la punta del triangolo al bordo della linea di piegatura. ![](images/sm8a.png ) Dispiegatura ![](images/sm9.png )

#### Perforazione di bordi e lembi {#perforazione_di_bordi_e_lembi}

Realizzare questi fori e tagli dopo la piegatura e prima della dispiegatura.
Fare sempre attenzione a non \"graffiare\" le linee di piegatura.
![](images/sm10.png )

#### Creare dei lembi tangenti {#creare_dei_lembi_tangenti}

Fare una piega sul bordo del lato, a 45° di 0,1 mm di lunghezza, poi un\'altra piega reversa a 45° della lunghezza del lembo contiguo, quindi estendere il lato opposto, un limbo passa sopra all\'altro e non vengono uniti.
![](images/sm11.png )

#### Caso speciale di questo stesso bordo forato {#caso_speciale_di_questo_stesso_bordo_forato}

In questo caso particolare, il dispiegamento funziona solo scegliendo la faccia gialla come riferimento.
![](images/sm12.png )

#### Caso speciale di foro a cavallo delle pieghe {#caso_speciale_di_foro_a_cavallo_delle_pieghe}

In precedenza si è detto più volte che non bisogna tagliare le linee di piegatura.
Come fare ?
![](images/sm13.png )

-   Creare la base con un foro semicircolare e fare le pighe sui due mezzi-lato separatamente.
-   Quindi fare una estensione su uno dei lati della larghezza dell\'apertura meno 0,1 mm, i due bordi rimangono quindi separati.
-   Quindi su questa estensione (in verde) tracciare il contorno del taglio e fare una tasca.
-   Il risultato è il pezzo rosso sopra, e il dispiegamento funziona, rimane la linea che in precedenza separava i due bordi.

![](images/sm14.png )


</div>


</div>


{{TOCright}}

## Link

-   [Macro Sheet Metal Unfolder](Macro_Sheet_Metal_Unfolder.md), la macro originale su cui si basa lo strumento Unfold.
-   [Sheet Metal Workbench](https://forum.freecadweb.org/viewtopic.php?t=11303) presentazione sul forum di FreeCAD
-   [Un tutorial in inglese e francese in formato PDF](https://forum.freecadweb.org/viewtopic.php?f=3&t=25002) nel forum di FreeCAD
-   File:
-   Segnalazione di bug o richieste di funzioni: <https://github.com/shaise/FreeCAD_SheetMetal/issues>

## Riferimenti

-   Autori:
    -   Strumenti di piegatura: Copyright 2015-2018 by Shai Seger
    -   Strumenti per dispiegare: Copyright 2014 by Ulrich Brammer
-   Licenza: [GPLv3](https://www.gnu.org/licenses/gpl-3.0.en.html)
-   Blog ufficiale: [Sheet metal Addon for FreeCAD](http://theseger.com/projects/2015/06/sheet-metal-addon-for-freecad/)
-   Codice sorgente su github: <https://github.com/shaise/FreeCAD_SheetMetal>

## Ambienti esterni {#ambienti_esterni}

Gli ambienti di FreeCAD sono facili da programmare in [Python](Python/it.md), quindi ci sono molte persone che sviluppano ambienti aggiuntivi al di fuori degli sviluppatori principali di FreeCAD.

La pagina [Ambienti complementari](external_workbenches/it.md) contiene alcune informazioni e tutorial su alcuni di loro, e il progetto [FreeCAD Addons](https://github.com/FreeCAD/FreeCAD-addons) mira a raccoglierli e renderli facilmente installabili dall\'interno di FreeCAD.

Sono in fase di sviluppo ulteriori nuovi ambienti.

[Category:SheetMetal{{\#translation:}}](Category:SheetMetal.md) [Category:Addons{{\#translation:}}](Category:Addons.md) [Category:External Command Reference{{\#translation:}}](Category:External_Command_Reference.md)
