---
- GuiCommand:/it
   Name:Std_AddonMgr
   Name/it:Addon manager
   MenuLocation:Strumenti → Addon manager
   Workbenches:Tutti
   Version:0.17
   SeeAlso:[Macro](Macros/it.md), [Ambienti complementari](External_workbenches/it.md)
---

# Std AddonMgr/it

## Descrizione

Il comando **Std AddonMgr** apre Addon manager. Con il gestore degli addon è possibile installare e gestire gli [ambienti esterni](external_workbenches/it.md) e le [macro](macros/it.md) forniti dalla comunità di FreeCAD. Gli ambienti e le macro disponibili sono presi da due repository, [FreeCAD-addons](https://github.com/FreeCAD/FreeCAD-addons/) e [FreeCAD-macros](https://github.com/FreeCAD/FreeCAD-macros/), e dalla pagina [Raccolta di macro](Macros_recipes/it.md).


<div class="mw-translate-fuzzy">

Si noti che gli addon contrassegnati come {{emphasis|Solo Python 2}} non funzioneranno nella versione 0.19 o successive di FreeCAD.


</div>

Due to changes to the GitHub platform in the year 2020 the Addon manager no longer works if you use FreeCAD version 0.17 or earlier. You need to upgrade to version [0.18.5](https://github.com/FreeCAD/FreeCAD/releases/tag/0.18.5) or a recent [0.19](https://github.com/FreeCAD/FreeCAD/releases/tag/0.19_pre) version. Alternatively you can install addons manually, see [Notes](#Notes.md) below.

![](images/Std_AddonMgr_dialog.png ) 
*La finestra di dialogo di Gestione de componenti aggiuntivi*

## Utilizzo

1.  Selezionare l\'opzione **Strumenti → <img src="images/Std_AddonMgr.svg" width=16px> Addon manager** dal menu principale.
2.  La prima volta che si usa il gestore Addon si apre una finestra di dialogo che avverte che i componenti aggiuntivi nel gestore Addon non fanno ufficialmente parte di FreeCAD. Premere il pulsante **OK** per confermare e continuare.
3.  Viene visualizzata la finestra di dialogo Addon manager. Per ulteriori informazioni, vedere le [Opzioni](Std_AddonMgr/it#Opzioni.md).
4.  Il pulsante **<img src="images/Button_valid.svg" width=16px> Aggiorna tutto** non funziona al momento.
5.  Premere il pulsante **<img src="images/Process-stop.svg" width=16px> Chiudi** per chiudere la finestra di dialogo.
6.  Se è stato installato o aggiornato un ambiente di lavoro, si aprirà una nuova finestra di dialogo per informare che si deve riavviare FreeCAD affinché le modifiche abbiano effetto.

## Opzioni

La finestra di Addon manager ha due schede a sinistra, una che elenca gli ambienti disponibili e l\'altra che elenca le macro disponibili. Il pannello delle informazioni sulla destra mostra la pagina iniziale del componente aggiuntivo selezionato.

### Disinstallazione

1.  Selezionare nella scheda <img alt="" src=images/Folder.svg  style="width:16px;"> **Ambienti di lavoro** o nelle <img alt="" src=images/Applications-python.svg  style="width:16px;"> **Macro** un componente aggiuntivo installato.
2.  Premere il pulsante **<img src="images/Delete.svg" width=16px> Disinstalla selezionati**.

### Installazione/aggiornamento

1.  Seleziona un componente aggiuntivo nella scheda <img alt="" src=images/Folder.svg  style="width:16px;"> **Ambienti di lavoro** o nella scheda <img alt="" src=images/Applications-python.svg  style="width:16px;"> **Macro** tab.
2.  Premere il pulsante **<img src="images/Edit_OK.svg" width=16px> Installa/aggiorna i selezionati**.
3.  Se si desidera aggiungere una macro a una barra degli strumenti personalizzata, non dimenticare di scaricare manualmente il file immagine dell\'icona, se disponibile, facendo clic sul collegamento nella pagina iniziale nel pannello delle informazioni. Vedere [Personalizzare l\'interfaccia](Interface_Customization/it#Barre_degli_strumenti.md).
4.  Per modificare la posizione di un ambiente aggiuntivo nella lista del [selettore degli ambienti](Std_Workbench/it.md) vedere [Personalizzare l\'interfaccia](Interface_Customization/it#Ambienti_di_lavoro.md).

### Configurazione

1.  Premere il pulsante **<img src="images/Preferences-general.svg" width=16px> Configura...**.
2.  Viene visualizzata la finestra di dialogo Opzioni del gestore dei componenti aggiuntivi.
3.  Opzionalmente selezionare la casella di controllo {{CheckBox|TRUE|Controlla automaticamente gli aggiornamenti all'avvio (richiede GitPython)}}.
4.  Opzionalmente aggiungere repository all\'elenco **Repository personalizzati**. I componenti aggiuntivi di questi repository verranno aggiunti nella scheda <img alt="" src=images/Folder.svg  style="width:16px;"> **Ambienti** o nella scheda <img alt="" src=images/Applications-python.svg  style="width:16px;"> **Macro**.
5.  Opzionalmente scegliere le impostazioni proxy.
6.  Premere il pulsante **OK** o il pulsante **Annulla** per chiudere la finestra di dialogo.

## Note


<div class="mw-translate-fuzzy">

-   I componenti aggiuntivi disponibili in Addon manager non fanno parte del programma ufficiale FreeCAD e non sono supportati dal team di sviluppo principale di FreeCAD. Bisogna leggere attentamente le informazioni fornite per assicurarsi di sapere cosa si sta installando.
-   Segnalazioni di bug e richieste di funzionalità devono essere inviate direttamente al creatore del componente aggiuntivo visitando il sito Web indicato. Molti sviluppatori di componenti aggiuntivi sono utenti regolari del [FreeCAD forum](https://forum.freecadweb.org), e possono anche essere contattato lì.
-   Se sul computer è installato il pacchetto [GitPython](https://github.com/gitpython-developers/GitPython), il gestore Addon lo utilizza, rendendo i download più veloci.
-   È inoltre possibile installare i componenti aggiuntivi manualmente. Vedere [Come installare gli ambienti aggiuntivi](How_to_install_additional_workbenches/it.md) and [Come installare le macro](How_to_install_macros/it.md).


</div>

## Informazioni per gli sviluppatori 

Se avete sviluppato un workbench o una macro e volete vederlo incluso in Addon manager, leggete come farlo nelle pagine del repository ([FreeCAD-addons](https://github.com/FreeCAD/FreeCAD-addons/) e [FreeCAD-macros](https://github.com/FreeCAD/FreeCAD-macros/)). Se aggiungete la vostra macro a [Raccolta di macro](Macros_recipes.md), non dovete fare nient\'altro, essa verrà automaticamente selezionata da Addon manager.

### Ambienti di lavoro in Python 


<div class="mw-translate-fuzzy">

Per i workbench Python, non è necessaria alcuna approvazione specifica per aggiungerlo a Addon manager e, essendo al di fuori del codice sorgente di FreeCAD, è possibile scegliere la licenza desiderata. Se si richiede che il proprio workbench sia aggiunto alla lista (senza la richiesta dei suoi autori non viene aggiunto nessun nuovo workbench), sia chiedendolo sul forum o aprendo una istanza nel repository [FreeCAD-addons](https://github.com/FreeCAD/FreeCAD-addons/), il codice continua a rimanere sul repository git dell\'autore, e viene semplicemente aggiunto come sottomodulo al repository [FreeCAD-addons](https://github.com/FreeCAD/FreeCAD-addons/). Ovviamente, prima di aggiungere un nuovo workbench, viene data un\'occhiata al codice per verificare che non contenga nulla di potenzialmente problematico.


</div>

### Workbench in C++ 

Se si sviluppa un workbench in C++, esso non può essere eseguito direttamente dagli utenti e deve prima essere compilato. Quindi si hanno due opzioni, o fornire le versioni precompilate del proprio workbench per i diversi sistemi operativi, oppure si deve chiedere di unire il proprio codice al codice sorgente di FreeCAD. Per questo, si deve usare la licenza LGPL (o una licenza completamente compatibile come MIT o BSD), e si deve presentare i nuovi strumenti alla comunità nel [forum di FreeCAD](https://forum.freecadweb.org) per la revisione. Quando il codice è stato testato e approvato, è necessario creare una biforcazione nel repository di FreeCAD, se non ancora fatto, e creare un nuovo ramo, inserirvi il codice e aprire una richiesta di pull in modo che il ramo venga unito al repository principale.


<div class="mw-translate-fuzzy">





</div>


{{Std Base navi

}}



---
![](images/Right_arrow.png) [documentation index](../README.md) > Std AddonMgr/it
