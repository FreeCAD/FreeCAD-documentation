---
- GuiCommand   */fr
   Name   *Arch Rebar BentShape
   Name/fr   *Arch Rebar Armature cintrée
   MenuLocation   *Arch → Rebar tools → Bent-Shape Rebar<br>3D/BIM → Reinforcement → Bent-Shape Rebar
   Workbenches   *[Arch](Arch_Workbench/fr.md), [BIM](BIM_Workbench/fr.md)
   Version   *0.17
   SeeAlso   *[Reinforcement](Reinforcement_Workbench.md), [Arch Armature personnalisée](Arch_Rebar/fr.md), [Arch Armature en étrier](Arch_Rebar_Stirrup/fr.md), 
---

# Arch Rebar BentShape/fr

## Description

L\'outil [Rebar Armature cintrée](Arch_Rebar_BentShape/fr.md) permet à l\'utilisateur de créer un ensemble de barres d\'armature pliées à l\'intérieur d\'un objet [Structure](Arch_Structure/fr.md).

L\'outil [BentShape Rebar](Arch_Rebar_BentShape/fr.md) est également intégré dans l\'[atelier BIM](BIM_Workbench/fr.md).

Cette commande fait partie de l\'[atelier Reinforcement](Reinforcement_Workbench/fr.md), un [atelier externe](External_workbenches/fr.md) que vous pouvez installer avec le <img alt="" src=images/Std_AddonMgr.svg  style="width   *24px;"> [Gestionnaire d\'Addon](Std_AddonMgr/fr.md) via le menu **Outils → Gestionnaire d'Addon → Reinforcement**.

<img alt="" src=images/Arch_Rebar_BentShape_example.png  style="width   *400px;"> 
*Deux jeux de barres de ferraillage pliées à l'intérieur d'une [Structure](Arch_Structure/fr.md)*

## Utilisation

1.  Sélectionnez n'importe quelle face d'un objet **<img src="images/Arch_Structure.svg" width=16px> [Arch Structure](Arch_Structure/fr.md)**.

2.  Ensuite, sélectionnez **<img src="images/Arch_Rebar_BentShape.svg" width=16px> [Arch Armature cintrée](Arch_Rebar_BentShape/fr.md)** à partir des outils de barres d\'armature.

3.  Un [Panneau des tâches](Task_Panel/fr.md) apparaîtra sur le côté gauche de l\'écran, comme indiqué ci-dessous.

4.  Sélectionnez l\'orientation souhaitée.

5.  Remplissez les entrées telles que \'Left Cover\', Right Cover, Top Cover, \'Bottom Cover\', \'Front Cover\', \'Bent Angle\', \'Bent Factor\', \'Rounding\' et \'Diameter\' of the rebar.

6.  Sélectionnez le mode de distribution \'Amount\' ou \'Spacing\'.
    -   Si \'Spacing\' est sélectionné, un utilisateur peut également opter pour [espacement personnalisé](Custom_Spacing/fr.md).

7.  
    **Pick Selected Face**(choisir la face sélectionnée) est utilisé pour vérifier ou modifier la face pour la distribution des barres.

8.  Cliquez sur **OK** ou **Apply** pour générer les barres.

9.  Cliquez sur **Cancel** pour quitter le panneau de tâches.

   *   <img alt="" src=images/BentShapeDialog.png  style="width   *250px;">



*Panneau de tâches pour l'outil Armature cintrée*

## Propriétés

-    {{PropertyData/fr|Orientation}}   * Il définit l\'orientation de l\'armature (comme fond, haut, droite et gauche).

-    {{PropertyData/fr|Front Cover}}   * La distance entre l\'armature et la face sélectionnée.

-    {{PropertyData/fr|Left Cover}}   * La distance entre l\'extrémité gauche de l\'armature et la face gauche de la structure.

-    {{PropertyData/fr|Right Cover}}   * La distance entre l\'extrémité droite de l\'armature et la face droite de la structure.

-    {{PropertyData/fr|Bottom Cover}}   * La distance entre l\'armature et la face inférieure de la structure.

-    {{PropertyData/fr|Top Cover}}   * La distance entre l\'armature et la face supérieure de la structure.

-    {{PropertyData/fr|Anchor Length}}   * Il s\'agit de la longueur de la forme courbée de l\'armature .

-    {{PropertyData/fr|Bent Angle}}   * Il définit l\'angle de cintrage de l\'armature.

-    {{PropertyData/fr|Amount}}   * La quantité de barres d\'armature.

-    {{PropertyData/fr|Spacing}}   * La distance entre les axes de chaque barre.

## Script


**Voir aussi    ***

[Arch API](Arch_API/fr.md) et [FreeCAD Scripts de Base](FreeCAD_Scripting_Basics/fr.md).

L\'outil Armature cintrée peut être utilisé dans une [macro](macros/fr.md) et à partir de la console [Python](Python/fr.md) à l\'aide de la fonction suivante    * 
```python
Rebar = makeBentShapeRebar(f_cover, b_cover, l_cover, r_cover,
                           diameter, t_cover, bentLength, bentAngle, rounding, amount_spacing_check, amount_spacing_value, orientation="Bottom",
                           structure=None, facename=None)
```

-   Crée un objet `Rebar` à partir de la `structure` donnée qui est une [Arch Structure](Arch_Structure.md) et `facename` qui est une face de cette structure.
    -   Si aucun `structure` ni `facename` n\'est donné, la face sélectionnée par l\'utilisateur sera entrée.

-    `f_cover`, `b_cover`, `l_cover`, `r_cover`, et `t_cover` sont des distances de décalage internes pour les éléments d\'armature avec respect des faces de la structure. Ce sont respectivement les décalages avant, inférieur, gauche, droit et supérieur.

-    `diameter`est le diamètre des barres de renforcement à l\'intérieur de la structure.

-    `rounding`est le paramètre qui détermine le rayon de courbure des barres d\'armature centrales.

-    `bentLength`et `bentAngle` définissent la longueur de la pointe des barres d\'armature et l\'angle de flexion à partir des barres centrales.

-    `amount_spacing_check`s\'il est `True`, il créera autant de barres de ferraillage que celles données par `amount_spacing_value`; s\'il est `False`, il créera des barres de renforcement séparées par la valeur numérique de `amount_spacing_value`.

-    `amount_spacing_value`spécifie le nombre de barres d\'armature ou la valeur de la distance qui les sépare en fonction de `amount_spacing_check`.

-    `orientation`spécifie l\'orientation de la barre. Il peut s\'agir de `"Bottom"`, `"Top"`, `"Left"`, ou `"Right"`.

### Exemples


```python
import FreeCAD, Arch, BentShapeRebar

Structure = Arch.makeStructure(length=1000, width=1000, height=100)
Structure.ViewObject.Transparency = 80
FreeCAD.ActiveDocument.recompute()

Rebar = BentShapeRebar.makeBentShapeRebar(50, 20, 20, 20,
                                          8, 40, 100, 135, 2, True, 4, "Bottom", Structure, "Face4")
Rebar.ViewObject.ShapeColor = (0.9, 0.0, 0.0)

Rebar2 = BentShapeRebar.makeBentShapeRebar(50, 40, 20, 20,
                                           8, 20, 100, 135, 2, True, 4, "Bottom", Structure, "Face6")
Rebar2.ViewObject.ShapeColor = (0.0, 0.0, 0.9) 
```

### Modifier la barre 

Vous pouvez changer les propriétés de la barre d'armature avec la fonction suivante   *


```python
editBentShapeRebar(Rebar, f_cover, b_cover, l_cover, r_cover,
                   diameter, t_cover, bentLength, bentAngle, rounding, amount_spacing_check, amount_spacing_value, orientation,
                   structure=None, facename=None)
```

-    `Rebar`est un objet `BentShapeRebar` créé précédemment.

-   Les autres paramètres sont les mêmes que ceux requis par la fonction `makeBentShapeRebar()`.

-    `structure`et `facename` peuvent être omis afin que l\'armature reste dans la structure d\'origine.


```python
import BentShapeRebar

BentShapeRebar.editBentShapeRebar(Rebar, 50, 20, 20, 20,
                                  12, 20, 100, 155, 2, True, 6, "Top")

BentShapeRebar.editBentShapeRebar(Rebar2, 50, 35, 20, 20,
                                  12, 35, 100, 155, 2, True, 6, "Top")
```





 

[Category   *Reinforcement](Category_Reinforcement.md)



---
![](images/Right_arrow.png) [documentation index](../README.md) > [Reinforcement](Category_Reinforcement.md) > [Arch](Arch_Workbench.md) > Arch Rebar BentShape/fr
