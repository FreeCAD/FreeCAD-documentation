# AppImage/it
**A partire dal 7 luglio 2019, la comunità di FreeCAD ha segnalato che il download di AppImages da Github sembra terminare prima del completamento. Non sappiamo perché accade questo. In questo caso, provare a scaricare di nuovo. Potrebbero essere necessari alcuni tentativi. Una pratica consigliata è quella di utilizzare la [https   *//wiki.freecadweb.org/AppImage/it#Aggiornamento_automatico funzione di aggiornamento automatico] di AppImage, che ripristina il download dal punto in cui si è interrotto.
**


{{TOCright}}

## Che cos\'è una AppImage? 

![](images/AppImage-logo.png ) **Impacchetta una volta ed esegui ovunque. Raggiungi gli utenti su tutte le principali distribuzioni desktop Linux.**

AppImage è un \"pacchetto binario universale\" destinato a distribuire un\'applicazione a qualsiasi distribuzione Linux. Maggiori informazioni al riguardo su [Appimage homepage](https   *//appimage.org) e [Wikipedia](https   *//en.wikipedia.org/wiki/AppImage).

Per eseguirlo, renderlo prima eseguibile, quindi digitare il percorso relativo o completo.


```python
chmod +x FreeCAD_xxx-x86_64.AppImage
./FreeCAD_xxx-x86_64.AppImage
```

Per altri tipi di installazione vedere [Download](Download/it.md).

## AppImages di FreeCAD 


**'''Nota   *''' Le versioni di sviluppo sono ora ospitate su [https   *//github.com/FreeCAD/FreeCAD-Bundle/releases/tag/weekly-builds '''FreeCAD-Bundle'''] github repo.<br/>Se i link per il download qui sotto non funzionano, si prega di scaricare manualmente i file dalla sezione "Assets" espansa del link sopra**

  Stable                                                                                                                Development
   
  ![](images/AppImage-logo.png ) [v0.20.1](https   *//github.com/FreeCAD/FreeCAD-Bundle/releases/tag/0.20.1)   ![](images/AppImage-logo.png ) [Weekly build](https   *//github.com/FreeCAD/FreeCAD-Bundle/releases/tag/weekly-builds)

     * style=\"text-align   * center; font-size   * 150%; \| Available FreeCAD AppImages \|+

**Note importanti   ***

-   Lo sviluppo avviene quotidianamente e rapidamente, il link di aggiornamento di AppImage è un obiettivo mobile.
-   Il link alla versione di sviluppo indicato sopra dovrebbe essere aggiornato perché viene aggiornato tramite uno script.
-   Molti utenti del forum utilizzano la versione di sviluppo.
-   Può essere eseguito sullo stesso sistema in parallelo con un\'altra versione di FreeCAD.
-   Gli utenti usano la versione dev per sfruttare le ultime funzionalità e correzioni di errori (poiché FreeCAD ha un lungo ciclo di rilascio). La usano anche per aiutare a testare e trovare i bug per stimolare lo sviluppo e il miglioramento di FreeCAD.

#### Avviso di cautela obbligatorio 

Per la maggior parte la versione di sviluppo è stabile ma ovviamente è importante aggiungere un obbligatorio avviso di cautela utilizzarla a proprio rischio. Anche se la maggior parte delle persone che utilizzano backup e \"salvano spesso\" fanno abbastanza bene.

## Aggiornamento automatico 

AppImage ha un modo intelligente ed economico di aggiornamento. Calcola la differenza tra il nuovo AppImage e quello vecchio e scaricherà solo le modifiche tra le loro versioni. In teoria l\'utente finisce per scaricare circa il 15% ogni volta invece di un AppImage completamente nuovo.

L\'aggiornamento automatico viene eseguito tramite diversi metodi opzionali. Attualmente ci sono 4 metodi, 2 attraverso l\'interfaccia grafica (GUI) e 2 attraverso l\'interfaccia a riga di comando / terminale (CLI).

### Aggiornamento sperimentale in-app 

Thanks to the efforts of several key devs, there is an [ongoing effort](https   *//forum.freecadweb.org/viewtopic.php?f=8&t=44324) to integrate a feature that allows **self-updating the AppImage within FreeCAD** itself. Starting from FC 0.19.21514 there now exists an AppImage section found via **Edit → Preferences → AppImage**. Please test this capability and report your experience to the [forum discussion](https   *//forum.freecadweb.org/viewtopic.php?f=8&t=44324).

### GUI method 1 (official) 

This is the official AppImageUpdate GUI application.

1.  Download [AppImageUpdate-x86_64.AppImage](https   *//github.com/AppImage/AppImageUpdate/releases/download/continuous/AppImageUpdate-x86_64.AppImage).
2.  Make it executable by right clicking on the file, going in to properties and \"Run as an executable\".
3.  Double click on the AppImage icon, a dialog box will appear and you\'ll be prompted to specify what AppImage you want to update.
4.  Specify the path to your existing AppImage.
5.  Once the AppImage is updated, press the button **Run updated AppImage**.

### GUI method 2 (unofficial) 

This is a sleeker 3rd-party unofficial version of AppImageUpdate named   * **AppImageUpdater**. It is still in development (at the time of this wiki edit) but nevertheless, quite nice to use.

1.  Download [AppImageUpdater-\*-x86_64.AppImage](https   *//github.com/antony-jr/AppImageUpdater/releases/tag/continuous)
2.  Make it executable   * 
```pythonchmod +x AppImageUpdater*-x86_64.AppImage```
3.  Run it   * 
```pythonsource AppImageUpdater*-x86_64.AppImage```
4.  Find your current FreeCAD AppImage and drag-drop it on to the AppImageUpdater

Result   * Follow the AppImageUpdater prompts

### CLI method 1 (official) 

Run the following instructions in your terminal


```python
wget https   *//github.com/AppImage/AppImageUpdate/releases/download/continuous/appimageupdatetool-x86_64.AppImage
chmod +x ./appimageupdatetool-x86_64.AppImage
./appimageupdatetool.AppImage path/to/old/FreeCAD.AppImage
chmod +x path/to/updated/FreeCAD.AppImage
./path/to/updated/FreeCAD.AppImage
```

Notes   *

-   The file names will be unique because of the version info is embedded in them. The above instructions are simplified for convenience.
-   Run `./appimageupdatetool-x86_64.AppImage --help` to learn about functionality like `--remove-old`, `--overwrite` and `--self-update`.
-   There is also an i386 version; see the [AppImageUpdate release](https   *//github.com/AppImage/AppImageUpdate/releases) page.

Todo   * share a script that can be added as an alias or [1](https   *//en.wikipedia.org/wiki/Cron%7Ccron) job.

### CLI method 2 (unofficial) 

Similarly to the Graphical methods having an official and unofficial approaches to downloading AppImages, the same applies to the command line. This is a sleeker 3rd-party command line option to download AppImages.

1.  Download [appimageupdater-\*-x86_64.AppImage](https   *//github.com/antony-jr/AppImageUpdater/releases/tag/continuous-cli)
2.  Make it executable   * 
```pythonchmod +x appimageupdater*-x86_64.AppImage```
3.  Run it   * 
```pythonsource appimageupdater*-x86_64.AppImage /path/to/old/FreeCAD-AppImage.AppImage```

**Result**   * Updates specified AppImage file if update exists

# Experimental

## Fixing AppImage zsync 

It may happen that an AppImage won\'t update because it\'s target file changed in some way. Instead of downloading a whole new AppImage, it\'s possible to rewrite the zsync file that is used by the AppImage to download the delta. More info can be found at <https   *//github.com/antony-jr/appimage-update-info-writer>.

This section needs more details.

## Downloading via Bittorrent 

An experimental feature that the FreeCAD packaging team is exploring (thanks to the work of Antony-jr) is being able to download an appimage delta of FreeCAD via bittorrent. The repository issue is at <https   *//github.com/FreeCAD/FreeCAD-Bundle/issues/49>

# Developer Section 


**Note   ***

the following sections are intended for developers

## Unpacking AppImages 

A very convenient aspect of FreeCAD is that a majority of it is built in [Python](Python.md), which doesn\'t need to be manually compiled like C++. Essentially, a Python file can be modified, and upon restarting FreeCAD those changes will be integrated into the application. A developer can quickly work on the latest FreeCAD release using this technique and an AppImage. Moreover, using an AppImage doesn\'t modify your system\'s environment in any way, that is, nothing is installed and no environmental variables are modified.

### Modifying AppImages 

An AppImage embeds a file system in it with everything that is required to run the application. In order to modify it, the file system needs to be extracted.


```python
./FreeCAD_xxx.AppImage --appimage-extract
cd squashfs-root/
```

Now open the required Python source files in your preferred code editor, modify them, and save them. Then run the application.


```python
./AppRun
```

### Repackaging AppImages 

If you\'ve modified the code, and now want to re-package the AppImage with your latest changes, use the [appimagetool-x86_64](https   *//github.com/AppImage/AppImageKit/releases/download/continuous/appimagetool-x86_64.AppImage) tool on the extracted file system.


```python
cd ..
wget "https   *//github.com/AppImage/AppImageKit/releases/download/continuous/appimagetool-x86_64.AppImage"
chmod +x appimagetool-x86_64.AppImage
./appimagetool-x86_64.AppImage squashfs-root
```

## Personalized AppImages 

Thanks to the work of **realthunder**, author of [App Link](App_Link.md) and [Assembly3 Workbench](Assembly3_Workbench.md), it is possible to build custom AppImages using a set of scripts.

This makes it very convenient to release images for a specific branch of the source code for others to test. Although AppImages only work on Linux, realthunder\'s scripts make it possible to generate AppImages also on Windows and MacOS.

The repository for these scripts is at [realthunder/FreeCADMakeImage](https   *//github.com/realthunder/FreeCADMakeImage). Please read the [Readme.md](https   *//github.com/realthunder/FreeCADMakeImage/blob/master/Readme.md) for more details.

## Related

-   [Snap](Ubuntu_Snap.md) packages.
-   [Flatpak](Flatpak.md) packages.



[Category   *Packaging](Category_Packaging.md) [Category   *Developer Documentation](Category_Developer_Documentation.md) [Category   *Testing](Category_Testing.md)



---
![](images/Right_arrow.png) [documentation index](../README.md) > [Packaging](Category_Packaging.md) > [Developer Documentation](Category_Developer Documentation.md) > [Testing](Category_Testing.md) > AppImage/it
