# Start up and Configuration/de
**In FreeCAD Version 0.20 wurde der voreingestellte Speicherort der Konfigurations-, Daten- und Cache-Dateien des Programms für Linux geändert.<br>
Siehe [Versionshinweise 0.20](Release_notes_0.20/de#Kernsystem.md) für weitere Informationen. Diese Seite wurde noch nicht entsprechend aktualisiert.**






## Übersicht

Diese Seite zeigt die verschiedene Wege FreeCAD zu starten und die wichtigsten Konfigurationsmöglichkeiten.



## FreeCAD von der Kommandozeile starten 

FreeCAD kann ganz normal durch einen Doppelklick auf das Desktop-Symbol oder durch Auswahl aus dem Startmenü gestartet werden, aber es kann auch direkt über die Befehlszeile gestartet werden. Dies erlaubt dir einige der Standard-Startoptionen zu ändern.



### Nutzen von Kommandozeilen-Optionen ohne eine Kommandozeilen-Shell 

-   Unter Ubuntu kannst du ein Desktop-Symbol erstellen und dessen Eigenschaften bearbeiten. Füge die Kommandozeilenoptionen durch Leerzeichen getrennt hinter dem Programmnamen in das Feld \"Befehl\" ein.
-   Unter Windows erstelle einen Tastenkürzel und bearbeite die Eigenschaften. Füge die Befehlszeilenoptionen durch Leerzeichen getrennt in das Feld \"Ziel\" ein.



### Befehlszeilen-Optionen 

Die Befehlszeilen-Optionen unterliegen häufigen Änderungen. Daher ist es eine gute Idee, die aktuellen Optionen durch Eintippen zu überprüfen:

FreeCAD --help

Aus der Antwort können die möglichen Parameter abgelesen werden. Für FreeCAD-Version 1.0 sind es:

 Usage: FreeCAD [options] File1 File2 ...
 
 Allowed options:
 
 Generic options:
   -v [ --version ]          Prints version string
   --verbose                 Prints verbose version string
   -h [ --help ]             Prints help message
   -c [ --console ]          Starts in console mode
   --response-file arg       Can be specified with '@name', too
   --dump-config             Dumps configuration
   --get-config arg          Prints the value of the requested configuration key
   --set-config arg          Sets the value of a configuration key
   --keep-deprecated-paths   If set then config files are kept on the old 
                             location
 
 Configuration:
   -l [ --write-log ]        Writes FreeCAD.log to the user directory.
   --log-file arg            Unlike --write-log this allows logging to an 
                             arbitrary file
   -u [ --user-cfg ] arg     User config file to load/save user settings
   -s [ --system-cfg ] arg   System config file to load/save system settings
   -t [ --run-test ] arg     Run a given test case (use 0 (zero) to run all 
                             tests). If no argument is provided then return list
                             of all available tests.
   -r [ --run-open ] arg     Run a given test case (use 0 (zero) to run all 
                             tests). If no argument is provided then return list
                             of all available tests.  Keeps UI open after 
                             test(s) complete.
   -M [ --module-path ] arg  Additional module paths
   -P [ --python-path ] arg  Additional python paths
   --single-instance         Allow to run a single instance of the application
   --safe-mode               Force enable safe mode
   --pass arg                Ignores the following arguments and pass them 
                             through to be used by a script

In der nachfolgenden Tabelle werden ausgewählte Optionen ausführlicher beschrieben:

++++
| Lange Option                              | Entsprechende [config var name](#Konfiguration_Satz.md) | Zusammenfassung                                                                                                                                                                                                                                                                                                    |
+===========================================+=================================================================+====================================================================================================================================================================================================================================================================================================================+
|                            | UserParameter                                                   | Dateiname oder relativer Pfad, der mit einem Dateinamen endet. Standardmäßig wird `user.cfg`.                                                                                                                                                                                               |
| `--user-cfg <filename>`          |                                                                 |                                                                                                                                                                                                                                                                                                                    |
|                                        |                                                                 |                                                                                                                                                                                                                                                                                                                    |
++++
|                            | Vorangestellt dem AdditionalModulePaths                         | Verzeichnis, das Module enthält, vorangestellt. Diese Option kann wiederholt angegeben werden, um mehrere Verzeichnisse anzugeben.                                                                                                                                                                                 |
| `--module-path <dir>`            |                                                                 |                                                                                                                                                                                                                                                                                                                    |
|                                        |                                                                 |                                                                                                                                                                                                                                                                                                                    |
++++
|                            | most                                                            | Gibt den gewünschten Wert in einem Aufklapp Dialog aus. Wird nach Bestätigung mit **OK** beendet. Kann nicht wiederholt verwendet werden. Wenn ein unbekannter/unzulässiger Variablenname verwendet wird, ist die Antwort leer. Das `--console` Flag wird nicht beachtet. |
| `--get-config <config-var-name>` |                                                                 |                                                                                                                                                                                                                                                                                                                    |
|                                        |                                                                 |                                                                                                                                                                                                                                                                                                                    |
++++

Optionen können in zwei Formen geschrieben werden: `--long-option arg` und `--long-option<nowiki>=</nowiki>arg`.



### Antwort und Konfigurationsdateien 

FreeCAD kann einige dieser Optionen aus einer Konfigurationsdatei lesen. Diese Datei muss sich im bin Pfad befinden und den Namen **FreeCAD.cfg** tragen. Beachte, dass Optionen, die in der Kommandozeile angegeben werden, die Konfigurationsdatei aufheben!

Bei einigen Betriebssystemen ist die Anzahl der Zeichen in der Befehlszeile sehr gering. Der übliche Weg, diese Beschränkungen zu umgehen, ist die Verwendung von Antwortdateien. Eine Antwortdatei ist lediglich eine Konfigurationsdatei, die die gleiche Syntax wie die Befehlszeile verwendet. Wenn in der Befehlszeile eine Antwortdatei angegeben ist, wird sie zusätzlich zur Befehlszeile geladen und analysiert:

    FreeCAD @ResponseFile.txt 

oder:

    FreeCAD --response-file=ResponseFile.txt

oder:

    FreeCAD --response-file ResponseFile.txt



### Versteckte Optionen 

Es gibt eine Reihe von Optionen, die nicht für den Benutzer sichtbar sind. Diese Optionen sind z.B. die X-Window-Parameter, die durch das Windows-System analysiert werden:

-   \"-display\" - setzt das X-Display (Standardwert ist \$DISPLAY).
-   \"-geometry\" - setzt die Client-Geometrie des ersten angezeigten Fensters.
-   \"-fn\" oder \"-font\" - definiert die Anwendungsschriftart. Die Schriftart sollte durch eine X logische Schriftartbeschreibung angegeben werden.
-   \"-bg\" oder \"-background\" - setzt die Standardhintergrundfarbe und eine Anwendungspalette (helle und dunkle Farbschattierungen werden berechnet).
-   \"-fg\" oder \"foreground\" - setzt die Standardvordergrundfarbe.
-   \"-btn\" oder \"-button\" - setzt die Standard-Button-Farbe.
-   \"-name\" - setzt den Anwendungsnamen.
-   \"-title\" - setzt den Anwendungstitel.
-   \"-visual\" - zwingt die Anwendung, TrueColor anstatt einer 8-Bit-Farbanzeige zu nutzen.
-   \"-ncols\" - begrenzt die Anzahl der im Farbwürfel verwendeten Farben auf einer 8-Bit-Anzeige, wenn die Anwendung die QApplication::ManyColor-Angabe verwendet. Wenn die Anzahl 216 ist, dann wird ein 6x6x6-Farbwürfel (d.h. 6 Stufen für Rot, 6 Stufen für Grün und 6 Stufen für Blau); bei anderen Werten wird ein Quader annähernd zu einem 2x3x1-Quader verwendet.
-   \"-cmap\" - führt dazu, dass die Anwendung eine eigene Farbpalette für eine 8-Bit-Anzeige installiert.



### FreeCAD ohne grafische Benutzeroberfläche ausführen (kopflos) 

FreeCAD wird normalerweise mit zwei ausführbaren Dateien gebaut: eine GUI-fähige mit dem Namen **FreeCAD** oder **freecad**, und eine kopflose mit dem Namen **FreeCADCmd** oder **freecadcmd**. FreeCAD kann im Konsolenmodus mit dem Schalter `--console` verwendet werden (dies ist das Standardverhalten von **FreeCADCmd**):

FreeCAD --console

Im Konsolenmodus wird keine grafische Benutzeroberfläche angezeigt, sondern eine Eingabeaufforderung des Python Interpreters: `>>>`. Von dieser Eingabeaufforderung aus hast du die gleiche Funktionalität wie der Python Interpreter, der innerhalb der FreeCAD GUI läuft, und Zugriff auf alle Module und Plugins von FreeCAD, ausser dem FreeCADGui Modul. Sei dir bewusst, dass Module, die von FreeCADGui abhängen, ebenfalls nicht verfügbar sein könnten.

Um mehr über den Konsolen- oder Headlessmodus zu erfahren, schaue dir [Headless FreeCAD](Headless_FreeCAD.md) an.



### Ausführen von Modulen, Makros und Skripten 

++++
| Dateityp        | System           | Befehlszeilen Beispiel                                                                                                             |
+=================+==================+====================================================================================================================================+
| Modul           | Windows          |                                                                                                                     |
|                 |                  | `"C:\Program Files\FreeCAD\bin\FreeCAD.exe" -M "C:\FreeCAD\Mod\Draft"`                                                    |
|                 |                  |                                                                                                                                 |
++++
|                 | Linux            |                                                                                                                     |
|                 |                  | `FreeCAD_0.19 -M ~/.FreeCAD/Mod/Draft`                                                                                    |
|                 |                  |                                                                                                                                 |
++++
|                 | Linux (AppImage) |                                                                                                                     |
|                 |                  | `path/to/FreeCADXXX.AppImage -M ~/.FreeCAD/Mod/Draft`                                                                     |
|                 |                  |                                                                                                                                 |
++++
|                 |                  |                                                                                                                                    |
++++
| .FCMacro or .py | Windows          |                                                                                                                     |
|                 |                  | `"C:\Program Files\FreeCAD\bin\FreeCAD.exe" "C:\Users\userName\AppData\Roaming\FreeCAD\Mod\WorkFeature\start_WF.FCMacro"` |
|                 |                  |                                                                                                                                 |
++++
|                 | Linux            |                                                                                                                     |
|                 |                  | `FreeCAD_0.19 ~/.FreeCAD/Mod/WorkFeature/start_WF.FCMacro`                                                                |
|                 |                  |                                                                                                                                 |
++++
|                 | Linux (AppImage) |                                                                                                                     |
|                 |                  | `path/to/FreeCADXXX.AppImage ~/.FreeCAD/Mod/WorkFeature/start_WF.FCMacro`                                                 |
|                 |                  |                                                                                                                                 |
++++

Siehe [Makro beim Start](Macro_at_Startup/de.md), wie man ein Makro einrichtet, das automatisch beim Start von FreeCAD ausgeführt wird.



## Umgebungsvariablen

FreeCAD unterstützt die folgenden Umgebungsvariablen, die zum Konfigurieren von Verzeichnissen genutzt werden können: <small>(v0.19)</small> 

++++
| Umgebungsvariable            | Entsprechende [config var name](#Configuration_set.md) | Zusammenfassung                                                                                                                                                         |
+==============================+================================================================+=========================================================================================================================================================================+
|               | UserHomePath                                                   | FreeCADs \"Basis\"-Verzeichnis für die Ablage von lokalen Benutzerdaten.                                                                                                |
| `FREECAD_USER_HOME` |                                                                |                                                                                                                                                                         |
|                           |                                                                |                                                                                                                                                                         |
++++
|               | UserAppData                                                    | Falls nicht gesetzt, ist die Voreinstellung `FREECAD_USER_HOME/.FreeCAD`, aber nur, wenn `FREECAD_USER_HOME` gesetzt ist. |
| `FREECAD_USER_DATA` |                                                                |                                                                                                                                                                         |
|                           |                                                                |                                                                                                                                                                         |
++++
|               | AppTempPath                                                    | Falls nicht gesetzt, ist die Voreinstellung `FREECAD_USER_HOME/temp`, aber nur, wenn `FREECAD_USER_HOME` gesetzt ist.     |
| `FREECAD_USER_TEMP` |                                                                |                                                                                                                                                                         |
|                           |                                                                |                                                                                                                                                                         |
++++

Falls der angegebene Pfad nicht existiert, wird die Einstellung ignoriert!

Die oben angegebenen Umgebungsvariablen sind für eine \"portable\" FreeCAD-Umgebung gedacht. Für ein Beispiel, wie Umgebungsvariablen auf der Linux-Kommandozeile benutzt werden können, siehe [Hinweise für GNU/Linux Anwender](Download#Notes_for_GNU.2FLinux_users/de.md) auf der [Herunterladen](Download/de.md)-Seite.

### `HOME`

FreeCAD benutzt [Qt](Third_Party_Libraries#Qt.md), das die Umgebungsvariable `HOME` berücksichtigt. Dadurch kann `HOME` verwendet werden, um das Basisverzeichnis von Qt-verwandten Konfigurationsdateien (`.config/FreeCAD/FreeCAD.conf`) anzugeben.

FreeCad selbst berücksichtigt die Umgebungsvariable `HOME` nicht (weil es das Benutzerverzeichnis über eine untergeordnete System-API ermittelt). Benutze `FREECAD_USER_HOME` für diesen Zweck.

### `TMPDIR` 

Das Standard-tmp-Verzeichnis ist **/tmp/**. Die Umgebungsvariable `TMPDIR` kann benutzt werden, um die Standardvorgabe zu überschreiben. (*Editor: Rangfolge?*).



### Bibliotheken

Einige Bibliotheken müssen Systemumgebungsvariablen aufrufen. Manchmal, wenn es ein Problem mit einer FreeCAD Installation gibt, liegt es daran, dass eine Umgebungsvariable fehlt oder nicht korrekt ist. Daher werden einige wichtige Variablen in der Konfig dupliziert und in der Log Datei gespeichert.

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



## Konfigurationssatz

Bei jedem Start prüft FreeCAD seine Umgebung und die Kommandozeilenparameter. Es baut einen **Konfigurationssatz** auf, der das Wesentliche der Laufzeitinformationen enthält. Diese Informationen werden später verwendet, um den Ort zu bestimmen, an dem Benutzerdaten oder Protokolldateien gespeichert werden sollen. Sie sind auch für Postmortem-Analysen sehr wichtig. Deshalb wird sie in der Protokolldatei gespeichert.



### Benutzerbezogene Informationen 

+++++
| Konfig.-Variable | Beschreibung                                                 | Beispiel Windows                                                           | Beispiel Linux                                                                                                                     |
+==================+==============================================================+============================================================================+====================================================================================================================================+
| UserAppData      | Pfad, wo FreeCAD benutzerbezogene Anwendungsdaten speichert. |                                                             |                                                                                                                     |
|                  |                                                              | **C:\Documents and Settings\username\AppData\FreeCAD**            | **/home/username/.FreeCAD**                                                                                               |
|                  |                                                              |                                                                         |                                                                                                                                 |
|                  |                                                              |                                                                  |                                                                                                                          |
|                  |                                                              | <hr />                                                                     | <hr />                                                                                                                             |
|                  |                                                              |                                                                         |                                                                                                                                 |
|                  |                                                              | *Short path :***%APPDATA%\FreeCAD**                 | *Short path :***~/.FreeCAD**                                                                                |
+++++
| UserParameter    | Datei, wo FreeCAD benutzerbezogene Anwendungsdaten speichert |                                                             |                                                                                                                     |
|                  |                                                              | **C:\Documents and Settings\username\AppData\FreeCAD\user.cfg**   | **/home/username/.config/FreeCAD/user.cfg**                                                                               |
|                  |                                                              |                                                                         |                                                                                                                                 |
|                  |                                                              |                                                                  |                                                                                                                          |
|                  |                                                              | <hr />                                                                     | <hr />                                                                                                                             |
|                  |                                                              |                                                                         |                                                                                                                                 |
|                  |                                                              | *Short path :***%APPDATA%\FreeCAD\user.cfg**        | *Short path :***~/.config/FreeCAD/user.cfg** oder **$HOME/.config/FreeCAD/user.cfg** |
+++++
| SystemParameter  | Datei, wo FreeCAD anwendungsbezogene Daten speichert         |                                                             |                                                                                                                     |
|                  |                                                              | **C:\Documents and Settings\username\AppData\FreeCAD\system.cfg** | **/home/username/.config/FreeCAD/system.cfg**                                                                             |
|                  |                                                              |                                                                         |                                                                                                                                 |
|                  |                                                              |                                                                  |                                                                                                                          |
|                  |                                                              | <hr />                                                                     | <hr />                                                                                                                             |
|                  |                                                              |                                                                         |                                                                                                                                 |
|                  |                                                              | *Short path :***%APPDATA%\FreeCAD\system.cfg**      | *Short path :***~/.FreeCAD/system.cfg** oder **$HOME/.FreeCAD/system.cfg**           |
+++++
| UserHomePath     | Home-Verzeichnis des aktuellen Benutzers                     |                                                             |                                                                                                                     |
|                  |                                                              | **C:\Documents and Settings\username**                            | **/home/username**                                                                                                        |
|                  |                                                              |                                                                         |                                                                                                                                 |
|                  |                                                              |                                                                  |                                                                                                                          |
|                  |                                                              | <hr />                                                                     | <hr />                                                                                                                             |
|                  |                                                              |                                                                         |                                                                                                                                 |
|                  |                                                              | *Short path :***%USERPROFILE%**                     | *Short path :***~**                                                                                         |
+++++

Hinweis: Bei Linux-Distributionen kann es eine weitere Konfigurationsdatei geben, die in Verbindung mit [Qt](Third_Party_Tools#Qt-Toolkit.md) steht und unter **/home/username/.config/FreeCAD/FreeCAD.conf** zu finden ist.



### Befehlszeilenargumente

++++
| Konfig.-Variable      | Beschreibung                                                                                                                                                                                                                                                                                                                              | Beispiel                                                                    |
+=======================+===========================================================================================================================================================================================================================================================================================================================================+=============================================================================+
| LoggingFile           | 1, wenn das Logging eingeschaltet ist                                                                                                                                                                                                                                                                                                     | 1                                                                           |
++++
| LoggingFileName       | Dateiname, wo die Log-Datei abgelegt wird                                                                                                                                                                                                                                                                                                 |                                                              |
|                       |                                                                                                                                                                                                                                                                                                                                           | **C:\Documents and Settings\username\AppData\FreeCAD\FreeCAD.log** |
|                       |                                                                                                                                                                                                                                                                                                                                           |                                                                          |
++++
| RunMode               | Dies beschreibt, wie die Hauptschleife ausgeführt wird. **\"Script\"** bedeutet, dass das Skript aufgerufen und dann beendet wird. **\"Cmd\"** startet den Kommandozeilen-Interpreter. **\"Internal\"** startet ein internes Skript. **\"Gui\"** Eintritt in die GUI-Ereignis-Schleife. **\"Module\"** lädt ein angegebenes Python-Modul. | \"Cmd\"                                                                     |
++++
| FileName              | Bedeutung abhängig von RunMode                                                                                                                                                                                                                                                                                                            |                                                                             |
++++
| ScriptFileName        | Bedeutung abhängig von RunMode                                                                                                                                                                                                                                                                                                            |                                                                             |
++++
| Verbose               | Ausführlichkeits-Level von FreeCAD                                                                                                                                                                                                                                                                                                        | \"\" oder \"strict\"                                                        |
++++
| OpenFileCount         | Enthält die Anzahl von Dateien, die durch Kommandozeilenargumente geöffnet wurden                                                                                                                                                                                                                                                         | \"12\"                                                                      |
++++
| AdditionalModulePaths | Enthält die zusätzlichen Modul-Pfade, die auf der Kommandozeile angegeben wurden                                                                                                                                                                                                                                                          | \"extraModules/\"                                                           |
++++



### Systembezogen

+++++
| Konfig var name  | Zusammenfassung                                                                                                                                                                                                                                                                                                                                                    | Beispiel Windows                          | Beispiel Linux                        |
+==================+====================================================================================================================================================================================================================================================================================================================================================================+===========================================+=======================================+
| AppHomePath      | Pfad, in dem FreeCAD installiert ist                                                                                                                                                                                                                                                                                                                               |                            |                        |
|                  |                                                                                                                                                                                                                                                                                                                                                                    | **c:/Progam Files/FreeCAD_0.19** | **/user/local/FreeCAD_0.19** |
|                  |                                                                                                                                                                                                                                                                                                                                                                    |                                        |                                    |
+++++
| PythonSearchPath | Enthält eine Liste von Pfaden, die Python Suchmodule. Dies ist beim Start und kann sich während der Ausführung ändern                                                                                                                                                                                                                                              |                                           |                                       |
+++++
| AppTempPath      | Pfad des temporären Verzeichnisses. Kann mit der Umgebungsvariablen `TMPDIR` oder mit der Option <img alt="" src=images/Std_DlgParameter.svg  style="width:16px;"> [Parameter Editor](Std_DlgParameter/de.md): **Werkzeuge → Parameter bearbeiten... → BasisAnwendung → Einstellungen → Allgemein → TempPfad** |                                           |                        |
|                  |                                                                                                                                                                                                                                                                                                                                                                    |                                           | **/tmp/**                    |
|                  |                                                                                                                                                                                                                                                                                                                                                                    |                                           |                                    |
|                  |                                                                                                                                                                                                                                                                                                                                                                    |                                           | (default)                             |
+++++



### Baubezogene Informationen 

Die folgende Tabelle zeigt die verfügbaren Informationen über die Bau Version. Das meiste davon stammt aus dem Subversion Repositorium. Dieses Zeug wird benötigt, um eine Version genau nachzubauen!

  Konfig.-Variable     Beschreibung                                                                                                    Beispiel
    
  BuildVersionMajor    Major Versionsnummer der Programmpaketausgabe. Definiert in **src/Build/Version.h.in**   0
  BuildVersionMinor    Minor Versionsnummer der Programmpaketausgabe. Definiert in **src/Build/Version.h.in**   7
  BuildRevision        SVN Repository Revisionsnummer der Source der Programmpaketausgabe. Generiert durch SVN                         356
  BuildRevisionRange   Bereich von verschiedenen Änderungen                                                                            123-356
  BuildRepositoryURL   Repository-URL                                                                                                  <https://free-cad.svn.sourceforge.net/svnroot/free-cad/trunk/src>
  BuildRevisionDate    Datum der obigen Revision                                                                                       2007/02/03 22:21:18
  BuildScrClean        Zeigt an, ob die Source nach dem Checkout verändert wurde                                                       Src modified
  BuildScrMixed                                                                                                                        Src not mixed



### Markenbezogenes

Diese Konfig Einträge beziehen sich auf den Markenmechanismus von FreeCAD. Siehe [Markenbildung](Branding/de.md) für weitere Details.

++++
| Konfig.-Variable | Beschreibung                                                                                                                               | Beispiel                 |
+==================+============================================================================================================================================+==========================+
| ExeName          | Name der ausführbaren Programmpaket-Datei. Kann von FreeCAD abweichen, falls eine andere **main.cpp** benutzt wird. |           |
|                  |                                                                                                                                            | **FreeCAD.exe** |
|                  |                                                                                                                                            |                       |
++++
| ExeVersion       | Während des Programmstarts angezeigte Hauptversion                                                                                         | \"0.19\"                 |
++++
| AppIcon          | Icon, das für das ausführbare Programm benutzt wird, angezeigt im Anwendungshauptfenster.                                                  | \"FCIcon\"               |
++++
| ConsoleBanner    | Banner, das im Konsolenmodus gezeigt wird                                                                                                  |                          |
++++
| SplashPicture    | Name des Icon, das für den Splash Screen benutzt wird                                                                                      | \"FreeCADSplasher\"      |
++++
| SplashAlignment  | Ausrichtung des Textes im Splash-Dialog                                                                                                    | \"Bottom\" oder \"Left\" |
++++
| SplashTextColor  | Farbe des Splasher-Textes                                                                                                                  | \"#000000\"              |
++++
| StartWorkbench   | Name des Arbeitsbereichs, der automatisch nach dem Programmstart gestartet wird                                                            | \"Part design\"          |
++++
| HiddenDockWindow | Liste von Andockfenstern (getrennt durch Semikolon), die versteckt werden                                                                  | \"Property editor\"      |
++++



### Abfrage der Konfiguration 

**Aus der FreeCAD Python Konsole**

Einträge der Konfiguration können über die **config var name**-Bezeichnung (sh. obige Tabellen) aus der [Python-Konsole](Python_console/de.md) abgefragt werden. Beispiel:

 >>> FreeCAD.ConfigGet("ExeVersion")
 '0.19'

Wird der Name nicht gefunden, wird eine leere Zeichenkette zurückgeliefert.

**Von der Befehlszeile**

Benutze die `--get-config <config-var-name>`-Option, um einen einzelnen Namen abzufragen. Nicht alle Namen werden unterstützt. Beispiel:

 FreeCAD --get-config ExeVersion

Benutze die `--dump-config`-Option, um eine Liste von Namen und ihren Werten zu erhalten. Nicht alle Namen werden unterstützt.

**Aus der FreeCAD Konsole**

Starte FreeCAD im Konsolenmodus mit `--console` und verwende Python-Code zur Abfrage. Beispiel:

 $ FreeCAD --console
 [FreeCAD Console mode <Use Ctrl-D (i.e. EOF) to exit.>]
 >>> FreeCAD.ConfigGet("ExeVersion")
 '0.19'
 >>> exit()

Bei Linux (bash shell) kannst du die folgenden Befehlszeile an deine Bedürfnisse anpassen:

 $ FreeCAD --console <<EOF
 print( "FREECAD_USER_HOME: " + ( "not set" if ( os.environ.get('FREECAD_USER_HOME') is None ) else os.environ.get('FREECAD_USER_HOME') ) )
 print( "UserHomePath: " + FreeCAD.ConfigGet("UserHomePath") )
 exit()
 EOF



## FreeCAD vom Schreibtisch aus starten 



### Linux: Erstellen einer zusätzlichen Startoption 

Im folgenden wird angenommen, dass dein Desktop so konfiguriert ist, dass du von dort FreeCAD aufrufen kannst. Abhängig von deiner Linux-Distribution und deiner Desktop-Umgebung musst du ggf. die folgenden Schritte anpassen:

1.  Kopiere die freecad.desktop-Datei für FreeCAD von **/usr/share/applications/freecad.desktop** nach **~/.local/share/applications**.
2.  Ändere den Namen von **freecad.desktop** auf etwas anderes (z.B. **MyFreeCADConfig.desktop**).
3.  Öffne die Datei mit einem Texteditor und ändere, wie FreeCAD aufgerufen wird durch ändern der Zeile, die mit `Exec` beginnt.
4.  Als Ergebnis gibt es einen zusätzlichen Eintrag in deinem Startmenü/Programmstart. Auf diese Weise kannst du mehrere FreeCAD-Einträge mit unterschiedliche Startoptionen haben.



## FreeCAD von einem USB Wechseldatenträger starten 

**Windows**

Lege die ausführbare FreeCAD Datei, **FreeCAD.exe**, auf dem USB Medium ab. Erstelle eine Stapelverarbeitungsdatei, **FreeCAD.bat**, und lege sie in das gleiche Verzeichnis wie **FreeCAD.exe**. Schreibe in die Stapelverarbeitungsdatei:


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

Die Stapelverarbeitungs-Datei befindet sich im Stammverzeichnis des USB-Mediums:


```python
set CURRENTDIR=%cd%
set FREECAD_USER_DATA=%CURRENTDIR%FreeCAD\
start %cd%FreeCAD\bin\FreeCAD.exe -u %FREECAD_USER_DATA%user.cfg -s %FREECAD_USER_DATA%system.cfg
```

Doppelklicke nun auf die Stapelverarbeitungs-Datei, um FreeCAD zu starten. ([siehe](https://forum.freecadweb.org/viewtopic.php?f=4&t=49028))



---
⏵ [documentation index](../README.md) > [Developer Documentation](Category_Developer Documentation.md) > [Start](Start_Workbench.md) > Start up and Configuration/de
