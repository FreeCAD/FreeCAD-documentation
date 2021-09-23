# Dialog creation/de



{{TOCright}}

## Einführung

Auf dieser Seite werden wir zeigen, wie man mit [Qt Designer](http://qt-project.org/doc/qt-4.8/designer-manual.html), Qt\'s offiziellem Werkzeug für die Gestaltung von Oberflächen, eine einfache grafische Oberfläche erstellt; der Dialog wird in [Python](Python/de.md) Code umgewandelt und dann innerhalb von FreeCAD verwendet. Wir gehen davon aus, dass der Benutzer weiß, wie man [Python](Python/de.md) allgemein bearbeitet und ausführt.

In diesem Beispiel ist die gesamte Oberfläche in [Python](Python/de.md) definiert. Obwohl dies bei kleinen Schnittstellen möglich ist, empfiehlt es sich bei größeren Schnittstellen, die erstellten {{FileName|.ui}} Dateien direkt in das Programm zu laden. Siehe [Obeflächenerstellung mit UI Dateien](Interface_creation_with_UI_files/de.md) für weitere Informationen.

<img alt="" src=images/FreeCAD_creating_interfaces.svg  style="width:600px;"> *Zwei allgemeine Methoden zur Erstellung von Oberflächen, durch Einfügen der Schnittstelle in die Python Datei oder durch die Verwendung von `.ui* Dateien.`

## Gestalten des Dialogs 

In CAD Anwendungen ist es sehr wichtig, eine gute UI (Benutzeroberfläche) zu entwerfend. Beinahe alles, das der Benutzer tun wird, wird über ein Teil der Oberfläche passieren: das Lesen von Dialog Kästen, drücken von Knöpfen, die Auswahl zwischen Piktogrammen, usw. Es ist also sehr wichtig, sich genau zu überlegen, was du tun willst, wie der Benutzer sich verhalten soll und wie der Ablauf deiner Aktion aussehen soll.

Ein paar Konzepte sollte man bei der Gestaltung der Oberfläche kennen:

-   [Dialoge](http://de.wikipedia.org/wiki/Dialogfenster): Ein modaler Dialog erscheint auf Ihrem Schirm, unterbricht die Handlung des Hauptfensters, zwingt den Benutzer auf den Dialog zu antworten, während ein nichtmodaler Dialog Sie nicht hindert, am Hauptfenster weiter zu arbeiten. In einigen Fällen ist der erste besser, in anderen Fällen nicht.
-   Erkennen, was erforderlich ist und was optional: Stellen Sie sicher, dass der Benutzer weiß, was er tun muss. Etikettieren Sie alles mit der richtigen Beschreibung, verwenden Sie tooltips usw.
-   Die Trennung von Befehlen und Parametern: Das wird gewöhnlich mit Knöpfen und Texteingabefeldern getan. Der Benutzer weiß, dass das Klicken eines Knopfs eine Handlung erzeugen wird, indem er einen Wert innerhalb eines Textfeldes ändert, wird irgendwo ein Parameter geändert. Heutzutage aber wissen Benutzer gewöhnlich gut, was ein Knopf ist, was ein Eingangsfeld usw ist. Das Schnittstellen-Werkzeug Qt, das wir verwenden, ist eines der modernsten Werkzeuge und wir werden uns nicht viel darum sorgen müssen, Dinge verständlich zu machen, da sie bereits in sich selbst sehr klar sein werden.

Nachdem wir gut definiert haben, was wir tun werden, ist es Zeit, den Qt-Designer zu öffnen. Lassen Sie uns einen sehr einfachen Dialog entwerfen:

![](images/Qttestdialog.jpg )

Wir werden dann mit diesem Dialog in FreeCAD eine schöne rechteckige Ebene erzeugen. Vielleicht finden Sie es nicht sehr nützlich, nette rechteckige Fläche zu produzieren, aber es wird leicht sein, sie später zu ändern, um komplexere Dinge zu tun. Wenn Sie es öffnen, sieht Qt-Designer wie folgt aus:

![](images/Qtdesigner-screenshot.jpg )

## Erstellen des Dialogs 

Qt Designer ist sehr einfach zu benutzen. Auf der linken Leiste hast du Elemente, die auf dein Widget gezogen werden können. Auf der rechten Seite hast du Eigenschaftspaneels, die alle Arten von editierbaren Eigenschaften der ausgewählten Elemente anzeigen. Beginne also mit der Erstellung eines neuen Widgets.

1.  Wähle \"Dialog ohne Schaltflächen\", da wir die Standardschaltflächen **OK**/**Abbrechen** nicht wollen.
2.  Wir brauchen **Labels** (Beschriftungen). Labels sind einfache Textzeichenfolgen, die auf deinem Widget erscheinen, um den Endbenutzer zu informieren. Wenn du ein Label auswählst, beachte, dass auf der rechten Seite verschiedene Eigenschaften erscheinen, die du ändern kannst, wie z.B.: Schriftstil, Höhe, usw\... Lass uns also 3 separate Label auf unser Widget ziehen:
    -   Ein Label für den Titel
    -   Ein weiteres Label zum Schreiben von \"**Height**\"
    -   Ein weiteres Label zum Schreiben von \"**Width**\"
3.  Wir brauchen jetzt LineEdits (eigentlich 2 davon). Ziehe zwei davon auf das Widget. **LineEdits** sind Textfelder, die der Endbenutzer ausfüllen kann. Wir brauchen also einen LineEdit für die *Höhe* und einen für die *Breite*. Auch hier können wir Eigenschaften bearbeiten. Warum nicht z.B. einen Standardwert setzen, sagen wir z.B.: 1,00 für jedes. Auf diese Weise werden beide Werte bereits ausgefüllt sein, wenn der Benutzer den Dialog sieht. Wenn der Endbenutzer zufrieden ist, kann er direkt auf die Schaltfläche drücken und so wertvolle Zeit sparen.
4.  Als nächstes können wir einen **PushButton** (Druckknopf) hinzufügen. Dies ist die Schaltfläche, die der Endbenutzer drücken muss, nachdem er beide Felder ausgefüllt hat.

**Hinweis:** dass wir hier sehr einfache Bedienelemente gewählt haben. Qt hat viel mehr Optionen, zum Beispiel könnte man **Spinboxes** anstelle von **LineEdits** verwenden, usw\... Schaudir an, was verfügbar ist, erkunde\... Du wirst sicher andere Ideen haben.

Das ist soweit alles, was wir im Qt Designer tun müssen. Eine letzte Sache noch: Benennen wir alle unsere Elemente mit einfacheren Namen um, damit sie in unseren Skripten leichter zu identifizieren sind:

![](images/Qtpropeditor.jpg )

## Umwandeln unseres Dialogs zu Python 

Jetzt werden wir unser Widget irgendwo speichern. Er wird als .ui Datei gespeichert, die wir einfach mittels pyuic zu einem Python Skript wandeln werden. Unter Windows ist das pyuic Programm meistens mit pyqt gebündelt (zu überprüfen), auf Linux weirst du es wahrscheinlich extra mit deinem Paketmanager installieren müssen (auf Debian-basierten Systemen, ist es ein Teil des pyqt4-dev-tools Pakets). Für die Konvertierung musst du ein Terminalfenster (oder ein Fenster der Eingabeaufforderung unter Windows) öffnen, in welchem du zu deiner .ui Datei navigierst und dort dann folgendes eingibst: 
```python
pyuic mywidget.ui > mywidget.py
``` Unter Windows befindet sich pyuic.py in \"C:\\Python27\\Lib\\site-Pakete\\PyQt4\\uic\\pyuic.py\". Erstelle für die Umwandlung eine Batchdatei mit dem Namen \"compQt4.bat\": 
```python
@"C:\Python27\python" "C:\Python27\Lib\site-packages\PyQt4\uic\pyuic.py" -x %1.ui > %1.py
``` In der DOS Konsole tippe ohne Erweiterung 
```python
compQt4 myUiFile
```

Unter macOS kannst du mit diesen Befehlen (pip erforderlich) die entsprechende Version von Qt bzw. Pyside ermitteln (die gleiche, die intern in FreeCAD 0.19 benutzt wird) 
```python
python3 -m pip install pyqt5
python3 -m pip install pySide2
``` Dies wird uic im Verzeichnis \"/Library/Frameworks/Python.framework/Versions/3.7/lib/python3.7/site-packages/PySide2/uic\" installieren und Designer in \"/Library/Frameworks/Python.framework/Versions/3.7/lib/python3.7/site-packages/PySide2/Designer.app\". Der Einfachheit halber kannst du einen Link auf uic in /usr/local/bin erstellen, um es einfach per uic -g python \... aufzurufen anstatt den ganzen Pfad zum Programm einzutippen und einen Link zu Designer, um ihn im Mac-Applikationsverzeichnis aufzurufen mit 
```python
sudo ln -s /Library/Frameworks/Python.framework/Versions/3.7/lib/python3.7/site-packages/PySide2/uic /usr/local/bin
ln -s /Library/Frameworks/Python.framework/Versions/3.7/lib/python3.7/site-packages/PySide2/Designer.app /Applications
```

In Linux: Zu Tun

Nachdem sich FreeCAD nach v0.13 zunehmend von PyQt zugunsten von [PySide](http://qt-project.org/wiki/PySide) entfernt hat (Wähle deine PySide Installation [PySide bauen](http://pyside.readthedocs.org/en/latest/building/)), um die Datei auf der Basis von PySide zu erstellen, musst du jetzt verwenden:


```python
pyside-uic mywidget.ui -o mywidget.py
```

Unter Windows ist uic.py in \"C:\\Python27\\Lib\\site-packages\\PySide\\scripts\\\" zu finden. Zum Erstellen der Batchdatei \"compSide.bat\": 
```python
@"C:\Python27\python" "C:\Python27\Lib\site-packages\PySide\scripts\uic.py" %1.ui > %1.py
``` In die DOS Konsole tippe ohne Erweiterung 
```python
compSide myUiFile
``` In Linux: Zu Tun

Auf einigen Systemen wird das Programm pyuic4 statt pyuic genannt. Dadurch wird die .ui Datei einfach in ein Python Skript umgewandelt. Wenn wir die Datei mywidget.py öffnen, ist ihr Inhalt sehr leicht zu verstehen: 
```python
from PySide import QtCore, QtGui

class Ui_Dialog(object):
    def setupUi(self, Dialog):
        Dialog.setObjectName("Dialog")
        Dialog.resize(187, 178)
        self.title = QtGui.QLabel(Dialog)
        self.title.setGeometry(QtCore.QRect(10, 10, 271, 16))
        self.title.setObjectName("title")
        self.label_width = QtGui.QLabel(Dialog)
        ...

        self.retranslateUi(Dialog)
        QtCore.QMetaObject.connectSlotsByName(Dialog)

   def retranslateUi(self, Dialog):
        Dialog.setWindowTitle(QtGui.QApplication.translate("Dialog", "Dialog", None, QtGui.QApplication.UnicodeUTF8))
        self.title.setText(QtGui.QApplication.translate("Dialog", "Plane-O-Matic", None, QtGui.QApplication.UnicodeUTF8))
        ...
``` Wie du siehst, hat es eine sehr einfache Struktur: eine Klasse genannt Ui\_Dialog wird erstellt, die die Elemente der Benutzeroberfläche unseres Widgets speichert. Diese Klasse hat zwei Methoden, eine für die Einrichtung des Widgets und eine für die Übersetzung ihres Inhalts, was ein Teil des allgemeinen Qt Mechanismus für die Übersetzung von Oberflächenelementen ist. Das Einrichtungsverfahren erzeugt einfach eins nach dem anderen die Widgets, wie wir sie in Qt Designer festgelegt haben und setzt ihre Optionen, die wir ebenfalls gewählt haben. Dann wird die ganze Schnittstelle schließlich übersetzt, die Slots werden verbunden (wir werden darüber später sprechen).

Wir können jetzt ein neues Widget erstellen und diese Klasse verwenden, um seine Oberfläche zu schaffen. Wir können bereits unser Widget in Aktion sehen, indem wir unsere mywidget.py Datei an einem Ort speichern, wo FreeCAD es findet (im FreeCAD bin Verzeichnis, oder in einem der Mod Unterverzeichnisse), und dann im FreeCAD Python Interpreter eintippen: 
```python
from PySide import QtGui
import mywidget
d = QtGui.QWidget()
d.ui = mywidget.Ui_Dialog()
d.ui.setupUi(d)
d.show()
``` Und unser Dialog wird erscheinen! Beachte, dass unser Python Interpreter immer noch arbeitet, wir haben einen nichtmodalen Dialog. Um es zu abzuschließen, können wir (abgesehen von einem Klick auf das Schließen Symbol, natürlich) eingeben: 
```python
d.hide()
```

## Unseren Dialog etwas tun lassen 

Nun, da wir unseren Dialog ein- und ausblenden können, müssen wir nur noch einen letzten Teil hinzufügen: Damit er etwas bewirkt! Wenn du ein wenig mit dem Qt Designer spielst, wirst du schnell einen ganzen Abschnitt namens \"Signals and Slots\" entdecken. Im Grunde funktioniert es so: Elemente auf deinen Widgets (in der Qt Terminologie sind diese Elemente selbst Widgets) können Signale senden. Diese Signale unterscheiden sich je nach Widget Typ. Zum Beispiel kann eine Taste ein Signal senden, wenn sie gedrückt wird und wenn sie losgelassen wird. Diese Signale können mit Slots verbunden werden, was eine spezielle Funktionalität anderer Widgets sein kann (z.B. hat ein Dialog einen \"Schließ\" Slot, mit dem du das Signal von einer Schaltfläche zum Schließen verbinden kannst), oder es können benutzerdefinierte Funktionen sein. Die [PyQt Referenzdokumentation](http://www.riverbankcomputing.co.uk/static/Docs/PyQt4/html/classes.html) listet alle qt Widgets auf, was sie können, welche Signale sie senden können, usw..

Was wir hier tun werden, ist eine neue Funktion zu erstellen, die eine Ebene erzeugt, beruhend auf Höhe und Breite, und in Verbindung steht diese Funktion mit dem gedrückt Signal, das unser \"Create\" Knopf abgibt. Also lass uns mit dem Importieren unserer FreeCAD Module beginnen, durch setzen der folgenden Zeile an den Anfang des Skripts, wo wir bereits QtCore und QtGui importieren: 
```python
import FreeCAD, Part
``` Dann lass uns eine neue Funktion zu unserer Ui\_Dialog Klasse hinzufügen: 
```python
def createPlane(self):
    try:
        # first we check if valid numbers have been entered
        w = float(self.width.text())
        h = float(self.height.text())
    except ValueError:
        print("Error! Width and Height values must be valid numbers!")
    else:
        # create a face from 4 points
        p1 = FreeCAD.Vector(0,0,0)
        p2 = FreeCAD.Vector(w,0,0)
        p3 = FreeCAD.Vector(w,h,0)
        p4 = FreeCAD.Vector(0,h,0)
        pointslist = [p1,p2,p3,p4,p1]
        mywire = Part.makePolygon(pointslist)
        myface = Part.Face(mywire)
        Part.show(myface)
        self.hide()
``` Dann müssen wir Qt mitteilen, dass die Schaltfläche mit der Funktion verbunden werden soll, indem wir die folgende Zeile unmittelbar vor QtCore.QMetaObject.connectSlotsByName(Dialog) setzen: 
```python
QtCore.QObject.connect(self.create,QtCore.SIGNAL("pressed()"),self.createPlane)
``` Dies verbindet, wie du siehst, das pressed() Signal unseres create Objekts (die Schaltfläche \"Create!\") mit einem Slot namens createPlane, den wir gerade definiert haben. Das war\'s! Als letzten Schliff können wir nun noch eine kleine Funktion zum Erstellen des Dialogs hinzufügen, die einfacher aufzurufen sein wird. Außerhalb der Klasse Ui\_Dialog fügen wir diesen Code hinzu: 
```python
class plane():
   def __init__(self):
       self.d = QtGui.QWidget()
       self.ui = Ui_Dialog()
       self.ui.setupUi(self.d)
       self.d.show()
``` (Python Erinnerung: Die \_\_init\_\_ Methode einer Klasse wird automatisch ausgeführt, wenn ein neues Objekt erzeugt wird!) Dann brauchen wir von FreeCAD aus nur folgendes zu tun: 
```python
import mywidget
myDialog = mywidget.plane()
``` Das ist alles, Leute\... Jetzt kannst du alle möglichen Dinge ausprobieren, wie z.B. dein Widget in die FreeCAD Oberfläche einzufügen (siehe die [Code Schnipsel](Code_snippets/de.md) Seite), oder viel fortgeschrittenere, eigene Werkzeuge zu erstellen, indem du andere Elemente auf deinem Widget verwendest.

## Das komplette Skript 

Dies ist das vollständige Skript, als Referenz: 
```python
# Form implementation generated from reading ui file 'mywidget.ui'
#
# Created: Mon Jun  1 19:09:10 2009
#      by: PyQt4 UI code generator 4.4.4
# Modified for PySide 16:02:2015 
# WARNING! All changes made in this file will be lost!

from PySide import QtCore, QtGui
import FreeCAD, Part 

class Ui_Dialog(object):
   def setupUi(self, Dialog):
       Dialog.setObjectName("Dialog")
       Dialog.resize(187, 178)
       self.title = QtGui.QLabel(Dialog)
       self.title.setGeometry(QtCore.QRect(10, 10, 271, 16))
       self.title.setObjectName("title")
       self.label_width = QtGui.QLabel(Dialog)
       self.label_width.setGeometry(QtCore.QRect(10, 50, 57, 16))
       self.label_width.setObjectName("label_width")
       self.label_height = QtGui.QLabel(Dialog)
       self.label_height.setGeometry(QtCore.QRect(10, 90, 57, 16))
       self.label_height.setObjectName("label_height")
       self.width = QtGui.QLineEdit(Dialog)
       self.width.setGeometry(QtCore.QRect(60, 40, 111, 26))
       self.width.setObjectName("width")
       self.height = QtGui.QLineEdit(Dialog)
       self.height.setGeometry(QtCore.QRect(60, 80, 111, 26))
       self.height.setObjectName("height")
       self.create = QtGui.QPushButton(Dialog)
       self.create.setGeometry(QtCore.QRect(50, 140, 83, 26))
       self.create.setObjectName("create")

       self.retranslateUi(Dialog)
       QtCore.QObject.connect(self.create,QtCore.SIGNAL("pressed()"),self.createPlane)
       QtCore.QMetaObject.connectSlotsByName(Dialog)

   def retranslateUi(self, Dialog):
       Dialog.setWindowTitle("Dialog")
       self.title.setText("Plane-O-Matic")
       self.label_width.setText("Width")
       self.label_height.setText("Height")
       self.create.setText("Create!")
       print("tyty")
   def createPlane(self):
       try:
           # first we check if valid numbers have been entered
           w = float(self.width.text())
           h = float(self.height.text())
       except ValueError:
           print("Error! Width and Height values must be valid numbers!")
       else:
           # create a face from 4 points
           p1 = FreeCAD.Vector(0,0,0)
           p2 = FreeCAD.Vector(w,0,0)
           p3 = FreeCAD.Vector(w,h,0)
           p4 = FreeCAD.Vector(0,h,0)
           pointslist = [p1,p2,p3,p4,p1]
           mywire = Part.makePolygon(pointslist)
           myface = Part.Face(mywire)
           Part.show(myface)

class plane():
  def __init__(self):
      self.d = QtGui.QWidget()
      self.ui = Ui_Dialog()
      self.ui.setupUi(self.d)
      self.d.show()

```

## Weitere Beispiele 

-   [Dialogerstellung mit verschiedenen Widgets](Dialog_creation_with_various_widgets/de.md) mit `QPushButton`, `QLineEdit`, `QCheckBox`, `QRadioButton`, und anderen.
-   [Dialogerstellung Lesen und Schreiben von Dateien](Dialog_creation_reading_and_writing_files/de.md) mit `QFileDialog`.
-   [Dialogerstellung Farben festlegen](Dialog_creation_setting_colors/de.md) mit `QColorDialog`.
-   [Dialogerstellung Bild und animierte GIF](Dialog_creation_image_and_animated_GIF/de.md) mit `QLabel` und `QMovie`.
-   [PySide Verwendungsschnipsel](PySide_usage_snippets/de.md).
-   [Qt Beispiel](Qt_Example/de.md)

## Relevante Verweise 

-   [Handbuch:Erstellen von Oberflächenwerkzeugen](Manual:Creating_interface_tools/de.md)
-   [Oberflächenerstellung mit UI Dateien](Interface_creation_with_UI_files/de.md)


{{Powerdocnavi

}} 

[Category:Developer Documentation](Category:Developer_Documentation.md) [Category:Python Code](Category:Python_Code.md)
