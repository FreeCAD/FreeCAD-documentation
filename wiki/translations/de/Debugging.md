# Debugging/de
{{TOCright}}

## Erster Test 

Bevor du den Schmerz der Fehlerdiagnose durchmachst, benutze das [Test Framework](Testing/de.md), um zu überprüfen, ob die Standardtests ordnungsgemäß funktionieren. Wenn sie nicht vollständig ausgeführt werden, liegt möglicherweise eine defekte Installation vor.

## Befehlszeile

Die *Fehlerdiagnose* von FreeCAD wird durch einige interne Mechanismen unterstützt. Die Kommandozeilenversion von FreeCAD bietet einige Optionen für die Fehlerdiagnoseunterstützung.

Dies sind die derzeit anerkannten Optionen in FreeCAD 0.19:

Grundlegende Optionen:

 -v [ --version ]      Druckt Versionszeichenkette
 -h [ --help ]         Druckt Hilfsmeldung aus
 -c [ --console ]      Startet im Konsolenmodus
 --response-file arg   Kann auch mit'@name' angegeben werden
 --dump-config         Dump der Konfiguration
 --get-config arg      Gibt den Wert des angegebenen Konfigurationsschlüssels aus

Konfiguration:

 -l [ --write-log ]       Schreibt eine Log-Datei nach:
                          $HOME/.FreeCAD/FreeCAD.log
                          $HOME/Library/Preferences/FreeCAD/FreeCAD.log (macOS)
                          %APPDATA%\FreeCAD\FreeCAD.log (Windows)
 --log-file arg           Anders als bei --write-log wird hier in eine Datei mit beliebigem Namen geschrieben
 -u [ --user-cfg ] arg    Benutzerkonfigurationsdatei, um Benutzereinstellungen zu laden/speichern
 -s [ --system-cfg ] arg  Systemkonfigurationsdatei, um Systemeinstellungen zu laden/speichern
 -t [ --run-test ] arg    Test-Level - oder 0 für alles
 -M [ --module-path ] arg Zusätzliche Modulpfade
 -P [ --python-path ] arg Zusätzliche Python-Pfade
 --single-instance        Startet eine (einzige) Instanz der Applikation zu starten

## Erzeugen einer Rückverfolgung 

Wenn Du eine FreeCAD Version der Anfangsphase der Entwicklungskurve verwendest, kann sie \"abstürzen\". Du kannst dabei helfen, diese Probleme zu lösen, indem Du einen \"Rückverfolgung\" an die Entwickler schickst. Um dies zu tun, musst Du ein \"Fehlerdiagnose build\" der Software haben. \"Fehlerdiagnose build\" ist ein Parameter, der zur Kompilierungszeit gesetzt wird, also musst Du entweder FreeCAD selbst kompilieren oder Dir eine vorkompilierte \"Fehlerdiagnose\" Version besorgen.

### Für Linux 


<div class="toccolours mw-collapsible mw-collapsed" style="width:800px;">

Linux Fehlerdiagnose →


<div class="mw-collapsible-content">

Voraussetzungen:

-   Softwarepaket gdb installiert
-   ein Fehlersuch-Build von FreeCAD (zur Zeit nur verfügbar unter [Für einen Fehlersuch Bau](Compile_on_Linux#For_a_Debug_build/de.md))
-   ein FreeCAD-Modell, das einen Absturz verursacht

Schritte: Gib in deinem Terminalfenster folgendes ein:

Finde das FreeCAD-Programm auf deinem System:


```python
$ whereis freecad
freecad: /usr/local/freecad <--- for example

$ cd /usr/local/freecad/bin
$ gdb FreeCAD
```

GNUdebugger gibt einige Initialisierungsinformationen aus. Die (gdb) zeigt, dass der GNUDebugger im Terminal läuft, das nun eingegeben wird:


```python
(gdb) handle SIG33 noprint nostop
(gdb) run
```

FreeCAD wird nun gestartet. Führe die Schritte aus, die dazu führen, dass FreeCAD abstürzt oder einfriert, und gib dann in das Terminalfenster ein:


```python
(gdb) bt
```

Dies führt zu einer langen Auflistung dessen, was das Programm beim Absturz oder Einfrieren genau getan hat. Füge dies deinem Problembericht bei.


```python
(gdb) bt full
```

Drucke auch die Werte der lokalen Variablen. Dies kann mit einer Zahl kombiniert werden, um die Anzahl der angezeigten Rahmen zu begrenzen.


</div>


</div>

### Für macOS 


<div class="toccolours mw-collapsible mw-collapsed" style="width:800px;">

macOS Debugging →


<div class="mw-collapsible-content">

Voraussetzungen:

-   Softwarepaket lldb installiert
-   ein Fehlerdiagnose build von FreeCAD
-   ein FreeCAD Modell, dass den Absturz verursacht

Schritte: Gib das Folgende in Dein Terminalfenster ein:


```python
$ cd FreeCAD/bin
$ lldb FreeCAD
```

LLDB gibt einige Initialisierungsinformationen aus. Die (lldb) zeigt an, dass das Fehlerdiagnoseprogramm im Terminal läuft, jetzt eingegeben:


```python
(lldb) run
```

FreeCAD wird nun gestartet. Führe die Schritte aus, die dazu führen, dass FreeCAD abstürzt oder einfriert, und gib dann in das Terminalfenster ein:


```python
(lldb) bt
```

Dies führt zu einer längeren Auflistung dessen, was das Programm genau getan hat, als es abgestürzt ist oder eingefroren ist. Füge dies deinem Problembericht bei.


</div>


</div>

## Von FreeCAD geladene Bibliotheken auflisten 

(Anwendbar auf Linux und macOS)

Manchmal ist es hilfreich zu verstehen, welche Bibliotheken FreeCAD lädt, insbesondere wenn mehrere Bibliotheken mit demselben Namen, aber unterschiedlichen Versionen geladen werden (Versionskollision). Um zu sehen, welche Bibliotheken von FreeCAD geladen werden, wenn es abstürzt, solltest du ein Terminal öffnen und es im Debugger ausführen. In einem zweiten Terminalfenster findest du die Prozess ID von FreeCAD heraus:


`ps -A &#124; grep FreeCAD`

Verwende die zurückgegebene ID und übergib sie an `lsof`:


` lsof -p process_id`

Dadurch wird eine lange Liste der geladenen Ressourcen gedruckt. Wenn z.B. herausgefunden werden soll, ob mehr als eine Coin3d Bibliotheksversion geladen ist, blättere durch die Liste oder suche direkt nach Coin in der Ausgabe:


`lsof -p process_id &#124; grep Coin`

## Python Fehlerdiagnose 

Für einen moderneren Ansatz zur Fehlerdiagnose bei Python siehe diese Beiträge:

-   [Fehlerdiagnosemakros mit VS 2017](https://forum.freecadweb.org/viewtopic.php?f=22&t=28901)
-   [Python Arbeitsbereiche Fehlersuche](https://forum.freecadweb.org/viewtopic.php?f=10&t=35383)
-   [python3.dll, Qt5Windgets.dll, Qt5Gui.dll und Qt5Core.dll nicht gefunden](https://forum.freecadweb.org/viewtopic.php?f=4&t=40251)

### winpdb


<div class="toccolours mw-collapsible mw-collapsed" style="width:800px;">

winpdb Fehlerdiagnose →


<div class="mw-collapsible-content">

Hier ist ein Beispiel für die Verwendung von *Winpdb* in FreeCAD:

Wir benötigen das Python-Fehlerdiagnoseprogramm *Winpdb*. Wenn es nicht installiert ist, lässt sich das auf Ubuntu/Debian wie folgt tun:


```python
sudo apt-get install winpdb
```

Jetzt werden wir das Fehlerdiagnoseprogramm einrichten.

1.  Starte *Winpdb*.
2.  Setze das Fehlerdiagnoseprogramm Passwort auf \"test\": Gehe zum Menü *Datei* → *Passwort* und setze das Passwort.

Jetzt werden wir ein Python-Test-Skript in FreeCAD Schritt-für-Schritt ablaufen lassen.

1.  Starten Sie winpdb und setzen Sie ein Passwort (z.B. Test)
2.  Erzeugen Sie eine Pythondatei mit folgendem Inhalt:


```python
import rpdb2
rpdb2.start_embedded_debugger("test")
import FreeCAD
import Part
import Draft
print "hello"
print "hello"
import Draft
points=[FreeCAD.Vector(-3.0,-1.0,0.0),FreeCAD.Vector(-2.0,0.0,0.0)]
Draft.makeWire(points,closed=False,face=False,support=None)
```

1.  Starte FreeCAD und lade die obige Datei in FreeCAD.
2.  Drücke F6, um es auszuführen.
3.  Jetzt wird FreeCAD nicht mehr reagieren, weil das Python Fehlerdiagnoseprogramm wartet.
4.  Wechsle zur Windpdb GUI und klicke auf \"Anhängen\". Nach einigen Sekunden erscheint ein Eintrag \"\", in dem du doppelt klicken musst.
5.  Nun erscheint das aktuell ausgeführte Skript in der Winpdb.
6.  Setze einen Bruch in der letzten Zeile und drücke F5.
7.  Drücke nun F7, um in den Python Code von Draft.makeWire zu gelangen.


</div>


</div>

### Visual Studio Code (VS Code) 


<div class="toccolours mw-collapsible mw-collapsed" style="width:800px;">

VS Code Fehlerdiagnose →


<div class="mw-collapsible-content">

Voraussetzungen:

-   Das ptvsd Paket muss installiert werden


```python
pip install ptvsd
```

[pypi Seite](https://pypi.org/project/ptvsd/)

[Visual Studio Code Dokumentation für die Fern Fehlerdiagnose](https://code.visualstudio.com/docs/python/debugging#_remote-debugging)

Schritte:

-   Füge folgenden Code am Anfang deines Skripts hinzu


```python
import ptvsd
print("Waiting for debugger attach")
# 5678 is the default attach port in the VS Code debug configurations
ptvsd.enable_attach(address=('localhost', 5678), redirect_output=True)
ptvsd.wait_for_attach()
```

-   Füge eine Fehlerdiagnosekonfiguration in Visual Studio Code {{MenuCommand/de|Fehlerdiagnose → Konfigurationen hinzufügen...}}. Es sollte so aussehen:




        "configurations": [
            {
                "name": "Python: Attacher",
                "type": "python",
                "request": "attach",
                "port": 5678,
                "host": "localhost",
                "pathMappings": [
                    {
                        "localRoot": "${workspaceFolder}",
                        "remoteRoot": "."
                    }
                ]
            },

-   Füge im VS-Code einen Haltepunkt hinzu, wo immer Du willst.
-   Starte das Skript in FreeCAD. FreeCAD Freeze wartet auf den Anhang.
-   In VS Code startest Du die Fehlerdiagnose durch Verwendung der erstellten Konfiguration. Du solltest Variablen im Fehlerdiagnosebereich sehen.
-   Beim Setzen von Haltepunkten wird sich VS Code darüber beschweren, die im VS Code-Editor geöffnete .py-Datei nicht zu finden.
    -   Ändere \"remoteRoot\": \".\" zu \"remoteRoot\": \"\"
    -   z.B. wenn sich die Python-Datei in */home/FC\_myscripts/myscript.py* befindet
    -   ändere zu \"remoteRoot\": \"/home/FC\_myscripts/myscript.py\"
-   Wenn dein Makro ptvsd nicht findet, obwohl du es irgendwo installiert hast, stelle \'import ptvsd\' folgendes voran


```python
from sys import path
sys.path.append('/path/to/site-packages')
```

wobei der Pfad das Verzeichnis ist, in dem ptvsd installiert wurde

-   Auf der linken unteren Seite des VSCode kannst Du das Python-Programm auswählen - es ist das Beste, die mit FreeCAD ausgelieferte Version zu verwenden.

In der Mac-Version ist es /Applications/FreeCAD.App/Contents/Resources/bin/python

Du kannst es auf deinem System lokalisieren durch Eingabe von 
```python
import sys
print(sys.executable)
``` in die FreeCAD-Python-Konsole.


</div>


</div>

## Fehlerdiagnose OpenCasCade 

Für Entwickler, die tiefer in den OpenCasCade Kernel einsteigen müssen, hat der Benutzer \@abdullah eine [Forumsbetrag](https://forum.freecadweb.org/viewtopic.php?f=10&t=47017) Orientierung erstellt, in der die Vorgehensweise diskutiert wird.





{{Powerdocnavi

}} 

[<img src="images/Property.png" style="width:16px"> Developer Documentation](Category_Developer_Documentation.md) [<img src="images/Property.png" style="width:16px"> Python Code](Category_Python_Code.md)

---
[documentation index](../README.md) > [Developer Documentation](Category_Developer Documentation.md) > Debugging/de
