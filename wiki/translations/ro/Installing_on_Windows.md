# Installing on Windows/ro
<div class="mw-translate-fuzzy">


{{docnav|Feature list|Install on Linux}}


</div>


{{TOCright}}

## Standard Installation 

The easiest way to install the latest stable version of FreeCAD is to use the installer:


{{DownloadWindowsStable}}


<div class="mw-translate-fuzzy">

Daca doriți sa descărcați versiunea pe 64 de biți sau versiunea aflată acum în dezvoltare (care ar putea fi instabilă) vizitați pagina de [descărcări](Download/ro.md).


</div>


<div class="mw-translate-fuzzy">

Dupa ce fișierul .msi (Microsoft Installer) a fost descarcat, doar faceți dublu-click pe el pentru a începe instalarea.


</div>


<div class="mw-translate-fuzzy">

Mai jos sunt descrise opțiunile de instalare. Daca pare complicat nu va ingrijorați! Cei mai mulți utilizatori nu vor avea nevoie de nimic mai mult decat fișierul de mai sus .msi și articolul **[ Primii pasi](Getting_started/ro.md)**!


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

### Dezinstalarea

Folosind

To uninstall FreeCAD it is preferable to use the Windows tools for uninstalling software. Alternatively you can execute the uninstaller directly. This is the file:

:   
    {{FileName|Uninstall-FreeCAD.exe}}
    

You can find it in the folder where FreeCAD is installed.

The uninstaller can also be executed silently using the command line:


{{Code|lang=text|code=
Uninstall-FreeCAD.exe /S}}

Note that (silent) uninstallation will fail if there is a running instance of FreeCAD, even if that instance is not the version being uninstalled.


<div class="mw-translate-fuzzy">


{{docnav|Feature list|Install on Linux}}


</div>



---
![](images/Right_arrow.png) [documentation index](../README.md) > Installing on Windows/ro
