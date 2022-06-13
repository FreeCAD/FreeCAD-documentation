# Macro Assembly/pl
{{Macro
|Name=Assembly Simulation
|Icon=Macro_Assembly.png
|Description=FreeCad Python assembly animation.
|Author=ralvejd
|Version=1.0
|Date=2014-08-08
|FCVersion=0.18 and below
|Download=The file [http   *//forum.freecadweb.org/download/file.php?id=6740 Assy.fcstd]<br />[https   *//www.freecadweb.org/wiki/images/a/a2/Macro_Assembly.png ToolBar Icon]
}}

## Description

Simulate assembly .

![](images/Assy.gif )

## Uses

Download the files in FreeCAD and run the macro

## The File 

[Assy.fcstd](http   *//forum.freecadweb.org/download/file.php?id=6740)

## Script

ToolBar Icon ![](images/Macro_Assembly.png )

**Macro\_Assembly.FCMacro**


{{MacroCode|code=

#******************************************************************************
#
# Assembly animation by Joakim Isaksson 20140803
#
#******************************************************************************

import FreeCAD, FreeCADGui, Draft, Part
from FreeCAD import Gui
import math
from pivy import coin
from PySide import QtCore, QtGui
from time import sleep

# + + + + + + BEGIN Animation configuration  + + + + + +

doc_name = "Assy"      # The document name of the FreeCAD model
ani_startwait = 3000   # Milliseconds before the animation starting
ani_partwait   = 50   # Milliseconds before the part begin to move
ani_bitrate = 10      # Milliseconds between part moves
ani_dist = 5         # Distance part moves each time
ani_offset_dist = 200   # Distance part is moved before the animation starts

# Tuples for all parts label
#  *  First item in Tuples is the animation view angle
#  *  The remaining items are label on parts to be assembled in list sequence
ani_1  = ( "z-" , "ChassieBack_001" , "ChassieWall_001" , "ChassieWall_002" ,
           "ChassieWall_003" , "ChassieWall_004" , "ChassieWall_005" ,
           "ChassieFront_001" ) ;
ani_2  = ( "z-" , "ISO4762_M4x12_001" , "ISO4762_M4x12_002" ,
           "ISO4762_M4x12_003" , "ISO4762_M4x12_004" , "ISO4762_M4x12_005" ,
           "ISO4762_M4x12_006" , "ISO4762_M4x12_007" , "ISO4762_M4x12_008" ,
           "ISO4762_M4x12_009" , "ISO4762_M4x12_010" ) ;
ani_3  = ( "z+" , "ISO4762_M4x12_011" , "ISO4762_M4x12_012" ,
           "ISO4762_M4x12_013" , "ISO4762_M4x12_014" , "ISO4762_M4x12_015" ,
           "ISO4762_M4x12_016" , "ISO4762_M4x12_017" , "ISO4762_M4x12_018" ,
           "ISO4762_M4x12_019" , "ISO4762_M4x12_020" ) ;
ani_4  = ( "z+" , "EuroCard_001" , "EuroCard_002" , "EuroCard_003" ,
           "EuroCard_004" ) ;
ani_5  = ( "z+" , "Panel_005" ,  "Panel_006" , "Panel_007" , "Panel_008" ) ;
ani_6  = ( "z+" , "ISO7380_M3x8_" , "ISO7380_M3x8_001" , "ISO7380_M3x8_002" ,
           "ISO7380_M3x8_003" , "ISO7380_M3x8_004" , "ISO7380_M3x8_005" ,
           "ISO7380_M3x8_006" , "ISO7380_M3x8_007" , "ISO7380_M3x8_008" ,
           "ISO7380_M3x8_009" ) ;
ani_7  = ( "z-" , "Panel_001" , "Panel_002" , "Panel_003" , "Panel_004" ) ;
ani_8  = ( "z-" , "ISO7380_M3x8_010" , "ISO7380_M3x8_011" ,
           "ISO7380_M3x8_012" , "ISO7380_M3x8_013" , "ISO7380_M3x8_014" ,
           "ISO7380_M3x8_015" , "ISO7380_M3x8_016" , "ISO7380_M3x8_017" ,
           "ISO7380_M3x8_018" , "ISO7380_M3x8_019" ) ;
ani_9  = ( "y-" , "LidBottom_001" ) ;
ani_10 = ( "y-" , "ISO10642_M3x8_" , "ISO10642_M3x8_001" ,
           "ISO10642_M3x8_002" , "ISO10642_M3x8_003" , "ISO10642_M3x8_004" ,
           "ISO10642_M3x8_005" , "ISO10642_M3x8_006" , "ISO10642_M3x8_007" ,
           "ISO10642_M3x8_008" , "ISO10642_M3x8_009" ) ;
ani_11 = ( "y+" , "LidTop_001" ) ;
ani_12 = ( "y+" , "ISO10642_M3x8_010" , "ISO10642_M3x8_011" ,
           "ISO10642_M3x8_012" , "ISO10642_M3x8_013" , "ISO10642_M3x8_014" ,
           "ISO10642_M3x8_015" , "ISO10642_M3x8_016" , "ISO10642_M3x8_017" ,
           "ISO10642_M3x8_018" , "ISO10642_M3x8_019" ) ;

# Set the animation end view
ani_end = "z-"

# Camera oriantations
#  *  Edit this tuples to your need
rear_view_pos    = ( -400 , -80 , 480 ) ;
rear_view_ang    = ( 0 , 1 , 0  ) ;
front_view_pos    = ( -400 , 80 , 480 ) ;
front_view_ang    = ( 0 , -1 , 0  ) ;
top_view_pos    = ( -400 , -80 , 480  ) ;
top_view_ang    = ( -1 , 0 , 0 ) ;
bottom_view_pos = ( -400 , 80 , -480 );
bottom_view_ang = ( 1 , 0 , 0 ) ;

# + + + + + + END Animation configuration  + + + + + +

# + + + + + + Function  + + + + + +

def pulse(milliseconds)   *
   for i in range(milliseconds/10  )   *
      Gui.updateGui( )
      sleep(0.01)

def setView(axis_vector, rotation_vector)   *
   r=App.Rotation(App.Vector(axis_vector),App.Vector(rotation_vector))
   Gui.ActiveDocument.ActiveView.setCameraOrientation(r.Q)

def getPartName(label)   *
   for i in App.ActiveDocument.Objects   *
      if str(i.Label) == label   *
         #App.Console.PrintMessage(str(i.Name) + "  <->  " + i.Label + "\n")
         return str(i.Name)

def animate(aniList)   *
   total = len(aniList)
   for n in range(1,total)   *
      direction = aniList[0]
      #App.Console.PrintMessage(str(aniList) + "    * " + str(direction) + "\n")
      part_name = getPartName(aniList[n])
      tmpX = App.getDocument(doc_name).getObject(part_name).Placement.Base[0]
      tmpY = App.getDocument(doc_name).getObject(part_name).Placement.Base[1]
      tmpZ = App.getDocument(doc_name).getObject(part_name).Placement.Base[2]
      tmpRotation=App.ActiveDocument.getObject(part_name).Placement.Rotation
      #Show the part
      if direction == "x+"   *   #TODO not tested
         setView(rear_view_pos , rear_view_ang)
         tmpDist = tmpX + ani_offset_dist
         sel = FreeCADGui.Selection.clearSelection (doc_name )
         App.ActiveDocument.getObject(part_name).Placement=App.Placement\
               (App.Vector(tmpX,tmpDist,tmpZ), App.Rotation(tmpRotation),\
                App.Vector(0,0,0))
         Gui.getDocument(doc_name).getObject(part_name).Visibility=True
         pulse(ani_partwait)
         
         for i in range(0,ani_step)   *
            tmpDist = tmpDist - ani_dist
            App.ActiveDocument.getObject(part_name).Placement=\
                   App.Placement(App.Vector(tmpX,tmpDist,tmpZ),\
                   App.Rotation(tmpRotation), App.Vector(0,0,0))
            pulse(ani_bitrate)

      elif direction == "x-"   *   #TODO not tested
         setView(front_view_pos , front_view_ang)
         tmpDist = tmpX - ani_offset_dist
         sel = FreeCADGui.Selection.clearSelection (doc_name )
         App.ActiveDocument.getObject(part_name).Placement=App.Placement\
               (App.Vector(tmpX,tmpDist,tmpZ),\
               App.Rotation(tmpRotation), App.Vector(0,0,0))
         Gui.getDocument(doc_name).getObject(part_name).Visibility=True
         pulse(ani_partwait)
         
         for i in range(0,ani_step)   *
            tmpDist = tmpDist + ani_dist
            App.ActiveDocument.getObject(part_name).Placement=App.\
                   Placement(App.Vector(tmpX,tmpDist,tmpZ),\
                   App.Rotation(tmpRotation), App.Vector(0,0,0))
            pulse(ani_bitrate)

      elif direction == "y+"   *
         setView(rear_view_pos , rear_view_ang)
         tmpDist = tmpY + ani_offset_dist
         sel = FreeCADGui.Selection.clearSelection (doc_name )
         App.ActiveDocument.getObject(part_name).Placement=App.Placement\
               (App.Vector(tmpX,tmpDist,tmpZ), App.Rotation(tmpRotation),\
               App.Vector(0,0,0))
         Gui.getDocument(doc_name).getObject(part_name).Visibility=True
         pulse(ani_partwait)
         
         for i in range(0,ani_step)   *
            tmpDist = tmpDist - ani_dist
            App.ActiveDocument.getObject(part_name).Placement=App.\
                   Placement(App.Vector(tmpX,tmpDist,tmpZ),\
                   App.Rotation(tmpRotation),App.Vector(0,0,0))
            pulse(ani_bitrate)

      elif direction == "y-"   *
         setView(front_view_pos , front_view_ang)
         tmpDist = tmpY - ani_offset_dist
         sel = FreeCADGui.Selection.clearSelection (doc_name )
         App.ActiveDocument.getObject(part_name).Placement=App.Placement\
               (App.Vector(tmpX,tmpDist,tmpZ), App.Rotation(tmpRotation),\
               App.Vector(0,0,0))
         Gui.getDocument(doc_name).getObject(part_name).Visibility=True
         pulse(ani_partwait)
         
         for i in range(0,ani_step)   *
            tmpDist = tmpDist + ani_dist
            App.ActiveDocument.getObject(part_name).Placement=App.\
                   Placement(App.Vector(tmpX,tmpDist,tmpZ),\
                   App.Rotation(tmpRotation), App.Vector(0,0,0))
            pulse(ani_bitrate)

      elif direction == "z+"   *
         setView(top_view_pos , top_view_ang)
         tmpDist = tmpZ +ani_offset_dist
         sel = FreeCADGui.Selection.clearSelection (doc_name )
         App.ActiveDocument.getObject(part_name).Placement=App.Placement\
               (App.Vector(tmpX,tmpY,tmpDist), App.Rotation(tmpRotation),\
               App.Vector(0,0,0))
         Gui.getDocument(doc_name).getObject(part_name).Visibility=True
         pulse(ani_partwait)
         
         for i in range(0,ani_step)   *
            tmpDist = tmpDist - ani_dist
            App.ActiveDocument.getObject(part_name).Placement=App.\
                   Placement(App.Vector(tmpX,tmpY,tmpDist),\
                   App.Rotation(tmpRotation), App.Vector(0,0,0))
            pulse(ani_bitrate)

      elif direction == "z-"   *
         setView(bottom_view_pos , bottom_view_ang)
         tmpDist = tmpZ - ani_offset_dist
         sel = FreeCADGui.Selection.clearSelection (doc_name )
         App.ActiveDocument.getObject(part_name).Placement=App.Placement\
               (App.Vector(tmpX,tmpY,tmpDist), App.Rotation(tmpRotation),\
               App.Vector(0,0,0))
         Gui.getDocument(doc_name).getObject(part_name).Visibility=True
         pulse(ani_partwait)
         
         for i in range(0,ani_step)   *
            tmpDist = tmpDist + ani_dist
            App.ActiveDocument.getObject(part_name).Placement=App.\
                   Placement(App.Vector(tmpX,tmpY,tmpDist),\
                   App.Rotation(tmpRotation), App.Vector(0,0,0))
            pulse(ani_bitrate)

def theend(direction)   *
   if direction == "x+"   *
      setView(rear_view_pos , rear_view_ang)
   elif direction == "x-"   *
      setView(front_view_pos , front_view_ang)
   elif direction == "y+"   *
      setView(rear_view_pos , rear_view_ang)
   elif direction == "y-"   *
      setView(front_view_pos , front_view_ang)
   elif direction == "z+"   *
      setView(top_view_pos , top_view_ang)
   elif direction == "z-"   *
      setView(bottom_view_pos , bottom_view_ang)

def startAnimation()   *
 # Animation sequence
   animate(ani_1)
   animate(ani_2)
   animate(ani_3)
   animate(ani_4)
   animate(ani_5)
   animate(ani_6)
   animate(ani_7)
   animate(ani_8)
   animate(ani_9)
   animate(ani_10)
   animate(ani_11)
   animate(ani_12)
   theend(ani_end)
   Gui.ActiveDocument.ActiveView.startAnimating(0,1,0,0.2) #TODO fixit

# + + + + + + Main + + + + + +
# Set full screen
App.setActiveDocument(doc_name)
App.ActiveDocument=App.getDocument(doc_name)
ActiveDocument=Gui.getDocument(doc_name)
Gui.updateGui ( )
mw=QtGui.qApp.activeWindow()
ev=QtGui.QKeyEvent(QtCore.QEvent.KeyPress,\
   QtCore.Qt.Key_F11,QtCore.Qt.NoModifier)
QtGui.qApp.sendEvent(mw,ev)

# A short break for the GUI to catch up
pulse(ani_startwait)

# Adjust ani_offset if Modulus != 0
ani_offset_dist = ani_offset_dist - ani_offset_dist % ani_dist

# Calculate the required number of steps for the animation
ani_step = ani_offset_dist / ani_dist

startAnimation()
}}

## Link

The page discussion [FreeCad Python assembly animation](http   *//forum.freecadweb.org/viewtopic.php?f=22&t=7256)

[See the animation on YouTube.](http   *//youtu.be/5Ik2Bh4wXYg)



---
![](images/Right_arrow.png) [documentation index](../README.md) > Macro Assembly/pl
