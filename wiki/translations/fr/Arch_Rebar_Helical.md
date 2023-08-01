---
- GuiCommand:/fr
   Name:Arch Rebar Helical
   Name/fr:Arch Rebar Armature hélicoïdale
   MenuLocation:Arch → Outils pour les armatures → Armature hélicoïdale<br>3D/BIM → Reinforcement tools → Armature hélicoïdale
   Workbenches:[Arch](Arch_Workbench/fr.md), [BIM](BIM_Workbench/fr.md)
   Version:0.17
   SeeAlso:[Reinforcement](Reinforcement_Workbench.md), [Arch Armature personnalisée](Arch_Rebar/fr.md), [Arch Rebar Armature en étrier](Arch_Rebar_Stirrup/fr.md), [Arch Rebar Armature en colonnes](Arch_Rebar_ColumnReinforcement/fr.md)
---

# Arch Rebar Helical/fr

## Description

L\'outil [Armature hélicoïdale](Arch_Rebar_Helical/fr.md) permet à l\'utilisateur de créer une armature hélicoïdale continue dans l\'élément structurel [Arch Structure](Arch_Structure/fr.md).

L\'outil [Armature hélicoïdale](Arch_Rebar_Helical/fr.md) est également intégré dans l\'[atelier BIM](BIM_Workbench/fr.md).

Cette commande fait partie de l\'[atelier Reinforcement](Reinforcement_Workbench/fr.md), un [atelier externe](External_workbenches/fr.md) qui peut être installé avec le <img alt="" src=images/Std_AddonMgr.svg  style="width:24px;"> [Gestionnaire des extensions](Std_AddonMgr/fr.md) via le menu **Outils → Gestionnaire des extensions → Reinforcement**.

:   <img alt="" src=images/Arch_Rebar_Helical_example.png  style="width:80px;">



*Une barre de renforcement hélicoïdale continue à l'intérieur d'une [Arch Structure](Arch_Structure/fr.md)*



## Utilisation

1.  Sélectionnez n'importe quelle face d'un objet créé précédemment **<img src="images/Arch_Structure.svg" width=16px> [Arch Structure](Arch_Structure/fr.md)**.

2.  Puis sélectionnez **<img src="images/Arch_Rebar_Helical.svg" width=16px> [Armature hélicoïdale](Arch_Rebar_Helical/fr.md)** dans les outils pour barres d\'armature.

3.  Un [panneau des tâches](Task_Panel/fr.md) apparaîtra sur le côté gauche de l\'écran, comme indiqué ci-dessous.

4.  Sélectionnez l\'orientation souhaitée.

5.  Remplissez les entrées telles que \"Face gauche\", \"Face droite\", \"Face supérieure\", \"Face inférieure\", \"Face avant\", \"Angle de flexion\", \"Facteur de courbure\", \"Arrondi\" et \"Diamètre\" de l\'armature.

6.  Sélectionnez le mode de distribution \"Quantité\" ou \"Écartement\".
    -   Si \"Écartement\" est sélectionné, l\'utilisateur peut également opter pour [espacement personnalisé](Custom_Spacing/fr.md).

7.  
    **Choisir la face sélectionnée**est utilisé pour vérifier ou modifier la face pour la distribution des barres.

8.  Cliquez sur **OK** ou **Appliquer** pour générer les barres.

9.  Cliquez sur **Annuler** pour quitter le panneau de tâches.

:   <img alt="" src=images/HelicalRebarDialog.png  style="width:250px;">



*Panneau de tâches pour l'outil Arch Armature hélicoïdale*



## Propriétés

-    **SideCover**: distance entre l\'armature et la face incurvée.

-    **Top Cover**: distance entre l\'armature et la face supérieure de la structure.

-    **Bottom Cover**: distance entre l\'armature et la face inférieure de la structure.

-    **Pitch**: pas d\'une hélice est la hauteur d\'un tour d\'hélice complet, mesuré parallèlement à l\'axe de l\'hélice.

-    **Diameter**: diamètre de l\'armature.



## Script


**Voir aussi :**

[Arch API](Arch_API/fr.md), [API de renforts](Reinforcement_API/fr.md) et [FreeCAD Scripts de Base](FreeCAD_Scripting_Basics/fr.md).

L\'outil Armature hélicoïdale peut être utilisé dans [macro](Macros/fr.md) et à partir de la console [Python](Python/fr.md) à l\'aide de la fonction suivante:


```python
Rebar = makeHelicalRebar(s_cover, b_cover, diameter, t_cover, pitch, structure=None, facename=None)
```

-   Crée un objet `Rebar` à partir de la `structure` qui est une [Arch Structure](Arch_Structure/fr.md) et `facename` qui est une face de cette structure.
    -   Si aucune `structure` ni `facename` n\'est donné, la face sélectionnée par l\'utilisateur sera entrée.

-    `s_cover`, `b_cover` et `t_cover` sont des distances de décalage internes pour la barre d\'armature par rapport aux faces de la structure. Ce sont respectivement les décalages latéraux, inférieurs et supérieurs.

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

### Modification de l\'armature 

Vous pouvez changer les propriétés de l\'armature avec la fonction suivante.


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
![](images/Button_right.svg) [documentation index](../README.md) > [Reinforcement](Category_Reinforcement.md) > [Arch](Arch_Workbench.md) > Arch Rebar Helical/fr
