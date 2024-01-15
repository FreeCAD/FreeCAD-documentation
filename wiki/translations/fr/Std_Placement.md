---
 GuiCommand:
   Name: Std Placement
   Name/fr: Std Positionner
   MenuLocation: Édition , Positionner...
‏‎   Workbenches: Tous
   SeeAlso: Std_Alignment/fr, Placement/fr
---

# Std Placement/fr

## Description

La commande **Std Positionner** affiche le [panneau des tâches](Task_Panel/fr.md) Positionner pour un objet sélectionné.

![](images/Std_Placement_taskpanel.png ) 
*Le panneau des tâches Positionner*



## Utilisation

1.  Sélectionnez un seul objet ayant une propriété **Placement** dans l\'[éditeur de propriétés](Property_editor/fr.md).
2.  Sélectionnez l\'option **Édition → Positionner...** du menu.
3.  Modifiez un ou plusieurs paramètres de translation et de rotation.
4.  Effectuez l\'une des actions suivantes :
    -   Appuyez sur le bouton **OK** pour appliquer les modifications et fermer le panneau des tâches.
    -   Appuyez sur le bouton **Appliquer** pour appliquer les modifications mais gardez le panneau des tâches ouvert pour d\'autres modifications.
5.  Appuyez sur **Echap** ou sur le bouton **Annuler** pour abandonner l\'opération. Cela annulera toutes les modifications qui n\'ont pas été appliquées.

La boîte de dialogue peut également être lancée en cliquant sur le bouton de sélection **...** qui apparaît dans l\'[éditeur de propriétés](Property_editor/fr.md) lorsque vous cliquez sur la propriété **Placement**.



## Remarques

-   Pour plus d\'informations sur les paramètres de placement, consultez la page [Placement](Placement/fr.md) et le tutoriel [Aéroplane](Aeroplane/fr.md).
-   L\'angle de rotation peut être défini en degrés dans l\'interface graphique, mais il est enregistré en radians en interne, de sorte que les angles doivent généralement être convertis lorsqu\'ils sont utilisés dans des scripts.



## Script


**Voir aussi :**

[FreeCAD Script de base](FreeCAD_Scripting_Basics/fr.md).

Voir le [Tutoriel pour scripter en Python](Python_scripting_tutorial/fr#Vecteurs_et_placements.md).

Un positionnement est défini en interne par une matrice. Dans de nombreux cas, il est plus simple de le représenter au moyen de deux composants, un point (vecteur) `Base` et une valeur `Rotation`. `Rotation` lui-même a différentes représentations. Il peut être entièrement défini par la valeur d\'un \"[quaternion](https://fr.wikipedia.org/wiki/Quaternion)\" `(xi + yj + zk + w)`, mais il peut aussi être décrit par une rotation `Axis` (vecteur unitaire) et une rotation `Angle` (radians).


```python
import FreeCAD as App

doc = App.newDocument()
obj = doc.addObject("Part::Cylinder", "Cylinder")

print(obj.Placement)
# Placement [Pos=(0,0,0), Yaw-Pitch-Roll=(0,0,0)]
print(obj.Placement.Base)
# Vector (0.0, 0.0, 0.0)
print(obj.Placement.Rotation)
# Rotation (0.0, 0.0, 0.0, 1.0)

print(obj.Placement.Rotation.Angle)
# 0.0
print(obj.Placement.Rotation.Axis)
# Vector (0.0, 0.0, 1.0)
print(obj.Placement.Rotation.Q)
# (0.0, 0.0, 0.0, 1.0)
```

Déplacez le point de base de l\'objet puis faites pivoter l\'objet de 45 degrés autour de l\'axe X.

Le module mathématique fournit une méthode en `radians()`. Il permet de convertir facilement les degrés en radians et doit être importé en premier lieu.


```python
import math

obj.Placement.Base = App.Vector(5, 3, 1)
obj.Placement.Rotation.Axis = App.Vector(1, 0, 0)
obj.Placement.Rotation.Angle = math.radians(45)

print(obj.Placement)
# Placement [Pos=(5,3,1), Yaw-Pitch-Roll=(0,0,45)]
print(obj.Placement.Rotation.Q)
# (0.3826834323650898, 0.0, 0.0, 0.9238795325112867)
print(obj.Placement.Matrix)
# Matrix ((1,0,0,5),(0,0.707107,-0.707107,3),(0,0.707107,0.707107,1),(0,0,0,1))
```





{{Std Base navi

}}



---
⏵ [documentation index](../README.md) > Std Placement/fr
