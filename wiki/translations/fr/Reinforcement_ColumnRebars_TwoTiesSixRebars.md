---
 GuiCommand:
   Name: Reinforcement ColumnRebars
   Name/fr: Reinforcement Armature 2 cadres 6 barres
   MenuLocation: 3D/BIM , Outils pour les armatures , Armature pour colonne
   Workbenches: BIM_Workbench/fr, Reinforcement_Workbench/fr
   Version: 0.19
   SeeAlso: Reinforcement_ColumnRebars/fr, Reinforcement_ColumnRebars_TwoTiesSixRebars/fr
---

# Reinforcement ColumnRebars TwoTiesSixRebars/fr

## Description

L\'outil [Armature pour colonne](Reinforcement_ColumnRebars/fr.md) permet à l\'utilisateur de créer des armatures à l\'intérieur d\'un objet colonne de [Arch Structure](Arch_Structure/fr.md). Cette page présente un exemple d\'utilisation supplémentaire de l\'outil.

Cet outil fait partie de l\'[atelier Reinforcement](Reinforcement_Workbench/fr.md), un [atelier externe](External_workbenches/fr.md) qui peut être installé avec le <img alt="" src=images/Std_AddonMgr.svg  style="width:24px;"> [gestionnaire des extensions](Std_AddonMgr/fr.md).

Trois exemples d\'utilisation sont disponibles :

-   [Colonne rectangulaire à une seul cadre](Reinforcement_ColumnRebars/fr.md)
-   [Armature 2 cadres 6 barres (voir ci-dessous)](#Utilisation/fr.md)
-   [Colonne circulaire ](Reinforcement_ColumnRebars_Circular/fr.md)

<img alt="" src=images/Arch_Rebar_ColumnReinforcement_TwoTies_example.png  style="width:400px;"> 
*Armature 2x6 à l'intérieur d'une [colonne](Arch_Structure/fr.md)*



## Utilisation

1\. Sélectionnez n\'importe quelle face d\'un objet **<img src="images/Arch_Structure.svg" width=16px> [Arch Structure](Arch_Structure/fr.md)**.

2\. Sélectionnez ensuite **<img src="images/Reinforcement_ColumnRebars.svg" width=16px> [Armature pour colonne](Reinforcement_ColumnRebars/fr.md)** de la barre d\'outils des armatures.

3\. Une boîte de dialogue apparaîtra à l\'écran, comme indiqué ci-dessous.

:   <img alt="" src=images/ColumnReinforcementDialog_Ties.png  style="width:700px;">

:   
    
*Boîte de dialogue pour l'outil Armature en colonne de Arch*
    

4\. Sélectionnez l\'armature TwoTiesSixRebars dans le menu déroulant à droite.

:   <img alt="" src=images/TwoTiesColumnReinforcementDialog_Ties.png  style="width:700px;">

:   
    
*Fenêtre de dialogue pour Armature 2 cadres 6 barres*
    

5\. Donnez des entrées pour les données relatives aux étriers.

6\. Cliquez sur **Suivant** et la boîte de dialogue sera mise à jour comme indiqué ci-dessous.

:   <img alt="" src=images/TwoTiesColumnReinforcementDialog_MainRebars.png  style="width:700px;">

:   
    
*Fenêtre de dialogue pour les données des armatures principales*
    

7\. Sélectionner le type d\'armature souhaité et remplir les données pour les armatures principales.

8\. Cliquez sur **OK** ou **Appliquer** pour générer une colonne d\'armatures.

9\. Cliquez sur **Annuler** pour quitter la fenêtre de dialogue.



## Propriétés

**Ties:** étriers

-    **Left Cover**: distance entre l\'extrémité gauche du cadre et la face gauche de la structure.

-    **Right Cover**: distance entre l\'extrémité droite du cadre et la face droite de la structure.

-    **Top Cover**: distance entre le cadre et la face supérieure de la structure.

-    **Bottom Cover**: distance entre le cadre et la face inférieure de la structure.

-    **Offset**: distance entre le cadre et la face supérieure/inférieure de la structure.

-    **Diameter**: diamètre du cadre.

-    **Bent Angle**: angle plié définit l\'angle aux extrémités d\'un cadre.

-    **Extension Factor**: facteur d\'extension définit la longueur de la fin du cadre, exprimée en diamètre.

-    **Number**: nombre de cadres.

-    **Spacing**: distance entre les axes de chaque cadre.

-    **Ties Sequence**: séquence des cadres de haut en bas par rapport à la vue de face.

**Main Rebars:** armatures présentes aux coins du cadre

-    **Rebar Type**: type d\'armature principale.

-    **Hook Orientation**: orientation des crochets en forme de L.

-    **Hook Extend Along**: direction pour l\'extension du crochet.

-    **Hook Extension**: longueur du crochet des armatures en forme de L.

-    **Rounding**: valeur d\'arrondi à appliquer aux coins des armatures en forme de L, exprimée en fois le diamètre.

-    **Top Offset**: distance entre les armatures de la face supérieure de la structure.

-    **Bottom Offset**: distance entre les armatures de la face inférieure de la structure.

-    **Diameter**: diamètre des armatures principales.



## Script


**Voir aussi :**

[Arch API](Arch_API/fr.md), [Reinforcement API](Reinforcement_API/fr.md) et [FreeCAD Débuter avec les scripts](FreeCAD_Scripting_Basics/fr.md).

L'outil Armature en colonne peut être utilisé dans une [macros](Macros/fr.md) et dans la console [Python](Python/fr.md) en utilisant la fonction suivante :



### Créer une armature 2 cadres 6 barres 


```python
RebarGroup = makeTwoTiesSixRebars(
    l_cover_of_ties,
    r_cover_of_ties,
    t_cover_of_ties,
    b_cover_of_ties,
    offset_of_ties,
    bent_angle_of_ties,
    extension_factor_of_ties,
    dia_of_ties,
    number_spacing_check,
    number_spacing_value,
    dia_of_main_rebars,
    t_offset_of_rebars,
    b_offset_of_rebars,
    main_rebars_type="StraightRebar",
    hook_orientation="Top Inside",
    hook_extend_along="x-axis",
    l_rebar_rounding=None,
    hook_extension=None,
    ties_sequence=("Tie1", "Tie2"),
    structure=None,
    facename=None,
)
```

-   Crée un objet `RebarGroup` à partir de la `structure` donnée, qui est une [ Arch Structure](Arch_Structure/fr.md), et de `facename`, qui est une face de cet objet structure.
    -   Si aucune `structure` ni `facename` n\'est donné, la face sélectionnée par l\'utilisateur sera utilisé.

-    `l_cover_of_ties`, `r_cover_of_ties`, `t_cover_of_ties`, `b_cover_of_ties` et `offset_of_ties` sont des distances internes de décalage pour les éléments des cadres en ce qui concerne aux faces de la structure. Ce sont respectivement les décalages gauche, droit, haut, bas et avant/arrière.

-    `bent_angle_of_ties`définit l\'angle de la pointe de la boucle des armatures des cadres.

-    `extension_factor_of_ties`définit la longueur de la pointe de la boucle des armatures des cadres, exprimée en fois le diamètre des cadres.

-    `dia_of_ties`est le diamètre des cadres.

-    `number_spacing_check`si `True`, cela créera autant d\'étriers que donné par `number_spacing_value` ; si `False`, cela créera deux ensembles d\'étriers par la valeur numérique de `number_spacing_value`.

-    `number_spacing_spue`spécifie le nombre de deux ensembles de cadres, ou la valeur de la séparation entre les ensembles, en fonction de `number_spacing_check`.

-    `dia_of_main_rebars`est le diamètre des armatures principales.

-    `t_offset_of_rebars`et `b_offset_of_rebars` sont des distances de décalage internes pour les armatures principales respectivement par rapport aux faces supérieure et inférieure de la structure.

-    `main_rebars_type`est le type d\'armature principale. il peut s\'agir de `"StraightRebar"` ou de `"LShapeRebar"`.

-    `hook_orientation`spécifie l\'orientation du crochet en forme de L. Il peut s\'agir de : `"Top Inside"`, `"Top Outside"`, `"Bottom Inside"`, `"Bottom Outside"`, `"Top Right"`, `"Top Left"`, `"Bottom Right"` ou `"Bottom Left"`.

-    `hook_extend_along`spécifie la direction de l\'extension du crochet. Il peut s\'agir de `"x-axis"` ou `"y-axis"`.

-    `l_rebar_rounding`est le paramètre qui détermine le rayon de courbure des armatures principales en forme de L, exprimé en diamètre.

-    `hook_extension`est la longueur du crochet des armatures en forme de L.

-    `ties_sequence`est la séquence des cadres de haut en bas par rapport à la vue de face. Il peut s\'agir de `("Tie1", "Tie2")` ou de `("Tie2", "Tie1")`.



#### Exemple


```python
import FreeCAD, Draft, Arch
from ColumnReinforcement import TwoTiesSixRebars

# It doesn't work if the structure is not based on a face
# Structure = Arch.makeStructure(length=1000, width=400, height=400)

Rect = Draft.makeRectangle(400, 400)
Structure = Arch.makeStructure(Rect, height=1600)
Structure.ViewObject.Transparency = 80
FreeCAD.ActiveDocument.recompute()

# For Straight Rebars
RebarGroup = TwoTiesSixRebars.makeTwoTiesSixRebars(
    l_cover_of_ties=40,        
    r_cover_of_ties=40,
    t_cover_of_ties=40,
    b_cover_of_ties=40,
    offset_of_ties=100,
    bent_angle_of_ties=135,
    extension_factor_of_ties=2,
    dia_of_ties=8,
    number_spacing_check=True,
    number_spacing_value=10,
    dia_of_main_rebars=16,
    t_offset_of_rebars=40,
    b_offset_of_rebars=40,
    main_rebars_type="StraightRebar",
    hook_orientation="Top Inside",
    hook_extend_along="x-axis",
    l_rebar_rounding=None,
    hook_extension=None,
    ties_sequence=("Tie1", "Tie2"),
    structure=Structure,
    facename="Face6",
)

# For LShaped Rebars with hook along x-axis
RebarGroup = TwoTiesSixRebars.makeTwoTiesSixRebars(
    l_cover_of_ties=40,
    r_cover_of_ties=40,
    t_cover_of_ties=40,
    b_cover_of_ties=40,
    offset_of_ties=100,
    bent_angle_of_ties=135,
    extension_factor_of_ties=2,
    dia_of_ties=8,
    number_spacing_check=True,
    number_spacing_value=10,
    dia_of_main_rebars=16,
    t_offset_of_rebars=-40,
    b_offset_of_rebars=-40,
    main_rebars_type="LShapeRebar",
    hook_orientation="Top Outside",
    hook_extend_along="x-axis",
    l_rebar_rounding=2,
    hook_extension=40,
    ties_sequence=("Tie1", "Tie2"),
    structure=Structure,
    facename="Face6",
)

# For LShaped Rebars with hook along y-axis and tie sequence ("Tie2", "Tie1")

RebarGroup = TwoTiesSixRebars.makeTwoTiesSixRebars(
    l_cover_of_ties=40,        
    r_cover_of_ties=40,
    t_cover_of_ties=40,
    b_cover_of_ties=40,
    offset_of_ties=100,
    bent_angle_of_ties=135,
    extension_factor_of_ties=2,
    dia_of_ties=8,
    number_spacing_check=True,
    number_spacing_value=10,
    dia_of_main_rebars=16,
    t_offset_of_rebars=-40,
    b_offset_of_rebars=-40,
    main_rebars_type="LShapeRebar",
    hook_orientation="Top Outside",
    hook_extend_along="y-axis",
    l_rebar_rounding=2,
    hook_extension=40,
    ties_sequence=("Tie2", "Tie1"),
    structure=Structure,
    facename="Face6",
)
```



### Éditer une armature 2 cadres 6 barres 

Vous pouvez modifier les propriétés des cadres et des armatures avec la fonction suivante :


```python
rebar_group = editTwoTiesSixRebars(
    rebar_group,
    l_cover_of_ties,
    r_cover_of_ties,
    t_cover_of_ties,
    b_cover_of_ties,
    offset_of_ties,
    bent_angle_of_ties,
    extension_factor_of_ties,
    dia_of_ties,
    number_spacing_check,
    number_spacing_value,
    dia_of_main_rebars,
    t_offset_of_rebars,
    b_offset_of_rebars,
    main_rebars_type="StraightRebar",
    hook_orientation="Top Inside",
    hook_extend_along="x-axis",
    l_rebar_rounding=None,
    hook_extension=None,
    ties_sequence=("Tie1", "Tie2"),
    structure=None,
    facename=None,
)
```

-    `rebar_group`est un objet de groupe `ColumnReinforcement` créé précédemment.

-   Les autres paramètres sont les mêmes que ceux requis par la fonction `makeSingleTieFourRebars()`.

-    `structure`et `facename` peuvent être omis afin que l\'armature reste dans la structure d\'origine.



#### Exemple 


```python
from ColumnReinforcement import TwoTiesSixRebars

rebar_group = TwoTiesSixRebars.editTwoTiesSixRebars(
    rebar_group,                                
    l_cover_of_ties=40,        
    r_cover_of_ties=40,
    t_cover_of_ties=40,
    b_cover_of_ties=40,
    offset_of_ties=100,
    bent_angle_of_ties=135,
    extension_factor_of_ties=2,
    dia_of_ties=8,
    number_spacing_check=True,
    number_spacing_value=10,
    dia_of_main_rebars=16,
    t_offset_of_rebars=-40,
    b_offset_of_rebars=-40,
    main_rebars_type="LShapeRebar",
    hook_orientation="Top Outside",
    hook_extend_along="x-axis",
    l_rebar_rounding=2,
    hook_extension=40,
    ties_sequence=("Tie2", "Tie1"),
    structure=None,
    facename=None,
)
```




{{BIM_Tools_navi}}



---
⏵ [documentation index](../README.md) > [External_Command_Reference](Category_External_Command_Reference.md) > [Reinforcement](Category_Reinforcement.md) > Reinforcement ColumnRebars TwoTiesSixRebars/fr
