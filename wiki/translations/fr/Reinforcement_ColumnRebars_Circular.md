---
 GuiCommand:
   Name: Reinforcement ColumnRebars
   Name/fr: Reinforcement Armature circulaire
   MenuLocation: 3D/BIM , Outils pour les armatures , Armature pour colonne
   Workbenches: BIM_Workbench/fr, Reinforcement_Workbench/fr
   Version: 0.19
   SeeAlso: Reinforcement_ColumnRebars/fr, Reinforcement_ColumnRebars_TwoTiesSixRebars/fr
---

# Reinforcement ColumnRebars Circular/fr

## Description

L\'outil [Armature pour colonne ](Reinforcement_ColumnRebars/fr.md) permet à l\'utilisateur de créer des armatures à l\'intérieur d\'un objet colonne de [Arch Structure](Arch_Structure/fr.md). Cette page présente un exemple d\'utilisation supplémentaire de l\'outil.

Cet outil fait partie de l\'[atelier Reinforcement](Reinforcement_Workbench/fr.md), un [atelier externe](External_workbenches/fr.md) qui peut être installé avec le <img alt="" src=images/Std_AddonMgr.svg  style="width:24px;"> [gestionnaire des extensions](Std_AddonMgr/fr.md).

Trois exemples d\'utilisation sont disponibles :

-   [Colonne rectangulaire à une seul cadre](Reinforcement_ColumnRebars/fr.md)
-   [Armature 2 cadres 6 barres](Reinforcement_ColumnRebars_TwoTiesSixRebars/fr.md)
-   [Colonne circulaire (voir ci-dessous)](#Utilisation.md)

<img alt="" src=images/Arch_Rebar_Circular_ColumnReinforcement_example.png  style="width:400px;"> 
*Armature circulaire à l'intérieur d'une [colonne](Arch_Structure/fr.md)*



## Utilisation

1\. Sélectionnez la face supérieur de l\'objet **<img src="images/Arch_Structure.svg" width=16px> [Arch Structure](Arch_Structure/fr.md)** précédemment crée.

2\. Sélectionnez ensuite **<img src="images/Reinforcement_ColumnRebars.svg" width=16px> [Armature pour colonne](Reinforcement_ColumnRebars/fr.md)** de la barre d\'outils des armatures.

3\. Une boîte de dialogue apparaîtra à l\'écran, comme indiqué ci-dessous.

:   <img alt="" src=images/ColumnReinforcementDialog_Ties.png  style="width:700px;">

:   
    
*Boîte de dialogue pour l'outil Armature en colonne de Arch*
    

4\. Sélectionnez Circular Column dans la boîte de dialogue Column Reinforcement.

:   <img alt="" src=images/CircularColumnReinforcementDialog.png  style="width:700px;">

:   
    
*Boîte de dialogue pour armature circulaire de colonne*
    

5\. Entrez les données relatives aux armatures des colonnes circulaires.

12\. Cliquez sur **OK** ou **Appliquer** pour générer un armature circulaire de colonne.

7\. Cliquez sur **Annuler** pour quitter la fenêtre de dialogue.



## Propriétés

**Helical Rebars:** barres hélicoïdales

-    **SideCover**: distance entre l\'armature et la face incurvée.

-    **Top Cover**: distance entre l\'armature et la face supérieure de la structure.

-    **Bottom Cover**: distance entre l\'armature et la face inférieure de la structure.

-    **Pitch**: pas d\'une hélice est la hauteur d\'un tour d\'hélice complet, mesuré parallèlement à l\'axe de l\'hélice.

-    **Diameter**: diamètre de l\'armature.

**Main Rebars:** armature principale

-    **Top Offset**: distance entre les armatures à partir de la face supérieure de la structure.

-    **Bottom Offset**: distance entre les armatures à partir de la face inférieure de la structure.

-    **Diameter**: diamètre des armatures principales.

-    **Number**: le nombre d\'armatures principales.

-    **Angle**: la distance angulaire entre les étriers.



## Script


**Voir aussi :**

[Arch API](Arch_API/fr.md), [Reinforcement API](Reinforcement_API/fr.md) et [FreeCAD Débuter avec les scripts](FreeCAD_Scripting_Basics/fr.md).

L'outil Armature circulaire peut être utilisé dans une [macros](Macros/fr.md) et dans la console [Python](Python/fr.md) en utilisant la fonction suivante :



### Créer une armature circulaire de colonne 


```python
RebarGroup = CircularColumn.makeReinforcement(
    s_cover,
    helical_rebar_t_offset,
    helical_rebar_b_offset,
    pitch,
    dia_of_helical_rebar,
    main_rebars_t_offset,
    main_rebars_b_offset,
    dia_of_main_rebars,
    number_angle_check,
    number_angle_value,
    structure=None,
    facename=None,
)
```

-   Crée un objet `RebarGroup` à partir de la `structure` donnée qui est une [Arch Structure](Arch_Structure/fr.md) et de `facename` qui est une face de cette structure.
    -   Si aucune `structure` ni `facename` n\'est donné, la face sélectionnée par l\'utilisateur sera entrée.

-    `s_cover`, `helical_rebar_t_offset` et `helical_rebar_b_offset` sont des distances internes de décalage pour l\'armature hélicoïdale par rapport aux faces de la structure. Ce sont respectivement les décalages latéraux, supérieurs et inférieurs.

-    `pitch`est le paramètre qui détermine la proximité ou l\'éloignement de chaque boucle hélicoïdale.

-    `dia_of_helical_rebar`est le diamètre de l\'armature hélicoïdale à l\'intérieur de la structure.

-    `main_rebars_t_offset`et {{incode | main_rebars_b_offset}} sont des distances de décalage internes pour les armatures principales par rapport aux faces supérieure et inférieure de la structure, respectivement.

-    `dia_of_main_rebars`est le diamètre des armatures principales.

-    `number_angle_check`s\'il est `True`, cela créera autant d\'armatures principales que celles données par `number_angle_value`. Si c\'est {{incode | False}}, cela créera des armatures principales avec un angle de `number_spacing_value`, exprimé en degrés.

-    `number_angle_value`spécifie le nombre d\'armatures principales, ou la valeur de l\'angle entre les armatures principales, selon `number_angle_check`.



#### Exemple


```python
import FreeCAD, Draft, Arch
from ColumnReinforcement import CircularColumn

Circle = Draft.makeCircle(radius=250)
Structure = Arch.makeStructure(Circle)
Structure.ViewObject.Transparency = 80
FreeCAD.ActiveDocument.recompute()

RebarGroup = CircularColumn.makeReinforcement(
    s_cover=20,
    helical_rebar_t_offset=40,
    helical_rebar_b_offset=40,
    pitch=50,
    dia_of_helical_rebar=8,
    main_rebars_t_offset=20,
    main_rebars_b_offset=20,
    dia_of_main_rebars=16,
    number_angle_check=True,
    number_angle_value=6,
    structure=Structure,
    facename="Face3",
).rebar_group
```



### Éditer une armature circulaire de colonne 

Vous pouvez modifier les propriétés des armatures hélicoïdales et des armatures principales à l'aide de la fonction suivante :


```python
rebar_group = editReinforcement(
    rebar_group,
    s_cover,
    helical_rebar_t_offset,
    helical_rebar_b_offset,
    pitch,
    dia_of_helical_rebar,
    main_rebars_t_offset,
    main_rebars_b_offset,
    dia_of_main_rebars,
    number_angle_check,
    number_angle_value,
    structure=None,
    facename=None,
)
```

-    `rebar_group`est un objet de groupe `ColumnReinforcement` créé précédemment.

-   Les autres paramètres sont les mêmes que ceux requis par la fonction `makeSingleTieFourRebars()`.

-    `structure`et `facename` peuvent être omis afin que l\'armature reste dans la structure d\'origine.



#### Exemple 


```python
from ColumnReinforcement import CircularColumn

rebar_group = CircularColumn.editReinforcement(
    rebar_group,
    s_cover=30,
    helical_rebar_t_offset=30,
    helical_rebar_b_offset=30,
    pitch=60,
    dia_of_helical_rebar=10,
    main_rebars_t_offset=-30,
    main_rebars_b_offset=-30,
    dia_of_main_rebars=18,
    number_angle_check=False,
    number_angle_value=45,
    structure=Structure,
    facename="Face3",
)
```




{{BIM_Tools_navi}}



---
⏵ [documentation index](../README.md) > [External_Command_Reference](Category_External_Command_Reference.md) > [Reinforcement](Category_Reinforcement.md) > Reinforcement ColumnRebars Circular/fr
