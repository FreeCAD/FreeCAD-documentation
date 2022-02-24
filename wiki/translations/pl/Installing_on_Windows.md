# Installing on Windows/pl
{{docnav/pl
|[Funkcjonalność programu](Feature_list/pl.md)
|[Instalacja w systemie Linux](Installing_on_Linux/pl.md)
}}


{{TOCright}}

## Standard Installation 

Najprostszym sposobem na zainstalowanie najnowszej stabilnej wersji FreeCAD jest użycie instalatora:


{{DownloadWindowsStable}}

Jeśli chcesz pobrać wersję rozwojową, która może być niestabilna, zobacz stronę [Pobieranie kompilacji tygodniowych](https://github.com/FreeCAD/FreeCAD-Bundle/releases/tag/weekly-builds).

Po pobraniu pliku .exe Instalatora, kliknij jego ikonę dwukrotnie, aby uruchomić proces instalacji.

Poniżej znajduje się więcej informacji na temat opcji technicznych. Większość użytkowników Windows nie będzie potrzebowała nic więcej niż instalator. Gdy zakończysz instalację przejdź do poradnika [Jak zacząć](Getting_started/pl.md).

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

W celu przeprowadzenia aktualizacji oprogramowania zaleca się jednak używanie menedżera pakietów, takiego jak **Chocolatey**.
Możesz zainstalować Chocolatey, postępując zgodnie z [instrukcjami](https://chocolatey.org/install), a następnie otworzyć terminal PowerShell jako administrator i uruchomić proces aktualizacji:


{{Code|lang=text|code=
choco install freecad
}}

Raz na jakiś czas można zaktualizować oprogramowanie poprzez:


{{Code|lang=text|code=
choco upgrade freecad
}}

Aby uzyskać najnowszą wersję dostępną w repozytorium Chocolatey. W przypadku wystąpienia jakichkolwiek problemów z pakietem Chocolatey, możesz skontaktować się z opiekunami na stronie [o tutaj](https://chocolatey.org/packages/freecad).

## Deinstalacja

To uninstall FreeCAD it is preferable to use the Windows tools for uninstalling software. Alternatively you can execute the uninstaller directly. This is the file:

:   
    {{FileName|Uninstall-FreeCAD.exe}}
    

You can find it in the folder where FreeCAD is installed.

The uninstaller can also be executed silently using the command line:


{{Code|lang=text|code=
Uninstall-FreeCAD.exe /S}}

Note that (silent) uninstallation will fail if there is a running instance of FreeCAD, even if that instance is not the version being uninstalled.


{{docnav/pl
|[Funkcjonalność programu](Feature_list/pl.md)
|[Instalacja w systemie Linux](Installing_on_Linux/pl.md)
}}



---
![](images/Right_arrow.png) [documentation index](../README.md) > Installing on Windows/pl
