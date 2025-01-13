# Installing Helpfile/it
## Mddulo Aiuto 

**Nota:** i file della guida offline di FreeCAD, descritti di seguito, verranno ritirati. Il sistema di aiuto di FreeCAD è ora gestito dal [Help Addon](https://github.com/yorikvanhavre/FreeCAD-Help), che si può installare tramite [Addon manager](Std_AddonMgr/it.md). L\'Help Addon è in grado di accedere alla documentazione online, senza bisogno di scaricare nulla, o ad una copia scaricabile offline della documentazione, che può essere installata anche tramite l\'Addon manager.



## File della Guida di FreeCAD 

La documentazione offline di FreeCAD è costruita dal wiki di FreeCAD usando gli script. Il file è cresciuto fino a superare i 220 MB. Questi file di grandi dimensioni non fanno parte dei programmi di installazione e degli eseguibili di FreeCAD, ma possono essere installati separatamente come documentato qui.

Le traduzioni della community sono incoraggiate, quindi la documentazione offline è ora disponibile anche in francese e italiano. Altre lingue possono trovarsi in diverse fasi di avanzamento.



## Scaricare i file di aiuto 

Una documentazione offline funzionante è costituita da almeno due file: **freecad.qhc** la configurazione Qt del file di aiuto e **freecad.qch** il file di aiuto Qt compresso. Sono uniti in un archivio ZIP.

I file della guida possono essere scaricati da: <https://github.com/FreeCAD/FreeCAD/releases/download/0.19.2/FreeCAD.0_19.Offline.Doc.7z>

In futuro potranno essere installati da FreeCAD con [Addon Manager](Std_AddonMgr/it.md).

I file della guida hanno sempre gli stessi nomi: **freecad.qhc** e **freecad.qch**. Per avere una versione diversa dei file della guida, è necessario installarli in directory diverse. In caso di download manuale, è sufficiente archiviare il file zip localmente ed estrarre l\'archivio nella directory desiderata.



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
-   Nella finestra di dialogo, cercare il nuovo file della guida **freecad.qch** e selezionarlo.
-   Chiudere la finestra di dialogo confermando la selezione. Ora la scheda **Documentazione** nelle preferenze dovrebbe avere di nuovo una riga con `org.freecad.usermanual`.
-   Chiudere le **Preferenze** con **OK**.
-   Ora si dovrebbe avere la nuova documentazione disponibile nell\'assistente Qt, accessibile da FreeCAD.



## Una nota su Ubuntu 

Possono sorgere difficoltà quando si tenta di installare i pacchetti di documentazione su Ubuntu (ad esempio, `freecad-doc` o `freecad-daily-doc`). In tal caso, l\'esecuzione dei passaggi seguenti consentirà di disporre della documentazione offline.

-   Scaricare i file di aiuto **freecad.qhc** e **freecad.qch** da <https://github.com/FreeCAD/FreeCAD/releases/download/0.19.2/FreeCAD.0_19.Offline> .Doc.7z ed estrarli usando 7zip.
-   In alternativa, è possibile ottenere le versioni di sviluppo dei file di aiuto **freecad.qhc** e **freecad.qch** da [/src/Doc GitHub](https://github.com/FreeCAD/FreeCAD/tree/master). Si dovranno [concatenare](http://man7.org/linux/man-pages/man1/cat.1.html) i file .part insieme: `cat freecad.qch.part00 freecad.qch.part01 freecad .qch.part02 freecad.qch.part03 > freecad.qch`.
-   Con privilegi di amministratore (es. `sudo`), copiare o spostare **freecad.qhc** e **freecad.qch** in **/usr/share/doc/ freecad-doc/**. Se si stà usando `freecad-daily`, questo sarà invece **/usr/share/doc/freecad-daily-doc/**.



---
⏵ [documentation index](../README.md) > Installing Helpfile/it
