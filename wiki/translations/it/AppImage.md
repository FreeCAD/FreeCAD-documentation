# AppImage/it
**A partire dal 7 luglio 2019, la comunità di FreeCAD ha segnalato che il download di AppImages da Github sembra terminare prima del completamento. Non sappiamo perché accade questo. In questo caso, provare a scaricare di nuovo. Ci vogliono alcuni tentativi. Una pratica consigliata è quella di utilizzare la [https://wiki.freecadweb.org/AppImage/it#Aggiornamento_automatico funzione di aggiornamento automatico] di AppImage, che ripristina il download dal punto in cui si è interrotto.
**


{{TOCright}}

## Che cos\'è una AppImage? 

![](images/AppImage-logo.png ) **Package once and run everywhere. Reach users on all major Linux desktop distributions.**

AppImage è un \"pacchetto binario universale\" destinato a distribuire un\'applicazione a qualsiasi distribuzione Linux. Maggiori informazioni al riguardo su [Appimage homepage](https://appimage.org) e [Wikipedia](https://en.wikipedia.org/wiki/AppImage).

Per eseguirlo, renderlo prima eseguibile, quindi digitare il percorso relativo o completo.


```python
chmod +x FreeCAD_xxx-x86_64.AppImage
./FreeCAD_xxx-x86_64.AppImage
```

Per altri tipi di installazione vedere [Download](Download/it.md).

## AppImages di FreeCAD 


<div class="mw-translate-fuzzy">


**Se i seguenti link di download non funzionano, scaricare manualmente i file dalla sezione "Assets" in [https://github.com/FreeCAD/FreeCAD/releases '''FreeCAD Github Releases''']**


</div>

  Stable                                                                                                                                                                                                                                                                                                              Development
  ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- ----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
  ![](images/AppImage-logo.png ) [0.19.3](https://github.com/FreeCAD/FreeCAD/releases/download/0.19.3/FreeCAD_0.19.3-Linux-Conda_glibc2.12-x86_64.AppImage) ([SHA256](https://github.com/FreeCAD/FreeCAD/releases/download/0.19.3/FreeCAD_0.19.3-Linux-Conda_glibc2.12-x86_64.AppImage-SHA256.txt))   ![](images/AppImage-logo.png ) \[<https://github.com/FreeCAD/FreeCAD-Bundle/releases/download/weekly-builds/FreeCAD_weekly-builds->{{:Template:Development-Version}}-Linux-Conda\_glibc2.12-x86\_64.AppImage {{:Template:Development-Version}}\] (\[<https://github.com/FreeCAD/FreeCAD-Bundle/releases/download/weekly-builds/FreeCAD_weekly-builds->{{:Template:Development-Version}}-Linux-Conda\_glibc2.12-x86\_64.AppImage-SHA256.txt SHA256\])

  : style=\"text-align: center; font-size: 150%; \| Available FreeCAD AppImages \|+

**Note importanti:**

-   Lo sviluppo avviene quotidianamente e rapidamente, il link di aggiornamento di AppImage è un obiettivo mobile.
-   Il link alla versione di sviluppo indicato sopra dovrebbe essere aggiornato perché viene aggiornato tramite uno script.
-   Molti utenti del forum utilizzano la versione di sviluppo.
-   Può essere eseguito sullo stesso sistema in parallelo con un\'altra versione di FreeCAD.
-   Gli utenti usano la versione dev per sfruttare le ultime funzionalità e correzioni di errori (poiché FreeCAD ha un lungo ciclo di rilascio). La usano anche per aiutare a testare e trovare i bug per stimolare lo sviluppo e il miglioramento di FreeCAD.

#### Avviso di cautela obbligatorio 

For the most part the development version is stable but of course it\'s important to add the obligatory statement to use it at your own risk. Though most people that utilize backups and \'save often\' do quite well.

## Aggiornamento automatico 

AppImage has a smart and economical way of updating. It calculates the difference between the new AppImage and the old one, and will only download the changes between their versions. In theory the user ends up downloading around 15% each time instead of an entirely new AppImage.

Automatic updating is done via several optional methods. Currently there are 4 methods, 2 through the graphical interface (GUI), and 2 through the command-line/terminal interface (CLI).

### Experimental in-app updating 

Thanks to the efforts of several key devs, there is an [ongoing effort](https://forum.freecadweb.org/viewtopic.php?f=8&t=44324) to integrate a feature that allows **self-updating the AppImage within FreeCAD** itself. Starting from FC 0.19.21514 there now exists an AppImage section found via **Edit → Preferences → AppImage**. Please test this capability and report your experience to the [forum discussion](https://forum.freecadweb.org/viewtopic.php?f=8&t=44324).

### GUI method 1 (official) 

This is the official AppImageUpdate GUI application.

1.  Download [AppImageUpdate-x86\_64.AppImage](https://github.com/AppImage/AppImageUpdate/releases/download/continuous/AppImageUpdate-x86_64.AppImage).
2.  Make it executable by right clicking on the file, going in to properties and \"Run as an executable\".
3.  Double click on the AppImage icon, a dialog box will appear and you\'ll be prompted to specify what AppImage you want to update.
4.  Specify the path to your existing AppImage.
5.  Once the AppImage is updated, press the button **Run updated AppImage**.

### GUI method 2 (unofficial) 

This is a sleeker 3rd-party unofficial version of AppImageUpdate named: **AppImageUpdater**. It is still in development (at the time of this wiki edit) but nevertheless, quite nice to use.

1.  Download [AppImageUpdater-\*-x86\_64.AppImage](https://github.com/antony-jr/AppImageUpdater/releases/tag/continuous)
2.  Make it executable: 
```pythonchmod +x AppImageUpdater*-x86_64.AppImage```
3.  Run it: 
```pythonsource AppImageUpdater*-x86_64.AppImage```
4.  Find your current FreeCAD AppImage and drag-drop it on to the AppImageUpdater

Result: Follow the AppImageUpdater prompts

### CLI method 1 (official) 

Run the following instructions in your terminal


```python
wget https://github.com/AppImage/AppImageUpdate/releases/download/continuous/appimageupdatetool-x86_64.AppImage
chmod +x ./appimageupdatetool-x86_64.AppImage
./appimageupdatetool.AppImage path/to/old/FreeCAD.AppImage
chmod +x path/to/updated/FreeCAD.AppImage
./path/to/updated/FreeCAD.AppImage
```

Notes:

-   The file names will be unique because of the version info is embedded in them. The above instructions are simplified for convenience.
-   Run `./appimageupdatetool-x86_64.AppImage --help` to learn about functionality like `--remove-old`, `--overwrite` and `--self-update`.
-   There is also an i386 version; see the [AppImageUpdate release](https://github.com/AppImage/AppImageUpdate/releases) page.

Todo: share a script that can be added as an alias or cron job.

### CLI method 2 (unofficial) 

Similarly to the Graphical methods having an official and unofficial approaches to downloading AppImages, the same applies to the command line. This is a sleeker 3rd-party command line option to download AppImages

1.  Download [appimageupdater-\*-x86\_64.AppImage](https://github.com/antony-jr/AppImageUpdater/releases/tag/continuous-cli)
2.  Make it executable: 
```pythonchmod +x appimageupdater*-x86_64.AppImage```
3.  Run it: 
```pythonsource appimageupdater*-x86_64.AppImage /path/to/old/FreeCAD-AppImage.AppImage```

**Result**: Updates specified AppImage file if update exists

# Experimental

## Fixing AppImage zsync 

It may happen that an AppImage won\'t update because it\'s target file changed in some way. Instead of downloading a whole new appimage, it\'s possible to rewrite the zsync file that is used by the AppImage to download the delta. More info can be found at <https://github.com/antony-jr/appimage-update-info-writer>.

This section needs more details.

## Downloading via Bittorrent 

An experimental feature that the FreeCAD packaging team is exploring (thanks to the work of Antony-jr) is being able to download an appimage delta of FreeCAD via bittorrent. The repository issue is at <https://github.com/FreeCAD/FreeCAD-Bundle/issues/49>

# Developer Section 


**Note:**

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

If you\'ve modified the code, and now want to re-package the AppImage with your latest changes, use the [appimagetool-x86\_64](https://github.com/AppImage/AppImageKit/releases/download/continuous/appimagetool-x86_64.AppImage) tool on the extracted file system.


```python
cd ..
wget "https://github.com/AppImage/AppImageKit/releases/download/continuous/appimagetool-x86_64.AppImage"
chmod +x appimagetool-x86_64.AppImage
./appimagetool-x86_64.AppImage squashfs-root
```

## Personalized AppImages 

Thanks to the work of **realthunder**, author of [App Link](App_Link.md) and [Assembly3 Workbench](Assembly3_Workbench.md), it is possible to build custom AppImages using a set of scripts.

This makes it very convenient to release images for a specific branch of the source code for others to test. Although AppImages only work on Linux, realthunder\'s scripts make it possible to generate AppImages also on Windows and MacOS.

The repository for these scripts is at _ for more details.

## Related

-   [Snap](Ubuntu_Snap.md) packages.
-   [Flatpak](Flatpak.md) packages.



_ _ _

---
[documentation index](../README.md) > [Packaging](Category_Packaging.md) > AppImage/it
