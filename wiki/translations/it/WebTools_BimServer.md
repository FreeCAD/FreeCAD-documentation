---
 GuiCommand:
   Name: WebTools BimServer
   Name/it: BimServer
‏‎‏‎   MenuLocation: Arch , Utilità , BIM server
   Workbenches: Arch_Workbench/it
   Shortcut: 
‏‎   SeeAlso: 
---

# WebTools BimServer/it


</div>


<div class="mw-translate-fuzzy">

**Nota:** A partire da FreeCAD v0.17, questo strumento è stato rimosso dall\'ambiente Arch e ora fa parte dell\'[ambiente esterno Webtools](WebTools_Workbench/it.md) che è possibile installare tramite il menu Strumenti → [Addons Manager](Std_AddonMgr/it.md).


</div>

## Descrizione


<div class="mw-translate-fuzzy">

Questo comando consente di interagire con una istanza [BIMServer](http://www.bimserver.org), aprire i file memorizzati sul BIMServer, e salvare nuove revisioni di tali file. BIMServer è un sistema server free, open-source realizzato per lavorare con i file IFC. Allo stato attuale, permette di gestire i progetti con più file IFC, e gestire le revisioni. La sua architettura di sistema di database e di plugin altamente estensibile permette anche di progettare avanzati strumenti di convalida e di interrogazione, e intelligenti flussi di lavoro incorporati.


</div>

Per poter utilizzare questo comando, devono essere soddisfatte le seguenti condizioni:


<div class="mw-translate-fuzzy">

-   Sul sistema devono essere installati i moduli Python **json** e **requests**
-   È necessario avere accesso a un\'istanza BIMServer (leggere la [documentazione di BIMServer](https://github.com/opensourceBIM/BIMserver/wiki) per installare localmente un BIMServer), e avere le credenziali (login e password) per tale server. Al momento della scrittura, la versione stabile di BIMServer è la 1,4, ma si consiglia di installare una delle versioni beta 1.5.x disponibili, che installano un sacco di plugin automaticamente (nella versione 1.4 è necessario installare i plugin manualmente).
-   Tutti i trasferimenti di file con il BIMServer sono fatti con dei file IFC. Pertanto, è necessario sapere come lavorare con i [Ifile FC](Arch_IFC/it.md).


</div>

## Utilizzo


<div class="mw-translate-fuzzy">

1.  Assicurarsi che i requisiti di cui sopra siano soddisfatti, e si ha accesso a un\'istanza BIMServer in esecuzione
2.  Selezionare il menu Arch -\> Utilità -\> **<img src="images/WebTools_BimServer.svg" width=16px> [BIM Server](Arch_BimServer/it.md)
**
3.  Premere il pulsante **Connect** e compilare i dati delle credenziali
4.  Stabilita la connessione al BIMServer, scegliere un progetto da lavorare dalla casella a discesa **Project**


</div>

## Opzioni

![](images/Arch_Bimserver_panel.jpg )


<div class="mw-translate-fuzzy">

-   Se questa è la prima volta che ci si connette a un BIMServer da FreeCAD, premere il pulsante **Connect**, e compilare l\'URL del server, i dati di accesso (login, che è sempre un indirizzo e-mail) e la password nella finestra di dialogo pop-up che appare. Se si desidera accedere automaticamente al successivo comando di BimServer, selezionare l\'opzione **salva le credenziali** (login e password non vengono salvati da FreeCAD, è solo un cookie di sessione).
-   Dopo che FreeCAD si è connesso con successo a un\'istanza BIMServer, il pulsante **Connect** si trasforma in **Connected**. Fare di nuovo clic sul pulsante per disconnettersi. Questo cancella anche il cookie di sessione memorizzato, per cui la prossima volta sarà di nuovo necessario inserire le proprie credenziali.
-   Per eliminare il cookie di sessione manualmente e resettare tutto, basta eliminare l\'URL BIMServer memorizzato in **Modifica -\> Preferenze -\> Arch -\> BimServer**.
-   Il pulsante **Open in browser** apre l\'interfaccia web del server BIM sia nel browser interno di FreeCAD, oppure, se l\'opzione in **Modifica -\> Preferenze -\> Arch -\> BimServer** è selezionata, in browser web esterno. Questo permette ad esempio di creare dei nuovi progetti, o di analizzare i contenuti memorizzati sul BIMServer.


</div>

### Scaricare le revisioni 

-   La casella a discesa **Project** mostra i progetti disponibili memorizzati sul BIMServer. Sceglierne uno per vedere le versioni disponibili per quel progetto.
-   Selezionare una revisione e fare clic su **Open** per scaricare il file IFC corrispondente a quella revisione e aprirlo in FreeCAD.
-   Quando si preme il pulsante **Open**, si apre una finestra di dialogo che consentire di salvare il file IFC scaricato in una posizione a propria scelta, prima di aprirlo. Se si preme **Cancel**, il file viene invece salvato con un nome temporaneo nella directory temporanea del sistema.

### Caricare le revisioni 


<div class="mw-translate-fuzzy">

-   Se si desidera caricare una nuova revisione, assicurarsi che nella casella a discesa **Project** sia selezionato il progetto giusto
-   Scegliere il **Root object** (l\'oggetto radice) che si desidera caricare. Deve essere un oggetto [Sito Arch](Arch_Site/it.md) o un [Edificio Arch](Arch_Building/it.md). Saranno caricati solo gli oggetti che appartengono a tale oggetto principale.
-   Scrivere un **Comment**, che sarà usato come descrizione (nome) della revisione.
-   Premere il pulsante **Upload**. Si apre una finestra di dialogo che consentire di salvare il file IFC prodotto in una posizione a propria scelta, prima di caricarlo. Se si preme **Cancel**, il file viene invece salvato con un nome temporaneo nella directory temporanea del sistema.


</div>



---
⏵ [documentation index](../README.md) > WebTools BimServer/it
