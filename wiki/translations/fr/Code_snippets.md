


{{TOCright}}

## Introduction

Cette page contient des exemples, des pièces, des extraits de code FreeCAD en Python, recueillis auprès d\'utilisateurs expérimentés et de discussions sur les [forums](https://forum.freecadweb.org/viewforum.php?f=22). Lisez les et utilisez les comme point de départ pour vos propres scripts\...

## Extraits

### Un fichier typique InitGui.py {#un_fichier_typique_initgui.py}

Chaque module doit contenir, en plus de votre fichier de module principal, un fichier InitGui.py, chargé d\'insérer le module dans l\'interface graphique principale. Ceci est un exemple simple.


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

### Un fichier module typique {#un_fichier_module_typique}

Ceci est un exemple de fichier de module principal, contenant tout ce que fait votre module. Il s\'agit du fichier Scripts.py appelé par l\'exemple précédent. Vous pouvez avoir toutes vos commandes personnalisées ici.


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

### Importer un nouveau type de fichier {#importer_un_nouveau_type_de_fichier}

Créer un importateur pour un nouveau type de fichier dans FreeCAD est facile. FreeCAD ne considère pas que vous importez des données dans un document ouvert mais plutôt que vous pouvez simplement ouvrir directement le nouveau type de fichier. Donc, ce que vous devez faire est d\'ajouter la nouvelle extension de fichier à la liste des extensions connues de FreeCAD et d\'écrire le code qui lira le fichier et créera les objets FreeCAD que vous voulez:

Cette ligne doit être ajoutée au fichier **InitGui.py** pour ajouter la nouvelle extension de fichier à la liste:


```python
# Assumes Import_Ext.py is the file that has the code for opening and reading .ext files
FreeCAD.addImportType("Your new File Type (*.ext)","Import_Ext") 
```

Puis, dans le fichier **Import\_Ext.py**, faites:


```python
def open(filename): 
   doc=App.newDocument()
   # here you do all what is needed with filename, read, classify data, create corresponding FreeCAD objects
   doc.recompute()
```

Pour exporter votre document avec une nouvelle extension, le fonctionnement est le même, mais vous devrez faire:

FreeCAD.addExportType("Your new File Type (*.ext)","Export_Ext")


{{Top}}

### Ajouter une ligne {#ajouter_une_ligne}

Une ligne a uniquement deux points.


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

### Ajouter un polygone {#ajouter_un_polygone}

Un polygone est simplement un ensemble de segments connnectés (une polyligne dans AutoCAD). Il n\'est pas obligatoirement fermé.


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

### Ajouter et supprimer un objet dans/d\'un groupe {#ajouter_et_supprimer_un_objet_dansdun_groupe}


```python
doc=App.activeDocument() 
grp=doc.addObject("App::DocumentObjectGroup", "Group") 
lin=doc.addObject("Part::Feature", "Line")
grp.addObject(lin) # adds the lin object to the group grp
grp.removeObject(lin) # removes the lin object from the group grp
```

Remarque: vous pouvez aussi ajouter d\'autres groupes à un groupe\... {{Top}}

### Ajouter une maille (Mesh) {#ajouter_une_maille_mesh}


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

### Ajouter un arc ou un cercle {#ajouter_un_arc_ou_un_cercle}


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

### Accéder et changer la représentation d\'un objet {#accéder_et_changer_la_représentation_dun_objet}

Chaque objet dans un document FreeCAD a un objet de représentation de vue associé qui stocke tous les paramètres qui définissent la façon dont cet objet apparaît: c\'est-à-dire la couleur, la largeur de ligne, etc\... Voir aussi l\'extrait ci-dessous [Lister les composantes d\'un objet](#Lister_les_composantes_d.27un_objet.md).


```python
gad = Gui.activeDocument() # access the active document containing all 
                           # view representations of the features in the
                           # corresponding App document 

v = gad.getObject("Cube")  # access the view representation to the Mesh feature 'Cube' 
v.ShapeColor               # prints the color to the console 
v.ShapeColor=(1.0,1.0,1.0) # sets the shape color to white
```


{{Top}}

### Remplacer la forme de la souris par une image {#remplacer_la_forme_de_la_souris_par_une_image}


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

### Remplacer la forme de la souris par une image (croix) {#remplacer_la_forme_de_la_souris_par_une_image_croix}

L\'image est créée par Gimp et exportée dans un fichier .XPM. Copiez et utilisez le code entre le crochet **\"{\"** code to copy **\"}\"**


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

### Observe camera change in the 3D viewer via Python {#observe_camera_change_in_the_3d_viewer_via_python}

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

### Observer des évènements de la souris dans la vue 3D via Python {#observer_des_évènements_de_la_souris_dans_la_vue_3d_via_python}

La structure Inventor permet d\'ajouter un ou plusieurs nœuds de rappel au graphe de scène de la vue. Par défaut dans FreeCAD, un nœud de rappel est installé par vue, ce qui permet d\'ajouter des fonctions C ++ globales ou statiques. Dans la liaison Python appropriée, certaines méthodes sont fournies pour utiliser cette technique à partir du code Python.


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

Maintenant, choisissez une zone dans l\'écran (surface de travail) 3D et observez les messages affichés dans la fenêtre de sortie. Pour terminer l\'observation il suffit de faire:


```python
v.removeEventCallback("SoMouseButtonEvent",c)
```

Les types d'évènements suivants sont pris en charge:

-   SoEvent \-- tous types d\'évènements
-   SoButtonEvent \-- tous les évènements, boutons, molette
-   SoLocation2Event \-- tous les évènements 2D (déplacements normaux de la souris)
-   SoMotion3Event \-- tous les évènements 3D (pour le spaceball)
-   SoKeyboardEvent \-- évènements des touches **flèche haut** et **flèche bas**
-   SoMouseButtonEvent \-- tous les évènements boutons Haut et Bas de la souris
-   SoSpaceballButtonEvent \-- tous les évènements Haut et Bas (pour le spaceball)

Les fonctions Python qui peuvent être enregistrées avec addEventCallback()\'\'\' attendent la définition d\'une bibliothèque.

Suivant la façon dont l'évènement survient, la bibliothèque peut disposer de différentes clefs.

Il y a une clef pour chaque événement:

-   Type \-- le nom du type d\'évènement par exemple SoMouseEvent, SoLocation2Event, \...\'\'\'
-   Time \-- l\'heure courante codée dans une chaîne string
-   Position \-- un tuple de deux **[integers](http://docs.python.org/library/functions.html#int)**, donant la position x,y de la souris
-   ShiftDown \-- type boolean, true si **Shift** est pressé sinon, false
-   CtrlDown \-- type boolean, true si **Ctrl** est pressé sinon, false
-   AltDown \-- type boolean, true si **Alt** est pressé sinon, false

Pour un évènement bouton comme clavier, souris ou spaceball

-   State \-- la chaîne UP si le bouton est relevé, DOWN si le bouton est enfoncé ou UNKNOWN si rien ne se passe

Pour un évènement clavier:

-   Key \-- le caractère de la touche qui est pressée

Pour un évènement bouton de souris:

-   Button \-- le bouton pressé peut être BUTTON1, \..., BUTTON5 ou tous

Pour un évènement spaceball:

-   Button \-- le bouton pressé peut être BUTTON1, \..., BUTTON7 ou tous

Et finalement les évènement de mouvements:

-   Translation \-- un tuple de trois [float()](http://docs.python.org/library/functions.html#float)
-   Rotation \-- un quaternion, tuple de quattre [float()](http://docs.python.org/library/functions.html#float)


{{Top}}

### Afficher les évènements claviers et commandes {#afficher_les_évènements_claviers_et_commandes}

Cette macro affiche dans la vue du rapport les touches enfoncées et tous les événements commande


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

### Manipuler des graphes de scène en Python {#manipuler_des_graphes_de_scène_en_python}

Il est également possible d\'obtenir et de modifier le graphe de scène en Python, avec le module \'pivy\' - une liaison Python pour Coin.


```python
from pivy.coin import *                # load the pivy module
view = Gui.ActiveDocument.ActiveView   # get the active viewer
root = view.getSceneGraph()            # the root is an SoSeparator node
root.addChild(SoCube())
view.fitAll()
```

L\'API Python de pivy est créé en utilisant l\'outil [SWIG](http://www.swig.org/). Comme dans FreeCAD nous utilisons certains noeuds (nodes) écrits automatiquement nous ne pouvons pas les créer directement en Python. Il est cependant, possible de créer un noeud avec son nom interne. Un exemple de type \'SoFCSelection\' peut être créé avec:


```python
type = SoType.fromName("SoFCSelection")
node = type.createInstance()
```


{{Top}}

### Ajouter et effacer des objets au/de graphe de scène {#ajouter_et_effacer_des_objets_aude_graphe_de_scène}

Ajouter de nouveaux noeuds dans le graphe de scène peut être fait de cette façon. Prenez toujours soin d\'ajouter un SoSeparator pour contenir les propriétés de la forme géométrique, les coordonnées et l\'information du matériau d\'un même objet. L\'exemple suivant ajoute une ligne rouge à partir de (0,0,0) à (10,0,0):


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

Pour le supprimer, il suffit de: 
```python
sg.removeChild(no)
``` {{Top}}


<div class="mw-collapsible mw-collapsed toccolours">

### Enregistrer le graphe de scène en 3 séries de 36 fichiers {#enregistrer_le_graphe_de_scène_en_3_séries_de_36_fichiers}

Affichez l\'extrait de code en développant cette section


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

### Ajouter des widgets personnalisés à l\'interface {#ajouter_des_widgets_personnalisés_à_linterface}

Vous pouvez créer des widgets personnalisés avec Qt Designer, les transformer en script Python, puis les charger dans l\'interface FreeCAD avec PySide.

Le code python produit par le compilateur python Ui (l\'outil qui convertit les fichiers .ui de qt-designer en code python) généralement codé comme ceci (il est simple, vous pouvez aussi le coder directement en Python):


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

Puis, vous devez créer une référence à la fenêtre FreeCAD Qt, lui insérer le widget personnalisé, et transférer le code Ui du widget que nous venons de faire dans le vôtre avec:


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

### Ajouter un onglet à la vue combinée {#ajouter_un_onglet_à_la_vue_combinée}

Le code suivant vous permet d\'ajouter un onglet à la [Vue combinée](Combo_view/fr.md), distinct des onglets \"Modèle\" et \"Tâches\" éxistants. Il utilise également le module `uic` pour charger un fichier d\'interface utilisateur directement dans cet onglet.


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

### Activer ou désactiver une fenêtre {#activer_ou_désactiver_une_fenêtre}

Ce script donne la possibilité de manipuler l\'interface utilisateur de la [console Python](Python_console/fr.md) pour afficher/masquer différents composants dans de l\'[interface](interface/fr.md) de FreeCAD tels que:

-   [Vue rapport](Report_view/fr.md)
-   [vue en arborescence](tree_view/fr.md)
-   [Éditeur de propriétés](Property_editor/fr.md)
-   [Fenêtre de sélection](Selection_view/fr.md)
-   [Vue Combinée](Combo_view/fr.md)
-   [console Python](Python_console/fr.md)
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

### Ouvrir une page web personnalisée {#ouvrir_une_page_web_personnalisée}


```python
import WebGui
WebGui.openBrowser("http://www.example.com")
```


{{Top}}

### Obtenir le code HTML d\'une page Web ouverte {#obtenir_le_code_html_dune_page_web_ouverte}


```python
from PySide import QtGui,QtWebKit
a = QtGui.qApp
mw = a.activeWindow()
v = mw.findChild(QtWebKit.QWebFrame)
html = unicode(v.toHtml())
print( html)
```


{{Top}}

### Extraire les coordonnées de 3 points ou 3 objets sélectionnés {#extraire_les_coordonnées_de_3_points_ou_3_objets_sélectionnés}


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

### Lister les objets {#lister_les_objets}


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

### Lister les dimensions en donnant le nom de l\'objet {#lister_les_dimensions_en_donnant_le_nom_de_lobjet}


```python
for edge in FreeCAD.ActiveDocument.MyObjectName.Shape.Edges: # replace "MyObjectName" for list
    print( edge.Length)
```


{{Top}}

### Fonction résidente avec action au clic de souris {#fonction_résidente_avec_action_au_clic_de_souris}

Ici avec **SelObserver** sur un objet selectionné


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

Autre exemple avec **ViewObserver** sur un objet selectionné


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

### Rechercher et sélectionner tous les éléments sous le curseur {#rechercher_et_sélectionner_tous_les_éléments_sous_le_curseur}


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

### Lister les composantes d\'un objet {#lister_les_composantes_dun_objet}

Cette fonction répertorie les composants d\'un objet et extrait:

-   de cet objet, ses coordonnées XYZ,
-   ses bords et leurs longueurs centre de masse et coordonnées
-   ses faces et leur centre de masse
-   ses faces et leurs surfaces et coordonnées


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

### Lister les PropertiesList {#lister_les_propertieslist}


```python
import FreeCADGui
from FreeCAD import Console
o = App.ActiveDocument.ActiveObject
op = o.PropertiesList
for p in op:
    Console.PrintMessage("Property: "+ str(p)+ " Value: " + str(o.getPropertyByName(p))+"\r\n")
```


{{Top}}

### Ajouter un seul commentaire de propriété {#ajouter_un_seul_commentaire_de_propriété}


```python
import Draft
obj = FreeCADGui.Selection.getSelection()[0]
obj.addProperty("App::PropertyString","GComment","Draft","Font name").GComment = "Comment here"
App.activeDocument().recompute()
```


{{Top}}


<div class="mw-collapsible mw-collapsed toccolours">

### Rechercher et extraire des données {#rechercher_et_extraire_des_données}

Exemple de recherche et décodage des informations d\'un objet

Chaque section est séparée par des dièses \"\#\#\#\#\#\#\#\#\#\#\#\#\" vous pouvez les copier directement dans la console, les utiliser dans vos macro ou utiliser la macro complète. La description de la commande est dans le commentaire.

L\'affichage se fait dans la \"vue rapport\" (Menu Affichage → Vues → Vue rapport)


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

### Rechercher manuellement un élément par son label {#rechercher_manuellement_un_élément_par_son_label}


```python
# Extract the coordinate X,Y,Z and Angle giving the label (here "Cylindre")
App.Console.PrintMessage("Base.x       : "+str(FreeCAD.ActiveDocument.getObjectsByLabel("Cylindre")[0].Placement.Base.x)+"\n")
App.Console.PrintMessage("Base.y       : "+str(FreeCAD.ActiveDocument.getObjectsByLabel("Cylindre")[0].Placement.Base.y)+"\n")
App.Console.PrintMessage("Base.z       : "+str(FreeCAD.ActiveDocument.getObjectsByLabel("Cylindre")[0].Placement.Base.z)+"\n")
App.Console.PrintMessage("Base.Angle   : "+str(FreeCAD.ActiveDocument.getObjectsByLabel("Cylindre")[0].Placement.Rotation.Angle)+"\n\n")
##################################################################################

```

**Remarque:** les angles sont généralement affichés en radian. Pour les convertir:

1.  angle en degré vers radian:
    -   Angle en radian = **pi \* (angle en degré) / 180**
    -   Angle en radian = math.radians(angle en degré)
2.  angle en radian vers degré :
    -   Angle en degré = **180 \* (angle en radian) / pi**
    -   Angle en degré = math.degrees(angle en radian)


{{Top}}

### Coordonnées cartésiennes {#coordonnées_cartésiennes}

Ce code affiche les coordonnées cartésiennes de l\'objet sélectionné.

Changer la valeur \"numberOfPoints\" si vous voulez plus ou moins de précision


```python
numberOfPoints = 100                                                         # Decomposition number (or precision you can change)
selectedEdge = FreeCADGui.Selection.getSelectionEx()[0].SubObjects[0].copy() # select one element
points  = selectedEdge.discretize(numberOfPoints)                            # discretize the element
i=0
for p in points:                                                             # list and display the coordinates
    i+=1
    print( i, " X", p.x, " Y", p.y, " Z", p.z)
```

Autre méthode d\'affichage \"Int\" et \"Float\"


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

### Sélectionner tous les objets du document {#sélectionner_tous_les_objets_du_document}


```python
import FreeCAD
for obj in FreeCAD.ActiveDocument.Objects:
    print( obj.Name )                               # display the object Name
    objName = obj.Name
    obj = App.ActiveDocument.getObject(objName)
    Gui.Selection.addSelection(obj)                 # select the object
```


{{Top}}

### Sélectionner une face d\'un objet par le nom de l\'objet et numéro de la face {#sélectionner_une_face_dun_objet_par_le_nom_de_lobjet_et_numéro_de_la_face}


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

### Obtenir le vecteur normal d\'une face d\'un objet par le nom de l\'objet et numéro de la face (r.Q) {#obtenir_le_vecteur_normal_dune_face_dun_objet_par_le_nom_de_lobjet_et_numéro_de_la_face_r.q}


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

### Obtenir le vecteur normal d\'une face d\'un objet par le nom de l\'objet et numéro de la face {#obtenir_le_vecteur_normal_dune_face_dun_objet_par_le_nom_de_lobjet_et_numéro_de_la_face}


```python
numero_Face = 2       # number of the face searched (begin 0, 1, 2, 3 .....)
nomObjet    = "Box"   # object name
normal      = Gui.ActiveDocument.getObject(nomObjet).Object.Shape.Faces[numero_Face].normalAt(0,0)
print("Face"+str(numero_Face), " : ", normal)

```


{{Top}}

### Obtenir le vecteur normal d\'un objet sélectionné et le numéro de la face {#obtenir_le_vecteur_normal_dun_objet_sélectionné_et_le_numéro_de_la_face}


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

### Obtenir le vecteur normal sur une surface {#obtenir_le_vecteur_normal_sur_une_surface}

Cet exemple montre comment trouver le vecteur normal() d\'une face en cherchant les paramètres uv d\'un point sur la surface et utiliser les paramètres u, v pour trouver le vecteur normal()


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

### Obtenir le vecteur normal d\'une surface à partir d\'un fichier STL {#obtenir_le_vecteur_normal_dune_surface_à_partir_dun_fichier_stl}


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

Vous avez terminé et voulez quitter :


```python
Gui.ActiveDocument.ActiveView.removeEventCallbackPivy(coin.SoMouseButtonEvent.getClassTypeId(), meth)
```


{{Top}}

### Créer un objet dans la position de la camera {#créer_un_objet_dans_la_position_de_la_camera}


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

Ici le même code simplifié


```python
import Draft
pl = FreeCAD.Placement()
pl.Rotation = FreeCADGui.ActiveDocument.ActiveView.getCameraOrientation()
pl.Base = FreeCAD.Vector(0.0,0.0,0.0)
rec = Draft.makeRectangle(length=10.0,height=10.0,placement=pl,face=False,support=None)
```


{{Top}}

### Lire et écrire une Expression {#lire_et_écrire_une_expression}


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

### Créer une esquisse sur une surface dans PartDesign {#créer_une_esquisse_sur_une_surface_dans_partdesign}

Cet extrait de code peut être utile si vous souhaitez créer une esquisse sur une surface dans PartDesign à partir d\'une macro. Notez que ce corps peut être Aucun si aucun corps actif n\'est sélectionné et que la sélection peut être vide.


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

### Comment simuler un clic de souris sur une coordonnée donnée {#comment_simuler_un_clic_de_souris_sur_une_coordonnée_donnée}

La position est relative au widget GL. Voir [fil du forum](https://forum.freecadweb.org/viewtopic.php?f=22&t=44008).


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

Si vous avez un point 3d et que vous voulez obtenir le point 2d sur le widget opengl, alors utilisez ceci:


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

### Comment créer une face avec des trous à l\'aide de l\'API Python {#comment_créer_une_face_avec_des_trous_à_laide_de_lapi_python}

Cet extrait montre comment créer une face avec des trous à l\'aide de l\'API Python. Voir [fil du forum](https://forum.freecadweb.org/viewtopic.php?f=22&t=56308).


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

## En relation {#en_relation}

-   [Objets crées par script](Scripted_objects/fr.md)
-   [Macros](Macros/fr.md)


{{Top}}


{{Powerdocnavi

}}

[Category:Developer Documentation{{\#translation:}}](Category:Developer_Documentation.md) [Category:Python Code{{\#translation:}}](Category:Python_Code.md)
