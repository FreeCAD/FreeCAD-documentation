 {{TutorialInfo/it|Topic=Programmazione|Level=Medio|Time=15 minuti|FCVersion=Tutte|Author=[r-frank](User:R-Frank.md)|Files=none}}

## Descrizione

Gli utenti esperti hanno esteso FreeCAD con vari [ambienti di lavoro esterni](external_workbenches/it.md) personalizzati, che non sono integrati nel codice sorgente di FreeCAD, ma che sono facili da implementare in una distribuzione FreeCAD esistente. Qui sono descritti i metodi di installazione per i diversi sistemi operativi.


**Nota:**

a partire dalla versione 0.17, FreeCAD include un <img alt="" src=images/AddonManager.svg  style="width:24px;"> [Addon Manager](Std_AddonMgr/it.md) nel menu **Strumenti → Addon manager**, che permette di installare sia macro che ambienti di lavoro. Le istruzioni seguenti sono necessarie solo si desidera installare manualmente un ambiente. Ciò potrebbe essere necessario se per qualche motivo Addon Manager non funziona ma si ha accesso all\'ambiente scaricato come pacchetto {{FileName|.zip}}.


<div class="mw-collapsible mw-collapsed toccolours">

## Installazione in Windows 

Come installare ulteriori ambienti e componenti aggiuntivi su Windows


<div class="mw-collapsible-content">

### Obsoleto


**Note:**

l\'uso di \"addons-installer\" non è più consigliato. Si consiglia di utilizzare [Addon Manager](Addon_Manager/it.md) in tutti i sistemi.

Usare [addons-installer da Github](https://github.com/FreeCAD/FreeCAD-addons).

Durante il Google Summer of Code 2016 lo studente Mandeep Singh ha iniziato a lavorare su una versione migliore
([disponibile qui](https://github.com/mandeeps708/PluginManager)) ma tale versione necessita di ulteriori lavori prima di poter essere completamente integrata in FreeCAD.

### Installazione manuale 


**Note:**

Dopo l\'introduzione di [Addon Manager](Addon_Manager/it.md) questo metodo è possibile ma non necessario. Tuttavia, queste informazioni potrebbero essere ancora utili per alcuni.

-   Scaricare il workbench da github cliccando sul pulsante **Clone** o **Download** sulla pagina GitHub (in alto a destra) e scegliendo \"Download ZIP\"
-   Decomprimere l\'archivio scaricato sul disco rigido locale
-   All\'interno di FreeCAD, individuare il percorso delle macro scegliendo **Modifica > Preferenze > Generale > Macro** e vedere quale è il "Percorso Macro"
-   Supponendo che il vostro login di Windows sia "*User-Name*" il percorso predefinito delle macro è "C:\\User-Name\\Appdata\\Roaming\\FreeCAD"
-   All\'interno della directory delle macro creare (se non è ancora presente) una cartella chiamata "{{FileName|Mod}}"
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

### Usando git 

Aggiungere il [community-ppa](https://launchpad.net/~freecad-community/+archive/ubuntu/ppa) al ppa-manager.
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


**Note:**

Dopo l\'introduzione di [Addon Manager](Addon_Manager/it.md) questo metodo è possibile ma non necessario. Tuttavia, queste informazioni potrebbero essere ancora utili per alcuni.

-   Scaricare il workbench da github cliccando sul pulsante **Clone** o **Download** sulla pagina GitHub (in alto a destra) e scegliendo \"Download ZIP\"
-   Decomprimere l\'archivio scaricato sul disco rigido locale
-   All\'interno di FreeCAD, individuare il percorso delle macro scegliendo **Modifica > Preferenze > Generale > Macro** e vedere quale è il "Percorso Macro"
-   Per impostazione predefinita, la directory delle macro è la directory (nascosta) **./.FreeCAD/** nella propria home-directory
-   All\'interno della directory delle macro creare (se non è ancora presente) una cartella chiamata "{{FileName|Mod}}"
-   All\'interno della cartella Mod/ creare una cartella con il nome dell\'ambiente, ad esempio "Curves"
-   Ora spostare i file decompressi e le sottocartelle del Workbench nella cartella dell\'ambiente appena creato
-   Dopo il riavvio di FreeCAD si dovrebbe avere una nuova voce nel menu a discesa nel [selettore degli ambienti](Std_Workbench/it.md)


</div>


</div>


<div class="mw-collapsible mw-collapsed toccolours">

## Installazione in Mac 

Come installare ulteriori ambienti e componenti aggiuntivi su MacOS


<div class="mw-collapsible-content">

### Installazione manuale 


**Note:**

Dopo l\'introduzione di [Addon Manager](Addon_Manager/it.md) questo metodo è possibile ma non necessario. Tuttavia, queste informazioni potrebbero essere ancora utili per alcuni.


<div class="mw-translate-fuzzy">

Per questo esempio, supponiamo di aver scelto [Curves](Curves_Workbench/it.md) come ambieente esterno che da installare:

-   Scaricare il repository git come file ZIP
-   Assumendo che FreeCAD sia installato in {{FileName|/Applications/FreeCAD/v0.xx}}, andare in {{FileName|/Applications/FreeCAD/v0.xx}} con il browser, e selezionare FreeCAD.app
-   Cliccare con il tasto destro del mouse e selezionare \"Show Package Contents\", appare una nuova scheda denominata \"Contents\"
-   Fare un singolo clic sulla cartella \"Contents\" e selezionare la cartella \"Mod\"
-   Nella cartella \"Mod\" creare una nuova cartella con il nome \"Curves\"
-   Decomprimere il repository scaricato nella cartella \"Contents/Mod/Curves\"


</div>


</div>


</div>

## Risoluzione dei problemi generali 

-   In Windows non utilizzare i caratteri speciali (ad esempio dieresi tedesca) per il nome utente, altrimenti FreeCAD non riconosce i file e le cartelle nel percorso delle macro.
-   Se è già stato impostato un nome utente con caratteri speciali, creare un nuovo nome utente o puntare il percorso macro a una directory che non utilizzi caratteri speciali.
-   Andare in **Strumenti → Personalizza → Ambienti** e assicurarsi che l\'ambiente non sia impostato su invisibile.
-   Per i sistemi 32-bit e FreeCAD 0.16.6706, dopo un tentativo di installazione, gli ambienti aggiuntivi potrebbero non essere disponibili. In questo caso
    -   tenere aperto il [pannello Report](report_view/it.md) mentre si avvia FreeCAD, e leggere l\'errore,
    -   vedere nel forum questa discussione: [Assembly2 in Version: 0.16.5602 (Git)](http://forum.freecadweb.org/viewtopic.php?t=12839#p102933)


 {{Powerdocnavi}}

[Category:External Workbenches{{\#translation:}}](Category:External_Workbenches.md) [Category:Addons{{\#translation:}}](Category:Addons.md)
