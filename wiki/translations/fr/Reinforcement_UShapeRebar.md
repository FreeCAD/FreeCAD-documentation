---
 GuiCommand:
   Name: Reinforcement UShapeRebar
   Name/fr: Reinforcement Armature en U
   MenuLocation: 3D/BIM , Outils pour les armatures , Armature en U
   Workbenches: BIM_Workbench/fr, Reinforcement_Workbench/fr
   Version: 0.17
   SeeAlso: 
---

# Reinforcement UShapeRebar/fr

## Description

L\'outil [Armature en U](Reinforcement_UShapeRebar/fr.md) permet à l\'utilisateur de créer un ensemble d\'armatures en forme de U à l\'intérieur d\'un objet de **<img src="images/Arch_Structure.svg" width=16px> [Arch Structure](Arch_Structure/fr.md)**.

Cet outil fait partie de l\'[atelier Reinforcement](Reinforcement_Workbench/fr.md), un [atelier externe](External_workbenches/fr.md) qui peut être installé avec le <img alt="" src=images/Std_AddonMgr.svg  style="width:24px;"> [gestionnaire des extensions](Std_AddonMgr/fr.md).

<img alt="" src=images/Arch_Rebar_UShape_example.png  style="width:400px;"> 
*Deux jeux d'armatures en forme de U à l'intérieur d'une [Arch Structure](Arch_Structure/fr.md)*



## Utilisation

1.  Sélectionnez n'importe quelle face d'un objet **<img src="images/Arch_Structure.svg" width=16px> [Arch Structure](Arch_Structure/fr.md)** crée précedemment.

2.  Ensuite, sélectionnez **<img src="images/Reinforcement_UShapeRebar.svg" width=16px> [Armature en U](Reinforcement_UShapeRebar/fr.md)** dans la barre d\'outil pour les armatures.

3.  Un [panneau des tâches](Task_Panel/fr.md) apparaîtra sur le côté gauche de l\'écran, comme indiqué ci-dessous.

4.  Sélectionnez l\'orientation souhaitée.

5.  Remplissez les entrées telles que \"Left Cover\", \"Right Cover\", \"Top Cover\", \"Bottom Cover\", \"Front Cover\", \"Bent Angle\", \"Bent Factor\", \"Rounding\" et \"Diameter\" de l\'armature.

6.  Sélectionnez le mode de distribution \"Amount\" ou \"Spacing\".
    -   Si \"Spacing\" est sélectionné, l\'utilisateur peut également opter pour un [espacement personnalisé](Custom_Spacing/fr.md).

7.  
    **Pick Selected Face**est utilisé pour vérifier ou modifier la face pour la distribution des armatures.

8.  Cliquez sur **OK** ou **Appliquer** pour générer les armatures.

9.  Cliquez sur **Annuler** pour quitter le panneau de tâches.

<img alt="" src=images/UShapeDialog.png  style="width:250px;"> 
*Panneau des tâches de l'outil*



## Propriétés

-    **Orientation**: définit l\'orientation de l\'armature (comme fond, haut, droite et gauche).

-    **Front Cover**: distance entre l\'armature et la face sélectionnée.

-    **Right Cover**: distance entre l\'extrémité droite de l\'armature et la face droite de la structure.

-    **Left Cover**: distance entre l\'extrémité gauche de l\'armature à la face gauche de la structure.

-    **Bottom Cover**: distance entre l\'armature de la face inférieure de la structure.

-    **Top Cover**: distance entre l\'armature et la face supérieure de la structure.

-    **Rounding**: valeur d\'arrondi à appliquer aux coins des armatures, exprimée en fois le diamètre.

-    **Amount**: nombre d\'armatures.

-    **Spacing**: distance entre les axes de chaque armature.



## Script


**Voir aussi :**

[Arch API](Arch_API/fr.md), [Reinforcement API](Reinforcement_API/fr.md) et [FreeCAD Débuter avec les scripts](FreeCAD_Scripting_Basics/fr.md).

L\'outil Armature en U peut être utilisé dans les [macro](Macros/fr.md) et à partir de la console [Python](Python/fr.md) à l\'aide de la fonction suivante :


```python
Rebar = makeUShapeRebar(f_cover, b_cover, r_cover, l_cover,
                        diameter, t_cover, rounding, amount_spacing_check, amount_spacing_value, orientation="Bottom",
                        structure=None, facename=None)
```

-   Crée un objet `Rebar` à partir de la `structure` donnée qui est une [Arch Structure](Arch_Structure/fr.md) et `facename` qui est une face de cette structure.
    -   Si aucune `structure` ni `facename` n\'est donné, la face sélectionnée par l\'utilisateur sera entrée.

-    `f_cover`, `b_cover`, `r_cover`, `l_cover` et `t_cover` sont des distances de décalage internes pour les éléments d\'armature avec respect des faces de la structure. Ce sont respectivement les décalages avant, inférieur, droit, gauche et supérieur.

-    `diameter`est le diamètre des armatures à l\'intérieur de la structure.

-    `rounding`est le paramètre qui détermine le rayon de courbure des armatures.

-    `amount_spacing_check`si `True`, cela créera autant d\'armatures que celles données par `amount_spacing_value`. Si `False`, cela créera des armatures séparées par la valeur numérique de `amount_spacing_value`.

-    `amount_spacing_value`spécifie le nombre d\'armatures, ou la valeur de la distance qui les sépare, en fonction de `amount_spacing_check`.

-    `orientation`spécifie l\'orientation de d\'armature. Il peut s\'agir de `"Bottom"` (bas), `"Top"` (haut), `"Right"` (droite), or `"Left"` (gauche).



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



### Éditer l\'armature 

Vous pouvez changer les propriétés de l'armature avec la fonction suivante :


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



---
⏵ [documentation index](../README.md) > [External_Command_Reference](Category_External_Command_Reference.md) > [Reinforcement](Category_Reinforcement.md) > [BIM](Category_BIM.md) > Reinforcement UShapeRebar/fr
