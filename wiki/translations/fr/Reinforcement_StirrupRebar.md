---
 GuiCommand:
   Name: Reinforcement Stirrup
   Name/fr: Reinforcement Armature en étrier
   MenuLocation: 3D/BIM , Outils pour les armatures , Armature en étrier
   Workbenches: BIM_Workbench/fr, Reinforcement_Workbench/fr
   Version: 0.17
   SeeAlso: 
---

# Reinforcement StirrupRebar/fr

## Description

L\'outil [Armature en étrier](Reinforcement_StirrupRebar/fr.md) permet à l\'utilisateur de créer un ensemble d\'armatures en étrier à l\'intérieur d\'un objet de [Structure](Arch_Structure/fr.md).

Cet outil fait partie de l\'[atelier Reinforcement](Reinforcement_Workbench/fr.md), un [atelier externe](External_workbenches/fr.md) qui peut être installé avec le <img alt="" src=images/Std_AddonMgr.svg  style="width:24px;"> [gestionnaire des extensions](Std_AddonMgr/fr.md).

<img alt="" src=images/Arch_Rebar_Stirrup_example.png  style="width:400px;"> 
*Un jeu d'armatures en étrier à l'intérieur d'une [Arch Structure](Arch_Structure/fr.md)*



## Utilisation

1.  Sélectionnez n'importe quelle face d'un objet précédemment créé **<img src="images/Arch_Structure.svg" width=16px> [Arch Structure](Arch_Structure/fr.md)**.

2.  Ensuite, sélectionnez **<img src="images/Reinforcement_StirrupRebar.svg" width=16px> [Armature en étrier](Reinforcement_StirrupRebar/fr.md)** dans la barre des outils pour les armatures.

3.  Un [panneau des tâches](Task_Panel/fr.md) apparaîtra sur le côté gauche de l\'écran, comme indiqué ci-dessous.

4.  Sélectionnez l\'orientation souhaitée.

5.  Remplissez les entrées telles que \"Left Cover\", \"Right Cover\", \"Top Cover\", \"Bottom Cover\", \"Front Cover\", \"Bent Angle\", \"Bent Factor\", \"Rounding\" et \"Diameter\" de l\'armature.

6.  Sélectionnez le mode de distribution \"Amount\" ou \"Spacing\".
    -   Si \"Spacing\" est sélectionné, l\'utilisateur peut également opter pour [espacement personnalisé](Custom_Spacing/fr.md).

7.  
    **Pick Selected Face**est utilisé pour vérifier ou modifier la face pour la distribution des armatures.

8.  Cliquez sur **OK** ou **Apply** pour générer les armatures.

9.  Cliquez sur **Cancel** pour quitter le panneau de tâches.

<img alt="" src=images/StirrupDialog.png  style="width:250px;"> 
*Panneau des tâches de l'outil*



## Propriétés

-    **Front Cover**: distance entre l\'armature et la face sélectionnée.

-    **Right Cover**: distance entre l\'extrémité droite de l\'armature et la face droite de la structure.

-    **Left Cover**: distance entre l\'extrémité gauche de l\'armature et la face gauche de la structure.

-    **Bottom Cover**: distance entre l\'armature et la face inférieure de la structure.

-    **Top Cover**: distance entre l\'armature et la face supérieure de la structure.

-    **Bent Angle**: angle de pliage définit l\'angle aux extrémités d\'un étrier.

-    **Bent Factor**: longueur de l\'extrémité de l\'étrier.

-    **Amount**: quantité de barres d\'armature.

-    **Spacing**: distance entre les axes de chaque barre.



## Script


**Voir aussi :**

[Arch API](Arch_API/fr.md), [Reinforcement API](Reinforcement_API/fr.md) et [FreeCAD Débuter avec les scripts](FreeCAD_Scripting_Basics/fr.md).

L\'outil Armature en étrier peut être utilisé dans une [macro](Macros/fr.md) et depuis la console [Python](Python/fr.md) en utilisant la fonction suivante : 
```python
Rebar = makeStirrup(l_cover, r_cover, t_cover, b_cover, f_cover,
                    bentAngle, bentFactor, diameter, rounding, amount_spacing_check, amount_spacing_value,
                    structure=None, facename=None)
```

-   Crée un objet `Rebar` à partir de la `structure` donnée qui est une [Arch Structure](Arch_Structure/fr.md), et `facename` qui est une face de cette structure.
    -   Si ni `structure` ni `facename` n\'est donné, la face sélectionnée par l\'utilisateur sera entrée.

-    `l_cover`, `r_cover`, `t_cover`, `b_cover` et `f_cover` sont des distances de décalage internes pour les éléments d\'armature avec respect des faces de la structure. Ce sont respectivement les décalages gauche, droit, haut, bas et avant.

-    `diameter`est le diamètre des armatures de renforcement à l\'intérieur de la structure.

-    `rounding`est le paramètre qui détermine le rayon de courbure des armature lors de la création d\'une boucle.

-    `bentLength`et `bentAngle` définissent la longueur et l\'angle de la pointe de la boucle de l\'armature.

-    `amount_spacing_check`si `True`, cela créera autant de boucles d\'armature que celles données par `amount_spacing_spue`. Si `False`, cela créera des boucles d\'armature séparées par la valeur numérique de `amount_spacing_value`.

-    `amount_spacing_value`spécifie le nombre de boucles d\'armature ou la valeur de la séparation entre elles, en fonction de `amount_spacing_check`.



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



### Éditer l\'armature 

Vous pouvez changer les propriétés de l'armature avec la fonction suivante :


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



---
⏵ [documentation index](../README.md) > [External_Command_Reference](Category_External_Command_Reference.md) > [Reinforcement](Category_Reinforcement.md) > Reinforcement StirrupRebar/fr
