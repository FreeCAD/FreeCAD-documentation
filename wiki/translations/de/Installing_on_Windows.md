# Installing on Windows/de
{{docnav/de
|[Funktionalitäten](Feature_list/de.md)
|[ Installieren auf Linux](Install_on_Linux/de.md)
}}


{{TOCright}}

## Standard Installation 


<div class="mw-translate-fuzzy">

Der einfachste Weg um **FreeCAD unter Windows zu installieren**, ist durch Verwendung des herunterladbaren Installationspakets oben. Diese Seite beschreibt die Verwendung und die Funktionen des *NSIS Installierers* für weitere Installationsoptionen.


</div>


{{DownloadWindowsStable}}


<div class="mw-translate-fuzzy">

Wenn du eine Entwicklungsversion herunterladen möchtest (die möglicherweise instabil ist), lies die Seite [Download](Download/de.md).


</div>


<div class="mw-translate-fuzzy">

Nachdem du die.exe-Datei (NSIS Installer) heruntergeladen hast, doppelklicke auf sie, um den Installationsprozess zu starten.


</div>


<div class="mw-translate-fuzzy">

Nachfolgend sind weitere Informationen zu einigen technischen Optionen. Dennoch benötigen die meisten Benutzer nicht mehr als die oben genannten .exe Dateien. Gehe nach Abschluss der Installation auf [Erste Schritte](Getting_started/de.md).


</div>

## Installation for all users of the Windows system 

By default FreeCAD will be installed for the user that executes the installer. If this user only has user permissions, the default installation path is:

:   
    {{FileName|C:\Users\<username>\AppData\Local\Programs\FreeCAD X.YY}}
    

If the installer is executed by an admin user, or you execute it as admin, you can choose if FreeCAD should be installed for all users of the system or just for you. The default is for all users.

If installed for all users, the default installation path is:

:   
    {{FileName|C:\Program Files\FreeCAD X.YY}}
    

## Silent Installation 

To install FreeCAD silently, you can execute the installer from the command line:


{{Code|lang=text|code=
FreeCAD-~.exe /S
}}

Default settings will be used for all options. A custom installation path can be specified in this manner:


{{Code|lang=text|code=
FreeCAD-~.exe /S /D=A path to FreeCAD with spaces
}}

By default, even with silent installations, there will be a short popup when the installer is checked for corruption. This so-called cyclic redundancy check only takes a few seconds at most. To disable this corruption check:


{{Code|lang=text|code=
FreeCAD-~.exe /S /NCRC
}}

Note that this {{Incode|/NCRC}} flag is **not recommended** since the corruption check assures that the installer was e.g. completely downloaded.

## Chocolatey


<div class="mw-translate-fuzzy">

Jedoch wird dringend empfohlen, dass du einen Paketmanager wie Chocolatey verwendest, um deine Software auf dem neuesten Stand zu halten. Du kannst Chocolatey nach [diese Anweisungen](https://chocolatey.org/install) installieren und dann ein PowerShell Terminal als Administrator öffnen und ausführen:


</div>


{{Code|lang=text|code=
choco install freecad
}}


<div class="mw-translate-fuzzy">

Von Zeit zu Zeit kannst du deine Software aktualisieren mit


</div>


{{Code|lang=text|code=
choco upgrade freecad
}}


<div class="mw-translate-fuzzy">

um die neueste Version zu erhalten, die im Chocolatey Repositorium verfügbar ist. Wenn es irgendwelche Probleme mit dem Chocolatey Paket gibt, kannst du dich an die Betreuer unter [auf dieser Seite](https://chocolatey.org/packages/freecad) wenden.


</div>

## Deinstallation

To uninstall FreeCAD it is preferable to use the Windows tools for uninstalling software. Alternatively you can execute the uninstaller directly. This is the file:

:   
    {{FileName|Uninstall-FreeCAD.exe}}
    

You can find it in the folder where FreeCAD is installed.

The uninstaller can also be executed silently using the command line:


{{Code|lang=text|code=
Uninstall-FreeCAD.exe /S}}

Note that (silent) uninstallation will fail if there is a running instance of FreeCAD, even if that instance is not the version being uninstalled.


{{docnav/de
|[Funktionalitäten](Feature_list/de.md)
|[ Installieren auf Linux](Install_on_Linux/de.md)
}}



---
![](images/Right_arrow.png) [documentation index](../README.md) > Installing on Windows/de
