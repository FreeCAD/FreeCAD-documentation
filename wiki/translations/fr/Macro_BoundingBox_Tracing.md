# Macro BoundingBox Tracing/fr
{{Macro/fr
|Name=Macro BoundingBox Tracing
|Icon=BoundBoxTracing.png
|Description=Crée un contour rouge de la BoundingBox (6 faces avec 6 rectangles) d'un objet, crée le volume du boundBox.
|Author=Mario52
|Version=0.12
|Date=2021/07/10
|FCVersion=Toutes versions
|Download=[https://www.freecadweb.org/wiki/images/6/60/BoundBoxTracing.png ToolBar Icon]
}}

## Description

Cette macro crée un contour rouge de la boîte englobante (6 faces avec 6 rectangles) d\'un objet, affiche la dimension du rectangle, crée le volume de la boîte englobante.

<img alt="" src=images/Macro_BoundingBox_Tracing_00.png  style="width:480px;">

:   
    
*La macro BoundingBox Tracing en action*
    



## Utilisation

1.  Sélectionner un objet
2.  Lancer la macro

:   Résultat : 6 rectangles seront soulignés en rouge.

<img alt="" src=images/Macro_BoundingBox_Tracing_01.png  style="width:480px;"> 
*Conteneur d'information*



## Remarques

Configuration : voir les lignes de 61 à 84



## Icône

Téléchargez l\'image du fichier et copiez-la dans votre répertoire de macros.

Cliquez sur l\'image, dans la nouvelle fenêtre positionnez la souris sur l\'image, cliquez sur le bouton droit de la souris et faites \"Save target as \...\"

Icône de la barre d\'outils ![](images/BoundBoxTracing.png )

## Script

**Macro_BoundingBox_Tracing.FCMacro**


{{MacroCode|code=
# -*- coding: utf-8 -*-
from __future__ import unicode_literals

# cette macro trace en rouge (modifiable) le tour du boundingbox avec 6 rectangles
# si "createVol" = 1 il sera cree un volume (rouge) de la dimension du BoundBox
# this macro red trace (editable) around the BoundingBox with 6 rectangles
# if "createVol" = 1 on volume (red) is created 
# Macro_BoundingBox_Tracing
#
#OS: Windows Vista     #OS: Windows 8.1                                #OS: Windows 10                                 #OS: Windows 10
#Platform: 32-bit      #Word size of OS: 64-bit                        #Word size of OS: 64-bit                        #Word size of OS: 64-bit
#Version: 0.14.3389    #Word size of FreeCAD: 64-bit                   #Word size of FreeCAD: 64-bit                   #Word size of FreeCAD: 64-bit
#Python version: 2.6.2 #Version: 0.15.4671 (Git)                       #Version: 0.16.6700 (Git)                       #Version: 0.17.13528 (Git)
#Qt version: 4.5.2     #Branch: releases/FreeCAD-0-15                  #Build type: Release                            #Build type: Release
#Coin version: 3.1.0   #Hash: 244b3aef360841646cbfe80a1b225c8b39c8380c #Branch: releases/FreeCAD-0-16                  #Branch: releases/FreeCAD-0-17
#SoQt version: 1.4.1   #Python version: 2.7.8                          #Hash: 7b925d11aa69ac405b423635adb1e2833f18a817 #Hash: 5c3f7bf8ec51e2c7187789f7edba71a7aa82a88b
#OCC version: 6.5.1    #Qt version: 4.8.6                              #Python version: 2.7.8                          #Python version: 2.7.14
#                      #Coin version: 4.0.0a                           #Qt version: 4.8.6                              #Qt version: 4.8.7
#                      #OCC version: 6.8.0.oce-0.17                    #Coin version: 4.0.0a                           #Coin version: 4.0.0a
#                                                                      #OCC version: 6.8.0.oce-0.17                    #OCC version: 7.2.0
###############################################################################################################################################
#OS: Windows 10 (10.0)                                #OS: Windows 10 (10.0)
#Word size of OS: 64-bit                              #Word size of FreeCAD: 64-bit
#Word size of FreeCAD: 64-bit                         #Version: 0.20.25131 (Git)
#Version: 0.19.16624 (Git)                            #Build type: Release
#Build type: Release                                  #Branch: master
#Branch: master                                       #Hash: 7c519689f0d5ea78fb3292be36a857d283c05507
#Hash: 222ae7305fdf1097e4ef3d050f69dff47dbd8786       #Python version: 3.8.10
#Python version: 3.6.8                                #Qt version: 5.12.9
#Qt version: 5.12.1                                   #Coin version: 4.0.0
#Coin version: 4.0.0a                                 #OCC version: 7.5.2
#OCC version: 7.3.0                                   #Locale: French/Mars (fr_MA)
###############################################################################################################################################
#
#2021/07/10 modified by edwilliams16 to handle objects in nested part containers
#https://forum.freecadweb.org/viewtopic.php?f=22&t=59852
#
__title__   = "BoundingBox_Tracing"
__author__  = "Mario52"
__url__     = "http://www.freecadweb.org/index-fr.html"
__Wiki__    = "https://www.freecadweb.org/wiki/Macro_BoundingBox_Tracing"
__version__ = "0.12"
__date__    = "2021/07/10" #  YYYY/MM/DD


import PySide
import FreeCAD, FreeCADGui, Draft, Part
App = FreeCAD
import sys

debug = False
if debug:
    from sys import path
    sys.path.append('/Users/ed/opt/anaconda3/lib/python3.7/site-packages')
    import ptvsd
    print("Waiting for debugger attach")
    # 5678 is the default attach port in the VS Code debug configurations
    ptvsd.enable_attach(address=('localhost', 5678), redirect_output=True)
    ptvsd.wait_for_attach()

##### Section configuration begin ##################
##### for volume begin ###################
createVol         = 1           # give 1 for create Volume # mettre a 1 pour creer un volume
createDimVol      = 1           # 1 = create dimension info : 0 = not dimension info
##### for volume end   ###################

##### for dimensions info begin ##########
createDim         = 1           # 1 = create dimension info : 0 = not create dimension info

if int(FreeCAD.Version()[1]) > 17:      # Version de FreeCAD
    DisplayModeText   = str(u"3D text") # available : u"2D text" or u"3D text" 
else:
    DisplayModeText   = str(u"Screen")  # available : u"Screen" or u"World" 

JustificationText = str(u"Center")    # available : "Center" or "Left" or "Right"
FontSizeText      = 3.0         # text info dimension
TextColorText_R   = 0.0         # text color info red      1 = 255
TextColorText_G   = 0.0         # text color info green    1 = 255
TextColorText_B   = 0.0         # text color info blue     1 = 255
arondi            = 3           # round the info ex: 3 = 3 decimals

##### for dimensions info end   ##########
##### Section configuration end ####################


def adjustedGlobalPlacement(obj, locVector):
    '''find global placement to make locVector the local origin with the correct orientation'''
    try:
        objectPlacement = obj.Shape.Placement
        objectGlobalPlacement = obj.getGlobalPlacement()
        locPlacement = App.Placement(locVector, App.Rotation(App.Vector(1,0,0),0))
        return objectGlobalPlacement.multiply(objectPlacement.inverse()).multiply(locPlacement)
    except Exception:
        locPlacement = App.Placement(App.Vector(0,0,0), App.Rotation(0,0,0), App.Vector(0,0,0))
        return locPlacement


sel   = FreeCADGui.Selection.getSelection()
selEx = FreeCADGui.Selection.getSelectionEx()
objs  = [selobj.Object for selobj in selEx]
    
if len(objs) >= 1:
    if hasattr(objs[0], "Shape"):
        s = objs[0].Shape
    elif hasattr(objs[0], "Mesh"):      # upgrade with wmayer thanks #http://forum.freecadweb.org/viewtopic.php?f=13&t=22331
        s = objs[0].Mesh
    elif hasattr(objs[0], "Points"):
        s = objs[0].Points

    try:
        # LineColor
        red   = 1.0  # 1 = 255
        green = 0.0  #
        blue  = 0.0  #    # boundBox
        boundBox_    = s.BoundBox
        boundBoxLX   = boundBox_.XLength
        boundBoxLY   = boundBox_.YLength
        boundBoxLZ   = boundBox_.ZLength
        boundBoxXMin = boundBox_.XMin
        boundBoxYMin = boundBox_.YMin
        boundBoxZMin = boundBox_.ZMin
        boundBoxLocation = App.Vector(boundBox_.XMin,boundBox_.YMin,boundBox_.ZMin)
        nameLabel  = sel[0].Label

        try:
            import unicodedata    
            nameLabel = str(unicodedata.normalize('NFKD', nameLabel).encode('ascii','ignore'))[2:]
        except Exception:
            None

        App.Console.PrintMessage(str(boundBox_)+"\r\n")
        App.Console.PrintMessage("Rectangle      : "+str(boundBoxLX)+" x "+str(boundBoxLY)+" x "+str(boundBoxLZ)+"\r\n")
        
        if (createVol == 1) and (boundBoxLX > 0) and (boundBoxLY > 0) and (boundBoxLZ > 0):  # Create Volume
            BDvol = App.ActiveDocument.addObject("Part::Box",nameLabel + "_BoundBoxVolume")
            #BDvol.Label = "BoundBoxVolume"
            BDvol.Length.Value = boundBoxLX
            BDvol.Width.Value  = boundBoxLY
            BDvol.Height.Value = boundBoxLZ
            BDvol.Placement = adjustedGlobalPlacement(objs[0], boundBoxLocation)
            BDPl = BDvol.Placement
            oripl_X=BDvol.Placement.Base.x
            oripl_Y=BDvol.Placement.Base.y
            oripl_Z=BDvol.Placement.Base.z
            #if debug: print(f'global {globalObjectPlacement}\n local {localObjectPlacement} BB {BBlocPlacement}')
            FreeCADGui.ActiveDocument.getObject(BDvol.Name).LineColor  = (red, green, blue)
            FreeCADGui.ActiveDocument.getObject(BDvol.Name).PointColor = (red, green, blue)
            FreeCADGui.ActiveDocument.getObject(BDvol.Name).ShapeColor = (red, green, blue)
            FreeCADGui.ActiveDocument.getObject(BDvol.Name).Transparency = 80
            App.Console.PrintMessage(nameLabel + "_BoundBoxVolume : " + str(BDvol.Shape.Volume)+"\r\n")        if createDimVol == 1:    # section create dimension info for volume
                conteneurVol = []
                del conteneurVol[:]
                conteneurVol = App.activeDocument().addObject("App::DocumentObjectGroup",nameLabel + "_BoundBoxVolume_Info")            #pl_0C1 = Draft.make_text([str(round(boundBoxLX,arondi))],point=FreeCAD.Vector(oripl_X + (boundBoxLX/2), oripl_Y, oripl_Z))
                pl_0C1 = Draft.make_text([str(round(boundBoxLX,arondi))],placement = BDPl.multVec(App.Vector(boundBoxLX/2,0,0)))
                pl_0C1.ViewObject.DisplayMode   = DisplayModeText
                pl_0C1.ViewObject.Justification = JustificationText
                pl_0C1.ViewObject.TextColor     = (TextColorText_R, TextColorText_G, TextColorText_B)
                pl_0C1.ViewObject.FontSize      = FontSizeText
                pl_0C1.Label      = nameLabel + "_Volume_X_" + str(round(boundBoxLX,arondi))
                conteneurVol.addObject(pl_0C1)            #pl_0C2 = Draft.make_text([str(round(boundBoxLY,arondi))],point=FreeCAD.Vector(oripl_X, oripl_Y + (boundBoxLY/2), oripl_Z))
                pl_0C2 = Draft.make_text([str(round(boundBoxLY,arondi))],placement = BDPl.multVec(App.Vector(0, boundBoxLY/2, 0)))
                pl_0C2.ViewObject.DisplayMode   = DisplayModeText
                pl_0C2.ViewObject.Justification = JustificationText
                pl_0C2.ViewObject.TextColor     = (TextColorText_R, TextColorText_G, TextColorText_B)
                pl_0C2.ViewObject.FontSize      = FontSizeText
                pl_0C2.Label      = nameLabel + "_Volume_Y_" + str(round(boundBoxLY,arondi))
                conteneurVol.addObject(pl_0C2)
        
                #pl_0C3 = Draft.make_text([str(round(boundBoxLZ,arondi))],placement=FreeCAD.Vector(oripl_X, oripl_Y, oripl_Z + (boundBoxLZ/2)))
                pl_0C3 = Draft.make_text([str(round(boundBoxLZ,arondi))],placement = BDPl.multVec(App.Vector(0, 0, boundBoxLZ/2)))
                pl_0C3.ViewObject.DisplayMode   = DisplayModeText
                pl_0C3.ViewObject.Justification = JustificationText
                pl_0C3.ViewObject.TextColor     = (TextColorText_R, TextColorText_G, TextColorText_B)
                pl_0C3.ViewObject.FontSize      = FontSizeText
                pl_0C3.Label      = nameLabel + "_Volume_Z_" + str(round(boundBoxLZ,arondi))
                conteneurVol.addObject(pl_0C3)#    else:
    #        App.Console.PrintMessage("Not Volume BoundBox possible"+"\r\n")
        App.Console.PrintMessage("_____________________"+"\r\n")
    #####
        conteneurRectangle = []
        del conteneurRectangle[:]
        conteneurRectangle = App.activeDocument().addObject("App::DocumentObjectGroup",nameLabel + "_BoundBoxRectangle")    if createDim == 1:    # conteneur dimension info
            conteneurInfo = []
            del conteneurInfo[:]
            conteneurInfo = App.activeDocument().addObject("App::DocumentObjectGroup",nameLabel + "_BoundBoxRectangle_Info")
        try:
            if (boundBoxLX and boundBoxLY) > 0.0:
                #pl_0 = App.Placement(App.Vector(oripl_X,oripl_Y,oripl_Z), App.Rotation(0.0,0.0,0.0))
                pl_0 = adjustedGlobalPlacement(objs[0], boundBoxLocation)
                double = Draft.makeRectangle(length=boundBoxLX,height=boundBoxLY,placement=pl_0,face=False,support=None) #OK
                double.Label = nameLabel + "_BoundBoxRectangle_Bo"
                FreeCADGui.activeDocument().activeObject().LineColor = (red, green, blue)
                conteneurRectangle.addObject(double)
    #        else:
    #            App.Console.PrintError("not value 0"+"\n")        if createDim == 1:    # section create dimension info
                #pl_0C1 = Draft.make_text([str(round(boundBoxLX,arondi))],placement=FreeCAD.Vector(pl_0.Base.x + (boundBoxLX/2), pl_0.Base.y, pl_0.Base.z))
                # XY -> XY
                pl_0C1 = Draft.make_text([str(round(boundBoxLX,arondi))],placement=pl_0.multVec(App.Vector(boundBoxLX/2, 0, 0)))
                pl_0C1.ViewObject.DisplayMode   = DisplayModeText
                pl_0C1.ViewObject.Justification = JustificationText
                pl_0C1.ViewObject.TextColor     = (TextColorText_R, TextColorText_G, TextColorText_B)
                pl_0C1.ViewObject.FontSize      = FontSizeText
                pl_0C1.Label      = nameLabel + "_Rectangle_Bo_0X_" + str(round(boundBoxLX,arondi))
                conteneurInfo.addObject(pl_0C1)
        
                #pl_0C2 = Draft.make_text([str(round(boundBoxLY,arondi))],placement=FreeCAD.Vector(pl_0.Base.x, pl_0.Base.y + (boundBoxLY/2), pl_0.Base.z))
                pl_0C2 = Draft.make_text([str(round(boundBoxLY,arondi))],placement=pl_0.multVec(App.Vector(0., boundBoxLY/2, 0.)))
                pl_0C2.ViewObject.DisplayMode   = DisplayModeText
                pl_0C2.ViewObject.Justification = JustificationText
                pl_0C2.ViewObject.TextColor     = (TextColorText_R, TextColorText_G, TextColorText_B)
                pl_0C2.ViewObject.FontSize      = FontSizeText
                pl_0C2.Label      = nameLabel + "_Rectangle_Bo_0Y_" + str(round(boundBoxLY,arondi))
                conteneurInfo.addObject(pl_0C2)    except:
            App.Console.PrintError("not done 0"+"\n")

        try:
            if (boundBoxLX and boundBoxLY) > 0.0:
                #pl_1 = App.Placement(App.Vector(oripl_X,oripl_Y,oripl_Z+boundBoxLZ), App.Rotation(0.0,0.0,0.0))
                pl_1 =adjustedGlobalPlacement(objs[0], boundBoxLocation + App.Vector(0,0,boundBoxLZ))
                double = Draft.makeRectangle(length=boundBoxLX,height=boundBoxLY,placement=pl_1,face=False,support=None) #Ok
                double.Label = nameLabel + "_BoundBoxRectangle_To"
                FreeCADGui.activeDocument().activeObject().LineColor = (red, green, blue)
                conteneurRectangle.addObject(double)
    #        else:
    #            App.Console.PrintError("not value 1"+"\n")        if createDim == 1:    # section create dimension info
                #pl_0C1 = Draft.make_text([str(round(boundBoxLX,arondi))],placement=FreeCAD.Vector(pl_1.Base.x + (boundBoxLX/2), pl_1.Base.y, pl_1.Base.z))
                #XY -> XY
                pl_0C1 = Draft.make_text([str(round(boundBoxLX,arondi))],placement=pl_1.multVec(App.Vector(boundBoxLX/2, 0, 0)))
                pl_0C1.ViewObject.DisplayMode   = DisplayModeText
                pl_0C1.ViewObject.Justification = JustificationText
                pl_0C1.ViewObject.TextColor     = (TextColorText_R, TextColorText_G, TextColorText_B)
                pl_0C1.ViewObject.FontSize      = FontSizeText
                pl_0C1.Label      = nameLabel + "_Rectangle_To_1X_" + str(round(boundBoxLX,arondi))
                conteneurInfo.addObject(pl_0C1)
        
                #pl_0C2 = Draft.make_text([str(round(boundBoxLY,arondi))],placement=FreeCAD.Vector(pl_1.Base.x, pl_1.Base.y + (boundBoxLY/2), pl_1.Base.z))
                pl_0C2 = Draft.make_text([str(round(boundBoxLY,arondi))],placement=pl_1.multVec(App.Vector(0., boundBoxLY/2, 0)))

                pl_0C2.ViewObject.DisplayMode   = DisplayModeText
                pl_0C2.ViewObject.Justification = JustificationText
                pl_0C2.ViewObject.TextColor     = (TextColorText_R, TextColorText_G, TextColorText_B)
                pl_0C2.ViewObject.FontSize      = FontSizeText
                pl_0C2.Label      = nameLabel + "_Rectangle_To_1Y_" + str(round(boundBoxLY,arondi))
                conteneurInfo.addObject(pl_0C2)    except:
            App.Console.PrintError("not done 1"+"\n")

        try:
            if (boundBoxLX and boundBoxLZ) > 0.0:
                #pl_2 = App.Placement(App.Vector(oripl_X,oripl_Y,oripl_Z), App.Rotation(0.0,0.0,90))
                pl_2 = pl_0.multiply(App.Placement(App.Vector(0.,0.,0.),App.Rotation(0.0,0.0,90)))
                double = Draft.makeRectangle(length=boundBoxLX,height=boundBoxLZ,placement=pl_2,face=False,support=None) #Ok
                double.Label = nameLabel + "_BoundBoxRectangle_Fr"
                FreeCADGui.activeDocument().activeObject().LineColor = (red, green, blue)
                conteneurRectangle.addObject(double)
    #        else:
    #            App.Console.PrintError("not value 2"+"\n")        if createDim == 1:    # section create dimension info
                #pl_0C1 = Draft.make_text([str(round(boundBoxLX,arondi))],placement=FreeCAD.Vector(pl_2.Base.x + (boundBoxLX/2), pl_2.Base.y, pl_2.Base.z))
                #XZ -> XY
                pl_0C1 = Draft.make_text([str(round(boundBoxLX,arondi))],placement=pl_2.multVec(App.Vector(boundBoxLX/2, 0, 0)))
                pl_0C1.ViewObject.DisplayMode   = DisplayModeText
                pl_0C1.ViewObject.Justification = JustificationText
                pl_0C1.ViewObject.TextColor     = (TextColorText_R, TextColorText_G, TextColorText_B)
                pl_0C1.ViewObject.FontSize      = FontSizeText
                pl_0C1.Label      = nameLabel + "_Rectangle_Fr_2X_" + str(round(boundBoxLX,arondi))
                conteneurInfo.addObject(pl_0C1)
       
                #pl_0C2 = Draft.make_text([str(round(boundBoxLZ,arondi))],placement=FreeCAD.Vector(pl_2.Base.x, pl_2.Base.y, pl_2.Base.z + (boundBoxLZ/2)))
                pl_0C2 = Draft.make_text([str(round(boundBoxLZ,arondi))],placement=pl_2.multVec(App.Vector(0, boundBoxLZ/2, 0)))
                pl_0C2.ViewObject.DisplayMode   = DisplayModeText
                pl_0C2.ViewObject.Justification = JustificationText
                pl_0C2.ViewObject.TextColor     = (TextColorText_R, TextColorText_G, TextColorText_B)
                pl_0C2.ViewObject.FontSize      = FontSizeText
                pl_0C2.Label      = nameLabel + "_Rectangle_Fr_2Z_" + str(round(boundBoxLZ,arondi))
                conteneurInfo.addObject(pl_0C2)    except:
            App.Console.PrintError("not done 2"+"\n")

        try:
            if (boundBoxLX and boundBoxLZ) > 0.0:
                #pl_3 = App.Placement(App.Vector(oripl_X,oripl_Y+boundBoxLY,oripl_Z), App.Rotation(0.0,0.0,90))
                pl_3 = adjustedGlobalPlacement(objs[0], boundBoxLocation+App.Vector(0, boundBoxLY, 0)).multiply(App.Placement(App.Vector(0.,0.,0.),App.Rotation(0.0,0.0,90)))
                double = Draft.makeRectangle(length=boundBoxLX,height=boundBoxLZ,placement=pl_3,face=False,support=None) #Ok
                double.Label = nameLabel + "_BoundBoxRectangle_Re"
                FreeCADGui.activeDocument().activeObject().LineColor = (red, green, blue)
                conteneurRectangle.addObject(double)
    #        else:
    #            App.Console.PrintError("not value 3"+"\n")        if createDim == 1:    # section create dimension info
                #XZ -> XY
                pl_0C1 = Draft.make_text([str(round(boundBoxLX,arondi))],placement=pl_3.multVec(App.Vector(boundBoxLX/2, 0, 0)))
                pl_0C1.ViewObject.DisplayMode   = DisplayModeText
                pl_0C1.ViewObject.Justification = JustificationText
                pl_0C1.ViewObject.TextColor     = (TextColorText_R, TextColorText_G, TextColorText_B)
                pl_0C1.ViewObject.FontSize      = FontSizeText
                pl_0C1.Label      = nameLabel + "_Rectangle_Re_3X_" + str(round(boundBoxLX,arondi))
                conteneurInfo.addObject(pl_0C1)
        
                pl_0C2 = Draft.make_text([str(round(boundBoxLZ,arondi))],placement=pl_3.multVec(App.Vector(0, boundBoxLZ/2, 0)))
                pl_0C2.ViewObject.DisplayMode   = DisplayModeText
                pl_0C2.ViewObject.Justification = JustificationText
                pl_0C2.ViewObject.TextColor     = (TextColorText_R, TextColorText_G, TextColorText_B)
                pl_0C2.ViewObject.FontSize      = FontSizeText
                pl_0C2.Label      = nameLabel + "_Rectangle_Re_3Z_" + str(round(boundBoxLZ,arondi))
                conteneurInfo.addObject(pl_0C2)    except:
            App.Console.PrintError("not done 3"+"\n")

        try:
            if (boundBoxLY and boundBoxLZ) > 0.0:
                #pl_4 = App.Placement(App.Vector(oripl_X,oripl_Y,oripl_Z), App.Rotation(90,0.0,90))
                pl_4 = pl_0.multiply(App.Placement(App.Vector(0.,0.,0.),App.Rotation(90,0,90)))
                double = Draft.makeRectangle(length=boundBoxLY,height=boundBoxLZ,placement=pl_4,face=False,support=None) #Ok
                double.Label = nameLabel + "_BoundBoxRectangle_Le"
                FreeCADGui.activeDocument().activeObject().LineColor = (red, green, blue)
                conteneurRectangle.addObject(double)
    #        else:
    #            App.Console.PrintError("not value 4"+"\n")        if createDim == 1:    # section create dimension info
                #pl_0C1 = Draft.make_text([str(round(boundBoxLY,arondi))],placement=FreeCAD.Vector(pl_4.Base.x, pl_4.Base.y + (boundBoxLY/2), pl_4.Base.z))
                #YZ ->XY
                pl_0C1 = Draft.make_text([str(round(boundBoxLY,arondi))],placement=pl_4.multVec(App.Vector(boundBoxLY/2, 0., 0.)))
                pl_0C1.ViewObject.DisplayMode   = DisplayModeText
                pl_0C1.ViewObject.Justification = JustificationText
                pl_0C1.ViewObject.TextColor     = (TextColorText_R, TextColorText_G, TextColorText_B)
                pl_0C1.ViewObject.FontSize      = FontSizeText
                pl_0C1.Label      = nameLabel + "_Rectangle_Le_4Y_" + str(round(boundBoxLY,arondi))
                conteneurInfo.addObject(pl_0C1)
        
                #pl_0C2 = Draft.make_text([str(round(boundBoxLZ,arondi))],placement=FreeCAD.Vector(pl_4.Base.x, pl_4.Base.y, pl_4.Base.z + (boundBoxLZ/2)))
                pl_0C2 = Draft.make_text([str(round(boundBoxLZ,arondi))],placement=pl_4.multVec(App.Vector(0., boundBoxLZ/2, 0)))
                pl_0C2.ViewObject.DisplayMode   = DisplayModeText
                pl_0C2.ViewObject.Justification = JustificationText
                pl_0C2.ViewObject.TextColor     = (TextColorText_R, TextColorText_G, TextColorText_B)
                pl_0C2.ViewObject.FontSize      = FontSizeText
                pl_0C2.Label      = nameLabel + "_Rectangle_Le_4Z_" + str(round(boundBoxLZ,arondi))
                conteneurInfo.addObject(pl_0C2)    except:
            App.Console.PrintError("not done 4"+"\n")

        try:
            if (boundBoxLY and boundBoxLZ) > 0.0:
                #pl_5 = App.Placement(App.Vector(oripl_X+boundBoxLX,oripl_Y,oripl_Z), App.Rotation(90,0.0,90))
                pl_5 = adjustedGlobalPlacement(objs[0], boundBoxLocation+App.Vector(boundBoxLX,0,0)).multiply(App.Placement(App.Vector(0.,0.,0.),App.Rotation(90,0.0,90)))
                double = Draft.makeRectangle(length=boundBoxLY,height=boundBoxLZ,placement=pl_5,face=False,support=None) #Ok
                double.Label = nameLabel + "_BoundBoxRectangle_Ri"
                FreeCADGui.activeDocument().activeObject().LineColor = (red, green, blue)
                conteneurRectangle.addObject(double)
    #            else:
    #                App.Console.PrintError("not value 5"+"\n")        if createDim == 1:    # section create dimension info
                #YZ-> XY
                pl_0C1 = Draft.make_text([str(round(boundBoxLY,arondi))],placement=pl_5.multVec(App.Vector(boundBoxLY/2, 0, 0)))
                pl_0C1.ViewObject.Justification = JustificationText
                pl_0C1.ViewObject.TextColor     = (TextColorText_R, TextColorText_G, TextColorText_B)
                pl_0C1.ViewObject.FontSize      = FontSizeText
                pl_0C1.Label      = nameLabel + "_Rectangle_Ri_5Y_" + str(round(boundBoxLY,arondi))
                conteneurInfo.addObject(pl_0C1)
        
                pl_0C2 = Draft.make_text([str(round(boundBoxLZ,arondi))],placement=pl_5.multVec(App.Vector(0, boundBoxLZ/2, 0 )))
                pl_0C2.ViewObject.DisplayMode   = DisplayModeText
                pl_0C2.ViewObject.Justification = JustificationText
                pl_0C2.ViewObject.TextColor     = (TextColorText_R, TextColorText_G, TextColorText_B)
                pl_0C2.ViewObject.FontSize      = FontSizeText
                pl_0C2.Label      = nameLabel + "_Rectangle_Ri_5Z_" + str(round(boundBoxLZ,arondi))
                conteneurInfo.addObject(pl_0C2)    except:
            App.Console.PrintError("not done 5"+"\n")    #####
        App.ActiveDocument.recompute()
    except Exception:
        App.Console.PrintError("Bad selection"+"\n")
else:
    App.Console.PrintMessage("Select an object !"+"\n")
}}

## Version

Version : 0.12 Date : 2021/07/10 : mise à jour par edwilliams16 pour gérer les objets dans des conteneurs de pièces imbriqués. [FCInfo CG of assemblies](https://forum.freecadweb.org/viewtopic.php?f=22&t=59852) a corrigé le placement global, merci edwilliams16


```python

def adjustedGlobalPlacement(obj, locVector):
    '''find global placement to make locVector the local origin with the correct orientation'''
    try:
        objectPlacement = obj.Shape.Placement
        objectGlobalPlacement = obj.getGlobalPlacement()
        locPlacement = App.Placement(locVector, App.Rotation(App.Vector(1,0,0),0))
        return objectGlobalPlacement.multiply(objectPlacement.inverse()).multiply(locPlacement)
    except Exception:
        locPlacement = App.Placement(App.Vector(0,0,0), App.Rotation(0,0,0), App.Vector(0,0,0))
        return locPlacement

```

Version: 0.11 Date : 2019/05/29: \"nameLabel = str(unicodedata.normalize(\'NFKD\', nameLabel).encode(\'ascii\',\'ignore\'))\" instead \"def()\"

Version : 0.10 Date : 2019/05/23 upgrade \> 0.19 et suppression des accentués \"éçà..\" avec une def() et pas encode()\....

Version : 0.9 Date : 2018-10-12: ajouter un test \> 17 
```python
if int(FreeCAD.Version()[1]) > 17:      # Version de FreeCAD
    DisplayModeText   = str(u"2D text") # available : u"2D text" or u"3D text" 
else:
    DisplayModeText   = str(u"Screen")  # available : u"Screen" or u"World" 
```

Version : 0.8 Date : 05/10/2018 : mise à jour de la ver 0.8 compatible avec FC 0.17 (getGlobalPlacement)

Version : 0.7 Date : 28/01/2018 : corrige l\'erreur d\'accentuation de l\'étiquette \"nameLabel = unicodedata.normalize(\'NFKD\', nameLabel).encode(\'ascii\',\'ignore\')\".

Version : 0.6 Date : 08/08/2017 : ajout de texte info dimension (annotation), conteneur pour rectangles, info rectangles, info volume, ajout d\'une section configuration couleur, label de l\'objet sélectionné

Version : 0.5 Date : 08/05/2017 : mise à jour accepte maintenant le \"maillage\" et les \"points\" merci wmayer [Makro Bounding-Box für STL importierte Teile und für Punktewolken](http://forum.freecadweb.org/viewtopic.php?f=13&t=22331)

Version : 0.4 Date : 04/06/2016 : test si une valeur = 0 alors ne crée pas de boundbox (ex : objet Draft)



---
![](images/Right_arrow.png) [documentation index](../README.md) > Macro BoundingBox Tracing/fr
