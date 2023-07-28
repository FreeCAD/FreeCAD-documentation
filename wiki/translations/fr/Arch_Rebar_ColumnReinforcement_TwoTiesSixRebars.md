---
- GuiCommand:/fr
   Name:Arch Rebar ColumnReinforcement
   Name/fr:Arch Rebar Armature 2x6
   MenuLocation:Arch → Rebar tools → Column Reinforcement ou 3D/BIM → Reinforcement → Column Reinforcement
   Workbenches:[Arch](Arch_Workbench/fr.md), [BIM](BIM_Workbench/fr.md)
   SeeAlso:[Reinforcement](Reinforcement_Workbench/fr.md), [Arch Rebar](Arch_Rebar/fr.md), [Arch Rebar Armature en colonne](Arch_Rebar_ColumnReinforcement/fr.md), [Arch Rebar Poutres](Arch_Rebar_BeamReinforcement/fr.md)
   Version:0.19
---

# Arch Rebar ColumnReinforcement TwoTiesSixRebars/fr

## Description

L\'outil [Armature 2x6](Arch_Rebar_ColumnReinforcement_TwoTiesSixRebars/fr.md) permet à l\'utilisateur de créer des barres d\'armature 2x6 à l\'intérieur d\'un objet colonne [Arch Structure](Arch_Structure/fr.md).

L\'outil [Armature 2x6](Arch_Rebar_ColumnReinforcement_TwoTiesSixRebars/fr.md) est également intégré dans [atelier BIM](BIM_Workbench/fr.md).

Cette commande fait partie de l\'[Atelier Reinforcement](Reinforcement_Workbench/fr.md), un [Atelier externe](External_workbenches/fr.md) qui peut être installé avec le <img alt="" src=images/Std_AddonMgr.svg  style="width:24px;"> [Gestionnaire des extensions](Std_AddonMgr/fr.md) via le menu **Outils → Gestionnaire des extensions → Reinforcement**.

<img alt="" src=images/Arch_Rebar_ColumnReinforcement_TwoTies_example.png  style="width:400px;">



*Renfort 2x6 de colonne à l'intérieur d'une colonne [Arch Structure](Arch_Structure/fr.md)*



## Utilisation

1\. Sélectionnez n\'importe quelle face d\'un objet **<img src="images/_Arch_Structure.svg" width=16px> [Arch Structure](Arch_Structure/fr.md) précédemment créé.**.
2. Ensuite, sélectionnez **<img src="images/_Arch_Rebar_ColumnReinforcement.svg" width=16px> [Column Reinforcement](Arch_Rebar_ColumnReinforcement/fr.md)** dans les outils d\'armature.
3. Une boîte de dialogue apparaîtra à l\'écran, comme indiqué ci-dessous.
<img alt="" src=images/ColumnReinforcementDialog_Ties.png  style="width:700px;">



*Boîte de dialogue pour l'outil Arch Rebar ColumnReinforcement*

4\. Sélectionnez le type de ferraillage de colonne TwoTiesSixRebars dans le menu déroulant situé à droite.
<img alt="" src=images/TwoTiesColumnReinforcementDialog_Ties.png  style="width:700px;">



*Dialog Box pour TwoTiesSixRebars ColumnReinforcement*

5\. Donnez des entrées pour les données relatives aux liens.
6. Cliquez sur **Next** et la boîte de dialogue sera mise à jour comme indiqué ci-dessous.
<img alt="" src=images/TwoTiesColumnReinforcementDialog_MainRebars.png  style="width:700px;">



*Boîte de dialogue pour les données de barres principales*

7\. Sélectionnez le type de barres souhaité et remplissez les données pour les barres principales.
8. Cliquez sur **OK** ou **Apply** pour générer un renforcement de colonne.
9. Cliquez sur **Cancel** pour quitter la boîte de dialogue.


## Propriétés

**Ties:**

-    **Left Cover**: distance entre l\'extrémité gauche de l\'attache et la face gauche de la structure.

-    **Right Cover**: distance entre l\'extrémité droite de l\'attache et la face droite de la structure.

-    **Top Cover**: distance entre l\'attache et la face supérieure de la structure.

-    **Bottom Cover**: distance entre l\'attache et la face inférieure de la structure.

-    **Offset**: distance entre l\'attache et la face supérieure / inférieure de la structure.

-    **Diameter**: diamètre de l\'attache.

-    **Bent Angle**: angle plié définit l\'angle aux extrémités d\'une attache .

-    **Extension Factor**: facteur d\'extension définit la longueur de la fin de l\'attache, exprimée en diamètre.

-    **Number**: nombre d\'attaches.

-    **Spacing**: distance entre les axes de chaque attache.

-    **Ties Sequence**: séquence des attaches de haut en bas par rapport à la vue de face.

**Main Rebars :** Les barres d\'armature sont présentes aux coins de l\'attache

-    **Rebar Type**: type d\'armature principale.

-    **Hook Orientation**: orientation des crochets en forme de L.

-    **Hook Extend Along**: direction pour l\'extension du crochet.

-    **Hook Extension**: longueur du crochet des barres d\'armature.

-    **Rounding**: valeur d\'arrondi à appliquer aux coins des barres d\'armature en forme de L, exprimée en fois le diamètre.

-    **Top Offset**: distance entre les barres d\'armature de la face supérieure de la structure.

-    **Bottom Offset**: distance entre les barres d\'armature de la face inférieure de la structure.

-    **Diameter**: diamètre des armatures principales.



## Script


**Voir aussi :**

[Arch API](Arch_API/fr.md), [Reinforcement API](Reinforcement_API/fr.md) et [FreeCAD Scripting Basics](FreeCAD_Scripting_Basics/fr.md).

L'outil ColumnReinforcement peut être utilisé dans une [macros](macros/fr.md) et dans la console [Python](Python/fr.md) en utilisant la fonction suivante :



### Créer une Armature 2 cadres 6 barres 


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

-    `l_cover_of_ties`, `r_cover_of_ties`, `t_cover_of_ties`, `b_cover_of_ties` et `offset_of_ties` sont des distances internes de décalage pour les éléments d\'attache en ce qui concerne aux faces de la structure. Ce sont respectivement les décalages gauche, droit, haut, bas et avant/arrière.

-    `bent_angle_of_ties`définit l\'angle de la pointe de la boucle de ferraillage des éléments de jonction.

-    `extension_factor_of_ties`définit la longueur de la pointe de la boucle de renforcement des éléments de liaison, exprimée en fois le diamètre des éléments de liaison.

-    `dia_of_ties`est le diamètre des éléments de liaison.

-    `number_spacing_check`s\'il est `True`, il créera autant de jeux de liens que donné par `number_spacing_value` ; s\'il est réglé sur `False`, il créera deux ensembles de liens séparés par la valeur numérique de `number_spacing_value`.

-    `number_spacing_spue`spécifie le nombre de deux ensembles de liens, ou la valeur de la séparation entre les ensembles, en fonction de `number_spacing_check`.

-    `dia_of_main_rebars`est le diamètre des armatures principales.

-    `t_offset_of_rebars`et `b_offset_of_rebars` sont des distances de décalage internes pour les armatures principales respectivement par rapport aux faces supérieure et inférieure de la structure.

-    `main_rebars_type`est le type de\'armature principale. il peut s\'agir de `"StraightRebar"` ou de `"LShapeRebar"`.

-    `hook_orientation`spécifie l\'orientation du hook en forme de LShaped ; il peut s\'agir de: `"Top Inside"`, `"Top Outside"`, `"Bottom Inside"`, `"Bottom Outside"`, `"Top Right"`, `"Top Left"`, `"Bottom Right"` ou `"Bottom Left"`.

-    `hook_extend_along`spécifie la direction de l\'extension du hook ; il peut s\'agir de `"x-axis"` ou `"y-axis"`.

-    `l_rebar_rounding`est le paramètre qui détermine le rayon de courbure des barres d\'armature principales LShaped , est exprimé en diamètre.

-    `hook_extension`est la longueur du hook des barres d\'armature en LShaped .

-    `ties_sequence`est la séquence d\'attaches de haut en bas par rapport à la vue de face ; il peut s\'agir de `("Tie1", "Tie2")` ou de `("Tie2", "Tie1")`.



#### Exemple


```python
import FreeCAD, Draft, Arch
from ColumnReinforcement import TwoTiesSixRebars

# Cela ne fonctionne pas si la structure n'est pas basée sur une face
# Structure = Arch.makeStructure(length=1000, width=400, height=400)

Rect = Draft.makeRectangle(400, 400)
Structure = Arch.makeStructure(Rect, height=1600)
Structure.ViewObject.Transparency = 80
FreeCAD.ActiveDocument.recompute()

# Pour les barres droites

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

# Pour barres de renfort en forme de crochet avec le crochet dirigé le long de l'axe des x

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

# Pour les barres d'armature en forme de crochet avec le crochet le long de l'axe des ordonnées et séquence de liens
 
("Tie2", "Tie1")

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

### Modifier une Armature 2 cadres 6 barres 

Vous pouvez modifier les propriétés des attaches et des armatures avec la fonction suivante


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



---
![](images/Right_arrow.png) [documentation index](../README.md) > [Reinforcement](Category_Reinforcement.md) > [Arch](Arch_Workbench.md) > Arch Rebar ColumnReinforcement TwoTiesSixRebars/fr
