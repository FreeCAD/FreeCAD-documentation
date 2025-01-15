---
 GuiCommand:
   Name: Reinforcement StraightRebar
   Name/fr: Reinforcement Armature droite
   MenuLocation: 3D/BIM , Outils pour les armatures , Armature droite
   Workbenches: BIM_Workbench/fr, Reinforcement_Workbench/fr
   Version: 0.17
   SeeAlso: 
---

# Reinforcement StraightRebar/fr



## Description

L\'outil [Armature droite](Reinforcement_StraightRebar/fr.md) permet à l\'utilisateur de créer un ensemble d\'armatures droites à l\'intérieur d\'un objet de [Arch Structure](Arch_Structure/fr.md).

Cet outil fait partie de l\'[atelier Reinforcement](Reinforcement_Workbench/fr.md), un [atelier externe](External_workbenches/fr.md) qui peut être installé avec le <img alt="" src=images/Std_AddonMgr.svg  style="width:24px;"> [gestionnaire des extensions](Std_AddonMgr/fr.md).

<img alt="" src=images/Arch_Rebar_Straight_example.png  style="width:400px;"> 
*Deux jeux d'armatures droites à l'intérieur d'une [Arch Structure](Arch_Structure/fr.md)*



## Utilisation

1.  Sélectionnez n'importe quelle face d'un objet précédemment créé **<img src="images/Arch_Structure.svg" width=16px> [Arch Structure](Arch_Structure/fr.md)**.

2.  Puis sélectionnez **<img src="images/Reinforcement_StraightRebar.svg" width=16px> [Armature droite](Reinforcement_StraightRebar/fr.md)** dans la barre des outils pour les armatures

3.  Un [panneau des tâches](Task_Panel/fr.md) apparaîtra sur le côté gauche de l\'écran comme indiqué ci-dessous.

4.  Sélectionnez l\'orientation souhaitée.

5.  Remplissez les entrées telles que \"Front cover\", \"Right side cover\", \"Left side cover\", \"Bottom cover\" et \"Diameter\" de l\'armature.

6.  Sélectionnez le mode de distribution \"Amount\" ou \"Spacing\".
    -   Si \"Spacing\" est sélectionné, l\'utilisateur peut également opter pour un [espacement personnalisé](Custom_Spacing/fr.md).

7.  
    **Pick Selected Face**est utilisé pour vérifier ou modifier la face pour la distribution des armatures.

8.  Cliquez sur **OK** ou **Appliquer** pour générer les barres.

9.  Cliquez sur **Annuler** pour quitter le panneau de tâches.

<img alt="" src=images/StraightRebarDialog.png  style="width:250px;"> 
*Panneau des tâches de l'outil*



## Propriétés

-    **Orientation**: définit l\'orientation de l\'armature (comme bas, haut, droite et gauche).

-    **Front Cover**: distance entre l\'armature et la face sélectionnée.

-    **Right Cover**: distance entre l\'extrémité droite de l\'armature et la face droite de la structure.

-    **Left Cover**: distance entre l\'extrémité gauche de l\'armature et la face gauche de la structure.

-    **Cover along**: ces propriétés permettent à l\'utilisateur de spécifier la couverture supérieure ou inférieure.

-    **Bottom Cover**: distance entre l\'armature et la face inférieure de la structure.

-    **Top Cover**: distance entre l\'armature et la face supérieure de la structure.

-    **Amount**: quantité d\'armatures.

-    **Spacing**: distance entre les axes de chaque armature.



## Script


**Voir aussi :**

[Arch API](Arch_API/fr.md), [Reinforcement API](Reinforcement_API/fr.md) et [FreeCAD Débuter avec les scripts](FreeCAD_Scripting_Basics/fr.md).

L\'outil Armature droite peut être utilisé dans une [macro](Macros/fr.md) et depuis la console [Python](Python/fr.md) en utilisant la fonction suivante :


```python
Rebar = makeStraightRebar(f_cover, coverAlong, rt_cover, lb_cover,
                          diameter, amount_spacing_check, amount_spacing_value, orientation="Horizontal",
                          structure=None, facename=None)
```

-   Crée un objet `Rebar` à partir de la `structure` donnée qui est une [Arch Structure](Arch_Structure/fr.md), et `facename` qui est une face de cette structure.
    -   Si ni `structure` ni `facename` n\'est donné, la face sélectionnée par l\'utilisateur sera entrée.

-    `f_cover`, `coverAlong`, `rt_cover` et `lb_cover` sont les distances internes de décalage des éléments d\'armature par rapport aux faces de la structure.

    -   
        `f_cover`
        
        est le décalage de la couverture avant.

    -   
        `coverAlong`
        
        est un tuple `(position, value)` qui définit la valeur de décalage dans une position (haut, bas, gauche, droite) en fonction de `orientation` .

    -   
        `rt_cover`
        
        correspond au décalage de la face droite ou supérieure en fonction de la valeur de `coverAlong` et `orientation`.

    -   
        `lb_cover`
        
        correspond au décalage de la face gauche ou inférieure en fonction de la valeur de `coverAlong` et `orientation`.

-    `diameter`est le diamètre des armatures à l\'intérieur de la structure.

-    `amount_spacing_check`si `True`, cela créera autant d\'armatures que celles données par `amount_spacing_value`. Si `False`, cela créera des armatures séparées par la valeur numérique de `amount_spacing_value`.

-    `amount_spacing_value`spécifie le nombre d\'armatures, ou la valeur de la distance qui les sépare, en fonction de `amount_spacing_check`.

-    `orientation`spécifie l\'orientation de l\'armature. Il peut s\'agir de `"Horizontal"` ou `"Vertical"`.

En fonction de l\'orientation de l\'armature, la fonction peut être appelée de deux manières générales en définissant `coverAlong` de manière appropriée.



### L\'armature est horizontale 


```python
Rebar = makeStraightRebar(f_cover, ("Top Side", value), right_cover, left_cover, ...)
Rebar = makeStraightRebar(f_cover, ("Bottom Side", value), right_cover, left_cover, ...)
```

-    `coverAlong`est un tuple avec un offset `"Top Side"` (Face supérieure) ou `"Bottom Side"` (Face inférieure) de la `valeur`.

-   Dans ce cas, `rt_cover` fait référence à l\'offset `right_cover` et `lb_cover` à l\'attente `left_cover`.



### L\'armature est verticale 


```python
Rebar = makeStraightRebar(f_cover, ("Left Side", value), top_cover, bottom_cover, ...)
Rebar = makeStraightRebar(f_cover, ("Right Side", value), top_cover, bottom_cover, ...)
```

-    `coverAlong`est un tuple avec un `"Left Side"` (Côté gauche)or a `"Right Side"` (Côté droit) d\'offset {{incode | valeur}}.

-   Dans ce cas, `rt_cover` fait référence à l\'offset `top_cover` et `lb_cover` à l\'offset `bottom_cover`.



### Exemple horizontal 


```python
import Arch, Draft, StraightRebar

Structure = Arch.makeStructure(length=1000, width=1000, height=400)
Structure.ViewObject.Transparency = 80
FreeCAD.ActiveDocument.recompute()

Rebar = StraightRebar.makeStraightRebar(50, ("Bottom Side", 20), 100, 100,
                                        12, True, 5, "Horizontal", Structure, "Face4")
Rebar.ViewObject.ShapeColor = (0.9, 0.0, 0.0)

Rebar2 = StraightRebar.makeStraightRebar(50, ("Bottom Side", 50), 100, 100,
                                         12, True, 5, "Horizontal", Structure, "Face6")
Rebar2.ViewObject.ShapeColor = (0.0, 0.0, 0.9)
```



### Exemple vertical 


```python
import Arch, Draft, StraightRebar

Structure2 = Arch.makeStructure(length=1000, width=1000, height=400)
Structure2.ViewObject.Transparency = 80
Draft.move(Structure2, FreeCAD.Vector(1500, 0, 0))
FreeCAD.ActiveDocument.recompute()

Rebar3 = StraightRebar.makeStraightRebar(50, ("Left Side", 20), 100, 100,
                                         12, True, 5, "Vertical", Structure2, "Face4")
Rebar3.ViewObject.ShapeColor = (0.9, 0.5, 0.0)

Rebar4 = StraightRebar.makeStraightRebar(50, ("Left Side", 50), 100, 100,
                                         12, True, 5, "Vertical", Structure2, "Face6")
Rebar4.ViewObject.ShapeColor = (0.0, 0.5, 0.5)
```



### Éditer l\'armature 

Vous pouvez changer les propriétés de l'armature avec la fonction suivante :


```python
editStraightRebar(Rebar, f_cover, coverAlong, rt_cover, lb_cover,
                  diameter, amount_spacing_check, amount_spacing_value, orientation,
                  structure=None, facename=None)
```

-    `Rebar`est un objet `StraightRebar` créé précédemment.

-   Les autres paramètres sont les mêmes que ceux requis par la fonction `makeStraightRebar()`.

-    `structure`et `facename` peuvent être omis afin que l\'armature reste dans la structure d\'origine.

Exemple :


```python
import StraightRebar

StraightRebar.editStraightRebar(Rebar, 50, ("Top Side", 20), 100, 100,
                                24, True, 7, "Horizontal")

StraightRebar.editStraightRebar(Rebar2, 50, ("Top Side", 50), 100, 100,
                                24, True, 7, "Horizontal")

StraightRebar.editStraightRebar(Rebar3, 50, ("Right Side", 20), 100, 100,
                                24, True, 7, "Vertical")

StraightRebar.editStraightRebar(Rebar4, 50, ("Right Side", 50), 100, 100,
                                24, True, 7, "Vertical")
```



---
⏵ [documentation index](../README.md) > [External_Command_Reference](Category_External_Command_Reference.md) > [Reinforcement](Category_Reinforcement.md) > Reinforcement StraightRebar/fr
