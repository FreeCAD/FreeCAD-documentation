---
- GuiCommand:
   Name: Path PostProcess
   Name/de: Pfad PostProzess
   MenuLocation: Pfad - Post Prozess
   Workbenches: [Pfad](Path_Workbench/de.md)
   Shortcut: **P** **P**
   SeeAlso: 
---

# Path Post/de


</div>



## Beschreibung


<div class="mw-translate-fuzzy">

Der **<img src="images/Path_PostProcess.svg" width=16px> [Post Prozess](Path_Post/de.md)** Befehl exportiert den ausgewählten **<img src="images/Path_Job.svg" width=16px> [Pfad Auftrag](Path_Job/de.md)** zu einer G-Code Datei.


</div>


<div class="mw-translate-fuzzy">

**Jede CNC Steuerung spricht einen spezifischen G-Code Dialekt, was einen Dialekt-korrekten Postprozessor erfordert, um die endgültige Ausgabe aus dem unabhängigen internen FreeCAD G-Code Dialekt zu übersetzen.**


</div>

### Typical functions of the Postprocessor include 


<div class="mw-translate-fuzzy">

### Typische Funktionen des Postprozessors schließen ein 

-   Verwenden einer korrekten G-Code Dateierweiterung für die Auftragsausgabe.
-   Auswahl der G-Code Befehle. CNC Steuerungen unterstützen typischerweise eine Teilmenge der verfügbaren G-Code Befehle. Die Obermenge der G-Code Befehle enthält leistungsfähige und spezialisierte Befehle, die sonst mit mehreren einfacheren Befehlen verarbeitet werden müssen. Postprozessoren werden geschrieben, um den besten G-Code für eine Operation auszuwählen, der auf dem Ziel verfügbar ist.
-   Formatierung der G-Code Syntax durch Umordnung der Eingänge Vorschub, X, Y, Z, A und B sowie der Präzision.
-   Einfügen einer Präambel zum Einstellen von Einheiten, Einheitenformat, Arbeitsebene, Koordinatensystem usw.
-   Einfügen einer Post-Ambel, um die Maschine zu parken, zu stoppen, alle Argumente zu verarbeiten.
-   Einfügen von Werkzeugwechseln oder Unterdrücken von Werkzeugwechseln zwischen aufeinanderfolgenden Operationen mit demselben Werkzeug.
-   Formatierung der Vorschub- und Geschwindigkeitsinformationen in Umdrehungen pro Minute oder pro Sekunde.
-   Formatierung der Funktionsaufrufe Benennung und Aufruf.


</div>

### Postprocessor Customization 


<div class="mw-translate-fuzzy">

### Postprozessor Anpassung 

Wenn du einen eigenen Postprozessor schreiben willst, wirf einen Blick auf die [Pfad Postprozessor Anpassung](Path_Postprocessor_Customization/de.md) Seite.


</div>

**Hinweis:** Mehrere mitgelieferte Postprozessoren erzeugen für viele CNC Steuerungen passenden Code oder können als Vorlage für Modifikationen verwendet werden


<div class="mw-translate-fuzzy">

Postprozessoren enthalten Konfigurationsflags und sind so konzipiert, dass sie durch Hinzufügen von G-Codes und M-Codes zu den bereitgestellten Definitionen feinabgestimmt werden können für:

-   Maschineninitialisierung
-   Auftagsabschluss
-   Werkzeug-Änderungen
-   Kühlung ein/aus
-   Usw\...


</div>


<div class="mw-translate-fuzzy">

Postprozessoren verwenden [FreeCADs internen G-Code Dialekt](Path_scripting/de#Das_FreeCAD_interne_GCode_Format.md) in Verbindung mit den Postprozessor Konfigurationsdefinitionen, um dialektkorrekten G-Code für Zielmaschinen zu erzeugen. Dadurch kann der Pfad Arbeitsbereich durch den Aufruf verschiedener Postprozessoren korrekten G-Code für verschiedene CNC Maschinensteuerungen erzeugen.


</div>

Die Typen der CNC Maschinensteuerungen umfassen:

-   CNC Fräsen
-   CNC Drehmaschinen
-   3D Drucker
-   Schleppmesserschneider
-   Laserschneider
-   Gravierer
-   Plasma-Brenner-Schneider
-   Drahtbieger
-   EDM Schneider
-   Usw\...


<div class="mw-translate-fuzzy">

Wenn nur eine CNC Maschine verwendet wird, oder wenn alle CNC Maschinen einen gemeinsamen Postprozessor verwenden, muss der Pfad Arbeitsbereich nur einen einzigen Postprozessor enthalten. Wenn ein einziger Postprozessor nicht ausreicht, um G-Code für alle Ziel CNC Steuerungen auszugeben, dann müssen mehrere Postprozessoren installiert werden.


</div>



## Anwendung


<div class="mw-translate-fuzzy">

1.  Wähle den **<img src="images/Path_Job.svg" width=16px> [Pfaf Auftrag](Path_Job/de.md)**, den du exportieren möchtest
    -   Rufe den Befehl mit mehreren Methoden auf:
    -   Durch Drücken der Schaltfläche **<img src="images/Path_Post.svg" width=24px>** in der Werkzeugleiste.
    -   Verwendung des Tastaturkürzels **P** und dann **P**.
    -   Unter Verwendung des **Pfad** → **<img src="images/Path_Post.svg" width=24px> [Postprozess](Path_Post/de.md)** aus dem oberen Menü.
2.  Bestätige den Namen und das Verzeichnis der **Ausgabedatei**.


</div>



## Optionen

Die Eigenschaften der Ausgabedatei und des Postprozessors können jederzeit vor dem Aufruf des Postprozessors im [Auftrag](Path_Job/de.md) eingestellt werden.

Die bereitgestellten Postprozessoren sind mit Kommentaren versehen, die Bereiche mit Flags, Konfigurationsvariablen und Abschnitten von G-Codes und M-Codes angeben, die vom Postprozessor zur Konfiguration der Ausgabe verwendet werden sollen.


<div class="mw-translate-fuzzy">

Zu den typischen True/False Merkern der Konfiguration gehören:

-   OUTPUT_COMMENTS (True = Zulassen, False = Unterdrücken), wird verwendet, um Textkommentare in die G-Code Ausgabedatei einzufügen.
-   OUTPUT_HEADER (True = Zulassen, False = Unterdrücken), Dient zum Einfügen von Textkopfzeilen in die G-Code Ausgabedatei.
-   OUTPUT_LINE_NUMBERS (True = Zulassen, False = Unterdrücken), Dient zum Einfügen von Zeilennummern in die G-Code Ausgabedatei.
-   SHOW_EDITOR (True = Zulassen, False = Unterdrücken), Dient zur Anzeige des ausgegebenen G-Codes in einem Aufklappfenster beim Aufruf des Postprozessors.
-   MODAL (True = Allow, False = Suppress), Reduziert die Anzahl der ausgegebenen G-Code Zeilen, indem die Modusinformationen entfernt werden, wenn sich der Modus nicht ändert.


</div>


<div class="mw-translate-fuzzy">

Typische Konfigurationsvariablen schließen ein:

-   LINENR (Zeilennummer), wird verwendet, um den Zeilennummernindex einzustellen.
-   UNITS (G20 oder G21), wird verwendet, um der Ziel CNC Steuerung ausdrücklich mitzuteilen, welche Einheiten zur Interpretation der endgültigen Ausgabedatei verwendet werden sollen.
-   MACHINE_NAME (Name der Ziel CNC Fräse), wird verwendet, um eine Maschinennamen Kennzeichnung in die endgültige Ausgabedatei einzufügen.
-   PRECISION, wird verwendet, um die Anzahl der Ziffern nach der Dezimalstelle in der endgültigen Ausgabedatei festzulegen.


</div>


<div class="mw-translate-fuzzy">

Typische Konfigurationsabschnitte sind:

-   PREAMBLE (Code Konfiguration, die zu Beginn des Auftrags eingefügt wird)
-   POSTAMBLE (Code Konfiguration, die an den Auftrag angehängt wird und das Parken der Maschine vorsieht, usw\...)
-   TOOL_CHANGE (Code, der bei jedem Werkzeugwechsel im Auftrag eingefügt wird)


</div>


<div class="mw-translate-fuzzy">

Der **Bearbeiten** → **Einstellungen...** → **Pfad** → **Auftragseinstellungen Reiter** → **Standardeinstellungen** → **Pfad** wird verwendet, um den bei der Auftragserstellung ausgewählten Standard Postprozessor festzulegen. Dies erlaubt Pfad Arbeitsbereich so konfiguriert zu werden, dass nur die gewünschten Postprozessoren angezeigt werden und ein Standard festgelegt wird.


</div>


<div class="mw-translate-fuzzy">

Enthaltene Postprozessoren werden standardmäßig in der **FreeCAD.Mod.Path.Pathscripts.Post** gespeichert:

-   centroid
-   comparams
-   dynapath
-   grbl, einschließlich Unterstützung für bCNC Kopfzeilenblöcke die das Auftrag Ausgabe Argument \--bcnc verwenden
-   [linuxcnc](http://linuxcnc.org/docs/html/gcode/g-code.html#gcode:g17-g19.1)
-   opensbp
-   phillips
-   rml
-   smoothie


</div>

## Limitations


<div class="mw-translate-fuzzy">

## Begrenzungen

-   Verwende **nicht** das **Datei** → **Export** Menü für den Export in G-Code, es wird beschädigten G-Code erzeugen!


</div>


<div class="mw-translate-fuzzy">





</div>


{{Path_Tools_navi

}}



---
⏵ [documentation index](../README.md) > [Path](Path_Workbench.md) > Path Post/de
