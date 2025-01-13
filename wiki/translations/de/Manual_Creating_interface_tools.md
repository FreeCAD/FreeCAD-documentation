# Manual:Creating interface tools/de
{{Manual:TOC}}

In den letzten beiden Kapiteln haben wir gesehen, wie man [Teilgeometrie erstellt](Manual:Creating_and_manipulating_geometry/de.md) und [parametrische Objekte erstellt](Manual:Creating_parametric_objects/de.md). Ein letztes Teil fehlt noch, um die volle Kontrolle über FreeCAD zu erhalten: Erstellen von Werkzeugen, die mit dem Benutzer interagieren.

In vielen Situationen ist es nicht sehr benutzerfreundlich, ein Objekt mit Nullwerten zu konstruieren, wie wir es im vorigen Kapitel mit dem Rechteck getan haben, und den Benutzer dann aufzufordern, die Werte für Höhe und Breite im Eigenschaften-Fenster einzugeben. Dies funktioniert bei einer sehr kleinen Anzahl von Objekten, wird aber sehr mühsam, wenn viele Rechtecke zu erstellen sind. Ein besserer Weg wäre es, die Werte für Höhe und Breite bereits beim Erstellen des Rechtecks angeben zu können.

Python bietet ein grundlegendes Werkzeug, mit dem der Benutzer Text auf dem Bildschirm eingeben kann:

text = raw_input("Höhe des Rechtecks?")
print("Die eingegebene Höhe ist",text)

Dies erfordert jedoch eine laufende Python Konsole, und wenn wir unseren Code von einem Makro aus ausführen, sind wir nicht immer sicher, dass die Python Konsole auf dem Rechner des Benutzers eingeschaltet ist.

Die grafische Benutzeroberfläche ([Graphical User Interface](https://en.wikipedia.org/wiki/Graphical_user_interface), GUI) - sie beinhaltet die Menüs, Symbolleisten, 3D-Ansichten und weitere visuelle Komponenten von FreeCAD - ist darauf ausgelegt, das Programm intuitiv und leicht zugänglich zu machen. Es dient als Verbindung zwischen dem Anwender und der Funktionalität, die FreeCAD zugrunde liegt, und ermöglicht sowohl den gelegentlichen Anwendern als auch den Experten, sich effektiv mit dem Programm auszutauschen.

FreeCADs grafische Benutzerschnittstelle wird mit Hilfe von [Qt](https://en.wikipedia.org/wiki/Qt_(software)) aufgebaut, einem leistungsfähigen und quelloffenen GUI-Werkzeugkasten mit großem Funktionsumfang. Qt stellt entscheidende Bausteine für die Entwicklung von Schnittstellen bereit, wie Dialogfenster, Schaltflächen, Beschriftungen, Texteingabefelder und Ausklappmenüs, die in ihrer Gesamtheit als \"Widgets\" bezeichnet werden. Diese Widgets bilden die Grundlage von FreeCADs Benutzererlebnis.

Einer der Hauptvorteile von Qt ist seine plattformübergreifende Kompatibilität, die es FreeCAD ermöglicht, nahtlos auf verschiedenen Betriebssystemen wie Windows, macOS und Linux zu laufen. Darüber hinaus erleichtert die Flexibilität von Qt Entwicklern die Erweiterung oder Anpassung der FreeCAD-Benutzeroberfläche, entweder durch die Erstellung neuer Symbolleisten und Menüs oder durch die Entwicklung völlig neuer Module, die in die Software integriert werden. Diese Anpassungsfähigkeit stellt sicher, dass FreeCAD sowohl benutzerfreundlich als auch hochgradig erweiterbar bleibt.

Für Benutzer, die an Skripten oder der Entwicklung neuer Tools interessiert sind, bietet die Python-API von FreeCAD auch Zugriff auf viele Qt-Funktionen. Dies bedeutet, dass du nicht nur Aufgaben automatisieren, sondern auch benutzerdefinierte Widgets oder Dialoge erstellen kannst, die direkt in die FreeCAD-Umgebung integriert werden.

Die Qt-Tools sind dank eines Python-Moduls namens [PySide](https://en.wikipedia.org/wiki/PySide) sehr einfach von Python aus zu verwenden. PySide ist die offizielle Python-Bindung für die Qt-Bibliothek und bietet eine nahtlose Möglichkeit, Widgets programmgesteuert zu erstellen und mit ihnen zu interagieren. Entwickler können damit Schnittstellen entwerfen, Benutzereingaben verwalten (z. B. Text aus Eingabefeldern lesen) und Aktionen basierend auf Benutzerinteraktionen definieren, z. B. das Reagieren auf einen Tastendruck. Mit PySide kannst du benutzerdefinierte Dialogfelder, Menüs und Symbolleisten direkt in FreeCAD erstellen und dessen Funktionalität auf eine Weise erweitern, die sich nahtlos in die vorhandene Schnittstelle integriert.

PySide macht es einfach, Benutzeraktionen mit bestimmten Funktionen in deinem Code zu verknüpfen. Du kannst beispielsweise eine Schaltfläche so einrichten, dass beim Drücken ein Skript ausgelöst wird, um einen Befehl auszuführen oder ein Objekt in der 3D-Ansicht zu ändern. Diese interaktive Funktion eröffnet endlose Möglichkeiten zur Anpassung von Arbeitsabläufen und zur Automatisierung sich wiederholender Aufgaben.

Qt bietet auch ein weiteres interessantes Werkzeug namens [Qt Designer](http://doc.qt.io/qt-4.8/designer-manual.html), das heute in eine größere Anwendung namens [Qt Creator](https://en.wikipedia.org/wiki/Qt_Creator) eingebettet ist. Es ermöglicht die grafische Gestaltung von Dialogfeldern und Schnittstellenfenster, anstatt sie manuell zu programmieren. In diesem Kapitel werden wir den Qt Creator verwenden, um ein Paneel-Widget zu entwerfen, das wir im **Aufgaben** -Fenster von FreeCAD verwenden werden. Daher musst der Qt Creator von seiner [offiziellen Seite](https://www.qt.io/ide/) heruntergeladen und installiert werden, wenn man unter Windows oder Mac arbeitet (unter Linux wird er normalerweise in der Softwareverwaltung bereitgestellt).

In der folgenden Übung werden wir zuerst ein Paneel mit Qt Creator erstellen, das nach Längen-, Breiten- und Höhenwerten fragt, dann erstellen wir eine Python Klasse darum herum, die die vom Benutzer eingegebenen Werte aus dem Paneel liest, und erstellen einen Kasten mit den gegebenen Abmessungen. Diese Python Klasse wird dann von FreeCAD verwendet, um das Aufgabenpaneel anzuzeigen und zu steuern:

![](images/Exercise_python_07.jpg )

Beginnen wir mit der Erstellung des Widgets. Den Qt Creator starten, dann den Menüeintrag **Datei → Neue Datei oder Projekt → Qt → Qt → Qt Designer Form → Dialog ohne Schaltflächen** auswählen. Auf **Weiter** klicken, einen Dateinamen zum Speichern angeben, auf **Weiter** klicken, alle Projektfelder auf ihrem Standardwert (\"\") belassen, und **Erstellen** anklicken. Das Aufgabensystem von FreeCAD fügt automatisch OK/Abbrechen-Schaltflächen hinzu, deshalb haben wir hier einen Dialog ohne Schaltflächen gewählt.

![](images/Exercise_python_06.jpg )

-   Die **Beschriftung** in der Liste in der linken Leiste suchen (unter dem Abschnitt Display Widgets) und auf die Leinwand unseres Widgets ziehen. Die zuletzt platzierte Beschriftung doppelt anklicken und ihren Text in **Länge** ändern.
-   Klicke mit der rechten Maustaste auf die Leinwand des Widgets und wähle **Darstellung → Darstellung in einem Gitter**. Dadurch wird unser Widget zu einem Gitter mit derzeit nur einer Zelle, die von unserem ersten Label belegt wird. Wir können nun die nächsten Elemente links, rechts, oben oder unten zu unserem ersten Label hinzufügen, und das Gitter wird automatisch erweitert.
-   Zwei weitere Beschriftungen unterhalb der ersten Beschriftung hinzufügen und ihren Text in Breite und Höhe ändern:

![](images/Exercise_python_08.jpg )

-   Jetzt 3 **Double Spin Box** Widgets neben unseren Etiketten Länge, Breite und Höhe positionieren. Für jedes dieser Widgets in der unteren rechten Leiste, die alle verfügbaren Einstellungen für das ausgewählte Widget anzeigt, wird nach **Suffix** gesucht und deren Suffix auf **mm** gesetzt. FreeCAD hat ein fortschrittlicheres Widget, das mit verschiedenen Einheiten umgehen kann, das aber im Qt Creator nicht standardmäßig zur Verfügung steht (aber [kompiliert](Compile_on_Linux/de#Qt_designer_plugin.md)) werden kann, so dass wir für den Moment eine normale Double-Spin-Box verwenden, und wir fügen das Suffix **mm** hinzu, um sicherzustellen, dass der Benutzer weiß, in welchen Einheiten er arbeitet:

![](images/Exercise_python_09.jpg )

-   Jetzt, wo unser Widget fertig ist, müssen wir uns nur noch um eine letzte Sache kümmern. Da FreeCAD auf dieses Widget zugreifen und die Werte für Länge, Breite und Höhe einlesen muss, müssen wir diesen Widgets richtige Namen geben, damit wir sie aus FreeCAD heraus leicht wiederfinden können. Dazu klicken wir auf jede der Double-Spin-Kästchen und doppelklicken im oberen rechten Fenster auf ihren Objektnamen, und ändern sie in etwas, das wir uns leicht merken können, z.B.: BoxLänge, BoxBreite und BoxHöhe:

![](images/Exercise_python_10.jpg )

-   Speichere die Datei, du kannst Qt Creator jetzt schließen, der Rest wird in Python erledigt.
-   Öffne FreeCAD und erstelle ein neues Makro aus dem Menü **Makro → Makros → Erstellen**
-   Füge den folgenden Code ein. Stelle sicher, dass du den Dateipfad so ändern, dass er mit dem Pfad übereinstimmt, in dem du die in QtCreator erstellte .ui Datei gespeichert hast:


```python
import FreeCAD,FreeCADGui,Part
 
# CHANGE THE LINE BELOW
path_to_ui = "C:\Users\yorik\Documents\dialog.ui"
 
class BoxTaskPanel:
   def __init__(self):
       # this will create a Qt widget from our ui file
       self.form = FreeCADGui.PySideUic.loadUi(path_to_ui)
 
   def accept(self):
       length = self.form.BoxLength.value()
       width = self.form.BoxWidth.value()
       height = self.form.BoxHeight.value()
       if (length == 0) or (width == 0) or (height == 0):
           print("Error! None of the values can be 0!")
           # we bail out without doing anything
           return
       box = Part.makeBox(length,width,height)
       Part.show(box)
       FreeCADGui.Control.closeDialog()
        
panel = BoxTaskPanel()
FreeCADGui.Control.showDialog(panel)
```

Im obigen Code haben wir eine Komfortfunktion **PySideUic.loadUi** aus dem Modul **FreeCADGui** verwendet. Diese Funktion lädt eine .ui-Datei, erzeugt daraus ein Qt Widget und ordnet die Namen zu, so dass wir leicht auf das Unterwidget über deren Namen zugreifen können (z.B.: self.form.BoxLength).

Die \"accept\" Funktion ist ebenfalls eine Annehmlichkeit, die Qt bietet. Wenn es eine \"OK\" Schaltfläche in einem Dialog gibt (was standardmäßig der Fall ist, wenn das FreeCAD Aufgabenpaneel verwendet wird), wird jede Funktion mit dem Namen \"accept\" automatisch ausgeführt, wenn die \"OK\" Schaltfläche gedrückt wird. Auf ähnliche Weise kannst du auch eine \"reject\" Funktion hinzufügen, die ausgeführt wird, wenn der \"Abbrechen\" Knopf gedrückt wird. In unserem Fall haben wir diese Funktion weggelassen, so dass das Drücken von \"Abbrechen\" das Standardverhalten bewirkt (nichts tun und den Dialog schließen).

Wenn wir eine der Annahme- oder Ablehnungsfunktionen implementieren, wird ihr Standardverhalten (nichts tun und schließen) nicht mehr auftreten. Wir müssen also das Aufgabenpaneel selbst schließen. Damit ist dies erledigt:


```python
FreeCADGui.Control.closeDialog() 
```

Sobald wir unser BoxTaskPanel haben, das 1- ein Widget namens \"self.form\" und 2- falls erforderlich, Akzeptieren und Ablehnen von Funktionen hat, können wir damit das Aufgabenpaneel öffnen, was mit diesen beiden letzten Zeilen erledigt ist:


```python
panel = BoxTaskPanel()
 FreeCADGui.Control.showDialog(panel)
```

Beachte, dass das von **PySideUic.loadUi** erzeugte Widget nicht spezifisch für FreeCAD ist, es ist ein normales Qt-Widget, das mit anderen Qt-Werkzeugen verwendet werden kann. Zum Beispiel hätten wir damit ein separates Dialogfeld anzeigen können. Versuche dies in der Python-Konsole von FreeCAD (natürlich unter Verwendung des korrekten Pfades zu deiner .ui Datei):


```python
from PySide import QtGui
 w = FreeCADGui.PySideUic.loadUi("C:\Users\yorik\Documents\dialog.ui")
 w.show()
```

Natürlich haben wir keine Schaltflächen \"OK\" oder \"Abbrechen\" zu unserem Dialog hinzugefügt, da er für die Verwendung in FreeCADs Aufgaben-Fenster vorgesehen ist, das solche Schaltflächen bereits bereit hält. Es gibt also keine Möglichkeit, den Dialog zu schließen (außer auf die Schaltfläche \"Fenster schließen\" zu drücken). Aber die Funktion show() erzeugt einen nicht-modalen Dialog, d.h. sie blockiert nicht den Rest der Schnittstelle. Solange unser Dialog also noch offen ist, können wir die Werte der Felder lesen:


```python
w.BoxHeight.value() 
```

Dies ist für Tests sehr nützlich.

Schliesslich vergiss nicht, dass es im FreeCAD Wiki im Abschnitt [Python Skripten](Power_users_hub/de.md) viel mehr Dokumentation über die Verwendung von Qt Widgets gibt, die ein [Tutorium zur Dialogerstellung](Dialog_creation/de.md), ein spezielles 3-teiliges [PySide Tutorium](PySide/de.md) enthält, das das Thema ausführlich behandelt.

## Maßgebliche Verweise 

-   [Qt Ersteller Dokumentation](https://en.wikipedia.org/wiki/Qt_Creator)
-   [Qt Ersteller installieren](https://www.qt.io/ide/)
-   [FreeCAD Python Dokumentation Skripten](Power_users_hub/de.md)
-   [FreeCAD Dialog Erstellung Tutorium](Dialog_creation/de.md)
-   [FreeCAD PySide Tutorien](PySide/de.md)
-   [PySide Dokumentation](http://srinikom.github.io/pyside-docs/index.html)



---
⏵ [documentation index](../README.md) > [Developer Documentation](Category_Developer Documentation.md) > [Python Code](Category_Python Code.md) > Manual:Creating interface tools/de
