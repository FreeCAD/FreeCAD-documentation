# Start up and Configuration/sv
{{TOCright}}


<div class="mw-translate-fuzzy">

Denna sida visar olika sätt att starta FreeCAD och de viktigaste konfigurationsegenskaperna.


</div>

## Starta FreeCAD från Kommandoraden 

FreeCAD kan startas normalt, genom att dubbelklicka på dess skrivbordsikon eller genom att välja den från startmenyn, men det kan också startas direkt från kommandoraden. Detta tillåter dig att ändra några av standard uppstartsalternativen.

### Using command line options without a command line shell 

-   On Ubuntu you can create a desktop icon and edit its properties. Add the command line options separated by spaces behind the program name in the \"Command\" field.
-   On Windows create a shortcut and edit the properties. Add the command line options separated by spaces to \"Target\" field.

### Kommandoradsalternativ


<div class="mw-translate-fuzzy">

Kommandoradsalternativen förändras ofta, så därför är det en bra ide att kontrollera alternativen genom att skriva:


</div>

FreeCAD --help

Från svaret kan du läsa de möjliga parametrarna:

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

In the following table, selected options are described in more detail:

+-------------------------------------------+----------------------------------------------------------------+------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| Long option                               | Corresponding [config var name](#Configuration_set.md) | Synopsis                                                                                                                                                                                                                                                         |
+===========================================+================================================================+==================================================================================================================================================================================================================================================================+
|                            | UserParameter                                                  | Filename or relative path that ends with a filename. Defaults to `user.cfg`.                                                                                                                                                              |
| `--user-cfg <filename>`          |                                                                |                                                                                                                                                                                                                                                                  |
|                                        |                                                                |                                                                                                                                                                                                                                                                  |
+-------------------------------------------+----------------------------------------------------------------+------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
|                            | Prepends to AdditionalModulePaths                              | Directory that contains modules. This option can be given repeatedly to specify multiple directories.                                                                                                                                                            |
| `--module-path <dir>`            |                                                                |                                                                                                                                                                                                                                                                  |
|                                        |                                                                |                                                                                                                                                                                                                                                                  |
+-------------------------------------------+----------------------------------------------------------------+------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
|                            | most                                                           | Outputs the requested value in a popup dialog. Exits upon confirmation with **OK**. Cannot be used repeatedly. If an unknown/illegal variable name is used, the response is empty. The `--console` flag is not honored. |
| `--get-config <config-var-name>` |                                                                |                                                                                                                                                                                                                                                                  |
|                                        |                                                                |                                                                                                                                                                                                                                                                  |
+-------------------------------------------+----------------------------------------------------------------+------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+

Options can written in two forms: `--long-option arg` and `--long-option<nowiki>=</nowiki>arg`.

### Respons och konfigurationsfiler 


<div class="mw-translate-fuzzy">

FreeCAD kan läsa en del av dessa alternativ från en konfigurationsfil. Denna fil måste ligga i bin sökvägen och måste ha namnet FreeCAD.cfg. Tänk på att alternativ som specificeras på kommandoraden har högre prioritet än konfigurationsfilen!


</div>

En del operativsystem har en låg gräns på kommandoradens längd. Det vanliga sättet att komma runt dessa begränsningar är att använda responsfiler. En responsfil är bara en konfigurationsfil som använder samma syntax som kommandoraden. Om kommandoraden specificerar namnet på den responsfil som ska användas, så laddas den och läses i tillägg till kommandoraden:

    FreeCAD @ResponseFile.txt 

eller:

    FreeCAD --response-file=ResponseFile.txt

or:

    FreeCAD --response-file ResponseFile.txt

### Gömda alternativ 

Det finns en del alternativ som inte visas för användaren. Dessa alternativ är egentligen X-fönsterparametrar som läses av fönstersystemet:

-   -display display, väljer X skärmen (standard är \$DISPLAY).
-   -geometry geometry, väljer klientgeometrin för det första fönstret som visas.
-   -fn or -font font, definierar applikationens typsnitt. Typsnittet ska specificeras med en X logisk typsnittsbeskrivning.
-   -bg or -background color, väljer standard bakgrundsfärg och en applikationspalett (ljusa och mörka skuggor beräknas).
-   -fg or -foreground color, väljer standard förgrundsfärg.
-   -btn or -button color, väljer standard knappfärg.
-   -name name, väljer applikationsnamnet.
-   -title title, väljer applikationstiteln.
-   -visual TrueColor, tvingar applikationen att använda TrueColor på en 8-bits skärm.
-   -ncols count, Begränsar antalet färger som allokeras i färgkuben på en 8-bitars skärm, om applikationen använder QApplication::ManyColor färgspecifikationen. Om antalet är 216 så används en 6x6x6 färgkub (d.v.s. 6 nivåer på rött, 6 på grönt, och 6 på blått); för andra värden, så används en kub som är ungefärligt proportionell till en 2x3x1 kub.
-   -cmap, får applikationen att installera en privat färgkarta på en 8-bitars skärm.


<div class="mw-translate-fuzzy">

## Köra FreeCAD utan användargränssnitt 


</div>


<div class="mw-translate-fuzzy">

FreeCAD startar normalt i gränssnittsläge, men du kan också tvinga det att starta i konsolläge genom att skriva:


</div>

FreeCAD --console


<div class="mw-translate-fuzzy">

på kommandoraden. I konsolläge, så kommer inget användargränssnitt att visas, och du kommer att presenteras med en pythontolks prompt. Från den pythonprompten så har du samma funktionalitet som den pythontolk som körs inuti FreeCAD gränssnittet, med normal åtkomst till alla FreeCADs moduler och plugin, förutom FreeCADGui modulen. Tänk på att moduler som beror på FreeCADGui kanske inte heller finns tillgängliga.


</div>

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

## Environment variables 

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


<div class="mw-translate-fuzzy">

En del bibliotek behöver anropa systemmiljövariabler. ibland när det är ett problem med en FreeCAD installation, så beror det på att en del miljövariabler saknas eller är felinställda. Därför dupliceras några viktiga variabler i Konfigurationen och sparas i loggfilen.


</div>


<div class="mw-translate-fuzzy">

**Python relaterade miljövariabler:**


</div>

-   PYTHONPATH
-   PYTHONHOME
-   TCL\_LIBRARY
-   TCLLIBPATH


<div class="mw-translate-fuzzy">

**OpenCascade relaterade miljövariabler:**


</div>

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


<div class="mw-translate-fuzzy">

## Konfigurationssetet


</div>


<div class="mw-translate-fuzzy">

Vid varje uppstart så undersöker FreeCAD sin omgivning och kommandoradsparametrarna. Det bygger upp ett **configuration set** vilket innehåller den huvudsakliga körinformationen. Denna information används senare för att avgöra vilken plats som användardata eller loggfiler ska sparas. Det är också mycket viktigt för postmortem analyser. Därför så sparas det i loggfilen.


</div>

### Användarrelaterad information 


<div class="mw-translate-fuzzy">

  Konfig. var. namn   Förklaring                                                      Exempel M\$                                                                   Exempel Posix (Linux)
  ------------------- --------------------------------------------------------------- ----------------------------------------------------------------------------- ------------------------------------
  UserAppData         Sökväg där FreeCAD lagrar användarrelaterad applikationsdata.   C:\\Documents and Settings\\username\\Application Data\\FreeCAD               /home/username/.FreeCAD
  UserParameter       Fil där FreeCAD lagrar användarrelaterad applikationsdata.      C:\\Documents and Settings\\username\\Application Data\\FreeCAD\\user.cfg     /home/username/.FreeCAD/user.cfg
  SystemParameter     Fil där FreeCAD lagrar applikationsrelaterad data.              C:\\Documents and Settings\\username\\Application Data\\FreeCAD\\system.cfg   /home/username/.FreeCAD/system.cfg
  UserHomePath        Nuvarande användares sökväg till hem mappen                     C:\\Documents and Settings\\username\\My Documents                            /home/username

  : Användarkonfiguration


</div>

Note: For Linux distributions, an additional configuration file that relates to [Qt](Third_Party_Tools#Qt-Toolkit.md) may exist at path {{FileName|/home/username/.config/FreeCAD/FreeCAD.conf}}.

### Kommandoradsargument


<div class="mw-translate-fuzzy">

  Konfig. var. namn       Förklaring                                                                                                                                                                                                                                                                                                       Exempel
  ----------------------- ---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- ------------------------------------------------------------------------------
  LoggingFile             1 om loggningen är påslagen                                                                                                                                                                                                                                                                                      1
  LoggingFileName         Filnamn där loggen sparas                                                                                                                                                                                                                                                                                        C:\\Documents and Settings\\username\\Application Data\\FreeCAD\\FreeCAD.log
  RunMode                 Detta indikerar hur huvudslingan kommer att fungera. **\"Script\"** innebär att det givna skriptet anropas och avslutas efter det. **\"Cmd\"** kör kommandotolken. **\"Internal\"** kör ett internt skript. **\"Gui\"** startar händelseslingan för gränssnittet. **\"Module\"** laddar en given python modul.   \"Cmd\"
  FileName                Innebörd beror på RunMode                                                                                                                                                                                                                                                                                        
  ScriptFileName          Innebörd beror på RunMode                                                                                                                                                                                                                                                                                        
  Verbose                 FreeCADs pratighet, d.v.s. hur mycket som loggas                                                                                                                                                                                                                                                                 \"\" eller \"strict\"
  OpenFileCount           Innehåller antalet filer som öppnas genom kommandoradsargument                                                                                                                                                                                                                                                   \"12\"
  AdditionalModulePaths   Innehåller sökvägen för de extramoduler som ges i kommandoraden                                                                                                                                                                                                                                                  \"extraModules/\"

  : Användarkonfiguration


</div>

### Systemrelaterat


<div class="mw-translate-fuzzy">

  Konfig. var. namn   Förklaring                                                                                                           Exempel M\$                    Exempel Posix (Linux)
  ------------------- -------------------------------------------------------------------------------------------------------------------- ------------------------------ --------------------------
  AppHomePath         Sökväg där FreeCAD är installerat                                                                                    c:/Progam Files/FreeCAD\_0.7   /user/local/FreeCAD\_0.7
  PythonSearchPath    Innehåller en lista på sökvägar där python söker efter moduler. Detta är vid uppstart och kan ändras under körning                                  

  : Användarkonfiguration


</div>

### Bygga relaterad information 


<div class="mw-translate-fuzzy">

Tabellen nedan visar tillgänglig information om Byggversionen. Det flesta av dem kommer från Subversion förrådet. dessa saker behövs för att exakt återuppbygga en version!


</div>


<div class="mw-translate-fuzzy">

  Konfig. var. namn    Förklaring                                                                Exempel
  -------------------- ------------------------------------------------------------------------- -------------------------------------------------------------------
  BuildVersionMajor    Byggningens Major Versionsnummer. Definierad i src/Build/Version.h.in     0
  BuildVersionMinor    Byggningens Minor Versionsnummer. Definierad i src/Build/Version.h.in     7
  BuildRevision        Källkodens SVN Repository Revisionnummer i byggningen. Genererad av SVN   356
  BuildRevisionRange   Område för olika ändringar                                                123-356
  BuildRepositoryURL   URL adress för förråd                                                     <https://free-cad.svn.sourceforge.net/svnroot/free-cad/trunk/src>
  BuildRevisionDate    Datum av ovanstående Revision                                             2007/02/03 22:21:18
  BuildScrClean        Indikerar om källkoden har ändrats efter kontroll                         Källkod ändrad
  BuildScrMixed                                                                                  Källkod inte blandad

  : Användarkonfiguration


</div>

### Märkningsrelaterat


<div class="mw-translate-fuzzy">

Dessa konfigurationspunkter är relaterade till FreeCADs märkningsmekanism. Se [Branding/sv](Branding/sv.md) för mer detaljer.


</div>


<div class="mw-translate-fuzzy">

  Konfig. var. namn   Förklaring                                                                               Exempel
  ------------------- ---------------------------------------------------------------------------------------- ---------------------
  ExeName             Namn på den byggda körfilen. Kan skilja sig från FreeCAD om en annan main.cpp används.   FreeCAD.exe
  ExeVersion          Allmän version som visas vid uppstart                                                    V0.7
  AppIcon             Ikon som används för körfilen, visas i Applikationens huvudfönster.                      \"FCIcon\"
  ConsoleBanner       Den banner som visas i konsolläge                                                        
  SplashPicture       Namn på den ikon som används till uppstartsskärmen                                       \"FreeCADSplasher\"
  SplashAlignment     Textjustering i uppstartsdialogen                                                        \"Bottom\|Left\"
  SplashTextColor     Textfärg i uppstartsfönstret                                                             \"\#000000\"
  StartWorkbench      Namn på den arbetsbänk som ska startas automatiskt efter uppstart                        \"Part design\"
  HiddenDockWindow    Lista på dockningsfönster (separerade av semikolon) som kommer att inaktiveras           \"Property editor\"

  : Användarkonfiguration


</div>

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

**From FreeCAD console**

Start FreeCAD in console mode with `--console` and query with Python code. For example:

 $ FreeCAD_0.19 --console
 [FreeCAD Console mode <Use Ctrl-D (i.e. EOF) to exit.>]
 >>> FreeCAD.ConfigGet("ExeVersion")
 '0.19'
 >>> exit()

For Linux (bash shell) you can modify the following command line to suit your needs:

 $ FreeCAD_0.19 --console <<EOF
 print( "FREECAD_USER_HOME: " + ( "not set" if ( os.environ.get('FREECAD_USER_HOME') is None ) else os.environ.get('FREECAD_USER_HOME') ) )
 print( "UserHomePath: " + FreeCAD.ConfigGet("UserHomePath") )
 exit()
 EOF

## Starting FreeCAD from the desktop 

### Linux: Creating an additional start option 

The following assumes that your desktop is configured such that you can launch FreeCAD from it. Depending on your Linux distribution and desktop environment, you may have to adapt the following steps:

1.  Copy the freedesktop entry file for FreeCAD from {{FileName|/usr/share/applications/freecad.desktop}} to {{FileName|~/.local/share/applications}}.
2.  Change the name from {{FileName|freecad.desktop}} to something else (e.g. {{FileName|MyFreeCADConfig.desktop}}).
3.  Open the file with a text editor and change how FreeCAD is invoked by modifying the line starting with `Exec`.
4.  As a result, an additional entry in your start menu/application launcher is available. This way, you can have multiple FreeCAD entries with various launch options.

## Starting FreeCAD from a portable USB medium 


<small>(v0.19)</small> 

**Windows**

Put the FreeCAD executable, {{FileName|FreeCAD.exe}}, on the USB medium. Create a batch file, {{FileName|FreeCAD.bat}}, and put it into the same directory as {{FileName|FreeCAD.exe}}. Inside the batch file write:


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

Now double-click the batch file to start FreeCAD. ([see](https://forum.freecadweb.org/viewtopic.php?f=4&t=49028))


<div class="mw-translate-fuzzy">


{{docnav/sv|Third Party Tools/sv|FreeCAD Build Tool/sv}}


</div>


 

_

---
[documentation index](../README.md) > [Developer Documentation](Category_Developer Documentation.md) > [Start](Start_Workbench.md) > Start up and Configuration/sv
