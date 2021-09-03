


{{TOCright}}

## Introduzione

Questa pagina contiene degli esempi di codice Python utilizzabili in FreeCAD, raccolti dalle esperienze degli utenti e dalle discussioni nei [forum](https://forum.freecadweb.org/viewforum.php?f=22). Dopo averli letti, è possibile usarli per iniziare a creare degli script personali \...

## Snippets

### Un tipico file InitGui.py 

Ogni modulo deve contenere, oltre al file del modulo principale, un file InitGui.py che ha il compito di inserire il modulo nella finestra grafica principale (GUI).

Questo è un esempio semplice di un file InitGui.py:


```python
class ScriptWorkbench (Workbench): 
    MenuText = "Scripts"
    def Initialize(self):
        import Scripts # assuming Scripts.py is your module
        list = ["Script_Cmd"] # That list must contain command names, that can be defined in Scripts.py
        self.appendToolbar("My Scripts",list) 
        
Gui.addWorkbench(ScriptWorkbench())
```


{{Top}}

### Un tipico file del modulo 

Il seguente è un esempio di un file del modulo principale. Esso contiene tutto ciò che il modulo deve seguire. È il file Scripts.py richiamato dall\'esempio precedente. In esso è possibile inserire tutti i comandi personalizzati.


```python
 import FreeCAD, FreeCADGui 
 
class ScriptCmd: 
   def Activated(self): 
       # Here your write what your ScriptCmd does...
       FreeCAD.Console.PrintMessage('Hello, World!')
   def GetResources(self): 
       return {'Pixmap' : 'path_to_an_icon/myicon.png', 'MenuText': 'Short text', 'ToolTip': 'More detailed text'} 
       
FreeCADGui.addCommand('Script_Cmd', ScriptCmd())
```


{{Top}}

### Importare un nuovo tipo di file 

In FreeCAD, è facile creare un importatore per un nuovo tipo di file. FreeCAD non considera che si importano dati in un documento aperto, ma piuttosto che si può semplicemente aprire direttamente il nuovo tipo di file. Quindi, quello che si deve fare è aggiungere la nuova estensione di file alla lista delle estensioni conosciute di FreeCAD, scrivere il codice che legge il file e creare gli oggetti di FreeCAD che si desidera:

Per aggiungere la nuova estensione di file all\'elenco si deve aggiungere questa riga al file InitGui.py :


```python
# Assumes Import_Ext.py is the file that has the code for opening and reading .ext files
FreeCAD.addImportType("Your new File Type (*.ext)","Import_Ext") 
```

Poi nel file Import\_Ext.py:


```python
def open(filename): 
   doc=App.newDocument()
   # here you do all what is needed with filename, read, classify data, create corresponding FreeCAD objects
   doc.recompute()
```

L\'esportazione di un proprio documento in un nuovo tipo di file funziona allo stesso modo, ma si utilizza:

FreeCAD.addExportType("Your new File Type (*.ext)","Export_Ext")


{{Top}}

### Aggiungere una linea 

Una linea ha semplicemente 2 punti.


```python

import Part,PartGui 
doc=App.activeDocument() 
# add a line element to the document and set its points 
l=Part.LineSegment()
l.StartPoint=(0.0,0.0,0.0)
l.EndPoint=(1.0,1.0,1.0)
doc.addObject("Part::Feature","Line").Shape=l.toShape() 
doc.recompute()
```


{{Top}}

### Aggiungere un poligono 

Un poligono è semplicemente un insieme di segmenti di linea collegati tra di loro (una polilinea in AutoCAD). Non è necessario che sia chiuso.


```python
import Part, PartGui 
doc = App.activeDocument()
n = list() 

# create a 3D vector, set its coordinates and add it to the list 
v = App.Vector(0,0,0) 
n.append(v) 
v = App.Vector(10,0,0) 
n.append(v) 
#... repeat for all nodes 

# Create a polygon object and set its nodes 
p = doc.addObject("Part::Polygon","Polygon") 
p.Nodes = n 
doc.recompute()
```


{{Top}}

### Aggiungere e rimuovere un oggetto in un gruppo 


```python
doc=App.activeDocument() 
grp=doc.addObject("App::DocumentObjectGroup", "Group") 
lin=doc.addObject("Part::Feature", "Line")
grp.addObject(lin) # adds the lin object to the group grp
grp.removeObject(lin) # removes the lin object from the group grp
```

Nota: È anche possibile annidare dei gruppi in altri gruppi e creare dei sottogruppi\... {{Top}}

### Aggiungere un Mesh 


```python
import Mesh
doc=App.activeDocument()
# create a new empty mesh
m = Mesh.Mesh()
# build up box out of 12 facets
m.addFacet(0.0,0.0,0.0, 0.0,0.0,1.0, 0.0,1.0,1.0)
m.addFacet(0.0,0.0,0.0, 0.0,1.0,1.0, 0.0,1.0,0.0)
m.addFacet(0.0,0.0,0.0, 1.0,0.0,0.0, 1.0,0.0,1.0)
m.addFacet(0.0,0.0,0.0, 1.0,0.0,1.0, 0.0,0.0,1.0)
m.addFacet(0.0,0.0,0.0, 0.0,1.0,0.0, 1.0,1.0,0.0)
m.addFacet(0.0,0.0,0.0, 1.0,1.0,0.0, 1.0,0.0,0.0)
m.addFacet(0.0,1.0,0.0, 0.0,1.0,1.0, 1.0,1.0,1.0)
m.addFacet(0.0,1.0,0.0, 1.0,1.0,1.0, 1.0,1.0,0.0)
m.addFacet(0.0,1.0,1.0, 0.0,0.0,1.0, 1.0,0.0,1.0)
m.addFacet(0.0,1.0,1.0, 1.0,0.0,1.0, 1.0,1.0,1.0)
m.addFacet(1.0,1.0,0.0, 1.0,1.0,1.0, 1.0,0.0,1.0)
m.addFacet(1.0,1.0,0.0, 1.0,0.0,1.0, 1.0,0.0,0.0)
# scale to a edge langth of 100
m.scale(100.0)
# add the mesh to the active document
me=doc.addObject("Mesh::Feature","Cube")
me.Mesh=m
```


{{Top}}

### Aggiungere un arco o un cerchio 


```python
import Part
doc = App.activeDocument()
c = Part.Circle() 
c.Radius=10.0  
f = doc.addObject("Part::Feature", "Circle") # create a document with a circle feature 
f.Shape = c.toShape() # Assign the circle shape to the shape property 
doc.recompute()
```


{{Top}}

### Accedere alla rappresentazione di un oggetto e modificarla 

A ogni oggetto di un documento di FreeCAD è associato un oggetto di rappresentazione della sua vista in cui sono memorizzati tutti i parametri che definiscono il modo in cui l\'oggetto deve apparire, come il colore, la larghezza di linea, ecc\... Vedere anche lo snippet sottostante [Elencare i componenti di un oggetto](Code_snippets/it#Elencare_i_componenti_di_un_oggetto.md).


```python
gad = Gui.activeDocument() # access the active document containing all 
                           # view representations of the features in the
                           # corresponding App document 

v = gad.getObject("Cube")  # access the view representation to the Mesh feature 'Cube' 
v.ShapeColor               # prints the color to the console 
v.ShapeColor=(1.0,1.0,1.0) # sets the shape color to white
```


{{Top}}

### Replace the form of mouse with one image 


```python
import PySide2
from PySide2 import QtCore, QtGui, QtWidgets
from PySide2.QtWidgets import QApplication
from PySide2.QtGui import QColor, QPixmap, QImage, QPainter, QCursor
from PySide2.QtCore import Qt

myImage = QtGui.QPixmap("Complete_Path_to_image.bmp")
cursor = QtGui.QCursor(myImage)
QtWidgets.QApplication.setOverrideCursor(QtGui.QCursor(cursor))

```


{{Top}}

### Replace the form of mouse with one image (cross) include 

The image is created by Gimp exported in a .XPM file. Copy and use the code between the bracket **\"{\"** code to copy **\"}\"**


```python
import PySide2
from PySide2 import QtCore, QtGui, QtWidgets
from PySide2.QtWidgets import QApplication
from PySide2.QtGui import QColor, QPixmap, QImage, QPainter, QCursor
from PySide2.QtCore import Qt

cross32x32Icon = [
"32 32 2 1",
"   c None",
".  c #FF0000",
"                .               ",
"                .               ",
"                .               ",
"                .               ",
"                .               ",
"                .               ",
"                .               ",
"                .               ",
"                .               ",
"                .               ",
"                .               ",
"                .               ",
"                .               ",
"                .               ",
"                .               ",
"                                ",
"............... . ..............",
"                                ",
"                .               ",
"                .               ",
"                .               ",
"                .               ",
"                .               ",
"                .               ",
"                .               ",
"                .               ",
"                .               ",
"                .               ",
"                .               ",
"                .               ",
"                .               ",
"                .               "
]

myImage = QtGui.QPixmap(cross32x32Icon)
cursor = QtGui.QCursor(myImage)
QtWidgets.QApplication.setOverrideCursor(QtGui.QCursor(cursor))

```


{{Top}}

### Observe camera change in the 3D viewer via Python 

This can be done adding a Node sensor to the camera. from pivy import coin


```python
def callback(*args):
    cam, sensor = args
    print()
    print("Cam position : {}".format(cam.position.getValue().getValue()))
    print("Cam rotation : {}".format(cam.orientation.getValue().getValue()))

camera_node = Gui.ActiveDocument.ActiveView.getCameraNode()
node_sensor = coin.SoNodeSensor(callback, camera_node)
node_sensor.attach(camera_node)```


{{Top}}

### Controllare gli eventi del mouse nel visualizzatore 3D tramite Python 

La struttura di Inventor permette di aggiungere uno o più nodi di richiamo (callback) al grafo di scena (Scenegraph) della vista. In FreeCAD è installato di default un nodo callback per la vista che permette di aggiungere funzioni C++ globali o statiche. In appropriate associazioni Python vengono forniti alcuni metodi per utilizzare questa tecnica all\'interno del codice Python.


```python
App.newDocument()
v=Gui.activeDocument().activeView()
 
#This class logs any mouse button events. As the registered callback function fires twice for 'down' and
#'up' events we need a boolean flag to handle this.
class ViewObserver:
   def logPosition(self, info):
       down = (info["State"] == "DOWN")
       pos = info["Position"]
       if (down):
           FreeCAD.Console.PrintMessage("Clicked on position: ("+str(pos[0])+", "+str(pos[1])+")\n")
       
o = ViewObserver()
c = v.addEventCallback("SoMouseButtonEvent",o.logPosition)
```

Ora, cliccate in qualche parte nella zona nella vista 3D e osservate i messaggi nella finestra di output. Per terminare l\'osservazione basta chiamare:


```python
v.removeEventCallback("SoMouseButtonEvent",c)
```

Sono supportati i seguenti tipi di eventi:

-   SoEvent \-- Tutti i tipi di eventi
-   SoButtonEvent \-- Tutti gli eventi del mouse e della tastiera
-   SoLocation2Event \-- Eventi di movimento 2D (normalmente i movimenti del mouse)
-   SoMotion3Event \-- Eventi di movimento 3D (normalmente di spaceball)
-   SoKeyboardEvent \-- Eventi dei tasti alto e basso
-   SoMouseButtonEvent \-- Eventi dei pulsanti del mouse verso il basso e verso l\'alto
-   SoSpaceballButtonEvent \-- Eventi di SpaceBall in basso e in alto

La funzione di Python che può essere registrata con addEventCallback() si aspetta una difinizione. Secondo l\'evento controllato la definizione può contenere chiavi differenti.

Per tutti gli eventi esistono le seguenti chiavi:

-   Type \-- Il nome del tipo di evento, ad esempio SoMouseEvent, SoLocation2Event, \...
-   Time \-- L\'ora corrente come stringa
-   Position \-- Una tupla di due interi, dipendenti dalla posizione del mouse
-   ShiftDown \-- un valore booleano, vero (true) se Shift è stato premuto altrimenti false
-   CtrlDown \-- un valore booleano, true se è stato premuto Ctrl altrimenti false
-   AltDown \-- un valore booleano, true se è stato premuto Alt altrimenti false

Per tutti gli eventi dei pulsanti, ad esempio eventi di tastiera, mouse o spaceball:

-   State \-- Una stringa \'UP\' se il pulsante è verso l\'alto, \'DOWN\' se è verso il basso o \'UNKNOWN\' per tutti gli altri casi

Per gli eventi da tastiera:

-   Key \-- Un carattere del tasto premuto

Per gli eventi del pulsante del mouse

-   Button \-- Il pulsante premuto, potrebbe essere BUTTON1, \..., BUTTON5 o ANY

Per gli eventi di Spaceball:

-   Button \-- Il pulsante premuto, potrebbe essere BUTTON1, \..., BUTTON7 o ANY

E infine eventi di movimento:

-   Translation \-- Una tupla di tre numeri in virgola mobile
-   Rotation \-- Un quaternione per la rotazione, cioè una tupla di quattro numeri in virgola mobile


{{Top}}

### Visualizzare i tasti premuti e gli eventi dei comandi 

Questa macro visualizza nel report i tasti premuti e tutti gli eventi dei comandi


```python
App.newDocument()
v=Gui.activeDocument().activeView()
class ViewObserver:
   def logPosition(self, info):
       try:
           down = (info["Key"])
           FreeCAD.Console.PrintMessage(str(down)+"\n") # here the character pressed
           FreeCAD.Console.PrintMessage(str(info)+"\n") # list all events command
           FreeCAD.Console.PrintMessage("_______________________________________"+"\n")
       except Exception:
           None
 
o = ViewObserver()
c = v.addEventCallback("SoEvent",o.logPosition)

#v.removeEventCallback("SoEvent",c) # remove ViewObserver
```


{{Top}}

### Manipolare il grafo della scena in Python 

È anche possibile ottenere il Scenegraph (grafo della scena) in Python e modificarlo, con il modulo \'Pivy\' - una associazione di Python per Coin.


```python
from pivy.coin import *                # load the pivy module
view = Gui.ActiveDocument.ActiveView   # get the active viewer
root = view.getSceneGraph()            # the root is an SoSeparator node
root.addChild(SoCube())
view.fitAll()
```

L\'API in Python di Pivy viene creato utilizzando lo strumento SWIG. In FreeCAD si usano alcuni nodi auto-scritti che non è possibile creare direttamente in Python. Tuttavia, è possibile creare un nodo dal suo nome interno. Si può creare una istanza di tipo \'SoFCSelection\' con:


```python
type = SoType.fromName("SoFCSelection")
node = type.createInstance()
```


{{Top}}

### Aggiungere e rimuovere oggetti nel grafo della scena 

Questo è un modo per aggiungere dei nuovi nodi al Scenegraph. Accertarsi di aggiungere sempre un SoSeparator per contenere la geometria, le coordinate e le informazioni sui materiale di uno stesso oggetto. L\'esempio seguente aggiunge una linea rossa da (0,0,0) a (10,0,0):


```python
from pivy import coin
sg = Gui.ActiveDocument.ActiveView.getSceneGraph()
co = coin.SoCoordinate3()
pts = [[0,0,0],[10,0,0]]
co.point.setValues(0,len(pts),pts)
ma = coin.SoBaseColor()
ma.rgb = (1,0,0)
li = coin.SoLineSet()
li.numVertices.setValue(2)
no = coin.SoSeparator()
no.addChild(co)
no.addChild(ma)
no.addChild(li)
sg.addChild(no)
```

Per rimuoverla, è sufficiente scrivere: 
```python
sg.removeChild(no)
``` {{Top}}


<div class="mw-collapsible mw-collapsed toccolours">

### Salvare il grafo della scena in 3 serie di 36 file 

View the code snippet by expanding this section


<div class="mw-collapsible-content">


```python
import math
import time
from FreeCAD import Base
from pivy import coin

size=(1000,1000)
dirname = "C:/Temp/animation/"
steps=36
angle=2*math.pi/steps

matX=Base.Matrix()
matX.rotateX(angle)
stepsX=Base.Placement(matX).Rotation

matY=Base.Matrix()
matY.rotateY(angle)
stepsY=Base.Placement(matY).Rotation

matZ=Base.Matrix()
matZ.rotateZ(angle)
stepsZ=Base.Placement(matZ).Rotation

view=Gui.ActiveDocument.ActiveView
cam=view.getCameraNode()
rotCamera=Base.Rotation(*cam.orientation.getValue().getValue())

# this sets the lookat point to the center of circumsphere of the global bounding box
view.fitAll()

# the camera's position, i.e. the user's eye point
position=Base.Vector(*cam.position.getValue().getValue())
distance=cam.focalDistance.getValue()

# view direction
vec=rotCamera.multVec(Base.Vector(0,0,-1))

# this is the point on the screen the camera looks at
# when rotating the camera we should make this point fix
lookat=position+vec*distance

# around x axis
for i in range(steps):
    rotCamera=stepsX.multiply(rotCamera)
    cam.orientation.setValue(*rotCamera.Q)
    vec=rotCamera.multVec(Base.Vector(0,0,-1))
    pos=lookat-vec*distance
    cam.position.setValue(pos.x,pos.y,pos.z)
    Gui.updateGui()
    time.sleep(0.3)
    view.saveImage(dirname+"x-%d.png" % i,*size)

# around y axis
for i in range(steps):
    rotCamera=stepsY.multiply(rotCamera)
    cam.orientation.setValue(*rotCamera.Q)
    vec=rotCamera.multVec(Base.Vector(0,0,-1))
    pos=lookat-vec*distance
    cam.position.setValue(pos.x,pos.y,pos.z)
    Gui.updateGui()
    time.sleep(0.3)
    view.saveImage(dirname+"y-%d.png" % i,*size)

# around z axis
for i in range(steps):
    rotCamera=stepsZ.multiply(rotCamera)
    cam.orientation.setValue(*rotCamera.Q)
    vec=rotCamera.multVec(Base.Vector(0,0,-1))
    pos=lookat-vec*distance
    cam.position.setValue(pos.x,pos.y,pos.z)
    Gui.updateGui()
    time.sleep(0.3)
    view.saveImage(dirname+"z-%d.png" % i,*size)
```


</div>


</div>


{{Top}}

### Aggiungere dei widget personalizzati all\'interfaccia 

È possibile creare widget personalizzati con Qt designer, trasformarli in uno script Python e poi caricarli nell\'interfaccia di FreeCAD con PySide.

Il codice Python prodotto dal compilatore Ui di Python (lo strumento che converte i file .ui di Qt-designer nel codice Python) appare in genere come questo (è semplice, si può anche codificare direttamente in Python):


```python
class myWidget_Ui(object):
    def setupUi(self, myWidget):
        myWidget.setObjectName("my Nice New Widget")
        myWidget.resize(QtCore.QSize(QtCore.QRect(0,0,300,100).size()).expandedTo(myWidget.minimumSizeHint())) # sets size of the widget
 
        self.label = QtGui.QLabel(myWidget) # creates a label
        self.label.setGeometry(QtCore.QRect(50,50,200,24)) # sets its size
        self.label.setObjectName("label") # sets its name, so it can be found by name

    def retranslateUi(self, draftToolbar): # built-in QT function that manages translations of widgets
        myWidget.setWindowTitle(QtGui.QApplication.translate("myWidget", "My Widget", None, QtGui.QApplication.UnicodeUTF8))
        self.label.setText(QtGui.QApplication.translate("myWidget", "Welcome to my new widget!", None, QtGui.QApplication.UnicodeUTF8))             
```

Dopo, basta creare un riferimento alla finestra Qt di FreeCAD, inserire un widget personalizzato in essa, e \"trasformare\" questo widget nel proprio con il codice Ui che abbiamo appena creato:


```python
app = QtGui.qApp
FCmw = app.activeWindow() # the active qt window, = the freecad window since we are inside it
# FCmw = FreeCADGui.getMainWindow() # use this line if the 'addDockWidget' error is declared
myNewFreeCADWidget = QtGui.QDockWidget() # create a new dckwidget
myNewFreeCADWidget.ui = myWidget_Ui() # load the Ui script
myNewFreeCADWidget.ui.setupUi(myNewFreeCADWidget) # setup the ui
FCmw.addDockWidget(QtCore.Qt.RightDockWidgetArea,myNewFreeCADWidget) # add the widget to the main window
```


{{Top}}

### Aggiungere una scheda alla Combo View 

Il seguente codice consente di aggiungere una nuova scheda nel pannello [Vista combinata](Combo_view/it.md) di FreeCAD, oltre le schede standard \"Modello\" e \"Azioni\" . Questo codice utilizza anche il modulo `uic` per caricare un file UI direttamente nella nuova scheda.


```python
# create new Tab in ComboView
from PySide import QtGui,QtCore
#from PySide import uic

def getMainWindow():
   "returns the main window"
   # using QtGui.qApp.activeWindow() isn't very reliable because if another
   # widget than the mainwindow is active (e.g. a dialog) the wrong widget is
   # returned
   toplevel = QtGui.qApp.topLevelWidgets()
   for i in toplevel:
       if i.metaObject().className() == "Gui::MainWindow":
           return i
   raise Exception("No main window found")

def getComboView(mw):
   dw=mw.findChildren(QtGui.QDockWidget)
   for i in dw:
       if str(i.objectName()) == "Combo View":
           return i.findChild(QtGui.QTabWidget)
       elif str(i.objectName()) == "Python Console":
           return i.findChild(QtGui.QTabWidget)
   raise Exception ("No tab widget found")

mw = getMainWindow()
tab = getComboView(getMainWindow())
tab2=QtGui.QDialog()
tab.addTab(tab2,"A Special Tab")

#uic.loadUi("/myTaskPanelforTabs.ui",tab2)
tab2.show()
#tab.removeTab(2)

```


{{Top}}

### Abilitare o disabilitare una finestra 

This script give the ability to manipulate the UI from the [Python console](Python_console.md) to show/hide different components in the FreeCAD [interface](interface.md) such as:

-   [Report view](Report_view.md)
-   [Tree view](Tree_view.md)
-   [Property view](Property_editor.md)
-   [Selection view](Selection_view.md)
-   [Combo View](Combo_View.md)
-   [Python console](Python_console.md)
-   draftToolbar


```python
from PySide import QtGui
mw = FreeCADGui.getMainWindow()
dws = mw.findChildren(QtGui.QDockWidget)

# objectName may be :
# "Report view"
# "Tree view"
# "Property view"
# "Selection view"
# "Combo View"
# "Python console"
# "draftToolbar"

for i in dws:
  if i.objectName() == "Report view":
    dw = i
    break

va = dw.toggleViewAction()
va.setChecked(True)        # True or False
dw.setVisible(True)        # True or False
```


{{Top}}

### Aprire una pagina web personalizzata 


```python
import WebGui
WebGui.openBrowser("http://www.example.com")
```


{{Top}}

### Ottenere il contenuto HTML di una pagina web aperta 


```python
from PySide import QtGui,QtWebKit
a = QtGui.qApp
mw = a.activeWindow()
v = mw.findChild(QtWebKit.QWebFrame)
html = unicode(v.toHtml())
print( html)
```


{{Top}}

### Reperire le coordinate di 3 punti o oggetti selezionati 


```python
# -*- coding: utf-8 -*-
# the line above to put the accentuated in the remarks
# If this line is missing, an error will be returned
# extract and use the coordinates of 3 objects selected
import Part, FreeCAD, math, PartGui, FreeCADGui
from FreeCAD import Base, Console
sel = FreeCADGui.Selection.getSelection() # " sel " contains the items selected
if len(sel)!=3 :
  # If there are no 3 objects selected, an error is displayed in the report view
  # The \r and \n at the end of line mean return and the newline CR + LF.
  Console.PrintError("Select 3 points exactly\r\n")
else :
  points=[]
  for obj in sel:
    points.append(obj.Shape.BoundBox.Center)

  for pt in points:
    # display of the coordinates in the report view
    Console.PrintMessage(str(pt.x)+"\r\n")
    Console.PrintMessage(str(pt.y)+"\r\n")
    Console.PrintMessage(str(pt.z)+"\r\n")

  Console.PrintMessage(str(pt[1]) + "\r\n")
```


{{Top}}

### Lista di oggetti 


```python
# -*- coding: utf-8 -*-
import FreeCAD,Draft
# List all objects of the document
doc = FreeCAD.ActiveDocument
objs = FreeCAD.ActiveDocument.Objects
#App.Console.PrintMessage(str(objs) + "\n")
#App.Console.PrintMessage(str(len(FreeCAD.ActiveDocument.Objects)) + " Objects"  + "\n")

for obj in objs:
    a = obj.Name                                             # list the Name  of the object  (not modifiable)
    b = obj.Label                                            # list the Label of the object  (modifiable)
    try:
        c = obj.LabelText                                    # list the LabeText of the text (modifiable)
        App.Console.PrintMessage(str(a) +" "+ str(b) +" "+ str(c) + "\n") # Displays the Name the Label and the text
    except:
        App.Console.PrintMessage(str(a) +" "+ str(b) + "\n") # Displays the Name and the Label of the object

#doc.removeObject("Box") # Clears the designated object
```


{{Top}}

### Ottenere la dimensione di un oggetto, dato il suo nome 


```python
for edge in FreeCAD.ActiveDocument.MyObjectName.Shape.Edges: # replace "MyObjectName" for list
    print( edge.Length)
```


{{Top}}

### Funzione residente per una azione con un clic del mouse 

Qui con **SelObserver** sopra uno obietto selezionato


```python
# -*- coding: utf-8 -*-
# causes an action to the mouse click on an object
# This function remains resident (in memory) with the function "addObserver(s)"
# "removeObserver(s) # Uninstalls the resident function
class SelObserver:
    def setPreselection(self,doc,obj,sub):                # Preselection object
        App.Console.PrintMessage(str(sub)+ "\n")          # The part of the object name

    def addSelection(self,doc,obj,sub,pnt):               # Selection object
        App.Console.PrintMessage("addSelection"+ "\n")
        App.Console.PrintMessage(str(doc)+ "\n")          # Name of the document
        App.Console.PrintMessage(str(obj)+ "\n")          # Name of the object
        App.Console.PrintMessage(str(sub)+ "\n")          # The part of the object name
        App.Console.PrintMessage(str(pnt)+ "\n")          # Coordinates of the object
        App.Console.PrintMessage("______"+ "\n")

    def removeSelection(self,doc,obj,sub):                # Delete the selected object
        App.Console.PrintMessage("removeSelection"+ "\n")

    def setSelection(self,doc):                           # Selection in ComboView
        App.Console.PrintMessage("setSelection"+ "\n")

    def clearSelection(self,doc):                         # If click on the screen, clear the selection
        App.Console.PrintMessage("clearSelection"+ "\n")  # If click on another object, clear the previous object
s =SelObserver()
FreeCADGui.Selection.addObserver(s)                       # install the function mode resident
#FreeCADGui.Selection.removeObserver(s)                   # Uninstall the resident function
```

Altro esempio con **ViewObserver** sopra uno obbietto selezionato


```python
App.newDocument()
v=Gui.activeDocument().activeView()
 
#This class logs any mouse button events. As the registered callback function fires twice for 'down' and
#'up' events we need a boolean flag to handle this.
class ViewObserver:
   def __init__(self, view):
       self.view = view
   
   def logPosition(self, info):
       down = (info["State"] == "DOWN")
       pos = info["Position"]
       if (down):
           FreeCAD.Console.PrintMessage("Clicked on position: ("+str(pos[0])+", "+str(pos[1])+")\n")
           pnt = self.view.getPoint(pos)
           FreeCAD.Console.PrintMessage("World coordinates: " + str(pnt) + "\n")
           info = self.view.getObjectInfo(pos)
           FreeCAD.Console.PrintMessage("Object info: " + str(info) + "\n")

o = ViewObserver(v)
c = v.addEventCallback("SoMouseButtonEvent",o.logPosition)

```


{{Top}}

### Trovare o selezionare tutti gli elementi sotto il cursore 


```python
from pivy import coin
import FreeCADGui

def mouse_over_cb( event_callback):
    event = event_callback.getEvent()
    pos = event.getPosition().getValue()
    listObjects = FreeCADGui.ActiveDocument.ActiveView.getObjectsInfo((int(pos[0]),int(pos[1])))
    obj = []
    if listObjects:
        FreeCAD.Console.PrintMessage("\n *** Objects under mouse pointer ***")
        for o in listObjects:
            label = str(o["Object"])
            if not label in obj:
                obj.append(label)
        FreeCAD.Console.PrintMessage("\n"+str(obj))


view = FreeCADGui.ActiveDocument.ActiveView

mouse_over = view.addEventCallbackPivy( coin.SoLocation2Event.getClassTypeId(), mouse_over_cb )

# to remove Callback :
#view.removeEventCallbackPivy( coin.SoLocation2Event.getClassTypeId(), mouse_over)

####
#The easy way is probably to use FreeCAD's selection.
#FreeCADGui.ActiveDocument.ActiveView.getObjectsInfo(mouse_coords)

####
#you get that kind of result :
#'Document': 'Unnamed', 'Object': 'Box', 'Component': 'Face2', 'y': 8.604081153869629, 'x': 21.0, 'z': 8.553047180175781

####
#You can use this data to add your element to FreeCAD's selection :
#FreeCADGui.Selection.addSelection(FreeCAD.ActiveDocument.Box,'Face2',21.0,8.604081153869629,8.553047180175781)
```


{{Top}}


<div class="mw-collapsible mw-collapsed toccolours">

### Elencare i componenti di un oggetto 

Questa funzione elenca i componenti ed estrae le coordinate XYZ di un oggetto, i bordi (edge) e le loro lunghezze, le sue facce e la loro superficie.

This function list the components of an object and extracts:

-   this object its XYZ coordinates,
-   its edges and their lengths center of mass and coordinates
-   its faces and their center of mass
-   its faces and their surfaces and coordinates


<div class="mw-collapsible-content">


```python
# -*- coding: utf-8 -*-
# This function list the components of an object
# and extract this object its XYZ coordinates,
# its edges and their lengths center of mass and coordinates
# its faces and their center of mass
# its faces and their surfaces and coordinates
# 8/05/2014

import Draft,Part
def detail():
    sel = FreeCADGui.Selection.getSelection()   # Select an object
    if len(sel) != 0:                           # If there is a selection then
        Vertx=[]
        Edges=[]
        Faces=[]
        compt_V=0
        compt_E=0
        compt_F=0
        pas    =0
        perimetre = 0.0   
        EdgesLong = []

        # Displays the "Name" and the "Label" of the selection
        App.Console.PrintMessage("Selection > " + str(sel[0].Name) + "  " + str(sel[0].Label) +"\n"+"\n")

        for j in enumerate(sel[0].Shape.Edges):                                     # Search the "Edges" and their lengths
            compt_E+=1
            Edges.append("Edge%d" % (j[0]+1))
            EdgesLong.append(str(sel[0].Shape.Edges[compt_E-1].Length))
            perimetre += (sel[0].Shape.Edges[compt_E-1].Length)                     # calculates the perimeter

            # Displays the "Edge" and its length
            App.Console.PrintMessage("Edge"+str(compt_E)+" Length > "+str(sel[0].Shape.Edges[compt_E-1].Length)+"\n")

            # Displays the "Edge" and its center mass
            App.Console.PrintMessage("Edge"+str(compt_E)+" Center > "+str(sel[0].Shape.Edges[compt_E-1].CenterOfMass)+"\n")

            num = sel[0].Shape.Edges[compt_E-1].Vertexes[0]
            Vertx.append("X1: "+str(num.Point.x))
            Vertx.append("Y1: "+str(num.Point.y))
            Vertx.append("Z1: "+str(num.Point.z))
            # Displays the coordinates 1
            App.Console.PrintMessage("X1: "+str(num.Point[0])+" Y1: "+str(num.Point[1])+" Z1: "+str(num.Point[2])+"\n")

            try:
                num = sel[0].Shape.Edges[compt_E-1].Vertexes[1]
                Vertx.append("X2: "+str(num.Point.x))
                Vertx.append("Y2: "+str(num.Point.y))
                Vertx.append("Z2: "+str(num.Point.z))
            except:
                Vertx.append("-")
                Vertx.append("-")
                Vertx.append("-")
            # Displays the coordinates 2
            App.Console.PrintMessage("X2: "+str(num.Point[0])+" Y2: "+str(num.Point[1])+" Z2: "+str(num.Point[2])+"\n")

            App.Console.PrintMessage("\n")
        App.Console.PrintMessage("Perimeter of the form  : "+str(perimetre)+"\n") 

        App.Console.PrintMessage("\n")
        FacesSurf = []
        for j in enumerate(sel[0].Shape.Faces):                                      # Search the "Faces" and their surface
            compt_F+=1
            Faces.append("Face%d" % (j[0]+1))
            FacesSurf.append(str(sel[0].Shape.Faces[compt_F-1].Area))

            # Displays 'Face' and its surface
            App.Console.PrintMessage("Face"+str(compt_F)+" >  Surface "+str(sel[0].Shape.Faces[compt_F-1].Area)+"\n")

            # Displays 'Face' and its CenterOfMass
            App.Console.PrintMessage("Face"+str(compt_F)+" >  Center  "+str(sel[0].Shape.Faces[compt_F-1].CenterOfMass)+"\n")

            # Displays 'Face' and its Coordinates
            FacesCoor = []
            fco = 0
            for f0 in sel[0].Shape.Faces[compt_F-1].Vertexes:                        # Search the Vertexes of the face
                fco += 1
                FacesCoor.append("X"+str(fco)+": "+str(f0.Point.x))
                FacesCoor.append("Y"+str(fco)+": "+str(f0.Point.y))
                FacesCoor.append("Z"+str(fco)+": "+str(f0.Point.z))

            # Displays 'Face' and its Coordinates
            App.Console.PrintMessage("Face"+str(compt_F)+" >  Coordinate"+str(FacesCoor)+"\n")

            # Displays 'Face' and its Volume
            App.Console.PrintMessage("Face"+str(compt_F)+" >  Volume  "+str(sel[0].Shape.Faces[compt_F-1].Volume)+"\n")
            App.Console.PrintMessage("\n")

        # Displays the total surface of the form
        App.Console.PrintMessage("Surface of the form    : "+str(sel[0].Shape.Area)+"\n")

        # Displays the total Volume of the form
        App.Console.PrintMessage("Volume  of the form    : "+str(sel[0].Shape.Volume)+"\n")

detail()
```


</div>


</div>


{{Top}}

### List the PropertiesList 


```python
import FreeCADGui
from FreeCAD import Console
o = App.ActiveDocument.ActiveObject
op = o.PropertiesList
for p in op:
    Console.PrintMessage("Property: "+ str(p)+ " Value: " + str(o.getPropertyByName(p))+"\r\n")
```


{{Top}}

### Aggiungere una singola Proprietà Comment 


```python
import Draft
obj = FreeCADGui.Selection.getSelection()[0]
obj.addProperty("App::PropertyString","GComment","Draft","Font name").GComment = "Comment here"
App.activeDocument().recompute()
```


{{Top}}


<div class="mw-collapsible mw-collapsed toccolours">

### Ricerca e estrazione di dati 

Esempi di ricerca e decodifica di informazioni su un oggetto.

Ogni sezione separata da \"\#\#\#\#\#\#\#\#\#\#\#\#\" è indipendente e può essere copiata direttamente nella console Python, o in una macro o usata come macro a sè stante. La descrizione della macro si trova nel commento.

Le informazioni ricercate in questo modo sono visualizzate nella finestra dei rapporti attivabile con Visualizza -\> Viste -\> Report


<div class="mw-collapsible-content">


```python
# -*- coding: utf-8 -*-
from __future__ import unicode_literals
 
# Exemples de recherche et de decodage d'informations sur un objet
# Chaque section peut etre copiee directement dans la console Python ou dans une macro ou utilisez la macro tel quel
# Certaines commandes se repetent seul l'approche est differente
# L'affichage se fait dans la Vue rapport : Menu Affichage > Vues > Vue rapport
#
# Examples of research and decoding information on an object
# Each section can be copied directly into the Python console, or in a macro or uses this macro
# Certain commands as repeat alone approach is different
# Displayed in Report view: View > Views > report view
#
# rev:30/08/2014:29/09/2014:17/09/2015 22/11/2019
 
from FreeCAD import Base
import DraftVecUtils, Draft, Part

# search the name of the active document 
mydoc = FreeCAD.activeDocument().Name                                     # Name of active Document
App.Console.PrintMessage("Active docu    : "+(mydoc)+"\n")
##################################################################################

# search the label of the object selected
sel = FreeCADGui.Selection.getSelection()                                 # select object with getSelection()
object_Label = sel[0].Label                                               # Label of the object (modifiable)
App.Console.PrintMessage("object_Label   : "+(object_Label)+"\n")
##################################################################################

#TypeID object FreeCAD selected
sel = FreeCADGui.Selection.getSelection()                                 # select object with getSelection()
App.Console.PrintMessage("sel            : "+str(sel[0])+"\n\n")          # sel[0] first object selected
##################################################################################

# search the Name of the object selected
sel = FreeCADGui.Selection.getSelection()                                 # select object with getSelection()
object_Name  = sel[0].Name                                                # Name of the object (not modifiable)
App.Console.PrintMessage("object_Name    : "+str(object_Name)+"\n\n")
##################################################################################

# search the Sub Element Name of the sub object selected
try:
    SubElement = FreeCADGui.Selection.getSelectionEx()                    # sub element name with getSelectionEx()
    element_ = SubElement[0].SubElementNames[0]                           # name of 1 element selected
    App.Console.PrintMessage("elementSelec   : "+str(element_)+"\n\n")            
except:
    App.Console.PrintMessage("Oups"+"\n\n")            
##################################################################################

# give the length of the subObject selected
SubElementLength = Gui.Selection.getSelectionEx()[0].SubObjects[0].Length # sub element or element name with getSelectionEx()
App.Console.PrintMessage("SubElement length: "+str(SubElementLength)+"\n")# length
##################################################################################

# list the edges and the coordinates of the object[0] selected
sel = FreeCADGui.Selection.getSelection()                                 # select object with getSelection()
i = 0
for j in enumerate(sel[0].Shape.Edges):                                   # list all Edges
    i += 1
    App.Console.PrintMessage("Edges n : "+str(i)+"\n")
    a = sel[0].Shape.Edges[j[0]].Vertexes[0]
    App.Console.PrintMessage("X1             : "+str(a.Point.x)+"\n")     # coordinate XYZ first point
    App.Console.PrintMessage("Y1             : "+str(a.Point.y)+"\n")     #
    App.Console.PrintMessage("Z1             : "+str(a.Point.z)+"\n")     #
    try:
        a = sel[0].Shape.Edges[j[0]].Vertexes[1]
        App.Console.PrintMessage("X2             : "+str(a.Point.x)+"\n") # coordinate XYZ second point
        App.Console.PrintMessage("Y2             : "+str(a.Point.y)+"\n") #
        App.Console.PrintMessage("Z2             : "+str(a.Point.z)+"\n") #
    except:
        App.Console.PrintMessage("Oups"+"\n")    
App.Console.PrintMessage("\n")    
##################################################################################

# give the sub element name, length, coordinates, BoundBox, BoundBox.Center, Area of the SubObjects selected
try:
    SubElement = FreeCADGui.Selection.getSelectionEx()                                        # sub element name with getSelectionEx()
    subElementName = Gui.Selection.getSelectionEx()[0].SubElementNames[0]                     # sub element name with getSelectionEx()
    App.Console.PrintMessage("subElementName : "+str(subElementName)+"\n")subObjectLength = Gui.Selection.getSelectionEx()[0].SubObjects[0].Length                  # sub element Length
    App.Console.PrintMessage("subObjectLength: "+str(subObjectLength)+"\n\n")subObjectX1 = Gui.Selection.getSelectionEx()[0].SubObjects[0].Vertexes[0].Point.x         # sub element coordinate X1
    App.Console.PrintMessage("subObject_X1   : "+str(subObjectX1)+"\n")
    subObjectY1 = Gui.Selection.getSelectionEx()[0].SubObjects[0].Vertexes[0].Point.y         # sub element coordinate Y1
    App.Console.PrintMessage("subObject_Y1   : "+str(subObjectY1)+"\n")
    subObjectZ1 = Gui.Selection.getSelectionEx()[0].SubObjects[0].Vertexes[0].Point.z         # sub element coordinate Z1
    App.Console.PrintMessage("subObject_Z1   : "+str(subObjectZ1)+"\n\n")

    try:
        subObjectX2 = Gui.Selection.getSelectionEx()[0].SubObjects[0].Vertexes[1].Point.x     # sub element coordinate X2
        App.Console.PrintMessage("subObject_X2   : "+str(subObjectX2)+"\n")
        subObjectY2 = Gui.Selection.getSelectionEx()[0].SubObjects[0].Vertexes[1].Point.y     # sub element coordinate Y2
        App.Console.PrintMessage("subObject_Y2   : "+str(subObjectY2)+"\n")
        subObjectZ2 = Gui.Selection.getSelectionEx()[0].SubObjects[0].Vertexes[1].Point.z     # sub element coordinate Z2
        App.Console.PrintMessage("subObject_Z2   : "+str(subObjectZ2)+"\n\n")
    except:
        App.Console.PrintMessage("Oups"+"\n\n")            

    subObjectBoundBox = Gui.Selection.getSelectionEx()[0].SubObjects[0].BoundBox              # sub element BoundBox coordinates
    App.Console.PrintMessage("subObjectBBox  : "+str(subObjectBoundBox)+"\n")subObjectBoundBoxCenter = Gui.Selection.getSelectionEx()[0].SubObjects[0].BoundBox.Center # sub element BoundBoxCenter
    App.Console.PrintMessage("subObjectBBoxCe: "+str(subObjectBoundBoxCenter)+"\n")surfaceFace = Gui.Selection.getSelectionEx()[0].SubObjects[0].Area                        # Area of the face selected
    App.Console.PrintMessage("surfaceFace    : "+str(surfaceFace)+"\n\n")
except:
    App.Console.PrintMessage("Oups"+"\n\n")            
##################################################################################

# give the area of the object
sel = FreeCADGui.Selection.getSelection()                                 # select object with getSelection()
surface = sel[0].Shape.Area                                               # Area object complete
App.Console.PrintMessage("surfaceObjet   : "+str(surface)+"\n\n")
##################################################################################

# give the Center Of Mass and coordinates of the object
sel = FreeCADGui.Selection.getSelection()                                 # select object with getSelection()
CenterOfMass = sel[0].Shape.CenterOfMass                                  # Center of Mass of the object
App.Console.PrintMessage("CenterOfMass   : "+str(CenterOfMass)+"\n")
App.Console.PrintMessage("CenterOfMassX  : "+str(CenterOfMass[0])+"\n")   # coordinates [0]=X [1]=Y [2]=Z
App.Console.PrintMessage("CenterOfMassY  : "+str(CenterOfMass[1])+"\n")   # or CenterOfMass.x, CenterOfMass.y, CenterOfMass.z
App.Console.PrintMessage("CenterOfMassZ  : "+str(CenterOfMass[2])+"\n\n")
##################################################################################

# list the all faces of the object selected
sel = FreeCADGui.Selection.getSelection()                                 # select object with getSelection()
for j in enumerate(sel[0].Shape.Faces):                                   # List alles faces of the object
    App.Console.PrintMessage("Face           : "+str("Face%d" % (j[0]+1))+"\n")
App.Console.PrintMessage("\n\n")
##################################################################################

# give the volume of the object selected
sel = FreeCADGui.Selection.getSelection()                                 # select object with getSelection()
volume_ = sel[0].Shape.Volume                                             # Volume of the object
App.Console.PrintMessage("volume_        : "+str(volume_)+"\n\n")
##################################################################################
 
# give the BoundBox of the oject selected all type
objs = FreeCADGui.Selection.getSelection()                                 # select object with getSelection()
if len(objs) >= 1:                                                         # serch the object type
    if hasattr(objs[0], "Shape"):
        s = objs[0].Shape
    elif hasattr(objs[0], "Mesh"):      # upgrade with wmayer thanks #http://forum.freecadweb.org/viewtopic.php?f=13&t=22331
        s = objs[0].Mesh
    elif hasattr(objs[0], "Points"):
        s = objs[0].Points

boundBox_= s.BoundBox                                                     # BoundBox of the object
App.Console.PrintMessage("boundBox_      : "+str(boundBox_)+"\n")         # 
 
boundBoxLX   = boundBox_.XLength                                          # Length x boundBox rectangle
boundBoxLY   = boundBox_.YLength                                          # Length y boundBox rectangle
boundBoxLZ   = boundBox_.ZLength                                          # Length z boundBox rectangle

boundBoxXMin = boundBox_.XMin                                             # coordonate XMin
boundBoxYMin = boundBox_.YMin                                             # coordonate YMin
boundBoxZMin = boundBox_.ZMin                                             # coordonate ZMin
boundBoxXMax = boundBox_.XMax                                             # coordonate XMax
boundBoxYMax = boundBox_.YMax                                             # coordonate YMax
boundBoxZMax = boundBox_.ZMax                                             # coordonate ZMax

boundBoxDiag= boundBox_.DiagonalLength                                    # Diagonal Length boundBox rectangle
boundBoxCenter = boundBox_.Center                                         # BoundBox Center

App.Console.PrintMessage("boundBoxLX     : "+str(boundBoxLX)+"\n")
App.Console.PrintMessage("boundBoxLY     : "+str(boundBoxLY)+"\n")
App.Console.PrintMessage("boundBoxLZ     : "+str(boundBoxLZ)+"\n\n")

App.Console.PrintMessage("boundBoxXMin   : "+str(boundBoxXMin)+"\n")
App.Console.PrintMessage("boundBoxYMin   : "+str(boundBoxYMin)+"\n")
App.Console.PrintMessage("boundBoxZMin   : "+str(boundBoxZMin)+"\n")
App.Console.PrintMessage("boundBoxXMax   : "+str(boundBoxXMax)+"\n")
App.Console.PrintMessage("boundBoxYMax   : "+str(boundBoxYMax)+"\n")
App.Console.PrintMessage("boundBoxZMax   : "+str(boundBoxZMax)+"\n\n")

App.Console.PrintMessage("boundBoxDiag   : "+str(boundBoxDiag)+"\n")
App.Console.PrintMessage("boundBoxCenter : "+str(boundBoxCenter)+"\n\n")

##################################################################################

# give the complete placement of the object selected
sel = FreeCADGui.Selection.getSelection()                                 # select object with getSelection()
pl = sel[0].Shape.Placement                                               # Placement Vector XYZ and Yaw-Pitch-Roll
App.Console.PrintMessage("Placement      : "+str(pl)+"\n")
##################################################################################

# give the placement Base (xyz) of the object selected
sel = FreeCADGui.Selection.getSelection()                                 # select object with getSelection()
pl = sel[0].Shape.Placement.Base                                          # Placement Vector XYZ
App.Console.PrintMessage("PlacementBase  : "+str(pl)+"\n\n")
##################################################################################
 
# give the placement Base (xyz) of the object selected
sel = FreeCADGui.Selection.getSelection()                                 # select object with getSelection()
oripl_X = sel[0].Placement.Base[0]                                        # decode Placement X
oripl_Y = sel[0].Placement.Base[1]                                        # decode Placement Y
oripl_Z = sel[0].Placement.Base[2]                                        # decode Placement Z

# same 
#oripl_X = sel[0].Placement.Base.x                                        # decode Placement X
#oripl_Y = sel[0].Placement.Base.y                                        # decode Placement Y
#oripl_Z = sel[0].Placement.Base.z                                        # decode Placement Z
 
App.Console.PrintMessage("oripl_X        : "+str(oripl_X)+"\n")
App.Console.PrintMessage("oripl_Y        : "+str(oripl_Y)+"\n")
App.Console.PrintMessage("oripl_Z        : "+str(oripl_Z)+"\n\n")
##################################################################################

# give the placement rotation of the object selected (x, y, z, angle rotation)
sel = FreeCADGui.Selection.getSelection()                                 # select object with getSelection()
rotation = sel[0].Placement.Rotation                                      # decode Placement Rotation
App.Console.PrintMessage("rotation              : "+str(rotation)+"\n\n")
##################################################################################

# give the placement rotation of the object selected (x, y, z, angle rotation)
sel = FreeCADGui.Selection.getSelection()                                 # select object with getSelection()
pl = sel[0].Shape.Placement.Rotation                                      # decode Placement Rotation other method
App.Console.PrintMessage("Placement Rot         : "+str(pl)+"\n\n")
##################################################################################

# give the rotation of the object selected (angle rotation)
sel = FreeCADGui.Selection.getSelection()                                 # select object with getSelection()
pl = sel[0].Shape.Placement.Rotation.Angle                                # decode Placement Rotation Angle
App.Console.PrintMessage("Placement Rot Angle   : "+str(pl)+"\n\n")
##################################################################################

# give the rotation.Q of the object selected (angle rotation in Radian) for convert: math.degrees(angleInRadian)
sel = FreeCADGui.Selection.getSelection()                                 # select object with getSelection()
Rot   = sel[0].Placement.Rotation.Q                                       # Placement Rotation Q
App.Console.PrintMessage("Rot           : "+str(Rot)+ "\n")
 
Rot_0 = sel[0].Placement.Rotation.Q[0]                                    # decode Placement Rotation Q
App.Console.PrintMessage("Rot_0         : "+str(Rot_0)+ " rad ,  "+str(180 * Rot_0 / 3.1416)+" deg "+"\n") # or math.degrees(angle)
 
Rot_1 = sel[0].Placement.Rotation.Q[1]                                    # decode Placement Rotation 1
App.Console.PrintMessage("Rot_1         : "+str(Rot_1)+ " rad ,  "+str(180 * Rot_1 / 3.1416)+" deg "+"\n") # or math.degrees(angle)
 
Rot_2 = sel[0].Placement.Rotation.Q[2]                                    # decode Placement Rotation 2
App.Console.PrintMessage("Rot_2         : "+str(Rot_2)+ " rad ,  "+str(180 * Rot_2 / 3.1416)+" deg "+"\n") # or math.degrees(angle)

Rot_3 = sel[0].Placement.Rotation.Q[3]                                    # decode Placement Rotation 3
App.Console.PrintMessage("Rot_3         : "+str(Rot_3)+"\n\n")

Rot_Axis = sel[0].Placement.Rotation.Axis                                 # Placement Rotation .Axis
App.Console.PrintMessage("Rot_Axis      : "+str(Rot_Axis)+ "\n")
 
Rot_Angle = sel[0].Placement.Rotation.Angle                               # Placement Rotation .Angle
App.Console.PrintMessage("Rot_Angle     : "+str(Rot_Angle)+ "\n\n")
##################################################################################

# give the rotation of the object selected toEuler (angle rotation in degrees)
sel = FreeCADGui.Selection.getSelection()                             # select object with getSelection()
angle   = sel[0].Shape.Placement.Rotation.toEuler()                   # angle Euler
App.Console.PrintMessage("Angle          : "+str(angle)+"\n")
Yaw   = sel[0].Shape.Placement.Rotation.toEuler()[0]                  # decode angle Euler Yaw (Z) lacet (alpha)
App.Console.PrintMessage("Yaw            : "+str(Yaw)+"\n")
Pitch = sel[0].Shape.Placement.Rotation.toEuler()[1]                  # decode angle Euler Pitch (Y) tangage (beta)
App.Console.PrintMessage("Pitch          : "+str(Pitch)+"\n")
Roll  = sel[0].Shape.Placement.Rotation.toEuler()[2]                  # decode angle Euler Roll (X) roulis (gamma)
App.Console.PrintMessage("Roll           : "+str(Roll)+"\n\n")
##################################################################################

# find Midpoint of the selected line
import Draft, DraftGeomUtils
sel = FreeCADGui.Selection.getSelection()
vecteur = DraftGeomUtils.findMidpoint(sel[0].Shape.Edges[0])              # find Midpoint
App.Console.PrintMessage(vecteur)
Draft.makePoint(vecteur)
##################################################################################
```


</div>


</div>


{{Top}}

### Ricerca manuale di un elemento dall\'etichetta 


```python
# Extract the coordinate X,Y,Z and Angle giving the label (here "Cylindre")
App.Console.PrintMessage("Base.x       : "+str(FreeCAD.ActiveDocument.getObjectsByLabel("Cylindre")[0].Placement.Base.x)+"\n")
App.Console.PrintMessage("Base.y       : "+str(FreeCAD.ActiveDocument.getObjectsByLabel("Cylindre")[0].Placement.Base.y)+"\n")
App.Console.PrintMessage("Base.z       : "+str(FreeCAD.ActiveDocument.getObjectsByLabel("Cylindre")[0].Placement.Base.z)+"\n")
App.Console.PrintMessage("Base.Angle   : "+str(FreeCAD.ActiveDocument.getObjectsByLabel("Cylindre")[0].Placement.Rotation.Angle)+"\n\n")
##################################################################################

```


<div class="mw-translate-fuzzy">

Note: Di solito gli angoli sono espressi in radianti da convertire con:


</div>

1.  da gradi a radianti :
    -   angolo in radianti = **pi \* (angolo in gradi) / 180**
    -   angolo in radianti = math.radians(angolo in gradi)
2.  da radianti a gradi :
    -   angolo in gradi = **180 \* (angolo in radianti) / pi**
    -   angolo in gradi = math.degrees(angolo in radianti)


{{Top}}

### Coordinate cartesiane 

Questo codice visualizza le coordinate cartesiane dell\'elemento selezionato.

Modificare il valore di \"numberOfPoints\" se si desidera un diverso numero di punti (modificare la precisione)


```python
numberOfPoints = 100                                                         # Decomposition number (or precision you can change)
selectedEdge = FreeCADGui.Selection.getSelectionEx()[0].SubObjects[0].copy() # select one element
points  = selectedEdge.discretize(numberOfPoints)                            # discretize the element
i=0
for p in points:                                                             # list and display the coordinates
    i+=1
    print( i, " X", p.x, " Y", p.y, " Z", p.z)
```

Altro metodo per visualizzare \"Int\" e \"Float\" (interi e valori in virgola mobile)


```python
import Part
from FreeCAD import Base

c=Part.makeCylinder(2,10)        # create the circle
Part.show(c)                     # display the shape

# slice accepts two arguments:
#+ the normal of the cross section plane
#+ the distance from the origin to the cross section plane. Here you have to find a value so that the plane intersects your object
s=c.slice(Base.Vector(0,1,0),0)  # 

# here the result is a single wire
# depending on the source object this can be several wires
s=s[0]

# if you only need the vertexes of the shape you can use
v=[]
for i in s.Vertexes:
    v.append(i.Point)

# but you can also sub-sample the section to have a certain number of points (int) ...
p1=s.discretize(20)
ii=0
for i in p1:
    ii+=1
    print( i )                                             # Vector()
    print( ii, ": X:", i.x, " Y:", i.y, " Z:", i.z )       # Vector decode
Draft.makeWire(p1,closed=False,face=False,support=None)    # to see the difference accuracy (20)

## uncomment to use
#import Draft
#Draft.downgrade(App.ActiveDocument.ActiveObject,delete=True)  # first transform the DWire in Wire         "downgrade"
#Draft.downgrade(App.ActiveDocument.ActiveObject,delete=True)  # second split the Wire in single objects   "downgrade"
#
##Draft.upgrade(FreeCADGui.Selection.getSelection(),delete=True) # to attach lines contiguous SELECTED use "upgrade"


# ... or define a sampling distance (float)
p2=s.discretize(0.5)
ii=0
for i in p2:
    ii+=1
    print( i )                                             # Vector()
    print( ii, ": X:", i.x, " Y:", i.y, " Z:", i.z )       # Vector decode 
Draft.makeWire(p2,closed=False,face=False,support=None)  # to see the difference accuracy (0.5)

## uncomment to use
#import Draft
#Draft.downgrade(App.ActiveDocument.ActiveObject,delete=True)  # first transform the DWire in Wire         "downgrade"
#Draft.downgrade(App.ActiveDocument.ActiveObject,delete=True)  # second split the Wire in single objects   "downgrade"
#
##Draft.upgrade(FreeCADGui.Selection.getSelection(),delete=True) # to attach lines contiguous SELECTED use "upgrade"

```


{{Top}}

### Selezionare tutti gli oggetti nel documento 


```python
import FreeCAD
for obj in FreeCAD.ActiveDocument.Objects:
    print( obj.Name )                               # display the object Name
    objName = obj.Name
    obj = App.ActiveDocument.getObject(objName)
    Gui.Selection.addSelection(obj)                 # select the object
```


{{Top}}

### Selezionare una faccia di un oggetto in base a Nome oggetto e Numero faccia 


```python
# select one face of the object
import FreeCAD, Draft
App=FreeCAD
nameObject = "Box"                             # objet
faceSelect = "Face3"                           # face to selection
loch=App.ActiveDocument.getObject(nameObject)  # objet
Gui.Selection.clearSelection()                 # clear all selection
Gui.Selection.addSelection(loch,faceSelect)    # select the face specified
s = Gui.Selection.getSelectionEx()
#Draft.makeFacebinder(s)                       # 
```


{{Top}}

### Ottienere il vettore normale di una faccia di un oggetto con Nome oggetto e Numero faccia (r.Q) 


```python
## normal of a face by giving the number of the face and the name of the object (rotation Q with yL, uV) = (App.Vector (x, y, z), angle))
## normal d'une face en donnant le numero de la face et le nom de l'objet (rotation Q avec yL, uV) = (App.Vector(x, y, z),angle))
from FreeCAD import Vector

numero_Face = 2      # number of the face searched (begin 0, 1, 2, 3 .....)
nomObjet    = "Box"  # object name
yL = Gui.ActiveDocument.getObject(nomObjet).Object.Shape.Faces[numero_Face].CenterOfMass
uv = Gui.ActiveDocument.getObject(nomObjet).Object.Shape.Faces[numero_Face].Surface.parameter(yL)

nv = Gui.ActiveDocument.getObject(nomObjet).Object.Shape.Faces[numero_Face].normalAt(uv[0], uv[1])
direction = yL.sub(nv + yL)
print("Direction  : ",direction)

r = App.Rotation(App.Vector(0,0,1),direction)
print("Rotation   : ", r)
print("Rotation Q : ", r.Q)

```


{{Top}}

### Get the normal vector of a face of an object by Name object and number of Face 


```python
numero_Face = 2       # number of the face searched (begin 0, 1, 2, 3 .....)
nomObjet    = "Box"   # object name
normal      = Gui.ActiveDocument.getObject(nomObjet).Object.Shape.Faces[numero_Face].normalAt(0,0)
print("Face"+str(numero_Face), " : ", normal)

```


{{Top}}

### Get the normal vector of an object selected and number of Face 


```python
## normal of a face by giving the number of the face of the selected object
selectionObjects = FreeCADGui.Selection.getSelection()     
numero_Face = 3    # numero de la face recherchee
normal = selectionObjects[0].Shape.Faces[numero_Face].normalAt(0,0)
print(normal)
# selectionne la face numerotee
Gui.Selection.clearSelection()
Gui.Selection.addSelection(selectionObjects[0],"Face"+str(numero_Face))
```


{{Top}}

### Ottenere il vettore normale alla superficie 

Questo esempio mostra come trovare vettore normale alla superficie trovando prima i parametri u, v di un punto sulla superficie e utilizzando poi i parametri u, v per trovare il vettore normale


```python
def normal(self):
   ss=FreeCADGui.Selection.getSelectionEx()[0].SubObjects[0].copy()#SubObjects[0] is the edge list
   points  = ss.discretize(3.0)#points on the surface edge, 
             #this example just use points on the edge for example. 
             #However point is not necessary on the edge, it can be anywhere on the surface. 
   face=FreeCADGui.Selection.getSelectionEx()[0].SubObjects[1]
   for pp in points:
      pt=FreeCAD.Base.Vector(pp.x,pp.y,pp.z)#a point on the surface edge
      uv=face.Surface.parameter(pt)# find the surface u,v parameter of a point on the surface edge
      u=uv[0]
      v=uv[1]
      normal=face.normalAt(u,v)#use u,v to find normal vector
      print( normal)
      line=Part.makeLine((pp.x,pp.y,pp.z), (normal.x,normal.y,normal.z))
      Part.show(line)
```


{{Top}}

### Ottieni il vettore normale di una superficie da un file STL 


```python
def getNormal(cb):
    if cb.getEvent().getState() == coin.SoButtonEvent.UP:
        pp = cb.getPickedPoint()
        if pp:
            vec = pp.getNormal().getValue()
            index = coin.cast(pp.getDetail(), "SoFaceDetail").getFaceIndex()
            print("Normal: {}, Face index: {}".format(str(vec), index))

from pivy import coin
meth=Gui.ActiveDocument.ActiveView.addEventCallbackPivy(coin.SoMouseButtonEvent.getClassTypeId(), getNormal)
```

hai finito quindi fai questo per uscire:


```python
Gui.ActiveDocument.ActiveView.removeEventCallbackPivy(coin.SoMouseButtonEvent.getClassTypeId(), meth)
```


{{Top}}

### Creare un oggetto della posizione della fotocamera 


```python
# create one object of the position to camera with "getCameraOrientation()"
# the object is still facing the screen
import Draft

plan = FreeCADGui.ActiveDocument.ActiveView.getCameraOrientation()
plan = str(plan)
###### extract data
a    = ""
for i in plan:
    if i in ("0123456789e.- "):
        a+=i
a = a.strip(" ")
a = a.split(" ")
####### extract data

#print( a)
#print( a[0])
#print( a[1])
#print( a[2])
#print( a[3])

xP = float(a[0])
yP = float(a[1])
zP = float(a[2])
qP = float(a[3])

pl = FreeCAD.Placement()
pl.Rotation.Q = (xP,yP,zP,qP)         # rotation of object
pl.Base = FreeCAD.Vector(0.0,0.0,0.0) # here coordinates XYZ of Object
rec = Draft.makeRectangle(length=10.0,height=10.0,placement=pl,face=False,support=None) # create rectangle
#rec = Draft.makeCircle(radius=5,placement=pl,face=False,support=None)                   # create circle
print( rec.Name)
```

stesso codice semplificato


```python
import Draft
pl = FreeCAD.Placement()
pl.Rotation = FreeCADGui.ActiveDocument.ActiveView.getCameraOrientation()
pl.Base = FreeCAD.Vector(0.0,0.0,0.0)
rec = Draft.makeRectangle(length=10.0,height=10.0,placement=pl,face=False,support=None)
```


{{Top}}

### Leggere e scrivere una Expression 


```python
import Draft
doc = FreeCAD.ActiveDocument

pl=FreeCAD.Placement()
pl.Rotation.Q=(0.0,-0.0,-0.0,1.0)
pl.Base=FreeCAD.Vector(0.0,0.0,0.0)
obj = Draft.makeCircle(radius=1.0,placement=pl,face=False,support=None)    # create circle

print( obj.PropertiesList )                                                  # properties disponible in the obj

doc.getObject(obj.Name).setExpression('Radius', u'2mm')                    # modify the radius
doc.getObject(obj.Name).setExpression('Placement.Base.x', u'10mm')         # modify the placement 
doc.getObject(obj.Name).setExpression('FirstAngle', u'90')                 # modify the first angle
doc.recompute()

expressions = obj.ExpressionEngine                                         # read the expression list
print( expressions)

for i in expressions:                                                      # list and separate the data expression
    print( i[0]," = ",i[1])

```


{{Top}}

### Create a Sketch on a Surface in PartDesign 

This snippet can be useful, if you want to create a sketch on a surface in PartDesign from inside a macro. Note, that body might be None, if no active body is selected and that the Selection might be empty.


```python
body = Gui.ActiveDocument.ActiveView.getActiveObject('pdbody')
first_selection = Gui.Selection.getSelectionEx()[0]

feature = first_selection.Object
face_name = first_selection.SubElementNames[0]

sketch = App.ActiveDocument.addObject('Sketcher::SketchObject','MySketch')
body.addObject(sketch)
sketch.MapMode = 'FlatFace'
sketch.Support = (feature, face_name)

App.ActiveDocument.recompute()
```


{{Top}}

### How to Simulate a Mouse Click at a given Coordinate 

The position is relative to the GL widget. See [forum thread](https://forum.freecadweb.org/viewtopic.php?f=22&t=44008).


```python
from PySide2 import QtCore
from PySide2 import QtGui
from PySide2 import QtWidgets

mw = Gui.getMainWindow()
gl = mw.findChild(QtWidgets.QOpenGLWidget)
me = QtGui.QMouseEvent(QtCore.QEvent.MouseButtonRelease, QtCore.QPoint(800,300), QtCore.Qt.LeftButton, QtCore.Qt.LeftButton, QtCore.Qt.NoModifier)

app = QtWidgets.QApplication.instance()
app.sendEvent(gl, me)
```

If you have a 3d point and want to get the 2d point on the opengl widget then use this:


```python
from PySide2 import QtCore
from PySide2 import QtGui
from PySide2 import QtWidgets
from FreeCAD import Base

x, y, z, = 10,10,10
v = Gui.ActiveDocument.ActiveView
point3d = Base.Vector(x, y, z)
point2d = v.getPointOnScreen(point3d)
size = v.getSize()
coordX = point2d[0]
coordY = size[1] - point2d[1]

me = QtGui.QMouseEvent(QtCore.QEvent.MouseButtonRelease, QtCore.QPoint(coordX,coordY), QtCore.Qt.LeftButton, QtCore.Qt.LeftButton, QtCore.Qt.NoModifier)

```


{{Top}}

### How to create a face with holes using Python API 

This snippet demonstrates how to create a face with internal holes through the Python API. See [forum thread](https://forum.freecadweb.org/viewtopic.php?f=22&t=56308).


```python
import FreeCAD, Part

# Create poles that will define the Face
pts = [(-2, 2, 0),
       (0, 2, 1),
       (2, 2, 0),
       (2, -2, 0),
       (0, -2, 1),
       (-2, -2, 0)]

bs = Part.BSplineCurve()
bs.buildFromPoles(pts, True)  # True makes this periodic/closed

# Make the Face from the curve
myFace = Part.makeFilledFace([bs.toShape()])

# Create geometry for holes that will be cut in the surface
hole0 = Part.Geom2d.Circle2d(FreeCAD.Base.Vector2d(0,0), 1.0)
hole1 = Part.Geom2d.Circle2d(FreeCAD.Base.Vector2d(0,1.5), 0.1)

edge0 = hole0.toShape(myFace)
edge1 = hole1.toShape(myFace)
wireb = Part.Wire(bs.toShape())
wire0 = Part.Wire(edge0)
wire1 = Part.Wire(edge1)

# Cut holes in the face
myFace.cutHoles([wire0])
myFace.validate()  # This is required
myFace.cutHoles([wire1])
myFace.validate()

Part.show(myFace)
```


{{Top}}

## Coin3D

See [Coin3d snippets](Coin3d_snippets.md)

## Correlazioni

-   [Oggetti da script](Scripted_objects/it.md)
-   [Macro](Macros/it.md)


{{Top}}


{{Powerdocnavi

}}

[Category:Developer Documentation{{\#translation:}}](Category:Developer_Documentation.md) [Category:Python Code{{\#translation:}}](Category:Python_Code.md)
