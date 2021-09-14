# PySide Advanced Examples/it




{{TOCright}}

## Introduzione


<div class="mw-translate-fuzzy">

Questa pagina contiene degli esempi di livello avanzato di gestione della GUI con [PySide](PySide/it.md). Gli [Esempi di base di PySide](PySide_Beginner_Examples/it.md) e gli [Esempi di livello medio di PySide](PySide_Intermediate_Examples/it.md) sono contenuti nelle rispettive pagine.


</div>

Quindi, usando il modulo PySide all\'interno di FreeCAD, si ha il controllo completo della sua interfaccia. È possibile ad esempio:

-   Aggiungere propri pannelli, widget e barre degli strumenti
-   Aggiungere o nascondere gli elementi nei pannelli già esistenti
-   Modificare, reindirizzare o aggiungere connessioni tra tutti questi elementi

## Create Reference for the Main Window 


<div class="mw-translate-fuzzy">

## Creare un riferimento per la finestra principale 

Se si vuole lavorare sull\'interfaccia di FreeCAD, la prima cosa da fare è creare un riferimento alla finestra principale di FreeCAD:


</div>


```python
import sys
from PySide import QtGui ,QtCore 
app = QtGui.qApp
mw = FreeCADGui.getMainWindow()
```

## Browse the Children of the Main Window 


<div class="mw-translate-fuzzy">

## Esplorare gli elementi della finestra principale 

Quindi, è possibile ad esempio esplorare tutti i widget dell\'interfaccia:


</div>


```python
for child in mw.children():
   print('widget name = ', child.objectName(), ', widget type = ', child)
```

Di solito, in una interfaccia Qt, i widget sono annidati in widget \"contenitori\", in questo modo i figli della finestra principale possono contenere altri figli. Secondo il tipo di widget, si possono fare un sacco di cose. Controllare la documentazione delle API per vedere quello che è possibile fare.

## Add New Widget Manually 


<div class="mw-translate-fuzzy">

## Aggiungere manualmente un nuovo widget 

Per aggiungere un nuovo widget, ad esempio un dockWidget (che può essere posizionato in uno dei pannelli laterali di FreeCAD), fare semplicemente:


</div>


```python
myWidget = QtGui.QDockWidget()
mw.addDockWidget(QtCore.Qt.RightDockWidgetArea,myWidget)
```

In seguito, si può continuare e aggiungere altre cose direttamente al proprio widget:


```python
myWidget.setObjectName("my Nice New Widget")
myWidget.resize(QtCore.QSize(300,100)) # sets size of the widget
label = QtGui.QLabel("Hello World", myWidget) # creates a label
label.setGeometry(QtCore.QRect(2,50,200,24))  # sets its size
label.setObjectName("myLabel") # sets its name, so it can be found by name
```

## Add New Widget by Creating UI Object 


<div class="mw-translate-fuzzy">

## Aggiungere un nuovo widget creando un oggetto UI 

Di solito, il metodo preferito consiste nel creare un oggetto UI (interfaccia utente) che faccia tutta la configurazione del proprio widget in una sola volta. Il grande vantaggio è che tale oggetto dell\'interfaccia utente può essere [creato graficamente](Dialog_creation/it.md) con il programma Qt Designer. Un tipico oggetto generato da Qt Designer si presenta come questo:


</div>


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

Per usarlo, basta applicarlo al pannello (widget) appena creato in questo modo:


```python
app = QtGui.qApp
FCmw = app.activeWindow()
myNewFreeCADWidget = QtGui.QDockWidget() # create a new dckwidget
myNewFreeCADWidget.ui = myWidget_Ui() # load the Ui script
myNewFreeCADWidget.ui.setupUi(myNewFreeCADWidget) # setup the ui
FCmw.addDockWidget(QtCore.Qt.RightDockWidgetArea,myNewFreeCADWidget) # add the widget to the main window
```

## Loading the UI from a Qt Designer .ui File 

The key to loading a UI file successfully is to use the full path to the file. As an example, the [Addon Manager](Std_AddonMgr.md) does it like this:


```python
self.dialog = FreeCADGui.PySideUic.loadUi(os.path.join(os.path.dirname(__file__), "AddonManager.ui"))
```


{{Powerdocnavi

}} 

[Category:Developer Documentation](Category:Developer_Documentation.md) [Category:Python Code](Category:Python_Code.md)
