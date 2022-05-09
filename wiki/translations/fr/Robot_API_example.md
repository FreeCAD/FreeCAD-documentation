# Robot API example/fr
## Introduction

Cet exemple est basé sur l\'exemple [RobotExample.py](https   *//github.com/FreeCAD/FreeCAD_sf_master/blob/master/src/Mod/Robot/RobotExample.py).

Tu peux utiliser ce fichier directement si tu veux.

Exemple d\'utilisation de la classe de robot de base Robot6Axis qui représente un robot industriel à 6 axes. Le module Robot dépend de Part mais pas d\'autres modules. Il fonctionne principalement avec les types de base Placement, Vecteur et Matrice. Nous n\'avons donc besoin que de    * 
```python
from Robot import *
from Part import *
from FreeCAD import *
```

### Trucs de base robot 

créer le robot. Si tu ne spécifies pas une autre cinématique, il devient un Puma 560 
```python
rob = Robot6Axis()
print rob
```

accéder à l\'axe et au TCP. Les axes vont de 1 à 6 et sont en degrés    * 
```python
Start = rob.Tcp
print Start
print rob.Axis1
```

déplacer le premier axe du robot    * 
```python
rob.Axis1 = 5.0
```

le TCP a changé (cinématique avant) 
```python
print rob.Tcp
```

déplacer le robot en position de départ (cinématique inverse)    * 
```python
rob.Tcp = Start
print rob.Axis1
```

de même pour l\'axe 2    * 
```python
rob.Axis2 = 5.0
print rob.Tcp
rob.Tcp = Start
print rob.Axis2
```

Pointspassage    * 
```python
w = Waypoint(Placement(),name="Pt",type="LIN")
print w.Name,w.Type,w.Pos,w.Cont,w.Velocity,w.Base,w.Tool
```

générer plus. La trajectoire trouve toujours automatiquement un nom unique pour les pointspassage. 
```python
l = [w]
for i in range(5)   *
  l.append(Waypoint(Placement(Vector(0,0,i*100),Vector(1,0,0),0),"LIN","Pt"))
```

créer une trajectoire 
```python
t = Trajectory(l)
print t
for i in range(7)   *
  t.insertWaypoints(Waypoint(Placement(Vector(0,0,i*100+500),Vector(1,0,0),0),"LIN","Pt"))
```

voir une liste de tous les pointspassage    * 
```python
print t.Waypoints
 
del rob,Start,t,l,w
```

### Travailler avec les objets du document 

Travailler avec les objets document robot   * créer en premier un robot dans le document actif 
```python
if(App.activeDocument() == None)   *App.newDocument()
 
App.activeDocument().addObject("Robot   *   *RobotObject","Robot")
```

Définir la représentation visuelle et la définition cinématique (voir [Robot 6-Axes](Robot_6-Axis/fr.md) et [Préparation VRML pour la simulation de robot](VRML_Preparation_for_Robot_Simulation/fr.md) pour plus de détails à ce sujet) 
```python
App.activeDocument().Robot.RobotVrmlFile = App.getResourceDir()+"Mod/Robot/Lib/Kuka/kr500_1.wrl"
App.activeDocument().Robot.RobotKinematicFile = App.getResourceDir()+"Mod/Robot/Lib/Kuka/kr500_1.csv"
```

position de départ de l\'axe (uniquement celle qui diffère de 0) 
```python
App.activeDocument().Robot.Axis2 = -90
App.activeDocument().Robot.Axis3 = 90
```

récupère la position TCP 
```python
pos = FreeCAD.getDocument("Unnamed").getObject("Robot").Tcp
```

déplacer le robot 
```python
pos.move(App.Vector(-10,0,0))
FreeCAD.getDocument("Unnamed").getObject("Robot").Tcp = pos
```

créer un objet Trajectoire vide dans le document actif 
```python
App.activeDocument().addObject("Robot   *   *TrajectoryObject","Trajectory")
```

obtenir la trajectoire 
```python
t = App.activeDocument().Trajectory.Trajectory
```

ajouter la position TCP réelle du robot à la trajectoire 
```python
StartTcp = App.activeDocument().Robot.Tcp
t.insertWaypoints(StartTcp)
App.activeDocument().Trajectory.Trajectory = t
print App.activeDocument().Trajectory.Trajectory
```

insérer d\'autres pointspassage et remettre le point de départ à la fin    * 
```python
for i in range(7)   *
  t.insertWaypoints(Waypoint(Placement(Vector(0,1000,i*100+500),Vector(1,0,0),i),"LIN","Pt"))

t.insertWaypoints(StartTcp) # end point of the trajectory
App.activeDocument().Trajectory.Trajectory = t
print App.activeDocument().Trajectory.Trajectory
```

### Simulation

A faire\.....

### Exportation de la trajectoire 

La trajectoire est exportée par Python. Cela veut dire que pour chaque type d\'armoire de commande, il existe un post-processeur module Python. Voici en détail la description du post-processeur de Kuka 
```python
from KukaExporter import ExportCompactSub

ExportCompactSub(App.activeDocument().Robot,App.activeDocument().Trajectory,'D   */Temp/TestOut.src')
```

et c\'est ainsi que ça se fait    * 
```python
for w in App.activeDocument().Trajectory.Trajectory.Waypoints   *
    (A,B,C) = (w.Pos.Rotation.toEuler())
    print ("LIN {X %.3f,Y %.3f,Z %.3f,A %.3f,B %.3f,C %.3f} ; %s"%(w.Pos.Base.x,w.Pos.Base.y,w.Pos.Base.z,A,B,C,w.Name))

```


{{Robot Tools navi

}} 

[Category   *API](Category_API.md)



---
![](images/Right_arrow.png) [documentation index](../README.md) > [API](Category_API.md) > [Robot](Robot_Workbench.md) > Robot API example/fr
