# Download/pt
{{TOCright}}


<div class="mw-translate-fuzzy">

## Instaladores oficiais 


</div>


<div class="mw-translate-fuzzy">

### Instaladores estáveis do FreeCAD 

A equipa do FreeCAD disponibiliza pacotes prontos a instalar para <img alt="" src=images/windows.png  style="width:16px;"> **Windows** (32 e 64bits), <img alt="" src=images/mac.png  style="width:16px;"> **Mac OS X** (Lion 10.7 32 e 64bits), e <img alt="" src=images/linux.png  style="width:16px;"> **Ubuntu** (LTS e atual, 32 e 64bits). Em baixo estão ligações para os ficheiros de instalação estáveis para vários sistemas. Estão também disponíveis na [Página de ficheiros do FreeCAD](https://github.com/FreeCAD/FreeCAD/releases) pacotes **instáveis**, que disponibilizam funcionalidades novas acabadas de adicionar, mas que podem bloquear mais frequentemente ou conter recursos que são incompatíveis com versões anteriores.

+---------------------------+---+------------------------+---+-----------------------+
|            |   |         |   |        |
| {{DownloadWindowsStable}} |   | {{DownloadUnixStable}} |   | {{DownloadMacStable}} |
|                        |   |                     |   |                    |
+---------------------------+---+------------------------+---+-----------------------+


</div>

You will find SHA256 checksums to verify the integrity of your download on the [0.19.2 release page](https://github.com/FreeCAD/FreeCAD/releases/tag/0.19.2).

Previous versions can be downloaded from the [releases](https://github.com/FreeCAD/FreeCAD/releases) page

+:----------------------------------------------------------------------------------------------------------------------------------------:+---+:------------------------------------------------------------------------------------------------------------------------------------------------------:+---+:-----------------------------------------------------------------------:+
| ![](images/Windows.png )                                                                                                           |   | ![](images/Mac.png )                                                                                                                                 |   | ![](images/AppImage-logo.png )                              |
|                                                                                                                                          |   |                                                                                                                                                        |   |                                                                         |
| Install on Windows                                                                                                                       |   | Install on Mac                                                                                                                                         |   | Install on Linux                                                        |
|                                                                                                                                          |   |                                                                                                                                                        |   |                                                                         |
| _ 64-bit |
+------------------------------------------------------------------------------------------------------------------------------------------+---+--------------------------------------------------------------------------------------------------------------------------------------------------------+---+-------------------------------------------------------------------------+


<div class="mw-translate-fuzzy">

### Notas para utilizadores Windows 

O instalador do windows deve funcionar também em plataformas Windows mais antigas, mas não foi testado. Precisa de ter instalado o *Windows Installer V1* no seu seu sistema (msiexec.exe). Veja [ Instalar em Windows](Install_on_Windows.md) para mais detalhes sobre diferentes opções de instalação. Transfira o ficheiro .msi mais recente para sistemas windows, ou ou ficheiro .deb apropriado para a sua versão do Ubuntu ou Debian.


</div>

### Notes for Mac OS X users 

Mac OS X 10.12 *Sierra* is the minimum supported version.

### Notes for GNU/Linux users 

Most distributions carry FreeCAD in their official repositories, however, if the distribution doesn\'t follow a rolling release model the version they provide might be outdated. Instead you can download the AppImage above, mark it as executable and launch it without installation.

Please see the [Installing on Linux](Installing_on_Linux.md) page for more installation options, including daily packages for Ubuntu and derivatives.

A portable version that doesn\'t need installation can be achieved by starting FreeCAD with these commands: <small>(v0.19)</small>  
```python
cd path/to/directory_containing_AppImage/
chmod +x ./FreeCAD_0.19-23756-Linux-Conda_glibc2.12-x86_64.AppImage
HOME="$PWD/Settings" FREECAD_USER_HOME="$PWD/Settings" ./FreeCAD_0.19-23756-Linux-Conda_glibc2.12-x86_64.AppImage
```

More information about FreeCAD\'s environment variables can be found on [the configuration page](Start_up_and_Configuration#Environment_variables.md).


<div class="mw-translate-fuzzy">

### Versões de desenvolvimento 

Se quiser instalar o FreeCAD com funcionalidades em desenvolvimento, e estiver disposto a aceitar que estas versões têm altas probabilidades de ter bugs ou de bloquear, então pode verificar a _ o FreeCAD, ou usar as [atualizações diárias do Ubuntu daily build](#Ubuntu_PPA_packages.md) ou instalar um dos ficheiros pré-lançados da página do github acima.


</div>

## Additional modules and macros 


<div class="mw-translate-fuzzy">

The FreeCAD community provides a wealth of additional modules and macros. They can now easily be installed directly from within FreeCAD using the [Addon Manager](Addon_Manager.md).


</div>

---
[documentation index](../README.md) > Download/pt
