---
 GuiCommand:
   Name: Reinforcement SlabRebars
   Name/fr: Reinforcement Armature de dalle
   MenuLocation: 3D/BIM , Outils pour les armatures , Armature de dalle 
   Workbenches: BIM_Workbench/fr, Reinforcement_Workbench/fr
   SeeAlso: 
---

# Reinforcement SlabRebars/fr

## Description

L\'outil [Armature de dalle](Reinforcement_SlabRebars/fr.md) permet à l\'utilisateur de créer des armatures à l\'intérieur d\'un objet dalle de [Arch Structure](Arch_Structure/fr.md).

Cet outil fait partie de l\'[atelier Reinforcement](Reinforcement_Workbench/fr.md), un [atelier externe](External_workbenches/fr.md) qui peut être installé avec le <img alt="" src=images/Std_AddonMgr.svg  style="width:24px;"> [gestionnaire des extensions](Std_AddonMgr/fr.md).

<img alt="" src=images/Isometric_view_of_Bent_Shape_rebars_in_parallel_and_cross_direction_with_distribution_rebars.png  style="width:600px;"> 
*Un exemple d'armature de dalle à l'intérieur d'une dalle de [Arch Structure](Arch_Structure/fr.md)*

<img alt="" src=images/Right_view_of_Bent_Shape_rebars_in_parallel_and_cross_direction_with_distribution_rebars.png  style="width:600px;"> 
*Vue de droite de l'exemple de l'armature de dalle*

<img alt="" src=images/Front_view_of_Bent_Shape_rebars_in_parallel_and_cross_direction_with_distribution_rebars.png  style="width:600px;"> 
*Vue de face de l'exemple de l'armature de dalle*



## Utilisation

1\. Sélectionnez n\'importe quelle face d\'une dalle **<img src="images/Arch_Structure.svg" width=16px> [Arch Structure](Arch_Structure/fr.md)** déjà créée comme indiqué dans l\'image ci-dessous.

:   <img alt="" src=images/Selected_face_for_Slab_Arch_Structure.png  style="width:400px;">

:   
    
*Face sélectionnée de la dalle de Arch Structure*.

2\. Sélectionnez ensuite **<img src="images/Reinforcement_SlabRebars.svg" width=16px> [Armature de dalle](Reinforcement_SlabRebars/fr.md)** dans les outils d\'armature.

3\. Une boîte de dialogue apparaîtra à l\'écran, comme indiqué ci-dessous.

:   <img alt="" src=images/Slab_Reinforcement_input_dialog_box.png  style="width:600px;">

:   
    
*Boîte de dialogue pour de l'armature de dalle*
    

4\. Sélectionnez le type de couverture du maillage de l\'armature souhaité (Dessus ou Dessous).

5\. Sélectionnez le type d\'armature souhaité et les autres données d\'entrée pour les armatures dans la direction parallèle à la face sélectionnée, comme le montre l\'image ci-dessous.

:   <img alt="" src=images/Bent_Shape_rebars_in_parallel_with_distribution_rebars_inputs_for_Slab_Reinforcement.png  style="width:600px;">

:   
    
*Boîte de dialogue pour des armatures de la dalle en direction parallèle de la face sélectionnée*.

6\. Cliquez maintenant sur **Suivant** ou sélectionnez Cross Rebars dans la liste.

7\. Maintenant, sélectionnez les données souhaitées pour les données d\'entrée pour les armatures dans la direction transversale de la face sélectionnée comme le montre l\'image ci-dessous.

:   <img alt="" src=images/Bent_Shape_rebars_in_cross_direction_with_distribution_rebars.png  style="width:600px;">

:   
    
*Boîte de dialogue pour des armatures de la dalle en direction transversale de la face sélectionnée*.

8\. Cliquez sur **OK** ou **Appliquer** ou **Terminer** pour générer l\'armature de la dalle.

9\. Cliquez sur **Annuler** pour quitter la fenêtre de dialogue.


## Propriétés

**Propriétés des armatures dans la direction parallèle à la face sélectionnée :**

-    **Mesh Cover Along**: représente l\'alignement du maillage de armatures le long de la face supérieure ou inférieure de la structure. Peut prendre deux valeurs : \"Top\" et \"Bottom\".

-    **Rebar Type**: type d\'armature pour les armatures parallèles pour l\'aramture de la dalles. Peut prendre quatre valeurs : \"StraightRebar\", \"LShapeRebar\", \"UShapeRebar\", \"BentShapeRebar\".

-    **Couverture avant**: distance entre l\'armature parallèle et la face sélectionnée.

-    **Left Cover**: distance entre l\'extrémité gauche de l\'armature parallèle et la face gauche de la structure.

-    **Right Cover**: distance entre l\'extrémité droite de l\'armature parallèle et la face droite de la structure.

-    **Bottom Cover**: distance entre les armatures parallèles et la face inférieure de la structure.

-    **Top Cover**: distance entre les armatures parallèles à partir de la face supérieure de la structure.

-    **Rear Cover**: couverture arrière pour l\'armature de la dalle des armatures parallèles.

-    **Anchor Length**: représente la longueur du bras de l\'armature parallèle pliée lorsque le type d\'armature parallèle est BentShapeRebar.

-    **Bent Angle**: représente l\'angle de l\'armature parallèle pliée lorsque le type d\'armature parallèle est BentShapeRebar.

-    **Rounding**: valeur d\'arrondi à appliquer aux coins des armatures, exprimée en fois le diamètre des barres d\'armature parallèles.

-    **Diameter**: diamètre des armature parallèles

-    **Amount**: nombre d\'armatures parallèles.

-    **Spacing**: espacement entre les armatures parallèles.

**Propriétés des armatures de distribution pour les armatures de forme pliée en direction parallèle à la face sélectionnée :**

-    **Amount**: nombre d\'armatures de distribution pour les armatures pliées en parallèle.

-    **Spacing**: espacement entre les armatures de distribution pour les armatures pliées en direction parallèle.

**Propriétés des armatures dans le sens transversal de la face sélectionnée :**

-    **Rebar Type**: type d\'armature pour les armatures transversales pour l\'armature des dalles. Peut prendre quatre valeurs : \"StraightRebar\", \"LShapeRebar\", \"UShapeRebar\", \"BentShapeRebar\".

-    **Front Cover**: distance entre l\'armature transversale et la face sélectionnée.

-    **Left Cover**: distance entre l\'extrémité gauche de l\'armature transversale et la face gauche de la structure.

-    **Right Cover**: distance entre l\'extrémité droite de l\'armature transversale et la face droite de la structure.

-    **Bottom Cover**: distance entre les armatures transversales et la face inférieure de la structure.

-    **Top Cover**: distance entre les armatures transversales depuis la face supérieure de la structure.

-    **Rear Cover**: couverture arrière pour l\'armature de la dalle des armatures transversales.

-    **Anchor Length**: représente la longueur du bras de l\'armature transversale pliée lorsque le type d\'armature transversale est BentShapeRebar.

-    **Bent Angle**: représente l\'angle de l\'armature transversale pliée lorsque le type d\'armature transversale est BentShapeRebar.

-    **Rounding**: valeur d\'arrondi à appliquer aux coins des armatures, exprimée en fois le diamètre des armatures transversales.

-    **Diameter**: diamètre des armatures transversales

-    **Amount**: nombre d\'armatures transversales.

-    **Spacing**: espacement entre les armatures transversales.

**Propriétés des armatures de distribution pour les armatures pliées dans le sens transversal par rapport à la face sélectionnée :**

-    **Amount**: nombre d\'armatures de distribution pour les armatures pliées dans le sens transversal.

-    **Spacing**: espacement entre les armatures de distribution pour les armatures pliées dans le sens transversal.



## Script


**Voir aussi :**

[Arch API](Arch_API/fr.md), [Reinforcement API](Reinforcement_API/fr.md) et [FreeCAD Débuter avec les scripts](FreeCAD_Scripting_Basics/fr.md).

L\'outil Armature de dalle peut être utilisé à partir de la console [Python](Python/fr.md) en utilisant la fonction suivante :



### Créer une armature de dalle 


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

-   Crée un objet `SlabReinforcementGroup` à partir des données `structure`, qui est une dalle de [Arch Structure](Arch_Structure/fr.md) et `facename`, qui est une face de cette structure.
    -   Si ni `structure` ni `facename` ne sont donnés, il prendra en entrée la face sélectionnée par l\'utilisateur.

**Propriétés des armatures dans la direction parallèle à la face sélectionnée :**

-    **parallel_rebar_type**: type d\'armature pour les armatures parallèles pour l\'armature de la dalle. Peut prendre quatre valeurs : \"StraightRebar\", \"LShapeRebar\", \"UShapeRebar\", \"BentShapeRebar\".

-    **parallel_front_cover**: distance entre l\'armature parallèle et la face sélectionnée.

-    **parallel_rear_cover**: face arrière pour l\'armature de la dalle des armatures parallèles.

-    **parallel_left_cover**: distance entre l\'extrémité gauche de l\'armature parallèle et la face gauche de la structure.

-    **parallel_right_cover**: distance entre l\'extrémité droite de l\'armature parallèle et la face droite de la structure.

-    **parallel_top_cover**: distance entre les armatures parallèles et la face supérieure de la structure.

-    **parallel_bottom_cover**: distance entre les armatures parallèles à partir de la face inférieure de la structure.

-    **parallel_diameter**: distance des armatures parallèles.

-    **parallel_amount_spacing_check**: si True, alors la valeur de parallel_amount_spacing_value est utilisée comme nombre d\'armatures, sinon la valeur de parallel_amount_spacing_value est utilisée comme espacement dans les armatures parallèles.

-    **parallel_amount_spacing_value**: nombre d\'armatures ou l\'espacement entre les armatures parallèles en fonction de la valeur de amount_spacing_check.

-    **parallel_rounding**: valeur d\'arrondi à appliquer aux coins des armatures, exprimée en fois parallel_diameter.

-    **parallel_bent_bar_length**: représente la longueur du bras de l\'armature parallèle pliée lorsque le type d\'armature parallèle est BentShapeRebar.

-    **parallel_bent_bar_angle**: représente l\'angle de l\'armature parallèle pliée lorsque parallel_rebar_type est BentShapeRebar.

-    **parallel_l_shape_hook_orintation**: représente l\'orientation du crochet de la barre d\'armature parallèle en forme de L si le type de barre parallèle est LShapeRebar. Il peut avoir trois valeurs : \"Left\", \"Right\", \"Alternate\".

-    **parallel_distribution_rebars_check**: si True, ajoute des armatures de distribution pour les armatures de forme pliées parallèles. La valeur par défaut est False.

-    **parallel_distribution_rebars_diameter**: diamètre des armatures de distribution pour les armatures parallèles pliées.

-    **parallel_distribution_rebars_amount_spacing_check**: si True, alors la valeur de parallel_distribution_rebars_amount_spacing_value est utilisée comme nombre d\'armatures, sinon la valeur de parallel_distribution_rebars_amount_spacing_value est utilisée comme espacement dans parallel_distribution_rebars. La valeur par défaut est True.

-    **parallel_distribution_rebars_amount_spacing_value**: nombre ou l\'espacement entre les armatures de distribution pour un côté des armatures parallèles pliées en fonction de la valeur de parallel_distribution_rebars_check. La valeur par défaut est 2.

**Propriétés des armatures dans le sens transversal de la face sélectionnée :**

-    **cross_rebar_type**: type d\'armature pour les armatures transversales pour l\'armature de la dalle. Peut prendre quatre valeurs : \"StraightRebar\", \"LShapeRebar\", \"UShapeRebar\", \"BentShapeRebar\".

-    **cross_front_cover**: distance entre l\'armature transversale et la face transversale (face perpendiculaire à la face sélectionnée).

-    **cross_rear_cover**: face arrière pour l\'armature de la dalle des armatures transversales.

-    **cross_left_cover**: distance entre l\'extrémité gauche de l\'armature transversale et la face gauche de la structure.

-    **cross_right_cover**: distance entre l\'extrémité droite d\'armature et la face droite de la structure par rapport à la face transversale.

-    **cross_top_cover**: distance entre l\'armature transversale et la face supérieure de la structure.

-    **cross_bottom_cover**: distance entre les armatures transversales de la face inférieure de la structure.

-    **cross_diameter**: diamètre des armatures transversales.

-    **cross_amount_spacing_check**: si True, la valeur de cross_amount_spacing_value est utilisée comme nombre d\'armatures, sinon la valeur de cross_amount_spacing_value est utilisée comme espacement entre les armatures.

-    **cross_amount_spacing_value**: nombre d\'armatures ou l\'espacement entre les armatures en fonction de la valeur de cross_amount_spacing_check.

-    **cross_rounding**: valeur d\'arrondi à appliquer aux coins des armatures, exprimée en fois cross_diameter.

-    **cross_bent_bar_length**: représente la longueur du bras de l\'armature transversale pliée lorsque le type d\'armature transversale est BentShapeRebar.

-    **cross_bent_bar_angle**: représente l\'angle de l\'armature transversale pliée lorsque le type d\'armature transversale est BentShapeRebar.

-    **cross_l_shape_hook_orintation**: représente l\'orientation du crochet d\'armature transversale en forme de L si le type d\'armature transversale est LShapeRebar. Peut prendre trois valeurs : \"Left\", \"Right\", \"Alternate\".

-    **cross_distribution_rebars_check**: si True, ajoute des armatures de distribution pour les armatures de forme pliées en croix. La valeur par défaut est False.

-    **cross_distribution_rebars_diameter**: diamètre des armatures de distribution pour les armatures pliées en croix.

-    **cross_distribution_rebars_amount_spacing_check**: di True, alors la valeur de cross_distribution_rebars_amount_spacing_value est utilisée comme nombre de barres, sinon la valeur de cross_distribution_rebars_amount_spacing_value est utilisée comme espacement dans cross_distribution_rebars. La valeur par défaut est True.

-    **cross_distribution_rebars_amount_spacing_value**: nombre ou l\'espacement entre les armatures de distribution pour un côté des armatures de forme pliée en croix en fonction de la valeur de cross_distribution_rebars_check. La valeur par défaut est 2.

**Propriétés communes aux armatures parallèles et transversales :**

-    **mesh_cover_along**: peut avoir deux valeurs \"Top\" et \"Bottom\". Représente l\'alignement des mailles d\'armature le long de la face supérieure ou inférieure de la structure.

-    **structure**: objet de structure de Arch. La valeur par défaut est None.

-    **facename**: face sélectionnée de la structure. La valeur par défaut est None.



### Éditer l\'armature de la dalle 

Vous pouvez modifier les propriétés de l\'armature de la dalle à l\'aide de la fonction suivante :


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



### Exemples d\'armature de dalle 

-   [Exemple Dalle s\'étendant dans deux directions](Example_Slab_Spanning_in_Two_Directions/fr.md)

<img alt="" src=images/Isometric_view_of_Bent_Shape_rebars_in_parallel_and_cross_direction_with_distribution_rebars.png  style="width:800px;">

-   [Exemple Dalle s\'étendant dans une direction](Example_Slab_Spanning_in_One_Direction/fr.md)

<img alt="" src=images/Slab_spanning_in_one_Direction.png  style="width:800px;">

-   [Exemple Dalle avec maillage d\'armatures droites](Example_Slab_Having_Mesh_Of_Straight_Rebars/fr.md)

<img alt="" src=images/Slab_having_straight_rebars_in_both_direction.png  style="width:800px;">

-   [Exemple Dalle avec armatures en forme de U](Example_Slab_Having_UShape_Rebars_Reinforcement_Mesh/fr.md)

<img alt="" src=images/U-shape_rebars_isometric_view.png  style="width:800px;">

-   [Exemple Dalle avec armatures en forme de L](Example_Slab_Having_LShape_Rebars_Reinforcement_Mesh/fr.md)

<img alt="" src=images/L-Shape_Rebars_isometric_view.png  style="width:800px;">



---
⏵ [documentation index](../README.md) > [External_Command_Reference](Category_External_Command_Reference.md) > [Reinforcement](Category_Reinforcement.md) > [BIM](Category_BIM.md) > Reinforcement SlabRebars/fr
