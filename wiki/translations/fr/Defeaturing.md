

## Introduction

La déconstruction de Modèles 3D a été ajouté à Open CASCADE 7.3 [1](https://dev.opencascade.org/index.php?q=node/1211) et peut être utilisé pour éditer des modèles STEP en supprimant des éléments du modèle.

Il permet également de modéliser directement le modèle lorsque l\'historique des opérations n\'est pas disponible. (C\'est le cas pour les modèles 3D STEP). Defeaturing peut également être utile pour supprimer les informations propriétaires du modèle avant de le partager.

Le moyen le plus simple d'utiliser Defeaturing est d'utiliser [l\'atelier Defeaturing](Defeaturing_Workbench/fr.md).

## Extrait de code {#extrait_de_code}

Defeaturing peut également être utilisé avec Python : 
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
*Forme Box3 utilisée dans le code python, avant d'être déconstruite* <img alt="" src=images/box4.PNG  style="width:200px;"> *Forme Box4 utilisée dans le code python, déconstruite*


 

[Category:Addons{{\#translation:}}](Category:Addons.md) [Category:External Workbenches{{\#translation:}}](Category:External_Workbenches.md)
