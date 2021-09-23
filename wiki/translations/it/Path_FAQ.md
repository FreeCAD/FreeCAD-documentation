# Path FAQ/it


## Domande frequenti su Path 


<div class="mw-translate-fuzzy">

### Quanti assi può gestire l\'ambiente Path? 


</div>

Al momento, per la versione 0.18, Path Workbench può gestire fino a 3 assi di fresatura. Attualmente, le funzioni del 4° asse sono in fase di sviluppo per la prossima versione ufficiale, e con alcune operazioni di Path già aggiornate allo stato base del 4° asse.

[top](#top.md)


<div class="mw-translate-fuzzy">

### Perché sembra che, in alcuni casi, il workbench Path offra più di un modo per specificare un\'operazione? 


</div>

Il workbench Path fornisce gli strumenti esistenti per soddisfare molte operazioni di fresatura, altri sono in corso di realizzazione e poiché FreeCAD è open source, non c\'è nulla che impedisca a qualsiasi utente di creare le proprie funzioni.

Come nel caso della modellazione 3D, sono spesso disponibili più metodi utilizzabili per le diverse operazioni lavorazioni. Si tratta di scegliere tra quelli più vantaggiosi. In alcuni casi vengono utilizzate delle combinazioni di operazioni per fornire la fresatura completa del pezzo.

Un esempio comune è, ad esempio, il taglio di contornatura può essere generato da bordi o facce. In alcuni casi può essere vantaggioso optare per un tipo di input geometrico rispetto ad un altro.

[top](#top.md)


<div class="mw-translate-fuzzy">

### Perché la modifica di un\'operazione di Ottimizzazione cambia la posizione nel flusso di lavoro della lavorazione mostrato nell\'elenco delle operazioni? 


</div>

Tutte le aggiunte alla lavorazione, comprese le modifiche e le copie di operazioni, vengono aggiunte alla fine del flusso di lavoro del lavoro. Se ciò interrompe la sequenza corretta della lavorazione, essa deve essere riordinata nell\'editor della Lavorazione -\> scheda Flusso di lavoro.

[top](#top.md)


<div class="mw-translate-fuzzy">

### Qual è la differenza tra altezza libera e altezza di sicurezza? 


</div>

Informazioni dettagliate sono disponibili in [ Profondità e Altezze](Template:Depths/Heights/it.md).

[top](#top.md)


<div class="mw-translate-fuzzy">

### Qual è l\'uso tipico del foglio di lavorazione? 


</div>

Il SetupSheet è un foglio di calcolo dedicato, contenuto in una lavorazione, modificabile nelle Proprietà vista, accessibile solo dal workbench Path. Fornisce un meccanismo che consente agli utenti più esperti di configurare gli aspetti della lavorazione utilizzando i valori e le espressioni contenute nel SetupSheet.

Gli ingressi correnti per Profondità, Altezza e Gestione utensile includono:

1.  Final Depth Expression \-- OpFinalDepth \-- Espressione della profondità finale dell\'operazione
2.  Start Depth Expression \-- OpStartDepth \-- Espressione della profondità iniziale dell\'operazione
3.  Step Down Expression \-- Il valore predefinito è dato da OpToolDiameter. Questa espressione viene utilizzata per ciascuna operazione per calcolare il valore di default di Step down (profondità della passata) in base al diametro dello strumento definito nel controller dello strumento associato.
4.  Clearance Height Expression \-- StartDepth+SetupSheet.ClearanceHeightOffset \-- Profondità iniziale + Offset di sorvolo
5.  Clearance Height Offset Value \-- Contiene il valore utilizzato nella precedente Espressione
6.  Safe Height Expression \-- StartDepth+SetupSheet.SafeHeightOffset \-- Profondità iniziale + Offset di sicurezza
7.  Safe Height Offset Value \-- Contiene il valore utilizzato nella precedente espressione Espressioni
8.  Horizontal Rapid Value \-- Fornisce il valore predefinito utilizzato per popolare inizialmente la velocità di avanzamento rapido orizzontale per tutti i controller degli utensili.
9.  Vertical Rapid Value \-- Fornisce il valore predefinito utilizzato per compilare inizialmente la velocità di avanzamento rapido verticale per tutti i controller degli utensili.

Questo fornisce flessibilità. Ad esempio, le espressioni sono fornite predefinite, ma possono essere sovrascritte dall\'utente. La modifica può anche ridurre l\'equazione di default a un valore se questo è utile all\'utente.

[top](#top.md)


<div class="mw-translate-fuzzy">

### Qual è l\'uso tipico dei modelli di lavorazione? 


</div>

I modelli di lavorazione consentono di salvare da una lavorazione le definizioni utilizzate comunemente e di riutilizzarle in successive lavorazioni configurate in modo simile.

[top](#top.md)


<div class="mw-translate-fuzzy">

### Quanti oggetti di base supporta il workbench Path? 


</div>

Esiste solo il supporto per un singolo oggetto Base. Per creare percorsi per più solidi in una singola Lavorazione, si può creare un Compound e utilizzarlo come oggetto base per la lavorazione.

[top](#top.md)


<div class="mw-translate-fuzzy">

### Perché un\'operazione non produce output utilizzabili? 


</div>

Esistono una serie di motivi che possono la causa per cui una singola operazione non genera output.

Un motivo frequente è che la geometria dell\'utensile definita nel controller dell\'utensile selezionato per l\'operazione è troppo grande per adattarsi alla geometria selezionata sul modello 3D per l\'operazione.

Be aware that this will typically exhibit as a Rapids movement to where the Operation beginning, completed by a Rapid Z movement to the geometry selected to define the Operation, and then a return to Rapid transit height.

Another common misunderstanding is that a Contour Operation is not outputting paths, when the Contour editor Operation-\>Cut Side is \"Inside\", the default, and toggling the 3D Model viability allows them to be seen.

[top](#top.md)


<div class="mw-translate-fuzzy">

### Path Workbench può eseguire la fresatura 3D della superficie? 


</div>

Sì, Path offre operazioni di fresatura 3D della superficie. Richiede l\'installazione nel percorso dei file delle macro di OpenCamLibrary, un modulo Open Source di terze parti.

OpenCamLibrary non è integrato in FreeCAD per garantire che non si verifichino violazioni delle licenze.

[top](#top.md)


<div class="mw-translate-fuzzy">

### Cosa devo fare se le strategie delle operazioni predefinite non soddisfano le mie esigenze? 


</div>

Per le operazioni tasca, il punto di partenza assume come valore predefinito XYZ = 000 ed è sempre attivo, ma può essere configurato anche nella finestra delle Proprietà vista. Nella scheda Operazione, le operazioni Tasca e Sfacciatura forniscono esplicita la modalità Discorde (Climb) opposta alla modalità di taglio convenzionale (taglio Concorde).

Per le operazioni di tipo Contorno, la scheda Operazione ha un input \"Direzione\" che può essere configurato come CW o CCW (rispettivamente orario o antiorario), che definisce la direzione di taglio. Per riferimento:

1.  Cut Side = Esteno, Direzione di taglio = CCW, taglio discorde
2.  Cut Side = Esteno, Direzione di taglio = CW, taglio convenzionale, concorde
3.  Cut Side = Inteno, Direzione di taglio = CW, taglio convenzionale, concorde
4.  Cut Side = Inteno, Direzione di taglio = CCW, taglio discorde

Gli Start Point possono essere abilitati e configurati nella finestra di delle proprietà vista.

Nelle operazioni di sfacciatura è possibile specificare la tolleranza del materiale, consentendo il sovradimensionento con i valori positivi (viene lasciato del sovrametallo) e il sottodimensionamento con i valori negativi.

Nelle operazioni Contornatura e Tasca, l\'Extra Offset ha lo stesso scopo.

Questi input sono preziosi, consentendo funzionalità tra cui:

1.  Definire le passate di sgrossatura, in conbinazione con i campi di immissione Profondità.
2.  Specificare il sovrametallo per le operazioni di sfacciatura
3.  Le funzioni di sfacciatura inferiori al diametro dell\'utensile possono essere migliorate specificando un taglio di un contorno esterno con un valore di scostamento extra negativo.

È necessario essere scrupolosi quando si specificano Tolleranze e Offset di materiali, c\'è il rischio di tagli indesiderati nel pezzo.

[top](#top.md)


<div class="mw-translate-fuzzy">

### Cosa faccio se un\'operazione genera più movimenti verticali di quelli che la lavorazione può tollerare? 


</div>

Le operazioni Tasca 3D, Tasca e Sfacciatura, *ma non l\'operazione Contornatura*, nella scheda Dati della Proprietà Vista hanno un\'opzione di configurazione per mantenere basso l\'utensile.

[top](#top.md)

## How can I leave tabs to clamp my milled work? 

Path workbench provides a Tag dressup for just this purpose.

[top](#top.md)


<div class="mw-translate-fuzzy">

### Cos\'è un postprocessore? 


</div>

Il Postprocessore viene utilizzato per personalizzare il codice di output per i controller CNC di destinazione secondo le varie macchine, nel loro dialetto G-Code.

[top](#top.md)


<div class="mw-translate-fuzzy">

### Posso modificare un postprocessore esistente o crearne uno mio? 


</div>

I postprocessori sono degli script Python e vengono salvati nel percorso dei file delle Macro. Sono destinati a essere modificati o utilizzati come modello per ulteriori sviluppi del Postprocessore.

[top](#top.md)


<div class="mw-translate-fuzzy">

### Voglio solo usare un solo Postprocessore, posso renderlo predefinito o nascondere le altre opzioni? 

Si.


</div>

Yes, The path preferences has a section for post processors where you can select which post processors to display and select a default post.

[top](#top.md)


<div class="mw-translate-fuzzy">

### Come posso impostare unità metriche o imperiali per il mio oggetto percorso? 


</div>

Le unità di misura del modello 3D sono definite in Modifica-\>Preferenze\...\>Generale-\>Unità del menu a discesa della scheda Sistema utente.

L\'impostazione delle Unità che configura come la fresa destinataria interpreta il G-Code della lavorazione si trova nel postprocessore dell\'output, che inserisce un comando G-Code G20 o G21 per indicare rispettivamente pollici o millimetri.

Il Postprocessore è anche configurato per Unità/Secondo o Unità/Minuto. Se impostato su Unità/Minuto, la velocità di avanzamento del dialetto G-Code interno di Path viene moltiplicata per 60.

La mancata corrispondenza tra il modello 3D e le impostazioni del Postprocessore sono probabilmente i responsabili di un fattore di errore 60 nella velocità di avanzamento e di un fattore 25,4 nella distanza.

[top](#top.md)


<div class="mw-translate-fuzzy">

### Come posso simulare le mie strategie di fresatura? 


</div>

Viene fornito un simulatore volumetrico per visualizzare il risultato del taglio delle geometrie da parte dell\'utensile incluse nelle operazioni della lavorazione rispetto al pezzo.

Se le linee del percorso oscurano il risultato della simulazione, la loro visibilità deve essere disattivata prima della simulazione.

[top](#top.md)


<div class="mw-translate-fuzzy">

### Qual è il significato dei colori delle linee del percorso? 


</div>

I colori delle linee del percorso sono definiti nella tabella dei colori in Modifica-\>Preferenze\...-\>Path-\>Path. I colori predefiniti sono:

1.  Verde per i percorsi normali.
2.  Rosso per i percorsi in rapida.
3.  Giallo per i percorsi sonda.

[top](#top.md)


<div class="mw-translate-fuzzy">

### Come abilitare o disabilitare la visibilità delle linee del percorso? 


</div>

Path consente il controllo della visualizzazione delle linee del percorso commutando la visibilità della lavorazione selezionandola nella Vista combinata. La visibilità delle singole o gruppi di operazioni viene quindi attivata dalla Vista combinata.

[top](#top.md)


<div class="mw-translate-fuzzy">

### Come posso verificare se la sequenza del mio codice G è corretta? 


</div>

Per impostazione predefinita, l\'output del postprocessore viene visualizzato in una finestra prima del salvataggio. Questo, insieme al simulatore CAM di Path fornisce un mezzo per esaminare il lavoro prima di eseguirlo su una macchina CNC. Lo strumento Ispeziona G-Code consente di ispezionare il codice G interno del percorso per ciascuna operazione, fornendo un mezzo per verificare se l\'output del postprocessore riflette ciò che è definito nell\'operazione.

L\'elenco delle Operazioni nel pannello Vista combinata mostra la sequenza in cui le operazioni verranno elaborate nella lavorazione. Se le operazioni sono corrette, ma non nella sequenza desiderata, è possibile regolarle facendo doppio clic sull\'elenco delle operazioni e trascinando le operazioni nella posizione corretta, oppure facendo doppio clic sull\'editor della lavorazione e selezionando la scheda Flusso di lavoro, quindi utilizzando i pulsanti freccia Su o Giù sulle operazioni selezionate per ordinarle.

[top](#top.md)


<div class="mw-translate-fuzzy">

### Perché non riesco a ottenere l\'output G-Code corretto dal mio Postprocessore per le operazioni inserito utilizzando Comando parziale-\> Comando personalizzato? 


</div>

Frequentemente, poiché il formato del comando G-Code personalizzato è sempre in Unità/secondo, può causare un fattore di errore 60 sulle macchine CNC che operano in Unità/minuto.

[top](#top.md)


<div class="mw-translate-fuzzy">

### Perché le modifiche ai valori di posizionamento nelle Proprietà vista sembrano non funzionare correttamente nel workbench Path? 


</div>

La funzione Path detiene inoltre una proprietà Placement. Cambiando il valore del posizionamento si cambia la posizione della funzione nella vista 3D, anche se le informazioni sul percorso sono invariate. La trasformazione è puramente visiva. Ciò consente, ad esempio, di creare un percorso attorno a una faccia che ha un particolare orientamento nel modello, e che non è lo stesso orientamento che il materiale da tagliare ha nella macchina CNC.

Tuttavia, i Path Compounds possono usufruire del Placement (posizionamento) dei propri figli (vedi sotto).

[https://www.freecadweb.org/wiki/Path\_scripting Path scripting](https://www.freecadweb.org/wiki/Path_scripting_Path_scripting.md)

[top](#top.md)


<div class="mw-translate-fuzzy">

### Perché il workbench Path sul mio computer sembra perdere delle funzionalità che vedo nei post di altri utenti del forum? 


</div>

Per impostazione predefinita, nell\'ambiente Path la funzionalità sperimentale è nascosta.

[top](#top.md)


<div class="mw-translate-fuzzy">

### Perché i video di YouTube pubblicati dagli sviluppatori del workbench Path non sono sincronizzati con il workbench Path? 


</div>

Il workbench Path è stato modificato drasticamente da FreeCAD v0.16 a v0.17, e qualsiasi video pubblicato prima del 1 ° gennaio 2018, molto probabilmente contiene informazioni che non sono più sincronizzate con la v0.17 del workbench Path di FreeCAD.

[top](#top.md)

## Why are arcs not round, but are made of a set of straight lines? 

This is only a matter of displaying the path. You can change this in the preferences: Load Path workbench.

1.  open Preferences-\>Path-\>Job Preferences
2.  set the values for *Default Geometry Tolerance* and *Default Curve Accuracy* to small values but not to 0, e.g. to 0.01mm.
3.  confirm the change
4.  Restart FreeCAD.

[top](#top.md)





{{Path_Tools_navi

}} 
