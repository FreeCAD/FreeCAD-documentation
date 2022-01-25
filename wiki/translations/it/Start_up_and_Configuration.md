# Start up and Configuration/it
<div class="mw-translate-fuzzy">





</div>


{{TOCright}}

## Overview


<div class="mw-translate-fuzzy">

Questa pagina descrive i diversi modi per avviare FreeCAD e le principali caratteristiche di configurazione.


</div>

## Avviare FreeCAD dalla riga di comando 

FreeCAD può essere avviato normalmente, facendo doppio clic sulla sua icona sul desktop o selezionandolo dal menu di avvio, ma può anche essere avviato direttamente dalla riga di comando. Ciò consente di modificare alcune delle opzioni di avvio di default.

### Using command line options without a command line shell 


<div class="mw-translate-fuzzy">

### Utilizzo delle opzioni della riga di comando senza una shell della riga di comando 

-   Su Ubuntu si può creare un\'icona sul desktop e modificarne le proprietà. Aggiungere le opzioni della riga di comando separate da spazi dopo il nome del programma nel campo \"Comando\".
-   Su Windows creare un collegamento e modificare le proprietà. Aggiungere le opzioni della riga di comando separate da spazi al campo \"Destinazione\".


</div>

### Le opzioni della riga di comando 

Le opzioni della riga di comando sono soggette a frequenti cambiamenti, quindi è bene verificare le opzioni correnti digitando:

FreeCAD --help

Nella risposta sono elencati i parametri utilizzabili:

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

++++
| Long option                               | Corresponding [config var name](#Configuration_set.md) | Synopsis                                                                                                                                                                                                                                                         |
+===========================================+================================================================+==================================================================================================================================================================================================================================================================+
|                            | UserParameter                                                  | Filename or relative path that ends with a filename. Defaults to `user.cfg`.                                                                                                                                                              |
| `--user-cfg <filename>`          |                                                                |                                                                                                                                                                                                                                                                  |
|                                        |                                                                |                                                                                                                                                                                                                                                                  |
++++
|                            | Prepends to AdditionalModulePaths                              | Directory that contains modules. This option can be given repeatedly to specify multiple directories.                                                                                                                                                            |
| `--module-path <dir>`            |                                                                |                                                                                                                                                                                                                                                                  |
|                                        |                                                                |                                                                                                                                                                                                                                                                  |
++++
|                            | most                                                           | Outputs the requested value in a popup dialog. Exits upon confirmation with **OK**. Cannot be used repeatedly. If an unknown/illegal variable name is used, the response is empty. The `--console` flag is not honored. |
| `--get-config <config-var-name>` |                                                                |                                                                                                                                                                                                                                                                  |
|                                        |                                                                |                                                                                                                                                                                                                                                                  |
++++

Options can written in two forms: `--long-option arg` and `--long-option<nowiki>=</nowiki>arg`.

### Risposta e file di configurazione 

FreeCAD può leggere alcune di queste opzioni da un file di configurazione. Questo file deve essere nella directory bin e deve essere nominato {{FileName|FreeCAD.cfg}}. Tenere presente che le opzioni specificate nella riga di comando sovrascrivono il file di configurazione!

Alcuni sistemi operativi hanno un limite di caratteri molto basso nella riga di comando. Il modo più comune per aggirare questa limitazione è quello di usare il file di risposta. Un file di risposta è semplicemente un file di configurazione che utilizza la stessa sintassi della riga di comando. Se la riga di comando specifica un nome di file di risposta da utilizzare, esso viene caricato e analizzato in aggiunta alla linea di comando:

    FreeCAD @ResponseFile.txt 

oppure:

    FreeCAD --response-file=ResponseFile.txt

or:

    FreeCAD --response-file ResponseFile.txt

### Opzioni nascoste 

Per l\'utente esistono alcune opzioni non visibili. Queste opzioni sono, per esempio, i parametri di X-Window analizzati dal sistema Windows:

-   -display display, imposta la visualizzazione di X (il valore predefinito è \$DISPLAY).
-   -geometry geometry, imposta la geometria client della prima finestra che viene visualizzata.
-   -fn oppure -font font, definisce il tipo carattere dell\'applicazione. Il carattere deve essere specificato utilizzando una descrizione logica dei font di X.
-   -bg oppure -background color, imposta il colore di sfondo predefinito e una tavolozza per applicarlo (sono calcolate le tonalità chiare e scure).
-   -fg oppure -foreground color, imposta il colore di primo piano predefinito.
-   -btn oppure -button color, imposta il colore predefinito dei pulsanti.
-   -name name, imposta il nome dell\'applicazione.
-   -title title, imposta il titolo dell\'applicazione.
-   -visual TrueColor, forza l\'applicazione a utilizzare una visualizzazione TrueColor su un display a 8-bit.
-   -ncols count, limita il numero di colori allocati nel cubo di colori su un display a 8 bit, se l\'applicazione sta usando la specifica di colore QApplication::ManyColor. Se count è 216 allora è utilizzato un cubo di colori di 6x6x6 (vale a dire 6 livelli di rosso, 6 di verde, e 6 di blu), per altri valori viene utilizzato un cubo approssimativamente proporzionale a un cubo 2x3x1.
-   -cmap, obbliga l\'applicazione a installare una mappa privata di colori su un display a 8 bit.


<div class="mw-translate-fuzzy">

## Eseguire FreeCAD senza interfaccia grafica 


</div>


<div class="mw-translate-fuzzy">

Di solito FreeCAD è costruito con due file eseguibili: uno con l\'interfaccia grafica chiamato {{FileName|FreeCAD}} e uno con sola riga di comando chiamato {{FileName|FreeCADCmd}}. FreeCAD può anche essere usato in modalità console usando l\'opzione \"-c\", questo è il comportamento predefinito di {{FileName|FreeCADCmd}}:


</div>

FreeCAD --console


<div class="mw-translate-fuzzy">

dalla riga di comando. In modalità console non viene visualizzata nessuna interfaccia utente, e appare un prompt dell\'interprete di Python. Da questo prompt di Python, si ha le stesse funzionalità che si ha dall\'interprete di Python che viene eseguito all\'interno della GUI di FreeCAD e si ha normale accesso a tutti i moduli e plugin di FreeCAD, eccettuato il modulo FreeCADGui. Tenere presente che anche i moduli che dipendono da FreeCADGui potrebbero non essere disponibili.


</div>

To read more about console or headless mode, refer to [Headless FreeCAD](Headless_FreeCAD.md).


<div class="mw-translate-fuzzy">

### Esempio lanciare un file 


</div>


<div class="mw-translate-fuzzy">

++++
| Execute a file                                            | System                | Command line configuration                                                                                                                          |
+===========================================================+=======================+=====================================================================================================================================================+
| Module, cfg                                               | Windows               |                                                                                                                                      |
|                                                           |                       | {{FileName|"C:\Program Files\FreeCAD\bin\FreeCAD.exe" -M "C:\FreeCAD\Mod\Draft" -u "C:\FreeCAD\Config\user.cfg" -s "C:\FreeCAD\Config\system.cfg"}} |
|                                                           |                       |                                                                                                                                                  |
++++
|                                                           | Linux                 |                                                                                                                                      |
|                                                           |                       | {{FileName|todo}}                                                                                                                                   |
|                                                           |                       |                                                                                                                                                  |
++++
|                                                           |                       |                                                                                                                                                     |
++++
| .FCMacro o .py                                            | Windows               |                                                                                                                                      |
|                                                           |                       | {{FileName|"C:\Program Files\FreeCAD\bin\FreeCAD.exe" "C:\Users\userName\AppData\Roaming\FreeCAD\Mod\WorkFeature\start_WF.FCMacro"}}                |
|                                                           |                       |                                                                                                                                                  |
++++
|                                                           | Linux                 |                                                                                                                                      |
|                                                           |                       | {{FileName|todo}}                                                                                                                                   |
|                                                           |                       |                                                                                                                                                  |
++++
| Eseguire automaticamente una macro all\'avvio di FreeCAD. | Windows / Linux / Mac | Andare su la pagina [Macro at Startup](Macro_at_Startup/it.md) Eseguire automaticamente una macro all\'avvio di FreeCAD.                    |
++++

: Linea di Commando configurazione per lanciare un file


</div>

See [Macro at Startup](Macro_at_Startup.md) on how to set up a macro to automatically run at FreeCAD startup.

## Environment variables 

FreeCAD supports the following environment variables, which can be used to configure directories: <small>(v0.19)</small> 

++++
| Environment variable         | Corresponding [config var name](#Configuration_set.md) | Synopsis                                                                                                                                    |
+==============================+================================================================+=============================================================================================================================================+
|               | UserHomePath                                                   | FreeCAD\'s \"base\" directory for keeping local user data.                                                                                  |
| `FREECAD_USER_HOME` |                                                                |                                                                                                                                             |
|                           |                                                                |                                                                                                                                             |
++++
|               | UserAppData                                                    | If not set, defaults to `FREECAD_USER_HOME/.FreeCAD`, but only if `FREECAD_USER_HOME` is set. |
| `FREECAD_USER_DATA` |                                                                |                                                                                                                                             |
|                           |                                                                |                                                                                                                                             |
++++
|               | AppTempPath                                                    | If not set, defaults to `FREECAD_USER_HOME/temp`, but only if `FREECAD_USER_HOME` is set.     |
| `FREECAD_USER_TEMP` |                                                                |                                                                                                                                             |
|                           |                                                                |                                                                                                                                             |
++++

If the specified path does not exist, the setting is ignored!

The above environment variables are meant to be used to realize a *portable* FreeCAD environment. For an example how environment variables can be used from the command line on Linux refer to the [notes for Linux users on the downloads page](Download#Notes_for_GNU.2FLinux_users.md).

### `HOME`

FreeCAD uses [Qt](Third_Party_Libraries#Qt.md), which does honor the `HOME` environmental variable. Thus, setting `HOME` can be used to specify the base directory of Qt-related configuration files (`.config/FreeCAD/FreeCAD.conf`).

FreeCad itself does not honor the `HOME` environmental variable (because it determines the user\'s home directory from a lower-level system API). Use `FREECAD_USER_HOME` for this pupose.

### `TMPDIR` 

The default temporary directory is {{FileName|/tmp/}}. The `TMPDIR` environmental variable can be used to override the default. (*Editor: precedence?*).

### Libraries


<div class="mw-translate-fuzzy">

Alcune librerie hanno bisogno di chiamare le variabili di ambiente del sistema. A volte, quando c\'è un problema con un\'installazione FreeCAD, è perché qualche variabile d\'ambiente è assente o è impostata in modo errato. Pertanto, alcune variabili importanti vengono duplicate in Config e salvate nel file di registro


</div>


<div class="mw-translate-fuzzy">

**Variabili d\'ambiente relative a Python:**


</div>

-   PYTHONPATH
-   PYTHONHOME
-   TCL\_LIBRARY
-   TCLLIBPATH


<div class="mw-translate-fuzzy">

**Variabili d\'ambiente relative a OpenCascade:**


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

## Il set di configurazione 


</div>


<div class="mw-translate-fuzzy">

A ogni avvio FreeCAD esamina i suoi ambienti ed i parametri della riga di comando. Si costruisce un **set di configurazione** che contiene l\'essenza delle informazioni per l\'esecuzione. Queste informazioni vengono poi utilizzate per determinare il luogo dove salvare i dati dell\'utente o file di log (registro). E\' anche molto importante per le analisi post-mortem. Pertanto viene salvato nel file di registro.


</div>

### Informazioni relative all\'utente 


<div class="mw-translate-fuzzy">

+++++
| Nome var config | Descrizione                                                                    | Esempio M\$                                                                      | Esempio Posix (Linux)                                                     |
+=================+================================================================================+==================================================================================+===========================================================================+
| UserAppData     | Percorso dove FreeCAD archivia i dati dell\'applicazione relativi all\'utente. |                                                                   |                                                            |
|                 |                                                                                | {{FileName|C:\Documents and Settings\username\AppData\FreeCAD}}                  | {{FileName|/home/username/.FreeCAD}}                                      |
|                 |                                                                                |                                                                               |                                                                        |
|                 |                                                                                |                                                                        |                                                                 |
|                 |                                                                                | <hr />                                                                           | <hr />                                                                    |
|                 |                                                                                |                                                                               |                                                                        |
|                 |                                                                                | \'\'Percorso breve : \'\'{{FileName|%APPDATA%\FreeCAD}}            | \'\'Percorso breve : \'\'{{FileName|~/.FreeCAD}}            |
+++++
| UserParameter   | File in cui FreeCAD archivia i dati dell\'applicazione relativi all\'utente.   |                                                                   |                                                            |
|                 |                                                                                | {{FileName|C:\Documents and Settings\username\AppData\FreeCAD\user.cfg}}         | {{FileName|/home/username/.FreeCAD/user.cfg}}                             |
|                 |                                                                                |                                                                               |                                                                        |
|                 |                                                                                |                                                                        |                                                                 |
|                 |                                                                                | <hr />                                                                           | <hr />                                                                    |
|                 |                                                                                |                                                                               |                                                                        |
|                 |                                                                                | \'\'Percorso breve : \'\'{{FileName|%APPDATA%\FreeCAD\user.cfg}}   | \'\'Percorso breve : \'\'{{FileName|~/.FreeCAD/user.cfg}}   |
+++++
| SystemParameter | File in cui FreeCAD archivia i dati relativi all\'applicazione.                |                                                                   |                                                            |
|                 |                                                                                | {{FileName|C:\Documents and Settings\username\AppData\FreeCAD\system.cfg}}       | {{FileName|/home/username/.FreeCAD/system.cfg}}                           |
|                 |                                                                                |                                                                               |                                                                        |
|                 |                                                                                |                                                                        |                                                                 |
|                 |                                                                                | <hr />                                                                           | <hr />                                                                    |
|                 |                                                                                |                                                                               |                                                                        |
|                 |                                                                                | \'\'Percorso breve : \'\'{{FileName|%APPDATA%\FreeCAD\system.cfg}} | \'\'Percorso breve : \'\'{{FileName|~/.FreeCAD/system.cfg}} |
+++++
| UserHomePath    | Percorso home dell\'utente corrente                                            |                                                                   |                                                            |
|                 |                                                                                | {{FileName|C:\Documents and Settings\username}}                                  | {{FileName|/home/username}}                                               |
|                 |                                                                                |                                                                               |                                                                        |
|                 |                                                                                |                                                                        |                                                                 |
|                 |                                                                                | <hr />                                                                           | <hr />                                                                    |
|                 |                                                                                |                                                                               |                                                                        |
|                 |                                                                                | \'\'Percorso breve : \'\'{{FileName|%USERPROFILE%}}                | \'\'Percorso breve : \'\'{{FileName|~}}                     |
+++++

: Voci di configurazione utente


</div>

Note: For Linux distributions, an additional configuration file that relates to [Qt](Third_Party_Tools#Qt-Toolkit.md) may exist at path {{FileName|/home/username/.config/FreeCAD/FreeCAD.conf}}.

### Argomenti della riga di comando 


<div class="mw-translate-fuzzy">

++++
| Nome var config       | Descrizione                                                                                                                                                                                                                                                                                                         | Esempio                                                                     |
+=======================+=====================================================================================================================================================================================================================================================================================================================+=============================================================================+
| LoggingFile           | 1 se il logging è attivato                                                                                                                                                                                                                                                                                          | 1                                                                           |
++++
| LoggingFileName       | Nome del file dove si trova il log                                                                                                                                                                                                                                                                                  |                                                              |
|                       |                                                                                                                                                                                                                                                                                                                     | {{FileName|C:\Documents and Settings\username\AppData\FreeCAD\FreeCAD.log}} |
|                       |                                                                                                                                                                                                                                                                                                                     |                                                                          |
++++
| RunMode               | Indica come funzionerà il ciclo principale. **\"Script\"** significa che richiama il file di script fornito e poi esce. **\"Cmd\"** esegue l\'interprete della riga di comando. **\"Internal\"** esegue uno script interno. **\"Gui\"** entra nel ciclo di evento Gui. **\"Module\"** carica un dato modulo python. | \"Cmd\"                                                                     |
++++
| FileName              | Il suo significato dipende da RunMode                                                                                                                                                                                                                                                                               |                                                                             |
++++
| ScriptFileName        | Il suo significato dipende da RunMode                                                                                                                                                                                                                                                                               |                                                                             |
++++
| Verbose               | Livello di verbosità di FreeCAD                                                                                                                                                                                                                                                                                     | \"\" o \"strict\"                                                           |
++++
| OpenFileCount         | Contiene il numero di file aperti attraverso gli argomenti della riga di comando                                                                                                                                                                                                                                    | \"12\"                                                                      |
++++
| AdditionalModulePaths | Contiene i percorsi di moduli aggiuntivi indicati nella linea di cmd                                                                                                                                                                                                                                                | \"extraModules/\"                                                           |
++++

: Voci di configurazione utente


</div>

### Relativi al sistema 


<div class="mw-translate-fuzzy">

+++++
| Nome var config  | Descrizione                                                                                                            | Esempioo M\$                             | Esempio Posix (Linux)                |
+==================+========================================================================================================================+==========================================+======================================+
| AppHomePath      | Percorso in cui è installato FreeCAD                                                                                   |                           |                       |
|                  |                                                                                                                        | {{FileName|c:/Progam Files/FreeCAD_0.7}} | {{FileName|/user/local/FreeCAD_0.7}} |
|                  |                                                                                                                        |                                       |                                   |
+++++
| PythonSearchPath | Contiene un elenco di percorsi dove python cerca i moduli. Questo vale all\'avvio e può cambiare durante l\'esecuzione |                                          |                                      |
+++++

: Voci di configurazione utente


</div>

### Informazioni relative alla costruzione 

La tabella seguente mostra le informazioni disponibili relative alla versione di costruzione. La maggior parte proviene dal repositorio di Subversion. Queste cose sono necessarie per ricostruire esattamente la versione!


<div class="mw-translate-fuzzy">

  Nome var config      Descrizione                                                                                                      Esempio
    
  BuildVersionMajor    Numero di versione principale della costruzione. Definito in {{FileName|src/Build/Version.h.in}}   0
  BuildVersionMinor    Numero di versione secondario della costruzione. Definito in {{FileName|src/Build/Version.h.in}}   7
  BuildRevision        Numero di revisione del repositorio SVN del src nella costruzione. Generato da SVN                               356
  BuildRevisionRange   Gamma di diversi cambiamenti                                                                                     123-356
  BuildRepositoryURL   URL del repositorio                                                                                              <https://free-cad.svn.sourceforge.net/svnroot/free-cad/trunk/src>
  BuildRevisionDate    Data della revisione precedente                                                                                  2007/02/03 22:21:18
  BuildScrClean        Indica se il codice sorgente è stato modificato dopo il suo checkout                                             Src modified
  BuildScrMixed                                                                                                                         Src not mixed

  : Voci di configurazione utente


</div>

### Relative al marchio 

Queste voci di configurazione sono legate al meccanismo di marchiatura di FreeCAD. Vedere [Marchiatura](Branding/it.md) per maggiori dettagli.


<div class="mw-translate-fuzzy">

++++
| Nome var config  | Descrizione                                                                                                                                 | Esempio                  |
+==================+=============================================================================================================================================+==========================+
| ExeName          | Nome del file di costruzione eseguibile. Può differire da quello di FreeCAD se è utilizzato un diverso {{FileName|main.cpp}}. |           |
|                  |                                                                                                                                             | {{FileName|FreeCAD.exe}} |
|                  |                                                                                                                                             |                       |
++++
| ExeVersion       | Versione globale mostrata all\'inizio                                                                                                       | V0.7                     |
++++
| AppIcon          | Icona che viene utilizzata per l\'eseguibile, mostrata in Application MainWindow.                                                           | \"FCIcon\"               |
++++
| ConsoleBanner    | Banner che viene mostrato in modalità console                                                                                               |                          |
++++
| SplashPicture    | Nome dell\'icona utilizzata per la schermata iniziale                                                                                       | \"FreeCADSplasher\"      |
++++
| SplashAlignment  | Allineamento del testo nella finestra di dialogo iniziale                                                                                   | \"Bottom o Left\"        |
++++
| SplashTextColor  | Colore del testo iniziale                                                                                                                   | \"\#000000\"             |
++++
| StartWorkbench   | Nome del Workbench che viene attivato automaticamente dopo l\'avvio                                                                         | \"Part design\"          |
++++
| HiddenDockWindow | Elenco dei dockwindows (separati da un punto e virgola) che saranno disabilitati                                                            | \"Property editor\"      |
++++

: Voci di configurazione utente


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

Or with `FREECAD_USER_DATA` ([see](https://forum.freecadweb.org/viewtopic.php?f=12&t=54784&start=60#p474759)):


```python
set CURRENTDIR="%cd%"
set FREECAD_USER_DATA=%CURRENTDIR%/..
start FreeCAD.exe -u %FREECAD_USER_DATA%/user.cfg -s %FREECAD_USER_DATA%/system.cfg```

With the batch in the root of the USB medium:


```python
set CURRENTDIR=%cd%
set FREECAD_USER_DATA=%CURRENTDIR%FreeCAD\
start %cd%FreeCAD\bin\FreeCAD.exe -u %FREECAD_USER_DATA%user.cfg -s %FREECAD_USER_DATA%system.cfg
```

Now double-click the batch file to start FreeCAD. ([see](https://forum.freecadweb.org/viewtopic.php?f=4&t=49028))


<div class="mw-translate-fuzzy">





</div>



---
![](images/Right_arrow.png) [documentation index](../README.md) > [Developer Documentation](Category_Developer Documentation.md) > [Start](Start_Workbench.md) > Start up and Configuration/it
