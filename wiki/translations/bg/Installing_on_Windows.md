# Installing on Windows/bg
{{TOCright}}

## Standard Installation 

The easiest way to install the latest stable version of FreeCAD is to use the installer:


{{DownloadWindowsStable}}


<div class="mw-translate-fuzzy">

Ако искате да свалите или 64-битова версия, или нестабилна \"най-нова\" версия (development version) вижте страницата [Downloads](Download/bg.md).


</div>


<div class="mw-translate-fuzzy">

След като свалите .msi (Microsoft Installer) файлът кликнете 2 пъти върху него за да стартирате инсталацията.


</div>


<div class="mw-translate-fuzzy">

По-доли има други опции за инсталация. Ако ви се струват трудни не се притеснявайте! За повечето потребители на Windows е достатъчно да инсталират със гореописаният инсталатор и да следват инструкциите в страницата **[Първи Стъпки](Getting_started/bg.md)**!


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

It is highly recommended that you use a package manager such as Chocolatey to keep your software updated. You can install Chocolatey following [these instructions](https://chocolatey.org/install) and then open a PowerShell terminal as admin and run:


{{Code|lang=text|code=
choco install freecad
}}

Every once in a while you can update your software with:


{{Code|lang=text|code=
choco upgrade freecad
}}

This will get the latest version available from the Chocolatey repository. If there are any issues with the Chocolatey package, you can contact maintainers on [this page](https://chocolatey.org/packages/freecad).

### Деинсталация

С

To uninstall FreeCAD it is preferable to use the Windows tools for uninstalling software. Alternatively you can execute the uninstaller directly. This is the file:

:   
    {{FileName|Uninstall-FreeCAD.exe}}
    

You can find it in the folder where FreeCAD is installed.

The uninstaller can also be executed silently using the command line:


{{Code|lang=text|code=
Uninstall-FreeCAD.exe /S}}

Note that (silent) uninstallation will fail if there is a running instance of FreeCAD, even if that instance is not the version being uninstalled.


<div class="mw-translate-fuzzy">


{{docnav|Feature list/bg|Install on Unix/bg}}


</div>



---
![](images/Right_arrow.png) [documentation index](../README.md) > Installing on Windows/bg
