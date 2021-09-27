---
- GuiCommand:/fr
   Name:Arch Rebar Stirrup
   Name/fr:Arch Rebar Armature en étrier
   MenuLocation:Arch → Rebar tools → Stirrup ou 3D/BIM → Reinforcement → Stirrup
   Workbenches:[Arch](Arch_Workbench/fr.md), [BIM](BIM_Workbench/fr.md)
   Version:0.17
   SeeAlso:[Reinforcement](Reinforcement_Workbench.md), [Arch Armature personnalisée](Arch_Rebar/fr.md), [Arch Armature hélicoïdale](Arch_Rebar_Helical/fr.md)
---

# Arch Rebar Stirrup/fr

## Description

L\'outil [Stirrup Rebar](Arch_Rebar_Stirrup/fr.md) permet à l\'utilisateur de créer un ensemble de barres d\'armature pliées à l\'intérieur d\'un objet [Structure](Arch_Structure/fr.md).

L\'outil [Stirrup Rebar](Arch_Rebar_Stirrup/fr.md) est également intégré dans l\'[atelier BIM](BIM_Workbench/fr.md).

Cette commande fait partie de l\'_ via le menu **Outils → Gestionnaire d'Addon → Reinforcement**.

<img alt="" src=images/Arch_Rebar_Stirrup_example.png  style="width:400px;"> 
*Un jeu de barres de renfort en étrié à l'intérieur d'une [Arch Structure](Arch_Structure/fr.md)*

## Utilisation

1.  Sélectionnez n'importe quelle face d'un objet créé précédemment **<img src="images/Arch_Structure.svg" width=16px> [Arch Structure](Arch_Structure/fr.md)**.

2.  Ensuite, sélectionnez **<img src="images/Arch_Rebar_Stirrup.svg" width=16px> [Stirrup Rebar](Arch_Rebar_Stirrup/fr.md)** dans les outils pour barres d\'armature.

3.  Un [Panneau des tâches](Task_Panel/fr.md) apparaîtra sur le côté gauche de l\'écran, comme indiqué ci-dessous.

4.  Sélectionnez l\'orientation souhaitée.

5.  Remplissez les entrées telles que \'Left Cover\', Right Cover, Top Cover, \'Bottom Cover\', \'Front Cover\', \'Bent Angle\', \'Bent Factor\', \'Rounding\' et \'Diameter\' of the rebar.

6.  Sélectionnez le mode de distribution \'Amount\' ou \'Spacing\'.
    -   Si \'Spacing\' est sélectionné, un utilisateur peut également opter pour [espacement personnalisé](Custom_Spacing/fr.md).

7.  
    **Pick Selected Face**(choisir la face sélectionnée) est utilisé pour vérifier ou modifier la face pour la distribution des barres.

8.  Cliquez sur **OK** ou **Apply** pour générer les barres d'arceau.

9.  Cliquez sur **Cancel** pour quitter le panneau de tâches.

:   <img alt="" src=images/StirrupDialog.png  style="width:250px;">


*Panneau d'affichage des tâches de l'outil Armature en étrier*

## Propriétés

-    {{PropertyData/fr|Front Cover}}: La distance entre l\'armature et la face sélectionnée.

-    {{PropertyData/fr|Right Cover}}: La distance entre l\'extrémité droite de l\'armature et la face droite de la structure.

-    {{PropertyData/fr|Left Cover}}: La distance entre l\'extrémité gauche de l\'armature et la face gauche de la structure.

-    {{PropertyData/fr|Bottom Cover}}: La distance entre l\'armature et la face inférieure de la structure.

-    {{PropertyData/fr|Top Cover}}: La distance entre l\'armature et la face supérieure de la structure.

-    {{PropertyData/fr|Bent Angle}}: L\'angle de pliage définit l\'angle aux extrémités d\'un étrier.

-    {{PropertyData/fr|Bent Factor}}: Définit la longueur de l\'extrémité de l\'étrier.

-    {{PropertyData/fr|Amount}}: La quantité de barres d\'armature.

-    {{PropertyData/fr|Spacing}}: La distance entre les axes de chaque barre.

## Script


**Voir aussi :**

[Arch API](Arch_API/fr.md), [API de renforts](Reinforcement_API/fr.md) et [FreeCAD Scripts de Base](FreeCAD_Scripting_Basics/fr.md).

L\'outil Armature en étrier peut être utilisé dans une [macro](macros/fr.md) et depuis la console [Python](Python/fr.md) en utilisant la fonction suivante : 
```python
Rebar = makeStirrup(l_cover, r_cover, t_cover, b_cover, f_cover,
                    bentAngle, bentFactor, diameter, rounding, amount_spacing_check, amount_spacing_value,
                    structure=None, facename=None)
```

-   Crée un objet `Rebar` à partir de la `structure` donnée qui est une [Arch Structure](Arch_Structure/fr.md), et `facename` qui est une face de cette structure.
    -   Si ni `structure` ni `facename` n\'est donné, la face sélectionnée par l\'utilisateur sera entrée.

-    `l_cover`, `r_cover`, `t_cover`, `b_cover` et `f_cover` sont des distances de décalage internes pour les éléments d\'armature avec respect des faces de la structure. Ce sont respectivement les décalages gauche, droit, haut, bas et avant.

-    `diameter`est le diamètre des barres de renforcement à l\'intérieur de la structure.

-    `rounding`est le paramètre qui détermine le rayon de courbure des barres d\'armature lors de la création d\'une boucle.

-    `bentLength`et `bentAngle` définissent la longueur et l\'angle de la pointe de la boucle de ferraillage.

-    `amount_spacing_check`s\'il est mis à `True`, il créera autant de boucles de renforcement que celles données par `amount_spacing_spue`; s\'il est mis à `False`, il créera des boucles de renforcement séparées par la valeur numérique de `amount_spacing_value`.

-    `amount_spacing_value`spécifie le nombre de boucles de renforcement ou la valeur de la séparation entre elles, en fonction de `amount_spacing_check`.

### Exemple


```python
import Draft, Arch, Stirrup

# It doesn't work if the structure is not based on a face
# Structure = Arch.makeStructure(length=1000, width=400, height=400)

Rect = Draft.makeRectangle(400, 400)
Structure = Arch.makeStructure(Rect, height=1600)
Structure.ViewObject.Transparency = 80
FreeCAD.ActiveDocument.recompute()

Rebar = Stirrup.makeStirrup(20, 20, 20, 20, 20,
                            115, 4, 8, 2, True, 10, Structure, "Face6")
```

### Édition de la barre d'armement 

Vous pouvez changer les propriétés de la barre d'armement avec la fonction suivante. 
```python
editStirrup(Rebar, l_cover, r_cover, t_cover, b_cover, f_cover,
            bentAngle, bentFactor, diameter, rounding, amount_spacing_check, amount_spacing_value,
            structure=None, facename=None)
```

-    `Rebar`est un objet `StirrupRebar` créé précédemment.

-   Les autres paramètres sont les mêmes que ceux requis par la fonction `makeStirrup()`.

-    `structure`et `facename` peuvent être omis afin que l\'armature reste dans la structure d\'origine.


```python
import Stirrup

Stirrup.editStirrup(Rebar, 20, 20, 20, 20, 50,
                    100, 4, 14, 8, True, 8)
```





 

_

---
[documentation index](../README.md) > [Reinforcement](Category_Reinforcement.md) > [Arch](Arch_Workbench.md) > Arch Rebar Stirrup/fr
