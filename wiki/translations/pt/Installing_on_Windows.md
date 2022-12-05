# Installing on Windows/pt
{{TOCright}}

## Standard Installation 

The easiest way to install the latest stable version of FreeCAD is to use the installer:


{{DownloadWindowsStable}}


<div class="mw-translate-fuzzy">

Se quiser fazer a transferência da versão 64 bits ou a versão de desenvolvimento instável, veja a página dos [Transferências](Download/pt.md).


</div>


<div class="mw-translate-fuzzy">

Depois de transferir o ficheiro .msi (instalador da Microsoft), faça duplo-clique para iniciar o processo de instalação.


</div>


<div class="mw-translate-fuzzy">

Em baixo encontra mais informação sobre opções técnicas. Se lhe parecer complicado, não se preocupe! A maioria dos utilizadores Windows não precisam de mais do que o ficheiro de instalação .msi para instalar o FreeCAD e **[ Começar](Getting_started/pt.md)**.


</div>

## Installation for all users of the Windows system 

By default FreeCAD will be installed for the user that executes the installer. If this user only has user permissions, the default installation path is:

:   
    **C:\Users\<username>\AppData\Local\Programs\FreeCAD X.YY**
    

If the installer is executed by an admin user, or you execute it as admin, you can choose if FreeCAD should be installed for all users of the system or just for you. The default is for all users.

If installed for all users, the default installation path is:

:   
    **C:\Program Files\FreeCAD X.YY**
    

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

### Desinstalação

Com

To uninstall FreeCAD it is preferable to use the Windows tools for uninstalling software. Alternatively you can execute the uninstaller directly. This is the file:

:   
    **Uninstall-FreeCAD.exe**
    

You can find it in the folder where FreeCAD is installed.

The uninstaller can also be executed silently using the command line:


{{Code|lang=text|code=
Uninstall-FreeCAD.exe /S}}

Note that (silent) uninstallation will fail if there is a running instance of FreeCAD, even if that instance is not the version being uninstalled.


<div class="mw-translate-fuzzy">


{{docnav/pt|[Lista de funcionalidades](Feature_list/pt.md)|[Install on Unix](Install_on_Unix/pt.md)}}


</div>



---
![](images/Right_arrow.png) [documentation index](../README.md) > Installing on Windows/pt
