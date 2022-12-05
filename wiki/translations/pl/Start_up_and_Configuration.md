# Start up and Configuration/pl
**W wersji 0.20 programu FreeCAD w systemie Linux zmieniono domyślną lokalizację plików konfiguracji, danych i pamięci podręcznej programu..<br>
Więcej informacji można znaleźć na stronie [Informacje o wydaniu 0.20](Release_notes_0.20/pl#Rdze.C5.84_programu.md). Niniejsza strona nie została jeszcze odpowiednio zaktualizowana.**


{{TOCright}}

## Informacje ogólne 

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

++++
| Długa opcja                               | Odpowiednio [nazwa zmiennej konfiguracji](#Zestaw_konfiguracji.md) | Opis                                                                                                                                                                                                                                                                                                   |
+===========================================+============================================================================+========================================================================================================================================================================================================================================================================================================+
|                            | UserParameter                                                              | Nazwa pliku lub ścieżka względna, która kończy się nazwą pliku. Domyślnie `user.cfg`.                                                                                                                                                                                           |
| `--user-cfg <filename>`          |                                                                            |                                                                                                                                                                                                                                                                                                        |
|                                        |                                                                            |                                                                                                                                                                                                                                                                                                        |
++++
|                            | Poprzedza AdditionalModulePaths                                            | Katalog zawierający moduły. Opcja ta może być podana wielokrotnie, aby określić wiele katalogów.                                                                                                                                                                                                       |
| `--module-path <dir>`            |                                                                            |                                                                                                                                                                                                                                                                                                        |
|                                        |                                                                            |                                                                                                                                                                                                                                                                                                        |
++++
|                            | most                                                                       | Wyprowadza żądaną wartość w oknie kontekstowym. Kończy pracę po potwierdzeniu przyciskiem **OK**. Nie może być używane wielokrotnie. Jeśli użyto nieznanej / nieprawidłowej nazwy zmiennej, odpowiedź jest pusta. Flaga `--console` nie jest respektowana. |
| `--get-config <config-var-name>` |                                                                            |                                                                                                                                                                                                                                                                                                        |
|                                        |                                                                            |                                                                                                                                                                                                                                                                                                        |
++++

Opcje mogą być zapisane w dwóch formach: `--long-option arg` oraz `--long-option<nowiki>=</nowiki>arg`.

### Pliki odpowiedzi i konfiguracji 

FreeCAD może odczytać niektóre z tych opcji z pliku konfiguracyjnego. Plik ten musi znajdować się w ścieżce bin i musi mieć nazwę **FreeCAD.cfg**. Pamiętaj, że opcje podane w linii poleceń nadpisują plik konfiguracyjny!

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

FreeCAD jest zazwyczaj zbudowany z dwóch plików wykonywalnych: obsługującego GUI, zwanego **FreeCAD** lub **freecad**, oraz bez interfejsu graficznego, zwanego **FreeCADCmd** lub **freecadcmd**. FreeCAD może być używany w trybie konsoli przy użyciu przełącznika `--console` *(co jest domyślnym zachowaniem **FreeCADCmd**)*:

FreeCAD --console

W trybie konsoli nie będzie wyświetlany żaden graficzny interfejs użytkownika, a pojawi się znak zachęty interpretera Python: `>>>`. Z poziomu tego monitu masz taką samą funkcjonalność jak z interpreterem Python, który działa wewnątrz GUI FreeCAD, oraz dostęp do wszystkich modułów i wtyczek programu, z wyjątkiem modułu FreeCADGui. Należy pamiętać, że moduły zależne od FreeCADGui mogą być również niedostępne.

Aby dowiedzieć się więcej o konsoli lub trybie bez GUI, odwiedź stronę [FreeCAD bez GUI](Headless_FreeCAD/pl.md).

### Uruchamianie modułów, makrodefinicji i skryptów 

++++
| Typ pliku       | System             | Przykład w wierszu poleceń                                                                                                         |
+=================+====================+====================================================================================================================================+
| Moduł           | Windows            |                                                                                                                     |
|                 |                    | `"C:\Program Files\FreeCAD\bin\FreeCAD.exe" -M "C:\FreeCAD\Mod\Draft"`                                                    |
|                 |                    |                                                                                                                                 |
++++
|                 | Linux              |                                                                                                                     |
|                 |                    | `FreeCAD_0.19 -M ~/.FreeCAD/Mod/Draft`                                                                                    |
|                 |                    |                                                                                                                                 |
++++
|                 | Linux *(AppImage)* |                                                                                                                     |
|                 |                    | `path/to/FreeCADXXX.AppImage -M ~/.FreeCAD/Mod/Draft`                                                                     |
|                 |                    |                                                                                                                                 |
++++
|                 |                    |                                                                                                                                    |
++++
| .FCMacro or .py | Windows            |                                                                                                                     |
|                 |                    | `"C:\Program Files\FreeCAD\bin\FreeCAD.exe" "C:\Users\userName\AppData\Roaming\FreeCAD\Mod\WorkFeature\start_WF.FCMacro"` |
|                 |                    |                                                                                                                                 |
++++
|                 | Linux              |                                                                                                                     |
|                 |                    | `FreeCAD_0.19 ~/.FreeCAD/Mod/WorkFeature/start_WF.FCMacro`                                                                |
|                 |                    |                                                                                                                                 |
++++
|                 | Linux *(AppImage)* |                                                                                                                     |
|                 |                    | `path/to/FreeCADXXX.AppImage ~/.FreeCAD/Mod/WorkFeature/start_WF.FCMacro`                                                 |
|                 |                    |                                                                                                                                 |
++++

Zobacz na stronie [Automatyczne uruchamianie makroinstrukcji](Macro_at_Startup/pl.md) jak skonfigurować makrodefinicję do automatycznego uruchamiania przy starcie programu FreeCAD.

## Zmienne środowiskowe 

FreeCAD obsługuje następujące zmienne środowiskowe, które mogą być używane do konfigurowania katalogów: {{Version/pl|0.19}}

++++
| Zmienna środowiskowa         | Odpowiadająca [nazwa zmiennej konfiguracyjnej](#Zestaw_konfiguracji.md) | Opis                                                                                                                                                                                    |
+==============================+=================================================================================+=========================================================================================================================================================================================+
|               | UserHomePath                                                                    | FreeCAD\'s \"base\" directory for keeping local user data.                                                                                                                              |
| `FREECAD_USER_HOME` |                                                                                 |                                                                                                                                                                                         |
|                           |                                                                                 |                                                                                                                                                                                         |
++++
|               | UserAppData                                                                     | Jeśli nie jest ustawiony, domyślnie ustawia się na `FREECAD_USER_HOME/.FreeCAD`, ale tylko wtedy, gdy `FREECAD_USER_HOME` jest ustawiony. |
| `FREECAD_USER_DATA` |                                                                                 |                                                                                                                                                                                         |
|                           |                                                                                 |                                                                                                                                                                                         |
++++
|               | AppTempPath                                                                     | Jeśli nie jest ustawiony, domyślnie ustawia się na `FREECAD_USER_HOME/temp`, ale tylko wtedy, gdy `FREECAD_USER_HOME` jest ustawiony.     |
| `FREECAD_USER_TEMP` |                                                                                 |                                                                                                                                                                                         |
|                           |                                                                                 |                                                                                                                                                                                         |
++++

Jeśli podana ścieżka nie istnieje, ustawienie jest ignorowane!

Powyższe zmienne środowiskowe są przeznaczone do użycia w celu stworzenia *przenośnego* środowiska FreeCAD. Dla przykładu, jak zmienne środowiskowe mogą być używane z linii poleceń w systemie Linux, zapoznaj się z [uwagi dla użytkowników Linuksa na stronie z plikami do pobrania](Download/pl#Uwagi_dla_u.C5.BCytkownik.C3.B3w_systemu_GNU.2FLinux.md).

### `HOME`

FreeCAD używa biblioteki [Qt](Third_Party_Libraries/pl#Qt.md), która honoruje zmienną środowiskową `HOME`. Tak więc ustawienie `HOME` może być użyte do określenia katalogu bazowego plików konfiguracyjnych związanych z Qt *(`.config/FreeCAD/FreeCAD.conf`)*.

Sam FreeCad nie honoruje zmiennej środowiskowej `HOME` *(ponieważ określa katalog domowy użytkownika na podstawie systemowego API niższego poziomu)*. Do tego celu należy użyć zmiennej `FREECAD_USER_HOME`.

### `TMPDIR` 

Domyślnym katalogiem tymczasowym jest **/tmp/**. Zmienna środowiskowa `TMPDIR` może być użyta do zastąpienia domyślnego ustawienia. *(Edytor: pierwszeństwo?)*.

### Biblioteki

Niektóre biblioteki muszą wywoływać systemowe zmienne środowiskowe. Czasami, gdy pojawia się problem z instalacją programu FreeCAD, jest to spowodowane brakiem lub nieprawidłowym działaniem jakiejś zmiennej środowiskowej. Dlatego niektóre ważne zmienne zostają zduplikowane w Configu i zapisane w pliku logu.

**Python**

-   PYTHONPATH
-   PYTHONHOME
-   TCL_LIBRARY
-   TCLLIBPATH

**OpenCascade**

-   CSF_MDTVFontDirectory
-   CSF_MDTVTexturesDirectory
-   CSF_UnitsDefinition
-   CSF_UnitsLexicon
-   CSF_StandardDefaults
-   CSF_PluginDefaults
-   CSF_LANGUAGE
-   CSF_SHMessage
-   CSF_XCAFDefaults
-   CSF_GraphicShr
-   CSF_IGESDefaults
-   CSF_STEPDefaults

## Zestaw konfiguracji 

Przy każdym uruchomieniu FreeCAD bada swoje otoczenie i parametry wiersza poleceń. Tworzy **zestaw konfiguracyjny**, który zawiera esencję informacji o przebiegu pracy. Informacje te są później wykorzystywane do określenia miejsca, w którym zapisywane są dane użytkownika lub pliki dziennika. Jest ona również bardzo ważna dla analiz po awarii. Dlatego jest ona zapisywana w pliku logu.

### Informacje dotyczące użytkownika 

+++++
| Nazwa zmiennej konfiguracyjnej | Opis                                                                            | Przykład Windows                                                           | Przykład Linux                                                 |
+================================+=================================================================================+============================================================================+================================================================+
| UserAppData                    | Ścieżka, w której FreeCAD przechowuje dane aplikacji powiązane z użytkownikiem. |                                                             |                                                 |
|                                |                                                                                 | **C:\Documents and Settings\username\AppData\FreeCAD**            | **/home/username/.FreeCAD**                           |
|                                |                                                                                 |                                                                         |                                                             |
|                                |                                                                                 |                                                                  |                                                      |
|                                |                                                                                 | <hr />                                                                     | <hr />                                                         |
|                                |                                                                                 |                                                                         |                                                             |
|                                |                                                                                 | *Short path :***%APPDATA%\FreeCAD**                 | *Short path :***~/.FreeCAD**            |
+++++
| UserParameter                  | Plik, w którym FreeCAD przechowuje dane aplikacji powiązanych z użytkownikiem.  |                                                             |                                                 |
|                                |                                                                                 | **C:\Documents and Settings\username\AppData\FreeCAD\user.cfg**   | **/home/username/.FreeCAD/user.cfg**                  |
|                                |                                                                                 |                                                                         |                                                             |
|                                |                                                                                 |                                                                  |                                                      |
|                                |                                                                                 | <hr />                                                                     | <hr />                                                         |
|                                |                                                                                 |                                                                         |                                                             |
|                                |                                                                                 | *Short path :***%APPDATA%\FreeCAD\user.cfg**        | *Short path :***~/.FreeCAD/user.cfg**   |
+++++
| SystemParameter                | Plik, w którym FreeCAD przechowuje dane powiązane z aplikacją.                  |                                                             |                                                 |
|                                |                                                                                 | **C:\Documents and Settings\username\AppData\FreeCAD\system.cfg** | **/home/username/.FreeCAD/system.cfg**                |
|                                |                                                                                 |                                                                         |                                                             |
|                                |                                                                                 |                                                                  |                                                      |
|                                |                                                                                 | <hr />                                                                     | <hr />                                                         |
|                                |                                                                                 |                                                                         |                                                             |
|                                |                                                                                 | *Short path :***%APPDATA%\FreeCAD\system.cfg**      | *Short path :***~/.FreeCAD/system.cfg** |
+++++
| UserHomePath                   | Ścieżka domowa bieżącego użytkownika                                            |                                                             |                                                 |
|                                |                                                                                 | **C:\Documents and Settings\username**                            | **/home/username**                                    |
|                                |                                                                                 |                                                                         |                                                             |
|                                |                                                                                 |                                                                  |                                                      |
|                                |                                                                                 | <hr />                                                                     | <hr />                                                         |
|                                |                                                                                 |                                                                         |                                                             |
|                                |                                                                                 | *Short path :***%USERPROFILE%**                     | *Short path :***~**                     |
+++++

Uwaga: Dla dystrybucji Linuksa, dodatkowy plik konfiguracyjny, który odnosi się do biblioteki [Qt](Third_Party_Tools/pl#Qt-Toolkit.md) może istnieć w ścieżce **/home/username/.config/FreeCAD/FreeCAD.conf**.

### Argumenty dla wiersza poleceń 

++++
| Nazwa zmiennej konfiguracyjnej | Opis                                                                                                                                                                                                                                                                                         | Przykład                                                                    |
+================================+==============================================================================================================================================================================================================================================================================================+=============================================================================+
| LoggingFile                    | **1** - jeżeli logowanie jest włączone                                                                                                                                                                                                                                                       | 1                                                                           |
++++
| LoggingFileName                | Nazwa pliku, w którym umieszczany jest dziennik                                                                                                                                                                                                                                              |                                                              |
|                                |                                                                                                                                                                                                                                                                                              | **C:\Documents and Settings\username\AppData\FreeCAD\FreeCAD.log** |
|                                |                                                                                                                                                                                                                                                                                              |                                                                          |
++++
| RunMode                        | To wskazuje, jak będzie działać pętla główna. **Script** oznacza, że dany skrypt zostanie wywołany i następnie zakończony. **Cmd** uruchamia interpreter wiersza poleceń. **Internal** uruchamia skrypt wewnętrzny. **Gui** włącza pętlę zdarzeń Gui. **Module** ładuje podany moduł python. | \"Cmd\"                                                                     |
++++
| FileName                       | Znaczenie zależy od trybu RunMode                                                                                                                                                                                                                                                            |                                                                             |
++++
| ScriptFileName                 | Znaczenie zależy od trybu RunMode                                                                                                                                                                                                                                                            |                                                                             |
++++
| Verbose                        | Poziom szczegółowości FreeCAD                                                                                                                                                                                                                                                                | \"\" or \"strict\"                                                          |
++++
| OpenFileCount                  | Przechowuje liczbę plików otwartych przez argumenty wiersza poleceń                                                                                                                                                                                                                          | \"12\"                                                                      |
++++
| AdditionalModulePaths          | Przechowuje dodatkowe ścieżki do modułów podane w linii cmd                                                                                                                                                                                                                                  | \"extraModules/\"                                                           |
++++

### Związane z systemem 

+++++
| Nazwa zmiennej konfiguracyjnej | Opis                                                                                                                                                                                                                                                                                                                                                         | Przykład Windows                          | Przykład Linux                        |
+================================+==============================================================================================================================================================================================================================================================================================================================================================+===========================================+=======================================+
| AppHomePath                    | Ścieżka instalacji FreeCAD                                                                                                                                                                                                                                                                                                                                   |                            |                        |
|                                |                                                                                                                                                                                                                                                                                                                                                              | **c:/Progam Files/FreeCAD_0.19** | **/user/local/FreeCAD_0.19** |
|                                |                                                                                                                                                                                                                                                                                                                                                              |                                        |                                    |
+++++
| PythonSearchPath               | Przechowuje listę ścieżek, według których python wyszukuje moduły. Dotyczy startu może się zmienić podczas wykonywania.                                                                                                                                                                                                                                      |                                           |                                       |
+++++
| AppTempPath                    | Ścieżka do katalogu tymczasowego. Może być podana za pomocą zmiennej środowiskowej `TMPDIR`, lub za pomocą <img alt="" src=images/Std_DlgParameter.svg  style="width:16px;"> [Edytora Parametrów](Std_DlgParameter/pl.md): **Przybory → Edycja parametrów → BaseApp → Preferences → General → TempPath** |                                           |                        |
|                                |                                                                                                                                                                                                                                                                                                                                                              |                                           | **/tmp/**                    |
|                                |                                                                                                                                                                                                                                                                                                                                                              |                                           |                                    |
|                                |                                                                                                                                                                                                                                                                                                                                                              |                                           | *(domyślnie)*                         |
+++++

### Informacje dotyczące kompilacji 

Poniższa tabela pokazuje dostępne informacje na temat wersji Build. Większość z nich pochodzi z repozytorium Subversion. Te informacje są niezbędne do dokładnej przebudowy wersji!

  Nazwa zmiennej konfiguracyjnej   Opis                                                                                                  Przykład
    
  BuildVersionMajor                Główny numer wersji kompilacji. Zdefiniowany w **src/Build/Version.h.in**      0
  BuildVersionMinor                Podrzędny numer wersji kompilacji. Zdefiniowany w **src/Build/Version.h.in**   7
  BuildRevision                    Numer rewizji Repozytorium SVN źródeł w kompilacji. Generowane przez SVN                              356
  BuildRevisionRange               Zakres różnych zmian                                                                                  123-356
  BuildRepositoryURL               URL Repozytorium                                                                                      <https://free-cad.svn.sourceforge.net/svnroot/free-cad/trunk/src>
  BuildRevisionDate                Data powyższej zmiany                                                                                 2007/02/03 22:21:18
  BuildScrClean                    Wskazuje, czy źródło zostało zmienione po wydaniu                                                     Src modified
  BuildScrMixed                                                                                                                          Src not mixed

### Związane z budowaniem marki 

Te wpisy konfiguracyjne są związane z mechanizmem brandingu FreeCAD. Zobacz temat [FreeCAD jako produkt obcej marki](Branding/pl.md), aby uzyskać więcej szczegółów.

++++
| Nazwa zmiennej konfiguracyjnej | Opis                                                                                                                       | Przykład                 |
+================================+============================================================================================================================+==========================+
| ExeName                        | Nazwa pliku wykonywalnego kompilacji. Może się różnić od FreeCAD, jeśli użyto innego **main.cpp**.. |           |
|                                |                                                                                                                            | **FreeCAD.exe** |
|                                |                                                                                                                            |                       |
++++
| ExeVersion                     | Numer ogólny wersji, wyświetlany jest w czasie startu                                                                      | \"0.19\"                 |
++++
| AppIcon                        | Ikona, która jest zastosowana dla pliku wykonywalnego, wyświetlana w oknie głównym aplikacji.                              | \"FCIcon\"               |
++++
| ConsoleBanner                  | Baner, który jest wyświetlany w trybie konsoli                                                                             |                          |
++++
| SplashPicture                  | Nazwa ikony używanej dla Ekranu powitalnego *(Splash Screen)*                                                              | \"FreeCADSplasher\"      |
++++
| SplashAlignment                | Wyrównanie tekstu w oknie dialogowym ekranu powitalnego                                                                    | \"Bottom\" lub \"Left\"  |
++++
| SplashTextColor                | Kolor tekstu ekranu powitalnego                                                                                            | \"#000000\"              |
++++
| StartWorkbench                 | NNazwa środowiska pracy, które automatycznie zostanie uruchomione po starcie.                                              | \"Part design\"          |
++++
| HiddenDockWindow               | Lista okien dokowanych *(oddzielonych średnikiem)*, które zostaną wyłączone                                                | \"Property editor\"      |
++++

### Zapytania o konfigurację 

**Z konsoli Python programu FreeCAD**

Wpisy w zestawie konfiguracyjnym mogą być wyszukiwane za pomocą **config var name** *(patrz tabele powyżej)* z [konsoli środowiska Python](Python_console/pl.md). Na przykład:

 >>> FreeCAD.ConfigGet("ExeVersion")
 '0.19'

Jeśli nazwa nie zostanie znaleziona, zwracany jest pusty ciąg znaków.

**Z linii wiersza poleceń**

Użyj opcji `--get-config <config-var-name>` aby zapytać o pojedynczą nazwę. Nie wszystkie nazwy są obsługiwane. Na przykład:

 FreeCAD --get-config ExeVersion

Użyj opcji `--dump-config`, aby uzyskać listę nazw i ich wartości. Nie wszystkie nazwy są obsługiwane.

**Z konsoli FreeCAD**

Uruchom FreeCAD w trybie konsoli za pomocą `--console` i zadawaj pytania za pomocą kodu Python. Na przykład: 
```python
  $ FreeCAD --console
  [FreeCAD Console mode <Use Ctrl-D (i.e. EOF) to exit.>]
  >>> FreeCAD.ConfigGet("ExeVersion")
  '0.19'
  >>> exit()
```

Dla Linuksa *(powłoka bash)* możesz zmodyfikować następującą linię poleceń, aby dostosować ją do swoich potrzeb: 
```python
  $ FreeCAD --console <<EOF
  print( "FREECAD_USER_HOME: " + ( "not set" if ( os.environ.get('FREECAD_USER_HOME') is None ) else os.environ.get('FREECAD_USER_HOME') ) )
  print( "UserHomePath: " + FreeCAD.ConfigGet("UserHomePath") )
  exit()
  EOF
```

## Uruchamianie programu FreeCAD z pulpitu 

### Linux: Tworzenie dodatkowej opcji startowej 

Poniżej zakładamy, że Twój pulpit jest tak skonfigurowany, że możesz z niego uruchomić FreeCAD. W zależności od dystrybucji Linuksa i środowiska graficznego, być może będziesz musiał dostosować następujące kroki:

1.  Skopiuj plik wpisu freedesktop dla FreeCAD z lokalizacji **/usr/share/applications/freecad.desktop** do **~/.local/share/applications**.
2.  Zmień nazwę pliku z **freecad.desktop** na coś innego *(np. **MyFreeCADConfig.desktop**)*.
3.  Otwórz plik w edytorze tekstu i zmień sposób wywoływania aplikacji FreeCAD, modyfikując linię zaczynającą się od `Exec`.
4.  W wyniku tego pojawi się dodatkowa pozycja w Twoim menu startowym/uruchomieniu aplikacji. W ten sposób możesz mieć wiele wpisów dla FreeCAD z różnymi opcjami uruchamiania.

## Uruchamianie programu FreeCAD z nośnika USB 


{{Version/pl|0.19}}

**Windows**

Umieść plik wykonywalny FreeCAD, **FreeCAD.exe**, na nośniku USB. Utwórz plik wsadowy **FreeCAD.bat** i umieść go w tym samym katalogu co **FreeCAD.exe**. Wewnątrz pliku wsadowego napisz:


```python
set CURRENTDIR=%cd%
set FREECAD_USER_HOME=%CURRENTDIR%
start FreeCAD.exe -u FreeCAD/user.cfg -s FreeCAD/system.cfg --write-log 
```

Or with `FREECAD_USER_DATA` ([see](https://forum.freecadweb.org/viewtopic.php?f=12&t=54784&start=60#p474759)):


```python
set CURRENTDIR="%cd%"
set FREECAD_USER_DATA=%CURRENTDIR%/..
start FreeCAD.exe -u %FREECAD_USER_DATA%/user.cfg -s %FREECAD_USER_DATA%/system.cfg```

Za pomocą skryptu umieszczonego w katalogu głównym nośnika USB


```python
set CURRENTDIR=%cd%
set FREECAD_USER_DATA=%CURRENTDIR%FreeCAD\
start %cd%FreeCAD\bin\FreeCAD.exe -u %FREECAD_USER_DATA%user.cfg -s %FREECAD_USER_DATA%system.cfg
```

Teraz kliknij dwukrotnie plik wsadowy, aby uruchomić program FreeCAD. *([zobacz](https://forum.freecadweb.org/viewtopic.php?f=4&t=49028))*



---
![](images/Right_arrow.png) [documentation index](../README.md) > [Developer Documentation](Category_Developer Documentation.md) > [Start](Start_Workbench.md) > Start up and Configuration/pl
