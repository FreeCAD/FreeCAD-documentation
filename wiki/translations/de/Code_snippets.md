# Code snippets/de
{{TOCright}}

## Einführung

Diese Seite enthält Beispiele, Stücke, Brocken von FreeCAD Python Code, die aus den Erfahrungen und Diskussionen der Benutzer auf den [Foren](https://forum.freecadweb.org/viewforum.php?f=22) gesammelt wurden. Lies und verwende sie als Ausgangspunkt für deine eigenen Skripte\...

## Schnipsel

### Eine typische InitGui.py Datei 

Jedes Modul muss, neben Deiner Hauptmoduldatei, eine InitGui.py Datei enthalten, die verantwortlich ist für das Einfügen des Moduls in die übergeordnete grafische Benutzeroberfläche. Dies ist ein Beispiel einer einfachen Datei.


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

### Eine typische Moduldatei 

Dies ist ein Beispiel für eine Hauptmoduldatei, die alles enthält, was dein Modul macht. Es handelt sich um die Datei Scripts.py, die durch das vorherige Beispiel aufgerufen wurde. Du kannst alle deine benutzerdefinierten Befehle hier haben.


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

### Importieren eines neuen Dateityps 

Es ist einfach, einen Importeur für einen neuen Dateityp in FreeCAD zu erstellen. FreeCAD berücksichtigt nicht, dass du Daten in ein geöffnetes Dokument importierst, sondern vielmehr, dass du den neuen Dateityp einfach direkt öffnen kannst. Was du also tun musst, ist, die neue Dateierweiterung zur Liste der bekannten Erweiterungen in FreeCAD hinzuzufügen und den Code zu schreiben, der die Datei liest und die von dir gewünschten FreeCAD Objekte erzeugt:

Diese Zeile muss zur Datei InitGui.py hinzugefügt werden, um die neue Erweiterung zur Liste hinzuzufügen:


```python
# Assumes Import_Ext.py is the file that has the code for opening and reading .ext files
FreeCAD.addImportType("Your new File Type (*.ext)","Import_Ext") 
```

Dann in der Datei Import_Ext.py:


```python
def open(filename): 
   doc=App.newDocument()
   # here you do all what is needed with filename, read, classify data, create corresponding FreeCAD objects
   doc.recompute()
```

Das Exportieren deines Dokuments in einen neuen Dateityp funktioniert auf demselben Weg, nur dass Du verwendest:

FreeCAD.addExportType("Dein neuer Dateityp (*.ext)", "Export_Ext")


{{Top}}

### Hinzufügen einer Linie 

Eine Linie hat einfach 2 Punkte.


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

### Hinzufügen eines Polygons 

Ein Polygon ist einfach ein Satz verbundener Liniensegmente (in AutoCAD eine Polylinie). Es muss nicht geschlossen sein.


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

### Hinzufügen und Entfernen eines Objekts in/aus eine(r) Gruppe 


```python
doc=App.activeDocument() 
grp=doc.addObject("App::DocumentObjectGroup", "Group") 
lin=doc.addObject("Part::Feature", "Line")
grp.addObject(lin) # adds the lin object to the group grp
grp.removeObject(lin) # removes the lin object from the group grp
```

Hinweis: Du kannst auch andere Gruppen zu einer Gruppe hinzufügen\... {{Top}}

### Hinzufügen eines Polygonnetzes 


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

### Hinzufügen eines Bogens oder eines Kreises 


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

### Zugriff und Änderung der Darstellung eines Objekts 

Jedes Objekt in einem FreeCAD Dokument hat ein zugeordnetes Ansichtsdarstellungsobjekt, das alle Parameter speichert, die definieren, wie das Objekt erscheint: d.h. Farbe, Linienbreite, usw\... Siehe auch [Liste die Komponenten eines Objekts auf](#List_the_components_of_an_object/de.md) Schnipsel unten


```python
gad = Gui.activeDocument() # access the active document containing all 
                           # view representations of the features in the
                           # corresponding App document 

v = gad.getObject("Cube")  # access the view representation to the Mesh feature 'Cube' 
v.ShapeColor               # prints the color to the console 
v.ShapeColor=(1.0,1.0,1.0) # sets the shape color to white
```


{{Top}}

### Ersetze die Form der Maus durch ein Bild 


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

### Ersetze die Form der Maus durch ein Bild einschliesslich (Kreuz) 

Das Bild wird durch Gimp erstellt exportiert in eine .XPM-Datei. Kopiere und verwende den Code zwischen der Klammer **\"{\"** Code zu kopieren **\"}\"**


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

### Beobachten von Kameraänderungen im 3D-Betrachter über Python 

Dies erreicht man, indem man einen Node-Sensor zur Kamera hinzufügt.


```python
from pivy import coin
def callback(*args):
    cam, sensor = args
    print()
    print("Cam position : {}".format(cam.position.getValue().getValue()))
    print("Cam rotation : {}".format(cam.orientation.getValue().getValue()))

camera_node = Gui.ActiveDocument.ActiveView.getCameraNode()
node_sensor = coin.SoNodeSensor(callback, camera_node)
node_sensor.attach(camera_node)```


{{Top}}

### Beobachten von Mausereignissen im 3D Betrachter über Python 

Das Inventor Framework ermöglicht es, einen oder mehrere Aufrufknoten zum Szenegraphen des Betrachters hinzuzufügen. Standardmäßig wird in FreeCAD ein Aufrufknoten vom Betrachter installiert, der es erlaubt, globale oder statische C++ Funktionen hinzuzufügen. In der entsprechenden Python Bindung werden einige Methoden zur Verfügung gestellt, um diese Technik aus dem Python Code heraus zu nutzen.


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

Wähle nun irgendwo auf der Fläche im 3D Betrachter und beobachte die Meldungen im Ausgabefenster. Um die Beobachtung zu beenden, rufe einfach auf


```python
v.removeEventCallback("SoMouseButtonEvent",c)
```

Folgende Ereignistypen werden unterstützt

-   SoEvent \-- alle Arten von Ereignissen
-   SoButtonEvent \-- alle Maus- und Schlüsselereignisse
-   SoLocation2Event \-- 2D Bewegungsereignisse (normalerweise Mausbewegungen)
-   SoMotion3Event \-- 3D Bewegungsereignisse (normalerweise Spaceball)
-   SoKeyboardEvent \-- Tastendruck auf und ab Ereignisse
-   SoMouseButtonEvent \-- Maustaste nach unten und oben Ereignisse
-   SoSpaceballButtonEvent \-- Spaceball Taste runter und hoch Ereignisse

Die Python Funktion, die mit addEventCallback() registriert werden kann, erwartet ein Verzeichnis. Abhängig vom beobachteten Ereignis kann das Verzeichnis verschiedene Schlüssel enthalten.

Für alle Ereignisse hat es die Schlüssel:

-   Typ \-- der Name des Veranstaltungstyps, z.B. SoMouseEvent, SoLocation2Event, \.....
-   Zeit \-- die aktuelle Zeit als Zeichenkette
-   Position \-- ein Tupel von zwei ganzen Zahlen, Mausposition
-   ShiftDown \-- ein boolescher, wahrer Wert, wenn Shift gedrückt wurde, ansonsten falsch.
-   CtrlDown \-- ein Boolescher, true, wenn Ctrl gedrückt wurde, ansonsten false.
-   AltDown \-- a boolean, true if Alt was pressed otherwise false

Für alle Tastenereignisse, d.h. Tastatur-, Maus- oder Spaceballereignisse.

-   Zustand \-- Eine Zeichenkette\'UP\', wenn die Taste oben war,\'DOWN\', wenn sie unten war, oder\'UNKNOWN\' für alle anderen Fälle.

Für Tastaturereignisse:

-   Taste \-- ein Zeichen der gedrückten Taste

Für das Ereignis der Maustaste

-   Taste \-- Die gedrückte Taste kann TASTE1, \...., TASTE5 oder JEDER sein.

Für Spaceball-Events:

-   Taste \-- Die gedrückte Taste kann TASTE1, \...., TASTE7 oder JEDER sein.

Und schließlich Bewegungsereignisse:

-   Übersetzung \-- ein Tupel von drei Gleitkommazahlen.
-   Rotation \-- ein Quaternion für die Drehung, d.h. ein Tupel von vier Gleitkommazahlen.


{{Top}}

### Gedrückte Tasten anzeigen und Ereignisbefehl 

Dieses Makro zeigt in der Berichtsansicht die gedrückten Tasten und alle Ereignisse an.


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

### Handhabung des Szenegraphen in Python 

Es ist auch möglich, den Szenegraphen in Python zu bekommen und zu ändern, mit dem Modul \'pivy\' - einer Python Bindung für Coin.


```python
from pivy.coin import *                # load the pivy module
view = Gui.ActiveDocument.ActiveView   # get the active viewer
root = view.getSceneGraph()            # the root is an SoSeparator node
root.addChild(SoCube())
view.fitAll()
```

Die Python API von pivy wird mit dem Tool SWIG erstellt. Da wir in FreeCAD einige selbstgeschriebene Knoten verwenden, können Sie diese nicht direkt in Python erstellen. Es ist jedoch möglich, einen Knoten über seinen internen Namen anzulegen. Eine Instanz vom Typ\'SoFCSelection\' kann erzeugt werden mit


```python
type = SoType.fromName("SoFCSelection")
node = type.createInstance()
```


{{Top}}

### Hinzufügen und Entfernen von Objekten zum/vom Szenegraphen 

Hinzufügen neuer Knoten zum Szenegraphen kann auf diese Weise erfolgen. Achte darauf, dass immer einen SoSeparator hinzufügen, der die Geometrie, Koordinaten und Materialinformationen eines Objekts enthält. Das folgende Beispiel fügt eine rote Linie von (0,0,0,0) bis (10,0,0,0) hinzu:


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

Um es zu entfernen, stelle es einfach aus: 
```python
sg.removeChild(no)
``` {{Top}}


<div class="mw-collapsible mw-collapsed toccolours">

### Speichern des SzenenGraphs in 3 Serien von 36 Dateien 

Sieh dir das Codeschnipsel durch Erweitern dieses Abschnitts an


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

### Hinzufügen von benutzerdefinierten Assistenten zur Oberfläche 

Du kannst benutzerdefinierte Widgets mit dem Qt Designer erstellen, sie in ein Python-Skript umwandeln und sie dann mit PySide in die FreeCAD Benutzeroberfläche laden.

Der Python Code, der vom Ui Python Compiler erzeugt wird (das Tool, das qt-designer .ui Dateien in Python Code umwandelt), sieht im Allgemeinen so aus (es ist einfach, Du kannst ihn auch direkt in Python kodieren):


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

Dann musst Du nur noch einen Verweis auf das FreeCAD Qt Fenster erstellen, ein benutzerdefiniertes Widget einfügen und dieses Widget mit dem gerade erstellten Ui Code in Dein Widget \"transformieren\":


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

### Hinzufügen eines Reiters zur Comboansicht 

Der folgende Code erlaubt dir, einen Reiter zur [Combo Ansicht](Combo_view/de.md) hinzuzufügen, getrennt von den bereits vorhandenen \"Modell\" und \"Aufgaben Reitern . Er verwendet auch das `uic` Modul, um eine UI Datei direkt in diesen Reiter zu laden.


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

### Aktivieren oder Deaktivieren eines Fensters 

Dieses Skript bietet die Möglichkeit, das UI von der Python Konsole aus zu verändern, um verschiedene Komponenten in der FreeCAD [Benutzeroberfläche](interface/de.md) ein-/auszublenden, wie z.B:

-   [Berichtsansicht](Report_view/de.md)
-   [Baumansicht](Tree_view/de.md)
-   [Eigenschaftsansicht](Property_editor/de.md)
-   [Auswahlansicht](Selection_view/de.md)
-   [Combo Ansicht](Combo_view/de.md)
-   [Python Konsole](Python_console/de.md)
-   EntwurfWerkzeugleiste


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

### Öffnen einer angepassten Webseite 


```python
import WebGui
WebGui.openBrowser("http://www.example.com")
```


{{Top}}

### Erfassung des HTML Inhalts einer geöffneten Webseite 


```python
from PySide import QtGui,QtWebKit
a = QtGui.qApp
mw = a.activeWindow()
v = mw.findChild(QtWebKit.QWebFrame)
html = unicode(v.toHtml())
print( html)
```


{{Top}}

### Abruf der Koordinaten von 3 ausgewählten Punkten oder Objekten 


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

### Liste alle Objekte 


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

### Liste die Abmessungen eines Objekts, angegeben durch seinen Namen 


```python
for edge in FreeCAD.ActiveDocument.MyObjectName.Shape.Edges: # replace "MyObjectName" for list
    print( edge.Length)
```


{{Top}}

### Der Mausklickhandlung innewohnende Funktion 

Hier mit **SelObserver** auf einem Objekt auswählen


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

Anderes Beispiel mit **ViewObserver** auf einem Objekt auswählen oder ansehen


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

### Finde/Wähle alle Elemente unter dem Mauszeiger 


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

### Liste die Komponenten eines Objektes auf 

Diese Funktion listet die Komponenten eines Objekts auf und extrahiert:

-   diesem Objekt seine XYZ Koordinaten,
-   seine Kanten und ihre Längen Massenmittelpunkt und Koordinaten
-   seine Flächen und deren Massenzentrum
-   seine Flächen und deren Oberflächen und Koordinaten


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

### Liste die EigenschaftenListe 


```python
import FreeCADGui
from FreeCAD import Console
o = App.ActiveDocument.ActiveObject
op = o.PropertiesList
for p in op:
    Console.PrintMessage("Property: "+ str(p)+ " Value: " + str(o.getPropertyByName(p))+"\r\n")
```


{{Top}}

### Hinzufügen eines einzelnen Eigenschaftskommentars 


```python
import Draft
obj = FreeCADGui.Selection.getSelection()[0]
obj.addProperty("App::PropertyString","GComment","Draft","Font name").GComment = "Comment here"
App.activeDocument().recompute()
```


{{Top}}


<div class="mw-collapsible mw-collapsed toccolours">

### Suche und Datenentnahme 

Beispiele für Forschung und Entschlüsselung von Informationen über ein Objekt.

Jeder Abschnitt ist unabhängig und durch \"###############\" getrennt und kann direkt in die Python Konsole oder in ein Makro kopiert werden oder dieses Makro verwenden. Die Beschreibung des Makros im Kommentar.

Anzeige im \"Berichtsansichts\" Fenster (Ansicht \> Ansichten \> Berichtsansicht)


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

### Manuelle Suche eines Elements mit Kennzeichnung 


```python
# Extract the coordinate X,Y,Z and Angle giving the label (here "Cylindre")
App.Console.PrintMessage("Base.x       : "+str(FreeCAD.ActiveDocument.getObjectsByLabel("Cylindre")[0].Placement.Base.x)+"\n")
App.Console.PrintMessage("Base.y       : "+str(FreeCAD.ActiveDocument.getObjectsByLabel("Cylindre")[0].Placement.Base.y)+"\n")
App.Console.PrintMessage("Base.z       : "+str(FreeCAD.ActiveDocument.getObjectsByLabel("Cylindre")[0].Placement.Base.z)+"\n")
App.Console.PrintMessage("Base.Angle   : "+str(FreeCAD.ActiveDocument.getObjectsByLabel("Cylindre")[0].Placement.Rotation.Angle)+"\n\n")
##################################################################################

```

**Hinweis:** Normalerweise sind die Winkel im Bogenmaß angegeben. Um sie zu konvertieren:

1.  Winkel in Grad zu Bogenmaß :
    -   Winkel im Bogenmaß = **pi \* (Winkel in Grad) / 180**
    -   Winkel im Bogenmaß = math.radians(Winkel in Grad)
2.  Winkel im Bogenmaß in Grad :
    -   Winkel in Grad = **180 \* (Winkel im Bogenmaß) / pi**
    -   Winkel in Grad = math.degrees(Winkel im Bogenmaß)


{{Top}}

### Kartesische Koordinaten 

Dieser Code zeigt die kartesischen Koordinaten des ausgewählten Elements an.

Ändere den Wert von \"numberOfPoints\", wenn du eine andere Anzahl von Punkten (Präzision) willst


```python
numberOfPoints = 100                                                         # Decomposition number (or precision you can change)
selectedEdge = FreeCADGui.Selection.getSelectionEx()[0].SubObjects[0].copy() # select one element
points  = selectedEdge.discretize(numberOfPoints)                            # discretize the element
i=0
for p in points:                                                             # list and display the coordinates
    i+=1
    print( i, " X", p.x, " Y", p.y, " Z", p.z)
```

Andere Methodenanzeige bei \"Int\" und \"Float\"


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

### Auswahl aller Objekte im Dokument 


```python
import FreeCAD
for obj in FreeCAD.ActiveDocument.Objects:
    print( obj.Name )                               # display the object Name
    objName = obj.Name
    obj = App.ActiveDocument.getObject(objName)
    Gui.Selection.addSelection(obj)                 # select the object
```


{{Top}}

### Auswahl einer Fläche eines Objekts nach Objektname und Flächennummer 


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

### Ermittelt den Normalenvektor einer Fläche eines Objekts nach Name Objekt und Nummer Fläche (r.Q) 


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

### Ermittelt den Normalenvektor einer Fläche eines Objekts durch Name Objekt und Nummer der Fläche 


```python
numero_Face = 2       # number of the face searched (begin 0, 1, 2, 3 .....)
nomObjet    = "Box"   # object name
normal      = Gui.ActiveDocument.getObject(nomObjet).Object.Shape.Faces[numero_Face].normalAt(0,0)
print("Face"+str(numero_Face), " : ", normal)

```


{{Top}}

### Ermittelt den Normalenvektor eines gewählten Objekts und die Nummer der Fläche 


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

### Ermittelt den Normalenvektor auf der Oberfläche 

Dieses Beispiel zeigt, wie man einen Normalenvektor auf der Oberfläche findet, indem man die u,v Parameter eines Punktes auf der Oberfläche findet und die u,v Parameter benutzt, um den Normalenvektor zu finden


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

### Ermittelt den Normalenvektor einer Fläche aus einer STL Datei 


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

Du bist fertig gehst dann zum Beenden:


```python
Gui.ActiveDocument.ActiveView.removeEventCallbackPivy(coin.SoMouseButtonEvent.getClassTypeId(), meth)
```


{{Top}}

### Erstellt ein Objekt zur Position der Kamera 


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

hier gleicher Code vereinfacht


```python
import Draft
pl = FreeCAD.Placement()
pl.Rotation = FreeCADGui.ActiveDocument.ActiveView.getCameraOrientation()
pl.Base = FreeCAD.Vector(0.0,0.0,0.0)
rec = Draft.makeRectangle(length=10.0,height=10.0,placement=pl,face=False,support=None)
```


{{Top}}

### Lese und schreibe einen Ausdruck 


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

### Erstelle eine Skizze auf einer Oberfläche in PartDesign 

Dieser Schnipsel kann nützlich sein, wenn du eine Skizze auf einer Oberfläche in PartDesign aus dem Inneren eines Makros heraus erstellen möchtest. Beachte, dass der Körper möglicherweise Keiner ist, wenn kein aktiver Körper ausgewählt ist, und dass die Auswahl möglicherweise leer ist.


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

### Wie man einen Mausklick auf eine gegebene Koordinate simuliert 

Die Position ist relativ zum GL Widget. Siehe [Forumsbeitrag](https://forum.freecadweb.org/viewtopic.php?f=22&t=44008).


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

Wenn du einen 3D Punkt hast und den 2D Punkt auf dem Opengl Assistenten bekommen möchtest, verwende dies:


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

### Erstellen einer Fläche mit Löchern mit der Python-API 

Dieser Schnipsel demonstriert, wie eine Fläche mit internen Löchern mit der Python-API erstellt werden kann. Siehe auch [forum thread](https://forum.freecadweb.org/viewtopic.php?f=22&t=56308).


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

### FreeCAD schließen und neu starten 


```python
import PySide2 
from PySide2 import QtWidgets, QtCore, QtGui

def restart_freecad():
    """Shuts down and restarts FreeCAD"""

    args = QtWidgets.QApplication.arguments()[1:]
    if FreeCADGui.getMainWindow().close():
        QtCore.QProcess.startDetached(
            QtWidgets.QApplication.applicationFilePath(), args
        )
```


{{Top}}

## Coin3D

Siehe [Coin3d Schnippsel](Coin3d_snippets/de.md)

## Verwandt

-   [geskriptete Objekte](Scripted_objects/de.md)
-   [Makros](Macros/de.md)


{{Top}}



---
![](images/Right_arrow.png) [documentation index](../README.md) > [Developer Documentation](Category_Developer Documentation.md) > [Python Code](Category_Python Code.md) > Code snippets/de
