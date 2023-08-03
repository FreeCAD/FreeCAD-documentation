---
 GuiCommand:
   Name: Arch Rebar ColumnReinforcement
   Name/fr: Arch Rebar Armature en colonne
   MenuLocation: Arch , Rebar tools , Column Reinforcement<br>3D/BIM , Reinforcement , Column Reinforcement
   Workbenches: Arch_Workbench/fr, BIM_Workbench/fr
   Version: 0.19
   SeeAlso: Reinforcement_Workbench/fr, Arch_Rebar/fr, Arch_Rebar_Helical/fr, Arch_Rebar_ColumnReinforcement_TwoTiesSixRebars/fr
---

# Arch Rebar ColumnReinforcement/fr

## Description

L\'outil [Renfort de colonnes](Arch_Rebar_Circular_ColumnReinforcement/fr.md) permet à l\'utilisateur de créer des barres de renforcement à l\'intérieur d\'un objet colonne [Arch Structure](Arch_Structure/fr.md).

L\'outil [Rebar Armature en colonne](Arch_Rebar_ColumnReinforcement.md) est également intégré dans [atelier BIM](BIM_Workbench/fr.md).

Cette commande fait partie de l\'[atelier Reinforcement](Reinforcement_Workbench/fr.md), un [atelier externe](External_workbenches/fr.md) que vous pouvez installer avec le <img alt="" src=images/Std_AddonMgr.svg  style="width:24px;"> [Gestionnaire des extensions](Std_AddonMgr/fr.md) via le menu **Outils → Gestionnaire des extensions → Reinforcement**.

<img alt="" src=images/Arch_Rebar_ColumnReinforcement_example.png  style="width:400px;"> 
*Renfort de colonne à l'intérieur d'une colonne [Arch Structure](Arch_Structure/fr.md)*



## Utilisation

1\. Sélectionnez n\'importe quelle face d\'un objet **<img src="images/_Arch_Structure.svg" width=16px> [Arch Structure](Arch_Structure/fr.md)** précédemment créé.
2. Ensuite, sélectionnez **<img src="images/_Arch_Rebar_ColumnReinforcement.svg" width=16px> [Column Reinforcement](Arch_Rebar_ColumnReinforcement/fr.md)** dans les outils d\'armature.
3. Une boîte de dialogue apparaîtra à l\'écran comme indiqué ci-dessous. <img alt="" src=images/ColumnReinforcementDialog_Ties.png  style="width:700px;">
*Boîte de dialogue pour l'outil Arch Rebar Renfort de colonnes*

4\. Sélectionnez le type de ferraillage souhaité.
5. Donnez des entrées pour les données relatives aux cadres.
6. Cliquez sur **Next** et la boîte de dialogue sera mise à jour comme indiqué ci-dessous.
<img alt="" src=images/ColumnReinforcementDialog_MainRebars.png  style="width:700px;">
*Boîte de dialogue pour les données des barres principales*

7\. Sélectionnez le type de barres souhaitées et remplissez les données pour les barres principales.
8. Cliquez sur **Next** et la boîte de dialogue sera mise à jour comme indiqué ci-dessous.
<img alt="" src=images/ColumnReinforcementDialog_XDirRebars.png  style="width:700px;">
*Boîte de dialogue pour les données selon la direction X des armatures*

9\. Sélectionnez le type d\'armatures souhaitées et remplissez les données pour les armatures de direction X.
10. Cliquez sur **Next** et la boîte de dialogue sera mise à jour comme indiqué ci-dessous.
<img alt="" src=images/ColumnReinforcementDialog_YDirRebars.png  style="width:700px;">
*Boîte de dialogue pour les données selon la direction Y des armatures*

7\. Sélectionnez le type d\'armatures souhaitées et remplissez les données pour les armatures de direction Y.
8. Cliquez sur **OK** ou **Apply** pour générer un renforcement de colonne.
9. Cliquez sur **Cancel** pour quitter la boîte de dialogue.


## Propriétés

**Etriers:**

-    {{PropertyData/fr|Left Cover}}: distance entre l\'extrémité gauche de l\'étrier et la face gauche de la structure.

-    {{PropertyData/fr|Right Cover}}: distance entre l\'extrémité droite de l\'étrier et la face droite de la structure.

-    {{PropertyData/fr|Top Cover}}: distance séparant la liaison de la face supérieure de la structure.

-    {{PropertyData/fr|Bottom Cover}}: distance séparant l\'étrier de la face inférieure de la structure.

-    {{PropertyData/fr|Offset}}: distance séparant l\'étrier de la face supérieure/inférieure de la structure.

-    {{PropertyData/fr|Diameter}}: diamètre de l\'étrier.

-    {{PropertyData/fr|Bent Angle}}: l\'angle courbé définit l\'angle aux extrémités de l\'étrier.

-    {{PropertyData/fr|Extension Factor}}: le facteur d\'extension définit la longueur de la fin de l\'étrier, exprimée en nombre de diamètre.

-    {{PropertyData/fr|Number}}: nombre d\'étriers.

-    {{PropertyData/fr|Spacing}}: distance entre les axes de chaque étrier.

**Armatures principales :** barres d\'armature présentes aux coins de l\'étrier

-    {{PropertyData/fr|Rebar Type}}: type d\'armatures principales.

-    {{PropertyData/fr|Hook Orientation}}: orientation du crochet en forme de L.

-    {{PropertyData/fr|Hook Extend Along}}: direction de l\'extension des crochets.

-    {{PropertyData/fr|Hook Extension}}: longueur du crochet des armatures en forme de L.

-    {{PropertyData/fr|Rounding}}: valeur arrondie à appliquer aux coins des barres d\'armature en forme de L, exprimée en nombre de diamètre.

-    {{PropertyData/fr|Top Offset}}: distance entre les barres d\'armature à partir de la face supérieure de la structure.

-    {{PropertyData/fr|Bottom Offset}}: distance entre les barres d\'armature et la face inférieure de la structure.

-    {{PropertyData/fr|Diameter}}: diamètre des armatures principales.

**Barres d\'armature secondaires XDir :** barres d\'armature suivant la direction X sauf les barres d\'armature principales

-    {{PropertyData/fr|Type d'armature}}: type d\'armatures de direction X.

-    {{PropertyData/fr|Hook Orientation}}: Orientation des crochets en forme de L.

-    {{PropertyData/fr|Hook Extension}}: longueur du crochet des armatures en forme de L.

-    {{PropertyData/fr|Rounding}}: valeur arrondie à appliquer aux coins des barres d\'armature en forme de L, exprimée en nombre de diamètre.

-    {{PropertyData/fr|Top Offset}}: distance entre les barres d\'armature à partir de la face supérieure de la structure.

-    {{PropertyData/fr|Bottom Offset}}: distance entre les barres d\'armature et la face inférieure de la structure.

-    {{PropertyData/fr|Number#Diameter}}: Number#Diameter ensemble des armatures dans la direction X.

**Barres d\'armature secondaires YDir :** barres d\'armature suivant la direction Y sauf les barres d\'armature principales

-    {{PropertyData/fr|Type d'armature}}: type d\'armatures de direction y.

-    {{PropertyData/fr|Hook Orientation}}: orientation des crochets en forme de L.

-    {{PropertyData/fr|Hook Extension}}: longueur du crochet des armatures en forme de L.

-    {{PropertyData/fr|Rounding}}: valeur arrondie à appliquer aux coins des barres d\'armature en forme de L, exprimée en nombre de diamètre.

-    {{PropertyData/fr|Top Offset}}: distance entre les barres d\'armature à partir de la face supérieure de la structure.

-    {{PropertyData/fr|Bottom Offset}}: distance entre les barres d\'armature et la face inférieure de la structure.

-    {{PropertyData/fr|Number#Diameter}}: Number#Diameter ensemble des armatures dans la direction Y.



## Script


**Voir aussi :**

[Arch API](Arch_API/fr.md), [API de renforts](Reinforcement_API/fr.md) et [FreeCAD Scripts de Base](FreeCAD_Scripting_Basics/fr.md).

L'outil Renfort de colonne (ColumnReinforcement) peut être utilisé dans une [macros](Macros/fr.md) et dans la console [Python](Python/fr.md) en utilisant la fonction suivante :



### Création d\'un seul cadre pour quatre armatures 


```python
RebarGroup = makeSingleTieFourRebars(
    l_cover_of_tie,
    r_cover_of_tie,
    t_cover_of_tie,
    b_cover_of_tie,
    offset_of_tie,
    bent_angle,
    extension_factor,
    dia_of_tie,
    number_spacing_check,
    number_spacing_value,
    dia_of_rebars,
    t_offset_of_rebars,
    b_offset_of_rebars,
    rebar_type="StraightRebar",
    hook_orientation="Top Inside",
    hook_extend_along="x-axis",
    l_rebar_rounding=None,
    hook_extension=None,
    structure=None,
    facename=None,
).rebar_group

```

-   Crée un objet `RebarGroup` à partir de la `structure` donnée, qui est une [Arch Structure](Arch_Structure/fr.md), et de `facename`, qui est une face de cette structure.
    -   Si ni `structure` ni `facename` n\'est donné, la face sélectionnée par l\'utilisateur sera entrée.

-    `l_cover_of_tie`, `r_cover_of_tie`, `t_cover_of_tie`, `b_cover_of_tie` et `offset_of_tie` sont les distances de décalage intérieures des éléments d\'ancrage par rapport aux faces de la structure. Ce sont respectivement les décalages gauche, droit, haut, bas et avant/arrière.

-    `bent_angle`définit l\'angle de la pointe de la boucle de l\'armature.

-    `extension_factor`définit la longueur de la pointe de la boucle de l\'armature, exprimée en nombre de diamètre.

-    `dia_of_tie`est le diamètre des étriers.

-    `number_spacing_check`s\'il est `True`, il créera autant d\'étriers que ceux donnés par `number_spacing_value`; s\'il s\'agit de `False`, il créera des étriers séparés par la valeur numérique de `number_spacing_value`.

-    `number_spacing_spue`spécifie le nombre d\'étriers, ou la valeur de la séparation entre eux, en fonction de `number_spacing_check`.

-    `dia_of_rebars`est le diamètre des armatures principales.

-    `t_offset_of_rebars`et `b_offset_of_rebars` sont des distances de décalage internes pour les armatures principales par rapport aux faces supérieure et inférieure de la structure, respectivement.

-    {{incode | rebar_type}}est le type des armatures principales. il peut s\'agir de `"StraightRebar"` ou de `"LShapeRebar"`.

-    `hook_orientation`spécifie l\'orientation du crochet en forme de L; il peut s\'agir de: `"Top Inside"`, `"Top Outside"`, `"Bottom Inside"`, `"Bottom Outside"`, `"Top Right"`, `"Top Left"`, `"Bottom Right"` or `"Bottom Left"`.

-    `hook_extend_along`spécifie la direction de l\'extension du crochet; il peut s\'agir de `"x-axis"` ou `"y-axis"`.

-    `l_rebar_rounding`est le paramètre qui détermine le rayon de courbure des armatures principales en forme de L, exprimé en fois le diamètre.

-    `hook_extension`est la longueur du crochet des barres d\'armature en forme de L.



#### Exemple


```python
import FreeCAD, Draft, Arch
from ColumnReinforcement import SingleTie

# Cela ne fonctionne pas si la structure n'est pas basée sur une face.
# Structure = Arch.makeStructure(length=1000, width=400, height=400)

Rect = Draft.makeRectangle(400, 400)
Structure = Arch.makeStructure(Rect, height=1600)
Structure.ViewObject.Transparency = 80
FreeCAD.ActiveDocument.recompute()

# Pour les armatures droites

RebarGroup = SingleTie.makeSingleTieFourRebars(
    l_cover_of_tie=40,        
    r_cover_of_tie=40,
    t_cover_of_tie=40,
    b_cover_of_tie=40,
    offset_of_tie=100,
    bent_angle=135,
    extension_factor=2,
    dia_of_tie=8,
    number_spacing_check=True,
    number_spacing_value=10,
    dia_of_rebars=16,
    t_offset_of_rebars=40,
    b_offset_of_rebars=40,
    rebar_type="StraightRebar",
    hook_orientation="Top Inside",
    hook_extend_along="x-axis",
    l_rebar_rounding=None,
    hook_extension=None,
    structure=Structure,
    facename="Face6",
).rebar_group

# Pour barres de renfort en forme de L avec le crochet dirigé le long de l'axe des x.

RebarGroup = SingleTie.makeSingleTieFourRebars(
    l_cover_of_tie=40,        
    r_cover_of_tie=40,
    t_cover_of_tie=40,
    b_cover_of_tie=40,
    offset_of_tie=100,
    bent_angle=135,
    extension_factor=2,
    dia_of_tie=8,
    number_spacing_check=True,
    number_spacing_value=10,
    dia_of_rebars=16,
    t_offset_of_rebars=-40,
    b_offset_of_rebars=-40,
    rebar_type="LShapeRebar",
    hook_orientation="Top Outside",
    hook_extend_along="x-axis",
    l_rebar_rounding=2,
    hook_extension=40,
    structure=Structure,
    facename="Face6",
).rebar_group

# Pour barres de renfort en forme de L avec le crochet dirigé le long de l'axe des y.

RebarGroup = SingleTie.makeSingleTieFourRebars(
    l_cover_of_tie=40,        
    r_cover_of_tie=40,
    t_cover_of_tie=40,
    b_cover_of_tie=40,
    offset_of_tie=100,
    bent_angle=135,
    extension_factor=2,
    dia_of_tie=8,
    number_spacing_check=True,
    number_spacing_value=10,
    dia_of_rebars=16,
    t_offset_of_rebars=-40,
    b_offset_of_rebars=-40,
    rebar_type="LShapeRebar",
    hook_orientation="Top Outside",
    hook_extend_along="y-axis",
    l_rebar_rounding=2,
    hook_extension=40,
    structure=Structure,
    facename="Face6",
).rebar_group

```



### Création d\'un seul cadre pour plusieurs armatures 


```python
RebarGroup = makeSingleTieMultipleRebars(
    l_cover_of_tie,
    r_cover_of_tie,
    t_cover_of_tie,           
    b_cover_of_tie,                      
    offset_of_tie,                       
    bent_angle,                          
    extension_factor,
    dia_of_tie,     
    number_spacing_check,
    number_spacing_value,
    dia_of_main_rebars,
    main_rebars_t_offset,
    main_rebars_b_offset,
    main_rebars_type="StraightRebar",
    main_hook_orientation="Top Inside",
    main_hook_extend_along="x-axis",
    l_main_rebar_rounding=None,
    main_hook_extension=None,
    sec_rebars_t_offset=None,
    sec_rebars_b_offset=None,
    sec_rebars_number_diameter=None,
    sec_rebars_type=("StraightRebar", "StraightRebar"),
    sec_hook_orientation=("Top Inside", "Top Inside"),
    l_sec_rebar_rounding=None,
    sec_hook_extension=None,
    structure=None,
    facename=None,
)

```

-   Crée un objet `RebarGroup` à partir de la `structure` donnée, qui est une [Arch Structure](Arch_Structure/fr.md), et de `facename`, qui est une face de cette structure.
    -   Si ni `structure` ni `facename` ne sont donnés, la face sélectionnée par l\'utilisateur sera entrée.

-    `l_cover_of_tie`, `r_cover_of_tie`, `t_cover_of_tie`, `b_cover_of_tie` et `offset_of_tie` sont les distances de décalage intérieures entre les éléments d\'ancrage et les faces de la structure. Il s\'agit respectivement des décalages gauche, droit, supérieur, inférieur et avant/arrière..

-    `bent_angle`définit l\'angle de la pointe de la boucle de l\'armature.

-    `extension_factor`définit la longueur de la pointe de la boucle de l\'armature, exprimée en nombre de diamètre.

-    `dia_of_tie`est le diamètre des étriers.

-    `number_spacing_check`en position `True`, il créera autant d\'étriers que ceux donnés par `number_spacing_value`. Mis à `False`, il créera des étriers séparés par la valeur numérique de `number_spacing_value`.

-    `number_spacing_spue`spécifie le nombre des étriers, ou la valeur de la séparation entre eux, en fonction de `number_spacing_check`.

-    `dia_of_main_rebars`est le diamètre des armatures principales.

-    `main_rebars_t_offset`et `main_rebars_b_offset` sont des distances de décalage internes pour les armatures principales par rapport aux faces supérieure et inférieure de la structure, respectivement.

-    `main_rebars_type`est le type des armatures principales. Il peut s\'agir de `"StraightRebar"` ou de `"LShapeRebar"`.

-    `main_hook_orientation`spécifie l\'orientation du crochet principal de forme L. Il peut s\'agir de: `"Top Inside"`, `"Top Outside"`, `"Bottom Inside"`, `"Bottom Outside"`, {{ incode\|\"En haut à droite\"}}, `"En haut à gauche"`, `"En bas à droite"` ou `"En bas à gauche"`.

-    `main_hook_extend_along`spécifie la direction de l\'extension du crochet principal. Il peut s\'agir de `"axe x"` ou de `"axe y"`.

-    `l_main_rebar_rebar_rounding`est le paramètre qui détermine le rayon de courbure des barres d\'armature principales en forme de LS, exprimé en nombre de diamètre.

-    `main_hook_extension`est la longueur du crochet des barres d\'armature principales en L.

-    `sec_rebars_t_offset`et `sec_rebars_b_offset` sont respectivement des tuples (xdir_rebars_t\_offset, ydir_rebars_t\_offset) et (xdir_rebars_b\_offset, ydir_rebars_b\_offset), qui définit les distances de décalage intérieures des barres d\'armature secondaires à axe des x et à axe des y par rapport aux faces supérieure et inférieure de la structure, respectivement.

-    `sec_rebars_number_diameter`est un tuple (xdir_rebars_number_diameter, ydir_rebars_number_diameter) qui définit l\'ensemble nombre#diamètre des armatures secondaires des directions x et y, respectivement.

-    `sec_rebars_type`est un tuple (xdir_rebars_type, ydir_rebars_type) qui définit le type de barres d\'armature secondaires en direction x et en direction y, respectivement. Il peut prendre pour valeur `"StraightRebar"` ou `"LShapeRebar"` comme type de barre.

-    `sec_hook_orientation`est un tuple (xdir_hook_orientation, ydir_hook_orientation) qui définit l\'orientation de la direction secondaire x et de la direction y du crochet en L. Il peut prendre pour valeur `"Top Inside"`, `"Top Outside"`, `"Bottom Inside"`, `"Bottom Outside"`, `"Bottom Outside"`, `"Top Right"`, `"Top Left"`, `"Bottom Left"`.

-    `l_sec_rebar_rounding`est un tuple (l_xdir_rebar_rounding, l_ydir_rebar_rounding) qui détermine le rayon de courbure des barres d\'armature secondaires en X et en Y en forme de L, exprimé en nombre de diamètre des barres en L en direction x et y respectivement.

-    `sec_hook_extension`est un tuple (xdir_hook_extension, ydir_hook_extension) qui définit la longueur du crochet des armatures secondaires en forme de L en direction x et y.



#### Exemple 


```python
import FreeCAD, Draft, Arch
from ColumnReinforcement import SingleTieMultipleRebars

# Cela ne fonctionne pas si la structure n'est pas basée sur une face.
# Structure = Arch.makeStructure(length=1000, width=400, height=400)

Rect = Draft.makeRectangle(400, 400)
Structure = Arch.makeStructure(Rect, height=1600)
Structure.ViewObject.Transparency = 80
FreeCAD.ActiveDocument.recompute()

RebarGroup = SingleTieMultipleRebars.makeSingleTieMultipleRebars(
    l_cover_of_tie=40,        
    r_cover_of_tie=40,
    t_cover_of_tie=40,
    b_cover_of_tie=40,
    offset_of_tie=100,
    bent_angle=135,
    extension_factor=2,
    dia_of_tie=8,
    number_spacing_check=True,
    number_spacing_value=10,
    dia_of_main_rebars=16,
    main_rebars_t_offset=-40,
    main_rebars_b_offset=-40,
    main_rebars_type="LShapeRebar",
    main_hook_orientation="Top Outside",
    main_hook_extend_along="x-axis",
    l_main_rebar_rounding=2,
    main_hook_extension=40,
    sec_rebars_t_offset=(-40, -40),
    sec_rebars_b_offset=(-40, -40),
    sec_rebars_number_diameter=("2#20mm+1#16mm+2#20mm", "1#20mm+1#16mm+1#20mm"),
    sec_rebars_type=("LShapeRebar", "LShapeRebar"),
    sec_hook_orientation=("Top Outside", "Top Outside"),
    l_sec_rebar_rounding=(2, 2),
    sec_hook_extension=(40, 40),
    structure=Structure,
    facename="Face6",
)

```

### Édition d\'un seul étrier pour quatre armatures 

Vous pouvez modifier les propriétés des étriers et des armatures avec la fonction suivante:


```python
rebar_group = editSingleTieFourRebars(
    rebar_group,
    l_cover_of_tie,
    r_cover_of_tie,    
    t_cover_of_tie,           
    b_cover_of_tie,
    offset_of_tie,
    bent_angle,
    extension_factor,
    dia_of_tie,
    number_spacing_check,
    number_spacing_value,
    dia_of_rebars,
    t_offset_of_rebars,
    b_offset_of_rebars,
    rebar_type="StraightRebar",
    hook_orientation="Top Inside",
    hook_extend_along="x-axis",
    l_rebar_rounding=None,
    hook_extension=None,
    structure=None,
    facename=None,
)

```

-    `rebar_group`est un objet de groupe `ColumnReinforcement` créé précédemment.

-   Les autres paramètres sont les mêmes que ceux requis par la fonction `makeSingleTieFourRebars()`.

-    `structure`et `facename` peuvent être omis afin que l\'armature reste dans la structure d\'origine.



#### Exemple 


```python
from ColumnReinforcement import SingleTie

rebar_group = SingleTie.editSingleTieFourRebars(
    rebar_group,                                
    l_cover_of_tie=40,        
    r_cover_of_tie=40,
    t_cover_of_tie=40,
    b_cover_of_tie=40,
    offset_of_tie=100,
    bent_angle=135,
    extension_factor=2,
    dia_of_tie=8,
    number_spacing_check=True,
    number_spacing_value=10,
    dia_of_rebars=16,
    t_offset_of_rebars=-40,
    b_offset_of_rebars=-40,
    rebar_type="LShapeRebar",
    hook_orientation="Top Outside",
    hook_extend_along="x-axis",
    l_rebar_rounding=2,
    hook_extension=40,
    structure=None,
    facename=None,
)

```

### Édition d\'un seul étrier pour plusieurs armatures 

Vous pouvez modifier les propriétés des étriers et des armatures avec la fonction suivante:


```python
rebar_group = editSingleTieMultipleRebars(
    rebar_group,
    l_cover_of_tie,      
    r_cover_of_tie,       
    t_cover_of_tie,                       
    b_cover_of_tie,                       
    offset_of_tie,                        
    bent_angle,
    extension_factor,
    dia_of_tie,
    number_spacing_check,
    number_spacing_value,
    dia_of_main_rebars,
    main_rebars_t_offset,
    main_rebars_b_offset,
    main_rebars_type="StraightRebar",
    main_hook_orientation="Top Inside",
    main_hook_extend_along="x-axis",
    l_main_rebar_rounding=None,
    main_hook_extension=None,
    sec_rebars_t_offset=None,
    sec_rebars_b_offset=None,
    sec_rebars_number_diameter=None,
    sec_rebars_type=("StraightRebar", "StraightRebar"),
    sec_hook_orientation=("Top Inside", "Top Inside"),
    l_sec_rebar_rounding=None,
    sec_hook_extension=None,
    structure=None,
    facename=None,
)

```

-    `rebar_group`est un objet de groupe `ColumnReinforcement` créé précédemment.

-   Les autres paramètres sont les mêmes que ceux requis par la fonction `makeSingleTieFourRebars()`.

-    `structure`et `facename` peuvent être omis afin que l\'armature reste dans la structure d\'origine.



#### Exemple 


```python
from ColumnReinforcement import SingleTieMultipleRebars

rebar_group = SingleTieMultipleRebars.editSingleTieMultipleRebars(
    rebar_group,                                
    l_cover_of_tie=40,        
    r_cover_of_tie=40,
    t_cover_of_tie=40,
    b_cover_of_tie=40,
    offset_of_tie=100,
    bent_angle=135,
    extension_factor=2,
    dia_of_tie=8,
    number_spacing_check=True,
    number_spacing_value=10,
    dia_of_main_rebars=16,
    main_rebars_t_offset=-40,
    main_rebars_b_offset=-40,
    main_rebars_type="LShapeRebar",
    main_hook_orientation="Top Outside",
    main_hook_extend_along="x-axis",
    l_main_rebar_rounding=2,
    main_hook_extension=40,
    sec_rebars_t_offset=(-40, -40),
    sec_rebars_b_offset=(-40, -40),
    sec_rebars_number_diameter=("2#20mm+1#16mm+2#20mm", "1#20mm+1#16mm+1#20mm"),
    sec_rebars_type=("StraightRebar", "StraightRebar"),
    sec_hook_orientation=None,
    l_sec_rebar_rounding=None,
    sec_hook_extension=None,
    structure=None,
    facename=None,
)
```



---
⏵ [documentation index](../README.md) > [Reinforcement](Category_Reinforcement.md) > [Arch](Arch_Workbench.md) > Arch Rebar ColumnReinforcement/fr
