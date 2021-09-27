# Python Development Environment/de
{{TOCright}}

## Eine vereinfachte Entwicklungsumgebung für Python in FreeCAD 

_ ist eine Programmierumgebung, die in das _).

Für die Programmentwicklung in Python stehen zahlreiche Werkzeuge zur Verfügung. Die komplizierenden Faktoren für die Entwicklung von Python zur Verwendung mit FreeCAD sind zweifach: Zum einen haben die Werkzeuge keine Unterstützung für die zahlreichen Datenstrukturen und Zugriffspunkte von FreeCAD; zum anderen funktionieren sie nicht \"innerhalb von FreeCAD\". Das bedeutet, dass Du mit ihnen Code außerhalb von FreeCAD entwickeln kannst und nicht in der Zielumgebung testen kannst; oder Du kannst Python in der Zielumgebung (d.h. der FreeCAD Umgebung) entwickeln, hast aber keine Unterstützung durch die Entwicklungswerkzeuge. Keines von beiden ist eine akzeptable Lösung.

## Hintergrund

Die moderne Softwareentwicklung auf dem kommerziellen Standard erfolgt in der Regel mit einem Satz von Werkzeugen, der üblicherweise als _ bezeichnet wird. Typischerweise umfassen diese Werkzeuge die folgenden 3:

-   Quellcode Editor
-   Automatisierungstools bauen
-   Fehlersuchprogramme

die Standard sind, während die folgenden in einigen IDEs vorhanden sind, in anderen aber nicht:

-   intelligente Code Vervollständigung
-   integrierter Compiler, Interpreter oder beides
-   Versionskontrollsystem
-   Konstruktion der grafischen Benutzeroberfläche (GUI)
-   Klasse Browser
-   Objekt Browser
-   Klassenhierarchie Diagramm

Eine Zusammenfassung des Status dieser Werkzeuge innerhalb von FreeCAD ist (\'N/V\' bedeutet \'Nicht Verfügbar\'.):


<table style="width: 100%" border="1">


<tr>


<td>

Quellcodeeditor


</td>


<td>

Eine Vielzahl von Editoren sind verfügbar, für die von FreeCAD unterstützten Plattformen, die im Folgenden besprochen werden


</td>


</tr>


<tr>


<td>

Bau Automatisierungswerkzeug


</td>


<td>

N/V


</td>


</tr>


<tr>


<td>

Fehlersuchprogramm


</td>


<td>

geplant, aber noch nicht verfügbar, es gibt einige Übergangslösungen, die unten diskutiert werden


</td>


</tr>


<tr>


<td>

intelligente Code Vervollständigung


</td>


<td>

es sind einige über die Python Konsole verfügbar, aber das ist alles


</td>


</tr>


<tr>


<td>

integrierter Compiler, Interpreter oder beides


</td>


<td>

Der Python Compiler ist in die Python Konsole integriert, aber nicht in die Editoren


</td>


</tr>


<tr>


<td>

Versionskontrollsystem


</td>


<td>

N/V - es gibt nur eine Version der Datei


</td>


</tr>


<tr>


<td>

Konstruktion der grafischen Benutzeroberfläche (GUI)


</td>


<td>

Was verfügbar ist, ist einfach und basiert auf Kopieren/Einfügen von Code (siehe [PySide](PySide/de.md))


</td>


</tr>


<tr>


<td>

Klassenbetrachter


</td>


<td>

N/V


</td>


</tr>


<tr>


<td>

Objektbetrachter


</td>


<td>

N/V


</td>


</tr>


<tr>


<td>

Klassenhierarchiediagramm


</td>


<td>

N/V


</td>


</tr>


</table>

Es gibt viele Werkzeuge zur Unterstützung der oben genannten Funktion für die Python Programmierung, aber leider lassen sie sich nicht in die FreeCAD Entwicklungsumgebung integrieren.

Eine Liste von IDEs für Python findest du unter [Integrierte Entwicklungsumgebungen für Python](https://wiki.python.org/moin/IntegratedDevelopmentEnvironments).

## Editoren

Es gibt einen Editor für Python als Teil von FreeCAD, er wird durch Klicken auf die Schaltfläche Bearbeiten im Menü Makro-\>Makros\... gestartet. Wenn du einen Editor eines Drittanbieters verwenden möchtest, der die Vorteile deiner Plattform ausnutzt, dann gibt es verschiedene Python Editoren, für zahlreiche Plattformen und mit unterschiedlichem Funktionsumfang. Ein Vorteil der Verwendung eines externen Editors ist, dass der Anzeigebereich von FreeCAD für die Ausgabe (sowohl grafisch als auch in Textform auf der Konsole) genutzt werden kann, während der Quellcode in einer anderen Anwendung angezeigt wird. Eine Liste von Editoren für Python für eine Vielzahl von Plattformen ist verfügbar unter [Python Editoren](https://wiki.python.org/moin/PythonEditors).

Hinweis: Für den Macintosh funktioniert der Texteditor [TextWrangler](http://www.barebones.com/products/textwrangler/) gut. Er verfügt über Code Hervorhebung und ausgezeichnete Suchmöglichkeiten. Es gibt Optionen zur Ausführung von Aufträgen in Python, aber diese funktionieren natürlich nicht mit der FreeCAD Umgebung.

### Makro Quellcode Verzeichnisse 

Es gibt zwei Verzeichnisse, die von FreeCAD verwendet werden. Standardmäßig handelt es sich um dasselbe Verzeichnis, aber sie werden von verschiedenen Aufrufpunkten in FreeCAD angesprochen:

-   FreeCAD.ConfigGet (\"UserAppData\")
-   FreeCAD.ParamGet(\'User parameter:BaseApp/Preferences/Macro\').GetString(\'MacroPath\')

Das erste \"UserAppData\" zeigt auf ein Verzeichnis, in dem Dinge wie Konfigurationsdateien oder andere Dateien, die für den Benutzer bestimmt sind, aber nicht vom Benutzer bearbeitet werden sollen, gespeichert werden können.

Das zweite \"MacroPath\" verweist auf ein Verzeichnis, in dem die Python Dateien, bei denen es sich um Makro Dateien für FreeCAD handelt, gespeichert sind. Um eine Python Datei als Makro Datei für FreeCAD zu markieren, wird die Dateierweiterung von \".py\" in \".FCMacro\" geändert.

Standardmäßig befinden sich diese beiden Verzeichnisse am selben Ort, aber dies ist nicht notwendig. Es kann sinnvoll sein, den Speicherort für die Makro Dateien (\*.FCMacro) auf einen anderen Speicherort zu ändern.

Das Bearbeiten von Dateien, die sich im \"MacroPath\" befinden, ist unkompliziert, der Texteditor wird dies berücksichtigen. Um die Benutzung von FreeCAD Makro Dateien zu erleichtern, ist es ratsam, alle Makro Dateien in dem Verzeichnis zu belassen, auf das \"MacroPath\" verweist.

Um das Verzeichnis \"MacroPath\" zu ändern, verwende Werkzeuge-\>Parameter bearbeiten und wähle dann Einstellungen/Makro/MakroPfad, wo der Text doppelgeklickt und bearbeitet werden kann. Alternativ kann \"MacroPath\" durch den Code geändert werden: 
```python
FreeCAD.ParamGet('User parameter:BaseApp/Preferences/Macro').SetString('MacroPath','/me/myself/and/I')
```

## Fehlersuchprogramm


**'''Ein Fehlersuchprogramm ist für FreeCAD geplant, und diese Schritte sind ein Übergangslösung, bis er verfügbar ist. Siehe github.com/mumme74/FreeCAD/tree/editor_fixes'''**

_ bieten typischerweise zwei Hauptfunktionen (unter anderem):

-   Haltepunkte im Quellcode
-   Variablenprüfung

**Haltepunkte** sind \'Fallen\', die in den Code gesetzt werden. Wenn der Ausführungspfad durch den Code auf einen dieser Haltepunkte trifft, wird die Ausführung angehalten oder unterbrochen. Beachte, dass die Ausführung nicht angehalten wird, da beim Anhalten eines Programms alle speicherresistenten Informationen wie z.B. Variablen verloren gehen. Während das Programm angehalten wird, kann der Inhalt der Variablen überprüft und manchmal geändert werden (was von der Fähigkeit des Fehlersuchprogramms abhängt). Im Allgemeinen kann der Quellcode nicht geändert werden, obwohl einige Umgebungen dies unterstützen. Wenn der Quellcode fertig ist, kann die Ausführung des Quellcodes wieder aufgenommen werden. Es können zahlreiche Haltepunkte im Code gesetzt werden und es kann zu zahlreichen Unterbrechungen durch die Haltepunkte kommen. Der Zweck des Fehlersuchprogramms besteht darin, sicherzustellen, dass die Ausführung mit den Haltepunkten und Unterbrechungen funktionell identisch mit der Ausführung ohne Haltepunkte ist.

**Variablenprüfungen** sind während der durch einen Haltepunkt verursachten Aussetzung der Ausführung verfügbar. Im Allgemeinen kann der Inhalt von Variablen eingesehen werden, viele Fehlersuchprogramme unterstützen auch die Bearbeitung des Inhalts, bevor die Ausführung wieder aufgenommen wird.

Obwohl ein voll funktionsfähiger Fehlersuchprogramm für FreeCAD geplant ist, ist es noch nicht verfügbar. In diesem Abschnitt werden einige Arbeitsumgehungen für die Zwischenzeit bis zur Freigabe des Fehlersuchprogramms beschrieben.

### Haltepunkte

Die Implementierung von Haltepunkten beinhaltet eine übergeordnete Ebene des Codes, die die Ausführung des in Entwicklung befindlichen Codes verwaltet. Eine solche Code Ebene für die Python Entwicklung innerhalb von FreeCAD ist derzeit nicht verfügbar. Als schwacher Ersatz ist der folgende Code eine Option. Anstatt die Ausführung zu unterbrechen, wird die Ausführung des Codes vollständig gestoppt, indem eine Zahl durch Null geteilt wird. Dies ist wirklich eine sehr schwache Option im Vergleich zu einem richtigen Fehlersuchprogramm Haltepunkt, außerdem ist diese Option nur von Nutzen, wenn sie zusammen mit der im nächsten Abschnitt \'Variablenprüfung\' gezeigten Routine verwendet wird.

**Breakpoint Code** 
```python
def breakpoint(*args):
    # this routine will print an optional parameter on the console and then stop execution by diving by zero
    # e.g. breakpoint()
    # e.g. breakpoint("summation module")
    #
    if len(args)>0:
        FreeCAD.Console.PrintMessage('Breakpoint: '+str(args[0])+"\n")
    hereWeStop = 12/0
    
``` **Konsolen Traceback (Rückverfolgung)**

Wenn ein Programm während der Ausführung fehlschlägt, erzeugt Python einen sogenannten Traceback (Rückverfolgung), der die Reihenfolge der Programmausführung auflistet (d.h. welches Programm welches Programm in welcher Reihenfolge aufgerufen hat).

Für das Codebeispiel 
```python
breakpoint('amalgamation routine')
``` erhalten wir den/die folgende(n) Traceback/Rückverfolgung: 
```python
Breakpoint: amalgamation routine
Traceback (most recent call last):
  File "/Users/wylbur/Library/Preferences/FreeCAD/testStub.FCMacro", line 40, in <module>
    breakpoint()
  File "/Users/wylbur/Library/Preferences/FreeCAD/myNewMacro.FCMacro", line 28, in breakpoint
    hereWeStop = 12/0
ZeroDivisionError: integer division or modulo by zero
``` Wenn wir den/die Traceback/Rückverfolgung lesen, können wir das feststellen:

-   eine Nachricht von \'Haltepunkt: Verschmelzungsroutine\' von dem Haltepunkt gesendet wurde, der die Zeichenkette \'Verschmelzungsroutine\' hat
-   der Ausführungsfehler trat in Zeile 28 des Moduls \'myNewMacro\' auf
-   die Routine \'myNewMacro\' wurde ab Zeile 40 im Modul \'testStub\' aufgerufen

Angenommen, die an den Haltepunktaufruf übergebene Zeichenfolge ist aussagekräftig, dann kann die Position des Haltepunkts leicht bestimmt werden. Beachte, dass es sich um ein komplexes System handelt, in dem die Rückverfolgung Dutzende oder sogar Hunderte von Einträgen enthalten kann.

Um mit diesen Haltepunkten produktiv zu werden, fahre mit dem nächsten Abschnitt fort.

### Variablenprüfung

Das zweite Hauptmerkmal eines Fehlersuchprogramms besteht darin, den Inhalt von Variablen zu untersuchen und möglicherweise zu ändern. Noch einmal, bis das FreeCAD Fehlersuchprogramm für Python fertig ist, sind wir auf Zwischenlösungen angewiesen.

Ein Merkmal des FreeCAD Systems ist die Bereitstellung von globalen Variablen. Diese Variablen werden durch den Python Code erzeugt und existieren im Speicher von FreeCAD, bis der Benutzer FreeCAD verlässt. Die Form dieser Variablen ist: 
```python
FreeCAD.myVariable = 123
``` Die Anweisung erzeugt eine Python Variable im FreeCAD Speicher, auf die Python Code uneingeschränkt zugreifen kann. Tatsächlich verhält sie sich identisch zu einer normalen Python Variable. Dennoch nach Beendigung der Ausführung des Python Codes, unabhängig davon, ob er als Makro oder über die Konsole ausgeführt wird, verbleibt im Speicher eine Variable \'FreeCAD.myVariable\' mit dem Wert 123. Eingabe: 
```python
>>> FreeCAD.myVariable
123
``` erzeugt den Inhalt der Variable auf der Konsole. Dieser Wert verbleibt in FreeCAD, bis er entweder geändert wird oder der Benutzer FreeCAD verlässt. Das bedeutet, dass der Wert vorhanden und für ein nachfolgendes Python Programm zum Lesen verfügbar ist. Er kann jederzeit von der Konsole aus überprüft werden, indem man seinen Namen eingibt. Also ein Programm namens \'Programm A\': 
```python
# program A
myListVariable = list()
myListVariable.append(123)
myListVariable.append('abc')
FreeCAD.myVariable = myListVariable
``` kann ausführen und Werte in die globale Variable laden. Später kann ein zweites Programm namens \'Programm B\' laufen und den Wert abrufen: 
```python
myOtherVariable = FreeCAD.myVariable
# further calculations involving myOtherVariable
``` Vermutlich führt \'Programm B\' dann Berechnungen mit den in FreeCAD.myVariable verbliebenen Werten durch. Der Benutzer kann jederzeit in die Konsole tippen, um den Inhalt der Variablen zu überprüfen: 
```python
>>> FreeCAD.myVariable
[123, 'abc']
>>> 
``` Eine wichtige Tatsache, die bei globalen Variablen in FreeCAD beachtet werden muss, ist, dass sie im Speicher existieren und verloren gehen, wenn das Programm beendet wird. Sie werden nicht mit Dokumenten gespeichert, sondern existieren nur im Speicher.

### Anwendung

Damit sind wir an einem Punkt angelangt, an dem wir die beiden Schritte zusammenfügen und sie dazu nutzen können, Fehler im Code aufzuspüren. Dies ist etwas umständlich in der Anwendung, aber es ist nur eine Option, bis das FreeCAD Fehlersuchprogramm fertig ist.

Es ist wahrscheinlich am einfachsten, es anhand eines Beispiels zu präsentieren, sagen wir, das folgende Programm wird fehlerbereinigt: 
```python
def monthCounter():
    # program to calculate the number of months in the year
    signsInTheZodiac = 12
    numberOfSeasons = 3
    numberOfCompassPoints = 5
    #
    temporaryVariable1 = signsInTheZodiac + numberOfSeasons
    numberOfMonths = temporaryVariable1 - numberOfCompassPoints
    #
    FreeCAD.Console.PrintMessage(numberOfMonths)
``` Die Ausführung des Programms auf der Konsole ergibt: 
```python
>>> monthCounter()
10
``` was nicht das ist, was wir erwartet haben! Angenommen, wir sind nicht in der Lage, die Fehler zu erkennen, dann können wir unseren unkomplizierten Haltepunkt- und Variablenprüfer wie folgt einsetzen. Wir können eine Zeile einfügen, um den Wert der Variablen, über die wir uns wundern, in eine globale Variable zu kopieren, dann können wir einen Haltepunkt setzen, um die Ausführung dort anzuhalten: 
```python
def monthCounter():
    # program to calculate the number of months in the year
    signsInTheZodiac = 12
    numberOfSeasons = 3
    numberOfCompassPoints = 5
    #
    temporaryVariable1 = signsInTheZodiac + numberOfSeasons
    FreeCAD.saveMyVariable = temporaryVariable1 # <<<<<<<<<<< first inserted line
    breakpoint('is this assignment faulty?') # <<<<<<<<<<<<<< second inserted line
    numberOfMonths = temporaryVariable1 - numberOfCompassPoints
    #
    FreeCAD.Console.PrintMessage(numberOfMonths)
``` Nun, wenn wir das Programm ausführen, erhalten wir: 
```python
>>> monthCounter()
Breakpoint: is this assignment faulty?
Traceback (most recent call last):
  File "<input>", line 1, in <module>
  File "<input>", line 9, in monthCounter
  File "<input>", line 5, in breakpoint
ZeroDivisionError: integer division or modulo by zero
>>> 
``` Wahrscheinlich sieht es nicht so gut aus, aber was wir jetzt tun können, ist, den Wert der Python Variablen \'temporaryVariable1\' zu überprüfen, wie wir ihren Wert der globalen Variablen \'FreeCAD.saveMyVariable\' zugewiesen haben: 
```python
>>> FreeCAD.saveMyVariable
15
>>>
``` Wenn wir uns daran erinnern, dass die Variable \'FreeCAD.saveMyVariable\' den Wert der Python Variablen \'temporaryVariable1\' enthält, können wir jetzt den Fehler im Wert bestimmen und mit der Rückverfolgung beginnen, um festzustellen, woher der Fehler kam. Wenn wir uns \'FreeCAD.saveMyVariable\' anschauen, ist es wichtig zu erkennen, dass die Variable \'temporaryVariable1\' nicht mehr verfügbar ist - sie wurde vom Python-System weggeholt.

Sobald der Fehler in der Anweisung lokalisiert wurde 
```python
numberOfSeasons = 3
``` und korrigiert auf: 
```python
numberOfSeasons = 4
``` Dann können wir das Programm erneut ausführen und erhalten den Wert \'11\', was immer noch nicht richtig ist. Wir können mehr Zuweisungen an globale FreeCAD Variablen vornehmen, mehrere Haltepunkte haben (obwohl der erste, der angetroffen wird, die Ausführung stoppt) 
```python
def monthCounter():
    # program to calculate the number of months in the year
    signsInTheZodiac = 12
    numberOfSeasons = 4
    numberOfCompassPoints = 5
    #
    temporaryVariable1 = signsInTheZodiac + numberOfSeasons
    FreeCAD.saveMyVariable1 = temporaryVariable1
    #breakpoint('first assignment')
    numberOfMonths = temporaryVariable1 - numberOfCompassPoints
    FreeCAD.saveMyVariable2 = numberOfMonths
    breakpoint('second assignment')
    #
    FreeCAD.Console.PrintMessage(numberOfMonths)
``` Wir haben jetzt zwei Haltepunkte (obwohl einer auskommentiert ist) und zwei globale FreeCAD Variablen in Verwendung. Es gibt keine praktische Begrenzung für die von FreeCAD verfügbaren globalen Variablen, so dass keine unnötigen Einsparungen erforderlich sind. Wir können jetzt auf der Konsole Folgendes erzeugen: 
```python
>>> FreeCAD.saveMyVariable1
10
>>> FreeCAD.saveMyVariable2
11
>>> 
``` Einige Punkte über die Verwendung der globalen FreeCAD Variablen:

-   Python behandelt diese Variablen identisch zu jeder anderen Python Variablen
-   diese Variablen können jeden Python Datentyp enthalten - alles, was eine reguläre Python Variable enthalten würde
-   diese Variablen können verwendet werden, um den Inhalt einer Python Variablen \'herauszubringen\', damit wir sie sehen können
-   auch diese Variablen können verwendet werden, um einer Python Variablen Werte \'zuzuführen\', indem ihr Wert von der Konsole aus vor der Ausführung einer Routine oder in einem früheren Python Programm gesetzt wird
-   diese Variablen können verwendet werden, um Daten zwischen zwei Programmen zu übergeben, die zu verschiedenen Zeitpunkten laufen
-   (zu wiederholen) diese Variablen sind nur für die Dauer der FreeCAD Sitzung, sobald der Benutzer FreeCAD verlässt, sind die Variablen verloren

### Variablen Beobachter 

Es gibt ein Dienstprogramm [Global Variable Watcher](Macro_Global_Variable_Watcher/de.md), um die globalen Variablen von FreeCAD zu überwachen. Es kann den Inhalt einer globalen Variable entweder auf Anfrage oder auf Zeitbasis anzeigen.

### Namensraum Konflikt 

Eine Sache, die man beachten muss, ist, dass FreeCAD keine Verwaltung von globalen Variablennamen hat, so dass die Möglichkeit besteht, eine Variable vom System oder ein anderes Stück Code zu ändern. Folglich ist es eine gute Idee, Ihren Variablen etwas Eindeutiges voranzustellen, wie z.B. den Routinenamen. Um beispielsweise eine Variable aus einer Routine namens \'alpha1\' zu verwenden, könnte der globale Name \'FreeCAD.alpha1MyVariable\' lauten.

## Codierungsgerüst

Bei der Entwicklung von kleinen Teilen des Python Codes in FreeCAD kann es ausreichen, die Python Konsole zu verwenden. Mit zunehmender Anzahl von Codezeilen macht es jedoch mehr Sinn, diese in einer Datei zu speichern. Python kann in jeder Datei mit der Endung \".py\" stehen, FreeCAD bietet jedoch auch einen Mechanismus namens Macro zum Speichern solcher Programme und zur Interaktion mit ihnen (z.B. Bearbeiten, Ausführen). Python in regulären \'.py\'-Dateien kann nur von der Python Konsole aus ausgeführt werden, während Python in der Makro Datei \'.FCMacro\' von der FreeCAD Schnittstelle zur Ausführung von Makros ausgeführt werden kann. Ein Nachteil der FreeCAD Menüoberfläche ist, dass sie menügeführt ist und ein Kontrollfenster enthält, was zu einem gewissen Durcheinander auf der Bildschirmoberfläche führen kann.

Ein einfacherer Ansatz ist es, den Python Code zu nehmen und ihn nicht aus dem FreeCAD Makro Menü zu starten, sondern aus einer Werkzeugleiste heraus. Eine Python Routine, die mit einer Schaltfläche in einer Symbolleiste verknüpft ist, kann mit einem Klick ausgeführt werden. Da es sich bei den Symbolleisten um schwebende Fenster handelt, wird die Bildschirmanzeige nicht überladen. Wenn das FreeCAD Fenster kleiner als die physische Größe des Bildschirms ist, kann die Symbolleiste außerhalb des FreeCAD Fensters schweben. Dies ist vorteilhaft, wenn Bildschirmschnappschüsse der FreeCAD Anzeige benötigt werden. Außerdem kann die Werkzeugleiste viel kleiner sein als das Makro-Steuerungsfenster, das im Makro Menü von FreeCAD angezeigt wird.

Das Verbinden eines Makros mit einer Schaltfläche auf einer Symbolleiste wird in [So installieren Sie Makros](How_to_install_macros/de.md) und [So passen Sie eine Symbolleiste an](Customize_Toolbars/de.md) behandelt. Es kann einige Minuten dauern, ein Makro mit einer Schaltfläche in der Symbolleiste zu verbinden, ein Symbol auszuwählen usw. Dies ist nicht immer erforderlich, da man manchmal einfach nur schnell ein Stück Code ausarbeiten möchte, das dann in einen anderen Code integriert wird. Für diese Situation kann ein Test Stub vorteilhaft sein. Es gibt keine wirkliche Definition dafür, was ein Test-Stub beinhalten würde, es hängt wirklich von der Person und dem Anwendungsbereich ab. Ein Beispiel ist unten dargestellt: 
```python
#
#           TEST
#           TEST stub to clip any code onto...
#           TEST
#
################################
# routine to <description goes here>
"""
script does <long winded description goes here>
"""

# import statements
import FreeCAD
from FreeCAD import Base
import math, collections
from PySide import QtGui, QtCore

# UI Class definitions

# Class definitions

# Functions definitions

# Constant definitions

# code ***********************************************************************************

QtGui.QMessageBox.information(None,"","Test Stub")

##########################################################################################
##########################################################################################
##########################################################################################
``` Dieser Test stub dient auch als Vorlage für Code mit definierten Stellen für die verschiedenen Aspekte eines großen Python Programms. Bei der Ausführung des Teststub Programms wird einfach eine Meldung mit dem Namen des Programms erzeugt und beendet. Bei der Verwendung eines Teststubs wird der geschriebene Hauptzeilencode ganz am Ende der Datei platziert, wobei der Code für die Klassendefinition, Funktionen usw. in den vorherigen Abschnitten platziert wird. Das Template kann einfach an die Situation angepasst werden. Bei einem Programm mit 5 Zeilen ist eine solche Menge an Dokumentation natürlich nicht notwendig.

Indem man einen Button permanent auf einer Symbolleiste behält und diesen Button mit dem Test Sub verknüpft, gibt es immer einen Bereich, in dem man Code schreiben und sofort ausführen kann. Die Ausführung erfolgt unabhängig von der Python Konsole. Die Ausführung kann auch unabhängig von der Bildschirm GUI erfolgen. Die Ausgaben des zu entwickelnden Programms erscheinen so, wie sie auf dem Bildschirm erscheinen sollen, ohne weitere Artefakte aus der Programmierumgebung. Die Python Konsole kann bei Bedarf ausgeblendet werden, um die Anzeigefläche zu vergrößern oder für andere Zwecke verwendet werden. Wenn die Ausführung über die Schaltfläche in der Werkzeugleiste erfolgt, wird die Konsole nicht benötigt.

Wenn der Code fertig ist, kann er einfach in eine andere Datei kopiert werden und der Text stub bleibt bis zum nächsten Mal leer.

Mehrere Code Stücke können unter Verwendung desselben Teststub mit etwas extra Code für die Bereitstellung mehrerer Buttons entwickelt werden, der sich unter [PySide Beginner Examples - More Than 2 Buttons](PySide_Beginner_Examples#More_Than_2_Buttons/de.md) befindet.

**Mehr PySide Unterstützung**

Für weitere Unterstützung bei der Verwendung der PySide GUI gibt es die Seite [PySide](PySide/de.md)

**Mehr Unterstützung für Python Programmierung**

Für weitere Unterstützung bei der Python Codierung gibt es ein Makro, das zur Unterstützung bei der Entwicklung von Python Code geschrieben wurde, befindet es sich unter [Python Assistenz Fenster](Macro_Python_Assistant_Window/de.md)

## Alles Zusammensetzen 

Die Bildschirmverwaltung kann eine Herausforderung sein, wenn es darum geht, Code zu entwickeln, der komplexe und detaillierte grafische Ausgaben hat, wie es FreeCAD tut. Das folgende System funktioniert gut:

-   FreeCAD für Konsole, Bericht, GUI-Anzeige
-   Symbolleiste zum Aufruf von in Entwicklung befindlichem Code
-   externer Editor zum Modifizieren des Codes
-   PAW (Python Assistant Window) zur Unterstützung der Python Code Generierung

**Bildschirmmanagement**

Wenn der Test stub über eine Symbolleiste bedient wird und ein externer Editor verwendet wird, wird das Fensterlayout auf dem Bildschirm in etwa so aussehen:

![](images/PythonDevelopmentEnvironment.jpg )

\"Baum\" im Diagramm bezieht sich auf den Combi oder Baum Browser, die Python Konsole und die Report Ansicht sind im unteren Fenster zusammengefasst und über Schaltflächen auswählbar. Durch den gezielten Einsatz der Werkzeuge kann der Entwicklungsstrom optimiert werden, das oben genannte ist nur eine Idee. Der Zuschnitt erfolgt auf einer persönlichen Basis.

## Verschiedene Verknüpfungen 

Einige andere Verknüpfungen über IDEs für Python, die von Interesse sein könnten, sind:

-   [Vergleich von Python-IDEs für die Entwicklung](http://www.pythoncentral.io/comparison-of-python-ides-development/)
-   [Die beste Python-IDE auswählen](http://pedrokroger.net/choosing-best-python-ide/)
-   [Ihre Entwicklungsumgebung](http://docs.python-guide.org/en/latest/dev/env/)
-   [PyCharm Community Edition IDE](http://www.jetbrains.com/pycharm/)


 

_ _

---
[documentation index](../README.md) > [Poweruser Documentation](Category_Poweruser Documentation.md) > Python Development Environment/de
