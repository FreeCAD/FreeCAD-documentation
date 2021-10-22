# Start up and Configuration/pl
{{TOCright}}

## Przegląd

Ta strona pokazuje różne sposoby uruchamiania programu FreeCAD i najważniejsze funkcje konfiguracyjne.

## Uruchamianie FreeCAD z wiersza poleceń 

FreeCAD może być uruchomiony normalnie poprzez dwukrotne kliknięcie na ikonie na pulpicie lub wybranie go z menu startowego, ale może być również uruchomiony bezpośrednio z wiersza poleceń. Pozwala to zmienić niektóre z domyślnych opcji uruchamiania.

### Używanie opcji wiersza poleceń bez powłoki wiersza poleceń 

-   W Ubuntu możesz utworzyć ikonę na pulpicie i edytować jej właściwości. Dodaj opcje wiersza poleceń oddzielone spacjami za nazwą programu w polu \"Polecenie\".
-   W systemie Windows utwórz skrót i edytuj jego właściwości. Dodaj opcje wiersza poleceń oddzielone spacjami do pola \"Cel\".

### Argumenty dla wiersza poleceń 

Opcje wiersza poleceń podlegają częstym zmianom, dlatego dobrze jest sprawdzić aktualne opcje wpisując:

FreeCAD --help

Z odpowiedzi można odczytać możliwe parametry:

 Usage: FreeCAD [options] File1 File2 ...
 
 Allowed options:
 
 Generic options:
   -v [ --version ]          Prints version string
   -h [ --help ]             Prints help message
   -c [ --console ]          Starts in console mode
   --response-file arg       Can be specified with '@name', too
   --dump-config             Dumps configuration
   --get-config arg          Prints the value of the requested configuration key
 
 Configuration:
   -l [ --write-log ]        Writes a log file to:
                             /home/username/.FreeCAD/FreeCAD.log
   --log-file arg            Unlike --write-log this allows logging to an 
                             arbitrary file
   -u [ --user-cfg ] arg     User config file to load/save user settings
   -s [ --system-cfg ] arg   System config file to load/save system settings
   -t [ --run-test ] arg     Test case - or 0 for all
   -M [ --module-path ] arg  Additional module paths
   -P [ --python-path ] arg  Additional python paths
   --single-instance         Allow to run a single instance of the application

W poniższej tabeli wybrane opcje zostały opisane bardziej szczegółowo:

+-------------------------------------------+----------------------------------------------------------------------------+--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| Długa opcja                               | Odpowiednio [nazwa zmiennej konfiguracji](#Zestaw_konfiguracji.md) | Opis                                                                                                                                                                                                                                                                                                   |
+===========================================+============================================================================+========================================================================================================================================================================================================================================================================================================+
|                            | UserParameter                                                              | Nazwa pliku lub ścieżka względna, która kończy się nazwą pliku. Domyślnie `user.cfg`.                                                                                                                                                                                           |
| `--user-cfg <filename>`          |                                                                            |                                                                                                                                                                                                                                                                                                        |
|                                        |                                                                            |                                                                                                                                                                                                                                                                                                        |
+-------------------------------------------+----------------------------------------------------------------------------+--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
|                            | Poprzedza AdditionalModulePaths                                            | Katalog zawierający moduły. Opcja ta może być podana wielokrotnie, aby określić wiele katalogów.                                                                                                                                                                                                       |
| `--module-path <dir>`            |                                                                            |                                                                                                                                                                                                                                                                                                        |
|                                        |                                                                            |                                                                                                                                                                                                                                                                                                        |
+-------------------------------------------+----------------------------------------------------------------------------+--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
|                            | most                                                                       | Wyprowadza żądaną wartość w oknie kontekstowym. Kończy pracę po potwierdzeniu przyciskiem **OK**. Nie może być używane wielokrotnie. Jeśli użyto nieznanej / nieprawidłowej nazwy zmiennej, odpowiedź jest pusta. Flaga `--console` nie jest respektowana. |
| `--get-config <config-var-name>` |                                                                            |                                                                                                                                                                                                                                                                                                        |
|                                        |                                                                            |                                                                                                                                                                                                                                                                                                        |
+-------------------------------------------+----------------------------------------------------------------------------+--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+

Opcje mogą być zapisane w dwóch formach: `--long-option arg` oraz `--long-option<nowiki>=</nowiki>arg`.

### Pliki odpowiedzi i konfiguracji 

FreeCAD może odczytać niektóre z tych opcji z pliku konfiguracyjnego. Plik ten musi znajdować się w ścieżce bin i musi mieć nazwę {{FileName|FreeCAD.cfg}}. Pamiętaj, że opcje podane w linii poleceń nadpisują plik konfiguracyjny!

Niektóre systemy operacyjne mają bardzo niski limit znaków w wierszu poleceń. Powszechnym sposobem na obejście tych ograniczeń jest użycie plików odpowiedzi. Plik odpowiedzi jest po prostu plikiem konfiguracyjnym, który używa tej samej składni co wiersz poleceń. Jeśli linia poleceń określa plik odpowiedzi, jest on ładowany i przetwarzany dodatkowo do linii poleceń:

    FreeCAD @ResponseFile.txt 

lub:

    FreeCAD --response-file=ResponseFile.txt

lub:

    FreeCAD --response-file ResponseFile.txt

### Opcje ukryte 

Istnieje kilka opcji niewidocznych dla użytkownika. Opcje te są np. parametrami X-Window parsowanymi przez system Windows:

-   *-display* - Ustawia wyświetlanie X-ów (domyślnie \$DISPLAY).
-   *-geometry* - ustawia geometrię klienta pierwszego wyświetlanego okna.
-   *-fn* lub *-font* - definiuje czcionkę aplikacji. Czcionka powinna być określona przy użyciu logicznego opisu czcionki X.
-   *-bg* lub *-background* - Ustawia domyślny kolor tła i paletę aplikacji (obliczane są jasne i ciemne odcienie).
-   *-fg* lub *-foreground* - Ustawia domyślny kolor pierwszego planu.
-   *-btn* lub *-button* - Ustawia domyślny kolor przycisku.
-   *-name* - Ustawia nazwę aplikacji.
-   *-title* - Ustawia tytuł aplikacji.
-   *-visual* - Zmusza aplikację do używania obrazu TrueColor na 8-bitowym wyświetlaczu.
-   *-ncols* - Ogranicza liczbę kolorów alokowanych w kostce kolorów na wyświetlaczu 8-bitowym, jeżeli aplikacja używa specyfikacji kolorów QApplication::ManyColor. Jeśli licznik wynosi 216, to używana jest kostka koloru 6x6x6 (tj. 6 poziomów czerwonego, 6 zielonego i 6 niebieskiego); dla innych wartości używana jest kostka w przybliżeniu proporcjonalna do kostki 2x3x1.
-   *-cmap* - Powoduje, że aplikacja instaluje prywatną mapę kolorów na 8-bitowym wyświetlaczu.

### Uruchamianie FreeCAD bez GUI 

FreeCAD jest zazwyczaj zbudowany z dwóch plików wykonywalnych: obsługującego GUI, zwanego {{FileName|FreeCAD}} lub {{FileName|freecad}}, oraz bez interfejsu graficznego, zwanego {{FileName|FreeCADCmd}} lub {{FileName|freecadcmd}}. FreeCAD może być używany w trybie konsoli przy użyciu przełącznika `--console` *(co jest domyślnym zachowaniem {{FileName|FreeCADCmd}})*:

FreeCAD --console

W trybie konsoli nie będzie wyświetlany żaden graficzny interfejs użytkownika, a pojawi się znak zachęty interpretera Python: `>>>`. Z poziomu tego monitu masz taką samą funkcjonalność jak z interpreterem Python, który działa wewnątrz GUI FreeCAD, oraz dostęp do wszystkich modułów i wtyczek programu, z wyjątkiem modułu FreeCADGui. Należy pamiętać, że moduły zależne od FreeCADGui mogą być również niedostępne.

To read more about console or headless mode, checkout [Headless FreeCAD](Headless_FreeCAD.md).

### Running modules, macros and scripts 

+-----------------+------------------+------------------------------------------------------------------------------------------------------------------------------------+
| File type       | System           | Command line example                                                                                                               |
+=================+==================+====================================================================================================================================+
| Module          | Windows          |                                                                                                                     |
|                 |                  | `"C:\Program Files\FreeCAD\bin\FreeCAD.exe" -M "C:\FreeCAD\Mod\Draft"`                                                    |
|                 |                  |                                                                                                                                 |
+-----------------+------------------+------------------------------------------------------------------------------------------------------------------------------------+
|                 | Linux            |                                                                                                                     |
|                 |                  | `FreeCAD_0.19 -M ~/.FreeCAD/Mod/Draft`                                                                                    |
|                 |                  |                                                                                                                                 |
+-----------------+------------------+------------------------------------------------------------------------------------------------------------------------------------+
|                 | Linux (AppImage) |                                                                                                                     |
|                 |                  | `path/to/FreeCADXXX.AppImage -M ~/.FreeCAD/Mod/Draft`                                                                     |
|                 |                  |                                                                                                                                 |
+-----------------+------------------+------------------------------------------------------------------------------------------------------------------------------------+
|                 |                  |                                                                                                                                    |
+-----------------+------------------+------------------------------------------------------------------------------------------------------------------------------------+
| .FCMacro or .py | Windows          |                                                                                                                     |
|                 |                  | `"C:\Program Files\FreeCAD\bin\FreeCAD.exe" "C:\Users\userName\AppData\Roaming\FreeCAD\Mod\WorkFeature\start_WF.FCMacro"` |
|                 |                  |                                                                                                                                 |
+-----------------+------------------+------------------------------------------------------------------------------------------------------------------------------------+
|                 | Linux            |                                                                                                                     |
|                 |                  | `FreeCAD_0.19 ~/.FreeCAD/Mod/WorkFeature/start_WF.FCMacro`                                                                |
|                 |                  |                                                                                                                                 |
+-----------------+------------------+------------------------------------------------------------------------------------------------------------------------------------+
|                 | Linux (AppImage) |                                                                                                                     |
|                 |                  | `path/to/FreeCADXXX.AppImage ~/.FreeCAD/Mod/WorkFeature/start_WF.FCMacro`                                                 |
|                 |                  |                                                                                                                                 |
+-----------------+------------------+------------------------------------------------------------------------------------------------------------------------------------+

See [Macro at Startup](Macro_at_Startup.md) on how to set up a macro to automatically run at FreeCAD startup.

## Zmienne środowiskowe 

FreeCAD supports the following environment variables, which can be used to configure directories: <small>(v0.19)</small> 

+------------------------------+----------------------------------------------------------------+---------------------------------------------------------------------------------------------------------------------------------------------+
| Environment variable         | Corresponding [config var name](#Configuration_set.md) | Synopsis                                                                                                                                    |
+==============================+================================================================+=============================================================================================================================================+
|               | UserHomePath                                                   | FreeCAD\'s \"base\" directory for keeping local user data.                                                                                  |
| `FREECAD_USER_HOME` |                                                                |                                                                                                                                             |
|                           |                                                                |                                                                                                                                             |
+------------------------------+----------------------------------------------------------------+---------------------------------------------------------------------------------------------------------------------------------------------+
|               | UserAppData                                                    | If not set, defaults to `FREECAD_USER_HOME/.FreeCAD`, but only if `FREECAD_USER_HOME` is set. |
| `FREECAD_USER_DATA` |                                                                |                                                                                                                                             |
|                           |                                                                |                                                                                                                                             |
+------------------------------+----------------------------------------------------------------+---------------------------------------------------------------------------------------------------------------------------------------------+
|               | AppTempPath                                                    | If not set, defaults to `FREECAD_USER_HOME/temp`, but only if `FREECAD_USER_HOME` is set.     |
| `FREECAD_USER_TEMP` |                                                                |                                                                                                                                             |
|                           |                                                                |                                                                                                                                             |
+------------------------------+----------------------------------------------------------------+---------------------------------------------------------------------------------------------------------------------------------------------+

If the specified path does not exist, the setting is ignored!

The above environment variables are meant to be used to realize a *portable* FreeCAD environment. For an example how environment variables can be used from the command line on Linux refer to the [notes for Linux users on the downloads page](Download#Notes_for_GNU.2FLinux_users.md).

### `HOME`

FreeCAD uses [Qt](Third_Party_Libraries#Qt.md), which does honor the `HOME` environmental variable. Thus, setting `HOME` can be used to specify the base directory of Qt-related configuration files (`.config/FreeCAD/FreeCAD.conf`).

FreeCad itself does not honor the `HOME` environmental variable (because it determines the user\'s home directory from a lower-level system API). Use `FREECAD_USER_HOME` for this pupose.

### `TMPDIR` 

The default temporary directory is {{FileName|/tmp/}}. The `TMPDIR` environmental variable can be used to override the default. (*Editor: precedence?*).

### Libraries

Some libraries need to call system environment variables. Sometimes when there is a problem with a FreeCAD installation, it is because some environment variable is absent or incorrect. Therefore, some important variables get duplicated in the Config and saved in the log file.

**Python**

-   PYTHONPATH
-   PYTHONHOME
-   TCL\_LIBRARY
-   TCLLIBPATH

**OpenCascade**

-   CSF\_MDTVFontDirectory
-   CSF\_MDTVTexturesDirectory
-   CSF\_UnitsDefinition
-   CSF\_UnitsLexicon
-   CSF\_StandardDefaults
-   CSF\_PluginDefaults
-   CSF\_LANGUAGE
-   CSF\_SHMessage
-   CSF\_XCAFDefaults
-   CSF\_GraphicShr
-   CSF\_IGESDefaults
-   CSF\_STEPDefaults

## Zestaw konfiguracji 

On every startup FreeCAD examines its surrounding and the command line parameters. It builds up a **configuration set** which holds the essence of the runtime information. This information is later used to determine the place where to save user data or log files. It is also very important for post postmortem analyzes. Therefore it is saved in the log file.

### User related information 

+-----------------+----------------------------------------------------------+------------------------------------------------------------------------------+-----------------------------------------------------------------------+
| Config var name | Synopsis                                                 | Example Windows                                                              | Example Linux                                                         |
+=================+==========================================================+==============================================================================+=======================================================================+
| UserAppData     | Path where FreeCAD stores User Related application data. |                                                               |                                                        |
|                 |                                                          | {{FileName|C:\Documents and Settings\username\AppData\FreeCAD}}              | {{FileName|/home/username/.FreeCAD}}                                  |
|                 |                                                          |                                                                           |                                                                    |
|                 |                                                          |                                                                    |                                                             |
|                 |                                                          | <hr />                                                                       | <hr />                                                                |
|                 |                                                          |                                                                           |                                                                    |
|                 |                                                          | \'\'Short path : \'\'{{FileName|%APPDATA%\FreeCAD}}            | \'\'Short path : \'\'{{FileName|~/.FreeCAD}}            |
+-----------------+----------------------------------------------------------+------------------------------------------------------------------------------+-----------------------------------------------------------------------+
| UserParameter   | File where FreeCAD stores User Related application data. |                                                               |                                                        |
|                 |                                                          | {{FileName|C:\Documents and Settings\username\AppData\FreeCAD\user.cfg}}     | {{FileName|/home/username/.FreeCAD/user.cfg}}                         |
|                 |                                                          |                                                                           |                                                                    |
|                 |                                                          |                                                                    |                                                             |
|                 |                                                          | <hr />                                                                       | <hr />                                                                |
|                 |                                                          |                                                                           |                                                                    |
|                 |                                                          | \'\'Short path : \'\'{{FileName|%APPDATA%\FreeCAD\user.cfg}}   | \'\'Short path : \'\'{{FileName|~/.FreeCAD/user.cfg}}   |
+-----------------+----------------------------------------------------------+------------------------------------------------------------------------------+-----------------------------------------------------------------------+
| SystemParameter | File where FreeCAD stores Application Related data.      |                                                               |                                                        |
|                 |                                                          | {{FileName|C:\Documents and Settings\username\AppData\FreeCAD\system.cfg}}   | {{FileName|/home/username/.FreeCAD/system.cfg}}                       |
|                 |                                                          |                                                                           |                                                                    |
|                 |                                                          |                                                                    |                                                             |
|                 |                                                          | <hr />                                                                       | <hr />                                                                |
|                 |                                                          |                                                                           |                                                                    |
|                 |                                                          | \'\'Short path : \'\'{{FileName|%APPDATA%\FreeCAD\system.cfg}} | \'\'Short path : \'\'{{FileName|~/.FreeCAD/system.cfg}} |
+-----------------+----------------------------------------------------------+------------------------------------------------------------------------------+-----------------------------------------------------------------------+
| UserHomePath    | Home path of the current user                            |                                                               |                                                        |
|                 |                                                          | {{FileName|C:\Documents and Settings\username}}                              | {{FileName|/home/username}}                                           |
|                 |                                                          |                                                                           |                                                                    |
|                 |                                                          |                                                                    |                                                             |
|                 |                                                          | <hr />                                                                       | <hr />                                                                |
|                 |                                                          |                                                                           |                                                                    |
|                 |                                                          | \'\'Short path : \'\'{{FileName|%USERPROFILE%}}                | \'\'Short path : \'\'{{FileName|~}}                     |
+-----------------+----------------------------------------------------------+------------------------------------------------------------------------------+-----------------------------------------------------------------------+

Note: For Linux distributions, an additional configuration file that relates to [Qt](Third_Party_Tools#Qt-Toolkit.md) may exist at path {{FileName|/home/username/.config/FreeCAD/FreeCAD.conf}}.

### Argumenty dla wiersza poleceń 

+-----------------------+---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+-----------------------------------------------------------------------------+
| Config var name       | Synopsis                                                                                                                                                                                                                                                                                    | Example                                                                     |
+=======================+=============================================================================================================================================================================================================================================================================================+=============================================================================+
| LoggingFile           | 1 if the logging is switched on                                                                                                                                                                                                                                                             | 1                                                                           |
+-----------------------+---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+-----------------------------------------------------------------------------+
| LoggingFileName       | File name where the log is placed                                                                                                                                                                                                                                                           |                                                              |
|                       |                                                                                                                                                                                                                                                                                             | {{FileName|C:\Documents and Settings\username\AppData\FreeCAD\FreeCAD.log}} |
|                       |                                                                                                                                                                                                                                                                                             |                                                                          |
+-----------------------+---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+-----------------------------------------------------------------------------+
| RunMode               | This indicates how the main loop will work. **\"Script\"** means that the given script is called and then exit. **\"Cmd\"** runs the command line interpreter. **\"Internal\"** runs an internal script. **\"Gui\"** enters the Gui event loop. **\"Module\"** loads a given python module. | \"Cmd\"                                                                     |
+-----------------------+---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+-----------------------------------------------------------------------------+
| FileName              | Meaning depends on the RunMode                                                                                                                                                                                                                                                              |                                                                             |
+-----------------------+---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+-----------------------------------------------------------------------------+
| ScriptFileName        | Meaning depends on the RunMode                                                                                                                                                                                                                                                              |                                                                             |
+-----------------------+---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+-----------------------------------------------------------------------------+
| Verbose               | Verbosity level of FreeCAD                                                                                                                                                                                                                                                                  | \"\" or \"strict\"                                                          |
+-----------------------+---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+-----------------------------------------------------------------------------+
| OpenFileCount         | Holds the number of files opened through command line arguments                                                                                                                                                                                                                             | \"12\"                                                                      |
+-----------------------+---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+-----------------------------------------------------------------------------+
| AdditionalModulePaths | Holds the additional Module paths given in the cmd line                                                                                                                                                                                                                                     | \"extraModules/\"                                                           |
+-----------------------+---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+-----------------------------------------------------------------------------+

### System related 

+------------------+----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+-------------------------------------------+---------------------------------------+
| Config var name  | Synopsis                                                                                                                                                                                                                                                                                                                                     | Example Windows                           | Example Linux                         |
+==================+==============================================================================================================================================================================================================================================================================================================================================+===========================================+=======================================+
| AppHomePath      | Path where FreeCAD is installed                                                                                                                                                                                                                                                                                                              |                            |                        |
|                  |                                                                                                                                                                                                                                                                                                                                              | {{FileName|c:/Progam Files/FreeCAD_0.19}} | {{FileName|/user/local/FreeCAD_0.19}} |
|                  |                                                                                                                                                                                                                                                                                                                                              |                                        |                                    |
+------------------+----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+-------------------------------------------+---------------------------------------+
| PythonSearchPath | Holds a list of paths which python search modules. This is at startup can change during execution                                                                                                                                                                                                                                            |                                           |                                       |
+------------------+----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+-------------------------------------------+---------------------------------------+
| AppTempPath      | Path of the temporary directory. Can be given with `TMPDIR` environment variable, or with the <img alt="" src=images/Std_DlgParameter.svg  style="width:16px;"> [Parameter Editor](Std_DlgParameter.md): **Tools → Edit parameters... → BaseApp → Preferences → General → TempPath** |                                           |                        |
|                  |                                                                                                                                                                                                                                                                                                                                              |                                           | {{FileName|/tmp/}}                    |
|                  |                                                                                                                                                                                                                                                                                                                                              |                                           |                                    |
|                  |                                                                                                                                                                                                                                                                                                                                              |                                           | (default)                             |
+------------------+----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+-------------------------------------------+---------------------------------------+

### Build related information 

The table below shows the available information about the Build version. Most of it comes from the Subversion repository. This stuff is needed to exactly rebuild a version!

  Config var name      Synopsis                                                                                          Example
  -------------------- ------------------------------------------------------------------------------------------------- -------------------------------------------------------------------
  BuildVersionMajor    Major Version number of the Build. Defined in {{FileName|src/Build/Version.h.in}}   0
  BuildVersionMinor    Minor Version number of the Build. Defined in {{FileName|src/Build/Version.h.in}}   7
  BuildRevision        SVN Repository Revision number of the src in the Build. Generated by SVN                          356
  BuildRevisionRange   Range of different changes                                                                        123-356
  BuildRepositoryURL   Repository URL                                                                                    <https://free-cad.svn.sourceforge.net/svnroot/free-cad/trunk/src>
  BuildRevisionDate    Date of the above Revision                                                                        2007/02/03 22:21:18
  BuildScrClean        Indicates if the source was changed after checkout                                                Src modified
  BuildScrMixed                                                                                                          Src not mixed

### Branding related 

These Config entries are related to the branding mechanism of FreeCAD. See [Branding](Branding.md) for more details.

+------------------+------------------------------------------------------------------------------------------------------------------------+--------------------------+
| Config var name  | Synopsis                                                                                                               | Example                  |
+==================+========================================================================================================================+==========================+
| ExeName          | Name of the build Executable file. Can differ from FreeCAD if a different {{FileName|main.cpp}} is used. |           |
|                  |                                                                                                                        | {{FileName|FreeCAD.exe}} |
|                  |                                                                                                                        |                       |
+------------------+------------------------------------------------------------------------------------------------------------------------+--------------------------+
| ExeVersion       | Over all Version shows up at start time                                                                                | \"0.19\"                 |
+------------------+------------------------------------------------------------------------------------------------------------------------+--------------------------+
| AppIcon          | Icon which is used for the Executable, shows in Application MainWindow.                                                | \"FCIcon\"               |
+------------------+------------------------------------------------------------------------------------------------------------------------+--------------------------+
| ConsoleBanner    | Banner which is prompted in console mode                                                                               |                          |
+------------------+------------------------------------------------------------------------------------------------------------------------+--------------------------+
| SplashPicture    | Name of the Icon used for the Splash Screen                                                                            | \"FreeCADSplasher\"      |
+------------------+------------------------------------------------------------------------------------------------------------------------+--------------------------+
| SplashAlignment  | Alignment of the Text in the Splash dialog                                                                             | \"Bottom\" or \"Left\"   |
+------------------+------------------------------------------------------------------------------------------------------------------------+--------------------------+
| SplashTextColor  | Color of the splasher Text                                                                                             | \"\#000000\"             |
+------------------+------------------------------------------------------------------------------------------------------------------------+--------------------------+
| StartWorkbench   | Name of the Workbench which get started automatically after Startup                                                    | \"Part design\"          |
+------------------+------------------------------------------------------------------------------------------------------------------------+--------------------------+
| HiddenDockWindow | List of dockwindows (separated by a semicolon) which will be disabled                                                  | \"Property editor\"      |
+------------------+------------------------------------------------------------------------------------------------------------------------+--------------------------+

### Querying the configuration 

**From FreeCAD\'s Python console**

Entries of the configuration set can be queried with the **config var name** (see tables above) from the [Python console](Python_console.md). For example:

 >>> FreeCAD.ConfigGet("ExeVersion")
 '0.19'

If the name is not found, an empty string is returned.

**From command line**

Use the `--get-config <config-var-name>` option to query a single name. Not all names are supported. For example:

 FreeCAD_0.19 --get-config ExeVersion

Use the `--dump-config` option to get a list of names and their values. Not all names are supported.

**Z konsoli FreeCAD**

Uruchom FreeCAD w trybie konsoli za pomocą `--console` i zadawaj pytania za pomocą kodu Python. Na przykład: 
```python
  $ FreeCAD_0.19 --console
  [FreeCAD Console mode <Use Ctrl-D (i.e. EOF) to exit.>]
  >>> FreeCAD.ConfigGet("ExeVersion")
  '0.19'
  >>> exit()
```

Dla Linuksa *(powłoka bash)* możesz zmodyfikować następującą linię poleceń, aby dostosować ją do swoich potrzeb: 
```python
  $ FreeCAD_0.19 --console <<EOF
  print( "FREECAD_USER_HOME: " + ( "not set" if ( os.environ.get('FREECAD_USER_HOME') is None ) else os.environ.get('FREECAD_USER_HOME') ) )
  print( "UserHomePath: " + FreeCAD.ConfigGet("UserHomePath") )
  exit()
  EOF
```

## Uruchamianie programu FreeCAD z pulpitu 

### Linux: Tworzenie dodatkowej opcji startowej 

Poniżej zakładamy, że Twój pulpit jest tak skonfigurowany, że możesz z niego uruchomić FreeCAD. W zależności od dystrybucji Linuksa i środowiska graficznego, być może będziesz musiał dostosować następujące kroki:

1.  Skopiuj plik wpisu freedesktop dla FreeCAD z lokalizacji {{FileName|/usr/share/applications/freecad.desktop}} do {{FileName|~/.local/share/applications}}.
2.  Zmień nazwę pliku z {{FileName|freecad.desktop}} na coś innego *(np. {{FileName|MyFreeCADConfig.desktop}})*.
3.  Otwórz plik w edytorze tekstu i zmień sposób wywoływania aplikacji FreeCAD, modyfikując linię zaczynającą się od `Exec`.
4.  W wyniku tego pojawi się dodatkowa pozycja w Twoim menu startowym/uruchomieniu aplikacji. W ten sposób możesz mieć wiele wpisów dla FreeCAD z różnymi opcjami uruchamiania.

## Uruchamianie programu FreeCAD z nośnika USB 


{{Version/pl|0.19}}

**Windows**

Umieść plik wykonywalny FreeCAD, {{FileName|FreeCAD.exe}}, na nośniku USB. Utwórz plik wsadowy {{FileName|FreeCAD.bat}} i umieść go w tym samym katalogu co {{FileName|FreeCAD.exe}}. Wewnątrz pliku wsadowego napisz:


```python
set CURRENTDIR=%cd%
set FREECAD_USER_HOME=%CURRENTDIR%
start FreeCAD.exe -u FreeCAD/user.cfg -s FreeCAD/system.cfg --write-log 
```

[or](https://forum.freecadweb.org/viewtopic.php?f=12&t=54784&start=60#p474759) with `FREECAD_USER_DATA`


```python
set CURRENTDIR="%cd%"
set FREECAD_USER_DATA=%CURRENTDIR%/..
start FreeCAD.exe -u %FREECAD_USER_DATA%/user.cfg -s %FREECAD_USER_DATA%/system.cfg```

za pomocą skryptu umieszczonego w katalogu głównym nośnika USB


```python
set CURRENTDIR=%cd%
set FREECAD_USER_DATA=%CURRENTDIR%FreeCAD\
start %cd%FreeCAD\bin\FreeCAD.exe -u %FREECAD_USER_DATA%user.cfg -s %FREECAD_USER_DATA%system.cfg
```

Teraz kliknij dwukrotnie plik wsadowy, aby uruchomić program FreeCAD. *([zobacz](https://forum.freecadweb.org/viewtopic.php?f=4&t=49028))*





 

_

---
[documentation index](../README.md) > [Developer Documentation](Category_Developer Documentation.md) > [Start](Start_Workbench.md) > Start up and Configuration/pl
