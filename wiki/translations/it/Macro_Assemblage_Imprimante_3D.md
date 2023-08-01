# Macro Assemblage Imprimante 3D/it
{{Macro/it
|Name=Macro_Assemblage_Imprimante_3D
|Icon=Macro_Assemblage_Imprimante_3D.png
|Translate=Simulazione stampante 3D
|Description=Simula il movimento di una stampante 3D sull'asse Z.
|Author=fran6t
|Version=1.0
|Date=2015-07-13
|FCVersion=0.15
|Download=Not file .FCStd for testing<br />[https://www.freecadweb.org/wiki/images/8/8c/Macro_Assemblage_Imprimante_3D.png ToolBar Icon]
}}

## Descrizione

Simula il movimento di una stampante 3D sull\'asse Z

![](images/Assemblage_Imprimante_3D.gif )

## Uso

Scaricare il file e aprirlo in FreeCAD

Copiare la macro e incollarla nella console Python

Per interrompere l\'animazione digitare: **animation.stop()**

## Il File 

[00_assemblage_total.fcstd](http://blog.passion-tarn-et-garonne.info/public/3D/pb-avec-freecad/00-assemblage-total.fcstd)

## Script

L\'autore dello script che è stato adottato per questo progetto è **[Javier Martínez García (JMG)](http://forum.freecadweb.org/memberlist.php?mode=viewprofile&u=2538)**.

ToolBar Icon ![](images/Macro_Assemblage_Imprimante_3D.png )

**00-assemblage-total.FCMacro**


{{MacroCode|code=
# Mouvement va et vient du chariot et tete selon axe Z
#
# Pour arreter l'animation il faut taper animation.stop() dans la console

__author__ = "Javier Martínez García"

import FreeCAD as App, FreeCADGui as Gui, Part, time, sys, math, Draft, DraftGeomUtils

try:
    from PyQt4 import QtGui,QtCore
except Exception:
    from PySide import QtGui,QtCore

class Animation(object):
   def __init__(self):
      App.Console.PrintMessage('init')
      App.ActiveDocument.recompute()
      self.timer = QtCore.QTimer()
      QtCore.QObject.connect(self.timer, QtCore.SIGNAL("timeout()"), self.my_update)
      self.timer.start(50)

      self.an = 0
      self.Tige_Guide_X = 142
      self.X_End_Tendeur = 90
      self.X_Chariot = 102
      self.Nema_17_motor_X = 119
      self.Anti_Backslash_Z_Gauche = 88
      self.Jhead_droite = 126.5
      self.enstopX = 168
      self.sens = 1

   def my_update(self):
      if ( self.an == 0 ) :
         self.sens = 1
      if ( self.an == 245 ) :
         self.sens = -1
      self.an = self.an + self.sens
      self.Tige_Guide_X = self.Tige_Guide_X + self.sens
      self.X_End_Tendeur = self.X_End_Tendeur + self.sens
      self.X_Chariot = self.X_Chariot + self.sens
      self.Nema_17_motor_X = self.Nema_17_motor_X + self.sens
      self.Jhead_droite = self.Jhead_droite + self.sens
      self.Anti_Backslash_Z_Gauche = self.Anti_Backslash_Z_Gauche + self.sens
      self.enstopX = self.enstopX + self.sens

      #12-X-End-Moteur
      #FreeCAD.getDocument("_0_assemblage_total").getObject("Pocket013").Placement = App.Placement(App.Vector(-133,0,self.an),App.Rotation(App.Vector(0,0,1),0))
      FreeCAD.getDocument("_0_assemblage_total").getObject("refine002").Placement = App.Placement(App.Vector(0,0,self.an),App.Rotation(App.Vector(0,0,1),0))      
      #Tige-Guide-X      
      FreeCAD.getDocument("_0_assemblage_total").getObject("Pad025").Placement = App.Placement(App.Vector(-180,13.55,self.Tige_Guide_X),App.Rotation(App.Vector(0.57735,0.57735,0.57735),120))
      #14-X-End-Tendeur      
      FreeCAD.getDocument("_0_assemblage_total").getObject("Pocket011").Placement = App.Placement(App.Vector(236,0,self.X_End_Tendeur),App.Rotation(App.Vector(0,0,1),0))
      #13-X-Chariot
      FreeCAD.getDocument("_0_assemblage_total").getObject("Pocket014").Placement = App.Placement(App.Vector(-18,25,self.X_Chariot),App.Rotation(App.Vector(1,0,0),90))
      #Nema-17-motor-X
      FreeCAD.getDocument("_0_assemblage_total").getObject("Chamfer003").Placement = App.Placement(App.Vector(-205.2,63,self.Nema_17_motor_X),App.Rotation(App.Vector(1,0,0),90))
      #15-Anti-Backslash-Z-x2-1
      FreeCAD.getDocument("_0_assemblage_total").getObject("Pad012").Placement = App.Placement(App.Vector(-156,-15,self.Anti_Backslash_Z_Gauche),App.Rotation(App.Vector(0.999985,0.00555547,0),180))
      #Jhead-Droite
      FreeCAD.getDocument("_0_assemblage_total").getObject("Pocket015").Placement = App.Placement(App.Vector(-50.8,-4.4,self.Jhead_droite),App.Rotation(App.Vector(0,0,1),0))
      #Endstop X
      FreeCAD.getDocument("_0_assemblage_total").getObject("refine003").Placement = App.Placement(App.Vector(-154.2,15,self.enstopX),App.Rotation(App.Vector(0.57735,0.57735,-0.57735),120))
   def stop(self):
      self.timer.stop()     

animation = Animation()

}}

## Link

La pagina della discussione nel forum: [Je galere pour tourner une piece](http://forum.freecadweb.org/viewtopic.php?f=12&t=11782)

Il canale Youtube dell\'autore della macro [FreeCAD: Gear Animation Tutorial](https://www.youtube.com/watch?v=KynMmsLJXV0) e il suo [blog](http://linuxforanengineer.blogspot.com.es/p/me.html)



---
⏵ [documentation index](../README.md) > Macro Assemblage Imprimante 3D/it
