# Crowdin Administration/it
## Ruoli

-   Traduttore
    -   Ha la possibilità di suggerire e votare le traduzioni in una lingua.
    -   Richiede più contestualizzazione; chiede chiarimenti; segnala errori nella stringa da tradurre; contesta una voce di traduzione corrente ecc\...

-   Correttore di bozze (proofreader)
    -   Gestisce le traduzioni suggerite e/o votate dai traduttori. Il correttore di bozze quindi accetta/rifiuta la traduzione.
    -   È necessario un ulteriore passaggio per dare anche l\'approvazione finale della stringa di traduzione. Poiché per \"Approvare\" una traduzione è necessario rileggerla e contrassegnarla, viene fornita una sorta di livello di \"Garanzia di qualità\". Una volta approvata la traduzione, la stringa verrà contrassegnata in verde e verranno aggiunti ulteriori progressi alla barra di stato verde della lingua che viene tradotta. La barra di avanzamento verde può indicare lo \"stato di salute\" della lingua da tradurre. Consente inoltre agli sviluppatori una maggiore flessibilità nell\'unire le traduzioni che sono state solo approvate.
    -   Risponde alle domande dei traduttori all\'interno dell\'interfaccia Crowdin. Ad esempio, se è necessaria maggiore contestualizzazione; oppure c\'è un errore nella stringa da tradurre, oppure una traduzione accettata o approvata viene contestata ecc\...
    -   Segnala agli sviluppatori eventuali problemi rilevanti che richiedono modifiche al codice sorgente, ecc.



### Filtraggio delle stringhe 

<img alt="" src=images/Crowdin_Filter_Strings.png  style="width:500px;">

Il filtraggio delle stringhe è una funzione utile per revisori e manager. Permette di ordinare in modo efficace molte stringhe di traduzione, per esempio mostra solo le stringhe che sono state contrassegnate come \'mancanti di informazioni più contestuali\' o \'stringa sorgente errata\'. Questo servizio che i traduttori stanno facendo per FreeCAD fornisce un ulteriore livello di test di garanzia della qualità. Molti errori di battitura, problemi di grammatica e persino bug possono essere scoperti controllando le stringhe di traduzione. Gli utenti contrassegnano queste stringhe problematiche in modo che possiamo rispondere e alla fine risolverle.



### Tasti di scelta rapida 

<img alt="" src=images/Crowdin_keyboard_shortcuts.png  style="width:300px;">

L\'utilizzo delle scorciatoie da tastiera è un trucco importante per risparmiare tempo ed essere più efficienti. Se siete un traduttore, un correttore di bozze o un manager vale la pena impararlo. È possibile visualizzare l\'elenco delle scorciatoie da tastiera premendo sull\'icona della tastiera nella parte in alto a destra dell\'interfaccia utente di Crowdin.

**Nota importante:** fare attenzione a non introdurre errori nelle stringhe di traduzione generate da pressioni di tasti inaffidabili che avrebbero dovuto essere una scorciatoia da tastiera.

**Scorciatoie usate frequentemente:**

-   Copia la traduzione originale: **Alt**+**C**
-   Salva la traduzione: **Ctrl**+**Enter**
-   Approva la traduzione: **Alt**+**L** (rilevante per i correttori di bozze)



## Risoluzione dei problemi di traduzione 

Se, nell\'interfaccia utente di FreeCAD, si nota una stringa non tradotta, procedere come segue:

1.  Se non si è sicuri a quale ambiente appartienga, individuarla prima nel codice sorgente di FreeCAD. Su Linux è possibile usare {{Incode|grep -r "testo inglese" *}}.
2.  Ad esempio, se la stringa è {{Incode|"Solver Calculix Standard"}} verrà trovato questo file: **src/Mod/Fem/femcommands/commands.py** e si capirà che la stringa appartiene all\'ambiente FEM.
3.  Ora, cercare questa stringa su Crowdin. Se la propria lingua è il francese, visitare <https://crowdin.com/project/freecad/fr>, andare all\'ambiente FEM e controlla se si trova lì ed è tradotta.
4.  Ci sono due possibilità:
    1.  La stringa non è su Crowdin perché non è stata rilevata dallo script che raccoglie le stringhe dal codice sorgente di FreeCAD e le comprime nei file **.ts**. Ci possono essere due ragioni per questo:
        -   La stringa non è gestita correttamente dal codice {{Incode|translate()}} (o dal codice {{Incode|QT_TRANSLATE_NOOP()}} per casi speciali come i nomi dei comandi), ciò significa che c\'è un problema che deve essere risolto nel codice sorgente.
        -   Sembra tutto normale, ma lo script di raccolta ha un problema con quella stringa specifica, il che può accadere poiché contiene molti bug.
    2.  La stringa è su Crowdin. Ci sono quindi diverse possibilità:
        -   Potrebbe darsi che le ultime stringhe di Crowdin non siano state ancora integrate nel codice programma. E\' possibile verificare se è così cercando la stringa (vedere sopra) e controllare se appare nei file **.ts** tradotti. Nel nostro esempio {{Incode|"Solver Calculix Standard"}} si troverebbe in **src/Mod/Fem/Gui/Resources/translations/Fem_fr.ts**. Ciò indica che la stringa tradotta si trova nel sorgente di FreeCAD e tutto dovrebbe sistemarsi nella build successiva.
        -   Se la stringa continua a mancare nella build successiva, il problema è più complesso ed è necessario fare un po\' di debug:
            1.  Controllare nel file sorgente se la stringa originale è gestita da {{Incode|translate()}} o {{Incode|QT_TRANSLATE_NOOP()}}.
            2.  Verificare che il contesto corrisponda a ciò che è su Crowdin.
            3.  Nel caso di {{Incode|QT_TRANSLATE_NOOP()}}, ci sono diversi casi particolari. Per i comandi, il contesto deve essere il nome esatto del comando, lo stesso utilizzato in {{Incode|FreeCADGui.runCommand()}}. Per le proprietà deve essere {{Incode|"App::Property"}}. Per i nomi dei menu e delle barre degli strumenti deve essere {{Incode|"Workbench"}}.



## Link

-   [Localizzazione](Localisation/it.md)
-   [Crowdin Scripts](Crowdin_Scripts/it.md)
-   [Release process](Release_process.md)



---
⏵ [documentation index](../README.md) > [Administration](Category_Administration.md) > Crowdin Administration/it
