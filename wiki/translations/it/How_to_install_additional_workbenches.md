---
 TutorialInfo:t   Topic: Programmazione   Level: Medio   Time: 15 minuti   FCVersion: Tutte   Author: User:R-Frank   r-frank|Files: none
---

# How to install additional workbenches/it







## Descrizione

Gli utenti esperti hanno esteso FreeCAD con vari [ambienti di lavoro esterni](external_workbenches/it.md) personalizzati, che non sono integrati nel codice sorgente di FreeCAD, ma che sono facili da implementare in una distribuzione FreeCAD esistente. Qui sono descritti i metodi di installazione per i diversi sistemi operativi.


**Nota:**

a partire dalla versione 0.17, FreeCAD include un <img alt="" src=images/Std_AddonMgr.svg  style="width:24px;"> [Addon Manager](Std_AddonMgr/it.md) nel menu **Strumenti → Addon manager**, che permette di installare sia macro che ambienti di lavoro. Le istruzioni seguenti sono necessarie solo si desidera installare manualmente un ambiente. Ciò potrebbe essere necessario se per qualche motivo Addon Manager non funziona ma si ha accesso all\'ambiente scaricato come pacchetto **.zip**.


<div class="mw-collapsible mw-collapsed toccolours">



## Installazione in Windows 

Come installare ulteriori ambienti e componenti aggiuntivi su Windows


<div class="mw-collapsible-content">



### Installazione manuale 


**Nota:**

Questo metodo è possibile ma non necessario grazie all\'introduzione di [Addon Manager](Std_AddonMgr/it.md). Tuttavia, queste informazioni potrebbero essere ancora utili per alcuni.

-   Scaricare il workbench da github cliccando sul pulsante **Clone** o **Download** sulla pagina GitHub (in alto a destra) e scegliendo \"Download ZIP\"
-   Decomprimere l\'archivio scaricato sul disco rigido locale
-   All\'interno di FreeCAD, individuare il percorso delle macro scegliendo **Modifica > Preferenze > Python > Macro** e vedere quale è il "Percorso Macro"
-   Supponendo che il vostro login di Windows sia "*User-Name*" il percorso predefinito delle macro è "C:\\User-Name\\Appdata\\Roaming\\FreeCAD"
-   All\'interno della directory delle macro creare (se non è ancora presente) una cartella chiamata "**Mod**"
-   All\'interno della cartella Mod creare una cartella con il nome dell\'ambiente, ad esempio "Curves"
-   Ora spostare i file decompressi e le sottocartelle del Workbench nella cartella dell\'ambiente appena creato
-   Dopo il riavvio di FreeCAD si dovrebbe avere una nuova voce nel menu a discesa [selettore degli ambienti](Std_Workbench/it.md)

**Raccomandazioni aggiuntive per l\'aggiornamento degli ambienti**

In Windows, durante l\'aggiornamento di un ambiente già installato, Windows mantiene il vecchio file .py come .pyc. Dato che questo può causare dei problemi, si consiglia di disinstallare l\'ambiente, riavviare FreeCAD e installare la nuova versione.


</div>


</div>


<div class="mw-collapsible mw-collapsed toccolours">



## Installazione in Linux 

Come installare ulteriori ambienti e componenti aggiuntivi su Linux


<div class="mw-collapsible-content">



### Utilizzo di git 

Aggiungere [community-ppa](https://launchpad.net/~freecad-community/+archive/ubuntu/ppa) all\'interno del ppa-manager.
Installare gli ambienti tramite il gestore dei pacchetti synaptic.


```python
$ sudo apt-get install git python-numpy python-pyside
$ mkdir ~/.FreeCAD/Mod
$ cd ~/.FreeCAD/Mod
$ git clone https://github.com/tomate44/CurvesWB.git
```

Ora negli ambienti di FreeCAD ci dovrebbe essere una nuova voce denominata \"CurvesWB\". Una volta installato, utilizzare git per l\'aggiornamento alla versione più recente in questo modo:


```python
$ cd ~/.FreeCAD/Mod/CurvesWB
$ git pull
$ rm *.pyc
```



### Installazione manuale 


**Nota:**

Questo metodo è possibile ma non necessario grazie all\'introduzione di [Addon Manager](Std_AddonMgr/it.md). Tuttavia, queste informazioni potrebbero essere ancora utili per alcuni.

-   Scaricare il workbench da github cliccando sul pulsante **Clone** o **Download** sulla pagina GitHub (in alto a destra) e scegliendo \"Download ZIP\"
-   Decomprimere l\'archivio scaricato sul disco rigido locale
-   All\'interno di FreeCAD, individuare il percorso delle macro scegliendo **Modifica > Preferenze > Python > Macro** e vedere quale è il "Percorso Macro"
-   Per impostazione predefinita, la directory delle macro è la directory (nascosta) **./.FreeCAD/** nella propria home-directory
-   All\'interno della directory delle macro creare (se non è ancora presente) una cartella chiamata "**Mod**"
-   All\'interno della cartella Mod/ creare una cartella con il nome dell\'ambiente, ad esempio "Curves"
-   Ora spostare i file decompressi e le sottocartelle del Workbench nella cartella dell\'ambiente appena creato
-   Dopo il riavvio di FreeCAD si dovrebbe avere una nuova voce nel menu a discesa nel [selettore degli ambienti](Std_Workbench/it.md)


</div>


</div>


<div class="mw-collapsible mw-collapsed toccolours">

## Installazione in Mac 

Come installare ulteriori ambienti e componenti aggiuntivi su macOS


<div class="mw-collapsible-content">



### Installazione manuale 


**Nota:**

Questo metodo è possibile ma non necessario grazie all\'introduzione di [Addon Manager](Std_AddonMgr/it.md). Tuttavia, queste informazioni potrebbero essere ancora utili per alcuni.

Nel caso di questo esempio, si supponga di aver scelto [Curves Workbench/it](Curves_Workbench/it.md) come ambiente di lavoro complementare che si desidera installare:

-   Scegliere e scaricare il repository git dell\'ambiente complementare scelto come file ZIP
-   Esistono due posizioni possibili per i \"Mod\" dell\'ambiente e del componente aggiuntivo:

1.  Tutti gli utenti: **/Applications/FreeCAD.app/Contents/Resources/Mod**
2.  Solo utente locale: **/Users/myusername/Library/Application Support/FreeCAD/Mod**

-   Se si utilizza Finder per navigare manualmente nella posizione Tutti gli utenti in Applicazioni, di dovrà procedere così
    -   andare su **/Applications**\" e selezionare FreeCAD.app
    -   fare clic con il tasto destro del mouse e selezionare \"Show Package Contents\", verrà visualizzata una nuova finestra con una cartella denominata \"Contents\"
    -   fare un solo clic sulla cartella \"Contents\" poi su \"Resources\" e fare doppio clic per aprire la cartella \"Mod\"
-   Una volta che ci si trova nella cartella \"Mod\" che si desidera utilizzare, creare una nuova cartella denominata \"Curves\"
-   Decomprimere il repository scaricato nella cartella \"Mod/Curves\"


</div>


</div>



## Risoluzione dei problemi generali 

-   In Windows non utilizzare i caratteri speciali (ad esempio dieresi tedesca) per il nome utente, altrimenti FreeCAD non riconosce i file e le cartelle nel percorso delle macro.
-   Se è già stato impostato un nome utente con caratteri speciali, creare un nuovo nome utente o puntare il percorso macro a una directory che non utilizzi caratteri speciali.
-   Andare in **Modifica → Preferenze → Ambienti di lavoro** e assicurarsi che l\'ambiente non sia impostato su invisibile.
-   Per i sistemi 32-bit e FreeCAD 0.16.6706, dopo un tentativo di installazione, gli ambienti aggiuntivi potrebbero non essere disponibili. In questo caso
    -   tenere aperto il [pannello Report](report_view/it.md) mentre si avvia FreeCAD, e leggere l\'errore,
    -   vedere nel forum questa discussione: [Assembly2 in Version: 0.16.5602 (Git)](http://forum.freecadweb.org/viewtopic.php?t=12839#p102933)



---
⏵ [documentation index](../README.md) > [External Workbenches](Category_External Workbenches.md) > [Addons](Category_Addons.md) > How to install additional workbenches/it
