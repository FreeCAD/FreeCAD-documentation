# Embedding FreeCADGui/pl
## Wprowadzenie

Możliwy jest [import modułu FreeCAD](Embedding_FreeCAD/pl.md) do środowiska [Python](Python/pl.md) i korzystanie ze wszystkich jego narzędzi z aplikacji hosta, ale graficzny interfejs użytkownika *(GUI)* może być również importowany jako moduł Python. Zwykle można importować tylko kompletny interfejs jako całość, a nie jego fragmenty. Dzieje się tak dlatego, że system interfejsu FreeCAD składa się nie tylko z niezależnych widżetów i pasków narzędzi, ale jest złożoną konstrukcją, w której kilka niewidocznych komponentów *(takich jak system wyboru itp.)* jest potrzebnych do funkcjonowania głównego [3D view](3D_view/pl.md).

Jednak przy odrobinie hakowania możliwe jest zaimportowanie całego interfejsu FreeCAD, a następnie przeniesienie z niego widoku 3D do własnej aplikacji Qt. Pokażemy tutaj 3 różne metody.



## Bezpośrednie użycie widżetu widoku FreeCAD 3D 

Należy pamiętać, że istnieje wiele problemów z tym podejściem. Obsługa zdarzeń Qt wydaje się nie działać *(nie mam pojęcia dlaczego)*, a jeśli użyjesz menu kontekstowego widoku 3D, aplikacja się zawiesi. Lepszym sposobem może być stworzenie własnego widoku 3D SoQtExaminerViewer lub SoQtViewer i \"wypchnięcie\" zawartości widoku 3D FreeCAD do swojego widoku, jak pokazano w innych sekcjach poniżej.

Najpierw pobierz główne okno przez [PySide](PySide/pl.md): 
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

Następnie uzyskaj widok View3DInventor w ten sam sposób: 
```python
def get3dview(mw):
      childs=mw.findChildren(QtGui.QMainWindow)
      for i in childs:
         if i.metaObject().className() == "Gui::View3DInventor":
            return i
      return None

v = get3dview(mw)
```

Poniższy kod jest generowany automatycznie przez [tworzenie pliku Ui za pomocą QtDesigner](Dialog_creation/pl.md) i konwertowanie go na kod Python za pomocą narzędzia pyuic: 
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

Następnie utwórz główne okno, które powinno być głównym oknem aplikacji, zastosuj do niego powyższą konfigurację interfejsu użytkownika, aby dodać obszar MDI i \"przenieś\" do niego nasz [widok 3D](3D_view/pl.md). 
```python
ui = Ui_MainWindow()
my_mw = QtGui.QMainWindow()
ui.setupUi(my_mw)
ui.mdiArea.addSubWindow(v)
my_mw.show()
```



## Tworzenie przeglądarki egzaminatora soGui 

Alternatywnie można również użyć modułu FreeCADGui do wyodrębnienia reprezentacji OpenInventor *(Coin)* obiektów sceny, a następnie użyć tych danych w zewnętrznej przeglądarce *(aplikacji)*. Oto prosty sposób na uzyskanie reprezentacji 3D obiektu. 
```python
from pivy import coin
import FreeCAD as App

box = App.activeDocument().addObject("Part::Box", "myBox")
s = box.ViewObject.toString()  # store as string
inp = coin.SoInput()
inp.setBuffer(s)
myNode = coin.SoDB.readAll(inp)  # restore from string
```

Następnie utwórz samodzielną przeglądarkę za pomocą [Pivy](Pivy/pl.md): 
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

Następnie wystarczy uruchomić przeglądarkę: 
```python
myViewer()
```



## Korzystanie z modułu quarter 

Zamiast korzystać z przeglądarki sogui, można również użyć bardziej nowoczesnego modułu quarter. Jest to ogólnie najlepsza z trzech opcji. 
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



## Nawet bez uruchamiania GUI FreeCAD 

Począwszy od FreeCAD rev2760 *(2010, [1](https://forum.freecadweb.org/viewtopic.php?f=8&t=203&start=20#p1226))*, możliwe jest teraz uzyskanie reprezentacji coin dowolnego obiektu FreeCAD bez otwierania głównego okna. Dzięki temu niezwykle łatwo jest zaimplementować własną przeglądarkę i w przejrzysty sposób aktualizować ją przez FreeCAD. Po zaimportowaniu modułu `FreeCADGui`, należy go uruchomić za pomocą metody `setupWithoutGUI()`, po czym można użyć wszystkich dostawców widoków FreeCAD do uzyskania węzłów OpenInventor *(Coin)*. 
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

Lub, jeśli użycie modułu sogui pivy nie działa *(moduł sogui staje się przestarzały, a programiści coin preferują teraz nową bibliotekę quarter, która ma znacznie lepszą interakcję z qt)*, tutaj jest ten sam skrypt, ale z użyciem quarter: 
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



## Informacje dodatkowe 

-   [Osadzanie widoku w innej aplikacji (QT)?](https://forum.freecadweb.org/viewtopic.php?f=8&t=203)
-   [Używanie funkcji Gui bez Gui.showMainWindow() w skrypcie Pythona](https://forum.freecadweb.org/viewtopic.php?t=12575)
-   [Dostęp do Scenegraph przez API Pythona bez trybu Gui](https://forum.freecadweb.org/viewtopic.php?t=14912)
-   [FreeCAD zawiesza się po wywołaniu z Pythona](https://forum.freecadweb.org/viewtopic.php?p=190353)
-   [Problem z FreeCADGui](https://forum.freecadweb.org/viewtopic.php?t=41697)

W kodzie źródłowym znajdują się przykłady osadzania FreeCAD z różnymi zestawami narzędzi graficznych:

-   [src/Tools/embedded](https://github.com/FreeCAD/FreeCAD/tree/master/src/Tools/embedded)



---
⏵ [documentation index](../README.md) > [Developer Documentation](Category_Developer%20Documentation.md) > [Python Code](Category_Python%20Code.md) > Embedding FreeCADGui/pl
