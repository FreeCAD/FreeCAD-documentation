# Installing on Windows/pt-br
## Standard Installation 


<div class="mw-translate-fuzzy">

A maneira mais fácil de **instalar o FreeCAD no Windows** é usando o arquivo de instalação para download acima. Esta página descreve o uso e as características do *Instalador NSIS* para mais opções de instalação.


</div>


{{DownloadWindowsStable}}


<div class="mw-translate-fuzzy">

Se você quiser baixar a versão de desenvolvimento (que pode ser instável), veja a página [Download](Download/pt-br.md).


</div>


<div class="mw-translate-fuzzy">

Após baixar o arquivo .exe (NSIS Installer), clique duas vezes nele para iniciar o processo de instalação.


</div>


<div class="mw-translate-fuzzy">

Abaixo estão mais informações sobre algumas opções técnicas. No entanto, a maioria dos usuários não precisa mais do que os arquivos .exe acima. Vá para [Introdução](Getting_started/pt-br.md) após completar a instalação.


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


<div class="mw-translate-fuzzy">

Entretanto, é altamente recomendado que você use um gerenciador de pacotes como o Chocolatey para manter seu software atualizado. Você pode instalar Chocolatey seguindo [estas instruções](https://chocolatey.org/install) e depois abrir um terminal PowerShell como administrador e executar:


</div>


{{Code|lang=text|code=
choco install freecad
}}


<div class="mw-translate-fuzzy">

de vez em quando, você pode atualizar seu software com


</div>


{{Code|lang=text|code=
choco upgrade freecad
}}


<div class="mw-translate-fuzzy">

para obter a última versão disponível no repositório Chocolatey. Se houver algum problema com o pacote Chocolatey, você pode entrar em contato com os mantenedores em [esta página](https://chocolatey.org/packages/freecad).


</div>

## Desinstalação

To uninstall FreeCAD it is preferable to use the Windows tools for uninstalling software. Alternatively you can execute the uninstaller directly. This is the file:

:   
    **Uninstall-FreeCAD.exe**
    

You can find it in the folder where FreeCAD is installed.

The uninstaller can also be executed silently using the command line:


{{Code|lang=text|code=
Uninstall-FreeCAD.exe /S}}

Note that (silent) uninstallation will fail if there is a running instance of FreeCAD, even if that instance is not the version being uninstalled.



---
⏵ [documentation index](../README.md) > Installing on Windows/pt-br
