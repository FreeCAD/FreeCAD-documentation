# Installing on Windows/it
{{docnav/it
|[Funzionalità](Feature_list/it.md)
|[Installare in Linux](Installing_on_Linux/it.md)
}}


{{TOCright}}

## Standard Installation 


<div class="mw-translate-fuzzy">

Il modo più semplice per **installare FreeCAD su Windows** è utilizzare il pacchetto di installazione scaricabile sopra. Questa pagina descrive l\'utilizzo e le funzionalità di \"NSIS Installer\" per ulteriori opzioni di installazione.


</div>


{{DownloadWindowsStable}}


<div class="mw-translate-fuzzy">

Se si desidera scaricare una versione di sviluppo (che potrebbe essere instabile), vedere la pagina [Download](Download/it.md).


</div>


<div class="mw-translate-fuzzy">

Dopo aver scaricato il file .exe (NSIS Installer), fare doppio clic su di esso per avviare il processo di installazione automatica.


</div>


<div class="mw-translate-fuzzy">

Più avanti sono riportate ulteriori informazioni sul alcune opzioni tecniche.
Tuttavia, la maggior parte degli utenti ha solo bisogno dei precedenti file .exe. Al termine dell\'installazione leggere la pagina [Per iniziare](Getting_started/it.md).


</div>

## Installation for all users of the Windows system 

By default FreeCAD will be installed for the user that executes the installer. If this user only has user permissions, the default installation path is   *

   *   
    **C   *Users\<username>\AppData\Local\Programs\FreeCAD X.YY**
    

If the installer is executed by an admin user, or you execute it as admin, you can choose if FreeCAD should be installed for all users of the system or just for you. The default is for all users.

If installed for all users, the default installation path is   *

   *   
    **C   *Program Files\FreeCAD X.YY**
    

## Silent Installation 

To install FreeCAD silently, you can execute the installer from the command line   *


{{Code|lang=text|code=
FreeCAD-~.exe /S
}}

Default settings will be used for all options. A custom installation path can be specified in this manner   *


{{Code|lang=text|code=
FreeCAD-~.exe /S /D=A path to FreeCAD with spaces
}}

By default, even with silent installations, there will be a short popup when the installer is checked for corruption. This so-called cyclic redundancy check only takes a few seconds at most. To disable this corruption check   *


{{Code|lang=text|code=
FreeCAD-~.exe /S /NCRC
}}

Note that this {{Incode|/NCRC}} flag is **not recommended** since the corruption check assures that the installer was e.g. completely downloaded.

## Chocolatey


<div class="mw-translate-fuzzy">

Tuttavia, si consiglia vivamente di utilizzare un gestore di pacchetti come Chocolatey per mantenere aggiornato il software. È possibile installare Chocolatey seguendo [queste istruzioni](https   *//chocolatey.org/install) e quindi aprire un terminale PowerShell come amministratore ed eseguire   *


</div>


{{Code|lang=text|code=
choco install freecad
}}


<div class="mw-translate-fuzzy">

di tanto in tanto si può aggiornare il proprio software con


</div>


{{Code|lang=text|code=
choco upgrade freecad
}}


<div class="mw-translate-fuzzy">

per ottenere l\'ultima versione disponibile sul repository Chocolatey. In caso di problemi con il pacchetto chocolatey, è possibile contattare i manutentori su [questa pagina](https   *//chocolatey.org/packages/freecad).


</div>

## Disinstallazione

To uninstall FreeCAD it is preferable to use the Windows tools for uninstalling software. Alternatively you can execute the uninstaller directly. This is the file   *

   *   
    **Uninstall-FreeCAD.exe**
    

You can find it in the folder where FreeCAD is installed.

The uninstaller can also be executed silently using the command line   *


{{Code|lang=text|code=
Uninstall-FreeCAD.exe /S}}

Note that (silent) uninstallation will fail if there is a running instance of FreeCAD, even if that instance is not the version being uninstalled.


{{docnav/it
|[Funzionalità](Feature_list/it.md)
|[Installare in Linux](Installing_on_Linux/it.md)
}}



---
![](images/Right_arrow.png) [documentation index](../README.md) > Installing on Windows/it
