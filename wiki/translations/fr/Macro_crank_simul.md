# Macro crank simul/fr
{{Macro/fr
|Name=Crank Simul
|Icon=Macro_crank_simul.png
|Description=Simulation de mouvement d'un vilebrequin.
|Author=kwahoo
|Version=1.0
|Date=2014-06-13
|FCVersion=All
|Download= [https   *//www.freecadweb.org/wiki/images/0/04/Macro_crank_simul.png ToolBar Icon]<br />The file [http   *//forum.freecadweb.org/download/file.php?id=5954 crank_simul.fcstd]
}}

## Description

Cette animation simple utilise une esquisse et le solveur afin de déterminer la position et la rotation du piston et de la bielle.

![](images/Crank_00.gif )

## Utilisation

Pour tester l\'animation    *

Télécharger les fichiers et copier le code dans la console Python de FreeCAD.

1\. Ouvrir le fichier joint

Pour stopper l\'animation, taper dans la console    * \"**animation.stop()**\"

## Le fichier 

[crank\_simul.fcstd](http   *//forum.freecadweb.org/download/file.php?id=5954)

## Script

ToolBar Icon ![](images/Macro_crank_simul.png )

**crank\_simul.FCMacro**


{{MacroCode|code=
import FreeCAD as App, FreeCADGui as Gui, Part, time, sys, math, Draft, DraftGeomUtils
from PySide import QtGui,QtCore

class Animation(object)   *
    def __init__(self)   *
        App.Console.PrintMessage('init')

        App.ActiveDocument.recompute()

        self.timer = QtCore.QTimer()
        QtCore.QObject.connect(self.timer, QtCore.SIGNAL("timeout()"), self.my_update)
        self.timer.start(50)

        self.an = 0.1

    def my_update(self)   *
        string = '{0}'.format(self.an)
        self.an = self.an + 0.01 if self.an < (2 * math.pi) else 0.0

        angle = math.degrees(self.an)
        App.ActiveDocument.Sketch.setDatum(5,App.Units.Quantity(str(angle)+' deg'))
        App.ActiveDocument.recompute()
        p1 = App.ActiveDocument.Sketch.Shape.Vertexes[0].Point
        p2 = App.ActiveDocument.Sketch.Shape.Vertexes[1].Point
        conrodangle = math.degrees(Draft.DraftVecUtils.angle(App.Vector(1,0,0),(p1-p2))) - 90
        App.ActiveDocument.getObject("Cylinder").Placement = App.Placement(p1,App.Rotation(App.Vector(1,0,0),-90))
        App.ActiveDocument.getObject("Sketch001").Placement = App.Placement(p1,App.Rotation(App.Vector(0,0,1),conrodangle))

    def stop(self)   *
        self.timer.stop()
         

animation = Animation()

}}

## Liens

La discussion sur le forum (en anglais) [Inline-four engine animation](http   *//forum.freecadweb.org/viewtopic.php?f=24&t=6815&hilit=animation#p55092)

Le blogue [freecad-tutorial.blogspot](http   *//freecad-tutorial.blogspot.be/)



---
![](images/Right_arrow.png) [documentation index](../README.md) > Macro crank simul/fr
