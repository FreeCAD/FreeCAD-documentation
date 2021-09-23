# Robot API example/es
## Introducción

Este ejemplo está basado en el ejemplo [RobotExample.py](https://github.com/FreeCAD/FreeCAD_sf_master/blob/master/src/Mod/Robot/RobotExample.py).

Puede utilizar este archivo directamente si lo desea.

Ejemplo de cómo utilizar la clase de robot básica Robot6Axis que representa un robot industrial de 6 ejes. El módulo Robot depende de Pieza pero no de otros módulos. Funciona principalmente con los tipos básicos Colocación, Vector y Matrix. Así que sólo necesitamos: 
```python
from Robot import *
from Part import *
from FreeCAD import *
```

### Cosas básicas del robot 

crea el robot. Si no se especifica otra cinemática se convierte en un Puma 560 
```python
rob = Robot6Axis()
print rob
```

accediendo al eje y al TCP. Los ejes van de 1 a 6 y están en grados: 
```python
Start = rob.Tcp
print Start
print rob.Axis1
```

mueve el primer eje del robot: 
```python
rob.Axis1 = 5.0
```

el TCP ha cambiado (cinemática de avance) 
```python
print rob.Tcp
```

mueve el robot de vuelta a la posición inicial (cinemática inversa): 
```python
rob.Tcp = Start
print rob.Axis1
```

lo mismo con el eje 2: 
```python
rob.Axis2 = 5.0
print rob.Tcp
rob.Tcp = Start
print rob.Axis2
```

Caminopuntos: 
```python
w = Waypoint(Placement(),name="Pt",type="LIN")
print w.Name,w.Type,w.Pos,w.Cont,w.Velocity,w.Base,w.Tool
```

generar más. La trayectoria siempre encuentra automáticamente un nombre único para los caminopuntos 
```python
l = [w]
for i in range(5):
  l.append(Waypoint(Placement(Vector(0,0,i*100),Vector(1,0,0),0),"LIN","Pt"))
```

crear una trayectoria 
```python
t = Trajectory(l)
print t
for i in range(7):
  t.insertWaypoints(Waypoint(Placement(Vector(0,0,i*100+500),Vector(1,0,0),0),"LIN","Pt"))
```

ver una lista de todos los caminopuntos: 
```python
print t.Waypoints
 
del rob,Start,t,l,w
```

### Trabajar con los objetos del documento 

Trabajar con los objetos del documento robot: crear primero un robot en el documento activo 
```python
if(App.activeDocument() == None):App.newDocument()
 
App.activeDocument().addObject("Robot::RobotObject","Robot")
```

Define la representación visual y la definición cinemática (ver [Robot 6-Ejes](Robot_6-Axis/es.md) y [Preparación de VRML para la simulación de robots](VRML_Preparation_for_Robot_Simulation/es.md) para más detalles) 
```python
App.activeDocument().Robot.RobotVrmlFile = App.getResourceDir()+"Mod/Robot/Lib/Kuka/kr500_1.wrl"
App.activeDocument().Robot.RobotKinematicFile = App.getResourceDir()+"Mod/Robot/Lib/Kuka/kr500_1.csv"
```

posición inicial del Eje (sólo la que difiere de 0) 
```python
App.activeDocument().Robot.Axis2 = -90
App.activeDocument().Robot.Axis3 = 90
```

recuperar la posición TCP 
```python
pos = FreeCAD.getDocument("Unnamed").getObject("Robot").Tcp
```

mueve el robot 
```python
pos.move(App.Vector(-10,0,0))
FreeCAD.getDocument("Unnamed").getObject("Robot").Tcp = pos
```

crear un objeto Trayectoria vacío en el documento activo 
```python
App.activeDocument().addObject("Robot::TrajectoryObject","Trajectory")
```

obtener la Trayectoria 
```python
t = App.activeDocument().Trajectory.Trajectory
```

añadir la posición TCP real del robot a la trayectoria 
```python
StartTcp = App.activeDocument().Robot.Tcp
t.insertWaypoints(StartTcp)
App.activeDocument().Trajectory.Trajectory = t
print App.activeDocument().Trajectory.Trajectory
```

insertar algunos caminopuntos más y el punto de inicio al final de nuevo: 
```python
for i in range(7):
  t.insertWaypoints(Waypoint(Placement(Vector(0,1000,i*100+500),Vector(1,0,0),i),"LIN","Pt"))

t.insertWaypoints(StartTcp) # end point of the trajectory
App.activeDocument().Trajectory.Trajectory = t
print App.activeDocument().Trajectory.Trajectory
```

### Simulación

Por hacer\.....

### Exportar la trayectoria 

La trayectoria es exportada por Python. Eso significa que para cada tipo de armario de control hay un post-procesador módulo de Python. Aquí se describe en detalle el post-procesador Kuka 
```python
from KukaExporter import ExportCompactSub

ExportCompactSub(App.activeDocument().Robot,App.activeDocument().Trajectory,'D:/Temp/TestOut.src')
```

y así es como se hace: 
```python
for w in App.activeDocument().Trajectory.Trajectory.Waypoints:
    (A,B,C) = (w.Pos.Rotation.toEuler())
    print ("LIN {X %.3f,Y %.3f,Z %.3f,A %.3f,B %.3f,C %.3f} ; %s"%(w.Pos.Base.x,w.Pos.Base.y,w.Pos.Base.z,A,B,C,w.Name))

```


{{Robot Tools navi/es}}


{{Userdocnavi/es}}

[Category:Robot API](Category:Robot_API.md)

---
[documentation index](../README.md) > [Robot](Robot_Workbench.md) > Robot API example/es
