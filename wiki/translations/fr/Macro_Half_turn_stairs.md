# Macro Half turn stairs/fr
 {{Macro/fr
|Name=Half_turn_stairs
|Icon=Text-x-python.png
|Description=Cette macro crée un escalier tournant à gauche ou à droite. La conception des escaliers est définie dans le fichier stairs.dat (vous devez copier les données qui se trouvent dans la page wiki)
|Author=Berner
|Version=1.0
|Date=2016-10-17
|FCVersion=All
|Download=[https://www.freecadweb.org/wiki/images/b/b8/Half_turn_stairs.png ToolBar Icon]
}}

## Description

Cette macro crée un escalier tournant à gauche ou à droite avec le fichier stairs.dat

<img alt="stairs" src=images/Half_turn_stairs.png  style="width:480px;"> 
*Stairs*

## Utilisation

-   Copiez et enregistrez les données en tant que fichier stairs.dat dans votre répertoire de macros, voir ci-dessous le code de (stairs.dat).

-   Lancez la macro et changez la hauteur de l\'escalier sur votre plancher (étage). Il peut tourner vers la gauche ou la droite.

## Script

ToolBar Icon <img alt="" src=images/Half_turn_stairs.png  style="width:64px;">

**Half\_turn\_stairs.FCMacro**


{{MacroCode|code=
<nowiki>
# -*- coding: utf-8 -*-
#
# Half_turn_stairs Macro runs with Freecad 0.17
#
# Author: Berner and Forum
#
# This macro creates a half turn stair from tupels of x,y,z 
# the tupels used to create a dwire for every stair.
# The dwire is extruded, so it give with 18 stairs the total rise 
#
# A sample file with parameters is in stairs.dat
#
# created a wire with coordinate x y z separated (in the file)
#Sample: (delete # on lines without comments)
# Stair 0
#0.0 -240.0 0.0 0.0 0.0 0.0 1000.0 0.0 0.0 1000.0 -240.0 0.0
# Stair 1
#0.0 0.0 0.0 0.0 240.0 0.0 1000.0 240.0 0.0 1000.0 0.0 0.0
#. . . .

from __future__ import unicode_literals
from FreeCAD import Base
import Draft, Part

App.Console.PrintMessage("Half_turn_stairs-Macro\n")
# Get location of user macros
p=FreeCAD.ParamGet("User parameter:BaseApp/Preferences/Macro")
path = p.GetString("MacroPath")
dataset = path + "/stairs.dat"                          # path and name of file.txt
docname = App.ActiveDocument.Name                       # Name of active document
 
debug='n' # Debug Values on Console
rise = 3100.0 # Geschosshoehe Total Rise

left_right="l"  # turn stairs left or left_right
# GUI

from PySide import QtGui
(rise, ok) = QtGui.QInputDialog.getDouble(
        QtGui.QWidget(), 'Total Rise / Geschosshoehe', 'Total Rise /  Geschosshoehe', 2000, 0, 3100, 4)
if ok:
 left_right = QtGui.QInputDialog.getText(None, "left_right", "Turn Left or Right l/r")[0]
if debug == 'y': FreeCAD.Console.PrintMessage("rise="+str(rise) + " " + str(ok) + "\n" )
if debug == 'y': FreeCAD.Console.PrintMessage("left_right="+str(left_right) + " " + str(ok) + "\n" )
# End Gui
step=float(rise/18)  # Treppensteigung / Step_high

# functions
def objnames():  # List object names
 doc = FreeCAD.ActiveDocument
 objs = FreeCAD.ActiveDocument.Objects
 names=''  #list of objectnames
 labels='' # list of objectlabels 
 for obj in objs:
    a = obj.Name                                             # list the Name  of the object  (not modifiable)
    b = obj.Label                                            # list the Label of the object  (modifiable)
    try:
        c = obj.LabelText                                    # list the LabeText of the text (modifiable)
        names=names+str(a)+" "
        labels=labels+str(b)+" "
    except:
        names=names+str(a)+" "
        labels=labels+str(b)+" "
 return names
 if debug == 'y': App.Console.PrintMessage("Names="+str(names) +"\n"+"Labels="+ str(labels) + "\n")
# end functions

file = open(dataset, "r") # open the file read
i = 0 #line counter
line = file.readline()
while(line != ''):    # read number of lines
   if line[0:1] != "#" and len(line) >0:
    i = i + 1
    if debug == "y": App.Console.PrintMessage("Parameter-Line" + str(i) + " " + line + "\n")
   line = file.readline() 
file.close()
numlines=i  # number of parameter-lines
if debug == "y": App.Console.PrintMessage("Number of Parameter-Lines =" + str(numlines) + "\n")
file = open(dataset, "r")                                  # open the file read
wire = []
X=Y=Z = 0.0
if left_right == "r": 
 i = 0 #line counter
else:
 i = numlines 
line = file.readline()
while(line != ''):
    num_words = len(line.split())
    num_tupel = num_words / 3
    if debug == "y": App.Console.PrintMessage(str(num_words) + "\n")
    if debug == "y": App.Console.PrintMessage(str(num_tupel) + "\n")
    if line[0:1] == "#" or num_words != (num_tupel * 3):
     if num_words != (num_tupel * 3):
      App.Console.PrintMessage("Error on Inputfile line " + str(i) + "\n")
      App.Console.PrintMessage("Only " + str(num_words) + " of multiple of 3 Words\n")
    else:
     if line[0:1] == "#": 
      num_words = 0   #  ignore comment
     if debug == "y": App.Console.PrintMessage(line + "\n")
     coordinates = line.split()
     if debug == "y": App.Console.PrintMessage(str(coordinates) + " " + str(num_words) + " " + str(num_tupel)+ str(type(num_words)) + "\n")
     if num_words > 0:
      data=""  # generate statement
      printline="App.Console.PrintMessage(" # generate variable for PrintMessage (debug)
      for x in range(1, num_tupel + 1):
       data=data + "X" + str(x) + ",Y" + str(x) + ",Z" + str(x)
       printline=printline + "str(X" + str(x) + ") + ' ' + " + "str(Y" + str(x) + ") + ' ' + " + "str(Z" + str(x) + ") + ' '"
       if x < num_tupel: 
        data=data + ","
        printline=printline + " + "
      data=data + " = coordinates" 
      printline=printline + ")\n"
      if debug == "y": App.Console.PrintMessage(data + "\n")
      if debug == "y": App.Console.PrintMessage(printline + "\n")
      # X1,Y1,Z1,X2,Y2,Z2,X3,Y3,Z3,X4,Y4,Z4 = coordinates
      exec(data) # coordinates to variables
      if debug == "y": exec(printline) # output input file
      #App.Console.PrintMessage(str(X1) + " " + str(Y1) + " " +str(Z1) + "\n")
      px=""
      pn="" # names of generated variables
      for x in range(1, num_tupel +1):
       if x < num_tupel:
        pn=pn + "p" + str(x) + ","
       else:
        pn=pn + "p" + str(x)
       data = "Z" + str(x) + " = " + str(i * step)  # Korrektur z= 0.0 auf aktuelle step
       if debug == "y": App.Console.PrintMessage(data + "\n")
       exec(data)
       px="p" + str(x) + "= FreeCAD.Vector(float(X" + str(x) + "),float(Y" + str(x) + "),float(Z" + str(x) + "))" 
       if debug == "y": App.Console.PrintMessage(px + "\n")
       exec(px)
      if debug == "y": App.Console.PrintMessage(pn + "\n")
      #p1 = FreeCAD.Vector(float(X1),float(Y1),float(Z1))
      #p2 = FreeCAD.Vector(float(X2),float(Y2),float(Z2))
      #p3 = FreeCAD.Vector(float(X3),float(Y3),float(Z3))
      #p4 = FreeCAD.Vector(float(X4),float(Y4),float(Z4))
      data="Draft.makeWire([" + pn + "],closed=True)"
      if debug == "y": App.Console.PrintMessage(data + "\n")
      exec(data)
      #Draft.makeWire([p1,p2,p3,p4,p5],closed=True)
      if left_right == "r": 
       i = i + 1
      else:
       i = i -1
    line = file.readline() 
file.close()
#
# List all objects of the document
names = objnames()    # list objectnames
App.Console.PrintMessage("names="+str(names) +"\n")
#extrude
extr="" # suffix for continues Extrude in commands
extrnames="Box Cut" #names of source object, because not consitend nameings in freecad
j=len(names.split())
n=0 #counter
if left_right == "r": 
 l1 = 0
 l2 = j
 step = 1
else:
 l1 = j
 l2 = -1
 step = -1
for x in range(l1, l2, step):
 w=str(names.split(" ")[x])
 if w[0:5] == "DWire":
  if debug == 'y':  App.Console.PrintMessage("w="+str(w) +"\n")
  data = 'f = FreeCAD.getDocument(docname).addObject("Part::Extrusion","Extrude' + str(extr)+ '")'
  if debug == "y": App.Console.PrintMessage(data + "\n")
  exec(data)
  data = 'f = App.getDocument(docname).getObject("Extrude' + str(extr) + '")'
  if debug == "y": App.Console.PrintMessage(data + "\n")
  exec(data)
  data = 'f.Base = App.getDocument(docname).getObject("' + str(w) + '")'
  if debug == "y": App.Console.PrintMessage(data + "\n")
  exec(data)
  data = 'f.DirMode = str("Custom")'
  if debug == "y": App.Console.PrintMessage(data + "\n")
  exec(data)
  data = 'f.Dir = App.Vector(0.000000000000000, 0.000000000000000, 1.000000000000000)'
  if debug == "y": App.Console.PrintMessage(data + "\n")
  exec(data)
  data = 'f.DirLink = None'
  if debug == "y": App.Console.PrintMessage(data + "\n")
  exec(data)
  data = 'f.LengthFwd = 180.000000000000000'
  if debug == "y": App.Console.PrintMessage(data + "\n")
  exec(data)
  data = 'f.LengthRev = 0.000000000000000'
  if debug == "y": App.Console.PrintMessage(data + "\n")
  exec(data)
  data = 'f.Solid = True'
  if debug == "y": App.Console.PrintMessage(data + "\n")
  exec(data)
  data = 'f.Reversed = False'
  if debug == "y": App.Console.PrintMessage(data + "\n")
  exec(data)
  data = 'f.Symmetric = False'
  if debug == "y": App.Console.PrintMessage(data + "\n")
  exec(data)
  data = 'f.TaperAngle = 0.000000000000000'
  if debug == "y": App.Console.PrintMessage(data + "\n")
  exec(data)
  data = 'f.TaperAngleRev = 0.000000000000000'
  if debug == "y": App.Console.PrintMessage(data + "\n")
  exec(data)
 # data = 'App.getDocument(docname).Extrude' + str(extr) + '.Placement=App.Placement(App.Vector(0,0,360), #App.Rotation(App.Vector(0,0,1),0), App.Vector(0,0,0))'
  #if debug == "y": App.Console.PrintMessage(data + "\n")
  #exec(data)
  n = n + 1
  extr = str("%03d" % n)  # count extrude suffix
  extrnames=extrnames + " Extrude" + str("%03d" % x)
#
FreeCAD.ActiveDocument.recompute()
</nowiki>
}}

## Data (stairs.dat) 

Sauvez les données dans un fichier nommé **stairs.dat** dans votre répertoire de macros

    #
    # Save this Data as file stairs.dat in your macro directory
    # 
    # Stufe 0
    0.0 -240.0 0.0 0.0 0.0 0.0 1000.0 0.0 0.0 1000.0 -240.0 0.0
    # Stufe 1
    0.0 0.0 0.0 0.0 240.0 0.0 1000.0 240.0 0.0 1000.0 0.0 0.0
    # Stufe 2
    0.0 240.0 0.0 0.0 520.0 0.0 1000.0 520.0 0.0 1000.0 240.0 0.0
    # Stufe 3
    0.0 520.0 0.0 0.0 840.0 0.0 1000.0 720.0 0.0 1000.0 520.0 0.0
    # Stufe 4
    0.0 840.0 0.0 0.0 1220.0 0.0 1000.0 860.0 0.0 1000.0 720.0 0.0
    # Stufe 5
    0.0 1220.0 0.0 0.0 1620.0 0.0 1000.0 1000.0 0.0 1000.0 860.0 0.0
    # Stufe 6
    0.0 1620.0 0.0 0.0 2170.0 0.0  140.0 2170.0 0.0 1000.0 1120.0 0.0 1000.0 1000.0 0.0
    # Stufe 7
    140.0 2170.0 0.0 680.0 2170.0 0.0 1020.0 1170.0 0.0 1000.0 1170.0 0.0 1000.0 1120.0 0.0 140.0 2170.0 0.0
    # Stufe 8
    680.0 2170.0 0.0 1115.0 2170.0 0.0 1115.0 1170.0 0.0 1020.0 1170.0 0.0 
    # Stufe 9
    1115.0 2170.0 0.0 1550.0 2170.0 0.0 1210.0 1170.0 0.0 1115.0  1170.0 0.0 1115.0 2170.0 0.0
    # Stufe 10
    1550.0 2170.0 0.0 2090.0 2170.0 0.0 1230.0 1120.0 0.0 1230.0 1170.0 0.0 1210.0 1170.0 0.0 1550.0 2170.0 0.0
    # Stufe 11
    2090.0 2170.0 0.0 2230.0 2170.0 0.0 2230.0 1620.0 0.0 1230.0 1000.0 0.0 1230.0 1120.0 0.0 2090.0 2170.0 0.0
    # Stufe 12
    1230.0 1000.0 0.0 2230.0 1620.0 0.0 2230.0 1230.0 0.0 1230.0 860.0 0.0 1230.0 1000.0 0.0
    # Stufe 13
    1230.0 720.0 0.0 1230.0 860.0 0.0 2230.0 1220.0 0.0 2230.0 840.0 0.0 1230.0 720.0 0.0
    # Stufe 14
    1230.0 520.0 0.0 1230.0 720.0 0.0 2230.0 840.0 0.0 2230.0 520.0 0.0 1230.0 520.0 0.0
    # Stufe 15
    1230.0 240.0 0.0 1230.0 520.0 0.0 2230 520.0 0.0 2230.0 240.0 0.0 1230.0 240.0 0.0
    # Stufe 16
    1230.0 0.0 0.0 1230.0 240.0 0.0 2230.0 240.0 0.0 2230.0 0.0 0.0 1230.0 0.0 0.0
    # Stufe 17
    1230.0 -240.0 0.0 1230.0 0.0 0.0 2230.0 0.0 0.0 2230.0 -240.0 0.0 1230.0 -240.0 0.0

### Liens

-   [Macro\_PartsLibrary](Macro_PartsLibrary.md) FreeCAD Library




