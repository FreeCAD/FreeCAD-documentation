# Macro Dump Objects/fr

 {{Macro/fr
|Name=Macro Dump Objects
|Description=Cette macro génère une liste de tous les objets du document courant, la liste peut être affichée dans une fenêtre ou dans la vue Rapport..
|Author=Piffpoof
|Version=1.0
|Date=2015-03-02
|FCVersion= <= 0.17
|Download=[https://www.freecadweb.org/wiki/images/2/2e/Macro_Dump_Objects.png ToolBar Icon]
}}

Lors du développement de modèles d\'objets complexes, il est facile de perdre la trace des objets présents car certains peuvent être cachés, masqués ou transparents. De plus, avec un grand nombre d\'objets, un système de nommage devient nécessaire pour suivre les objets.

<img alt="" src=images/DumpObjectsScreenSnapshot.jpg  style="width:500px;">

## Description

Le code d\'objet de vidage prend le document en cours et énumère tous les objets. Un rapport est ensuite généré, répertoriant chaque objet, puis un résumé indiquant le nombre total d\'instances de chaque classe, suivi du nombre total de classes et enfin du nombre total d\'objets. La sortie peut être dirigée vers la vue Rapport ou vers une fenêtre. La fenêtre est non modale et restera ouverte jusqu\'à sa fermeture par l\'utilisateur. Chaque fenêtre a l\'heure de vidage de l\'objet dans la barre de titre, ce qui permet de comparer le contenu de plusieurs fenêtres, par exemple avant et après un morceau de code en cours d\'exécution.

L\'opération par défaut répertorie tous les objets, éventuellement le placement de chaque objet peut être répertorié. Pour les esquisses, chaque segment de la géométrie peut également être répertorié.

## Installation

Tout le code pour dumpObject.FCMacro est dans une macro. L\'installation consiste donc à copier le code dans le répertoire Macro approprié et à appeler dumpObject à partir du menu Macro. Sinon, il peut être exécuté depuis la console.

-   voir [Comment installer des macros](How_to_install_macros/fr.md) pour plus d\'informations sur l\'installation de ce code de macro
-   voir [Personnaliser les barres d\'outils](Customize_Toolbars/fr.md) pour plus d\'informations sur l\'installation d\'un bouton sur une barre d\'outils

## Utilisation

Sélectionnez le document pour lequel vous souhaitez vider des objets, puis lancez la macro à partir de l\'un des éléments suivants:

-   le menu Macro
-   depuis la console Python
-   à partir d\'une barre d\'outils

Selon les paramètres sélectionnés dans la première fenêtre, le rapport sera affiché dans la vue Rapport ou dans une fenêtre. Les informations afficheront tous les objets du document en cours. Certains des avantages à attendre sont la détection de:

-   irrégularités dans les noms d\'objet (par exemple, les fautes d\'orthographe ou les noms par défaut générés par FreeCAD)
-   dupliquer des objets
-   objets avec des noms en double (où FreeCAD a dû rendre le nom du deuxième objet unique)
-   objets inattendus
-   Emplacements d\'objet inattendus (lorsque l\'option Afficher les positions est sélectionnée)
-   segments inattendus dans la géométrie d\'esquisse (lorsque l\'option Afficher les segments d\'esquisse est sélectionnée)

## Interface utilisateur 

La première fenêtre entrera en entrée pour configurer l\'objet Object Dump:

![](images/DumpObjectsGui1.jpg )

La seconde fenêtre sera le rapport sur les objets du document en cours:

![](images/DumpObjectsGui2.jpg )

## Options

-   La sortie peut être dirigée vers l\'un des:
    -   la vue Rapport
    -   une fenêtre non modale
-   les segments de la géométrie de chaque dessin peuvent être listés
-   Les spécificités de placement peuvent être répertoriées pour les objets

## Remarques

Bien que testé avec de nombreux types d\'objet dans FreeCAD, certains objets ne sont probablement pas attendus. Dans ce cas, il convient de les répertorier de manière générique.

## Liens

aucun (jusqu\'à présent)

## Script

ToolBar Icon ![](images/Macro_Dump_Objects.png )

**Macro\_Dump\_Objects.FCMacro**


{{MacroCode|code=
#
#                       Dump Object
#                       v 0.2 - added report to CSV file
#                       v 0.1 - added report to window
#                       v 0.0 - report to Report view
#
#***********************************************************************************
# routine to dump object space for Geometric model in the currently active file
#
# import statements
from PySide import QtGui, QtCore
from datetime import datetime       # datestamp on output window
from os.path import expanduser      # output directory for CSV

# UI Class definitions

class configureMacro(QtGui.QDialog):
    """"""
    def __init__(self):
        super(configureMacro, self).__init__()
        self.initUI()
    def initUI(self):
        self.result         = None
        # set up display only field for selected path type
        self.cbss           = QtGui.QCheckBox("Show Sketcher Segments?", self)
        self.cbss.move(20,20)
        self.cbp            = QtGui.QCheckBox("Show Positions?", self)
        self.cbp.move(220,20)
        self.pathTypeLbl    = QtGui.QLabel("Select Report Destination:", self)
        self.pathTypeLbl.move(20, 70)
        # cancel button
        cancelButton = QtGui.QPushButton('Cancel', self)
        cancelButton.clicked.connect(self.onCancel)
        cancelButton.move(10, 100)
        # button #1
        button1 = QtGui.QPushButton(choice1, self)
        button1.clicked.connect(self.onBtn1)
        button1.move(120, 100)
        # button #2
        button2 = QtGui.QPushButton(choice2, self)
        button2.clicked.connect(self.onBtn2)
        button2.move(235, 100)
        # button #3
        button3 = QtGui.QPushButton(choice3, self)
        button3.clicked.connect(self.onBtn3)
        button3.move(327, 100)
        # define window     xLoc,yLoc,xDim,yDim
        self.setGeometry(   250, 250, 435, 150)
        self.setWindowTitle("Select a Report Destination")
        self.setWindowFlags(QtCore.Qt.WindowStaysOnTopHint)
        self.show()
    def onCancel(self):
        self.result = "cancelled"
        self.close()
    def onBtn1(self):
        self.result = choice1
        self.close()
    def onBtn2(self):
        self.result = choice2
        self.close()
    def onBtn3(self):
        self.result = choice3
        self.close()

class DisplayText(QtGui.QWidget):
    """"""
    def __init__(self, textToDisplay):
        self.text = textToDisplay
        super(DisplayText, self).__init__()
        self.initUI(textToDisplay)
    def initUI(self, textToDisplay):
        """Constructor"""
        self.textToDisplay = textToDisplay
        # some window dimensions
        self.windowHome = screenWidth * 0.05
        self.windowWidth = screenWidth * 0.9
        self.windowHeight = 400
        self.fieldMargin = 40
        # some column titles
        columnLabels = QtGui.QLabel(formatPrintLine("Type / WB","Shape","User Supplied Label","Name"))
        columnLabels.setFont('Courier')
        # set up text editing widget
        text_editor = QtGui.QTextEdit(self)
        #self.setCentralWidget(self.text_editor)
        text_editor.setFont('Courier')
        text_editor.setLineWrapMode(QtGui.QTextEdit.NoWrap)
        text_editor.move(self.fieldMargin,self.fieldMargin)
        text_editor.move(0,self.fieldMargin)
        text_editor.resize(self.windowWidth-(2*self.fieldMargin),self.windowHeight-(2*self.fieldMargin))
        text_editor.resize(self.windowWidth,self.windowHeight-(2*self.fieldMargin))
        text_editor.append(self.textToDisplay)
        # set up the layout
        vBox = QtGui.QVBoxLayout()
        vBox.addWidget(columnLabels)
        vBox.addWidget(text_editor)
        self.setLayout(vBox)
        # define window     xLoc,yLoc,xDim,yDim
        self.setGeometry(   self.windowHome, self.windowHome, self.windowWidth, self.windowHeight)
        self.setWindowTitle("Object Dump of '" + FreeCADGui.ActiveDocument.Document.Label + "' at " + str(datetime.now()))
        self.show()
    #----------------------------------------------------------------------
    def onOk(self):
        self.close()

# Class definitions

# Function Definitions

def countObjects():
    printList = list()
    objectTypeTable = {}
    # build up dictionary of different classes and keep a count
    for obj in FreeCAD.ActiveDocument.Objects:
        if objectTypeTable.has_key(obj.TypeId):
            objectTypeTable[obj.TypeId] = objectTypeTable[obj.TypeId]+1
        else:
            objectTypeTable[obj.TypeId] = 1
        wb = obj.TypeId[0:obj.TypeId.find("::")]
        shape = obj.TypeId[obj.TypeId.find("::")+2:]
        #print wb + "---" + shape
        placementString = ""
        if obj.TypeId == "Sketcher::SketchObject":
            printList.append(formatPrintLine("Sketch", "", str(obj.Label)))
            if showSketcherSegmentsFlag:
                for i in obj.Geometry:
                    printList.append(formatPrintLine("", " -segment", str(i)))
        elif wb == "Part":
            if showPlacementFlag:
                placementString = str(obj.Placement)
            if shape in ("Cylinder", "Cut", "Box", "Fuse", "Loft", "Feature", "FeaturePython", "Part2DObjectPython"):
                printList.append(formatPrintLine(wb, shape, str(obj.Label), str(obj.Name)))
            else: # print shapes not in list above
                printList.append(formatPrintLine(str(obj.TypeId), "", str(obj.Label), str(obj.Name)))
        elif wb == "PartDesign":
            if showPlacementFlag:
                placementString = str(obj.Placement)
            if shape in ("Pad", "Feature", "Fillet", "Part2DObjectPython"):
                printList.append(formatPrintLine(wb, shape, str(obj.Label), str(obj.Name)))
            else: # print shapes not in list above
                printList.append(formatPrintLine(str(obj.TypeId), "", str(obj.Label), str(obj.Name)))
        elif obj.TypeId == "App::DocumentObjectGroup":
            printList.append(formatPrintLine("Group", "", str(obj.Label)))
        elif obj.TypeId == "Image::ImagePlane":
            printList.append(formatPrintLine(wb, shape, str(obj.Label), str(obj.Name)))     
        else: # print workbench shapes not in lists above
            printList.append(formatPrintLine(str(obj.TypeId), str(obj.Label), str(obj.Name)))
        if showPlacementFlag and len(placementString)!=0:
            printList.append(formatPrintLineMax("", " -placement", placementString))

    printList.append("")
    printList.append(summarySeparator)
    from collections import OrderedDict
    sortedByTags = OrderedDict(sorted(objectTypeTable.items(), key=lambda x: x[1], reverse=True))
    for k, v in sortedByTags.items():
        printList.append(formatPrintLineSum(k,v))
    printList.append("")
    objectClassCount = 0; objectTotalCount = 0
    for i in objectTypeTable:
        objectTotalCount = objectTotalCount + objectTypeTable[i]
    objectCLassCount = len(objectTypeTable)
    printList.append(formatPrintLineSum("Object Class Total is ", str(objectCLassCount)))
    printList.append(formatPrintLineSum("Object Total is ", str(objectTotalCount)))
    printList.append(summarySeparator)
    return printList

def formatPrintLineSum(a,b):
    return printLineFormatter(2, a, str(b), "", "")

def formatPrintLineMax(a,b,c):
    return printLineFormatter(1, a, b, "", "")

def formatPrintLine(a,b,c, *args):
    d = ""
    if len(args)==1:
        d = args[0]
    return printLineFormatter(0, a, b, c, d)

def printLineFormatter(flag,a,b,c,d):
    # flag = 0  standard print, spread values over 4 columns
    # flag = 1  printing verbose things like Sketch details or Placements, combine columns 3 & 4
    # flag = 2  printing the summary lines, combine columns 1 & 2
    suffix = ""
    if csvFlag:
        pfs2 = printFormatString2csv
        pfs3 = printFormatString3csv
        pfs4 = printFormatString4csv
    else:
        pfs2 = printFormatString2
        pfs3 = printFormatString3
        pfs4 = printFormatString4
    if flag==0:
        aa = a[:f1]
        bb = b[:f2]
        cc = c[:f3]
        dd = d[:f4]
        return pfs4.format(aa,bb,cc,dd)
    elif flag==1:
        aa = a[:f1]
        bb = b[:f2]
        cc = c[:f3+f4]
        dd = d[:f4]
        return pfs3.format(aa,bb,cc)
    else:
        aa = a[:f1+f2]
        bb = b[:f3+f4]
        return pfs2.format(aa,bb)

# Constant definitions
# set some field widths
screenWidth = QtGui.QDesktopWidget().screenGeometry().width()
global f1, f2, f3, f4
# f1 = 15; f2 = 25; f3 = 45; f4 = 25 # 110 columns in 1000 pixels
f1 = 15*screenWidth/1000; f2 = 25*screenWidth/1000; f3 = 45*screenWidth/1000; f4 = 25*screenWidth/1000
# and some print format strings
global printFormatString2, printFormatString3, printFormatString4
global printFormatString2csv, printFormatString3csv, printFormatString4csv
printFormatString2 = "{0:<"+str(f1+f2)+"} {1:<"+str(f3)+"}"
printFormatString2csv = "{0}, {1}"
printFormatString3 = "{0:<"+str(f1)+"} {1:<"+str(f2)+"} {2:<"+str(f3+f4)+"}"
printFormatString3csv = "{0}, {1}, {2}"
printFormatString4 = "{0:<"+str(f1)+"} {1:<"+str(f2)+"} {2:<"+str(f3)+"} {3:<"+str(f4)+"}"
printFormatString4csv = "{0}, {1}, {2}, {3}"
# some button labels that are checked in the code
global choice1, choice2, choice3, csvFlag
choice1 = "Report View"; choice2 = "CSV File"; choice3 = "Window"
csvFlag = False
summarySeparator = "======================================================="
summarySeparatorCsv = "-------------------------------------------------------"
# code ***********************************************************************************
if FreeCAD.ActiveDocument != None:
    # ask if to window or to Report View...
    form = configureMacro()
    form.exec_()
    showSketcherSegmentsFlag = False
    if form.cbss.isChecked():
        showSketcherSegmentsFlag = True
    showPlacementFlag = False
    if form.cbp.isChecked():
        showPlacementFlag = True
    if form.result == choice2:
        csvFlag = True
        showSketcherSegmentsFlag = False
        showPlacementFlag = False
        summarySeparator = summarySeparatorCsv
    printList = countObjects()
    if form.result == choice1: # report to Report View
        mainWindow = FreeCADGui.getMainWindow()
        dockWidgets = mainWindow.findChildren(QtGui.QDockWidget)
        reportViewFlag = False
        for dw in dockWidgets:
            if dw.objectName() == "Report view":
                reportViewFlag = True
        if reportViewFlag:
            print printFormatString4.format(    "", "", "(User Supplied)", "")
            print printFormatString4.format(    "Type", "Shape", "Label", "Name")
            print ""
            for line in printList:
                print line + "\n"
        else:
            QtGui.QMessageBox.information(None,"","Please use 'Menu->View->Views->Report view' to open the 'Report view'")
    if form.result == choice2: # report to CSV file
        filePath = QtGui.QFileDialog.getSaveFileName(parent=None,caption="Save CSV file as",dir=expanduser("~"),filter="*.csv")
        file = open(filePath[0],"w")
        for line in printList:
            file.write(line + "\n")
        file.close()
    if form.result == choice3: # report to window
        #----------------------------------------------------------------------
        longPrintLine = ""
        for line in printList:
            longPrintLine = longPrintLine + line + "\n"
        form = DisplayText(longPrintLine)
#
#OS: Mac OS X
#Word size: 64-bit
#Version: 0.14.3703 (Git)
#Branch: releases/FreeCAD-0-14
#Hash: c6edd47334a3e6f209e493773093db2b9b4f0e40
#Python version: 2.7.5
#Qt version: 4.8.6
#Coin version: 3.1.3
#SoQt version: 1.5.0
#OCC version: 6.7.0
#
#thus ends the macro...
}}




