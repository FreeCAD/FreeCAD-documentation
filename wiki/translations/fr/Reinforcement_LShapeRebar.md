---
 GuiCommand:
   Name: Reinforcement LShape
   Name/fr: Reinforcement Armature en L
   MenuLocation: 3D/BIM , Outils pour les armatures , Armature en L
   Workbenches: BIM_Workbench/fr, Reinforcement_Workbench/fr
   Version: 0.17
   SeeAlso: 
---

# Reinforcement LShapeRebar/fr

## Description

L\'outil [Armature en L](Arch_Rebar_LShape/fr.md) permet à l\'utilisateur de créer un ensemble d\'armatures en forme de L à l\'intérieur d\'un objet de [Arch Structure](Arch_Structure/fr.md).

Cet outil fait partie de l\'[atelier Reinforcement](Reinforcement_Workbench/fr.md), un [atelier externe](External_workbenches/fr.md) qui peut être installé avec le <img alt="" src=images/Std_AddonMgr.svg  style="width:24px;"> [gestionnaire des extensions](Std_AddonMgr/fr.md).

<img alt="" src=images/Arch_Rebar_LShape_example.png  style="width:400px;"> 
*Quatre jeux d'armatures en forme de L à l’intérieur d’une [Arch Structure](Arch_Structure/fr.md)*



## Utilisation

1.  Sélectionnez n'importe quelle face d'un objet de **<img src="images/Arch_Structure.svg" width=16px> [Arch Structure](Arch_Structure/fr.md)** créé précédemment.

2.  Ensuite, sélectionnez **<img src="images/Reinforcement_LShapeRebar.svg" width=16px> [Armature en L](Reinforcement_LShapeRebar/fr.md)** à partir de la barre d\'outils des armatures

3.  Un [panneau des tâches](Task_Panel/fr.md) apparaîtra sur le côté gauche de l\'écran, comme indiqué ci-dessous.

4.  Sélectionnez l\'orientation souhaitée.

5.  Remplissez les entrées telles que \"Left Cover\", Right Cover, Top Cover, \"Bottom Cover\", \"Front Cover\", \"Bent Angle\", \"Bent Factor\", \"Rounding\" et \"Diameter\" de l\'armature.

6.  Sélectionnez le mode de distribution \"Amount\" ou \"Spacing\".
    -   Si \"Spacing\" est sélectionné, un utilisateur peut également opter pour un [espacement personnalisé](Custom_Spacing/fr.md).

7.  
    **Pick Selected Face**est utilisé pour vérifier ou modifier la face pour la distribution des armatures.

8.  Cliquez sur **OK** ou **Appliquer** pour générer l\'armature.

9.  Cliquez sur **Annuler** pour quitter le panneau des tâches.

<img alt="" src=images/LShapeDialog.png  style="width:250px;"> 
*Panneau des tâches de l'outil*



## Propriétés

-    **Orientation**: définit l\'orientation de l\'armature (comme bas, haut, droite et gauche).

-    **Front Cover**: distance entre l\'armature et la face sélectionnée.

-    **Right Cover**: distance entre l\'extrémité droite de l\'armature et la face droite de la structure.

-    **Left Cover**: distance entre l\'extrémité gauche de l\'armature et la face gauche de la structure.

-    **Bottom Cover**: distance entre l\'armature et la face inférieure de la structure.

-    **Top Cover**: distance entre l\'armature et la face supérieure de la structure.

-    **Rounding**: valeur d\'arrondi à appliquer aux coins des armatures, exprimée en fois le diamètre.

-    **Amount**: nombre d\'armatures.

-    **Spacing**: distance entre les axes de chaque armature.



## Script


**Voir aussi:**

[Arch API](Arch_API/fr.md), [API de renforts](Reinforcement_API/fr.md) et [FreeCAD Débuter avec les scripts](FreeCAD_Scripting_Basics/fr.md).

L\'outil Armature en L peut être utilisé dans les [macro](Macros/fr.md) et à partir de la console [Python](Python/fr.md) à l\'aide de la fonction suivante :


```python
Rebar = makeLShapeRebar(f_cover, b_cover, l_cover, r_cover,
                        diameter, t_cover, rounding, amount_spacing_check, amount_spacing_value, orientation="Bottom Left",
                        structure=None, facename=None):
```

-   Crée un objet `Rebar` à partir de la `structure` donnée, qui est une [Arch Structure](Arch_Structure/fr.md) et `facename` qui est une face de cette structure.
    -   Si aucune `structure` ni `facename` n\'est donné, la face sélectionnée par l\'utilisateur sera entrée.

-    `f_cover`, `b_cover`, `l_cover`, `r_cover` et `t_cover` sont des distances de décalage internes pour les éléments de l\'armature par rapport aux faces de la structure. Ce sont respectivement les décalages avant, inférieur, gauche, droit et supérieur.

-    ` diameter`est le diamètre des armatures à l\'intérieur de la structure.

-    `rounding`est le paramètre qui détermine le rayon de courbure des armatures.

-    `amount_spacing_check`mis à True, cela créera autant de armatures que celles indiquées par amount_spacing_value. Si la valeur est False, des armatures seront séparées par la valeur numérique de amount_spacing_value.

-    `amount_spacing_value`spécifie le nombre d\'armatures ou la valeur de la séparation les séparant en fonction de amount_spacing_check.

-    `orientation`spécifie l\'orientation de l\'armature. Il peut s\'agir de


`"Bottom Right"`

(En bas à droite), `"Bottom Left"` (En bas à gauche), `"Top Right"` (En haut à droite), or `"Top Left"` (en haut à gauche).



### Exemple


```python
import FreeCAD, Arch, LShapeRebar

Structure = Arch.makeStructure(length=1000, width=1000, height=400)
Structure.ViewObject.Transparency = 80
FreeCAD.ActiveDocument.recompute()

Rebar = LShapeRebar.makeLShapeRebar(50, 20, 20, 20,
                                    8, 50, 4, True, 6, "Bottom Left", Structure, "Face4")
Rebar.ViewObject.ShapeColor = (0.9, 0.0, 0.0)

Rebar2 = LShapeRebar.makeLShapeRebar(50, 50, 20, 20,
                                     8, 50, 4, True, 6, "Bottom Left", Structure, "Face6")
Rebar2.ViewObject.ShapeColor = (0.0, 0.0, 0.9) 
```



### Éditer l\'armature 

Vous pouvez changer les propriétés de l'armature avec la fonction suivante :


```python
editLShapeRebar(Rebar, f_cover, b_cover, l_cover, r_cover,
                diameter, t_cover, rounding, amount_spacing_check, amount_spacing_value, orientation,
                structure=None, facename=None)
```

-    `Rebar`est un objet `LShapeRebar` créé précédemment.

-   Les autres paramètres sont les mêmes que ceux requis par la fonction `makeLShapeRebar()`.

-    `structure`et `facename` peuvent être omis afin que l\'armature reste dans la structure d\'origine.


```python
import LShapeRebar

LShapeRebar.editLShapeRebar(Rebar, 50, 50, 20, 20,
                            12, 50, 6, True, 5, "Top Right")

LShapeRebar.editLShapeRebar(Rebar2, 50, 50, 20, 20,
                            12, 70, 6, True, 5, "Top Right")
```




{{BIM_Tools_navi}}



---
⏵ [documentation index](../README.md) > [External_Command_Reference](Category_External_Command_Reference.md) > [Reinforcement](Category_Reinforcement.md) > Reinforcement LShapeRebar/fr
