# Defeaturing/it
## Introduzione

La defeaturing del modello 3D è stata aggiunta con Open CASCADE 7.3 [1](https://dev.opencascade.org/index.php?q=node/1211) e può essere utilizzata per la modifica dei modelli STEP rimuovendo le funzioni dal modello.

Permette la rimodellazione anche quando la cronologia delle operazioni non è disponibile. (Questo è il caso dei modelli 3D STEP). La defeaturing può anche essere utile per rimuovere le informazioni proprietarie del modello prima di condividerlo.

Il modo più semplice per usare defeaturing è usare l\'ambiente [Defeaturing](Defeaturing_Workbench/it.md)

## Esempio di codice 

Defeaturing può essere utilizzato anche con Python: 
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
*Forma Box3 usata nel codice Python, prima del defeaturing* <img alt="" src=images/box4.PNG  style="width:200px;"> 
*Forma Box4 usata nel codice Python, dopo il defeaturing*


 

_ _

---
[documentation index](../README.md) > [Addons](Category_Addons.md) > Defeaturing/it
