# Installing on Windows/zh
{{TOCright}}

## Standard Installation 

The easiest way to install the latest stable version of FreeCAD is to use the installer:


{{DownloadWindowsStable}}


<div class="mw-translate-fuzzy">

如果要下载开发版本（程序运行可能不稳定），请参阅[下载页面](Download.md)。


</div>


<div class="mw-translate-fuzzy">

下载.msi（Microsoft Installer）文件后，双击它启动安装过程。


</div>


<div class="mw-translate-fuzzy">

以下是有关技术选项的更多信息。如果它看起来令人生畏，不要担心！大多数Windows用户不需要上述.msi以外的任何东西来完成安装并**[入门](Getting_started.md)**FreeCAD！


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

## Uninstallation

To uninstall FreeCAD it is preferable to use the Windows tools for uninstalling software. Alternatively you can execute the uninstaller directly. This is the file:

:   
    **Uninstall-FreeCAD.exe**
    

You can find it in the folder where FreeCAD is installed.

The uninstaller can also be executed silently using the command line:


{{Code|lang=text|code=
Uninstall-FreeCAD.exe /S}}

Note that (silent) uninstallation will fail if there is a running instance of FreeCAD, even if that instance is not the version being uninstalled.


<div class="mw-translate-fuzzy">


{{docnav/zh|Feature list/zh|Install on Unix/zh}}


</div>



---
![](images/Right_arrow.png) [documentation index](../README.md) > Installing on Windows/zh
