

## File della Guida di FreeCAD 


<div class="mw-translate-fuzzy">

La documentazione offline di FreeCAD è costruita dal wiki di FreeCAD usando gli script. Il file è cresciuto fino a superare i 100 MB. Questi file di grandi dimensioni non fanno parte dei programmi di installazione e degli eseguibili di FreeCAD, ma possono essere installati separatamente come documentato qui.


</div>

Le traduzioni della community sono incoraggiate, quindi la documentazione offline è ora disponibile anche in francese e italiano. Altre lingue possono trovarsi in diverse fasi di avanzamento.

## Scaricare i file di aiuto 

Una documentazione offline funzionante è costituita da almeno due file: {{FileName|freecad.qhc}} la configurazione Qt del file di aiuto e {{FileName|freecad.qch}} il file di aiuto Qt compresso. Sono uniti in un archivio ZIP.


<div class="mw-translate-fuzzy">

I file della guida possono essere scaricati da: <https://github.com/FreeCAD/FreeCAD/releases/download/0.18.1/FreeCAD.0_18.Offline.Doc.7z>


</div>

In futuro potranno essere installati da FreeCAD con [Addon Manager](Addon_Manager/it.md).

I file della guida hanno sempre gli stessi nomi: {{FileName|freecad.qhc}} e {{FileName|freecad.qch}}. Per avere una versione diversa dei file della guida, è necessario installarli in directory diverse. In caso di download manuale, è sufficiente archiviare il file zip localmente ed estrarre l\'archivio nella directory desiderata.

## Registrare la documentazione 

Il sistema di documentazione di FreeCAD utilizza Qt Assistant. Nel caso in cui il proprio sistema operativo non abbia Qt Assistant, bisogna installarlo prima.

L\'organizzazione attuale della guida offline consente di attivare solo un file della guida. Non è quindi possibile avere file di aiuto in diverse lingue accessibili contemporaneamente da FreeCAD.

Per rendere attiva un\'altra documentazione di FreeCAD, è necessario applicare i seguenti passaggi:

-   In FreeCAD fare clic nel menu **Aiuto → Aiuto**. Dovrebbe aprirsi il programma Qt Assistant.
-   In Qt-assistant cliccare sul menu **Modifica → Preferenze**.
-   Nella finestra di dialogo delle preferenze fare clic sulla scheda **Documentazione**.
-   Nell\'elenco della documentazione registrata selezionare `org.freecad.usermanual` e fare clic sul pulsante **Rimuovi**.
-   Chiudere la finestra di dialogo con **OK**, ma non chiudere Qt-assistant. Questo è importante, altrimenti non verrà registrato un altro file di aiuto.
-   Aprire nuovamente la finestra di dialogo delle preferenze tramite il menu **Modifica → Preferenze**.
-   Selezionare la scheda della documentazione e fai clic sul pulsante **Aggiungi...**.
-   Nella finestra di dialogo, cercare il nuovo file della guida {{FileName|freecad.qch}} e selezionarlo.
-   Chiudere la finestra di dialogo confermando la selezione. Ora la scheda **Documentazione** nelle preferenze dovrebbe avere di nuovo una riga con `org.freecad.usermanual`.
-   Chiudere le **Preferenze** con **OK**.
-   Ora si dovrebbe avere la nuova documentazione disponibile nell\'assistente Qt, accessibile da FreeCAD.

## A Note About Ubuntu 

Difficulties may arise when trying to install the documentation packages on Ubuntu (for example, `freecad-doc` or `freecad-daily-doc`). If this is found to be the case, then executing the following steps will enable you to have offline documentation.

-   Download the {{FileName|freecad.qhc}} and {{FileName|freecad.qch}} help files from <https://github.com/FreeCAD/FreeCAD/releases/download/0.19.2/FreeCAD.0_19.Offline.Doc.7z> and extract them using 7zip.
-   Alternatively, you can instead get the development versions of the {{FileName|freecad.qhc}} and {{FileName|freecad.qch}} help files from [GitHub](https://github.com/FreeCAD/FreeCAD/tree/master/src/Doc). You will need to [concatenate](http://man7.org/linux/man-pages/man1/cat.1.html) the .part files together: `cat freecad.qch.part00 freecad.qch.part01 freecad.qch.part02 freecad.qch.part03 > freecad.qch`.
-   With administrative privileges (e.g., `sudo`), copy or move {{FileName|freecad.qhc}} and {{FileName|freecad.qch}} to {{FileName|/usr/share/doc/freecad-doc/}}. If you are using `freecad-daily`, this will instead be {{FileName|/usr/share/doc/freecad-daily-doc/}}.



