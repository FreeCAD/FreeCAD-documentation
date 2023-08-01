# Robot API example/de
## Einleitung

Dieses Beispiel basiert auf dem [RobotExample.py](https://github.com/FreeCAD/FreeCAD_sf_master/blob/master/src/Mod/Robot/RobotExample.py) Beispiel.

Du kannst diese Datei direkt verwenden, wenn Du möchtest.

Beispiel für die Verwendung der Basis Roboterklasse Robot6Axis, die einen 6-achsigen Industrieroboter darstellt. Das Modul Robot ist abhängig von Part, aber nicht von anderen Modulen. Es arbeitet hauptsächlich mit den Grundtypen Placement, Vector und Matrix. Wir brauchen also nur: 
```python
from Robot import *
from Part import *
from FreeCAD import *
```

### Grundlegendes zum Roboter 

Erstelle den Roboter. Wenn du keine andere Kinematik angibst, wird daraus ein Puma 560 
```python
rob = Robot6Axis()
print rob
```

Zugriff auf die Achse und den TCP. Die Achsen gehen von 1-6 und sind in Grad angegeben: 
```python
Start = rob.Tcp
print Start
print rob.Axis1
```

bewege die erste Achse des Roboters: 
```python
rob.Axis1 = 5.0
```

der TCP hat sich geändert (Vorwärtskinematik) 
```python
print rob.Tcp
```

bewege den Roboter zurück in die Startposition (umgekehrte Kinematik): 
```python
rob.Tcp = Start
print rob.Axis1
```

das gleiche mit Achse 2: 
```python
rob.Axis2 = 5.0
print rob.Tcp
rob.Tcp = Start
print rob.Axis2
```

Wegpunkte: 
```python
w = Waypoint(Placement(),name="Pt",type="LIN")
print w.Name,w.Type,w.Pos,w.Cont,w.Velocity,w.Base,w.Tool
```

erzeuge mehr. Die Trajektorie findet immer automatisch einen eindeutigen Namen für die Wegpunkte 
```python
l = [w]
for i in range(5):
  l.append(Waypoint(Placement(Vector(0,0,i*100),Vector(1,0,0),0),"LIN","Pt"))
```

erstelle eine Trajektorie 
```python
t = Trajectory(l)
print t
for i in range(7):
  t.insertWaypoints(Waypoint(Placement(Vector(0,0,i*100+500),Vector(1,0,0),0),"LIN","Pt"))
```

siehe eine Liste aller Wegpunkte: 
```python
print t.Waypoints
 
del rob,Start,t,l,w
```

### Arbeiten mit den Dokument Objekten 

Arbeiten mit den Roboter Dokumentenobjekten: Erstelle zunächst einen Roboter im aktiven Dokument 
```python
if(App.activeDocument() == None):App.newDocument()
 
App.activeDocument().addObject("Robot::RobotObject","Robot")
```

Definiere die visuelle Darstellung und die Kinematikdefinition (siehe [Roboter 6-Achse](Robot_6-Axis/de.md) und [VRML Vorbereitung für Robotersimulation](VRML_Preparation_for_Robot_Simulation/de.md) für Details dazu) 
```python
App.activeDocument().Robot.RobotVrmlFile = App.getResourceDir()+"Mod/Robot/Lib/Kuka/kr500_1.wrl"
App.activeDocument().Robot.RobotKinematicFile = App.getResourceDir()+"Mod/Robot/Lib/Kuka/kr500_1.csv"
```

Startposition der Achse (nur die, die von 0 abweichen) 
```python
App.activeDocument().Robot.Axis2 = -90
App.activeDocument().Robot.Axis3 = 90
```

Abrufen der TCP Position 
```python
pos = FreeCAD.getDocument("Unnamed").getObject("Robot").Tcp
```

bewege den Roboter 
```python
pos.move(App.Vector(-10,0,0))
FreeCAD.getDocument("Unnamed").getObject("Robot").Tcp = pos
```

ein leeres Trajektorienobjekt im aktiven Dokument erzeugen 
```python
App.activeDocument().addObject("Robot::TrajectoryObject","Trajectory")
```

die Trajektorie erhalten 
```python
t = App.activeDocument().Trajectory.Trajectory
```

die aktuelle TCP Position des Roboters zur Trajektorie hinzufügen 
```python
StartTcp = App.activeDocument().Robot.Tcp
t.insertWaypoints(StartTcp)
App.activeDocument().Trajectory.Trajectory = t
print App.activeDocument().Trajectory.Trajectory
```

Füge weitere Wegpunkte und den Startpunkt am Ende wieder ein: 
```python
for i in range(7):
  t.insertWaypoints(Waypoint(Placement(Vector(0,1000,i*100+500),Vector(1,0,0),i),"LIN","Pt"))

t.insertWaypoints(StartTcp) # end point of the trajectory
App.activeDocument().Trajectory.Trajectory = t
print App.activeDocument().Trajectory.Trajectory
```

### Simulation

Zu erledigen\.....

### Exportieren der Trajektorie 

Die Trajektorie wird mit Python exportiert. Das heißt, für jeden Schaltschranktyp gibt es ein Postprozessor Python Modul. Hier ist der Kuka Postprozessor im Detail beschrieben 
```python
from KukaExporter import ExportCompactSub

ExportCompactSub(App.activeDocument().Robot,App.activeDocument().Trajectory,'D:/Temp/TestOut.src')
```

und so wird es auch gemacht: 
```python
for w in App.activeDocument().Trajectory.Trajectory.Waypoints:
    (A,B,C) = (w.Pos.Rotation.toEuler())
    print ("LIN {X %.3f,Y %.3f,Z %.3f,A %.3f,B %.3f,C %.3f} ; %s"%(w.Pos.Base.x,w.Pos.Base.y,w.Pos.Base.z,A,B,C,w.Name))

```


{{Robot Tools navi

}}



---
![](images/Button_right.svg) [documentation index](../README.md) > [API](Category_API.md) > [Robot](Robot_Workbench.md) > Robot API example/de
