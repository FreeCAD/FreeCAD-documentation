# Robot API example/pt-br
## Introduction

This example is based on the [RobotExample.py](https://github.com/FreeCAD/FreeCAD_sf_master/blob/master/src/Mod/Robot/RobotExample.py) example.

You may use this file directly if you want.

Example how to use the basic robot class Robot6Axis which represents a 6-axis industrial robot. The Robot module is dependent on Part but not on other modules. It works mostly with the basic types Placement, Vector and Matrix. So we need only: 
```python
from Robot import *
from Part import *
from FreeCAD import *
```

### Basic robot stuff 

create the robot. If you do not specify another kinematic it becomes a Puma 560 
```python
rob = Robot6Axis()
print rob
```

accessing the axis and the TCP. Axes go from 1-6 and are in degree: 
```python
Start = rob.Tcp
print Start
print rob.Axis1
```

move the first axis of the robot: 
```python
rob.Axis1 = 5.0
```

the TCP has changed (forward kinematic) 
```python
print rob.Tcp
```

move the robot back to start position (reverse kinematic): 
```python
rob.Tcp = Start
print rob.Axis1
```

the same with axis 2: 
```python
rob.Axis2 = 5.0
print rob.Tcp
rob.Tcp = Start
print rob.Axis2
```

Waypoints: 
```python
w = Waypoint(Placement(),name="Pt",type="LIN")
print w.Name,w.Type,w.Pos,w.Cont,w.Velocity,w.Base,w.Tool
```

generate more. The trajectory always finds automatically a unique name for the waypoints 
```python
l = [w]
for i in range(5):
  l.append(Waypoint(Placement(Vector(0,0,i*100),Vector(1,0,0),0),"LIN","Pt"))
```

create a trajectory 
```python
t = Trajectory(l)
print t
for i in range(7):
  t.insertWaypoints(Waypoint(Placement(Vector(0,0,i*100+500),Vector(1,0,0),0),"LIN","Pt"))
```

see a list of all waypoints: 
```python
print t.Waypoints
 
del rob,Start,t,l,w
```

### Working with the document objects 

Working with the robot document objects: first create a robot in the active document 
```python
if(App.activeDocument() == None):App.newDocument()
 
App.activeDocument().addObject("Robot::RobotObject","Robot")
```

Define the visual representation and the kinematic definition (see [Robot 6-Axis](Robot_6-Axis.md) and [VRML Preparation for Robot Simulation](VRML_Preparation_for_Robot_Simulation.md) for details about that) 
```python
App.activeDocument().Robot.RobotVrmlFile = App.getResourceDir()+"Mod/Robot/Lib/Kuka/kr500_1.wrl"
App.activeDocument().Robot.RobotKinematicFile = App.getResourceDir()+"Mod/Robot/Lib/Kuka/kr500_1.csv"
```

start positon of the Axis (only that which differ from 0) 
```python
App.activeDocument().Robot.Axis2 = -90
App.activeDocument().Robot.Axis3 = 90
```

retrieve the TCP position 
```python
pos = FreeCAD.getDocument("Unnamed").getObject("Robot").Tcp
```

move the robot 
```python
pos.move(App.Vector(-10,0,0))
FreeCAD.getDocument("Unnamed").getObject("Robot").Tcp = pos
```

create an empty Trajectory object in the active document 
```python
App.activeDocument().addObject("Robot::TrajectoryObject","Trajectory")
```

get the Trajectory 
```python
t = App.activeDocument().Trajectory.Trajectory
```

add the actual TCP position of the robot to the trajectory 
```python
StartTcp = App.activeDocument().Robot.Tcp
t.insertWaypoints(StartTcp)
App.activeDocument().Trajectory.Trajectory = t
print App.activeDocument().Trajectory.Trajectory
```

insert some more Waypoints and the start point at the end again: 
```python
for i in range(7):
  t.insertWaypoints(Waypoint(Placement(Vector(0,1000,i*100+500),Vector(1,0,0),i),"LIN","Pt"))

t.insertWaypoints(StartTcp) # end point of the trajectory
App.activeDocument().Trajectory.Trajectory = t
print App.activeDocument().Trajectory.Trajectory
```

### Simulation

To be done\.....

### Exporting the trajectory 

The trajectory is exported by Python. That means for every control cabinet type there is a post-processor Python module. Here is in detail the Kuka post-processor described 
```python
from KukaExporter import ExportCompactSub

ExportCompactSub(App.activeDocument().Robot,App.activeDocument().Trajectory,'D:/Temp/TestOut.src')
```

and that\'s kind of how it\'s done: 
```python
for w in App.activeDocument().Trajectory.Trajectory.Waypoints:
    (A,B,C) = (w.Pos.Rotation.toEuler())
    print ("LIN {X %.3f,Y %.3f,Z %.3f,A %.3f,B %.3f,C %.3f} ; %s"%(w.Pos.Base.x,w.Pos.Base.y,w.Pos.Base.z,A,B,C,w.Name))

```


{{Robot Tools navi}}




_

---
[documentation index](../README.md) > [Robot API](Category_Robot API.md) > [Robot](Robot_Workbench.md) > Robot API example/pt-br
