---
- GuiCommand:/fr
   Name:Arch Rebar UShape
   Name/fr:Arch Rebar Armature en U
   MenuLocation:Arch → Rebar tools → Rebar UShape ou 3D/BIM → Reinforcement → Rebar UShape
   Workbenches:[Arch](Arch_Workbench/fr.md), [BIM](BIM_Workbench/fr.md)
   SeeAlso:[Reinforcement](Reinforcement_Workbench.md), [Arch Armature personnalisée](Arch_Rebar/fr.md), [Arch Armature en L](Arch_Rebar_LShape/fr.md)
   Version:0.17
---

## Description

L\'outil [Armature en U](Arch_Rebar_UShape/fr.md) permet à l\'utilisateur de créer un ensemble de barres d\'armature en forme de U à l\'intérieur d\'un objet [Arch Structure](Arch_Structure/fr.md).

L\'outil **<img src="images/Arch_Rebar_UShape.svg" width=16px> [UShape Rebar](Arch_Rebar_UShape/fr.md)** esy aussi intégré dans l\'[atelier BIM](BIM_Workbench.md).

Cette commande fait partie de l\'[atelier Reinforcement](Reinforcement_Workbench/fr.md), un [atelier externe](External_workbenches/fr.md) qui peut être installé avec <img alt="" src=images/AddonManager.svg  style="width:24px;"> [Gestionnaire d\'Addon](Addon_Manager/fr.md) via le menu **Outils → Gestionnaire d'Addon → Reinforcement**.

<img alt="" src=images/Arch_Rebar_UShape_example.png  style="width:400px;"> 
*Deux jeux d'armatures de renforcement en forme de U à l'intérieur d'une [Structure](Arch_Structure/fr.md)*

## Comment faire 

1.  Sélectionnez n'importe quelle face d'un objet **<img src="images/Arch_Structure.svg" width=16px> [[Arch Structure]]** crée précedemment.

2.  Ensuite, sélectionnez **<img src="images/Arch_Rebar_UShape.svg" width=16px> [UShape Rebar](Arch_Rebar_UShape.md)** dans les outils pour barres d\'armature.

3.  Un [Panneau des tâches](Task_Panel/fr.md) apparaîtra sur le côté gauche de l\'écran, comme indiqué ci-dessous.

4.  Sélectionnez l\'orientation souhaitée.

5.  Remplissez les entrées telles que \'Left Cover\', Right Cover, Top Cover, \'Bottom Cover\', \'Front Cover\', \'Bent Angle\', \'Bent Factor\', \'Rounding\' et \'Diameter\' of the rebar.

6.  Sélectionnez le mode de distribution \'Amount\' ou \'Spacing\'.
    -   Si \'Spacing\' est sélectionné, un utilisateur peut également opter pour [espacement personnalisé](Custom_Spacing/fr.md).

7.  
    **Pick Selected Face**(choisir la face sélectionnée) est utilisé pour vérifier ou modifier la face pour la distribution des barres.

8.  Choisir la face sélectionnée est utilisé pour vérifier ou modifier la face pour la distribution des barres.

9.  Cliquez sur **OK** ou **Apply** pour générer les barres d'arceau.

10. Cliquez sur **Cancel** pour quitter le panneau de tâches.

:   <img alt="" src=images/UShapeDialog.png  style="width:250px;">


*Panneau d'affichage des tâches de l'outil Armature en U Arch*

## Propriétés

-    {{PropertyData/fr|Orientation}}: Il définit l\'orientation de l\'armature (comme fond, haut, droite et gauche).

-    {{PropertyData/fr|Front Cover}}: La distance entre l\'armature et la face sélectionnée.

-    {{PropertyData/fr|Right Cover}}: La distance entre l\'extrémité droite de l\'armature et la face droite de la structure.

-    {{PropertyData/fr|Left Cover}}: La distance entre l\'extrémité gauche de l\'armature à la face gauche de la structure.

-    {{PropertyData/fr|Bottom Cover}}: La distance entre l\'armature de la face inférieure de la structure.

-    {{PropertyData/fr|Top Cover}}: La distance entre l\'armature et la face supérieure de la structure.

-    {{PropertyData/fr|Rounding}}: Valeur d\'arrondi à appliquer aux coins des barres, exprimée en fois le diamètre.

-    {{PropertyData/fr|Amount}}: La quantité de barres d\'armature.

-    {{PropertyData/fr|Spacing}}: La distance entre les axes de chaque barre.

## Script


**Voir aussi :**

[Arch API](Arch_API/fr.md), [API de renforts](Reinforcement_API/fr.md) et [FreeCAD Scripts de Base](FreeCAD_Scripting_Basics/fr.md).

L\'outil Armature en U peut être utilisé dans les [macro](macros/fr.md) et à partir de la console [Python](Python/fr.md) à l\'aide de la fonction suivante : 
```python
Rebar = makeUShapeRebar(f_cover, b_cover, r_cover, l_cover,
                        diameter, t_cover, rounding, amount_spacing_check, amount_spacing_value, orientation="Bottom",
                        structure=None, facename=None)
```

-   Crée un objet `Rebar` à partir de la `structure` donnée qui est une [Arch Structure](Arch_Structure/fr.md) et `facename` qui est une face de cette structure.
    -   Si aucune `structure` ni `facename` n\'est donné, la face sélectionnée par l\'utilisateur sera entrée.

-    `f_cover`, `b_cover`, `r_cover`, `l_cover` et `t_cover` sont des distances de décalage internes pour les éléments d\'armature avec respect des faces de la structure. Ce sont respectivement les décalages avant, inférieur, droit, gauche et supérieur.

-    `diameter`est le diamètre des barres de renforcement à l\'intérieur de la structure.

-    `rounding`est le paramètre qui détermine le rayon de courbure des barres d\'armature.

-    `amount_spacing_check`s\'il est mis à `True`, il créera autant de barres de ferraillage que celles données par `amount_spacing_value`; S\'il est mis à `False`, il créera des barres de renforcement séparées par la valeur numérique de `amount_spacing_value`.

-    `amount_spacing_value`spécifie le nombre de barres d\'armature, ou la valeur de la distance qui les sépare, en fonction de `amount_spacing_check`.

-    `orientation`spécifie l\'orientation de la barre; il peut s\'agir de `"Bottom"` (bas), `"Top"` (haut), `"Right"` (droite), or `"Left"` (gauche).

### Exemple


```python
import FreeCAD, Arch, UShapeRebar

Structure = Arch.makeStructure(length=1000, width=1000, height=400)
Structure.ViewObject.Transparency = 80
FreeCAD.ActiveDocument.recompute()

Rebar = UShapeRebar.makeUShapeRebar(50, 20, 20, 20,
                                    8, 50, 4, True, 6, "Bottom", Structure, "Face4")
Rebar.ViewObject.ShapeColor = (0.9, 0.0, 0.0)

Rebar2 = UShapeRebar.makeUShapeRebar(50, 50, 20, 20,
                                     8, 50, 4, True, 6, "Bottom", Structure, "Face6")
Rebar2.ViewObject.ShapeColor = (0.0, 0.0, 0.9)
```

### Édition de la barre d'armement 

Vous pouvez changer les propriétés de la barre d'armement avec la fonction suivante. 
```python
editUShapeRebar(Rebar, f_cover, b_cover, r_cover, l_cover,
                diameter, t_cover, rounding, amount_spacing_check, amount_spacing_value, orientation,
                structure=None, facename=None) 
```

-    `Rebar`est un objet `UShapeRebar` créé précédemment.

-   Les autres paramètres sont les mêmes que ceux requis par la fonction `makeUShapeRebar()`.

-    `structure`et `facename` peuvent être omis afin que l\'armature reste dans la structure d\'origine.


```python
import UShapeRebar

UShapeRebar.editUShapeRebar(Rebar, 50, 50, 20, 20,
                            16, 20, 5, True, 5, "Top")

UShapeRebar.editUShapeRebar(Rebar2, 70, 50, 20, 20,
                            16, 70, 5, True, 5, "Top")
```





 

[Category:Reinforcement](Category:Reinforcement.md)
