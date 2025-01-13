# Installing on Windows/zh-cn
## Standard Installation 

The easiest way to install the latest stable version of FreeCAD is to use the installer, see the [Download](Download.md) page.


<div class="mw-translate-fuzzy">

如果你想下载一个 64 位或者不稳定的开发版本，请参考 [下载](Download/zh-cn.md) 页。


</div>


<div class="mw-translate-fuzzy">

下载完 .msi (微软安装文件格式) 文件，只需要双击它以启动安装过程。


</div>


<div class="mw-translate-fuzzy">

下面是更多关于技术选项的信息。 如果它看起来很吓人，不要紧张！绝大部分 Windows 用户只需要使用 .msi 安装 FreeCAD 和 阅读 **[入门](Getting_started/zh-cn.md)**!


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

Using the [Chocolatey](https://chocolatey.org/install) package manager is currently not recommended as that repository is no longer kept up-to-date.



### 卸载

使用

To uninstall FreeCAD it is preferable to use the Windows tools for uninstalling software. Alternatively you can execute the uninstaller directly. This is the file:

:   
    **Uninstall-FreeCAD.exe**
    

You can find it in the folder where FreeCAD is installed.

The uninstaller can also be executed silently using the command line:


{{Code|lang=text|code=
Uninstall-FreeCAD.exe /S}}

Note that (silent) uninstallation will fail if there is a running instance of FreeCAD, even if that instance is not the version being uninstalled.


<div class="mw-translate-fuzzy">


{{docnav|Feature list/zh-cn|Install on Unix/zh-cn}}


</div>



---
⏵ [documentation index](../README.md) > Installing on Windows/zh-cn
