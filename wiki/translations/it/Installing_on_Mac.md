# Installing on Mac/it
FreeCAD può essere installato in macOS da un pacchetto .dmg che è possibile trascinare nella cartella Applicazioni:


{{DownloadMacStable}}

e la build settimanale può essere scaricata da

<img alt="" src=images/Nightly.png  style="width:30px;">[Weekly](https://github.com/FreeCAD/FreeCAD-AppImage/releases/tag/weekly-builds)

Si può utilizzare un gestore di pacchetti come HomeBrew per mantenere aggiornato il software. Le istruzioni per installare HomeBrew possono essere visualizzate [qui](https://brew.sh/). Quando HomeBrew è installato potete semplicemente installare FreeCAD 0.18.4 attraverso il vostro terminale bash con


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

## Installazione semplice 

L\'installatore di FreeCAD viene fornito come pacchetto di installazione (.app) incluso in un file di immagine disco.

È possibile scaricare l\'ultima versione dell\'installatore dalla pagina [Download](Download/it.md). Dopo aver scaricato il file, basta montare l\'immagine, poi trascinarla nella cartella Applicazioni o in una cartella a scelta..

![](images/mac_installer_1.png )

Questo è tutto. Basta cliccare sulla app per lanciare FreeCAD. Se si riceve il messaggio \"FreeCAD non può essere aperto in quanto proviene da uno sviluppatore non identificato\", aprire la cartella (Applicazione) e fare clic destro sulla App quindi fare clic su apri e accettare di aprire l\'applicazione.

## Disinstallazione

Attualmente non c\'è un programma di disinstallazione per FreeCAD installato con dmg package. Per rimuovere completamente FreeCAD e tutti i componenti installati, trascinare i seguenti file e cartelle nel cestino:

-   In /Applications:
    -   FreeCAD

Se avete installato FreeCAD con homebrew utilizzate semplicemente il comando `brew uninstall freecad`. Tutto qui.

---
[documentation index](../README.md) > Installing on Mac/it
