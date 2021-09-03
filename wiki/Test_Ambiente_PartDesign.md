
{{VeryImportantMessage|This section is work in progress, for test. For now only in Italian.
There are no links that direct to this page.
Sezione in costruzione.}}

# PartDesign e i suoi strumenti {#partdesign_e_i_suoi_strumenti}


{{TOCright}}

## Descrizione

Part Design mette a disposizione gli strumenti per modellare delle parti solide complesse basate su dei disegni 2D. Non è un doppione di Part, è un ambiente pensato per lavorare su del materiale.
Di solito, in PartDesign la forma finale viene ottenuta lavorando una forma iniziale. Sovente, sia la forma iniziale che le lavorazioni sono realizzate utilizzando dei semplici disegni di base prodotti con l\'ambiente [Sketcher](Sketcher_Workbench/it.md), ma si possono usare anche altri flussi di lavoro.

### Gli strumenti di PartDesign {#gli_strumenti_di_partdesign}

Gli strumenti dell\'ambiente PartDesign sono tutti situati nel \'\'\'Menu PartDesign \'\'\' che viene visualizzato quando si carica questo modulo.

#### Gli strumenti di costruzione {#gli_strumenti_di_costruzione}

Sono gli strumenti per creare gli oggetti solidi o rimuovere del materiale da un oggetto solido esistente.

-   <img alt="" src=images/PartDesign_Pad.svg  style="width:32px;"> [Prisma](PartDesign_Pad/it.md): Estrude lo schizzo selezionato - Questo strumento utilizza un disegno selezionato come input (lo \"schizzo scelto\") per produrre un Pad. Ad esempio, se viene selezionato uno schizzo che contiene due cerchi concentrici e su di esso si usa lo strumento Pad si ottiene un tubo. Le estrusioni sono realizzate [normali](http://en.wikipedia.org/wiki/Surface_normal) al piano su cui giace lo schizzo.

Un Pad è una protuberanza realizzata estrudendo uno schizzo di base. (questa denominazione viene utilizzata per distinguere le operazioni realizzate con questo strumento da quelle realizzate con lo strumento \"estrusione\" di Part).

-   <img alt="" src=images/PartDesign_Pocket.svg  style="width:32px;"> [Scavo](PartDesign_Pocket/it.md): Crea uno scavo o tasca da uno schizzo selezionato, ad es. un foro in una pistra. Lo schizzo deve essere posizionato sulla superficie di un oggetto solido. Gli scavi si realizzano [normali](http://en.wikipedia.org/wiki/Surface_normal) al piano dello schizzo. Si può stabilire il verso e la profondità.
-   <img alt="" src=images/PartDesign_Revolution.svg  style="width:32px;"> [Rivoluzione](PartDesign_Revolution/it.md): Crea un solido ruotando un disegno attorno ad un asse. Per ottenere un oggetto solido, il disegno deve avere un profilo chiuso. Numerose opzioni consentono di regolare e orientare la rotazione.
-   <img alt="" src=images/PartDesign_Groove.svg  style="width:32px;"> [Scanalatura](PartDesign_Groove/it.md): Crea una scanalatura ruotando uno schizzo attorno ad un asse. Il disegno deve essere mappato sulla faccia di un oggetto solido.

#### Gli strumenti di modifica {#gli_strumenti_di_modifica}

Sono gli strumenti per modificare gli oggetti esistenti.

-   <img alt="" src=images/PartDesign_Fillet.svg  style="width:32px;"> [Raccordo](PartDesign_Fillet/it.md): Raccorda (arrotonda) i bordi di un oggetto. Prestare attenzione alle differenze con il [Raccordo dell\'ambiente Parte](Part_Fillet/it.md)
-   <img alt="" src=images/PartDesign_Chamfer.svg  style="width:32px;"> [Smusso](PartDesign_Chamfer/it.md): Smussa i bordi di un oggetto. Non deve essere confuso con lo [smusso di Part](Part_Chamfer/it.md).
-   <img alt="" src=images/PartDesign_Draft.svg  style="width:32px;"> [Sformo](PartDesign_Draft/it.md): Applica uno sformo angolare alle facce di un oggetto.

#### Gli strumenti di trasformazione {#gli_strumenti_di_trasformazione}

Sono gli strumenti per trasformare gli elementi esistenti.

-   <img alt="" src=images/PartDesign_Mirrored.svg  style="width:32px;"> [Rifletti](PartDesign_Mirrored/it.md): Operazione di simmetria su un piano o una faccia. Produce una copia di una operazione originale riflessa rispetto a un determinato piano.
-   <img alt="" src=images/PartDesign_LinearPattern.svg  style="width:32px;"> [Schiera lineare](PartDesign_LinearPattern/it.md): Crea una schiera lineare di elementi.
-   <img alt="" src=images/PartDesign_PolarPattern.svg  style="width:32px;"> [Schiera polare](PartDesign_PolarPattern/it.md): Crea una schiera polare di elementi.
-   <img alt="" src=images/PartDesign_Scaled.png  style="width:32px;"> [Scala](PartDesign_Scaled/it.md): Scala gli elementi in un formato differente.
-   <img alt="" src=images/PartDesign_MultiTransform.svg  style="width:32px;"> [MultiTrasformazione](PartDesign_MultiTransform/it.md): Permette di creare una trasformazione con qualsiasi combinazione delle altre trasformazioni.

#### I disegni di base {#i_disegni_di_base}

Per vedere come creare gli schizzi di base fare riferimento alla pagina dedicata a [Sketcher](Sketcher_Workbench/it.md).

Torna a [Esercitazioni](Esercitazioni.md) 

[Category:User Documentation/it](Category:User_Documentation/it.md)
