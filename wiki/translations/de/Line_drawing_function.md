# Line drawing function/de
{{TOCright}}

## Einführung

Diese Seite zeigt, wie erweiterte Funktionalität in Python einfach erstellt werden kann. In dieser Übung werden wir ein neues Werkzeug bauen, das eine Linie zeichnet. Dieses Werkzeug kann dann mit einem FreeCAD Befehl verknüpft werden, und dieser Befehl kann von jedem Element in der Oberfläche, wie z.B. einem Menüpunkt oder einer Werkzeugleistenschaltfläche, aufgerufen werden.

## Das Hauptskript 

Zuerst werden wir ein Skript schreiben, das unsere gesamte Funktionalität enthält. Dann werden wir dieses in einer Datei speichern und in FreeCAD importieren, so dass alle von uns geschriebenen Klassen und Funktionen in FreeCAD zur Verfügung stehen. Starte deinen bevorzugten Codeeditor und gib die folgenden Zeilen ein:


```python
import FreeCADGui, Part
from pivy.coin import *

class line:

    """This class will create a line after the user clicked 2 points on the screen"""

    def __init__(self):
        self.view = FreeCADGui.ActiveDocument.ActiveView
        self.stack = []
        self.callback = self.view.addEventCallbackPivy(SoMouseButtonEvent.getClassTypeId(), self.getpoint)

    def getpoint(self, event_cb):
        event = event_cb.getEvent()
        if event.getState() == SoMouseButtonEvent.DOWN:
            pos = event.getPosition()
            point = self.view.getPoint(pos[0], pos[1])
            self.stack.append(point)
            if len(self.stack) == 2:
                l = Part.LineSegment(self.stack[0], self.stack[1])
                shape = l.toShape()
                Part.show(shape)
                self.view.removeEventCallbackPivy(SoMouseButtonEvent.getClassTypeId(), self.callback)
```


{{Top}}

## Detaillierte Erklärung 


```python
import Part, FreeCADGui
from pivy.coin import *
```

Wenn Du in Python Funktionen aus einem anderen Modul verwenden willst, musst Du es importieren. In unserem Fall benötigen wir Funktionen aus dem [Part-Arbeitsbereich](Part_Workbench/de.md), um die Linie zu erstellen, und aus dem Gui Modul `FreeCADGui`, um auf die [3D-Ansicht](3D_view/de.md) zuzugreifen. Außerdem benötigen wir die kompletten Inhalte der Coin-Bibliothek, damit wir alle Coin-Objekte wie `SoMouseButtonEvent`, usw. direkt verwenden können.


```python
class line:
```

Hier definieren wir unsere Hauptklasse. Warum verwenden wir eine Klasse und keine Funktion? Der Grund dafür ist, dass wir unser Werkzeug \"am Leben\" halten müssen, während wir darauf warten, dass der Benutzer auf den Bildschirm klickt. Eine Funktion endet, wenn ihre Aufgabe erledigt ist, aber ein Objekt (eine Klasse definiert ein Objekt) bleibt am Leben, bis es zerstört wird.


```python
"""This class will create a line after the user clicked 2 points on the screen"""
```

In Python kann jede Klasse oder Funktion einen Dokumentationszeichenkette (docstring) haben. Dies ist besonders in FreeCAD nützlich, denn wenn du diese Klasse im Interpreter aufrufst, wird der Beschreibungszeichenkette als Tooltip angezeigt.


```python
def __init__(self):
```

Python Klassen können immer eine `__init__` Funktion enthalten, die beim Aufruf der Klasse zur Erzeugung eines Objekts ausgeführt wird. Wir werden hier also alles ablegen, was sich ereignen soll, wenn unser Linienwerkzeug beginnt.


```python
self.view = FreeCADGui.ActiveDocument.ActiveView
```

In einer Klasse möchte man normalerweise `self.` vor einem Variablennamen anhängen, damit sie für alle Funktionen innerhalb und außerhalb dieser Klasse leicht zugänglich ist. Hier werden wir `self.view` verwenden, um auf die aktive 3D Ansicht zuzugreifen und sie zu verändern.


```python
self.stack = []
```

Hier erstellen wir eine leere Liste, die die von der `getpoint()` Funktion gesendeten 3D Punkte enthält.


```python
self.callback = self.view.addEventCallbackPivy(SoMouseButtonEvent.getClassTypeId(), self.getpoint)
```

Das ist der wichtige Teil: Da es sich eigentlich um eine [coin3D](http://www.coin3d.org/) Szene handelt, verwendet FreeCAD einen Coin Rückruf Mechanismus, der es erlaubt, eine Funktion jedes Mal aufzurufen, wenn ein bestimmtes Szene Ereignis eintritt. In unserem Fall erstellen wir einen Rückruf für [SoMouseButtonEvent](http://doc.coin3d.org/Coin/group__events.html) Ereignisse, und wir binden ihn an die `getpoint()` Funktion. Nun wird jedes Mal, wenn eine Maustaste gedrückt oder losgelassen wird, die `getpoint()` Funktion ausgeführt.

Beachte, dass es auch eine Alternative zu `addEventCallbackPivy()` namens `addEventCallback()` gibt, welche die Verwendung von pivy überflüssig macht. Aber da pivy ein sehr effizienter und natürlicher Weg ist, um auf jeden Teil der coin Szene zuzugreifen, ist es viel besser, es so oft wie möglich zu verwenden. {{Top}} 
```python
def getpoint(self, event_cb):
```

Nun definieren wir die `getpoint()` Funktion, die beim Drücken einer Maustaste in einer 3D Ansicht ausgeführt wird. Diese Funktion erhält ein Argument, das wir `event_cb` aufrufen. Von diesem Ereignisrückruf aus können wir auf das Ereignisobjekt zugreifen, das verschiedene Informationen enthält (Mode Info [Hier](Code_snippets/de#Observing_mouse_events_in_the_3D_viewer_via_Python/de.md)).


```python
if event.getState() == SoMouseButtonEvent.DOWN:
```

Die `getpoint()` Funktion wird aufgerufen, wenn eine Maustaste gedrückt oder losgelassen wird. Aber wir wollen einen 3D Punkt nur dann aufnehmen, wenn er gedrückt ist, sonst würden wir zwei 3D Punkte sehr nahe aneinander bekommen. Das müssen wir also hier überprüfen.


```python
pos = event.getPosition()
```

Hier erhalten wir die Bildschirmkoordinaten des Mauszeigers.


```python
point = self.view.getPoint(pos[0], pos[1])
```

Diese Funktion gibt uns einen FreeCAD Vektor (x,y,z), der den 3D Punkt enthält, der auf der Brennpunktebene direkt unter unserem Mauszeiger liegt. Wenn Du Dich in der Kameraansicht befindest, stelle dir einen Strahl vor, der von der Kamera kommt, durch den Mauszeiger hindurchgeht und auf die Brennpunktebene trifft. Das ist die Position ist unseres 3D Punktes. Wenn wir uns in der orthogonalen Ansicht befinden, ist der Strahl parallel zur Blickrichtung.


```python
self.stack.append(point)
```

Wir fügen unseren neuen Punkt dem Stapel hinzu.


```python
if len(self.stack) == 2:
```

Haben wir schon genug Punkte? Wenn ja, dann zeichnen wir die Linie!


```python
l = Part.LineSegment(self.stack[0], self.stack[1])
```

Hier verwenden wir die `LineSegment()`-Funktion aus dem Part-Arbeitsbereich, die eine Linie aus zwei FreeCAD-Vektoren erzeugt. Die Linie ist nicht an irgendein Objekt unseres aktiven Dokuments gebunden, so dass nichts auf dem Bildschirm erscheint.


```python
shape = l.toShape()
```

Das FreeCAD Dokument kann nur Formen aus dem Part Modul übernehmen. Formen sind der grundlegendste Typ des Part Moduls. Daher müssen wir unsere Linie in eine Form konvertieren, bevor wir sie dem Dokument hinzufügen.


```python
Part.show(shape)
```

Das Part Modul hat eine sehr nützliche `show()` Funktion, die ein neues Objekt im Dokument erzeugt und eine Form daran bindet. Wir hätten auch zuerst ein neues Objekt im Dokument erstellen können, und dann die Form manuell an dieses Objekt binden können.


```python
self.view.removeEventCallbackPivy(SoMouseButtonEvent.getClassTypeId(), self.callback)
```

Da wir mit unserer Linie fertig sind, entfernen wir den Rückrufmechanismus hier. {{Top}}

## Testen des Skripts 

Nun speichern wir unser Skript an einem Ort, an dem der FreeCAD Python Interpreter es finden kann. Beim Import von Modulen wird der Interpreter an folgenden Stellen suchen: die Python Installationspfade, das FreeCAD bin Verzeichnis und alle FreeCAD Modulverzeichnisse. Die beste Lösung ist also, ein neues Verzeichnis in einem der FreeCAD [Mod Verzeichnisse](Installing_more_workbenches/de.md) anzulegen und unser Skript darin zu speichern. Erstellen wir zum Beispiel ein Verzeichnis \"MyScripts\" und speichern unser Skript als \"exercise.py\".

Nun, alles ist bereit. Lass uns FreeCAD starten, ein neues Dokument erstellen und im Python Interpreter eingeben:


```python
import exercise
```

Wenn keine Fehlermeldung erscheint wurde unser Übungsskript erfolgreich geladen. Wir können nun seinen Inhalt überprüfen mit:


```python
dir(exercise)
```

Der Befehl `dir()` ist ein eingebauter Python Befehl, der den Inhalt eines Moduls auflistet. Wir können prüfen, dass unsere `line()` Klasse da ist mit:


```python
'line' in dir(exercise)
```

Nun wollen wir es testen:


```python
exercise.line()
```

Klicke zwei Mal in der 3D Ansicht, und Bingo, hier ist unsere Linie! Um es zu wiederholen, tippe einfach nochmal `exercise.line()`. {{Top}}

## Registrierung des Skripts 

Nun, damit unser neues Linienwerkzeug wirklich cool ist, sollte es einen Knopf auf der Oberfläche haben, damit wir nicht immer all dieses Zeug tippen müssen. Am einfachsten ist es, unser neues MyScripts Verzeichnis in einen vollständige FreeCAD Arbeitsbereich zu verwandeln. Es ist einfach, alles was benötigt wird ist eine Datei namens **InitGui.py** in deinem MyScripts Verzeichnis zu speichern. Die Datei InitGui.py enthält die Anweisungen zum Erstellen eines neuen Arbeitsbereichs und fügt unser neues Werkzeug hinzu. Außerdem müssen wir auch unseren Übungscode ein wenig umwandeln, damit das line()-Werkzeug als offizieller FreeCAD Befehl erkannt wird. Beginnen wir damit, eine InitGui.py-Datei zu erstellen, und schreiben wir den folgenden Code hinein:


```python
class MyWorkbench (Workbench):

    MenuText = "MyScripts"

    def Initialize(self):
        import exercise
        commandslist = ["line"]
        self.appendToolbar("My Scripts", commandslist)

Gui.addWorkbench(MyWorkbench())
```

Inzwischen solltest Du das obige Skript schon selbst verstehen, Ich denke: Wir erstellen eine neue Klasse, die wir `MyWorkbench` nennen, wir geben ihr einen Titel `MenuText` und wir definieren eine `Initialize()` Funktion, die ausgeführt wird, wenn der Arbeitsbereich in FreeCAD geladen wird. In dieser Funktion laden wir den Inhalt unserer Übungsdatei ein und hängen die darin enthaltenen FreeCAD Befehle an eine Befehlsliste an. Dann erstellen wir eine Werkzeugleiste namens \"Meine Skripte\" und weisen ihr unsere Befehlsliste zu. Derzeit haben wir natürlich nur ein Werkzeug, so dass unsere Befehlsliste nur ein Element enthält. Sobald unser Arbeitsbereich fertig ist, fügen wir es zur Hauptoberfläche hinzu.

Aber das wird trotzdem nicht funktionieren, da ein FreeCAD Befehl auf eine bestimmte Art und Weise formatiert werden muss, um zu funktionieren. Also müssen wir unser `line()` Werkzeug ein wenig umwandeln. Unser neues **exercise.py** Skript wird nun so aussehen:


```python
import FreeCADGui, Part
from pivy.coin import *

class line:

    """This class will create a line after the user clicked 2 points on the screen"""

    def Activated(self):
        self.view = FreeCADGui.ActiveDocument.ActiveView
        self.stack = []
        self.callback = self.view.addEventCallbackPivy(SoMouseButtonEvent.getClassTypeId(), self.getpoint)

    def getpoint(self, event_cb):
        event = event_cb.getEvent()
        if event.getState() == SoMouseButtonEvent.DOWN:
            pos = event.getPosition()
            point = self.view.getPoint(pos[0], pos[1])
            self.stack.append(point)
            if len(self.stack) == 2:
                l = Part.LineSegment(self.stack[0], self.stack[1])
                shape = l.toShape()
                Part.show(shape)
                self.view.removeEventCallbackPivy(SoMouseButtonEvent.getClassTypeId(), self.callback)

    def GetResources(self):
        return {'Pixmap': 'path_to_an_icon/line_icon.png', 'MenuText': 'Line', 'ToolTip': 'Creates a line by clicking 2 points on the screen'}

FreeCADGui.addCommand('line', line())
```

Was wir hier gemacht haben, ist die Umwandlung unserer `__init__()` Funktion in eine `Activated()` Funktion, denn wenn FreeCAD Befehle ausgeführt werden, führen sie automatisch die `Activated()` Funktion aus. Wir haben auch eine `GetResources()` Funktion hinzugefügt, die FreeCAD darüber informiert, wo es ein Icon für das Werkzeug finden kann und wie der Name und der Tooltip unseres Werkzeugs lauten wird. Jedes **jpg**, **png** oder **svg** Bild wird als Symbol funktionieren, es kann jede beliebige Größe haben, aber es ist am besten, eine Größe zu verwenden, die dem fertigen Seitenverhältnis nahe kommt, wie 16x16, 24x24 oder 32x32. Dann fügen wir die `line()` Klasse als offiziellen FreeCAD Befehl mit der `addCommand()` Methode hinzu.

Das war\'s, anschließend müssen wir nur noch FreeCAD neu starten und schon haben wir einen schönen neuen Arbeitsbereich mit unserem brandneuen Linienwerkzeug! {{Top}}

## Also willst du mehr? 

Wenn Dir diese Übung gefallen hat, warum versuchst Du nicht, dieses kleine Werkzeug zu verbessern? Es gibt viele Dinge, die man tun kann, wie zum Beispiel

-   Benutzer Rückmeldungen hinzufügen: Bis jetzt haben wir ein sehr nacktes Tool gemacht, der Benutzer könnte etwas verloren sein, wenn er es benutzt. Wir könnten also eine Rückmeldung hinzufügen, das ihm sagt, was er als nächstes tun soll. Zum Beispiel könntest Du Meldungen an die FreeCAD Konsole ausgeben. Schaue dir das FreeCAD.Console Modul an
-   Füge die Möglichkeit hinzu, die Koordinaten der 3D Punkte manuell einzugeben. Schaue dir die Python input() Funktion an, zum Beispiel
-   Füge die Möglichkeit hinzu, mehr als 2 Punkte hinzuzufügen
-   Füge Ereignisse für andere Dinge hinzu: Jetzt überprüfen wir nur noch, ob es Ereignisse für die Maustaste gibt, was wäre, wenn wir auch etwas tun würden, wenn die Maus bewegt wird, wie z.B. die aktuellen Koordinaten anzeigen?
-   Gib dem erstellten Objekt einen Namen

Zögere nicht, deine Fragen oder Ideen im [Forum](http://forum.freecadweb.org/) zu teilen! {{Top}}



---
![](images/Button_right.svg) [documentation index](../README.md) > [Developer Documentation](Category_Developer Documentation.md) > [Python Code](Category_Python Code.md) > Line drawing function/de
