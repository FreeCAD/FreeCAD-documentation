# Defeaturing/fr
## Introduction

La suppression de fonctions de modèles 3D a été ajoutée à [Open CASCADE 7.3](https://dev.opencascade.org/index.php?q=node/1211) et peut être utilisée pour modifier des modèles STEP en supprimant des fonctions du modèle.

Il est également possible de l\'utiliser pour la modélisation directe, lorsque l\'historique des opérations n\'est pas disponible. (C\'est le cas pour les modèles 3D STEP). La suppression de fonctions peut également être utile pour supprimer les informations propriétaires du modèle avant de le partager.

Le moyen le plus simple de supprimer des fonctions est d'utiliser l\'[atelier Defeaturing](Defeaturing_Workbench/fr.md).



## Extrait de code 

La suppression de fonctions peut également être utilisé avec Python :


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
*Forme Box3 utilisée dans le code Python, avant la suppression d'une fonction*

<img alt="" src=images/box4.PNG  style="width:200px;"> 
*Forme Box4 utilisée dans le code Python, après la suppression de la fonction*



---
⏵ [documentation index](../README.md) > [Addons](Category_Addons.md) > [External Workbenches](Category_External%20Workbenches.md) > Defeaturing/fr
