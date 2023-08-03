---
 GuiCommand:
   Name: Arch Rebar Straight
   Name/fr: Arch Rebar Armature droite
   MenuLocation: Arch , Outils pour les armatures , Armature droite<br>3D/BIM , Reinforcement tools , Armature droite
   Workbenches: Arch_Workbench/fr, BIM_Workbench/fr
   Version: 0.17
   SeeAlso: Reinforcement_Workbench/fr, Arch_Rebar/fr, Arch_Rebar_BOM/fr
---

# Arch Rebar Straight/fr



## Description

L\'outil [Armature droite](Arch_Rebar_Straight/fr.md) permet à l\'utilisateur de créer un ensemble de barres d\'armature droites à l\'intérieur d\'un objet [Arch Structure](Arch_Structure/fr.md).

L\'outil [Armature droite](Arch_Rebar_Straight/fr.md) est également intégré à l\'[atelier BIM](BIM_Workbench/fr.md).

Cette commande fait partie de l\'[atelier Reinforcement](Reinforcement_Workbench/fr.md), un [atelier externe](External_workbenches/fr.md) qui peut être installé avec le <img alt="" src=images/Std_AddonMgr.svg  style="width:24px;"> [Gestionnaire des extensions](Std_AddonMgr/fr.md) via le menu **Outils → Gestionnaire des extensions → Reinforcement**.

<img alt="" src=images/Arch_Rebar_Straight_example.png  style="width:400px;"> 
*Deux jeux d'armatures droites à l'intérieur d'une [Arch Structure](Arch_Structure/fr.md)*



## Utilisation

1.  Sélectionnez n'importe quelle face d'un objet créé précédemment **<img src="images/Arch_Structure.svg" width=16px> [Arch Structure](Arch_Structure/fr.md)**.

2.  Puis sélectionnez **<img src="images/Arch_Rebar_Straight.svg" width=16px> [Armature droite](Arch_Rebar_Straight/fr.md)** dans les outils pour barres d\'armature.

3.  Un [panneau des tâches](Task_Panel/fr.md) apparaîtra sur le côté gauche de l\'écran comme indiqué ci-dessous.

4.  Sélectionnez l\'orientation souhaitée.

5.  Remplissez les entrées telles que \"Face avant\", \"Face droite\", \"Face gauche\", \"Face inférieure\" et \"Diamètre\" de l\'armature.

6.  Sélectionnez le mode de distribution \"Quantité\" ou \"Écartement\".
    -   Si \"Écartement\" est sélectionné, l\'utilisateur peut également opter pour [espacement personnalisé](Custom_Spacing/fr.md).

7.  
    **Choisir la face sélectionnée**est utilisé pour vérifier ou modifier la face pour la distribution des barres.

8.  Cliquez sur **OK** ou **Appliquer** pour générer les barres.

9.  Cliquez sur **Annuler** pour quitter le panneau de tâches.

<img alt="" src=images/StraightRebarDialog.png  style="width:250px;"> 
*Panneau de tâches pour l'outil Armature droite*



## Propriétés

-    **Orientation**: définit l\'orientation de la barre d\'armature (comme fond, haut, droite et gauche).

-    **Front Cover**: distance entre l\'armature et la face sélectionnée.

-    **Right Cover**: distance entre l\'extrémité droite de l\'armature et la face droite de la structure.

-    **Left Cover**: distance entre l\'extrémité gauche de l\'armature et la face gauche de la structure.

-    **Cover along**: ces propriétés permettent à l\'utilisateur de spécifier la couverture supérieure ou inférieure.

-    **Bottom Cover**: distance entre l\'armature et la face inférieure de la structure.

-    **Top Cover**: distance entre l\'armature et la face supérieure de la structure.

-    **Amount**: quantité de barres d\'armature.

-    **Spacing**: distance entre les axes de chaque barre.



## Script


**Voir aussi :**

[Arch API](Arch_API/fr.md), [Reinforcement API](Reinforcement_API/fr.md) et [FreeCAD Scripts de bases](FreeCAD_Scripting_Basics/fr.md).

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
        
        est le décalage du capot frontal.

    -   
        `coverAlong`
        
        est un tuple `(position, value)` qui définit la valeur de décalage dans une position (haut, bas, gauche, droite) en fonction de `orientation` .

    -   
        `rt_cover`
        
        correspond au décalage de la face droite ou supérieure en fonction de la valeur de `coverAlong` et `orientation`.

    -   
        `lb_cover`
        
        correspond au décalage de la face gauche ou inférieure en fonction de la valeur de `coverAlong` et `orientation`.

-    `diameter`est le diamètre des barres de renforcement à l\'intérieur de la structure.

-    `amount_spacing_check`s\'il est mis à `True`, il créera autant de barres de ferraillage que celles données par `amount_spacing_value`; S\'il est mis à `False`, il créera des barres de renforcement séparées par la valeur numérique de `amount_spacing_value`.

-    `amount_spacing_value`spécifie le nombre de barres d\'armature, ou la valeur de la distance qui les sépare, en fonction de `amount_spacing_check`.

-    `orientation`spécifie l\'orientation de la barre; il peut s\'agir de `"Horizontal"` ou `"Vertical"`.

En fonction de l\'orientation de la barre, la fonction peut être appelée de deux manières générales en définissant `coverAlong` de manière appropriée.



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

### Modification de l\'armature 

Vous pouvez changer les propriétés de l\'armature avec la fonction suivante. 
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
⏵ [documentation index](../README.md) > [Reinforcement](Category_Reinforcement.md) > [Arch](Arch_Workbench.md) > Arch Rebar Straight/fr
