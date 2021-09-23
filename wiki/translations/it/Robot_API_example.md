# Robot API example/it
## Introduzione

Questo esempio è basato sull\'esempio [RobotExample.py](https://github.com/FreeCAD/FreeCAD_sf_master/blob/master/src/Mod/Robot/RobotExample.py).

È possibile usare direttamente questo file se si vuole.

Esempio di come utilizzare la classe robot di base Robot6Axis che rappresenta un robot industriale a 6 assi. Il modulo Robot dipende da Part ma non da altri moduli. Funziona principalmente con i tipi base Placement, Vector e Matrix. Quindi abbiamo bisogno solo di: 
```python
from Robot import *
from Part import *
from FreeCAD import *
```

### Roba di base per i robot 

creare il robot. Se non si specifica un\'altra cinematica diventa un Puma 560 
```python
rob = Robot6Axis()
print rob
```


<div class="mw-translate-fuzzy">

accedere all\'asse e alla TCP. Gli assi vanno da 1 a 6 e sono in gradi:


</div>


```python
Start = rob.Tcp
print Start
print rob.Axis1
```

spostare il primo asse del robot: 
```python
rob.Axis1 = 5.0
```


<div class="mw-translate-fuzzy">

il TCP è cambiato (cinematica in avanzamento)


</div>


```python
print rob.Tcp
```

muovere il robot in posizione di partenza (cinematica inversa): 
```python
rob.Tcp = Start
print rob.Axis1
```

lo stesso con l\'asse 2: 
```python
rob.Axis2 = 5.0
print rob.Tcp
rob.Tcp = Start
print rob.Axis2
```

Viapunti: 
```python
w = Waypoint(Placement(),name="Pt",type="LIN")
print w.Name,w.Type,w.Pos,w.Cont,w.Velocity,w.Base,w.Tool
```

generare di più. La traiettoria trova sempre automaticamente un nome unico per i viapunti 
```python
l = [w]
for i in range(5):
  l.append(Waypoint(Placement(Vector(0,0,i*100),Vector(1,0,0),0),"LIN","Pt"))
```

creare una traiettoria 
```python
t = Trajectory(l)
print t
for i in range(7):
  t.insertWaypoints(Waypoint(Placement(Vector(0,0,i*100+500),Vector(1,0,0),0),"LIN","Pt"))
```

vedere un elenco di tutti i viapunti: 
```python
print t.Waypoints
 
del rob,Start,t,l,w
```

### Lavorare con gli oggetti del documento 

Lavorare con gli oggetti del documento robot: creare prima un robot nel documento attivo 
```python
if(App.activeDocument() == None):App.newDocument()
 
App.activeDocument().addObject("Robot::RobotObject","Robot")
```

Definire la rappresentazione visiva e la definizione cinematica (vedere [Robot 6-Axis](Robot_6-Axis/it.md) e [Preparazione VRML per la simulazione di robot](VRML_Preparation_for_Robot_Simulation/it.md) per dettagli su questo) 
```python
App.activeDocument().Robot.RobotVrmlFile = App.getResourceDir()+"Mod/Robot/Lib/Kuka/kr500_1.wrl"
App.activeDocument().Robot.RobotKinematicFile = App.getResourceDir()+"Mod/Robot/Lib/Kuka/kr500_1.csv"
```

posizione iniziale dell\'asse (solo quella che differisce da 0) 
```python
App.activeDocument().Robot.Axis2 = -90
App.activeDocument().Robot.Axis3 = 90
```


<div class="mw-translate-fuzzy">

recuperare la posizione TCP


</div>


```python
pos = FreeCAD.getDocument("Unnamed").getObject("Robot").Tcp
```

muovere il robot 
```python
pos.move(App.Vector(-10,0,0))
FreeCAD.getDocument("Unnamed").getObject("Robot").Tcp = pos
```

creare un oggetto Traiettoria vuota nel documento attivo 
```python
App.activeDocument().addObject("Robot::TrajectoryObject","Trajectory")
```

ottenere la traiettoria 
```python
t = App.activeDocument().Trajectory.Trajectory
```

aggiungere la posizione TCP effettiva del robot alla traiettoria 
```python
StartTcp = App.activeDocument().Robot.Tcp
t.insertWaypoints(StartTcp)
App.activeDocument().Trajectory.Trajectory = t
print App.activeDocument().Trajectory.Trajectory
```

inserire altri viapunti e il punto di partenza alla fine di nuovo: 
```python
for i in range(7):
  t.insertWaypoints(Waypoint(Placement(Vector(0,1000,i*100+500),Vector(1,0,0),i),"LIN","Pt"))

t.insertWaypoints(StartTcp) # end point of the trajectory
App.activeDocument().Trajectory.Trajectory = t
print App.activeDocument().Trajectory.Trajectory
```

### Simulazione

Da fare\.....

### Esportare la traiettoria 

La traiettoria è esportata da Python. Ciò significa che per ogni tipo di cabina c\'è un post-processore modulo Python. Qui è descritto in dettaglio il post-processore Kuka 
```python
from KukaExporter import ExportCompactSub

ExportCompactSub(App.activeDocument().Robot,App.activeDocument().Trajectory,'D:/Temp/TestOut.src')
```

ed è più o meno così che si fa: 
```python
for w in App.activeDocument().Trajectory.Trajectory.Waypoints:
    (A,B,C) = (w.Pos.Rotation.toEuler())
    print ("LIN {X %.3f,Y %.3f,Z %.3f,A %.3f,B %.3f,C %.3f} ; %s"%(w.Pos.Base.x,w.Pos.Base.y,w.Pos.Base.z,A,B,C,w.Name))

```


{{Robot Tools navi/it}}


{{Userdocnavi/it}}

[Category:Robot API](Category:Robot_API.md)

---
[documentation index](../README.md) > [Robot](Robot_Workbench.md) > Robot API example/it
