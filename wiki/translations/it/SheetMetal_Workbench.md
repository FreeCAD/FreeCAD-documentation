# SheetMetal Workbench/it
}

<img alt="Sheet Metal External workbench icon" src=images/Sheetmetal_workbench_icon.svg  style="width:128px;">


{{TOCright}}



## Introduzione

<img alt="" src=images/Sheetmetal_workbench_icon.svg  style="width:32px;"> [Sheet Metal](SheetMetal_Workbench.md) è un [ambiente esterno](External_workbenches.md) e non appartiene all\'installazione standard di FreeCAD. È stato sviluppato per fornire strumenti per realizzare e dispiegare oggetti in lamiera.

Le caratteristiche degli oggetti in lamiera sono:

-   Hanno uno spessore costante
-   Possono essere dispiegati, se sono fatti solo di pareti piane e connessioni cilindriche

Lo strumento di svolgimento in entrambe le sue versioni non è limitato alle parti fatte con gli strumenti di questo banco di lavoro, ma può gestire anche oggetti degli ambienti [Part](Part_Workbench.md) e [PartDesign](PartDesign_Workbench.md), purché soddisfino le caratteristiche di cui sopra.

<img alt="" src=images/SheetMetal_Example.png  style="width:600px;"> 
*Il modello in lamiera costruito con l'addon Sheet Metal; di fronte, il solido dispiegato; in primo piano, lo schizzo aperto con linee di piegatura per l'esportazione in DXF.*

Se l\'esportazione in DXF viene utilizzata per controllare una macchina (ad esempio Lasercut), è necessario modificare il DXF per rimuovere le linee che mostrano le pieghe, perché queste linee potrebbero essere utilizzate come linee di taglio dalla macchina.



## Installazione

Questo ambiente di lavoro può essere installato da [Addon Manager](Std_AddonMgr/it.md). Per l\'installazione manuale vedi [Installare ulteriori ambienti di lavoro](Installing_more_workbenches/it.md).



## Strumenti

È possibile trovare una descrizione dettagliata degli strumenti [sul blog dell\'autore](http://theseger.com/projects/2015/06/sheet-metal-addon-for-freecad/). Attualmente è un po\' datato, dato che sono stati aggiunti alcuni nuovi strumenti.

-   <img alt="" src=images/SheetMetal_AddBase.svg  style="width:32px;"> [Make Base Wall](SheetMetal_AddBase/it.md):Crea un oggetto base in lamiera da uno schizzo, un profilo o un piatto.

-   <img alt="" src=images/SheetMetal_AddWall.svg  style="width:32px;"> [Make Wall](SheetMetal_AddWall/it.md): Aggiunge una flangia su ogni bordo selezionato di una piastra di base. (La flangia può essere trasformata in un risvolto modificando il suo angolo).

-   <img alt="" src=images/SheetMetal_Extrude.svg  style="width:32px;"> [Extend Face](SheetMetal_Extrude/it.md): Estende una lastra di lamiera in corrispondenza di una faccia del bordo selezionata lungo la sua normale. (Aggiungendo uno schizzo di contorno può essere utilizzato per creare una geometria ad incastro.)

-   <img alt="" src=images/SheetMetal_AddFoldWall.svg  style="width:32px;"> [Fold a Wall](SheetMetal_AddFoldWall/it.md): Piega una faccia su una linea scelta con un raggio di curvatura specificato.

-   <img alt="" src=images/SheetMetal_Unfold.svg  style="width:32px;"> [Unfold](SheetMetal_Unfold/it.md): Appiattisce un oggetto in lamiera piegata e genera un solido non piegato e uno schizzo di contorno con linee di piegatura (fornisce un dialogo per impostare i parametri).

-   <img alt="" src=images/SheetMetal_UnattendedUnfold.svg  style="width:32px;"> [Unattended Unfold](SheetMetal_UnattendedUnfold.md): Appiattisce un oggetto in lamiera piegata e genera un solido non piegato e uno schizzo di contorno con linee di piegatura (se i parametri sono già stati impostati).

-   <img alt="" src=images/SheetMetal_AddCornerRelief.svg  style="width:32px;"> [Add Corner Relief](SheetMetal_AddCornerRelief/it.md): Aggiunge rilievo ad un angolo.

-   <img alt="" src=images/SheetMetal_AddRelief.svg  style="width:32px;"> [Make Relief](SheetMetal_AddRelief/it.md): 1° passo per convertire un oggetto shell in un oggetto in lamiera spiegabile, aggiunge un rilievo (ritaglio) ad un angolo.

-   <img alt="" src=images/SheetMetal_AddJunction.svg  style="width:32px;"> [Make Junction](SheetMetal_AddJunction/it.md): 2° passo per convertire un oggetto shell in un oggetto di lamiera spiegabile, crea una giunzione aperta sul bordo di due facciate.

-   <img alt="" src=images/SheetMetal_AddBend.svg  style="width:32px;"> [Make Bend](SheetMetal_AddBend/it.md): 3° passo per convertire un oggetto a shell in un oggetto in lamiera spiegabile, sostituisce gli spigoli vivi con curve rotonde.

-   <img alt="" src=images/SheetMetal_SketchOnSheet.svg  style="width:32px;"> [Sketch On Sheet metal](SheetMetal_SketchOnSheet/it.md): Esegue una foratura basata su uno schizzo lungo le pareti piegate di un oggetto in lamiera.

-   <img alt="" src=images/SheetMetal_Forming.svg  style="width:32px;"> [Make Forming in Wall](SheetMetal_Forming/it.md): Imprime forme con o senza fori in una lastra di metallo.



## Descrizione breve 

Questo ambiente di lavoro fornisce strumenti per i due compiti principali:

-   Creare oggetti di lamiera
-   Dispiegare oggetti di lamiera

Questa sezione ha lo scopo di dare un\'idea approssimativa di come usare gli strumenti forniti. Informazioni più dettagliate possono essere trovate sulla pagina di ogni strumento (vedi sopra) o nei tutorial collegati (vedi sotto).



### Creare un oggetto in lamiera 



#### Iniziare con un profilo 

1.  Crea una polilinea aperta(preferibilmente con lo sketcher)
2.  Utilizzare il comando <img alt="" src=images/SheetMetal_AddBase.svg  style="width:16px;"> [Make Base Wall](SheetMetal_AddBase/it.md) per creare un profilo di lamiera.



#### Iniziare con una lamiera grezza 

1.  Crea una polilinea chiusa (preferibilmente con lo sketcher)
2.  Utilizzare il comando <img alt="" src=images/SheetMetal_AddBase.svg  style="width:16px;"> [Make Base Wall](SheetMetal_AddBase.md) per creare una lamiera grezza.

#### Start with a PartDesign Pad 

1.  Create a closed polyline (preferably with the sketcher)
2.  Use the <img alt="" src=images/PartDesign_Pad.svg  style="width:16px;"> [PartDesign Pad](PartDesign_Pad.md) command to create a prismatic body.
3.  The <img alt="" src=images/PartDesign_Thickness.svg  style="width:16px;"> [PartDesign Thickness](PartDesign_Thickness.md) command will make it an object of constant thickness.
4.  To make it unfoldable it needs some gaps or connections between the walls:
    1.  The <img alt="" src=images/SheetMetal_AddRelief.svg  style="width:16px;"> [Make Relief](SheetMetal_AddRelief.md) command will cut off selected corners.
    2.  The <img alt="" src=images/SheetMetal_AddJunction.svg  style="width:16px;"> [Make Junction](SheetMetal_AddJunction.md) command will create junctions with gaps between adjoining walls that need to be disjoined.
    3.  The <img alt="" src=images/SheetMetal_AddBend.svg  style="width:16px;"> [Make Bend](SheetMetal_AddBend.md) command will create cylindrical connections for the remaining walls that need to stay joined.

Some parameters will be inherited from the parent object(s) but it is better to check the relevant parameters at each stage.

It should now be checked if the resulting sheet metal object can be unfolded. (see [Unfold\...](#Unfold_a_sheet_metal_object.md) below).

#### Adding more features 

The unfoldable basic sheet metal objects can be extended:

1.  Use the <img alt="" src=images/SheetMetal_Extrude.svg  style="width:16px;"> [Extend Face](SheetMetal_Extrude.md) command to enlarge walls.
2.  The <img alt="" src=images/SheetMetal_AddWall.svg  style="width:16px;"> [Make Wall](SheetMetal_AddWall.md) command will add new flanges or hems to the existing object.
3.  Use the <img alt="" src=images/SheetMetal_AddCornerRelief.svg  style="width:16px;"> [Add Corner Relief](SheetMetal_AddCornerRelief.md) command to add or reshape corner reliefs.
4.  The <img alt="" src=images/SheetMetal_AddFoldWall.svg  style="width:16px;"> [Fold a Wall](SheetMetal_AddFoldWall.md) command will fold a wall at a chosen line, i.e. it will trimm a wall at said line, relocate the cut away side, and rejoin them with a cylindrical connection.
5.  Use the <img alt="" src=images/SheetMetal_SketchOnSheet.svg  style="width:16px;"> [Sketch on Sheet metal](SheetMetal_SketchOnSheet.md) command to cut holes into the object starting on a chosen wall and then following the adjoined walls and connections.
6.  The <img alt="" src=images/SheetMetal_Forming.svg  style="width:16px;"> [Make Forming in Wall](SheetMetal_Forming.md) command will stamp a shape into a plate (wall).

:   

    :   After the creation of a WallForming feature the SheetMetal object is **no longer unfoldable**!

Several tools from other workbenches can be used to add holes or to reshape edges.

### Unfold a sheet metal object 

To unfold a sheet metal object activate the <img alt="" src=images/SheetMetal_Unfold.svg  style="width:16px;"> [Unfold](SheetMetal_Unfold.md) or the <img alt="" src=images/SheetMetal_UnattendedUnfold.svg  style="width:16px;"> [Unattended Unfold](SheetMetal_UnattendedUnfold.md) tool.

The result will be a 3D object with an optional outline sketch including bend lines.

### Examples

Until tutorial pages are available on this wiki there is an [Examples](SheetMetal_Examples.md) page.

<img alt="" src=images/SheetMetal_Example-01.png  style="width:100px;"> <img alt="" src=images/SheetMetal_Example-02.png  style="width:100px;"> <img alt="" src=images/SheetMetal_Example-03.png  style="width:100px;"> <img alt="" src=images/SheetMetal_Example-04.png  style="width:100px;"> <img alt="" src=images/SheetMetal_Example-05.png  style="width:100px;">

It contains some hints about [properties](SheetMetal_Examples#SheetMetal_properties.md) as well.



## Limitazioni

-   Il workbench è influenzato dal problema della [denominazione topologica](Glossary#Topological_Naming.md) inerente a FreeCAD. Se una modifica di una piega precedente nella cronologia della parte rinomina le facce, le piegature successive potrebbero essere influenzate e cambiare le facce. Se le funzioni di piegatura non si interrompono, si può fare doppio clic su di esse per ottenere una finestra di dialogo in cui è possibile selezionare la faccia corretta nella vista 3D e aggiornare la Piegatura.
-   Lo strumento Unfold ha alcune limitazioni e fallisce in alcune situazioni complesse. Quando fallisce, provare a selezionare una faccia diversa.
-   Caso frequente di crash: prendere tutte le precauzioni per non tagliare le cerniere (le pieghe) né lungo le facce o negli angoli e per non fare fori o tacche negli angoli.



## Tutorial


<div class="mw-collapsible mw-collapsed toccolours" style="width:800px">

### Sheet Metal Tutorial by meme2704 

Il seguente tutorial è riprodotto dal tutorial in PDF menzionato nei [Link](#Link.md).


<div class="mw-collapsible-content">



#### Presentazione dell\'ambiente di lavoro 

Dopo aver scaricato e installato l\'estensione, aprirla. ![](images/sm1.png )

#### 1st operation 

-   Creare la base: usare gli ambienti \"Part\" o \"Draft\", creare uno schizzo che contenga tutti i fori e qualsiasi taglio, estrudere questa base allo spessore corrispondente allo spessore del foglio di lamiera.
-   Tenere presente che i bordi saranno sempre delle aggiunte, così come i raggi di piegatura.

![](images/sm2.png )

#### 2nd operation 

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

#### Unfolding

Scegliere una faccia di riferimento (qui la faccia arancione) e fare clic sul pulsante nella barra degli strumenti.
Si ottiene la parte blu in cui è sufficiente modificare i valori X, Y o Z per vederla completamente.
![](images/sm6.png ) 

#### Tagliare i lembi a 45° 

Dopo aver piegato i lembi senza averne ritratto nessuno, la forma appare così. ![](images/sm7a.png ) Per poter fare ciò, si deve dividere i lembi a 45° (o seguendo le bisettrici per larghezze non uguali).
\* Creare un nuovo schizzo correlato alla parte comune dei due lembi.

-   Creare un arresto collegato selezionando il bordo esterno della \"cerniera\".
-   Disegnare un triangolo la cui cima è vincolata all\'arresto, orientare un lato a 45°, dare al lato corto una larghezza minima (0,1 mm è sufficiente) e creare una tasca.

Fare attenzione a non graffiare la \"cerniera\" dove la nudità lega la punta del triangolo al bordo della linea di piegatura. ![](images/sm8a.png ) Dispiegatura ![](images/sm9.png ) 

#### Bordi e lembi forati 

Realizzare questi fori e tagli dopo la piegatura e prima della dispiegatura.
Fare sempre attenzione a non \"graffiare\" le linee di piegatura.
![](images/sm10.png ) 

#### Realizzare lembi metallici 

Fare una piega sul bordo del lato, a 45° di 0,1 mm di lunghezza, poi un\'altra piega reversa a 45° della lunghezza del lembo contiguo, quindi estendere il lato opposto, un limbo passa sopra all\'altro e non vengono uniti.
![](images/sm11.png ) 

#### Caso speciale di questo bordo forato 

In questo caso particolare, il dispiegamento funziona solo scegliendo la faccia gialla come riferimento.
![](images/sm12.png ) 

#### Caso speciale foro a cavallo tra le pieghe 

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

## Videos

-   [I\' legante ambiente di lavoro per la lamiera](https://www.youtube.com/watch?v=xidvQYkC4so) di Joko Engineering



## Link


<div class="mw-translate-fuzzy">

-   [Macro Sheet Metal Unfolder](Macro_Sheet_Metal_Unfolder.md), la macro originale su cui si basa lo strumento Unfold.
-   [Sheet Metal Workbench](https://forum.freecadweb.org/viewtopic.php?t=11303) presentazione sul forum di FreeCAD
-   [Un tutorial in inglese e francese in formato PDF](https://forum.freecadweb.org/viewtopic.php?f=3&t=25002) nel forum di FreeCAD
-   File:
-   Segnalazione di bug o richieste di funzioni: <https://github.com/shaise/FreeCAD_SheetMetal/issues>


</div>



## Riferimenti


<div class="mw-translate-fuzzy">

-   Autori:
    -   Strumenti di piegatura: Copyright 2015-2018 by Shai Seger
    -   Strumenti per dispiegare: Copyright 2014 by Ulrich Brammer
-   Licenza: [GPLv3](https://www.gnu.org/licenses/gpl-3.0.en.html)
-   Blog ufficiale: [Sheet metal Addon for FreeCAD](http://theseger.com/projects/2015/06/sheet-metal-addon-for-freecad/)
-   Codice sorgente su github: <https://github.com/shaise/FreeCAD_SheetMetal>


</div>



---
![](images/Right_arrow.png) [documentation index](../README.md) > [SheetMetal](Category_SheetMetal.md) > [Addons](Category_Addons.md) > [External Command Reference](Category_External Command Reference.md) > SheetMetal Workbench/it
