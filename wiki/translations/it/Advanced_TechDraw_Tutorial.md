---
 TutorialInfo:t
   Topic: Modeling
   Level: Experienced User
   Author: domad
   FCVersion: 0.19.23300 or higher
---

# Advanced TechDraw Tutorial/it










## Scopo in breve 

Creare punti, linee, cerchi, archi, ecc. nelle viste TechDraw e/o interi disegni \"cosmetici\" con assoluta precisione, adatti agli strumenti di dimensionamento di cui è dotato l\'ambiente, per generare disegni tecnici conformi e dettagliati.



## Introduzione

Questo tutorial introduce l\'utente esperto all\'uso avanzato degli strumenti e delle tecniche esistenti di altri ambienti di lavoro per estendere le funzionalità effettivamente mancanti in <img alt="" src=images/Workbench_TechDraw.svg  style="width:24px;"> [TechDraw](TechDraw_Workbench/it.md). Questo tutorial non è una guida completa ed esauriente a TechDraw e molti degli strumenti e delle funzionalità non sono trattati. Dovrebbe contribuire a superare le difficoltà che si incontrano nel quotare e arricchire il disegno tecnico utilizzando TechDraw. Questo tutorial guiderà gli utenti avanzati attraverso i passaggi necessari per produrre disegni tecnici complessi di una parte presa dal [Tutorial di base](Basic_Part_Design_Tutorial/it.md) utilizzando gli strumenti di disegno di

1.  <img alt="" src=images/Workbench_Draft.svg  style="width:24px;"> [Draft](Draft_Workbench/it.md) (linee, polilinee, circonferenze, archi, spline, bezier, ecc.), in particolare gli snap, per creare sull\'oggetto dei \"punti cosmetici\" effettivamente precisi che potranno poi essere utilizzati per la quotatura in TechDraw.
2.  È anche possibile utilizzare <img alt="" src=images/Workbench_Sketcher.svg  style="width:24px;"> [Sketcher](Sketcher_Workbench/it.md) per
    -   generare \"base-sketchTD\" (basi di schizzi per TechDraw) in 2D (ad esempio come schemi di sistema, planimetrie, prospetti, viste di parti meccaniche o generiche, ecc.) o per
    -   utilizzare direttamente gli schizzi che hanno generato i modelli 3D, oppure tramite
    -   la conversione in schizzo del "facebinder" generato con Draft ottenuto da facce e/o sezioni dei modelli 3D.
3.  Per ottenere sezioni particolari (tagli su piani o assi diversi) da presentare nella pagina in TechDraw (si consiglia di utilizzare una copia dell\'oggetto 3D originale), poi tramite la creazione di piani (anche su assi diversi) utilizzando il pulsante \[ \[Image:Workfeature_workbench_icon.svg\|24px\]\] [Workfeature](Workfeature_Workbench/it.md), è possibile sezionare la copia dell\'oggetto 3D <img alt="" src=images/Part_SliceApart.svg  style="width:24px;"> [Part](Part_SliceApart/it.md) per ottenere le facce da convertire in schizzo <img alt="" src=images/Draft_Draft2Sketch.svg  style="width:24px;"> [Draft](Draft_Draft2Sketch/it.md) e poi attraverso Sketcher modificarle per renderle adatte al disegno tecnico che ci interessa generare in TechDraw. [Workfeature](Workfeature_Workbench.md) (e le [Macro WorkFeatures](Macro_WorkFeatures/it.md)) sono ricche di comode funzioni aggiuntive, che ci permettono di creare facilmente piani (teoricamente infiniti in estensione e quantità) selezionando tre punti (vertici) *(ricordiamo che per tre punti non allineati passa uno ed un solo piano)* è un assioma geometrico, che conferma senza alcuna ambiguità (!) la validità e importanza dello strumento WorkFeatureDev per creare piani precisi con estrema facilità.

(\**Questo è abbastanza paragonabile al comando AutoCAD Slice [-872B-927D69517CBF-htm.html](https://knowledge.autodesk.com/support/autocad/learn-explore/caas/CloudHelp/cloudhelp/2019/ENU/AutoCAD-Core/files/GUID-27593C5E-4B89-41F2) che si basa su quell\'assioma. Senza precostruire alcun nuovo piano, viene definito un piano di taglio utilizzando tre punti.*)

*Nota: Questi piani possono essere uniti tra loro mediante sovrapposizione/coincidenza di due bordi utilizzando la funzione booleana <img alt="" src=images/Part_Fuse.svg  style="width:24px;"> [Unione di Part](Part_Fuse/it.md).* I piani così formati e opportunamente posizionati (secondo le nostre disposizioni) verranno utilizzati come **lame di taglio** di <img alt="" src=images/Part_SliceApart.svg  style="width:24px;"> [Part](Part_SliceApart/it.md), tagliando il nostro oggetto 3D in più parti a seconda del piano di taglio scelto.\'\'



## Prima di iniziare 

Gli ambienti utilizzati per produrre i disegni degli esempi allegati sono:
\* <img alt="" src=images/Workbench_Part.svg  style="width:24px;"> [Part](Part_Workbench/it.md)

-   <img alt="" src=images/Workbench_Draft.svg  style="width:24px;"> [Draft](Draft_Workbench/it.md)
-   <img alt="" src=images/Workbench_Sketcher.svg  style="width:24px;"> [Sketcher](Sketcher_Workbench/it.md)
-   <img alt="" src=images/Workfeature_workbench_icon.svg  style="width:24px;"> [Workfeature](Workfeature_Workbench/it.md)
-   <img alt="" src=images/Workbench_TechDraw.svg  style="width:24px;"> [TechDraw](TechDraw_Workbench/it.md)



## Il compito 

Fasi della procedura:

1.  Realizzazione dell\'oggetto/i 3D secondo i canoni della modellazione tradizionale;
2.  Possibile creazione di copie indipendenti o semplici, ad es. da utilizzare per la creazione di specifiche sezioni continue posizionate su più piani o assi, e che poi attraverso l\'utilizzo delle funzioni \"facebinder\", \"Draft to Sketch\", Shape 2D View, ecc. ci permetterà di produrre "Sketches" perfetti, per poi modificarli per renderli (creando "punti o linee cosmetiche" ad hoc) utilizzabili in TechDraw; a questi schizzi ho dato il nome di \"base-sketchTD\";
3.  inserimento/creazione di "base-sketchTD" nei layer di appartenenza (anche con "drag and drop");
4.  creazione della pagina di disegno con relativo template;
5.  creazione della vista con TechDraw: selezionare il layer o la cartella di raggruppamento (che contiene il "base-sketchTD") dalla struttura, quindi cliccare sul pulsante "inserisci vista"; TechDraw inserirà nella vista il contenuto del livello o della cartella di raggruppamento. Per una corretta creazione "base-sketchTD" deve essere perpendicolare alla vista del monitor/display; C\'e da segnalare che qualunque cosa aggiungeremo successivamente nel layer o nella cartella di raggruppamento, o modifiche del "base-sketchTD", verrà aggiornato in tempo reale nella vista TechDraw. Tienere presente che aggiornamenti e/o modifiche potrebbero interessare le quote già introdotte o le linee cosmetiche create con lo specifico tool di TechDraw nella vista.
6.  una volta definita nella vista la "base-sketchTD" possiamo passare al dimensionamento con gli appositi strumenti TechDraw;

E\' possibile inserire il \"base-sketchTD\" anche nelle viste dei gruppi di proiezione:

-   seleziona la vista proiettata -\> Proprietà -\> Dati -\> sezione "Projection" -\> in Source clicca sul pulsante con i tre punti e aggiungi direttamente il "base-sketchTD" ovvero il layer che lo contiene.

:   Da notare che il \"base-sketchTD\" deve essere posizionato sulla faccia più alta del modello/oggetto, altrimenti verrà nascosto e risulterà invisibile in TechDraw.

Le sezioni ottenute dalle viste non sembrano avere questa possibilità. Qualora sia necessario creare punti cosmetici precisi adatti al dimensionamento (es. punti di tangenza), si possono generare:

-   in \"Sketcher\" attraverso linee di costruzione e inserendo nelle estremità cerchi con diametro/raggio infinitesimo (0,00001), questi verranno visti da TechDraw come punti/vertici idonei alla quotatura;
-   in Draft con lo stesso metodo per essere inserito nel relativo layer o raggruppamento di cartelle;

:   una volta modificato il \"base-sketchTD\" o aggiunto l\'oggetto Draft nella cartella layer o raggruppamento, TechDraw aggiornerà automaticamente la vista, se ciò non avviene aggiornare manualmente con l\'apposito comando.

Per inserire riempimenti o motivi di sezione:
prestare attenzione alle linee create sulle facce che intersecano due o più bordi, sono viste da TechDraw come elementi di separazione della faccia che influenzano la creazione dei riempimenti o dei motivi. Ciò si verifica ad es. quando si creano le linee esterne che definiscono la filettatura di un foro, questa linea impedirà al riempimento o al disegno di estendersi ulteriormente impedendogli di arrivare su quello che definisce il preforo. In questo caso è meglio creare punti cosmetici tramite linee di costruzione inserendo nei vertici cerchi di raggio infinitesimo che verranno visti da TechDraw come punti cosmetici e poi unirli in TechDraw con crea linea cosmetica da due punti.
Tutte le linee e/o i percorsi (compresi quelli cosmetici) visualizzati nelle viste possono essere modificati nella formattazione tramite il comando \"Cambia aspetto delle linee selezionate\" di TechDraw.
Per creare specifiche sezioni continue su assi o piani diversi, ho utilizzato l\'ambiente "WorkFeatureDev" che consente di creare piani "solidi", con spessore "0", selezionando tre vertici. Questi piani possono essere uniti tramite un bordo comune o sovrapposto utilizzando le funzioni booleane dell\'ambiente "Parte" e successivamente utilizzati per affettare/sezionare il modello solido tramite il comando "Seziona" dello stesso ambiente. Le facce degli oggetti tagliati possono essere opportunamente sfruttate per la creazione, con la funzione "Facebinder", dei "base-sketchTD" per produrre specifiche viste in sezione in TechDraw e quindi poterle quotare e dettagliare.
Si reputa di aver reso pubblico ogni \"trucco\" (o meglio sistema) sperimentato per poter utilizzare strumenti più specifici (non forniti per TechDraw) e creare disegni tecnici professionali di alta qualità senza alcun limite, rendendo l\'ambiente TechDraw più efficiente e adattabile a qualsiasi esigenza, con ogni probabilità alla pari (se non più flessibile e potente) rispetto ai concorrenti commerciali.
C\'è da dire, cosa non trascurabile, che con questo sistema è possibile creare interi file 2D e quotarli con TechDraw allo stesso modo di \"LibreCad\" o \"Autocad LT\" o altri cad bidimensionali.
Si spera di essere stato abbastanza chiaro (traduzione permettendo) nello spiegare la procedura (\"trucco/sistema\") che ritengo \"più facile a farsi che a dirsi\", in quanto si tratta di poter inserire i disegni 2D nelle viste di TD creati con "Draft" e/o con "Sketcher" semplicemente selezionandoli dalla struttura e creando una vista in TD con l\'apposito comando "crea una vista"; ma si è pensato di fare una cosa gradevole e più tecnica descrivendo la procedura, sicuramente, in maniera \"semplificata\" per creare un minimo di flusso di lavoro organizzato.
Sta a ciascuno di noi, con fantasia ed inventiva, ottimizzarlo al massimo per ottenere il miglior risultato.
Allego i file di alcuni esempi di flusso di lavoro di disegni tecnici (non realizzabili solo con TechDraw) da cui sono state prese le immagini mostrate di seguito.
Nella speranza che siano stati utili, buon lavoro e buona sperimentazione!


## Note



## Prospettive future 

Tuttavia il percorso descritto potrebbe rappresentare il punto di partenza (o l\'idea) per scrivere codice aggiuntivo per automatizzare il sistema e integrarlo direttamente in TechDraw con apposite funzioni di pulsanti/comandi.



## Riferimenti

-   [Macro WorkFeatures](https://wiki.freecadweb.org/Macro_WorkFeatures) Wiki page della macro
-   [FreeCAD WorkFeature Workbench](https://github.com/Rentlau/WorkFeature-WB) Repository del codice sorgente
-   [TechDraw without limits = Layout autocad](https://forum.freecadweb.org/viewtopic.php?t=54499) Forum Thread
-   [TechDraw: -- come utilizzare gli strumenti Draft/Snaps per creare " vertici/punti cosmetici"](https://forum.freecadweb.org/viewtopic.php?f=28&t=53329) Forum Thread in lingua italiana


{{TechDraw Tools navi

}}



---
⏵ [documentation index](../README.md) > [TechDraw](Category_TechDraw.md) > Advanced TechDraw Tutorial/it
