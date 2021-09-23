# Macro Corner shapes wizard/update/it
{{Macro/it
|Icon=Macro_Corner_shapes_wizard.png
|Name=Corner shapes wizard
|Name/it=Angolare 2
|Description=Questa macro è un'applicazione completa che apre una finestra di dialogo per dimensionare pezzi angolari, quindi crea l'oggetto nel documento e crea una pagina con la vista superiore, frontale e laterale del pezzo.
|Author=Nicotuf
|Version=2.0
|Date=2013-03-10
|FCVersion= <= 0.17
|Download=[https://www.freecadweb.org/wiki/images/6/60/Macro_Corner_shapes_wizard.png ToolBar Icon]
}}

## Descrizione

Questa macro è un\'applicazione completa che apre una finestra di dialogo per dimensionare pezzi angolari, quindi crea l\'oggetto nel documento e crea una pagina con la vista superiore, frontale e laterale del pezzo. Versione originale: [Macro Corner shapes wizard](Macro_Corner_shapes_wizard/it.md)

## Script

ToolBar Icon ![](images/Macro_Corner_shapes_wizard.png )

**Macro\_Corner\_shapes\_wizard\_update.FCMacro**

     
    # Corner Shape Wizard
    # http://www.freecadweb.org/wiki/index.php?title=Macro_Corner_shapes_wizard/update
    # Version 10.03.2013
    # Modifications: Neondata, Rainer Nase
    # original source: http://www.freecadweb.org/wiki/index.php?title=Macro_Corner_shapes_wizard
    # -*- coding:utf-8 -*-
    #
    # output to page file commented out ?
    #####################################
    # import external functions
     
    #from os import *
    import FreeCAD as App, FreeCADGui as Gui, Part, Draft, math, MeshPart, Mesh, Drawing
    #from PyQt4 import QtGui,QtCore
    from PySide import QtGui,QtCore
    from FreeCAD import Base
    App=FreeCAD
    Gui=FreeCADGui
     
    ##################################
    # Class definition
      
    class CornerSteel:
       def __init__(self, obj):
          obj.addProperty("App::PropertyLength","L1","CornerSteel","Width_1").L1=20.0
          obj.addProperty("App::PropertyLength","L2","CornerSteel","Width_2").L2=20.0
          obj.addProperty("App::PropertyLength","e1","CornerSteel","Thickness").e1=2.0
          #obj.addProperty("App::PropertyLength","e2","CornerSteel","Thickness2").e2=2.0
          obj.addProperty("App::PropertyLength","Length","CornerSteel","Length").Length=200.0
          obj.Proxy = self
     
       def execute(self, fp):
          P1=Base.Vector(fp.e1,fp.e1,0)
          S1=Part.makeBox(fp.L1,fp.L2,fp.Length)
          S2=Part.makeBox(fp.L1-fp.e1,fp.L2-fp.e1,fp.Length,P1)
          fp.Shape=S1.cut(S2)   
      
    ##################################
    # definition of local functions :
      
      
    def proceed():
       QtGui.qApp.setOverrideCursor(QtCore.Qt.WaitCursor)
     
       if App.ActiveDocument==None:
          App.newDocument("CornerSteel")
      
       oldDocumentObjects=App.ActiveDocument.Objects
      
       try:
          QL1     = float(l[0].text())   
          QL2     = float(l[1].text())
          Qe      = float(l[2].text())
          QLength = float(l[3].text())
       except:
          App.Console.PrintError("Wrong input! Only numbers allowed...\n")
      
       Cor=App.ActiveDocument.addObject("Part::FeaturePython","CornerSteel")
       CornerSteel(Cor)
       Cor.ViewObject.Proxy=0
       Cor.L1 = QL1
       Cor.L2 = QL2
       Cor.e1 = Qe
       Cor.Length=QLength
     
       App.ActiveDocument.recompute()
       Gui.SendMsgToActiveView("ViewFit")
     
       QtGui.qApp.restoreOverrideCursor()
         
       Drawing(Cor)
         
       dialog.hide()
      
    def hide():
      
       dialog.hide()
      
    def Drawing(obj):
      
       ObjetProjete=obj.Shape
      
       DimX=ObjetProjete.BoundBox.XLength
       DimY=ObjetProjete.BoundBox.YLength
       DimZ=ObjetProjete.BoundBox.ZLength
      
       page = App.activeDocument().addObject('Drawing::FeaturePage','Page')
       page.Template = App.getResourceDir()+'Mod/Drawing/Templates/A3_Landscape.svg'   
       ProfileView = App.activeDocument().addObject('Drawing::FeatureViewPart','ProfileView')
       ProfileView.Source = obj
       ProfileView.Direction = (0.0,0.0,1.0)
       ProfileView.Scale = 1.0
       ProfileView.X = 50.0
       ProfileView.Y = 50.0
       page.addObject(ProfileView)
      
       LeftView = App.activeDocument().addObject('Drawing::FeatureViewPart','LeftView')
       LeftView.Source = obj
       LeftView.Direction = (-1.0,0.0,0.0)
       LeftView.ShowHiddenLines = True
       LeftView.Scale = 1.0
       LeftView.Rotation = 180.0
       LeftView.X = 50.0+DimX/2+DimX
       LeftView.Y = 50.0
       page.addObject(LeftView)
      
       TopView = App.activeDocument().addObject('Drawing::FeatureViewPart','TopView')
       TopView.Source = obj
       TopView.Direction = (0.0,-1.0,0.0)
       TopView.ShowHiddenLines = True
       TopView.Scale = 1.0
       TopView.Rotation = 180.0
       TopView.X = 50.0+DimX/2+DimX
       TopView.Y = 50.0+DimX/2+DimY+DimX
       page.addObject(TopView)
      
       IsoView = App.activeDocument().addObject('Drawing::FeatureViewPart','IsoView')
       IsoView.Source = obj
       IsoView.Direction = (-1.0,-1.0,0.5)
       IsoView.Scale = 1.0
       IsoView.ShowSmoothLines = True
       IsoView.X = DimZ+DimX/2
       IsoView.Y = 7*DimZ+3*DimY
       page.addObject(IsoView)
         
      
       App.activeDocument().recompute()
      
     #  PageFile = open(page.PageResult,'r')
     #  OutFile = open('temp.svg','w')
     #  OutFile.write(PageFile.read())
     #  del OutFile,PageFile
         
      
      
      
      
    l = []  # Array to transfer parameters to the process
      
    F =     [ ["Width first side"         ,   "20."] ]
    F.append(["Width second side"        ,   "10."])
    F.append(["Thickness"                ,    "3."])
    F.append(["Length"                   ,  "100."])
      
    dialog = QtGui.QDialog()
    dialog.resize(200,200)
    dialog.setWindowTitle("Angle profile (angle steel)")
    la = QtGui.QVBoxLayout(dialog)
      
    # adding the input fields to the GUI
    for field in range(len(F)):
      
      la.addWidget(QtGui.QLabel(F[field][0]))
      l.append( QtGui.QLineEdit(F[field][1]) )
      la.addWidget(l[field])
      
    e1 = QtGui.QLabel("Dimensions of the corner profile")
    commentFont=QtGui.QFont("Arial",10,True)
    e1.setFont(commentFont)
    la.addWidget(e1)
      
      
    okbox = QtGui.QDialogButtonBox(dialog)
    okbox.setOrientation(QtCore.Qt.Horizontal)
    okbox.setStandardButtons(QtGui.QDialogButtonBox.Cancel|QtGui.QDialogButtonBox.Ok)
    la.addWidget(okbox)
      
    QtCore.QObject.connect(okbox, QtCore.SIGNAL("accepted()"), proceed)
    QtCore.QObject.connect(okbox, QtCore.SIGNAL("rejected()"), hide)
    QtCore.QMetaObject.connectSlotsByName(dialog)
    dialog.show()

---
[documentation index](../README.md) > Macro Corner shapes wizard/update/it
