# Manual:Creating interface tools/de
{{Manual:TOC/de}}

In den letzten beiden Kapiteln haben wir gesehen, wie man [Teilgeometrie erstellt](Manual:Creating_and_manipulating_geometry/de.md) und [parametrische Objekte erstellt](Manual:Creating_parametric_objects/de.md). Ein letztes Teil fehlt noch, um die volle Kontrolle über FreeCAD zu erhalten: Erstellen von Werkzeugen, die mit dem Benutzer interagieren.

In vielen Situationen ist es nicht sehr benutzerfreundlich, ein Objekt mit Nullwerten zu konstruieren, wie wir es im vorigen Kapitel mit dem Rechteck getan haben, und den Benutzer dann aufzufordern, die Werte für Höhe und Breite im Eigenschaftenpaneel einzugeben. Dies funktioniert bei einer sehr kleinen Anzahl von Objekten, wird aber sehr mühsam, wenn du viele Rechtecke zu erstellen hast. Ein besserer Weg wäre es, die Werte für Höhe und Breite bereits beim Erstellen des Rechtecks angeben zu können.

Python bietet ein grundlegendes Werkzeug, mit dem der Benutzer Text auf dem Bildschirm eingeben kann:

text = raw_input("Höhe des Rechtecks?")
print("Die eingegebene Höhe ist",text)

Dies erfordert jedoch eine laufende Python Konsole, und wenn wir unseren Code von einem Makro aus ausführen, sind wir nicht immer sicher, dass die Python Konsole auf dem Rechner des Benutzers eingeschaltet ist.

Die [Graphische Benutzeroberfläche](https://en.wikipedia.org/wiki/Graphical_user_interface), oder GUI, d.h. alle Teile von FreeCAD, die auf deinem Bildschirm angezeigt werden (das Menü, die Werkzeugleisten, die 3D Ansicht, usw.), sind alle zu diesem Zweck da: zur Interaktion mit dem Benutzer. Die Schnittstelle von FreeCAD ist mit [Qt](https://en.wikipedia.org/wiki/Qt_(software)) aufgebaut, einem sehr verbreiteten Open Source GUI Werkzeugsatz, der eine breite Palette von Werkzeugen wie Dialogfelder, Schaltflächen, Beschriftungen, Texteingabefelder oder Auswahlmenüs bietet. Diese werden alle allgemein als \"Widgets\" bezeichnet.

Die Qt Werkzeuge sind von Python aus dank eines Python Moduls namens [Pyside](https://en.wikipedia.org/wiki/PySide) sehr einfach zu benutzen (es gibt auch mehrere andere Python Module, um von Python aus mit Qt zu kommunizieren). Dieses Modul erlaubt es dir, Widgets zu erstellen und mit ihnen zu interagieren, zu lesen, was der Benutzer mit ihnen gemacht hat (was in Textfeldern ausgefüllt wurde) oder Dinge zu tun, wenn z.B. eine Schaltfläche gedrückt wurde.

Qt bietet auch ein weiteres interessantes Werkzeug namens [Qt Designer](http://doc.qt.io/qt-4.8/designer-manual.html), das heute in eine größere Anwendung namens [Qt Creator](https://en.wikipedia.org/wiki/Qt_Creator) eingebettet ist. Es ermöglicht die grafische Gestaltung von Dialogfeldern und Schnittstellen Paneels, anstatt sie manuell zu programmieren. In diesem Kapitel werden wir den Qt Creator verwenden, um ein Paneel Widget zu entwerfen, das wir im **Aufgaben** Paneel von FreeCAD verwenden werden. Daher musst du den Qt Creator von seiner [offiziellen Seite](https://www.qt.io/ide/) herunterladen und installieren, wenn du unter Windows oder Mac arbeitest (unter Linux wird er normalerweise in deiner Software Verwaltungsanwendung verfügbar sein).

In der folgenden Übung werden wir zuerst ein Paneel mit Qt Creator erstellen, das nach Längen-, Breiten- und Höhenwerten fragt, dann erstellen wir eine Python Klasse darum herum, die die vom Benutzer eingegebenen Werte aus dem Paneel liest, und erstellen einen Kasten mit den gegebenen Abmessungen. Diese Python Klasse wird dann von FreeCAD verwendet, um das Aufgabenpaneel anzuzeigen und zu steuern:

![](images/Exercise_python_07.jpg )

Beginnen wir mit der Erstellung des Widgets. Starte Qt Creator, dann Menü **Datei → Neue Datei oder Projekt → Dateien und Klassen → Qt → Qt → Qt Designer Form → Dialog ohne Schaltflächen**. Klicke auf **Weiter**, gib einen Dateinamen zum Speichern an, klicke auf **Weiter**, belasse alle Projektfelder auf ihrem Standardwert (\"\"), und **Erstellen**. Das Aufgabensystem von FreeCAD fügt automatisch OK/Abbrechen-Schaltflächen hinzu, deshalb haben wir hier einen Dialog ohne Schaltflächen gewählt.

![](images/Exercise_python_06.jpg )

-   Suche die **Beschriftung** in der Liste in der linken Leiste und ziehe sie auf die Leinwand unseres Widgets. Doppelklicke auf die zuletzt platzierte Beschriftung und ändere ihren Text in **Länge**.
-   Klicke mit der rechten Maustaste auf die Leinwand des Widgets und wähle **Darstellung → Darstellung in einem Gitter**. Dadurch wird unser Widget zu einem Gitter mit derzeit nur einer Zelle, die von unserem ersten Label belegt wird. Wir können nun die nächsten Elemente links, rechts, oben oder unten zu unserem ersten Label hinzufügen, und das Gitter wird automatisch erweitert.
-   Füge zwei weitere Beschriftungen unterhalb der ersten Beschriftung hinzu und ändere ihren Text in Breite und Höhe:

![](images/Exercise_python_08.jpg )


<div class="mw-translate-fuzzy">

-   Platziere jetzt 3 **Double Spin Box** Widgets neben unseren Etiketten Länge, Breite und Höhe. Suche für jedes dieser Widgets in der unteren rechten Leiste, die alle verfügbaren Einstellungen für das ausgewählte Widget anzeigt, nach **Suffix** und setze deren Suffix auf **mm**. FreeCAD hat ein fortschrittlicheres Widget, das verschiedene Einheiten handhaben kann, das aber im Qt Creator nicht standardmäßig verfügbar ist (aber [Kompiliert](Compile_on_Linux/Unix/de#Qt_designer_plugin.md)), so dass wir für den Moment eine Standard Double Spin Box verwenden werden, und wir fügen das Suffix **mm** hinzu, um sicherzustellen, dass der Benutzer weiß, in welchen Einheiten er arbeitet:


</div>

![](images/Exercise_python_09.jpg )

-   Jetzt, wo unser Widget fertig ist, müssen wir uns nur noch um eine letzte Sache kümmern. Da FreeCAD auf dieses Widget zugreifen und die Werte für Länge, Breite und Höhe einlesen muss, müssen wir diesen Widgets richtige Namen geben, damit wir sie aus FreeCAD heraus leicht wiederfinden können. Klicke auf jede der Double Spin Kästchen und doppelklicke im oberen rechten Fenster auf ihren Objektnamen, und ändere sie z.B. in etwas, das du dir leicht merken kannst: BoxLänge, BoxBreite und BoxHöhe:

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

Im obigen Code haben wir eine Komfortfunktion (PySideUic.loadUi) aus dem FreeCADGui Modul verwendet. Diese Funktion lädt eine .ui-Datei, erzeugt daraus ein Qt Widget und ordnet die Namen zu, so dass wir leicht auf das Unterwidget über deren Namen zugreifen können (z.B.: self.form.BoxLength).

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

Beachte, dass das von PySideUic.loadUi erzeugte Widget nicht spezifisch für FreeCAD ist, es ist ein Standard Qt Widget, das mit anderen Qt Werkzeugen verwendet werden kann. Zum Beispiel hätten wir damit ein separates Dialogfeld anzeigen können. Versuche dies in der Python Konsole von FreeCAD (natürlich unter Verwendung des korrekten Pfades zu deiner .ui Datei):


```python
from PySide import QtGui
 w = FreeCADGui.PySideUic.loadUi("C:\Users\yorik\Documents\dialog.ui")
 w.show()
```

Natürlich haben wir keine \"OK\" oder \"Abbrechen\" Schaltflächen zu unserem Dialog hinzugefügt, da er für die Verwendung im FreeCAD Aufgabenpaneel vorgesehen ist, das solche Schaltflächen bereits anbietet. Es gibt also keine Möglichkeit, den Dialog zu schließen (außer auf die Schaltfläche \"Fenster schließen\" zu drücken). Aber die Funktion show() erzeugt einen nicht-modalen Dialog, d.h. sie blockiert nicht den Rest der Schnittstelle. Solange unser Dialog also noch offen ist, können wir die Werte der Felder lesen:


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
![](images/Right_arrow.png) [documentation index](../README.md) > [Developer Documentation](Category_Developer Documentation.md) > [Python Code](Category_Python Code.md) > Manual:Creating interface tools/de
