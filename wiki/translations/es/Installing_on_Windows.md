# Installing on Windows/es
## Standard Installation 


<div class="mw-translate-fuzzy">

La forma más fácil de *instalar FreeCAD en Windows* es usando el paquete de instalación descargable de arriba. Esta página describe el uso y las características del *NSIS Instalador* para más opciones de instalación.


</div>


<div class="mw-translate-fuzzy">

Si desea descargar una versión en desarrollo (que puede ser inestable), mira la página [Descargas](Download/es.md).


</div>


<div class="mw-translate-fuzzy">

Después de descargar el archivo .exe (NSIS Installer), haga doble clic en él para iniciar el proceso de instalación.


</div>


<div class="mw-translate-fuzzy">

Abajo hay más información sobre algunas opciones técnicas. Sin embargo, la mayoría de los usuarios no necesitan más que los anteriores archivos .exe. Continuar a [Empieza](Getting_started/de.md) después de que la instalación se haya completado.


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



## Desinstalación

To uninstall FreeCAD it is preferable to use the Windows tools for uninstalling software. Alternatively you can execute the uninstaller directly. This is the file:

:   
    **Uninstall-FreeCAD.exe**
    

You can find it in the folder where FreeCAD is installed.

The uninstaller can also be executed silently using the command line:


{{Code|lang=text|code=
Uninstall-FreeCAD.exe /S}}

Note that (silent) uninstallation will fail if there is a running instance of FreeCAD, even if that instance is not the version being uninstalled.



---
⏵ [documentation index](../README.md) > Installing on Windows/es
