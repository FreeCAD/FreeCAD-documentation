---
- GuiCommand:
   Name: Arch Rebar ColumnReinforcement
   Name/fr: Arch : Rebar Armature circulaire
   MenuLocation: Arch -> Rebar tools
   Workbenches: Arch_Workbench/fr, BIM_Workbench/fr
   Version: 0.19
   SeeAlso: Reinforcement_Workbench/fr, Arch_Rebar_ColumnReinforcement_TwoTiesSixRebars/fr, Arch_Rebar/fr
---

# Arch Rebar Circular ColumnReinforcement/fr

## Description

L\'outil [Renforcement de colonnes](Arch_Rebar_Circular_ColumnReinforcement/fr.md) permet à l\'utilisateur de créer des barres de renforcement à l\'intérieur d\'un objet Column [Arch Structure](Arch_Structure/fr.md).

Cette commande fait partie de l\'[atelier Reinforcement](Reinforcement_Workbench/fr.md), un [atelier externe](External_workbenches/fr.md) que vous pouvez installer avec le <img alt="" src=images/Std_AddonMgr.svg  style="width:24px;"> [Gestionnaire des extensions](Std_AddonMgr/fr.md) via le menu **Outils → Gestionnaire des extensions → Reinforcement**.

<img alt="" src=images/Arch_Rebar_Circular_ColumnReinforcement_example.png  style="width:400px;"> 
*Renfort de colonne circulaire à l'intérieur d'une colonne [Arch Structure](Arch_Structure/fr.md)*

## Utilisation

1\. Sélectionnez n\'importe quelle face d\'un objet **<img src="images/_Arch_Structure.svg" width=16px> [Arch Structure](Arch_Structure/fr.md) précédemment créé.**.
2. Ensuite, sélectionnez **<img src="images/_Arch_Rebar_ColumnReinforcement.svg" width=16px> [Renforcement de colonne](Arch_Rebar_ColumnReinforcement/fr.md)** dans les outils d\'armature.
3. Une boîte de dialogue apparaîtra à l\'écran comme indiqué ci-dessous.

<img alt="" src=images/ColumnReinforcementDialog_Ties.png  style="width:700px;"> 
*Boîte de dialogue pour l'outil Arch Rebar renforcement de colonnes*

4\. Sélectionnez Circular Column dans la boîte de dialogue Renforcement de colonne.

<img alt="" src=images/CircularColumnReinforcementDialog.png  style="width:700px;"> 
*Boîte de dialogue pour le renforcement de colonne circulaire*

5\. Entrez les données relatives au ferraillage des colonnes circulaires.
6. Cliquez sur **OK** ou **Apply** pour générer un renforcement de la colonne circulaire.

15\. Cliquez sur **Cancel** pour quitter la boîte de dialogue.

## Propriétés

**Barres hélicoïdales:**

-    {{PropertyData/fr|SideCover}}: La distance entre l\'armature et la face incurvée.

-    {{PropertyData/fr|Top Cover}}: La distance entre l\'armature et la face supérieure de la structure.

-    {{PropertyData/fr|Bottom Cover}}: La distance entre l\'armature et la face inférieure de la structure.

-    {{PropertyData/fr|Pitch}}: Le pas d\'une hélice est la hauteur d\'un tour d\'hélice complet, mesuré parallèlement à l\'axe de l\'hélice.

-    {{PropertyData/fr|Diameter}}: Diamètre de l\'armature.

**Main Rebars :**

-    {{PropertyData/fr|Top Offset}}: distance entre les armatures à partir de la face supérieure de la structure.

-    {{PropertyData/fr|Bottom Offset}}: distance entre les barres d\'armature à partir de la face inférieure de la structure.

-    {{PropertyData/fr|Diameter}}: diamètre des armatures principales.

-    {{PropertyData/fr|Number}}: le nombre d\'armatures principales.

-    {{PropertyData/fr|Angle}}: la distance angulaire entre les liens.

## Script


**Voir aussi :**

[Arch API](Arch_API/fr.md), [API de renforts](Reinforcement_API/fr.md) et [FreeCAD Scripts de Base](FreeCAD_Scripting_Basics/fr.md).

L'outil Renforcement de colonne (ColumnReinforcement) peut être utilisé dans une [macros](macros/fr.md) et dans la console [Python](Python/fr.md) en utilisant la fonction suivante :

### Création d\'un renfort de colonne circulaire 


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

-    `s_cover`, `helical_rebar_t_offset` et `helical_rebar_b_offset` sont des distances internes de décalage pour la barre d\'armature hélicoïdale par rapport aux faces de la structure. Ce sont respectivement les décalages latéraux, supérieurs et inférieurs.

-    `pitch`est le paramètre qui détermine la proximité ou l\'éloignement de chaque boucle hélicoïdale.

-    `dia_of_helical_rebar`est le diamètre de l\'armature hélicoïdale à l\'intérieur de la structure.

-    `main_rebars_t_offset`et {{incode | main_rebars_b_offset}} sont des distances de décalage internes pour les armatures principales par rapport aux faces supérieure et inférieure de la structure, respectivement.

-    `dia_of_main_rebars`est le diamètre des armatures principales.

-    `number_angle_check`s\'il est `True`, cela créera autant de barres d\'armement principales que celles données par `number_angle_value`. Si c\'est {{incode | False}}, cela créera des armatures principales avec un angle de `number_spacing_value`, exprimé en degrés.

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

### Edition du renfort de colonne circulaire 

Vous pouvez modifier les propriétés des barres d'armature hélicoïdale et principale à l'aide de la fonction suivante:


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



---
⏵ [documentation index](../README.md) > [Reinforcement](Category_Reinforcement.md) > [Arch](Arch_Workbench.md) > Arch Rebar Circular ColumnReinforcement/fr
