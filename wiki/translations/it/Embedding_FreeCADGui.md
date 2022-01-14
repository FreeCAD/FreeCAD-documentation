# Embedding FreeCADGui/it
## Introduction

È possibile [importare il modulo FreeCAD](Embedding_FreeCAD/it.md) in una applicazione [Python](Python/it.md) e utilizzare tutti i suoi strumenti dall\'applicazione che lo ospita, ma l\'interfaccia utente (GUI) di FreeCAD può anche essere importata come modulo Python. Normalmente è possibile importare solo, in blocco, l\'interfaccia completa, e non le sue singole parti. Questo perché il sistema dell\'interfaccia di FreeCAD non è fatto soltanto di widget e di barre degli strumenti indipendenti, ma è una costruzione complessa in cui sono necessari diversi componenti invisibili (come ad esempio il sistema di selezione, ecc) affinchè la vista 3D principale possa funzionare.

Ma, con un po\' di hacking, è possibile importare prima l\'intera interfaccia di FreeCAD e poi spostare la vista 3D nella propria applicazione Qt. Qui sono descritti 3 metodi diversi.

## Utilizzando direttamente il componente aggiuntivo (Widget) di FreeCAD per la vista 3D 

Tenete presente che con questo approccio ci sono molti problemi. L\'elaborazione di Qt sembra non funzionare (nessuna idea sul perché) e quando si utilizza il menu contestuale della vista 3D l\'applicazione si blocca. Un approccio migliore potrebbe essere quello di creare il proprio SoQtExaminerViewer o SoQtViewer della vista 3D e \"spingere\" il contenuto della vista FreeCAD 3D, come mostrato più avanti, nelle altre sezioni.

In primo luogo, ottenere la finestra principale via [PySide](PySide/it.md): 
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

Poi ottenere la vista View3DInventor nello stesso modo: 
```python
def get3dview(mw):
      childs=mw.findChildren(QtGui.QMainWindow)
      for i in childs:
         if i.metaObject().className() == "Gui::View3DInventor":
            return i
      return None

v = get3dview(mw)
```

Il seguente codice viene generato automaticamente, tramite la [creazione di una interfaccia grafica di QtDesigner](Dialog_creation/it.md), e convertito in codice python con lo strumento pyuic: 
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

Quindi, creare una finestra principale che dovrebbe essere la finestra principale dell\'applicazione, applicarvi sopra la configurazione dell\'interfaccia utente per aggiungere una zona MDI e \"spostare\" in essa la vista 3D. 
```python
ui = Ui_MainWindow()
my_mw = QtGui.QMainWindow()
ui.setupUi(my_mw)
ui.mdiArea.addSubWindow(v)
my_mw.show()
```

Creazione di un esaminatore \"soGui Viewer\"

In alternativa, è possibile utilizzare anche il modulo FreeCADGui per estrarre una rappresentazione OpenInventor (Coin) degli oggetti di scena, quindi utilizzare tali dati coin in un visualizzatore esterno (la propria applicazione). Ecco un modo facile per ottenere la rappresentazione 3D di un oggetto. 
```python
from pivy import coin
import FreeCAD as App

box = App.activeDocument().addObject("Part::Box", "myBox")
s = box.ViewObject.toString()  # store as string
inp = coin.SoInput()
inp.setBuffer(s)
myNode = coin.SoDB.readAll(inp)  # restore from string
```

Quindi, creare un visualizzatore autonomo con [Pivy](Pivy/it.md): 
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

Poi basta eseguire il proprio visualizzatore: 
```python
myViewer()
```

## Utlizzando il modulo Quarter 

Invece di utilizzare il visualizzatore soGui, è possibile utilizzare il più moderno modulo Quarter. Delle tre soluzioni questa è probabilmente la migliore. 
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

## Senza avviare la GUI di FreeCAD 

A partire da FreeCAD rev2760 (2010, [1](https://forum.freecadweb.org/viewtopic.php?f=8&t=203&start=20#p1226)), è possibile avere la rappresentazione coin di qualsiasi oggetto di FreeCAD senza aprire la finestra principale. Questo rende estremamente facile implementare il proprio visualizzatore e avere FreeCAD aggiornato. Dopo aver importato il modulo FreeCADGui, è necessario attivarlo con il metodo `setupWithoutGUI()`, dopo di che è possibile utilizzare tutti i fornitori di viste di FreeCAD per ottenere i nodi OpenInventor (Coin). 
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

Oppure, se utilizzando il modulo sogui di pivy per voi non funziona (il modulo sogui sta diventando obsoleto e gli sviluppatori di coin ora stanno favorendo la nuova libreria Quarter che ha una migliore interazione con qt), questo è lo stesso script, ma utilizzando Quarter: 
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

## Informazioni aggiuntive 

-   [Embedding a view to another (QT) application?](https://forum.freecadweb.org/viewtopic.php?f=8&t=203)
-   [Using Gui functions without Gui.showMainWindow() in python script](https://forum.freecadweb.org/viewtopic.php?t=12575)
-   [Acess Scenegraph through python API in without Gui mode](https://forum.freecadweb.org/viewtopic.php?t=14912)
-   [FreeCAD Hangs When Called from Python](https://forum.freecadweb.org/viewtopic.php?p=190353)
-   [Problem with FreeCADGui](https://forum.freecadweb.org/viewtopic.php?t=41697)

Nel codice sorgente ci sono esempi di incorporamento di FreeCAD con vari toolkit grafici:

-   [src/Tools/embedded](https://github.com/FreeCAD/FreeCAD/tree/master/src/Tools/embedded)


{{Powerdocnavi

}} 

[<img src="images/Property.png" style="width:16px"> Developer Documentation](Category_Developer_Documentation.md) [<img src="images/Property.png" style="width:16px"> Python Code](Category_Python_Code.md)

---
[documentation index](../README.md) > [Developer Documentation](Category_Developer Documentation.md) > Embedding FreeCADGui/it
