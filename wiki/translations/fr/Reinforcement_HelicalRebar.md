---
 GuiCommand:
   Name: Reinforcement HelicalRebar
   Name/fr: Reinforcement Armature hélicoïdale
   MenuLocation: 3D/BIM , Reinforcement tools , Armature hélicoïdale
   Workbenches: BIM_Workbench/fr, Reinforcement_Workbench/fr
   Version: 0.17
   SeeAlso: 
---

# Reinforcement HelicalRebar/fr

## Description

L\'outil [Armature hélicoïdale](Reinforcement_HelicalRebar/fr.md) permet à l\'utilisateur de créer une armature hélicoïdale continue dans un objet de [Arch Structure](Arch_Structure/fr.md).

Cet outil fait partie de l\'[atelier Reinforcement](Reinforcement_Workbench/fr.md), un [atelier externe](External_workbenches/fr.md) qui peut être installé avec le <img alt="" src=images/Std_AddonMgr.svg  style="width:24px;"> [gestionnaire des extensions](Std_AddonMgr/fr.md).

:   <img alt="" src=images/Arch_Rebar_Helical_example.png  style="width:80px;">



*Une armature hélicoïdale continue à l'intérieur d'une [Arch Structure](Arch_Structure/fr.md)*



## Utilisation

1.  Sélectionnez n'importe quelle face d'un objet créé précédemment **<img src="images/Arch_Structure.svg" width=16px> [Arch Structure](Arch_Structure/fr.md)**.

2.  Puis sélectionnez **<img src="images/Reinforcement_HelicalRebar.svg" width=16px> [Armature hélicoïdale](Reinforcement_HelicalRebar/fr.md)** dans la barre d\'outils des armatures.

3.  Un [panneau des tâches](Task_Panel/fr.md) apparaîtra sur le côté gauche de l\'écran, comme indiqué ci-dessous.

4.  Sélectionnez l\'orientation souhaitée.

5.  Remplissez les entrées telles que \"Left Cover\", \"Right Cover\", \"Top Cover\", \"Bottom Cover\", \"Front Cover\", \"Bent Angle\", \"Bent Factor\", \"Rounding\" et \"Diameter\" de l\'armature.

6.  Sélectionnez le mode de distribution \"Amount\" ou \"Spacing\".
    -   Si \"Spacing\" est sélectionné, l\'utilisateur peut également opter pour un [espacement personnalisé](Custom_Spacing/fr.md).

7.  
    **Pick Selected Face**est utilisé pour vérifier ou modifier la face pour la distribution des armatures.

8.  Cliquez sur **OK** ou **Apply** pour générer les armatures.

9.  Cliquez sur **Cancel** pour quitter le panneau des tâches.

<img alt="" src=images/HelicalRebarDialog.png  style="width:250px;"> 
*Panneau des tâches de l'outil*



## Propriétés

-    **SideCover**: distance entre l\'armature et la face incurvée.

-    **Top Cover**: distance entre l\'armature et la face supérieure de la structure.

-    **Bottom Cover**: distance entre l\'armature et la face inférieure de la structure.

-    **Pitch**: pas d\'une hélice est la hauteur d\'un tour d\'hélice complet, mesuré parallèlement à l\'axe de l\'hélice.

-    **Diameter**: diamètre de l\'armature.



## Script


**Voir aussi :**

[Arch API](Arch_API/fr.md), [Reinforcement API](Reinforcement_API/fr.md) et [FreeCAD Débuter avec les scripts](FreeCAD_Scripting_Basics/fr.md).

L\'outil Armature hélicoïdale peut être utilisé dans [macro](Macros/fr.md) et à partir de la console [Python](Python/fr.md) à l\'aide de la fonction suivante :


```python
Rebar = makeHelicalRebar(s_cover, b_cover, diameter, t_cover, pitch, structure=None, facename=None)
```

-   Crée un objet `Rebar` à partir de la `structure` qui est une [Arch Structure](Arch_Structure/fr.md) et `facename` qui est une face de cette structure.
    -   Si aucune `structure` ni `facename` n\'est donné, la face sélectionnée par l\'utilisateur sera entrée.

-    `s_cover`, `b_cover` et `t_cover` sont des distances de décalage internes pour l\'armature par rapport aux faces de la structure. Ce sont respectivement les décalages latéraux, inférieurs et supérieurs.

-    `diameter`est le diamètre de la spirale de renforcement à l\'intérieur de la structure.

-    `pitch`est le paramètre qui détermine la proximité ou l\'éloignement de chaque boucle en spirale.



### Exemple


```python
import FreeCAD, Draft, Arch, HelicalRebar

Circle = Draft.makeCircle(radius=250)
Structure = Arch.makeStructure(Circle)
Structure.ViewObject.Transparency = 80
FreeCAD.ActiveDocument.recompute()

Rebar = HelicalRebar.makeHelicalRebar(10, 50, 8, 50, 50, structure, "Face2")
```



### Éditer l\'armature 

Vous pouvez changer les propriétés de l\'armature avec la fonction suivante :


```python
editHelicalRebar(Rebar, s_cover, b_cover, diameter, t_cover, pitch, structure=None, facename=None)
```

-    `Rebar`est un objet `HelicalRebar` créé précédemment.

-   Les autres paramètres sont les mêmes que ceux requis par la fonction `makeHelicalRebar()`.

-    `structure`et `facename` peuvent être omis afin que l\'armature reste dans la structure d\'origine.


```python
import HelicalRebar

HelicalRebar.editHelicalRebar(Rebar, 20, 100, 20, 20, 100)
```



---
⏵ [documentation index](../README.md) > [External_Command_Reference](Category_External_Command_Reference.md) > [Reinforcement](Category_Reinforcement.md) > [BIM](Category_BIM.md) > Reinforcement HelicalRebar/fr
