# Installing on Windows/it
{{docnav/it
|[Funzionalità](Feature_list/it.md)
|[Installare in Linux](Installing_on_Linux/it.md)
}}


{{TOCright}}

## Installazione Standard 

Il modo più semplice per installare l\'ultima versione stabile di FreeCAD è di utilizzare l\'installer.


{{DownloadWindowsStable}}

Se si desidera scaricare una versione di sviluppo, che potrebbe essere instabile, vedere la pagina [Weekly builds download](https   *//github.com/FreeCAD/FreeCAD-Bundle/releases/tag/weekly-builds).

Dopo aver scaricato l\'installer, fare doppio clic su di esso per avviare il processo di installazione.

Più avanti sono riportate ulteriori informazioni sul alcune opzioni tecniche. Ma la maggior parte degli utenti necessita solo dell\'installer. Al termine dell\'installazione leggere la pagina [Per iniziare](Getting_started/it.md).

## Installazione per tutti gli utenti in ambiente Windows 

Di default FreeCAD verrà installato per l\'utente che esegue l\'installazione. Se l\'utente ha permessi per il solo utente, il percorso d\'installazione è   *

   *   
    **C   *Users\<username>\AppData\Local\Programs\FreeCAD X.YY**
    

Se l\'installer è eseguito da un utente amministratore, o se lo esegui come amministratore, puoi scegliere se FreeCAD deve essere installato per tutti gli utenti del sistema o solo per te. Il default è per tutti gli utenti.

Se installato per tutti gli utenti, il percorso di default è   *

   *   
    **C   *Program Files\FreeCAD X.YY**
    

## Installazione in modalità silente 

Per installare FreeCAD in modalità silente, puoi eseguire l\'installer dalla riga di comando.


{{Code|lang=text|code=
FreeCAD-~.exe /S
}}

Le impostazioni di default verranno utilizzate per tutte le opzioni. Si può specificare un percorso d\'installazione personalizzato in questo modo   *


{{Code|lang=text|code=
FreeCAD-~.exe /S /D=A path to FreeCAD with spaces
}}

Di default, anche con installazioni in modalità silente, ci sarà un breve avviso quando l\'installer viene verificato per eventuali corruzioni. Questo è detto controllo ciclico di ridondanza e richiede normalmente pochi secondi. Per disabilitare il controllo di corruzione   *


{{Code|lang=text|code=
FreeCAD-~.exe /S /NCRC
}}

Notare che questa selezione {{Incode|/NCRC}} \"non è raccomandata\" perché il controllo di corruzione assicura che l\'installer sia stato completamente scaricato.

## Chocolatey

Si consiglia vivamente di utilizzare un gestore di pacchetti come Chocolatey per mantenere aggiornato il software. È possibile installare Chocolatey seguendo [queste istruzioni](https   *//chocolatey.org/install) e quindi aprire un terminale PowerShell come amministratore ed eseguire   *


{{Code|lang=text|code=
choco install freecad
}}

di tanto in tanto si può aggiornare il proprio software con


{{Code|lang=text|code=
choco upgrade freecad
}}

Questo otterrà l\'ultima versione disponibile dal repository Chocolatey. In caso di problemi con il pacchetto Chocolatey, è possibile contattare i manutentori su [questa pagina](https   *//chocolatey.org/packages/freecad).

## Disinstallazione

Per disinstallare FreeCAD è preferibile utilizzare gli strumenti di Windows per la disinstallazione del software. In alternativa puoi eseguire l\'uninstaller direttamente. Questo è il file   *

   *   
    **Uninstall-FreeCAD.exe**
    

Si trova nella cartella dove FreeCAD è installato.

L\'uninstaller può anche essere eseguito in modalità silente dalla riga di comando.


{{Code|lang=text|code=
Uninstall-FreeCAD.exe /S}}

Notare che la disinstallazione silente fallisce se c\'è un\'instanza aperta di FreeCAD, anche se l\'istanza non è quella della versione che sta per essere disinstallata.


{{docnav/it
|[Funzionalità](Feature_list/it.md)
|[Installare in Linux](Installing_on_Linux/it.md)
}}



---
![](images/Right_arrow.png) [documentation index](../README.md) > Installing on Windows/it
