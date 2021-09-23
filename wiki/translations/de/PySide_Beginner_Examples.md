# PySide Beginner Examples/de
## Einführung

Der Zweck dieser Seite ist es, Beispiele auf Anfängerniveau für die [PySide](PySide/de.md) GUI Verwalter (es gibt begleitende Seiten [Zwischen PySide Beispiele](PySide_Intermediate_Examples/de.md) und [Fortgeschrittene PySide Beispiele](PySide_Advanced_Examples/de.md)).

Neulinge in der GUI Programmierung könnten über das Wort \"Widget\" stolpern. Seine Bedeutung außerhalb der Computerwelt wird gewöhnlich wie folgt angegeben

> \"eine kleine Spielerei oder mechanisches Gerät, insbesondere eines, dessen Name unbekannt oder unspezifiziert ist\"

Für GUI Arbeiten wie PySide wird der Begriff \"Widget\" am häufigsten verwendet, um die sichtbaren Elemente der GUI zu bezeichnen - Fenster, Dialoge und Ein-/Ausgabefunktionen. Alle sichtbaren Elemente von PySide werden Widgets genannt, und für diejenigen, die daran interessiert sind, sie stammen alle von einer gemeinsamen Elternklasse ab, nämlich QWidget. Zusätzlich zu den sichtbaren Elementen bietet PySide auch Widgets für Netzwerk-, XML-, Multimedia- und Datenbankintegration.

Ein Widget, das nicht in ein übergeordnetes Widget eingebettet ist, wird als Fenster bezeichnet, und normalerweise haben Fenster einen Rahmen und eine Titelleiste. Die gebräuchlichsten Fenstertypen sind das \"Hauptfenster\" (aus der Klasse QMainWindow) und die verschiedenen Unterklassen des Dialogs (aus der Klasse QDialog). Ein großer Unterschied besteht darin, dass QDialog modal ist (d.h. der Benutzer kann nichts außerhalb des Dialogfensters tun, während es geöffnet ist) und das QMainWindow nicht-modal ist, was es dem Benutzer erlaubt, parallel mit anderen Fenstern zu interagieren.

Dieser Führer ist eine Abkürzungsliste, um ein PySide Programm schnell unter FreeCAD zum Laufen zu bringen. Es ist nicht dazu gedacht, Python oder PySide zu lehren. Einige Websites, die dies tun, sind es:

-   [PySide Tutorium](http://zetcode.com/gui/pysidetutorial/) auf zetcode.com
-   [PySide/PyQt Ttutorium](http://www.pythoncentral.io/series/python-pyside-pyqt-tutorial/) auf PythonCentral.io
-   [PySide 1.0.7 Referenz](http://srinikom.github.io/) auf Srinikom.github.io (beachte, dass dies eine Referenz und kein Tutorium ist)

## Import Anweisung 

PySide wird standardmäßig nicht mit Python geladen, es muss vor der Verwendung angefordert werden. Der folgende Befehl: 
```python
from PySide import QtCore
from PySide import QtGui
``` bewirkt, dass die 2 Teile von PySide geladen werden - QtGui enthält Klassen zur Verwaltung der grafischen Benutzeroberfläche, während QtCore Klassen enthält, die sich nicht direkt auf die Verwaltung der GUI beziehen (z.B. Timer und Geometrie). Obwohl es möglich ist, nur das zu importieren, was benötigt wird, werden im Allgemeinen beide benötigt und beide importiert.

Die Importangaben werden in den folgenden Schnipseln nicht wiederholt; es wird davon ausgegangen, dass dies jeweils am Anfang geschieht.

## Einfachstes Beispiel 

Die einfachste Interaktion mit PySide besteht darin, dem Benutzer eine Nachricht zu präsentieren, die er nur akzeptieren kann: 
```python
reply = QtGui.QMessageBox.information(None,"","Houston, we have a problem")
```

![](images/PySideScreenSnapshot5.jpg )

## Ja oder Keine Abfrage 

Die nächst einfachste Interaktion ist die Frage nach einer Ja/Nein Antwort: 
```python
reply = QtGui.QMessageBox.question(None, "", "This is your chance to answer, what do you think?",
         QtGui.QMessageBox.Yes {{!``` QtGui.QMessageBox.No, QtGui.QMessageBox.No) if reply == QtGui.QMessageBox.Yes:

        # this is where the code relevant to a 'Yes' answer goes
        pass

if reply == QtGui.QMessageBox.No:

        # this is where the code relevant to a 'No' answer goes
        pass

}}

![](images/PySideScreenSnapshot6.jpg )

## Textabfrage eingeben 

Der nächste Codeschnipsel fragt den Benutzer nach einem Stück Text - beachte, dass dies wirklich jede Taste auf der Tastatur sein kann: 
```python
reply = QtGui.QInputDialog.getText(None, "Ouija Central","Enter your thoughts for the day:")
if reply[1]:
    # user clicked OK
    replyText = reply[0]
else:
    # user clicked Cancel
    replyText = reply[0] # which will be "" if they clicked Cancel
```

![](images/PySideScreenSnapshot7.jpg )

Denke daran, dass selbst wenn der Benutzer nur Ziffern eingibt, z.B. \"1234\", es sich um Zeichenketten handelt, die mit einem der folgenden Verfahren in eine Zahlendarstellung umgewandelt werden müssen: 
```python
anInteger = int(userInput) # to convert to an integer from a string representation

aFloat = float(userInput) # to convert to a float from a string representation
```

## Mehr als 2 Schaltflächen 

Das letzte Beispiel für das Anfängerniveau zeigt, wie man einen Dialog mit einer beliebigen Anzahl von Schaltflächen aufbaut. Dieses Beispiel ist programmtechnisch zu komplex, um von einer einzigen Python Anweisung aus aufgerufen zu werden, daher sollte es in gewisser Weise auf der nächsten Seite, die PySide Medium Beispiele enthält, aufgeführt werden. Aber andererseits ist dies oft alles, was benötigt wird, ohne sich in komplexe GUI Definitionen zu vertiefen, so dass der Code am Ende der Seite dieser PySide Einsteigerseite und nicht am Anfang der folgenden PySide Medium Seite platziert wird. 
```python
from PySide import QtGui, QtCore

class MyButtons(QtGui.QDialog):
    """"""
    def __init__(self):
        super(MyButtons, self).__init__()
        self.initUI()
    def initUI(self):      
        option1Button = QtGui.QPushButton("Option 1")
        option1Button.clicked.connect(self.onOption1)
        option2Button = QtGui.QPushButton("Option 2")
        option2Button.clicked.connect(self.onOption2)
        option3Button = QtGui.QPushButton("Option 3")
        option3Button.clicked.connect(self.onOption3)
        option4Button = QtGui.QPushButton("Option 4")
        option4Button.clicked.connect(self.onOption4)
        option5Button = QtGui.QPushButton("Option 5")
        option5Button.clicked.connect(self.onOption5)
        #
        buttonBox = QtGui.QDialogButtonBox()
        buttonBox = QtGui.QDialogButtonBox(QtCore.Qt.Horizontal)
        buttonBox.addButton(option1Button, QtGui.QDialogButtonBox.ActionRole)
        buttonBox.addButton(option2Button, QtGui.QDialogButtonBox.ActionRole)
        buttonBox.addButton(option3Button, QtGui.QDialogButtonBox.ActionRole)
        buttonBox.addButton(option4Button, QtGui.QDialogButtonBox.ActionRole)
        buttonBox.addButton(option5Button, QtGui.QDialogButtonBox.ActionRole)
        #
        mainLayout = QtGui.QVBoxLayout()
        mainLayout.addWidget(buttonBox)
        self.setLayout(mainLayout)
        # define window     xLoc,yLoc,xDim,yDim
        self.setGeometry(   250, 250, 0, 50)
        self.setWindowTitle("Pick a Button")
        self.setWindowFlags(QtCore.Qt.WindowStaysOnTopHint)
    def onOption1(self):
        self.retStatus = 1
        self.close()
    def onOption2(self):
        self.retStatus = 2
        self.close()
    def onOption3(self):
        self.retStatus = 3
        self.close()
    def onOption4(self):
        self.retStatus = 4
        self.close()
    def onOption5(self):
        self.retStatus = 5
        self.close()

def routine1():
    print 'routine 1'

form = MyButtons()
form.exec_()
if form.retStatus==1:
    routine1()
elif form.retStatus==2:
    routine2()
elif form.retStatus==3:
    routine3()
elif form.retStatus==4:
    routine4()
elif form.retStatus==5:
    routine5()

``` Jedes zu testende Codestück würde sich in einer Funktion mit dem Namen \'routine1()\', \'routine2()\' usw. befinden. Es können so viele Schaltflächen verwendet werden, wie auf den Bildschirm passen. Folge den Mustern im Codebeispiel und füge bei Bedarf zusätzliche Knöpfe hinzu - das Dialogfeld wird seine Breite entsprechend der Bildschirmbreite einstellen.

![](images/PySideScreenSnapshot8.jpg )

Es gibt eine Codezeile: 
```python
buttonBox = QtGui.QDialogButtonBox(QtCore.Qt.Horizontal)
``` was dazu führt, dass die Schaltflächen in einer horizontalen Linie liegen. Um sie in eine vertikale Linie zu setzen, ändere die zu lesende Zeile des Codes: 
```python
buttonBox = QtGui.QDialogButtonBox(QtCore.Qt.Vertical)
```


{{Powerdocnavi

}} 

[Category:Developer Documentation](Category:Developer_Documentation.md) [Category:Python Code](Category:Python_Code.md)

---
[documentation index](../README.md) > [Developer Documentation](Category:Developer Documentation.md) > PySide Beginner Examples/de
