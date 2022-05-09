---
- GuiCommand   */it
   Name   *Std_DependencyGraph
   Name/it   *Grafico delle dipendenze
   Empty   *1
   MenuLocation   *Strumenti → Grafico delle dipendenze...
   Workbenches   *Tutti
---

# Std DependencyGraph/it


</div>

## Descrizione

Il **Grafico delle dipendenze** mostra sotto forma di grafico le dipendenze tra gli oggetti presenti nel documento attivo. A differenza della [Vista ad albero](Tree_view/it.md), gli oggetti sono elencati in ordine cronologico inverso, con il primo oggetto creato situato nella parte inferiore.


<div class="mw-translate-fuzzy">

Può essere utile per analizzare un documento di FreeCAD e localizzare le biforcazioni nell\'albero della struttura. L\'aspetto grafico delle dipendenze dipende da quale ambiente di lavoro è stato utilizzato per creare gli oggetti presenti nel documento. Ad esempio, un modello realizzato esclusivamente nell\'ambiente [PartDesign](PartDesign_Workbench/it.md) dovrebbe visualizzare un grafico delle dipendenze lineare con un singolo ramo verticale. Un modello realizzato con operazioni [Parte](Part_Workbench/it.md) ha molti rami, ma per avere una sola parte questi rami devono confluire in un unico elemento collocato in cima dopo le [operazioni booleane](Part_Boolean/it.md). Se non lo fanno, vuol dire che ci sono degli oggetti separati.


</div>

Il grafico delle dipendenze è uno strumento di pura visualizzazione, quindi non può essere modificato, Si aggiorna automaticamente se vengono apportate delle modifiche al modello.

<img alt="" src=images/Std_DependencyGraph_example.svg  style="width   *400px;"> 
*Esempio di grafico delle dipendenze con un corpo di PartDesign a sinistra e un oggetto creato con le operazioni di Parte a destra*

## Installazione

Per utilizzare il grafico delle dipendenze, si deve prima installare un software di terze parti chiamato [Graphviz](http   *//graphviz.org/). Se Graphviz non è installato in precedenza o è installato in una posizione non convenzionale, FreeCAD visualizza il seguente dialogo   *

![](images/FreeCAD-0.17-missing-Graphviz-error-dialogue.png )

### Windows


<div class="mw-translate-fuzzy">

Scaricare l\'installatore **graphviz-2.xx.msi** dalla pagina [Graphviz Download](https   *//graphviz.gitlab.io/_pages/Download/Download_windows.html) e lanciarlo per eseguire l\'installazione.


</div>

### Mac/OSX


<div class="mw-translate-fuzzy">

È possibile installare graphviz usando [Homebrew](https   *//brew.sh/)   *


</div>


{{Code|lang=text|code=
brew install graphviz
}}


<div class="mw-translate-fuzzy">

Questo installa i binari graphviz in /usr/local/bin. Purtroppo non è possibile esplorare quella posizione direttamente dalla finestra di dialogo sui file che si apre con **Strumenti → Grafico delle dipendenze...**.

Quando si ottiene la finestra di selezione dei file utilizzare i tasti Cmd+Shift+G per ottenere un campo di input per il percorso. Inserire


</div>


{{Code|lang=text|code=
/usr/local/bin
}}

or


{{Code|lang=text|code=
/opt/homebrew/bin
}}

poi confermare il campo di immissione e la finestra di dialogo di selezione dei file.

Nel caso in cui i binari di Graphviz non siano installati nella posizione standard, cercare di trovare il programma con il comando


{{Code|lang=text|code=
type dot
}}

Uscirà qualcosa di simile


{{Code|lang=text|code=
dot is /usr/local/bin/dot
}}

Quindi si può dire a FreeCAD di cercare in quella directory.

### Linux

Sulla maggior parte delle distribuzioni Linux (Debian/Ubuntu, Fedora, OpenSUSE), è sufficiente installare il pacchetto graphviz dai repository. Nel caso in cui i binari di Graphviz non siano installati nella posizione standard, cercare di trovare il programma con il comando   *


{{Code|lang=text|code=
type dot
}}

Può produrre qualcosa di simile


{{Code|lang=text|code=
dot is /usr/local/bin/dot
}}

Quindi si può dire a FreeCAD di cercare in quella directory.

## Utilizzo


<div class="mw-translate-fuzzy">

1.  Andare nel menu **Strumenti → Grafico delle dipendenze...**.
2.  Nella [vista principale](Main_view_area/it.md) si apre una nuova finestra dal titolo **Grafico delle dipendenze**.
3.  Utilizzare la rotellina del mouse per ingrandire o rimpicciolire il grafico.
4.  Utilizzare il dispositivo di scorrimento orizzontale nella parte inferiore dello schermo per scorrere la vista lateralmente.


</div>

## Salva

È possibile salvare un grafico delle dipendenze   *

1.  Assicurarsi che la scheda del grafico delle dipendenze sia in primo piano.
2.  Selezionare l\'opzione **File → [Salva](Std_Save/it.md)** o **File → [Salva con nome](Std_SaveAs/it.md)** dal menu.
3.  Immettere un nome per il file e selezionare il tipo di file (\*.png, \*.bmp, \*.gif, \*.jpg, \*.svg or \*.pdf).
4.  Premere il pulsante **Salva**.

## Principi generali 


<div class="mw-translate-fuzzy">

-   Il grafico mostra gli oggetti in ordine cronologico inverso, dal basso verso l\'alto.
-   La direzione delle frecce che mostrano le dipendenze dovrebbe sempre puntare verso il basso, dall\'oggetto figlio all\'oggetto genitore. Una freccia rivolta verso l\'alto indica una dipendenza ciclica, ed è un problema che deve essere risolto.
-   Uno schizzo che contiene collegamenti a una [geometria esterna](Sketcher_External/it.md), oltre alla freccia che lo collega al suo genitore, ha un numero con un suffisso \'x\' e mostra il numero della geometria esterna collegata nello schizzo.
-   Gli oggetti possono avere dipendenze da più genitori. Ad esempio, per un modello costruito in [PartDesign](PartDesign_Workbench/it.md), una Tasca può essere collegata al suo Schizzo e alla funzione Pad che lo precede.
-   Le dipendenze non consentite (ad esempio tra un\'operazione di [Draft](Draft_Workbench/it.md) o [Part](Part_Workbench/it.md) e un elemento all\'interno di un [Corpo di PartDesign](PartDesign_Body/it.md)) sono visualizzate con una freccia rossa. Questo tipo di collegamento mostra in genere un errore \'Links go out of allowed scope\' nella [vista reportvista](Report_view/it.md) report.
-   Un [Contenitore Part](Std_Part/it.md) e un [Corpo PartDesign](PartDesign_Body/it.md) racchiudono il loro contenuto all\'interno di una cornice con uno sfondo colorato a caso. Anche la loro origine racchiude il suo contenuto (piani e assi standard) in una cornice.
-   Un [Gruppo](Std_Group/it.md) viene visualizzato come un singolo elemento collegato al suo contenuto.


</div>

## Limitazioni


<div class="mw-translate-fuzzy">

-   Il grafico delle dipendenze non è di aiuto con problemi causati dal problema della [denominazione topologica](topological_naming_problem/it.md). Se uno schizzo scambia le facce di una funzione dopo una modifica, esso è ancora collegato alla funzione. Anche se alcune funzioni sono interrotte, il grafico delle dipendenze rimane invariato.


</div>


<div class="mw-translate-fuzzy">





</div>


{{Std Base navi

}} 

[Category   *3rd Party](Category_3rd_Party.md)



---
![](images/Right_arrow.png) [documentation index](../README.md) > [3rd Party](Category_3rd Party.md) > Std DependencyGraph/it
