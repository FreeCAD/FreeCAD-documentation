---
 GuiCommand:
   Name: Std_DependencyGraph
   Name/it: Grafico delle dipendenze
   MenuLocation: Strumenti , Grafico delle dipendenze...
   Workbenches: Tutti
   SeeAlso: Std_ExportDependencyGraph/it
---

# Std DependencyGraph/it



## Descrizione

Il **Grafico delle dipendenze** mostra sotto forma di grafico le dipendenze tra gli oggetti presenti nel documento attivo. A differenza della [Vista ad albero](Tree_view/it.md), gli oggetti sono elencati in ordine cronologico inverso, con il primo oggetto creato situato nella parte inferiore.

Può essere utile per analizzare un documento di FreeCAD e localizzare le biforcazioni nell\'albero della struttura. L\'aspetto grafico delle dipendenze dipende da quale ambiente di lavoro è stato utilizzato per creare gli oggetti presenti nel documento. Ad esempio, un modello realizzato esclusivamente nell\'ambiente [PartDesign](PartDesign_Workbench/it.md) dovrebbe visualizzare un grafico delle dipendenze lineare con un singolo ramo verticale. Un modello realizzato con operazioni [Part](Part_Workbench/it.md) ha molti rami, ma per avere una sola parte questi rami devono confluire in un unico elemento collocato in cima dopo le [operazioni booleane](Part_Boolean/it.md). Se non lo fanno, vuol dire che ci sono degli oggetti separati.

Il grafico delle dipendenze è uno strumento di pura visualizzazione, quindi non può essere modificato, Si aggiorna automaticamente se vengono apportate delle modifiche al modello.

<img alt="" src=images/Std_DependencyGraph_example.svg  style="width:400px;"> 
*Esempio di grafico delle dipendenze con un corpo di PartDesign a sinistra e un oggetto creato con le operazioni di Parte a destra*



## Installazione

Per utilizzare il grafico delle dipendenze, si deve prima installare un software di terze parti chiamato [Graphviz](https://graphviz.org/). Se Graphviz non è installato in precedenza o è installato in una posizione non convenzionale, FreeCAD visualizza il seguente dialogo:

![](images/FreeCAD-0.17-missing-Graphviz-error-dialogue.png )

### Windows

Scaricare il programma di installazione **graphviz-2.xx** dalla [Graphviz Download page](https://graphviz.org/download/#windows) ed eseguirlo per l\'installazione. Alcune versioni precedenti sembrano avere problemi nella visualizzazione del grafico; la versione 2.38 e successive sono note per essere affidabili. E\' possibile trovare tutte le versioni di graphviz su [Gitlab](https://gitlab.com/graphviz/graphviz/-/releases).

### macOS

E\' possibile installare Graphviz usando [Homebrew](https://brew.sh/) avendo macOS Big Sur (11) (o superiore). Durante l\'installazione di Homebrew, non innervosirsi, se macOS chiede di installare aggiornamenti, ad es. per gli strumenti della riga di comando Xcode. Questi aggiornamenti vengono eseguiti successivamente dal processo di installazione.


{{Code|lang=text|code=
brew install graphviz
}}

Questo installa i binari di Graphviz in **/usr/local/bin** per macOS su Intel, o **/opt/homebrew** per macOS su Apple Silicon/ARM. FreeCAD dovrebbe trovare automaticamente queste posizioni. Se il programma Graphviz non viene trovato, verrà chiesto di specificare un percorso. Sfortunatamente non è possibile navigare direttamente al programma nella finestra di dialogo del file che appare da **Strumenti → Grafico delle dipendenze...**. Ci sono due opzioni: E\' possibile usare la combinazione di tasti Cmd+Maiusc+. per mostrare gli elementi nascosti. Oppure è possibile utilizzare la combinazione di tasti Cmd+Maiusc+G per ottenere un campo di input per il percorso. Inserire uno di questi percorsi nel [Terminal](https://en.wikipedia.org/wiki/Terminal_(macOS)):


{{Code|lang=text|code=
/usr/local/bin
}}

oppure:


{{Code|lang=text|code=
/opt/homebrew/bin
}}

poi confermare il campo di immissione e la finestra di dialogo di selezione dei file.

Nel caso in cui i binari di Graphviz non siano installati nella posizione standard, cercare di trovare il programma con il comandoː


{{Code|lang=text|code=
type dot
}}

Uscirà qualcosa di simileː


{{Code|lang=text|code=
dot is /usr/local/bin/dot
}}

Quindi si può dire a FreeCAD di cercare in quella directory.

Se non si ha macOS Big Sur (11) (o superiore) Homebrew potrebbe non funzionare, ma è possibile utilizzare [MacPorts](https://www.macports.org/index.php). Basta scaricare la [versione appropriata per il proprio sistema operativo](https://www.macports.org/install.php). Una volta completata l\'installazione, inserire questo comando nel [Terminal](https://en.wikipedia.org/wiki/Terminal_(macOS)):


{{Code|lang=text|code=
sudo port install graphviz
}}

Inserire la propria password e attendere mentre le dipendenze vengono scaricate e installate (può richiedere del tempo).

I binari di Graphviz possono trovarsi in **/usr/local/bin** o **/opt/local/bin/dot**. FreeCAD potrebbe trovare automaticamente il programma Graphviz con la finestra di dialogo del file che viene visualizzata da **Strumenti → Grafico delle dipendenze...**, in caso contrario immettere questo comando:


{{Code|lang=text|code=
type dot
}}

Uscirà qualcosa di simileː


{{Code|lang=text|code=
dot is /opt/local/bin/dot
}}

E si può dire a FreeCAD di cercare in quella directory come spiegato prima.

È anche possibile rendere visibile la directory opt con questo comando:


{{Code|lang=text|code=
defaults write com.apple.finder AppleShowAllFiles YES;
}}

poiː


{{Code|lang=text|code=
killall Finder /System/Library/CoreServices/Finder.app;
}}

Pertanto si puoò dire a FreeCAD di seguire questo percorso. È stato testato con successo su macOS 10.13 (High Sierra).

### Linux

Sulla maggior parte delle distribuzioni Linux (Debian/Ubuntu, Fedora, OpenSUSE), è sufficiente installare il pacchetto Graphviz dai repository. Tuttavia, analogamente a macOS, nel caso in cui i binari di Graphviz non siano installati nella posizione standard, cercare di trovare il programma con il comando:


{{Code|lang=text|code=
type dot
}}

Può produrre qualcosa di simile


{{Code|lang=text|code=
dot is /usr/local/bin/dot
}}

Quindi si può dire a FreeCAD di cercare in quella directory.



## Utilizzo

1.  Andare nel menu **Strumenti →  <img src="images/Std_DependencyGraph.svg" width=16px> Grafico delle dipendenze...**.
2.  Nella [vista principale](Main_view_area/it.md) si apre una nuova finestra dal titolo **Grafico delle dipendenze**.
3.  Utilizzare la rotellina del mouse per ingrandire o rimpicciolire il grafico.
4.  Utilizzare il dispositivo di scorrimento orizzontale nella parte inferiore dello schermo per scorrere la vista lateralmente. In alternativa tenere premuto il pulsante sinistro del mouse e muoverlo.



## Salva

È possibile salvare un grafico delle dipendenze:

1.  Assicurarsi che la scheda del grafico delle dipendenze sia in primo piano.
2.  Selezionare l\'opzione **File → [Salva](Std_Save/it.md)** o **File → [Salva con nome](Std_SaveAs/it.md)** dal menu.
3.  Immettere un nome per il file e selezionare il tipo di file (\*.gv, \*.png, \*.bmp, \*.gif, \*.jpg, \*.svg or \*.pdf).
4.  Premere il pulsante **Salva**.



## Principi generali 

-   Il grafico mostra gli oggetti in ordine cronologico inverso, dal basso verso l\'alto.
-   La direzione delle frecce che mostrano le dipendenze dovrebbe sempre puntare verso il basso. Una freccia rivolta verso l\'alto indica una dipendenza ciclica, ed è un problema che deve essere risolto.
-   Uno schizzo che contiene collegamenti a una [geometria esterna](Sketcher_External/it.md), oltre alla freccia che lo collega al suo genitore, ha un numero con un suffisso \'x\' e mostra il numero della geometria esterna collegata nello schizzo.
-   Gli oggetti possono avere dipendenze da più genitori. Ad esempio, per un modello costruito in [PartDesign](PartDesign_Workbench/it.md), una Tasca può essere collegata al suo Schizzo e alla funzione Pad che lo precede.
-   Le dipendenze non consentite (ad esempio tra un\'operazione di [Draft](Draft_Workbench/it.md) o [Part](Part_Workbench/it.md) e un elemento all\'interno di un [Corpo di PartDesign](PartDesign_Body/it.md)) sono visualizzate con una freccia rossa. Questo tipo di collegamento mostra in genere un errore \'Links go out of allowed scope\' nella [vista reportvista](Report_view/it.md) report.
-   Un [Contenitore Part](Std_Part/it.md) e un [Corpo PartDesign](PartDesign_Body/it.md) racchiudono il loro contenuto all\'interno di una cornice con uno sfondo colorato a caso. Anche la loro origine racchiude il suo contenuto (piani e assi standard) in una cornice.
-   Un [Gruppo](Std_Group/it.md) viene visualizzato come un singolo elemento collegato al suo contenuto.





{{Std_Base_navi

}}



---
⏵ [documentation index](../README.md) > [3rd_Party](Category_3rd_Party.md) > Std DependencyGraph/it
