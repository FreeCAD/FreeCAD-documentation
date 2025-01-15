# PySide Advanced Examples/de
## Einführung

Der Zweck dieser Seite ist es, Beispiele auf fortgeschrittenem Niveau für den [PySide](PySide/de.md)-GUI-Verwalter zu behandeln (es gibt begleitende Seiten [PySide Beispiele für Anfänger](PySide_Beginner_Examples/de.md) und [PySide Weiterführende Beispiele](PySide_Intermediate_Examples/de.md)).

Durch Verwendung des PySide Moduls innerhalb von FreeCAD, hast du die volle Kontrolle über seine Oberfläche. Du kannst zum Beispiel:

-   Hinzufügen deiner eigenen Paneele, Widgets und Werkzeugleisten
-   Hinzufügen oder Ausblenden von Elementen zu bestehenden Paneelen
-   Ändern, umleiten oder hinzufügen von Verbindungen zwischen all diesen Elementen



## Eine Referenz auf das Hauptfenster erstellen 

Soll an der FreeCAD-Oberfläche gearbeitet werden, muss als allererstes eine Referenz auf das FreeCAD-Hauptfenster erstellt werden:


```python
import sys
from PySide import QtGui ,QtCore 
app = QtGui.qApp
mw = FreeCADGui.getMainWindow()
```



## Durchsuchen der untergeordneten Elemente des Hauptfensters 

Anschließend kannst du beispielsweise alle Widgets der Benutzeroberfläche durchsuchen:


```python
for child in mw.children():
   print('widget name = ', child.objectName(), ', widget type = ', child)
```

Die Widgets in einer Qt-Schnittstelle sind normalerweise in „Container"-Widgets verschachtelt, sodass die untergeordneten Elemente unseres Hauptfensters selbst andere untergeordnete Elemente enthalten können. Je nach Widgettyp kannst du viele Dinge tun. Schau dir die API-Dokumentation an, um zu sehen, was möglich ist.



## Neues Widget manuell hinzufügen 

Das Hinzufügen eines neuen Widgets, beispielsweise eines DockWidgets (das in einer der Seitenleisten von FreeCAD platziert werden kann), ist einfach:


```python
myWidget = QtGui.QDockWidget()
mw.addDockWidget(QtCore.Qt.RightDockWidgetArea,myWidget)
```

Du kannst dann Dinge direkt zu deinem Widget hinzufügen:


```python
myWidget.setObjectName("my Nice New Widget")
myWidget.resize(QtCore.QSize(300,100)) # sets size of the widget
label = QtGui.QLabel("Hello World", myWidget) # creates a label
label.setGeometry(QtCore.QRect(2,50,200,24))  # sets its size
label.setObjectName("myLabel") # sets its name, so it can be found by name
```



## Neues Widget durch Erstellen eines UI-Objekts hinzufügen 

Eine bevorzugte Methode ist jedoch, ein UI-Objekt zu erstellen, das die gesamte Einrichtung deines Widgets auf einmal übernimmt. Der große Vorteil besteht darin, dass ein solches UI-Objekt mit dem Programm Qt Designer grafisch erstellt werden kann. Ein typisches von Qt Designer generiertes Objekt sieht folgendermaßen aus:


```python
class myWidget_Ui(object):
  def setupUi(self, myWidget):
    myWidget.setObjectName("my Nice New Widget")
    myWidget.resize(QtCore.QSize(300,100).expandedTo(myWidget.minimumSizeHint())) # sets size of the widget

    self.label = QtGui.QLabel(myWidget) # creates a label
    self.label.setGeometry(QtCore.QRect(50,50,200,24)) # sets its size
    self.label.setObjectName("label") # sets its name, so it can be found by name

  def retranslateUi(self, draftToolbar): # built-in QT function that manages translations of widgets
    myWidget.setWindowTitle(QtGui.QApplication.translate("myWidget", "My Widget", None, QtGui.QApplication.UnicodeUTF8))
    self.label.setText(QtGui.QApplication.translate("myWidget", "Welcome to my new widget!", None, QtGui.QApplication.UnicodeUTF8))
```

Um es zu verwenden, musst du es nur wie folgt auf dein neu erstelltes Widget anwenden:


```python
app = QtGui.qApp
FCmw = app.activeWindow()
myNewFreeCADWidget = QtGui.QDockWidget() # create a new dckwidget
myNewFreeCADWidget.ui = myWidget_Ui() # load the Ui script
myNewFreeCADWidget.ui.setupUi(myNewFreeCADWidget) # setup the ui
FCmw.addDockWidget(QtCore.Qt.RightDockWidgetArea,myNewFreeCADWidget) # add the widget to the main window
```



## Laden der Benutzeroberfläche aus einer Qt Designer .ui-Datei 

Der Schlüssel zum erfolgreichen Laden einer UI-Datei ist die Verwendung des vollständigen Pfads zur Datei. Der [Addon Manager](Std_AddonMgr/de.md) macht es beispielsweise so:


```python
self.dialog = FreeCADGui.PySideUic.loadUi(os.path.join(os.path.dirname(__file__), "AddonManager.ui"))
```



---
⏵ [documentation index](../README.md) > [Developer Documentation](Category_Developer%20Documentation.md) > [Python Code](Category_Python%20Code.md) > PySide Advanced Examples/de
