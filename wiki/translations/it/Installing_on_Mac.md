


<div class="mw-translate-fuzzy">





</div>


<div class="mw-translate-fuzzy">

FreeCAD può essere installato su macOS nel pacchetto .dmg che è possibile trascinare nella cartella Applicazioni:


</div>


{{DownloadMacStable}}


<div class="mw-translate-fuzzy">

e la build notturna può essere scaricata da


</div>


<div class="mw-translate-fuzzy">

<img alt="" src=images/Nightly.png  style="width:30px;">[Nightly 19\_pre](https://github.com/FreeCAD/FreeCAD/releases/download/0.19_pre/FreeCAD_0.19-18589-OSX-x86_64-conda-Qt5-Py3.dmg)  [(sha256)](https://github.com/FreeCAD/FreeCAD/releases/download/0.19_pre/FreeCAD_0.19-18589-OSX-x86_64-conda-Qt5-Py3.dmg-SHA256.txt)


</div>


<div class="mw-translate-fuzzy">

Tuttavia, si consiglia vivamente di utilizzare un gestore di pacchetti come HomeBrew per mantenere aggiornato il software. Le istruzioni per installare HomeBrew possono essere visualizzate [qui](https://brew.sh/). Quando HomeBrew è installato potete semplicemente installare FreeCAD 0.18.4 attraverso il vostro terminale bash con


</div>


```python
brew install --cask freecad
```

e per utilizzare l\'ultima versione disponibile (0.19pre) su HomeBrew è possibile eseguire


```python
brew install freecad
```

Se ci sono problemi con l\'HomeBrew Cask o Formula puoi segnalarli a [qui](https://github.com/FreeCAD/homebrew-freecad).

Questa pagina descrive l\'uso e le caratteristiche del programma di installazione di FreeCAD. Essa comprende anche le istruzioni di disinstallazione.

Terminata l\'installazione, è possibile [iniziare](Getting_started/it.md)!

## Installazione semplice {#installazione_semplice}

L\'installatore di FreeCAD viene fornito come pacchetto di installazione (.app) incluso in un file di immagine disco.

È possibile scaricare l\'ultima versione dell\'installatore dalla pagina [Download](Download/it.md). Dopo aver scaricato il file, basta montare l\'immagine, poi trascinarla nella cartella Applicazioni o in una cartella a scelta..

![](images/mac_installer_1.png )

Questo è tutto. Basta cliccare sulla app per lanciare FreeCAD. Se si riceve il messaggio \"FreeCAD non può essere aperto in quanto proviene da uno sviluppatore non identificato\", aprire la cartella (Applicazione) e fare clic destro sulla App quindi fare clic su apri e accettare di aprire l\'applicazione.

## Disinstallazione

Attualmente non c\'è un programma di disinstallazione per FreeCAD installato con dmg package. Per rimuovere completamente FreeCAD e tutti i componenti installati, trascinare i seguenti file e cartelle nel cestino:

-   In /Applications:
    -   FreeCAD


<div class="mw-translate-fuzzy">

Se avete installato FreeCAD con homebrew utilizzate semplicemente il comando freecad di disinstallazione. Tutto qui.


</div>


<div class="mw-translate-fuzzy">





</div>



