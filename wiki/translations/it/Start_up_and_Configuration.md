# Start up and Configuration/it
**In FreeCAD versione 0.20 la posizione predefinita dei file di configurazione, dati e cache del programma è stata modificata per Linux.<br>
Vedere [Note sulla versione 0.20](Release_notes_0.20/it#Core.md) per ulteriori informazioni. Questa pagina non è stata ancora aggiornata di conseguenza.**






## Panoramica

Questa pagina descrive i diversi modi per avviare FreeCAD e le principali caratteristiche di configurazione.



## Avviare FreeCAD dalla riga di comando 

FreeCAD può essere avviato normalmente, facendo doppio clic sulla sua icona sul desktop o selezionandolo dal menu di avvio, ma può anche essere avviato direttamente dalla riga di comando. Ciò consente di modificare alcune delle opzioni di avvio di default.



### Utilizzo delle opzioni della riga di comando senza una shell della riga di comando 

-   Su Ubuntu si può creare un\'icona sul desktop e modificarne le proprietà. Aggiungere le opzioni della riga di comando separate da spazi dopo il nome del programma nel campo \"Comando\".
-   Su Windows creare un collegamento e modificare le proprietà. Aggiungere le opzioni della riga di comando separate da spazi al campo \"Destinazione\".



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

Nella tabella seguente, le opzioni selezionate sono descritte in modo più dettagliato:

++++
| Opzione lunga                             | [Nome della variabile di configurazione](#Set_di_configurazione.md) corrispondente | Sinossi                                                                                                                                                                                                                                                                                                 |
+===========================================+============================================================================================+=========================================================================================================================================================================================================================================================================================================+
|                            | UserParameter                                                                              | Nome file o percorso relativo che termina con un nome file. Il valore predefinito è `user.cfg`.                                                                                                                                                                                  |
| `--user-cfg <filename>`          |                                                                                            |                                                                                                                                                                                                                                                                                                         |
|                                        |                                                                                            |                                                                                                                                                                                                                                                                                                         |
++++
|                            | Antepone a AdditionalModulePaths                                                           | Directory che contiene moduli. Questa opzione può essere fornita ripetutamente per specificare più directory.                                                                                                                                                                                           |
| `--module-path <dir>`            |                                                                                            |                                                                                                                                                                                                                                                                                                         |
|                                        |                                                                                            |                                                                                                                                                                                                                                                                                                         |
++++
|                            | most                                                                                       | Emette il valore richiesto in una finestra di dialogo popup. Esce alla conferma con **OK**. Non può essere utilizzato ripetutamente. Se viene utilizzato un nome di variabile sconosciuto/illegale, la risposta è vuota. Il flag `--console` non è rispettato. |
| `--get-config <config-var-name>` |                                                                                            |                                                                                                                                                                                                                                                                                                         |
|                                        |                                                                                            |                                                                                                                                                                                                                                                                                                         |
++++

Le opzioni possono essere scritte in due forme: `--long-option arg` e `--long-option<nowiki>=</nowiki>arg`.



### Risposta e file di configurazione 

FreeCAD può leggere alcune di queste opzioni da un file di configurazione. Questo file deve essere nella directory bin e deve essere nominato **FreeCAD.cfg**. Tenere presente che le opzioni specificate nella riga di comando sovrascrivono il file di configurazione!

Alcuni sistemi operativi hanno un limite di caratteri molto basso nella riga di comando. Il modo più comune per aggirare questa limitazione è quello di usare il file di risposta. Un file di risposta è semplicemente un file di configurazione che utilizza la stessa sintassi della riga di comando. Se la riga di comando specifica un nome di file di risposta da utilizzare, esso viene caricato e analizzato in aggiunta alla linea di comando:

    FreeCAD @ResponseFile.txt 

oppure:

    FreeCAD --response-file=ResponseFile.txt

oppure:

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



## Eseguire FreeCAD senza GUI (senza testa) 

Di solito FreeCAD è costruito con due file eseguibili: uno con l\'interfaccia grafica chiamato **FreeCAD** o **freecad** e uno headless chiamato **FreeCADCmd** o **freecadcmd**. FreeCAD può essere utilizzato in modalità console utilizzando l\'opzione `--console` (che è il comportamento predefinito di **FreeCADCmd**):

FreeCAD --console

In modalità console, non verrà visualizzata alcuna interfaccia utente grafica e ti verrà presentato un prompt dell\'interprete Python: `>>>`. Da quel prompt, hai le stesse funzionalità dell\'interprete Python che gira all\'interno della GUI di FreeCAD e accedi a tutti i moduli e plugin di FreeCAD, eccetto il modulo FreeCADGui. Tieni presente che anche i moduli che dipendono da FreeCADGui potrebbero non essere disponibili.

Per ulteriori informazioni sulla modalità console o headless, fare riferimento a [FreeCAD Headless](Headless_FreeCAD/it.md).



### Esecuzione di moduli, macro e script 

++++
| Tipo di file   | Sistema          | Esempio di riga di comando                                                                                                        |
+================+==================+===================================================================================================================================+
| Modulo         | Windows          |                                                                                                                    |
|                |                  | `"C:\Programmi\FreeCAD\bin\FreeCAD.exe" -M "C:\FreeCAD\Mod\Draft"`                                                       |
|                |                  |                                                                                                                                |
++++
|                | Linux            |                                                                                                                    |
|                |                  | `FreeCAD_0.19 -M ~/.FreeCAD/Mod/Draft`                                                                                   |
|                |                  |                                                                                                                                |
++++
|                | Linux (AppImage) |                                                                                                                    |
|                |                  | `percorso/di/FreeCADXXX.AppImage -M ~/.FreeCAD/Mod/Draft`                                                                |
|                |                  |                                                                                                                                |
++++
|                |                  |                                                                                                                                   |
++++
| .FCMacro o .py | Windows          |                                                                                                                    |
|                |                  | `"C:\Programmi\FreeCAD\bin\FreeCAD.exe" "C:\Utenti\nomeutente\AppData\Roaming\FreeCAD\Mod\WorkFeature\start_WF.FCMacro"` |
|                |                  |                                                                                                                                |
++++
|                | Linux            |                                                                                                                    |
|                |                  | `FreeCAD_0.19 ~/.FreeCAD/Mod/WorkFeature/start_WF.FCMacro`                                                               |
|                |                  |                                                                                                                                |
++++
|                | Linux (AppImage) |                                                                                                                    |
|                |                  | `percorso/di/FreeCADXXX.AppImage ~/.FreeCAD/Mod/WorkFeature/start_WF.FCMacro`                                            |
|                |                  |                                                                                                                                |
++++

Vedere [Eseguire automaticamente una macro all\'avvio](Macro_at_Startup/it.md) su come impostare una macro da eseguire automaticamente all\'avvio di FreeCAD.



## Variabili d\'ambiente 

FreeCAD supporta le seguenti variabili di ambiente, che possono essere utilizzate per configurare le directory: {{Version/it|0.19}}

++++
| Variabile d\'ambiente        | Corrispondente [nome della variabile di configurazione](#Set_di_configurazione.md) | Sinossi                                                                                                                                                             |
+==============================+============================================================================================+=====================================================================================================================================================================+
|               | UserHomePath                                                                               | Directory \"base\" di FreeCAD per la conservazione dei dati utente locali.                                                                                          |
| `FREECAD_USER_HOME` |                                                                                            |                                                                                                                                                                     |
|                           |                                                                                            |                                                                                                                                                                     |
++++
|               | UserAppData                                                                                | Se non è impostato, il valore predefinito è `FREECAD_USER_HOME/.FreeCAD`, ma solo se è impostato `FREECAD_USER_HOME`. |
| `FREECAD_USER_DATA` |                                                                                            |                                                                                                                                                                     |
|                           |                                                                                            |                                                                                                                                                                     |
++++
|               | AppTempPath                                                                                | Se non è impostato, il valore predefinito è `FREECAD_USER_HOME/temp`, ma solo se è impostato `FREECAD_USER_HOME`.     |
| `FREECAD_USER_TEMP` |                                                                                            |                                                                                                                                                                     |
|                           |                                                                                            |                                                                                                                                                                     |
++++

Se il percorso specificato non esiste, l\'impostazione viene ignorata!

Le suddette variabili d\'ambiente sono pensate per essere usate per realizzare un ambiente FreeCAD *portatile*. Per un esempio su come utilizzare le variabili di ambiente dalla riga di comando su Linux, fare riferimento a [note per gli utenti Linux sulla pagina dei download](Download/it#Note_per_gli_utenti_GNU/Linux.md).

### `HOME`

FreeCAD utilizza [Qt](Third_Party_Libraries/it#Qt.md), che rispetta la variabile ambientale `HOME`. Pertanto, l\'impostazione `HOME` può essere utilizzata per specificare la directory di base dei file di configurazione relativi a Qt (`.config/FreeCAD/FreeCAD.conf`).

FreeCad stesso non rispetta la variabile ambientale `HOME` (perché determina la home directory dell\'utente da un\'API di sistema di livello inferiore). Usa `FREECAD_USER_HOME` per questo scopo.

### `TMPDIR` 

La directory temporanea predefinita è **/tmp/**. La variabile d\'ambiente `TMPDIR` può essere utilizzata per sovrascrivere l\'impostazione predefinita. (*Editor: precedence?*).



### Librerie

Alcune librerie hanno bisogno di chiamare le variabili di ambiente del sistema. A volte, quando c\'è un problema con un\'installazione FreeCAD, è perché qualche variabile d\'ambiente è assente o è errata. Pertanto, alcune variabili importanti vengono duplicate in Config e salvate nel file di registro

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



## Set di configurazione 

Ad ogni avvio FreeCAD esamina i suoi ambienti ed i parametri della riga di comando. Si costruisce un **set di configurazione** che contiene l\'essenza delle informazioni per l\'esecuzione. Queste informazioni vengono poi utilizzate per determinare il luogo dove salvare i dati dell\'utente o file di log (registro). E\' anche molto importante per le analisi post-mortem. Pertanto viene salvato nel file di registro.



### Informazioni relative all\'utente 

+++++
| Nome var config | Descrizione                                                                    | Esempio Windows                                                            | Esempio Linux                                                                                                                         |
+=================+================================================================================+============================================================================+=======================================================================================================================================+
| UserAppData     | Percorso dove FreeCAD archivia i dati dell\'applicazione relativi all\'utente. |                                                             |                                                                                                                        |
|                 |                                                                                | **C:\Documents and Settings\username\AppData\FreeCAD**            | **/home/username/.config/.FreeCAD**                                                                                          |
|                 |                                                                                |                                                                         |                                                                                                                                    |
|                 |                                                                                |                                                                  |                                                                                                                             |
|                 |                                                                                | <hr />                                                                     | <hr />                                                                                                                                |
|                 |                                                                                |                                                                         |                                                                                                                                    |
|                 |                                                                                | *Percorso breve :***%APPDATA%\FreeCAD**             | *Percorso breve :***~/.FreeCAD**                                                                               |
+++++
| UserParameter   | File in cui FreeCAD archivia i dati dell\'applicazione relativi all\'utente.   |                                                             |                                                                                                                        |
|                 |                                                                                | **C:\Documents and Settings\username\AppData\FreeCAD\user.cfg**   | **/home/username/.FreeCAD/user.cfg**                                                                                         |
|                 |                                                                                |                                                                         |                                                                                                                                    |
|                 |                                                                                |                                                                  |                                                                                                                             |
|                 |                                                                                | <hr />                                                                     | <hr />                                                                                                                                |
|                 |                                                                                |                                                                         |                                                                                                                                    |
|                 |                                                                                | *Percorso breve :***%APPDATA%\FreeCAD\user.cfg**    | *Percorso breve :***~/.config/FreeCAD/user.cfg** or **$HOME/.config/.FreeCAD/user.cfg** |
+++++
| SystemParameter | File in cui FreeCAD archivia i dati relativi all\'applicazione.                |                                                             |                                                                                                                        |
|                 |                                                                                | **C:\Documents and Settings\username\AppData\FreeCAD\system.cfg** | **/home/username/.config/.FreeCAD/system.cfg**                                                                               |
|                 |                                                                                |                                                                         |                                                                                                                                    |
|                 |                                                                                |                                                                  |                                                                                                                             |
|                 |                                                                                | <hr />                                                                     | <hr />                                                                                                                                |
|                 |                                                                                |                                                                         |                                                                                                                                    |
|                 |                                                                                | *Percorso breve :***%APPDATA%\FreeCAD\system.cfg**  | *Percorso breve :***~/.FreeCAD/system.cfg** or **$HOME/.FreeCAD/system.cfg**            |
+++++
| UserHomePath    | Percorso home dell\'utente corrente                                            |                                                             |                                                                                                                        |
|                 |                                                                                | **C:\Documents and Settings\username**                            | **/home/username**                                                                                                           |
|                 |                                                                                |                                                                         |                                                                                                                                    |
|                 |                                                                                |                                                                  |                                                                                                                             |
|                 |                                                                                | <hr />                                                                     | <hr />                                                                                                                                |
|                 |                                                                                |                                                                         |                                                                                                                                    |
|                 |                                                                                | *Percorso breve :***%USERPROFILE%**                 | *Percorso breve :***~**                                                                                        |
+++++

Nota: per le distribuzioni Linux, un file di configurazione aggiuntivo relativo a [Qt](Third_Party_Tools/it#Qt-Toolkit.md) può esistere nel percorso **/home/username/.config/FreeCAD/FreeCAD.conf**.



### Argomenti della riga di comando 

++++
| Nome var config       | Descrizione                                                                                                                                                                                                                                                                                                         | Esempio                                                                     |
+=======================+=====================================================================================================================================================================================================================================================================================================================+=============================================================================+
| LoggingFile           | 1 se il logging è attivato                                                                                                                                                                                                                                                                                          | 1                                                                           |
++++
| LoggingFileName       | Nome del file dove si trova il log                                                                                                                                                                                                                                                                                  |                                                              |
|                       |                                                                                                                                                                                                                                                                                                                     | **C:\Documents and Settings\username\AppData\FreeCAD\FreeCAD.log** |
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



### Relativi al sistema 

+++++
| Nome var config  | Descrizione                                                                                                                                                                                                                                                                                                                                                | Esempioo Windows                          | Esempio Linux                         |
+==================+============================================================================================================================================================================================================================================================================================================================================================+===========================================+=======================================+
| AppHomePath      | Percorso in cui è installato FreeCAD                                                                                                                                                                                                                                                                                                                       |                            |                        |
|                  |                                                                                                                                                                                                                                                                                                                                                            | **c:/Progam Files/FreeCAD_0.19** | **/user/local/FreeCAD_0.19** |
|                  |                                                                                                                                                                                                                                                                                                                                                            |                                        |                                    |
+++++
| PythonSearchPath | Contiene un elenco di percorsi dove python cerca i moduli. Questo vale all\'avvio e può cambiare durante l\'esecuzione                                                                                                                                                                                                                                     |                                           |                                       |
+++++
| AppTempPath      | Percorso della directory temporanea. Può essere fornito con la variabile d\'ambiente `TMPDIR` o con <img alt="" src=images/Std_DlgParameter.svg  style="width:16px;"> [Modifica parametri](Std_DlgParameter/it.md): **Strumenti → Modifica parametri... → BaseApp → Preferences → General → TempPath** |                                           |                        |
|                  |                                                                                                                                                                                                                                                                                                                                                            |                                           | **/tmp/**                    |
|                  |                                                                                                                                                                                                                                                                                                                                                            |                                           |                                    |
|                  |                                                                                                                                                                                                                                                                                                                                                            |                                           | (predefinito)                         |
+++++



### Informazioni relative alla costruzione 

La tabella seguente mostra le informazioni disponibili relative alla versione di Build. La maggior parte proviene dal repositorio di Subversion. Queste cose sono necessarie per ricostruire esattamente la versione!

  Nome var config      Descrizione                                                                                                      Esempio
    
  BuildVersionMajor    Numero di versione principale della costruzione. Definito in **src/Build/Version.h.in**   0
  BuildVersionMinor    Numero di versione secondario della costruzione. Definito in **src/Build/Version.h.in**   7
  BuildRevision        Numero di revisione del repositorio SVN del src nella costruzione. Generato da SVN                               356
  BuildRevisionRange   Gamma di diversi cambiamenti                                                                                     123-356
  BuildRepositoryURL   URL del repositorio                                                                                              <https://free-cad.svn.sourceforge.net/svnroot/free-cad/trunk/src>
  BuildRevisionDate    Data della revisione precedente                                                                                  2007/02/03 22:21:18
  BuildScrClean        Indica se il codice sorgente è stato modificato dopo il suo checkout                                             Src modified
  BuildScrMixed                                                                                                                         Src not mixed



### Relative al marchio 

Queste voci di configurazione sono legate al meccanismo di marchiatura di FreeCAD. Vedere [Marchiatura](Branding/it.md) per maggiori dettagli.

++++
| Nome var config  | Descrizione                                                                                                                                 | Esempio                  |
+==================+=============================================================================================================================================+==========================+
| ExeName          | Nome del file di costruzione eseguibile. Può differire da quello di FreeCAD se è utilizzato un diverso **main.cpp**. |           |
|                  |                                                                                                                                             | **FreeCAD.exe** |
|                  |                                                                                                                                             |                       |
++++
| ExeVersion       | Versione globale mostrata all\'inizio                                                                                                       | V0.19                    |
++++
| AppIcon          | Icona che viene utilizzata per l\'eseguibile, mostrata in Application MainWindow.                                                           | \"FCIcon\"               |
++++
| ConsoleBanner    | Banner che viene mostrato in modalità console                                                                                               |                          |
++++
| SplashPicture    | Nome dell\'icona utilizzata per la schermata iniziale                                                                                       | \"FreeCADSplasher\"      |
++++
| SplashAlignment  | Allineamento del testo nella finestra di dialogo iniziale                                                                                   | \"Bottom o Left\"        |
++++
| SplashTextColor  | Colore del testo iniziale                                                                                                                   | \"#000000\"              |
++++
| StartWorkbench   | Nome del Workbench che viene attivato automaticamente dopo l\'avvio                                                                         | \"Part design\"          |
++++
| HiddenDockWindow | Elenco dei dockwindows (separati da un punto e virgola) che saranno disabilitati                                                            | \"Property editor\"      |
++++



### Interrogazione della configurazione 

**Dalla console Python di FreeCAD**

Le voci del set di configurazione possono essere interrogate con il **config var name** (vedi tabelle sopra) dalla [console Python](Python_console/it.md). Per esempio:

  >>> FreeCAD.ConfigGet("ExeVersion")
  '0.19'

Se il nome non viene trovato, viene restituita una stringa vuota.

**Dalla riga di comando**

Utilizzare l\'opzione `--get-config <config-var-name>` per interrogare un singolo nome. Non tutti i nomi sono supportati. Per esempio:

Usa l\'opzione `--dump-config` per ottenere un elenco di nomi e dei loro valori. Non tutti i nomi sono supportati.

**Dalla console di FreeCAD**

Avvia FreeCAD in modalità console con `--console` ed esegui query con codice Python. Per esempio:

 $ FreeCAD --console
 [FreeCAD Console mode <Use Ctrl-D (i.e. EOF) to exit.>]
 >>> FreeCAD.ConfigGet("ExeVersion")
 '0.19'
 >>> exit()

Per Linux (shell bash) puoi modificare la seguente riga di comando in base alle tue esigenze:

 $ FreeCAD --console <<EOF
 print( "FREECAD_USER_HOME: " + ( "not set" if ( os.environ.get('FREECAD_USER_HOME') is None ) else os.environ.get('FREECAD_USER_HOME') ) )
 print( "UserHomePath: " + FreeCAD.ConfigGet("UserHomePath") )
 exit()
 EOF



## Avvio di FreeCAD dal desktop 



### Linux: creazione di un\'opzione di avvio aggiuntiva 

Quanto segue presuppone che il desktop sia configurato in modo tale da poter avviare FreeCAD dallo stesso. A seconda della distribuzione Linux e dell\'ambiente desktop, potrebbe essere necessario adattare i seguenti passaggi:

1.  Copiare il file di ingresso di freedesktop per FreeCAD da **/usr/share/applications/freecad.desktop** a **~/.local/share/applications**.
2.  Cambiare il nome da **freecad.desktop** in qualcos\'altro (ad es. **MyFreeCADConfig.desktop**).
3.  Aprire il file con un editor di testo e modificare il modo in cui viene invocato FreeCAD modificando la riga che inizia con `Exec`.
4.  Di conseguenza, è disponibile una voce aggiuntiva nel menu di avvio/avvio dell\'applicazione. In questo modo, puoi avere più voci di FreeCAD con varie opzioni di avvio.



## Avvio di FreeCAD da un supporto USB portatile 

**Windows**

Mettere l\'eseguibile di FreeCAD, **FreeCAD.exe**, sul supporto USB. Creare un file batch, **FreeCAD.bat**, e metterlo nella stessa directory di **FreeCAD.exe**. All\'interno del file batch scrivere:


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

Con il batch nella root del supporto USB:


```python
set CURRENTDIR=%cd%
set FREECAD_USER_DATA=%CURRENTDIR%FreeCAD\
start %cd%FreeCAD\bin\FreeCAD.exe -u %FREECAD_USER_DATA%user.cfg -s %FREECAD_USER_DATA%system.cfg
```

Ora fai doppio clic sul file batch per avviare FreeCAD. ([vedere](https://forum.freecadweb.org/viewtopic.php?f=4&t=49028))



---
⏵ [documentation index](../README.md) > [Developer Documentation](Category_Developer Documentation.md) > [Start](Start_Workbench.md) > Start up and Configuration/it
