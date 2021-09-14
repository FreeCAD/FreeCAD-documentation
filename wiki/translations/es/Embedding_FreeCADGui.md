# Embedding FreeCADGui/es



## Introduction


<div class="mw-translate-fuzzy">

Ya sabes que puedes [importar el módulo de FreeCAD](Embedding_FreeCAD.md) en una aplicación en Python, y utilizar todas sus herramientas desde la aplicación anfritriona. Pero el entorno gráfico de usuario GUI de FreeCAD también puede importarse como un módulo de Python. Normalmente solo puedes importar el interfaz completo como un todo, no unas partes de él. Esto es porque el sistema de interfaz de FreeCAD no sólo está hecho de complementos (widgets) y barras de herramientas independientes, pero es una construcción compleja donde varios componentes individuales (como el sistema de selección, etc.) son necesarios para que la vista 3D principal pueda funcionar.


</div>

Pero, trasteando un poco, es posible importar el interfaz completo de FreeCAD, luego mover la vista 3D desde allí a tu propia aplicación Qt. Mostraremos aquí 3 métodos diferentes.

## Utilizando el complemento (widget) de la vista 3D de FreeCAD directamente 

Debes ser consciente de que existen muchos problemas con este enfoque. El tratamiento de eventos de Qt parece que no funciona (ni idea del por qué) y si utilizas el menú contextual de la vista 3D la aplicación se cuelga. Un método mejor podría ser crear tu propio SoQtExaminerViewer de la vista 3D o SoQtViewer y \"empujar\" el contenido de la vista 3D de FreeCAD, como se muestra en las otras secciones más abajo.


<div class="mw-translate-fuzzy">

Primero, consigue la ventana principal vía PyQt:


</div>


```python
from PySide import QtGui
from PySide import QtCore

def getMainWindow():
   toplevel = QtGui.qApp.topLevelWidgets()
   for i in toplevel:
      if i.metaObject().className() == "Gui::MainWindow":
         return i
   raise Exception("No main window found")

mw = getMainWindow()
```

Luego consigue la vista View3DInventor del mismo modo: 
```python
def get3dview(mw):
      childs=mw.findChildren(QtGui.QMainWindow)
      for i in childs:
         if i.metaObject().className() == "Gui::View3DInventor":
            return i
      return None

v = get3dview(mw)
```

El siguiente código es generado automáticamente, por la [creación de un interfaz de usuario con QtDesigner](Dialog_creation/es.md), y convirtiéndola a código en Python con la herramienta pyuic: 
```python
# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'mainwindow.ui'
#
# Created: Sun Dec 27 11:18:56 2009
#      by: PySide UI code generator 4.6
#
# Modify for PySide 11/02/2015
#      Python version: 2.7.8
#      Qt version: 4.8.6
#
# WARNING! All changes made in this file will be lost!

from PySide import QtCore, QtGui

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(508, 436)
        self.centralwidget = QtGui.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.gridLayout = QtGui.QGridLayout(self.centralwidget)
        self.gridLayout.setObjectName("gridLayout")
        self.mdiArea = QtGui.QMdiArea(self.centralwidget)
        self.mdiArea.setViewMode(QtGui.QMdiArea.TabbedView)
        self.mdiArea.setTabPosition(QtGui.QTabWidget.South)
        self.mdiArea.setObjectName("mdiArea")
        self.gridLayout.addWidget(self.mdiArea, 0, 0, 1, 1)
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtGui.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 508, 27))
        self.menubar.setObjectName("menubar")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtGui.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QtGui.QApplication.translate("MainWindow", "MainWindow", None, QtGui.QApplication.UnicodeUTF8))
```


<div class="mw-translate-fuzzy">

Luego, crea una ventana principal que debería ser la ventana principal de tu aplicación, aplica el setup de la interfaz de usuario UI de arriba para añadir un área MDI y \"mueve\" mueve nuestra vista 3D a ella


</div>


```python
ui = Ui_MainWindow()
my_mw = QtGui.QMainWindow()
ui.setupUi(my_mw)
ui.mdiArea.addSubWindow(v)
my_mw.show()
```

## Creación de un Visor examinador soGui 


<div class="mw-translate-fuzzy">

Alternativamente, también puedes utilizar el módulo FreeCADGui para extraer una representación de coin/openInventor de los objetos de tu escena, luego utilizar esos datos de coin en un visor externo (tu aplicación). Aquí tienes un sencillo modo para obtener la representación de un objeto:


</div>


```python
from pivy import coin
import FreeCAD as App

box = App.activeDocument().addObject("Part::Box", "myBox")
s = box.ViewObject.toString()  # store as string
inp = coin.SoInput()
inp.setBuffer(s)
myNode = coin.SoDB.readAll(inp)  # restore from string
```


<div class="mw-translate-fuzzy">

Luego, crea un visor te a autónomo con pivy:


</div>


```python
from pivy.sogui import *
from pivy.coin import *
import sys

def myViewer():
    # Initialize Coin. This returns a main window to use.
    # If unsuccessful, exit.
    myWindow = SoGui.init(sys.argv[0])
    if myWindow == None:
        sys.exit(1)

    # Make an empty scene and add our node to it
    scene = SoSeparator()
    scene.addChild(myNode)

    # Create a viewer in which to see our scene graph.
    viewer = SoGuiExaminerViewer(myWindow)

    # Put our scene into viewer, change the title
    viewer.setSceneGraph(scene)
    viewer.setTitle("FreeCAD Object Viewer")
    viewer.show()

    SoGui.show(myWindow) # Display main window
    SoGui.mainLoop()     # Main Coin event loop
```

entonces simplemente necesitas ejecutar tu visor: 
```python
myViewer()
```

## Utilizando el módulo quarter 


<div class="mw-translate-fuzzy">

En lugar de utilizar el visor sogui, también puedes utilizar el más reciente módulo quarter. Esta es posiblemente la mejor solución de las tres.


</div>


```python
#!/usr/bin/env python
 
###
# Copyright (c) 2002-2008 Kongsberg SIM
#
# Permission to use, copy, modify, and distribute this software for any
# purpose with or without fee is hereby granted, provided that the above
# copyright notice and this permission notice appear in all copies.
#
# THE SOFTWARE IS PROVIDED "AS IS" AND THE AUTHOR DISCLAIMS ALL WARRANTIES
# WITH REGARD TO THIS SOFTWARE INCLUDING ALL IMPLIED WARRANTIES OF
# MERCHANTABILITY AND FITNESS. IN NO EVENT SHALL THE AUTHOR BE LIABLE FOR
# ANY SPECIAL, DIRECT, INDIRECT, OR CONSEQUENTIAL DAMAGES OR ANY DAMAGES
# WHATSOEVER RESULTING FROM LOSS OF USE, DATA OR PROFITS, WHETHER IN AN
# ACTION OF CONTRACT, NEGLIGENCE OR OTHER TORTIOUS ACTION, ARISING OUT OF
# OR IN CONNECTION WITH THE USE OR PERFORMANCE OF THIS SOFTWARE.
#
 
import os
import sys
 
from PySide import QtCore, QtGui
from PySide.QtGui import QMainWindow, QWorkspace, QAction, QFileDialog, QApplication
 
from pivy.coin import SoInput, SoDB
from pivy.quarter import QuarterWidget
 
import FreeCAD, FreeCADGui
 
def getMainWindow():
   toplevel = QtGui.qApp.topLevelWidgets()
   for i in toplevel:
      if i.metaObject().className() == "Gui::MainWindow":
         return i
   raise Exception("No main window found")
 
class MdiQuarterWidget(QuarterWidget):
    def __init__(self, parent, sharewidget):
        QuarterWidget.__init__(self, parent=parent, sharewidget=sharewidget)
 
    def loadFile(self, filename):
        in_ = SoInput()
        if (in_.openFile(str(filename.toLatin1()))):
            root = SoDB.readAll(in_)
        if (root):
            self.setSceneGraph(root)
            self.currentfile = filename
            self.setWindowTitle(filename)
            return True
        return False
 
    def currentFile(self):
        return self.currentfile
 
    def minimumSizeHint(self):
        return QtCore.QSize(640, 480)
 
class MdiMainWindow(QMainWindow):
    def __init__(self, qApp):
        QMainWindow.__init__(self)
        self._firstwidget = None
        self._workspace = QWorkspace()
        self.setCentralWidget(self._workspace)
        self.setAcceptDrops(True)
        self.setWindowTitle("Pivy Quarter MDI example")
 
        filemenu = self.menuBar().addMenu("&File")
        windowmenu = self.menuBar().addMenu("&Windows")
 
        fileopenaction = QAction("&Create Box", self)
        fileexitaction = QAction("E&xit", self)
        tileaction = QAction("Tile", self)
        cascadeaction = QAction("Cascade", self)
 
        filemenu.addAction(fileopenaction)
        filemenu.addAction(fileexitaction)
        windowmenu.addAction(tileaction)
        windowmenu.addAction(cascadeaction)
 
        self.connect(fileopenaction, QtCore.SIGNAL("triggered()"), self.createBoxInFreeCAD)
        self.connect(fileexitaction, QtCore.SIGNAL("triggered()"), QtGui.qApp.closeAllWindows)
        self.connect(tileaction, QtCore.SIGNAL("triggered()"), self._workspace.tile)
        self.connect(cascadeaction, QtCore.SIGNAL("triggered()"), self._workspace.cascade)
 
        windowmapper = QtCore.QSignalMapper(self)
        self.connect(windowmapper, QtCore.SIGNAL("mapped(QWidget *)"), self._workspace.setActiveWindow)
 
        self.dirname = os.curdir       
 
    def dragEnterEvent(self, event):
        # just accept anything...
        event.acceptProposedAction()
 
    def dropEvent(self, event):
        mimedata = event.mimeData()
        if mimedata.hasUrls():
            path = mimedata.urls().takeFirst().path()
            self.open_path(path)
 
    def closeEvent(self, event):
        self._workspace.closeAllWindows()
 
    def open(self):
        self.open_path(QFileDialog.getOpenFileName(self, "", self.dirname))
 
    def open_path(self, filename):
        self.dirname = os.path.dirname(str(filename.toLatin1()))
        if not filename.isEmpty():
            existing = self.findMdiChild(filename)
            if existing:
                self._workspace.setActiveWindow(existing)
                return
        child = self.createMdiChild()
        if (child.loadFile(filename)):
            self.statusBar().showMessage("File loaded", 2000)
            child.show()
        else:
            child.close()
 
    def findMdiChild(self, filename):
        canonicalpath = QtCore.QFileInfo(filename).canonicalFilePath()
        for window in self._workspace.windowList():
            mdiwidget = window
            if mdiwidget.currentFile() == canonicalpath:
                return mdiwidget
        return 0;
 
    def createMdiChild(self):
        widget = MdiQuarterWidget(None, self._firstwidget)
        self._workspace.addWindow(widget)
        if not self._firstwidget:
            self._firstwidget = widget
        return widget
 
    def createBoxInFreeCAD(self):
        widget = MdiQuarterWidget(None, self._firstwidget)
        self._workspace.addWindow(widget)
        if not self._firstwidget:
            self._firstwidget = widget
        widget.show()
        doc = FreeCAD.newDocument()
        doc.addObject("Part::Box","myBox")
        iv_=FreeCADGui.getDocument(doc.Name).getObject("myBox").toString()
        in_ = SoInput()
        in_.setBuffer(iv_)
        root = SoDB.readAll(in_)
        if (root):
            widget.setSceneGraph(root)
 
def main():
    app = QApplication(sys.argv) 
    mdi = MdiMainWindow(app)   
    mdi.show()
    FreeCADGui.showMainWindow() # setup the GUI stuff of FreeCAD
    mw=getMainWindow()
    mw.hide() # hide all
    if len(sys.argv)==2:
        mdi.open_path(QtCore.QString(sys.argv[1]))
    sys.exit(app.exec_())
 
def show():
    mdi = MdiMainWindow(QtGui.qApp)   
    mdi.show()
    mw=getMainWindow()
    #mw.hide() # hide all
 
if __name__ == '__main__':
    main()
```

## Incluso sin encender el entorno gráfico de usuario de FreeCAD 


<div class="mw-translate-fuzzy">

Desde la revisión rev2760 de FreeCAD, es posible obtener la representación en coin de cualquier objeto de FreeCAD sin abrir la ventana principal. Esto hace extremadamente sencillo implementar tu propio visor y transparentemente tener a FreeCAD actualizándolo. Después de la importación del módulo FreeCADGui, necesitas encenderlo con el método setupWithoutGUI(), después del cual puedes utilizar todos los proveedores de vistas de FreeCAD para obtener nodos coin/openInventor.


</div>


```python
import os, sys, FreeCAD, FreeCADGui
from PyQt4 import QtCore, QtGui
from PyQt4.QtGui import QMainWindow, QWorkspace, QAction, QFileDialog, QApplication
from pivy.coin import SoInput, SoDB, sogui
 
class MdiMainWindow(QMainWindow):
    def __init__(self, qApp):
        QMainWindow.__init__(self)
        self._firstwidget = None
        self._workspace = QWorkspace()
        self.setCentralWidget(self._workspace)
        self.setAcceptDrops(True)
        self.setWindowTitle("Pivy Quarter MDI example")
        self.viewers=[]
 
        filemenu = self.menuBar().addMenu("&File")
        windowmenu = self.menuBar().addMenu("&Windows")
 
        fileopenaction = QAction("&Create Box", self)
        fileexitaction = QAction("E&xit", self)
        tileaction = QAction("Tile", self)
        cascadeaction = QAction("Cascade", self)
 
        filemenu.addAction(fileopenaction)
        filemenu.addAction(fileexitaction)
        windowmenu.addAction(tileaction)
        windowmenu.addAction(cascadeaction)
 
        self.connect(fileopenaction, QtCore.SIGNAL("triggered()"), self.createBoxInFreeCAD)
        self.connect(fileexitaction, QtCore.SIGNAL("triggered()"), QtGui.qApp.closeAllWindows)
        self.connect(tileaction, QtCore.SIGNAL("triggered()"), self._workspace.tile)
        self.connect(cascadeaction, QtCore.SIGNAL("triggered()"), self._workspace.cascade)
 
        windowmapper = QtCore.QSignalMapper(self)
        self.connect(windowmapper, QtCore.SIGNAL("mapped(QWidget *)"), self._workspace.setActiveWindow)
 
    def closeEvent(self, event):
        self._workspace.closeAllWindows()
 
    def createBoxInFreeCAD(self):
        widget = QtGui.QWidget(self._firstwidget)
        viewer = sogui.SoGuiExaminerViewer(widget)
        self._workspace.addWindow(widget)
        if not self._firstwidget:
            self._firstwidget = widget
        widget.show()
        self.viewers.append(viewer)
        doc = FreeCAD.newDocument()
        obj=doc.addObject("Part::Box","myBox")
        doc.recompute()
        root=FreeCADGui.subgraphFromObject(obj)
        viewer.setSceneGraph(root)
 
def main():
    app = QApplication(sys.argv)
    mdi = MdiMainWindow(app)   
    mdi.show()
    FreeCADGui.setupWithoutGUI()
    sys.exit(app.exec_())
 
if __name__ == '__main__':
    main()
```

O, si no te funciona utilizando el modulo sogui de pivy (el módulo sogui se está haciendo obsoleto y los desarrolladores de coin están ahora a favor de la nueva biblioteca quarter, la cual tiene una integración mucho mejor con Qt), este es el mismo archivo de guión pero utilizando quarter: 
```python
#!/usr/bin/env python
 
import os
import sys
 
from PyQt4 import QtCore, QtGui
from PyQt4.QtGui import QMainWindow, QWorkspace, QAction, QApplication
 
from pivy.coin import SoInput, SoDB
from pivy.quarter import QuarterWidget
import FreeCADGui
 
 
class MdiQuarterWidget(QuarterWidget):
    def __init__(self, parent, sharewidget):
        QuarterWidget.__init__(self, parent=parent, sharewidget=sharewidget)
 
    def minimumSizeHint(self):
        return QtCore.QSize(640, 480)
 
 
class MdiMainWindow(QMainWindow):
    def __init__(self, qApp):
        QMainWindow.__init__(self)
        self._firstwidget = None
        self._workspace = QWorkspace()
        self.setCentralWidget(self._workspace)
        self.setAcceptDrops(True)
        self.setWindowTitle("Pivy Quarter MDI example")
 
        filemenu = self.menuBar().addMenu("&File")
        windowmenu = self.menuBar().addMenu("&Windows")
 
        fileopenaction = QAction("&Create Box", self)
        fileexitaction = QAction("E&xit", self)
        tileaction = QAction("Tile", self)
        cascadeaction = QAction("Cascade", self)
 
        filemenu.addAction(fileopenaction)
        filemenu.addAction(fileexitaction)
        windowmenu.addAction(tileaction)
        windowmenu.addAction(cascadeaction)
 
        self.connect(fileopenaction, QtCore.SIGNAL("triggered()"), self.createBoxInFreeCAD)
        self.connect(fileexitaction, QtCore.SIGNAL("triggered()"), QtGui.qApp.closeAllWindows)
        self.connect(tileaction, QtCore.SIGNAL("triggered()"), self._workspace.tile)
        self.connect(cascadeaction, QtCore.SIGNAL("triggered()"), self._workspace.cascade)
 
        windowmapper = QtCore.QSignalMapper(self)
        self.connect(windowmapper, QtCore.SIGNAL("mapped(QWidget *)"), self._workspace.setActiveWindow)
 
        self.dirname = os.curdir       
 
    def closeEvent(self, event):
        self._workspace.closeAllWindows()
 
    def createBoxInFreeCAD(self):
        d=FreeCAD.newDocument()
        o=d.addObject("Part::Box")
        d.recompute()
        s=FreeCADGui.subgraphFromObject(o)
        child = self.createMdiChild()
        child.show()
        child.setSceneGraph(s)
 
    def createMdiChild(self):
        widget = MdiQuarterWidget(None, self._firstwidget)
        self._workspace.addWindow(widget)
        if not self._firstwidget:
            self._firstwidget = widget
        return widget
 
 
def main():
    app = QApplication(sys.argv)
    FreeCADGui.setupWithoutGUI()        
    mdi = MdiMainWindow(app)   
    mdi.show()
    sys.exit(app.exec_())
 
 
if __name__ == '__main__':
    main()
```

## Additional information 

-   [Embedding a view to another (QT) application?](https://forum.freecadweb.org/viewtopic.php?f=8&t=203)
-   [Using Gui functions without Gui.showMainWindow() in python script](https://forum.freecadweb.org/viewtopic.php?t=12575)
-   [Acess Scenegraph through python API in without Gui mode](https://forum.freecadweb.org/viewtopic.php?t=14912)
-   [FreeCAD Hangs When Called from Python](https://forum.freecadweb.org/viewtopic.php?p=190353)
-   [Problem with FreeCADGui](https://forum.freecadweb.org/viewtopic.php?t=41697)

In the source code there are examples of embedding FreeCAD with various graphical toolkits:

-   [src/Tools/embedded](https://github.com/FreeCAD/FreeCAD/tree/master/src/Tools/embedded)


{{Powerdocnavi

}} 

[Category:Developer Documentation](Category:Developer_Documentation.md) [Category:Python Code](Category:Python_Code.md)
