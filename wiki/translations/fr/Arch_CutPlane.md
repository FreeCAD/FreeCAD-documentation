---
- GuiCommand:/fr
   Name:Arch CutPlane
   Name/fr:Arch Couper selon un plan
   MenuLocation:Arch → Couper selon un plan
   Workbenches:[Arch](Arch_Module/fr.md)
   SeeAlso:[Arch Couper suivant une ligne](Arch_CutLine/fr.md), [Arch Soustraire](Arch_Remove/fr.md)
---


</div>

## Description

L\'outil Couper le plan vous permet de couper un objet Arch selon un plan:

-   Vous pouvez couper un objet Arch avec la face sélectionnée, normale ou opposée au plan de la face.
-   Cela ajoute un composant de soustraction CutVolume à l\'objet Arch

<img alt="" src=images/Arch_CutPlane_example.jpg  style="width:640px;">


*A gauche: avant d'appliquer l'outil Couper suivant un plan. Milieu: mur résultant après la coupe. À droite: encore un autre résultat facultatif*

## Utilisation

1.  Sélectionner l\'objet à couper, puis une face (la face doit être sélectionnée en dernier, et doit être sélectionnée sur la [vue 3D](3D_view/fr.md)).
2.  Appuyer sur le bouton **<img src="images/Arch_CutPlane.svg" width=24px> [Couper un objet selon un plan](Arch_CutPlane/fr.md)**.
3.  Choisissez si l\'objet est coupé **derrière** la face normale ou **devant** de la face normale.
4.  Cliquer sur le bouton **OK**.

## Script


**Voir aussi:**

[Arch API](Arch_API/fr.md) et [FreeCAD Scripts de Base](FreeCAD_Scripting_Basics/fr.md).

L\'outil Couper selon un plan peut être utilisé dans une [macro](macros/fr.md), et, à partir de la console [Python](Python/fr.md) en utilisant la fonction suivante : 
```python
cutObj = cutComponentwithPlane(archObject, cutPlane, sideFace)
```

-   Crée un objet `cutObj` à partir de `archObject` qui est coupé par `cutPlane` lequel est la face d\'un autre objet.
    -   
        `archObject`
        
        doit être un `SelectionObject` obtenu à partir de `FreeCADGui.Selection.SelectionEx()[0]`.

    -   
        `cutPlane`
        
        doit être un `FaceObject` obtenu à partir de `FreeCADGui.Selection.SelectionEx()[0].SubObjects[0]`.

-    `sideFace`indique de quel côté de `FaceObject` un volume sera créé; ce volume sera ensuite utilisé pour être soustrait de `archObject`. Si `sideFace` vaut `0`, cela créera un volume à l\'arrière de la face, sinon il le créera devant la face.

Exemple: 
```python
import FreeCAD, FreeCADGui, Draft, Arch

p1 = FreeCAD.Vector(0, 0, 0)
p2 = FreeCAD.Vector(2000, 2000, 0)

Line = Draft.makeWire([p1, p2])
Wall = Arch.makeWall(Line, width=150, height=2000)

p3 = FreeCAD.Vector(0, 2000, 0)
p4 = FreeCAD.Vector(3000, 0, 0)

Line2 = Draft.makeWire([p3, p4])
Wall2 = Arch.makeWall(Line2, width=150, height=2000)
FreeCAD.ActiveDocument.recompute()

# Select the Wall
main_object = FreeCADGui.Selection.getSelectionEx()[0]

# Select the face of Wall2
selection = FreeCADGui.Selection.getSelectionEx()[0]
cut_face = selection.SubObjects[0]

cutObj = Arch.cutComponentwithPlane(main_object, cut_face, 0)
FreeCAD.ActiveDocument.recompute()

Wall3 = Draft.move(Wall, FreeCAD.Vector(-4000, 0, 0), copy=True)
Wall4 = Draft.move(Wall2, FreeCAD.Vector(-4000, 0, 0), copy=True)
FreeCAD.ActiveDocument.recompute()

# Select the Wall3
main_object2 = FreeCADGui.Selection.getSelectionEx()[0]

# Select the face of Wall4
selection2 = FreeCADGui.Selection.getSelectionEx()[0]
cut_face2 = selection2.SubObjects[0]

cutObj2 = Arch.cutComponentwithPlane(main_object2, cut_face2, 1)
FreeCAD.ActiveDocument.recompute()
```


<div class="mw-translate-fuzzy">





</div>


 
