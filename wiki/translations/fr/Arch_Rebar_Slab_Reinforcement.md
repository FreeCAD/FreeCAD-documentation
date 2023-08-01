---
- GuiCommand:
   Name: Arch Rebar Slab Reinforcement
   Name/fr: Arch Rebar Renfort de dalle
   MenuLocation: Arch - Rebar tools - Slab Reinforcement<br>3D/BIM - Reinforcement tools - Slab 
   Workbenches: [Arch](Arch_Workbench/fr.md)
   SeeAlso: [Reinforcement](Reinforcement_Workbench/fr.md), [Arch Armature personnalisée](Arch_Rebar/fr.md), [Arch Rebar Armature hélicoïdale](Arch_Rebar_Helical/fr.md)
---

# Arch Rebar Slab Reinforcement/fr

## Description

L\'outil [Renfort de dalle](Arch_Rebar_Slab_Reinforcement/fr.md) permet à l\'utilisateur de créer des barres d\'armature à l\'intérieur d\'un objet dalle [Arch Structure](Arch_Structure/fr.md).

Cette commande fait partie de l\'[atelier Reinforcement](Reinforcement_Workbench/fr.md), un [atelier externe](External_workbenches/fr.md) que vous pouvez installer avec le <img alt="" src=images/Std_AddonMgr.svg  style="width:24px;"> [Gestionnaire des extensions](Std_AddonMgr/fr.md) via le menu **Outils → Gestionnaire des extensions → Reinforcement**.

<img alt="" src=images/Isometric_view_of_Bent_Shape_rebars_in_parallel_and_cross_direction_with_distribution_rebars.png  style="width:800px;"> 
*Un exemple de renfort de dalle à l'intérieur d'une dalle [Arch Structure](Arch_Structure/fr.md)*

<img alt="" src=images/Right_view_of_Bent_Shape_rebars_in_parallel_and_cross_direction_with_distribution_rebars.png  style="width:800px;"> 
*Vue de droite de l'exemple de renfort de dalle*

<img alt="" src=images/Front_view_of_Bent_Shape_rebars_in_parallel_and_cross_direction_with_distribution_rebars.png  style="width:800px;"> 
*Vue de face de l'exemple de renfort de dalle*



## Utilisation

1\. Sélectionnez n\'importe quelle face d\'une dalle **<img src="images/Arch_Structure.svg" width=16px> [Arch Structure](Arch_Structure/fr.md)** déjà créée comme indiqué dans l\'image ci-dessous.

<img alt="" src=images/Selected_face_for_Slab_Arch_Structure.png  style="width:400px;"> 
*Face sélectionnée de la dalle Arch Structure*.

2\. Sélectionnez ensuite **<img src="images/Arch_Rebar_Slab_Reinforcement.svg" width=16px> [Slab Reinforcement](Arch_Rebar_Slab_Reinforcement/fr.md)** dans les outils d\'armature.

3\. Une boîte de dialogue apparaîtra à l\'écran comme indiqué ci-dessous.

![](images/Slab_Reinforcement_input_dialog_box.png ) 
*Boîte de dialogue pour le renfort de dalle*.

4\. Sélectionnez le type de couverture de la maille d\'armature souhaité (Dessus ou Dessous).

5\. Sélectionnez le type de barre d\'armature souhaité et les autres données d\'entrée pour les barres d\'armature dans la direction parallèle à la face sélectionnée, comme le montre l\'image ci-dessous.

![](images/Bent_Shape_rebars_in_parallel_with_distribution_rebars_inputs_for_Slab_Reinforcement.png ) 
*Boîte de dialogue pour le renfort de dalle des armatures en direction parallèle de la face sélectionnée*.

6\. Cliquez maintenant sur le bouton **Suivant** ou sélectionnez Cross Rebars dans la liste.

7\. Maintenant, sélectionnez les données souhaitées pour les données d\'entrée pour les barres dans la direction transversale de la face sélectionnée comme le montre l\'image ci-dessous.

![](images/Bent_Shape_rebars_in_cross_direction_with_distribution_rebars.png ) 
*Boîte de dialogue pour le renfort de dalle des armatures dans le sens transversal de la face sélectionnée*.

8\. Cliquez sur **OK** ou **Apply** ou **Finish** pour générer le renfort de dalle.

9\. Cliquez sur **Cancel** pour quitter la boîte de dialogue.


## Propriétés

**Propriétés des barres d\'armature dans la direction parallèle à la face sélectionnée :**

-    **Mesh Cover Along**: représente l\'alignement du maillage de barres d\'armature le long de la face supérieure ou inférieure de la structure. Peut avoir deux valeurs : \"Top\" et \"Bottom\".

-    **Rebar Type**: type de barre d\'armature pour les barres d\'armature parallèles pour le renforcement des dalles. Peut avoir quatre valeurs : \'StraightRebar\', \'LShapeRebar\', \'UShapeRebar\', \'BentShapeRebar\'.

-    **Couverture avant**: distance entre la barre d\'armature parallèle et la face sélectionnée.

-    **Left Cover**: distance entre l\'extrémité gauche de la barre d\'armature parallèle et la face gauche de la structure.

-    **Right Cover**: distance entre l\'extrémité droite de la barre d\'armature parallèle et la face droite de la structure.

-    **Bottom Cover**: distance entre les barres d\'armature parallèles et la face inférieure de la structure.

-    **Top Cover**: distance entre les barres d\'armature parallèles à partir de la face supérieure de la structure.

-    **Rear Cover**: couverture arrière pour le renforcement des dalles de barres d\'armature parallèles.

-    **Anchor Length**: représente la longueur du bras de la barre d\'armature parallèle pliée lorsque le type de barre d\'armature parallèle est BentShapeRebar.

-    **Bent Angle**: représente l\'angle de la barre d\'armature parallèle pliée lorsque le type de barre d\'armature parallèle est BentShapeRebar.

-    **Rounding**: valeur d\'arrondi à appliquer aux coins des barres, exprimée en fois le diamètre des barres d\'armature parallèles.

-    **Diameter**: diamètre des barres d\'armature parallèles

-    **Amount**: nombre de barres d\'armature parallèles.

-    **Spacing**: espacement entre les barres d\'armature parallèles.

**Propriétés des armatures de distribution pour les armatures de forme pliée en direction parallèle à la face sélectionnée :**

-    **Amount**: nombre d\'armatures de distribution pour les armatures pliées en parallèle.

-    **Spacing**: espacement entre les armatures de distribution pour les armatures pliées en direction parallèle.

**Propriétés des barres d\'armature dans le sens transversal de la face sélectionnée :**

-    **Rebar Type**: type de barre d\'armature pour les armatures transversales pour le renforcement des dalles. Peut avoir quatre valeurs : \'StraightRebar\', \'LShapeRebar\', \'UShapeRebar\', \'BentShapeRebar\'.

-    **Front Cover**: distance entre la barre d\'armature transversale et la face sélectionnée.

-    **Left Cover**: distance entre l\'extrémité gauche de la barre d\'armature transversale et la face gauche de la structure.

-    **Right Cover**: distance entre l\'extrémité droite de la barre d\'armature transversale et la face droite de la structure.

-    **Bottom Cover**: distance entre les armatures transversales et la face inférieure de la structure.

-    **Top Cover**: distance entre les barres d\'armature transversales depuis la face supérieure de la structure.

-    **Rear Cover**: couverture arrière pour le renforcement de la dalle des armatures transversales.

-    **Anchor Length**: représente la longueur du bras de l\'armature transversale pliée lorsque le type d\'armature transversale est BentShapeRebar.

-    **Bent Angle**: représente l\'angle de la barre d\'armature transversale pliée lorsque le type de barre d\'armature transversale est BentShapeRebar.

-    **Rounding**: valeur d\'arrondi à appliquer aux coins des barres, exprimée en fois le diamètre des barres d\'armature transversales.

-    **Diameter**: diamètre des armatures transversales

-    **Amount**: nombre d\'armatures transversales.

-    **Spacing**: espacement entre les armatures transversales.

**Propriétés des armatures de distribution pour les armatures pliées dans le sens transversal par rapport à la face sélectionnée :**

-    **Amount**: nombre d\'armatures de distribution pour les armatures pliées dans le sens transversal.

-    **Spacing**: espacement entre les armatures de distribution pour les armatures pliées dans le sens transversal.



## Script


**Voir aussi :**

[Arch API](Arch_API/fr.md), [Reinforcement API](Reinforcement_API/fr.md) et [FreeCAD Scripts de bases](FreeCAD_Scripting_Basics/fr.md).

L\'outil Renfort de dalle peut être utilisé à partir de la console [Python](Python/fr.md) en utilisant la fonction suivante :



### Créer un renfort de dalle 


```python
from SlabReinforcement.SlabReinforcement import makeSlabReinforcement
SlabReinforcementGroup = makeSlabReinforcement(
    parallel_rebar_type,
    parallel_front_cover,
    parallel_rear_cover,
    parallel_left_cover,
    parallel_right_cover,
    parallel_top_cover,
    parallel_bottom_cover,
    parallel_diameter,
    parallel_amount_spacing_check,
    parallel_amount_spacing_value,
    cross_rebar_type,
    cross_front_cover,
    cross_rear_cover,
    cross_left_cover,
    cross_right_cover,
    cross_top_cover,
    cross_bottom_cover,
    cross_diameter,
    cross_amount_spacing_check,
    cross_amount_spacing_value,
    cross_rounding = 2,
    cross_bent_bar_length = 50,
    cross_bent_bar_angle = 135,
    cross_l_shape_hook_orintation = "Alternate",
    cross_distribution_rebars_check = False,
    cross_distribution_rebars_diameter = 8,
    cross_distribution_rebars_amount_spacing_check = True,
    cross_distribution_rebars_amount_spacing_value = 2,
    parallel_rounding = 2,
    parallel_bent_bar_length = 50,
    parallel_bent_bar_angle = 135,
    parallel_l_shape_hook_orintation = "Alternate",
    parallel_distribution_rebars_check = False,
    parallel_distribution_rebars_diameter = 8,
    parallel_distribution_rebars_amount_spacing_check = True,
    parallel_distribution_rebars_amount_spacing_value = 2,
    mesh_cover_along = "Bottom",
    structure = None,
    facename = None,
)
```

-   Crée un objet `SlabReinforcementGroup` à partir des données `structure`, qui est une dalle [Arch Structure](Arch_Structure/fr.md) et `facename`, qui est une face de cette structure.
    -   Si ni `structure` ni `facename` ne sont donnés, il prendra en entrée la face sélectionnée par l\'utilisateur.

**Propriétés des barres d\'armature dans la direction parallèle à la face sélectionnée :**

-    **parallel_rebar_type**: type de barre d\'armature pour les barres d\'armature parallèles pour le renforcement des dalles. Peut avoir quatre valeurs : \'StraightRebar\', \'LShapeRebar\', \'UShapeRebar\', \'BentShapeRebar\'.

-    **parallel_front_cover**: distance entre la barre d\'armature parallèle et la face sélectionnée.

-    **parallel_rear_cover**: face arrière pour le renfort de dalle des armatures parallèles.

-    **parallel_left_cover**: distance entre l\'extrémité gauche de la barre d\'armature parallèle et la face gauche de la structure.

-    **parallel_right_cover**: distance entre l\'extrémité droite de la barre d\'armature parallèle et la face droite de la structure.

-    **parallel_top_cover**: distance entre les barres d\'armature parallèles et la face supérieure de la structure.

-    **parallel_bottom_cover**: distance entre les barres d\'armature parallèles à partir de la face inférieure de la structure.

-    **parallel_diameter**: distance des barres d\'armature parallèles.

-    **parallel_amount_spacing_check**: si True, alors la valeur de parallel_amount_spacing_value est utilisée comme nombre de barres, sinon la valeur de parallel_amount_spacing_value est utilisée comme espacement dans les barres parallèles.

-    **parallel_amount_spacing_value**: nombre d\'armatures ou l\'espacement entre les armatures parallèles en fonction de la valeur de amount_spacing_check.

-    **parallel_rounding**: valeur d\'arrondi à appliquer aux coins des barres, exprimée en fois le parallel_diamètre.

-    **parallel_bent_bar_length**: représente la longueur du bras de la barre d\'armature parallèle pliée lorsque le type de barre parallèle est BentShapeRebar.

-    **parallel_bent_bar_angle**: représente l\'angle de la barre d\'armature parallèle pliée lorsque le type de parallélogramme est BentShapeRebar.

-    **parallel_l_shape_hook_orintation**: représente l\'orientation du crochet de la barre d\'armature parallèle en forme de L si le type de barre parallèle est LShapeRebar. Il peut avoir trois valeurs : \"Left\", \"Right\", \"Alternate\".

-    **parallel_distribution_rebars_check**: si True, ajoute des barres de distribution pour les barres de forme pliées parallèles. La valeur par défaut est False.

-    **parallel_distribution_rebars_diameter**: diamètre des armatures de distribution pour les armatures parallèles pliées.

-    **parallel_distribution_rebars_amount_spacing_check**: si True, alors la valeur de parallel_distribution_rebars_amount_spacing_value est utilisée comme nombre de barres, sinon la valeur de parallel_distribution_rebars_amount_spacing_value est utilisée comme espacement dans parallel_distribution_rebars. La valeur par défaut est True.

-    **parallel_distribution_rebars_amount_spacing_value**: nombre ou l\'espacement entre les armatures de distribution pour un côté des armatures parallèles pliées en fonction de la valeur de parallel_distribution_rebars_check. La valeur par défaut est 2.

**Propriétés des barres d\'armature dans le sens transversal de la face sélectionnée :**

-    **cross_rebar_type**: type d\'armature pour les armatures transversales pour le renforcement des dalles. Peut avoir quatre valeurs : \'StraightRebar\', \'LShapeRebar\', \'UShapeRebar\', \'BentShapeRebar\'.

-    **cross_front_cover**: distance entre l\'armature transversale et la face transversale (face perpendiculaire à la face sélectionnée).

-    **cross_rear_cover**: face arrière pour le renfort de dalle des armatures transversales.

-    **cross_left_cover**: distance entre l\'extrémité gauche de l\'armature transversale et la face gauche de la structure.

-    **cross_right_cover**: distance entre l\'extrémité droite de la barre d\'armature et la face droite de la structure par rapport à la face transversale.

-    **cross_top_cover**: distance entre la barre d\'armature transversale et la face supérieure de la structure.

-    **cross_bottom_cover**: distance entre les barres d\'armature croisées de la face inférieure de la structure.

-    **cross_diameter**: diamètre des barres d\'armature transversales.

-    **cross_amount_spacing_check**: si True, la valeur de cross_amount_spacing_value est utilisée comme nombre de barres, sinon la valeur de cross_amount_spacing_value est utilisée comme espacement entre les barres.

-    **cross_amount_spacing_value**: nombre d\'armatures ou l\'espacement entre les armatures en fonction de la valeur de cross_amount_spacing_check.

-    **cross_rounding**: valeur d\'arrondi à appliquer aux coins des barres, exprimée en fois le cross_diameter.

-    **cross_bent_bar_length**: Représente la longueur du bras de la barre d\'armature transversale pliée lorsque le type de barre transversale est BentShapeRebar.

-    **cross_bent_bar_angle**: représente l\'angle de la barre d\'armature transversale pliée lorsque le type de barre transversale est BentShapeRebar.

-    **cross_l_shape_hook_orintation**: représente l\'orientation du crochet de la barre d\'armature transversale en forme de L si le type de barre transversale est LShapeRebar. Il peut avoir trois valeurs : \"Left\", \"Right\", \"Alternate\".

-    **cross_distribution_rebars_check**: si True, ajoute des barres de distribution pour les barres de forme pliées en croix. La valeur par défaut est False.

-    **cross_distribution_rebars_diameter**: diamètre des armatures de distribution pour les armatures pliées en croix.

-    **cross_distribution_rebars_amount_spacing_check**: di True, alors la valeur de cross_distribution_rebars_amount_spacing_value est utilisée comme nombre de barres, sinon la valeur de cross_distribution_rebars_amount_spacing_value est utilisée comme espacement dans cross_distribution_rebars. La valeur par défaut est True.

-    **cross_distribution_rebars_amount_spacing_value**: nombre ou l\'espacement entre les barres de distribution pour un côté des barres de forme pliée en croix en fonction de la valeur de cross_distribution_rebars_check. La valeur par défaut est 2.

**Propriétés communes aux armatures parallèles et croisées :**

-    **mesh_cover_along**: peut avoir deux valeurs \"Top\" et \"Bottom\". Représente l\'alignement des mailles d\'armature le long de la face supérieure ou inférieure de la structure.

-    **structure**: objet de structure d\'arc. La valeur par défaut est None.

-    **facename**: face sélectionnée de la structure. La valeur par défaut est None.



### Modification du renfort de dalle 

Vous pouvez modifier les propriétés du renfort de dalle à l\'aide de la fonction suivante


```python
from SlabReinforcement.SlabReinforcement import editSlabReinforcement
slabReinforcementGroup = editSlabReinforcement(
    slabReinforcementGroup,
    parallel_rebar_type,
    parallel_front_cover,
    parallel_rear_cover,
    parallel_left_cover,
    parallel_right_cover,
    parallel_top_cover,
    parallel_bottom_cover,
    parallel_diameter,
    parallel_amount_spacing_check,
    parallel_amount_spacing_value,
    cross_rebar_type,
    cross_front_cover,
    cross_rear_cover,
    cross_left_cover,
    cross_right_cover,
    cross_top_cover,
    cross_bottom_cover,
    cross_diameter,
    cross_amount_spacing_check,
    cross_amount_spacing_value,
    cross_rounding = 2,
    cross_bent_bar_length = 50,
    cross_bent_bar_angle = 135,
    cross_l_shape_hook_orintation = "Alternate",
    cross_distribution_rebars_check = False,
    cross_distribution_rebars_diameter = 8,
    cross_distribution_rebars_amount_spacing_check = True,
    cross_distribution_rebars_amount_spacing_value = 2,
    parallel_rounding = 2,
    parallel_bent_bar_length = 50,
    parallel_bent_bar_angle = 135,
    parallel_l_shape_hook_orintation = "Alternate",
    parallel_distribution_rebars_check = False,
    parallel_distribution_rebars_diameter = 8,
    parallel_distribution_rebars_amount_spacing_check = True,
    parallel_distribution_rebars_amount_spacing_value = 2,
    mesh_cover_along: str = "Bottom",
    structure = None,
    facename = None,
)
```

-    `slabReinforcementGroup`est un objet groupe `Slab Reinforcement` préalablement créé.

-   Les autres paramètres sont les mêmes que ceux requis par la fonction `makeSlabReinforcement()`.



### Exemples de renfort de dalle 

-   [Portée des dalles dans deux directions](Example_Slab_Spanning_in_Two_Directions/fr.md)

<img alt="" src=images/Isometric_view_of_Bent_Shape_rebars_in_parallel_and_cross_direction_with_distribution_rebars.png  style="width:800px;">

-   [Portée de la dalle dans une direction](Example_Slab_Spanning_in_One_Direction/fr.md)

<img alt="" src=images/Slab_spanning_in_one_Direction.png  style="width:800px;">

-   [Dalle avec renfort de dalle droite](Example_Slab_Having_Mesh_Of_Straight_Rebars/fr.md)

<img alt="" src=images/Slab_having_straight_rebars_in_both_direction.png  style="width:800px;">

-   [Dalle avec renfort de dalle en forme de U](Example_Slab_Having_UShape_Rebars_Reinforcement_Mesh/fr.md)

<img alt="" src=images/U-shape_rebars_isometric_view.png  style="width:800px;">

-   [Dalle avec renfort de dalle en forme de L](Example_Slab_Having_LShape_Rebars_Reinforcement_Mesh/fr.md)

<img alt="" src=images/L-Shape_Rebars_isometric_view.png  style="width:800px;">



---
⏵ [documentation index](../README.md) > [Reinforcement](Category_Reinforcement.md) > [Arch](Arch_Workbench.md) > Arch Rebar Slab Reinforcement/fr
