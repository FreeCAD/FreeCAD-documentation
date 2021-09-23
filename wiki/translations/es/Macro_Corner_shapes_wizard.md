# Macro Corner shapes wizard/es
{{Macro/es
|Name=Corner shapes wizard
|Translate=Corner shapes wizard
|Icon=Macro_Corner_shapes_wizard.png
|Description=Esta macro es una aplicación completa, muestra un letrero de diálogo preguntando por las dimensiones de tu cantonera, luego crea el objeto en el documento y crea una página con las vistas en planta, alzado y laterales de la pieza.<br/>This macro use the DrawingWorkBench
|Author=Nicotuf
|Version=1.0
|Date=2011-08-01
|FCVersion= <= 0.17
|Download=[https://www.freecadweb.org/wiki/images/6/60/Macro_Corner_shapes_wizard.png ToolBar Icon]
}}

## Descriptivo

Esta macro es una aplicación completa, muestra un letrero de diálogo preguntando por las dimensiones de tu cantonera, luego crea el objeto en el documento y crea una página con las vistas en planta, alzado y laterales de la pieza.

There is a [modified version](Macro_Corner_shapes_wizard/update.md) with changes GUI.

![](images/CornerShape1.png )

## Script

ToolBar Icon ![](images/Macro_Corner_shapes_wizard.png )

**Macro\_Corner\_shapes\_wizard.FCMacro**

    # -*- coding:utf-8 -*-
     
    #####################################
    # Importation de fonctions externes :
     
    #from os import *
    import FreeCAD, FreeCADGui, Part, Draft, math, MeshPart, Mesh, Drawing
    #from PyQt4 import QtGui,QtCore
    from PySide import QtGui,QtCore
    from FreeCAD import Base
    App=FreeCAD
    Gui=FreeCADGui
     
    ##################################
    # Défnition Class :
     
    class Corniere:
       def __init__(self, obj):
          obj.addProperty("App::PropertyLength","L1","Corniere","Largeur 1").L1=20.0
          obj.addProperty("App::PropertyLength","L2","Corniere","Largeur 2").L2=20.0
          obj.addProperty("App::PropertyLength","e1","Corniere","Epaisseur 1").e1=2.0
          #obj.addProperty("App::PropertyLength","e2","Corniere","Epaisseur 2").e2=2.0
          obj.addProperty("App::PropertyLength","Longueur","Corniere","Longueur").Longueur=200.0
          obj.Proxy = self
     
       def execute(self, fp):
          P1=Base.Vector(fp.e1,fp.e1,0)
          S1=Part.makeBox(fp.L1,fp.L2,fp.Longueur)
          S2=Part.makeBox(fp.L1-fp.e1,fp.L2-fp.e1,fp.Longueur,P1)
          fp.Shape=S1.cut(S2)   
     
    ##################################
    # Défnition locale de fonctions :
     
     
    def proceed():
       QtGui.qApp.setOverrideCursor(QtCore.Qt.WaitCursor)
     
       if FreeCAD.ActiveDocument==None:
          FreeCAD.newDocument("Corniere")
     
       oldDocumentObjects=App.ActiveDocument.Objects
     
       try:
          QL1 = float(l1.text())   
          QL2 = float(l2.text())
          Qe = float(l3.text())
          QLongueur = float(l4.text())
       except:
          FreeCAD.Console.PrintError("Wrong input! Only numbers allowed...\n")
     
       Cor=FreeCAD.ActiveDocument.addObject("Part::FeaturePython","Corniere")
       Corniere(Cor)
       Cor.ViewObject.Proxy=0
       Cor.L1=QL1
       Cor.L2=QL2
       Cor.e1=Qe
       Cor.Longueur=QLongueur
     
       App.ActiveDocument.recompute()
       Gui.SendMsgToActiveView("ViewFit")
     
       QtGui.qApp.restoreOverrideCursor()
     
       Plan(Cor)
     
       dialog.hide()
     
    def hide():
     
       dialog.hide()
     
    def Plan(obj):
     
       ObjetProjete=obj.Shape
     
       TailleX=ObjetProjete.BoundBox.XLength
       TailleY=ObjetProjete.BoundBox.YLength
       TailleZ=ObjetProjete.BoundBox.ZLength
     
       page = App.activeDocument().addObject('Drawing::FeaturePage','Page')
       page.Template = App.getResourceDir()+'Mod/Drawing/Templates/A3_Landscape.svg'   
       vueprofil = App.activeDocument().addObject('Drawing::FeatureViewPart','VueProfil')
       vueprofil.Source = obj
       vueprofil.Direction = (0.0,0.0,1.0)
       vueprofil.Scale = 1.0
       vueprofil.X = 50.0
       vueprofil.Y = 50.0
       page.addObject(vueprofil)
     
       vuegauche = App.activeDocument().addObject('Drawing::FeatureViewPart','Vuegauche')
       vuegauche.Source = obj
       vuegauche.Direction = (-1.0,0.0,0.0)
       vuegauche.ShowHiddenLines = True
       vuegauche.Scale = 1.0
       vuegauche.Rotation = 180.0
       vuegauche.X = 50.0+TailleX/2+TailleX
       vuegauche.Y = 50.0
       page.addObject(vuegauche)
     
       vuedessus = App.activeDocument().addObject('Drawing::FeatureViewPart','Vuedessus')
       vuedessus.Source = obj
       vuedessus.Direction = (0.0,-1.0,0.0)
       vuedessus.ShowHiddenLines = True
       vuedessus.Scale = 1.0
       vuedessus.Rotation = 180.0
       vuedessus.X = 50.0+TailleX/2+TailleX
       vuedessus.Y = 50.0+TailleX/2+TailleY+TailleX
       page.addObject(vuedessus)
     
       vueiso = App.activeDocument().addObject('Drawing::FeatureViewPart','VueIso')
       vueiso.Source = obj
       vueiso.Direction = (-1.0,-1.0,0.5)
       vueiso.Scale = 1.0
       vueiso.ShowSmoothLines = True
       vueiso.X = TailleZ+TailleX/2
       vueiso.Y = 7*TailleZ+3*TailleY
       page.addObject(vueiso)
     
     
       App.activeDocument().recompute()
     
       PageFile = open(page.PageResult,'r')
       OutFile = open('temp.svg','w')
       OutFile.write(PageFile.read())
       del OutFile,PageFile
     
     
    dialog = QtGui.QDialog()
    dialog.resize(200,200)
    dialog.setWindowTitle("Corniere")
    la = QtGui.QVBoxLayout(dialog)
     
    e1 = QtGui.QLabel("Dimensions de la corniere")
    commentFont=QtGui.QFont("Arial",10,True)
    e1.setFont(commentFont)
    la.addWidget(e1)
     
    t1 = QtGui.QLabel("L1")
    la.addWidget(t1)
    l1 = QtGui.QLineEdit()
    l1.setText("20")
    la.addWidget(l1)
     
    t2 = QtGui.QLabel("L2")
    la.addWidget(t2)
    l2 = QtGui.QLineEdit()
    l2.setText("20")
    la.addWidget(l2)
     
    t3 = QtGui.QLabel("e")
    la.addWidget(t3)
    l3 = QtGui.QLineEdit()
    l3.setText("2")
    la.addWidget(l3)
     
    t4 = QtGui.QLabel("Longueur")
    la.addWidget(t4)
    l4 = QtGui.QLineEdit()
    l4.setText("300")
    la.addWidget(l4)
     
    okbox = QtGui.QDialogButtonBox(dialog)
    okbox.setOrientation(QtCore.Qt.Horizontal)
    okbox.setStandardButtons(QtGui.QDialogButtonBox.Cancel|QtGui.QDialogButtonBox.Ok)
    la.addWidget(okbox)
    QtCore.QObject.connect(okbox, QtCore.SIGNAL("accepted()"), proceed)
    QtCore.QObject.connect(okbox, QtCore.SIGNAL("rejected()"), hide)
    QtCore.QMetaObject.connectSlotsByName(dialog)
    dialog.show()

---
[documentation index](../README.md) > Macro Corner shapes wizard/es
