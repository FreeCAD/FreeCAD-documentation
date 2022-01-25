# Defeaturing/de
## Einführung

3D Modell Vereinfachung wurde mit Open CASCADE 7.3 [1](https://dev.opencascade.org/index.php?q=node/1211) hinzugefügt und kann zur Bearbeitung von STEP Modellen verwendet werden, indem die Formelemente aus dem Modell entfernt werden.

Es ist auch möglich, das Modell direkt zu modellieren, wenn die Historie der Operationen nicht verfügbar ist. (Dies ist der Fall bei 3D STEP Modellen). Das Defeaturing kann auch nützlich sein, um proprietäre Details des Modells zu entfernen, bevor es freigegeben wird.

Der einfachste Weg, das Defeaturing zu verwenden, ist die Verwendung des [Defeaturing Arbeitsbereichs](Defeaturing_Workbench/de.md)

## Code Schnipsel 

Defeaturing kann auch mit Python verwendet werden: 
```python
box = Part.makeBox(10,10,10)
box2 = Part.makeBox(5,5,5,FreeCAD.Vector(5,5,0))
box3 = box.cut(box2)
Part.show(box3)
faces = App.ActiveDocument.ActiveObject.Shape.Faces[6:] #the faces of box3 that are part of the corner pocket
box4 = App.ActiveDocument.ActiveObject.Shape.defeaturing(faces) #defeature the shape
Part.show(box4) #show defeatured shape
```

<img alt="" src=images/box3.PNG  style="width:200px;"> 
*Box3 Form in Python Code verwendet, vor der defeaturing.* <img alt="" src=images/box4.PNG  style="width:200px;"> 
*Box4 Form in Python Code verwendet, defeatured*



---
![](images/Right_arrow.png) [documentation index](../README.md) > [Addons](Category_Addons.md) > [External Workbenches](Category_External Workbenches.md) > Defeaturing/de
