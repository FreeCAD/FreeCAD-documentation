---
- GuiCommand:
   Name:Std_AddonMgr
   Name/it:Addon manager
   MenuLocation:Strumenti - Addon manager
   Workbenches:Tutti
   Version:0.17
   SeeAlso:[Macro](Macros/it.md), [Ambienti complementari](External_workbenches/it.md)
---

# Std AddonMgr/it



## Descrizione

Il comando **Addon manager** apre il gestore Addon. Con Addon Manager è possibile installare e gestire [Ambienti complementari](external_workbenches/it.md), [macro](macros/it.md) e [Pacchetti di Preferenze](Preference_Packs/it.md) forniti dalla community di FreeCAD. Per impostazione predefinita, i componenti aggiuntivi disponibili sono presi da due repository, [1](https://github.com/FreeCAD/FreeCAD-addons/FreeCAD-addons) e dalla pagina [Raccolta di macro](Macros_recipes/it.md). Se GitPython e git sono installati sul proprio sistema, macro aggiuntive verranno caricate da [FreeCAD-macros](https://github.com/FreeCAD/FreeCAD-macros/). I repository personalizzati possono essere aggiunti nelle [Preferenze di Addon manager](Preferences_Editor#Addon_Manager/it.md).

A causa delle modifiche alla piattaforma GitHub nell\'anno 2020, il gestore Addon non funziona più se si utilizza FreeCAD versione 0.17 o precedente. È necessario eseguire l\'aggiornamento alla versione [0.18.5](https://github.com/FreeCAD/FreeCAD/releases/tag/0.18.5) o successiva. In alternativa è possibile installare i componenti aggiuntivi manualmente, vedi [Note](#Note.md) di seguito.



## Utilizzo

1.  Selezionare l\'opzione **Strumenti → <img src="images/Std_AddonMgr.svg" width=16px> Addon manager** dal menu principale.
2.  La prima volta che si usa il gestore Addon si apre una finestra di dialogo che avverte che i componenti aggiuntivi nel gestore Addon non fanno ufficialmente parte di FreeCAD. Presenta inoltre diverse opzioni relative all\'utilizzo dei dati da parte del gestore Addon. Regolare queste opzioni a proprio piacimento e premere il pulsante **OK** per confermare e continuare.
3.  Viene visualizzata la finestra di dialogo Addon manager. Per ulteriori informazioni, vedere le [Opzioni](Std_AddonMgr/it#Opzioni.md).
4.  Se è stato installato o aggiornato un ambiente di lavoro, si aprirà una nuova finestra di dialogo per informare che si deve riavviare FreeCAD affinché le modifiche abbiano effetto.



## Opzioni

<img alt="" src=images/AddonManager_Main.png  style="width:600px;">

1.  Il gestore Addon fornisce due layout di visualizzazione: \"Condensato\" ed \"Espanso\". Nella vista \"Condensata\", ogni componente aggiuntivo occupa una singola riga e la sua descrizione viene troncata per adattarsi allo spazio disponibile. \"Espanso\" mostra dettagli aggiuntivi, tra cui più testo descrittivo, informazioni sul manutentore, ulteriori dettagli sull\'installazione, ecc.
2.  Sono supportati tre diversi tipi di componenti aggiuntivi: [Ambienti di lavoro](external_workbenches/it.md), [Macro](macros/it.md) e [Pacchetti Preferenze](Preference_Packs/it.md). E\' possibile scegliere di mostrare solo un tipo o tutti in un unico elenco.
3.  L\'elenco può essere limitato per mostrare solo i pacchetti installati, solo i pacchetti con aggiornamenti disponibili o solo i pacchetti che non sono ancora installati.
4.  L\'elenco può essere filtrato, cercando una parola chiave nel titolo, nella descrizione e nei tag (descrizione e tag devono essere specificati dallo sviluppatore dell\'addon nei metadati dell\'addon). Il filtro può anche essere un\'espressione regolare, per un controllo granulare dell\'esatto termine di ricerca.
5.  La vista espansa mostra le informazioni sulla versione disponibili, la descrizione, le informazioni sul manutentore e le informazioni sulla versione dell\'installazione, per i pacchetti che forniscono un file [Metadati pacchetto](Metadati_pacchetto/it.md) (o per macro con metadati incorporati).
6.  I dati del componente aggiuntivo vengono memorizzati nella cache locale, con una frequenza di aggiornamento della cache variabile impostata nelle preferenze dell\'utente.
7.  In qualsiasi momento è possibile scegliere di aggiornare manualmente la propria cache locale per vedere gli ultimi aggiornamenti disponibili per ogni componente aggiuntivo.
8.  I controlli degli aggiornamenti possono essere impostati per essere automatici o eseguiti manualmente tramite un clic del pulsante (configurato nelle preferenze dell\'utente). Se GitPython e git sono installati sul proprio sistema, le informazioni di aggiornamento vengono recuperate utilizzando git. In caso contrario, le informazioni di aggiornamento vengono ottenute da qualsiasi file di metadati presente.

Facendo clic su un componente aggiuntivo in questa visualizzazione viene visualizzata la pagina dei dettagli del componente aggiuntivo:

<img alt="" src=images/AddonManager_Details.png  style="width:600px;">

La pagina dei dettagli mostra i pulsanti che consentono di installare, disinstallare, aggiornare e disabilitare temporaneamente un componente aggiuntivo. Per i componenti aggiuntivi installati elenca la versione attualmente installata e la data di installazione e se si tratta della versione più recente disponibile. Di seguito è riportata una finestra del browser Web incorporata che mostra la pagina README dell\'addon (per Ambiente di lavoro e Pacchetti di preferenze) o la pagina Wiki (per le macro).



## Preferenze

Le preferenze per Addon Manager si trovano nell\'[Editor delle Preferenze](Preferences_Editor/it#Addon_Manager.md). {{Version/it|0.20}}



## Note

-   L\'uso dei componenti aggiuntivi non è limitato alla versione di FreeCAD da cui sono stati installati. Si potrà anche usarli in qualsiasi altra versione di FreeCAD, supportata dall\'addon, presente sul proprio sistema.
-   I componenti aggiuntivi disponibili in Addon manager non fanno parte del programma ufficiale FreeCAD e non sono supportati dal team di sviluppo principale di FreeCAD. Bisogna leggere attentamente le informazioni fornite per assicurarsi di sapere cosa si sta installando.
-   Segnalazioni di bug e richieste di funzionalità devono essere inviate direttamente al creatore del componente aggiuntivo visitando il sito Web indicato. Molti sviluppatori di componenti aggiuntivi sono utenti regolari del [FreeCAD forum](https://forum.freecadweb.org), e possono anche essere contattato lì.
-   Se sul computer è installato il pacchetto [GitPython](https://github.com/gitpython-developers/GitPython), il gestore Addon lo utilizza, rendendo i download più veloci.
-   È inoltre possibile installare i componenti aggiuntivi manualmente. Vedere [Come installare gli ambienti aggiuntivi](How_to_install_additional_workbenches/it.md) and [Come installare le macro](How_to_install_macros/it.md).



## Informazioni per gli sviluppatori di addon 

Vedere [Addon](Addon/it#Informazioni_per_sviluppatori.md).



## Script


{{Version/it|0.21}}

Alcune funzionalità del gestore Addon sono progettate per l\'accesso tramite l\'API Python di FreeCAD. In particolare un componente aggiuntivo può essere installato, aggiornato e rimosso tramite l\'interfaccia Python. La maggior parte degli usi di questa API richiede la creazione di un oggetto con almeno tre attributi: {{Incode|name}}, {{Incode|branch}} e {{Incode|url}}. Per esempio:


```python
class MyAddonClass:
    def __init__(self):
        self.name = "TestAddon"
        self.url = "https://github.com/Me/MyTestAddon"
        self.branch = "main"
my_addon = MyAddonClass()
```

Il proprio oggetto {{Incode|my_addon}} è ora pronto per essere utilizzato con l\'API Addon Manager.



### Utilizzo da riga di comando (non-GUI) 

Se il proprio codice deve installare o aggiornare un componente aggiuntivo in modo sincrono (ad esempio senza una GUI), il codice può essere molto semplice:


```python
from addonmanager_installer import AddonInstaller
installer = AddonInstaller(my_addon)
installer.run()
```

Notare che questo codice si blocca fino al completamento, quindi non lo si dovrebbe eseguire sul thread della GUI principale. Per il gestore Addon, \"install\" e \"update\" sono la stessa chiamata: se questo addon è già installato e git è disponibile, verrà aggiornato tramite \"git pull\". Se non è installato o è stato installato tramite un metodo di installazione diverso da git, viene scaricato da zero (utilizzando git se disponibile).

Per disinstallare, utilizzare:


```python
from addonmanager_uninstaller import AddonUninstaller
uninstaller = AddonUninstaller(my_addon)
uninstaller.run()
```



### Utilizzo con GUI 

Se si prevede di eseguire il codice in una GUI o di supportare l\'esecuzione nella versione completa di FreeCAD, è meglio eseguire l\'installazione in un thread non GUI separato, in modo che la GUI rimanga reattiva. Per fare ciò, controllare prima se la GUI è in esecuzione e, in tal caso, generare un {{Incode|QThread}} (non provare a generare un {{Incode|QThread}} se la GUI non è attiva: richiedono un ciclo di eventi attivo per funzionare).


```python
from PySide import QtCore
from addonmanager_installer import AddonInstaller

worker_thread = QtCore.QThread()
installer = AddonInstaller(my_addon)
installer.moveToThread(worker_thread)
installer.success.connect(installation_succeeded)
installer.failure.connect(installation_failed)
installer.finished.connect(worker_thread.quit)
worker_thread.started.connect(installer.run)
worker_thread.start() # Returns immediately
```

Quindi definire le funzioni {{Incode|installation_succeeded}} e {{Incode|installation_failed}} da eseguire in ciascun caso. Per la disinstallazione è possibile usare la stessa tecnica, anche se di solito è molto più veloce e non bloccherà la GUI per molto tempo, quindi in generale è sicuro usare direttamente il programma di disinstallazione, come mostrato sopra.





{{Std Base navi

}}



---
![](images/Button_right.svg) [documentation index](../README.md) > Std AddonMgr/it
