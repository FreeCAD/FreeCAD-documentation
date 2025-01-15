# Flamingo Workbench/it
**Flamingo Workbench (Python2/Qt4) è stato sostituito da Dodo Workbench (Python3/Qt5). Questa pagina wiki evidenzia le differenze tra questi due ambienti. I link indicati qui si riferiscono all'attuale [Dodo](Dodo_Workbench/it.md).**

## Introduzione

Questo ambiente è un insieme di comandi e oggetti personalizzati di FreeCAD che aiutano principalmente a velocizzare il disegno di strutture e tubazioni.



:   L\'ambiente \"*Flamingo*\" è dedicato alle versioni che utilizzano la sintassi di Python\>2.7 e il toolkit Qt4.





:   L\'ambiente \"*Dodo*\" è per Python \>3.6 e Qt5.



Per comodità gli strumenti di Flamingo e Dodo sono raggruppati in tre barre di strumenti/menu, più un set di utilità.

![](images/flamingoBlob.png )

![](images/dodoBlob.png )

  - **Frame tools**: strumenti struttura che hanno lo scopo di posizionare strutture, travi e simili in FreeCAD usando gli oggetti Structure del modulo Arch. \.../flamingo/tutorials/tutorialFrame.pdf

  - **Pype tools**: strumenti tubazione che sono la continuazione logica dello strumento Frame poiché si occupano della creazione di condutture e strutture tubolari. Questo gruppo dispone inoltre di proprie classi Python per creare gli oggetti tubazioni, come tubi, gomiti, flange, ecc. \.../flamingo/tutorials/tutorialPype2.pdf

  - **Eagle tools**: è fondamentalmente un\'aggiunta, e una scorciatoia, al molto professionale ambiente [FreeCAD-PCB](https://github.com/marmni/FreeCAD-PCB) (disponibile anche nel repository aggiuntivo di FreeCAD) to import position of objects from a .brd Eagle\'s file on a PCB drawn in FreeCAD with the a.m. workbench relating only on their names. È anche l\'origine, per estensione, del nome dell\'intero workbench. \.../flamingo/tutorials/tutorialEagle.pdf

  - **Utils** è una barra degli strumenti fornisce alcune funzionalità per interrogare gli oggetti nel modello e la loro distanza, per spostare o ruotare il piano di lavoro e una scorciatoia alla finestra di dialogo per la creazione di [Draft Wire](Draft_Wire/it.md) del modulo Draft, che consente di modificare la posizione del piano di lavoro al volo.

## Riferimenti

-   Autore: oddtopus
-   Codice sorgente in github:

<https://github.com/oddtopus/flamingo>

<https://github.com/oddtopus/dodo>

## Installazione

Questo ambiente può essere installato dall\'[Addon Manager](Std_AddonMgr/it.md). Per una installazione manuale vedere [Installare ulteriori ambienti di lavoro](Installing_more_workbenches/it.md).

## Strumenti Frame 


<div class="center" style="width: auto; margin-left: auto; margin-right: auto;">

![](images/Flamingos_frame2.jpg )


</div>


:   1\) Place one-beam over one-edge (class frameIt). Posiziona una-trave su un-segmento

Dato un oggetto trave e una linea nel modello, questo strumento posiziona la trave sulla linea selezionandoli uno dopo l\'altro fino a quando non si preme ESC.

:   2\) Fill the frame (class fillFrame). Riempi la struttura

Finestra di dialogo per creare su più spigoli selezionati nella vista le travi del tipo scelto in precedenza tra quelli presenti nel modello.

Con il pulsante **Select** è possibile modificare il tipo di trave.


**Dodo: nel dialogo "Insert framebranch" questa funzione è stata sostituita con il pulsante "Add single"**


:   3\) Insert a path (class insertPath). Inserisci un percorso

Strumento per creare un DWire (polilinea o percorso) continuo sul percorso definito da bordi selezionati nella vista, anche se questi non si toccano o si intersecano o appartengono a oggetti diversi. L\'unico vincolo è che esista l\'intersezione tra due spigoli successivi, nell\'ordine in cui sono stati selezionati. Al DWire vengono anche date le proprietà di visualizzazione di una linea centrale, cioè arancione e tratteggiata.

:   4\) Insert Std. Sections (class insertSection). Inserisci sezioni standard

Finestra di dialogo per creare il set di profili da utilizzare nel modello per l\'oggetto FrameLine.

-   **Section** lista: include tutte le sezioni definite nel file .csv corrispondente al tipo di sezione selezionato.
-   **Section types** elenco: i tipi di profili definiti con i file .csv inclusi nella cartella / tabelle
-   **Insert** pulsante: crea il gruppo \"Profiles_set\", se non già esistente, e aggiunge ad esso l\'oggetto del profilo selezionato.

Possono essere create altre tabelle profili aggiungendo il file .csv pertinente nella cartella / tabelle. Le regole per creare o personalizzare tali tabelle sono simili a quelle per le pipe lines.

Nel modello possono essere disegnati altri profili e poi trascinati all\'interno del gruppo \"Profili_set\".

L\'orientamento dei DWire può influenzare il rendering delle travi.


**Dodo: la portata di questa funzione è cambiata.
In dodo si apre una finestra di dialogo dalla quale è possibile creare 10 sagome per sezione trave con dimensioni personalizzate:
* quadrato vuoto e pieno
* cerchio vuoto e pieno
* T, I, C, L, Z
* omega
È anche possibile cambiare la posizione del centro o modificare una sezione esistente.**


:   5\) FrameLine manager (class FrameLineManager). Gestore di Frame Line

Come per gli oggetti \"pype-line\", questa è una finestra di dialogo per creare e modificare le proprietà degli oggetti \"frame-line\".

Analogamente a quanto visto sopra, le frame-lines sono oggetti che raccolgono le proprietà comuni a un insieme di travi (ovvero sono la sezione delle travi) che sono incluse in un gruppo comune nell\'albero del modello. Hanno anche una proprietà opzionale \". Base\", per impostazione predefinita impostata su Nessuna, che è la linea centrale delle travi della struttura. Dopo che viene definito un percorso (un DWire o uno Sketch), alias .Base, alla frame-line possono essere aggiunte altre travi ma verranno eliminate quando viene richiamato **Redraw**. La finestra di dialogo fornisce le seguenti funzioni:

-   un elenco di profili di travi precedentemente inclusi nel modello dalla finestra di dialogo \"Inserisci sezioni standard\" (leggere più avanti);
-   una casella combinata per selezionare il FrameLine attivo tra quelli già creati o  per crearne uno nuovo;
-   una casella di testo in cui scrivere il nome della FrameLine che verrà creata; se non viene inserito nulla o \"\", FrameLined sarà denominato come predefinito \"Telaio00n\";
-   **Insert** pulsante: crea un nuovo oggetto FrameLine o aggiunge nuovi membri a quello selezionato nella casella combinata se nella vista attiva ci sono bordi selezionati.
-   **Redraw** pulsante: crea nuove travi e le posiziona sul percorso selezionato. Le nuove travi verranno raccolte all\'interno del gruppo di FrameLine. Non crea o aggiorna le travi aggiunte a FrameLine al di fuori del percorso definito.
-   **Clear** pulsante: cancella tutte le travi nel gruppo FrameLine. Si applica anche alle travi aggiunte a FrameLine al di fuori del suo percorso definito.
-   **Get Path** pulsante: assegna il Dwire selezionato all\'attributo Path dell\'oggetto FrameLine.
-   **Get Profile** pulsante: modifica l\'attributo Profilo dell\'oggetto FrameLine su quello della trave selezionata nella vista o quella selezionata nell\'elenco.
-   **Copy profile** checkbox: se spuntato genera un nuovo oggetto profilo per ogni trave al fine di evitare riferimenti multipli nel modello.
-   **Move to origin** checkbox: se selezionato, sposta il centro di massa del profilo all\'origine del sistema di coordinate: ciò fa coincidere la linea centrale della trave con il c.o.m. del profilo.

Se il nome di un oggetto FrameLine viene modificato, anche il nome del gruppo pertinente cambia automaticamente ma non viceversa

:   6\) FrameBranch manager

Simile alla funzione analoga nel menu Pype, questo è un contenitore per travi strutturato su una .Base. La base può essere un DWire, uno Sketch o anche i bordi di una forma solida. Quando viene modificata la base sottostante, anche la posizione e la lunghezza delle travi vengono modificate di conseguenza. È possibile tagliare o estendere a qualsiasi geometria le travi e ruotare le sezioni intorno alla linea centrale attraverso i comandi forniti nella finestra di dialogo: in questo modo la modifica non viene persa quando il documento viene ricalcolato.

-   **OK** crea un FrameBranch sulla geometria preselezionata.
-   **Cancel** chiude la finestra di dialogo.
-   la casella di testo **** consente di inserire un nome personalizzato per la funzione.
-   la **combo box** consente di selezionare il tipo di sezione che viene visualizzato nel **list box**. (vedere ../Mod/flamingo/shapes o ../Mod/dodo/shapez to customize).
-   **AddBeams** aggiunge un membro alla struttura sul bordo attualmente selezionato. Il bordo deve appartenere a un framebranch esistente.
-   **RemoveBeams** rimuove la trave selezionata dal bordo corrispondente.
-   **ChangeProfile** cambia i profili nel framebranch. Per selezionare il framebranch basta selezionare nell\'area di visualizzazione uno dei suoi membri.
-   **Get targets** seleziona la geometria nell\'area della vista per tagliarla o estenderla alle travi. I target possono anche non appartenere a nessun framebranch.
-   **Trim/Extend** cambia la lunghezza dei membri selezionati fino ai target.
-   **Add single** crea una trave di una data ****, non collegata alla base su qualsiasi bordo o superficie selezionata.
-   **Redraw** ricrea la struttura, cancellando tutti gli offset e le rotazioni.

Quando viene selezionata una trave appartenente a un framebranch nell\'area di visualizzazione, TAIL (la coda) viene evidenziata visivamente. Ciò consente di modificare manualmente gli offset di coda e di testa, oltre alla rotazione della sezione, utilizzando i comandi forniti nella finestra di dialogo.

:   7\) Spin beams by 45 deg. (class spinSect). Ruota le travi di 45 gradi

Strumento per ruotare un oggetto di 45 gradi attorno all\'asse \"Z\" della sua forma.

:   8\) Reverse orientation (class reverseBeam). Orientamento inverso

Strumento per ruotare un oggetto di 180 gradi attorno all\'asse \"X\" della sua forma. Note: se viene selezionato un bordo dell\'oggetto, tale bordo viene utilizzato come perno di rotazione.

:   9\) Shift the beam (class shiftBeam). Sposta la trave

Finestra di dialogo per traslare e copiare oggetti.

**X**, **Y** e **Z** caselle di testo per l\'immissione diretta della quantità di traslazione in ciascuna direzione.

**Multiple** è la casella di testo per indicare il coefficiente multiplicativo della quota di traslazione.

**Steps** è la casella di testo per il denominatore dell\'importo della quota di traslazione. Viene utilizzata quando la quota di traslazione deve essere coperta con diversi passi.

**Get displacement** è il pulsante per prelevare la quantità e la direzione della traslazione dalla distanza delle entità selezionate (punti, bordi, facce) o anche da un singolo bordo. In quest\'ultimo caso, viene visualizzata una freccia verde per mostrare la direzione.

**OK** per eseguire l\'azione e **Cancel** per chiudere la finestra di dialogo.

:   13\) Rotate + mate the edges (class rotJoin). Ruota + accoppia i bordi

Strumento per traslare e ruotare le travi per accoppiare due bordi. Come sopra ma rende anche i bordi co-lineari.

:   10\) pivotTheBeam (class pivotBeam). Pivotta la trave

Finestra di dialogo per ruotare una trave o un altro oggetto attorno a uno dei suoi bordi

**Angle** casella di testo per inserire i gradi della rotazione.

**Reverse** per ruotare nella direzione opposta, se necessario.

**OK** per eseguire l\'azione e **Cancel** per chiudere la finestra di dialogo.

:   11\) Flush the surfaces (class levelBeam). Abbina le superfici

Strumento per rendere parallele le facce di due oggetti. In realtà il comando acquisisce e mantiene il livello, rispetta la posizione e l\'orientamento della prima faccia selezionata, il centro di massa di tutte le facce selezionate. Quindi trasla gli oggetti fino a che le facce non sono parallele.

:   12\) Mate the Edges (class alignEdge). Accoppia i bordi

Strumento per accoppiare due bordi paralleli. In realtà il comando sposta gli oggetti lungo la distanza minima del loro bordo selezionato rispetto al primo. Quindi trasla l\'oggetto fino a che i bordi non sono paralleli ed è un buon modo per posizionare gli oggetti nella posizione desiderata. È anche possibile selezionare due bordi degli stessi oggetti. Con questo metodo è possibile spostare rapidamente un oggetto per passi definiti sulla propria geometria.

:   14\) alignFlange (class alignFlange). Allinea la flangia

Finestra di dialogo per ruotare le travi in modo che le loro superfici siano parallele a un piano di riferimento.

È possibile preselezionare la faccia di riferimento prima di invocare il comando.

I tre pulsanti **XY**, **XZ** e **YZ** consentono di scegliere direttamente l\'orientamento dei piani principali come riferimento.

Infine è possibile inserire direttamente il nuovo orientamento delle facce con le tre coordinate della normale e il pulsante **Set normal**.

:   15\) Stretch the beam (class stretchBeam). Stira la trave

Finestra di dialogo per modificare la lunghezza delle travi.

Nella casella di testo scrivere la nuova lunghezza che verrà applicata alle travi o ai tubi selezionati. Altrimenti, il pulsante **Get Length** acquisisce la nuova lunghezza dalla geometria selezionata (la lunghezza di una trave o di un bordo o la distanza tra le entità geometriche).

Con il cursore è possibile modificare la lunghezza scritta nella casella di testo da -100% a + 100%.

I pulsanti radio **Head** e **Tail** consentono di scegliere il lato della trave che verrà modificato.

:   16\) Extend the beam (class extend). Estendi la trave

Finestra di dialogo per estendere una trave fino a un obiettivo selezionato.

Se le entità sono preselezionate prima di chiamare questo comando, la prima entità viene automaticamente presa come destinazione e l\'oggetto ad esso associato viene rimosso dal gruppo di selezione. In ogni caso è possibile cambiare l\'oggetto obiettivo con il pulsante **Select**.

:   17\) Adjust frames\' angle (class adjustFrameAngle). Regola l\'angolo delle strutture

Strumento per regolare l\'angolo tra le travi di strutture. Per capire al meglio come funziona, fare riferimento al tutorial precedente.

## Strumenti Pype 


<div class="center" style="width: auto; margin-left: auto; margin-right: auto;">

![](images/Flamingos_pype2.jpg )


</div>


:   1\) Inserisci un tubo

Apre una finestra di dialogo per inserire i tubi.

La combo in alto a destra è una caratteristica comune per tutte le finestre di dialogo \"Inserisci \...\": elenca gli oggetti della linea pype definiti nel documento corrente: con questo è possibile selezionare a quale linea di tubazioni assegnare le tubazioni appena create. Si può anche lasciarlo su  in modo che l\'oggetto venga creato sulla linea principale dei modelli di parti. Nell\'angolo in alto a sinistra vengono mostrate le caratteristiche del tubo attualmente selezionato, prese dalla casella di riepilogo nella colonna di destra. Le dimensioni dei tubi per ciascun tubo sono definite nel file .csv, dove è possibile aggiungere o modificare in base alle esigenze, rispettando poche semplici regole di denominazione. Curve, riduzioni, ecc. usano le stesse regole per la definizione delle loro tabelle dimensionali: vedere i file in ../Mod/flamingo/Tables. Leggere anche il \"tutorialPype.pdf\" per sapere come personalizzarle o crearle.

Per definire la posizione e l\'orientamento dei tubi, sono possibili le seguenti selezioni:

-   uno o più bordi dritti
-   uno o più bordi curvi
-   uno o più vertici
-   nulla; in questo caso il tubo verrà posizionato all\'origine.

Se non viene specificata alcuna lunghezza, il valore predefinito è 200 unità (solo una lunghezza comoda, in mm).

**Reverse** pulsante consente di ruotare di 180° l\'ultimo tubo creato o quelli attualmente selezionati.

**Apply** pulsante consente di applicare una lunghezza diversa o un diametro nominale ai tubi attualmente selezionati.


**Dodo: aggiunto un menu a torta (scorciatoia da tastiera: "Z") per creare oggetti "pype": questo ha lo scopo di inserire rifiniture più veloci nel disegno**


:   2\) Inserisci una curva

Apre una finestra di dialogo per inserire un gomito.

Oltre ai widget comuni con le altre finestre di dialogo \"Inserisci \...\", il pulsante **Taglia/Estendi** consente di regolare la lunghezza dei tubi selezionati sul bordo selezionato della curva. Per definire la posizione e l\'orientamento sono possibili le seguenti selezioni:

-   un vertice,
-   un bordo circolare
-   un tubo ad una delle sue estremità; in questo caso il diametro e lo spessore della curva si adatteranno automaticamente a quelli del tubo selezionato
-   una coppia di bordi o tubi o travi, anche non contigui ma intersecanti; in questo caso le proprietà della curva si adatteranno automaticamente per connettere i due oggetti selezionati; anche le tubazioni selezionate verranno automaticamente tagliate o estese ai bordi della curva
-   nulla; in questo caso la curva verrà posizionata all\'origine.

Se non viene specificata alcuna angolazione, il valore predefinito è 90 gradi.

:   3\) Inserisci una riduzione

Apre una finestra di dialogo per inserire riduzioni concentriche.

Per definire la posizione e l\'orientamento sono possibili le seguenti selezioni: due tubi paralleli (possibilmente collineari)

-   un tubo ad una delle sue estremità
-   un tubo
-   un bordo circolare
-   un bordo dritto
-   un vertice
-   nulla (creato all\'origine)

Nel caso sia selezionato un tubo, le sue proprietà vengono applicate alla riduzione.

Nel caso in cui siano selezionati due tubi, lo strumento proverà automaticamente a collegarli con il diametro maggiore e minore giusti.

:   4\) Inserisci un tappo

Apre una finestra di dialogo per inserire tappi.

Per definire la posizione e l\'orientamento sono possibili le seguenti selezioni: uno o più bordi curvi (asse e origine al centro) uno o più vertici nulla Se viene selezionato un bordo del tubo, le proprietà del tappo si adatteranno automaticamente a quelle del tubo.

:   2\) Inserisci una valvola

Crea un \"segnaposto\" di una valvola da una tabella .csv come sopra. Oltre alla dimensione di offset, è importante perché definisce anche il coefficiente Kv che verrà utilizzato per calcolare le perdite di carico con lo strumento pertinente nel menu \"Utils\". Notare che il simbolo del segnaposto cambia in base al tipo di valvola, se nel suo nome si trova una parola chiave tipo \"ball\", \"butterfly\" o \"globe\" (\"sfera\", \"farfalla\" o \"palla\").

:   6\) Inserisci una flangia

Apre la finestra di dialogo per inserire le flange. Per definire la posizione e l\'orientamento sono possibili le seguenti selezioni: uno o più bordi curvi uno o più vertici nulla Nel caso sia selezionato un tubo, le sue proprietà vengono applicate alla flangia.

:   7\) Inserisci un bullone a U.

Apre la finestra di dialogo per inserire i bulloni a U.

Per definire la posizione e l\'orientamento sono possibili le seguenti selezioni:

-   uno o più bordi circolari
-   uno o più tubi
-   nulla.

Nel caso sia selezionato un tubo, le sue proprietà vengono applicate al bullone a U. Inoltre, è possibile scegliere di posizionare il cavallotto all\'estremità **Testa** o **Coda** o nel **Mezzo** delle tubature attivando la casella corrispondente.

Con il pulsante **Ref. face** è possibile selezionare la faccia del supporto su cui orientare l\'asse del cavallotto.



*Solo in **Dodo**: i componenti di tubazione sopra possono essere inseriti anche dal menu a torta dedicato.*



:   8\) Gestore PypeLine

Prima di parlare della finestra di dialogo, vale la pena di ricordare che cosa è l\'oggetto pype-line nel contesto dell\'ambiente Flamingo.

Questo oggetto rappresenta una raccolta di oggetti \"PType\" che vengono aggiornati con i metodi definiti nella classe stessa di Python. Al momento attuale crea, con il metodo \"obj.Proxy.update (obj, \[edges\])\", tubi e curve sui bordi dati e li raccoglie in un gruppo chiamato secondo la obj.Label dell\'oggetto. Per le curve viene applicato un raggio di curvatura standard \"3D\" (cioè 1,5xO.D. diametro esterno). Il raggio di piega è una proprietà comune dell\'oggetto pype-line, quindi può essere modificato e quindi ridisegnato. Quando l\'etichetta dell\'oggetto pype-line viene rinominata, il nome del suo gruppo viene modificato di conseguenza.

La classe PypeLine2 ha anche l\'attributo opzionale \".Base\", che rappresenta la linea centrale della tubazione:

-   Se Base è None, PypeLine2 si comporta come un contenitore nudo di oggetti, con possibilità di raggrupparli automaticamente, assegnare un colore ed estrarre l\'elenco delle parti.
-   .Base può essere una polilina o uno Schizzo o qualsiasi oggetto che contiene dei bordi nella sua Forma.
-   Eseguendo \"obj.Proxy.update(obj)\", senza alcun \[edges\], la classe tenta di costruire la pypeline (oggetti Pipe e Gomito) sui bordi \"obj.Base\": per geometrie ben definite questo di solito porta al risultato desiderato. Se vengono assegnati \[edges\], vengono disegnati tubi e curve.
-   Eseguendo \"obj.Proxy.purge(obj)\" si eliminano dal modello tutti i tubi e i gomiti appartenenti alla linea pype-line.
-   Ricordare che l\'oggetto creato al di fuori di .Base non verrà aggiornato quando il .Base viene modificato e la Pypeline viene ridisegnata e (eccetto tubi e curve) non verrà cancellata se la Pype-line viene eliminata.

Capito questo, il comando apre la finestra di dialogo per creare o modificare una tubazione.

La finestra di dialogo è molto simile a quella per inserire altri oggetti visti prima.

Le tabelle delle classificazioni delle tubazioni, dove è definito il valore del diametro esterno O.D. e lo spessore, sono le stesse di quelle per tubi (es. Pipe_SCH-STD.csv).

Quando nella casella combo c\'è  e viene premuto **Insert**, nel documento viene creato un nuovo oggetto pype-line con il gruppo pertinente.

È possibile creare una pipeline in tre modi, in base agli oggetti selezionati nella finestra quando viene premuto Inserisci:

-   nessuna selezione. Viene creata una linea pype con la proprietà .Base = None e inclusa nel suo gruppo con il nome e il colore specificati (o i valori predefiniti). Gli oggetti piping per popolarlo possono essere creati uno a uno con i comandi visti sopra o in alternativa può essere selezionata una linea di mezzeria e gli oggetti possono essere aggiunti successivamente con i pulsanti **Get Profile** e **Redraw**.
-   è selezionato un oggetto DWire. Viene automaticamente preso come Base e convertito in un percorso (arancione, tratteggiato) e i tubi e le curve sono disegnati lungo di esso.
-   viene selezionata una serie di spigoli (anche non contigui ma comunque aventi intersezioni sulle loro estensioni). Viene creato un tracciato che collega tutti i bordi (vedere lo strumento Tracciato nella barra degli strumenti Frame) e assegnato come .Base alla tubazione appena creata. Quindi i tubi e le curve sono disegnati sopra, come prima.

Dopodiché è ancora possibile aggiungere altri oggetti (come Flange, Riduzioni \...) utilizzando i comandi di inserimento pertinenti descritti sopra. Quando gli oggetti vengono creati all\'interno di una tubazione, vengono automaticamente inclusi nel relativo gruppo del modello e vengono applicate le proprietà comuni (ad esempio, O.D., spessore, colore, raggio di curvatura ecc.).

Se nel modello è già presente almeno una pype-line, è possibile selezionarla dalla casella combinata: in questo caso, premendo Insert si creano i tubi e le curve come descritto sopra ma, invece di creare un nuovo oggetto pype-line, li aggiunge alla tubazione esistente selezionata. Attenzione che le tubazioni create in questo modo verranno cancellate al prossimo **Redraw**.

**Get Path**, Get Profile e Color consentono rispettivamente di modificare la proprietà .Base, la dimensione nominale e il colore dell\'oggetto.

**Redraw** ricrea tubi e curve lungo il .Base (se definito) dopo ogni modifica al percorso o alle proprietà della tubazione.

**Part list** genera un file .csv con la distinta base dell\'oggetto piping inclusa nella linea di tubazioni selezionata nella combo

:   9\) Inserisci un PypeBranch

Questo oggetto pype si comporta come un PypeLine tranne che si aggiorna automaticamente ogni volta che la Base (un DWire o un SketchObject) viene modificato: ciò include la modifica del posizionamento, lo stretching, lo spostamento, l\'aggiunta o l\'eliminazione di bordi. È principalmente inteso a rappresentare i rami secondari di una PypeLine (vedere il tutorial dedicato) ma può anche fungere da oggetto autonomo. Questo è una azione importante che consente di modificare rapidamente il layout dei tubi ma, come inconveniente, la sua geometria è definita più rigidamente. In altre parole, i tubi non possono essere suddivisi o ridimensionati in modo indipendente perché saranno eventualmente ridisegnati sulla base. Invece il cambio del diametro esterno OD, dello spessore thk o del raggio di curvatura BendRadius di PypeBranch, si applicherà su tutte le sue valvole e le sue curve.

:   10\) Inserire un serbatoio

[Vedere il tutorial Part 4 (1/2)](#Links.md)

:   11\) Inserisci un percorso di tubi

[Vedere il tutorial Part 4 (2/2)](#Links.md)

:   12\) Interrompere il tubo

Apre una finestra di dialogo per interrompere un tubo in un punto definito, opzionalmente creando uno spazio tra le estremità delle due parti. La selezione multipla è possibile.

Inserisci nella casella di testo **Point** la lunghezza a cui la conduttura o il tubo devono essere interrotti: questo può essere un valore assoluto o solo una percentuale della lunghezza (un numero seguito da %). In alcuni casi è più rapido utilizzare la barra di scorrimento in basso per modificare questo valore.

Il pulsante **Length** consente di misurare la lunghezza del tubo selezionato e usarlo come riferimento della scala della barra di scorrimento.

Se basta solo per spezzare i tubi in due, lasciare la casella di testo **Gap** a 0; altrimenti definire la lunghezza del gap. Se viene scelta una lunghezza di riferimento, anche il gap può essere definito in percentuale. Come visto nel [tutorial](https://github.com/oddtopus/flamingo/blob/master/tutorial), è possibile misurare il divario dalle geometrie nel modello con il pulsante **Get gap**: questa è la distanza tra qualsiasi entità geometrica o anche la lunghezza di un singolo bordo.

Premendo su **Break** si esegue l\'azione.

La combo Pypeline, come al solito, consente di scegliere il gruppo a cui assegnare i nuovi oggetti creati.

:   13\) Accoppia i bordi dei tubi.

Quando vengono selezionati due bordi circolari appartenenti a oggetti diversi, premendo questo pulsante si sposta il secondo oggetto per rendere i bordi concentrici e complanari.

Funziona non solo con i tubi.

:   14\) Unisci i tubi

Unisce le Ports di diversi oggetti in modo grafico. Funziona solo su oggetti pype, anche da diversi workbench, in cui la proprietà Ports\[\] è definita congruentemente.

:   15\) Adatta un gomito

Selezionare 2 tubi intersecanti + 1 curva: eseguendo questo comando essi verranno uniti. Funziona solo su oggetti pype, anche da workbench diversi.

:   16\) Estendi i tubi all\'intersezione

Selezionando due tubi, questo comando li estende entrambi fino al loro punto di intersezione, se esiste.

:   17\) Estendi i tubi all\'intersezione

Selezionando due tubi, questo comando li estende entrambi fino al loro punto di intersezione, se esiste.

:   18\) Posa i tubi

Selezionando una faccia e diversi tubi, questo comando traduce il tubo lungo la normale della faccia per farla giacere sul suo piano.

:   19\) Alza il supporto

Simile allo strumento precedente, ma in questo caso è il supporto che viene sollevato o abbassato, in modo che la faccia sia tangente al tubo.

:   20\) Attacca al tubo

Attacca rigidamente un oggetto pype (2, 3, 4, 5 o 6) all\'estremità più vicina di un tubo (1). Per staccarlo, fare clic sul pulsante mentre l\'oggetto associato è selezionato da solo.

:   21\) Crea tubi da punto a punto

Apre una finestra di dialogo simile a \"Disegna un DWire\" insieme alla finestra di dialogo \"Inserisci un tubo\": ciò consente di disegnare una sequenza di tubi, collegati da curve, selezionando un punto dopo l\'altro. È anche permesso cambiare le proprietà del tubo e/o la tubazione al volo.

:   22\) Inserisci qualsiasi forma

Questo è uno strumento per creare un oggetto \"pype\" da un file .STEP o .IGES o .BREP. Carica il file importato nella proprietà Shape di una FeaturePython.

## Utilità


<div class="center" style="width: auto; margin-left: auto; margin-right: auto;">

![](images/Flamingos_utils.jpg )


</div>


:   1\) Crea un poligono

I primi due strumenti di utilità fanno parte di un progetto separato che mira a creare uno scanner automatico di stanze con un motore passo-passo e un misuratore di distanza ad ultrasuoni. Questo strumento crea un poligono regolare all\'interno di uno schizzo.

:   2\) Poligono da file

Strumento per creare qualsiasi poligono all\'interno di uno schizzo che prelevi i vertici da un file .csv, dove sono memorizzati in coordinate polari.

:   3\) Interroga il modello

Strumento per ottenere varie informazioni in base all\'oggetto o agli oggetti selezionati. Oltre alla lunghezza o alle distanze, è particolarmente adatto per fornire informazioni relative a travi e tubi (lunghezza, sezione, angolazioni).

:   4\) Allinea piano di lavoro

Strumento per impostare la posizione e la rotazione del piano di lavoro in base alla geometria esistente selezionata.

La normale del piano di lavoro è definita analizzando gli elementi nel seguente ordine:

1.  la normale di una faccia
2.  la normale del piano di una curva
3.  la normale del piano contenente due segmenti

L\'origine del piano di lavoro è definita (in ordine) da

1.  un vertice
2.  il centro di curvatura di una linea
3.  l\'intersezione di due linee
4.  il centro di un bordo

:   5\) Offset piano di lavoro

Sposta il piano di lavoro lungo il suo vettore normale. Per mostrare la direzione dell\'offset viene visualizzata sullo schermo una freccia verde temporanea. Chiaramente sono ammessi anche valori negativi.

:   6\) Ruota il piano di lavoro

Ruota il piano di lavoro attorno a uno dei suoi assi. Anche in questo caso viene visualizzata una freccia verde nella finestra per identificare l\'orientamento attuale del piano di lavoro: la freccia è puntata nella direzione Z e la base lunga della freccia è posizionata sopra la direzione X.

:   7\) Disegna un DWire

Questo strumento funziona esattamente come lo strumento corrispondente dell\'ambiente Draft, ma con alcune opzioni aggiuntive alla fine della finestra di dialogo. Come impostazione predefinita, l\'origine del piano di lavoro viene ridefinita ad ogni punto aggiunto poiché ciò semplifica il tracciamento mediante l\'opzione snap-to-grid dei segmenti con lunghezza e orientamento noti. Quindi due pulsanti, richiamati anche con la combinazione di tasti Ctrl+Maiusc+(), consentono di ruotare e sfalsare il piano di lavoro come visto sopra senza interrompere l\'oggetto DWire. Gli ultimi tre pulsanti consentono di modificare rapidamente la rotazione del piano di lavoro per renderlo parallelo ai piani principali.

:   8\) Sposta rapidamente gli oggetti

Per spostare rapidamente qualsiasi parte, ad esempio per accedere agli oggetti sottostanti, questo strumento fornisce una maniglia grafica (freccia verde), e facendo clic su di essa è possibile spostare e ruotare gli oggetti selezionati.

:   9\) Calcola la perdita di carico

Apre una finestra di dialogo per calcolare le perdite di carico attraverso le parti di pype selezionate nel viewport o attraverso un ramo della tubazione, PypeBranch. Viene calcolato il coefficiente di attrito per ciascun tubo dritto e gomito. Per altri oggetti, la perdita di carico concentrata viene calcolata attraverso il fattore di flusso, a condizione che l\'attributo Kv sia disponibile e impostato su un valore positivo.

## Link

-   Forum: [Nuovo ambiente di lavoro per strutture metalliche](http://forum.freecadweb.org/viewtopic.php?f=8&t=17035) (annuncio)
-   Forum: [Flamingo & Dodo workbench(s) discussione](https://forum.freecadweb.org/viewtopic.php?t=22711)
-   Tutorials: [flamingo/tutorials](https://github.com/oddtopus/flamingo/tree/master/tutorials)

-   Video tutorial:
    -   [Semplice tutorial video per la creazione di strutture con tubi](https://www.youtube.com/watch?v=_Or91gdBLMU)
    -   [Part 1: how to created pipe lines](https://www.youtube.com/watch?v=cBj0umlvzAk)
    -   [Part 2: frames, supports, flanges, and imported components](https://www.youtube.com/watch?v=e81PpWY5L00)
    -   [Part 3: drawing one building with four sketches (and a bunch of other features)](https://www.youtube.com/watch?v=IqEccmsg5dU)
    -   [Part 4 (1/2): Pump room layout and piping plan](https://www.youtube.com/watch?v=aPF8SS_1Aqo)
    -   [Part 4 (2/2): Pump room import in building and pipe-route](https://www.youtube.com/watch?v=iGnW88x9bKQ)
-   Reporting bugs:
    -   [Flamingo GitHub issue queue](https://github.com/oddtopus/flamingo/issues)
    -   [Dodo GitHub issue queue](https://github.com/oddtopus/dodo/issues)

## Altri link utili 

-   [Ambienti complementari](External_workbenches/it.md)
-   [Esempi di Macro](Macros_recipes/it.md)
-   [OSE-Piping-Workbench: applicazione per creare ulteriori raccordi per tubi](https://wiki.opensourceecology.org/wiki/OSE_Piping_Workbench)

## Ambienti esterni 

Gli ambienti di lavoro per FreeCAD sono facilmente programmabili in [Python](Python/it.md), quindi ci sono molte persone che stanno sviluppando degli ambienti aggiuntivi al di fuori del codice di base di FreeCAD.

La pagina [Ambienti complementari](external_workbenches/it.md) contiene alcune informazioni e tutorial su alcuni di loro, e il progetto [FreeCAD Addons](https://github.com/FreeCAD/FreeCAD-addons) mira a raccoglierli e renderli facilmente installabili dall\'interno di FreeCAD.

Sono in fase di sviluppo ulteriori nuovi ambienti.



---
⏵ [documentation index](../README.md) > [Addons](Category_Addons.md) > [External Workbenches](Category_External%20Workbenches.md) > Flamingo Workbench/it
