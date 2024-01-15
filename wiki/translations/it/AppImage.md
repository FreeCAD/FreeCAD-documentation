# AppImage/it
## Che cos\'è una AppImage? 

![](images/AppImage-logo.png ) **Impacchetta una volta ed esegui ovunque. Raggiungi gli utenti su tutte le principali distribuzioni desktop Linux.**

AppImage è un \"pacchetto binario universale\" destinato a distribuire un\'applicazione a qualsiasi distribuzione Linux. Maggiori informazioni al riguardo su [Appimage homepage](https://appimage.org) e [Wikipedia](https://en.wikipedia.org/wiki/AppImage).

Per eseguirlo, renderlo prima eseguibile, quindi digitare il percorso relativo o completo.


```python
chmod +x FreeCAD_xxx-x86_64.AppImage
./FreeCAD_xxx-x86_64.AppImage
```

Per altri tipi di installazione vedere [Download](Download/it.md).



## AppImages di FreeCAD 

  Stable                                                                                                                Development
   
  ![](images/AppImage-logo.png ) [v0.21.2](https://github.com/FreeCAD/FreeCAD-Bundle/releases/tag/0.21.2)   ![](images/AppImage-logo.png ) [Weekly build](https://github.com/FreeCAD/FreeCAD-Bundle/releases/tag/weekly-builds)

  : style=\"text-align: center; font-size: 150%; \| Available FreeCAD AppImages \|+

**Note importanti:**

-   Lo sviluppo avviene quotidianamente e rapidamente.
-   Molti utenti del forum utilizzano la versione di sviluppo.
-   Può essere eseguito sullo stesso sistema in parallelo con un\'altra versione di FreeCAD.
-   Gli utenti usano la versione dev per sfruttare le ultime funzionalità e correzioni di errori (poiché FreeCAD ha un lungo ciclo di rilascio). La usano anche per aiutare a testare e trovare i bug per stimolare lo sviluppo e il miglioramento di FreeCAD.



#### Avviso di cautela obbligatorio 

Per la maggior parte la versione di sviluppo è stabile ma ovviamente è importante aggiungere un avviso obbligatorio di cautela e utilizzarla a proprio rischio e pericolo. Anche se la maggior parte delle persone che la utilizzano giustamente fanno il backup e \"salvano spesso\".



## Aggiornamento automatico 

AppImage ha un modo intelligente ed economico di aggiornamento. Calcola la differenza tra il nuovo AppImage e quello vecchio e scaricherà solo le modifiche tra le loro versioni. In teoria l\'utente finisce per scaricare circa il 15% ogni volta invece di un AppImage completamente nuovo.

L\'aggiornamento automatico viene eseguito tramite diversi metodi opzionali. Attualmente ci sono 4 metodi, 2 attraverso l\'interfaccia grafica (GUI) e 2 attraverso l\'interfaccia a riga di comando / terminale (CLI).



### Aggiornamento sperimentale in-app 

Grazie agli sforzi di diversi sviluppatori chiave, c\'è uno [sforzo in corso](https://forum.freecadweb.org/viewtopic.php?f=8&t=44324) per integrare una funzionalità che consenta **auto-aggiornamento dell\'AppImage all\'interno FreeCAD** stesso. A partire da FC 0.19.21514 ora esiste una sezione AppImage trovata tramite **Modifica → Preferenze → AppImage**. Prova questa funzionalità e segnala la tua esperienza al [forum di discussione](https://forum.freecadweb.org/viewtopic.php?f=8&t=44324).



### Metodo GUI 1 (ufficiale) 

Questa è l\'applicazione GUI ufficiale di AppImageUpdate.

1.  Scaricare [AppImageUpdate-x86_64.AppImage](https://github.com/AppImage/AppImageUpdate/releases/download/continuous/AppImageUpdate-x86_64.AppImage).
2.  Renderlo eseguibile facendo clic con il pulsante destro del mouse sul file, accedendo alle proprietà e selezionando \"Eseguibile\".
3.  Fare doppio clic sull\'icona AppImage, verrà visualizzata una finestra di dialogo e verrà richiesto di specificare quale AppImage desideri aggiornare.
4.  Specificare il percorso della tua AppImage esistente.
5.  Una volta aggiornata l\'AppImage, premere il pulsante **Eseguire l'AppImage aggiornata**.



### Metodo GUI 2 (non ufficiale) 

Questa è una versione non ufficiale di terze parti più elegante di AppImageUpdate denominata: **AppImageUpdater**. È ancora in fase di sviluppo (al momento di questa modifica della wiki) ma è comunque abbastanza piacevole da usare.

1.  Scarica [AppImageUpdater-\*-x86_64.AppImage](https://github.com/antony-jr/AppImageUpdater/releases/tag/continuous)
2.  Rendilo eseguibile: 
```pythonchmod +x AppImageUpdater*-x86_64.AppImage```
3.  Eseguilo: 
```pythonsource AppImageUpdater*-x86_64.AppImage```
4.  Trova la tua AppImage di FreeCAD corrente e trascinala su AppImageUpdater

Risultato: segui le istruzioni di AppImageUpdater



### Metodo CLI 1 (ufficiale) 

Eseguire le seguenti istruzioni nel terminale


```python
wget https://github.com/AppImage/AppImageUpdate/releases/download/continuous/appimageupdatetool-x86_64.AppImage
chmod +x ./appimageupdatetool-x86_64.AppImage
./appimageupdatetool.AppImage path/to/old/FreeCAD.AppImage
chmod +x path/to/updated/FreeCAD.AppImage
./path/to/updated/FreeCAD.AppImage
```

Appunti:

-   I nomi dei file saranno univoci perché le informazioni sulla versione sono incorporate in essi. Le istruzioni sopra riportate sono semplificate per comodità.
-   Eseguire `./appimageupdatetool-x86_64.AppImage --help` per conoscere funzionalità come `--remove-old`, `--overwrite` e `- -autoaggiornamento`.
-   Esiste anche una versione i386; vedere la pagina [Versione di AppImageUpdate](https://github.com/AppImage/AppImageUpdate/releases).

Da fare: condividere uno script che può essere aggiunto come alias o job di [cron](https://en.wikipedia.org/wiki/Cron).



### Metodo CLI 2 (non ufficiale) 

Analogamente ai metodi grafici che hanno un approccio ufficiale e non ufficiale per scaricare AppImages, lo stesso vale per la riga di comando. Questa è un\'opzione della riga di comando di terze parti più elegante per scaricare AppImages.

1.  Scaricare [appimageupdater-\*-x86_64.AppImage](https://github.com/antony-jr/AppImageUpdater/releases/tag/continuous-cli)
2.  Renderlo eseguibile: 
```pythonchmod +x appimageupdater*-x86_64.AppImage```
3.  Eseguirlo: 
```pythonsource appimageupdater*-x86_64.AppImage /path/to/old/FreeCAD-AppImage.AppImage```

**Risultato**: Aggiornare il file AppImage specificato se l\'aggiornamento esiste



# Sperimentale



## Riparare l\'AppImage zsync 

Può succedere che un\'AppImage non si aggiorni perché il file di destinazione è cambiato in qualche modo. Invece di scaricare un\'AppImage completamente nuova, è possibile riscrivere il file zsync utilizzato da AppImage per scaricare il delta. Maggiori informazioni sono disponibili su <https://github.com/antony-jr/appimage-update-info-writer>.

Questa sezione necessita di maggiori dettagli.



## Download tramite Bittorrent 

Una funzionalità sperimentale che il team per il packaging di FreeCAD sta esplorando (grazie al lavoro di Antony-jr) è la possibilità di scaricare un\'appimage delta di FreeCAD tramite bittorrent. L\'issue del repository è su <https://github.com/FreeCAD/FreeCAD-Bundle/issues/49>



# Sezione sviluppatori 


**Nota:**

le seguenti sezioni sono destinate agli sviluppatori



## Unpacking di AppImages 

Un aspetto molto utile di FreeCAD è che la maggior parte di esso è costruita in [Python](Python/it.md), che non necessita di essere compilato manualmente come C++. In sostanza, un file Python può essere modificato e al riavvio di FreeCAD tali modifiche verranno integrate nell\'applicazione. Uno sviluppatore può lavorare rapidamente sull\'ultima versione di FreeCAD utilizzando questa tecnica e un\'AppImage. Inoltre, l\'utilizzo di un\'AppImage non modifica in alcun modo l\'ambiente del tuo sistema, ovvero non viene installato nulla e non vengono modificate variabili ambientali.



### Modifica di AppImages 

Un\'AppImage incorpora un file system al suo interno con tutto ciò che è necessario per eseguire l\'applicazione. Per modificarlo è necessario estrarre il file system.


```python
./FreeCAD_xxx.AppImage --appimage-extract
cd squashfs-root/
```

Ora aprire i file sorgente Python richiesti nel tuo editor di codice preferito, modificarli e salvarli. Quindi eseguire l\'applicazione.


```python
./AppRun
```



### Repackaging di AppImages 

Se si è modificato il codice e quindi si desidera fare il re-package di AppImage con le ultime modifiche, utilizzare [appimagetool- x86_64](https://github.com/AppImage/AppImageKit/releases/download/continuous/appimagetool-x86_64.AppImage) sul file system estratto.


```python
cd ..
wget "https://github.com/AppImage/AppImageKit/releases/download/continuous/appimagetool-x86_64.AppImage"
chmod +x appimagetool-x86_64.AppImage
./appimagetool-x86_64.AppImage squashfs-root
```



## AppImages personalizzate 

Grazie al lavoro di **realthunder**, autore di [App Link](App_Link/it.md) e [Assembly3 Workbench](Assembly3_Workbench/it.md), è possibile creare AppImage personalizzate utilizzando una serie di script.

Ciò rende molto conveniente rilasciare immagini per un ramo specifico del codice sorgente affinché altri possano testarle. Sebbene AppImages funzioni solo su Linux, gli script di realthunder consentono di generare AppImages anche su Windows e MacOS.

Il repository per questi script è su [realthunder/FreeCADMakeImage](https://github.com/realthunder/FreeCADMakeImage). Si prega di leggere il [Readme.md](https://github.com/realthunder/FreeCADMakeImage/blob/master/Readme.md) per maggiori dettagli.



## Correlati

-   Pacchetti [Snap](Ubuntu_Snap/it.md).
-   Pacchetti [Flatpak](Flatpak/it.md).



---
⏵ [documentation index](../README.md) > [Packaging](Category_Packaging.md) > [Developer Documentation](Category_Developer Documentation.md) > [Testing](Category_Testing.md) > AppImage/it
