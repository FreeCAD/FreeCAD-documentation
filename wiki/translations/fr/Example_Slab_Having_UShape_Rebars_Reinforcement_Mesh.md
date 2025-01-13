---
 TutorialInfo:r
   Topic/fr: Exemple de dalles avec armatures en forme de U
   Level: Intermédiaire
   Author: Shiv Charan
   FCVersion: 0.20
---

# Example Slab Having UShape Rebars Reinforcement Mesh/fr





## Description

L\'outil <img alt="" src=images/Reinforcement_SlabRebars.svg  style="width:24px;"> [Renfort de dalle](Reinforcement_SlabRebars/fr.md) permet à l\'utilisateur de créer des armatures à l\'intérieur d\'un objet dalle de [Arch Structure](Arch_Structure/fr.md).

Cet outil fait partie de l\'<img alt="" src=images/Reinforcement_Workbench.svg  style="width:24px;"> [atelier Reinforcement](Reinforcement_Workbench/fr.md), un [atelier externe](External_workbenches/fr.md) que vous pouvez installer avec le <img alt="" src=images/Std_AddonMgr.svg  style="width:24px;"> [Gestionnaire des extensions](Std_AddonMgr/fr.md).

Dans cet exemple, nous allons créer une armature de dalle avec des armatures en forme de U pour les deux directions, comme le montre la figure ci-dessous.

<img alt="" src=images/U-shape_rebars_isometric_view.png  style="width:800px;"> 
*Exemple d'armature de dalle avec des armatures en forme de U dans la dalle [Arch Structure](Arch_Structure/fr.md)*



## Utilisation

1\. Sélectionnez n\'importe quelle face d\'une dalle **<img src="images/Arch_Structure.svg" width=16px> [Arch Structure](Arch_Structure/fr.md)** déjà créée comme indiqué dans l\'image ci-dessous.

:   <img alt="" src=images/Selected_face_for_Slab_Arch_Structure.png  style="width:400px;">

:   
    
*Face sélectionnée de la dalle de Arch Structure*
    

2\. Sélectionnez ensuite **<img src="images/Reinforcement_SlabRebars.svg" width=16px> [Slab Reinforcement](Reinforcement_SlabRebars/fr.md)** dans les outils d\'armature.

3\. Une boîte de dialogue apparaîtra à l\'écran, comme indiqué ci-dessous.

:   ![](images/Slab_Reinforcement_input_dialog_box.png )

:   
    
*Fenêtre de dialogue pour le renfort des dalles*
    

4\. Sélectionnez le type souhaité de recouvrement du maillage du renfort (Haut ou Bas). Dans l\'exemple, c\'est le type Bas (Bottom) qui est sélectionné.

5\. Sélectionnez le type de barre d\'armature UShapeRebar et les autres données d\'entrée pour les barres d\'armature dans la direction parallèle à la face sélectionnée, comme le montre l\'image ci-dessous.

:   ![](images/U-shape_parallel_rebars_inputs.png )

:   
    
*Boîte de dialogue pour le renfort des dalles des armatures en direction parallèle de la face sélectionnée*
    

6\. Cliquez maintenant sur le bouton **Suivant** ou sélectionnez Cross Rebars dans la vue en liste.

7\. Sélectionnez maintenant le type de barre d\'armature UShapeRebar et les autres données souhaitées pour les données d\'entrée des barres d\'armature dans la direction transversale de la face sélectionnée, comme le montre l\'image ci-dessous.

:   ![](images/U-Shape_rebars_in_cross_direction_inputs.png )

:   
    
*Boîte de dialogue pour le renfort des dalles des armatures dans le sens transversal de la face sélectionnée*
    

8\. Cliquez sur **OK** ou **Apply** ou **Finish** pour générer le ferraillage des dalles.

9\. Cliquez sur **Annuler** pour quitter la fenêtre de dialogue.



## Propriétés utilisées pour le renfort de dalles avec des armatures en forme de U 

**Propriétés des armatures dans la direction parallèle à la face sélectionnée :**

-    **Mesh Cover Along**: représente l\'alignement du maillage des barres d\'armature le long de la face supérieure ou inférieure de la structure. Peut avoir deux valeurs : \"Top\" et \"Bottom\".

-    **Rebar Type**: type de barre d\'armature pour les barres d\'armature parallèles pour le renfort des dalles. Peut avoir quatre valeurs : \"StraightRebar\", \"LShapeRebar\", \"UShapeRebar\", \"BentShapeRebar\".

-    **Front Cover**: distance entre la barre d\'armature parallèle et la face sélectionnée.

-    **Left Cover**: distance entre l\'extrémité gauche de la barre d\'armature parallèle et la face gauche de la structure.

-    **Right Cover**: distance entre l\'extrémité droite de la barre d\'armature parallèle et la face droite de la structure.

-    **Bottom Cover**: distance entre les barres d\'armature parallèles et la face inférieure de la structure.

-    **Top Cover**: distance entre les barres d\'armature parallèles depuis la face supérieure de la structure.

-    **Rear Cover**: couverture arrière pour le renfort de la dalle des armatures parallèles.

-    **Diameter**: diamètre des barres d\'armature parallèles.

-    **Rounding**: valeur d\'arrondi à appliquer aux coins des barres, exprimée en fois le diamètre des barres d\'armature parallèles.

-    **Amount**: contient le nombre de barres d\'armature parallèles.

-    **Spacing**: contient l\'espacement entre les barres d\'armature parallèles.

**Propriétés des armatures dans le sens transversal de la face sélectionnée :**

-    **Rebar Type**: type de barre d\'armature pour les armatures transversales pour le renfort des dalles. Peut avoir quatre valeurs : \"StraightRebar\", \"LShapeRebar\", \"UShapeRebar\", \"BentShapeRebar\".

-    **Front Cover**: distance entre la barre d\'armature transversale et la face sélectionnée.

-    **Left Cover**: distance entre l\'extrémité gauche de la barre d\'armature transversale et la face gauche de la structure.

-    **Right Cover**: distance entre l\'extrémité droite de la barre d\'armature transversale et la face droite de la structure.

-    **Bottom Cover**: distance entre les armatures transversales et la face inférieure de la structure.

-    **Top Cover**: distance entre les armatures transversales depuis la face supérieure de la structure.

-    **Rear Cover**: couverture arrière pour le renforcement de la dalle des armatures transversales.

-    **Rounding**: valeur d\'arrondi à appliquer aux coins des barres, exprimée en fois le diamètre des armatures transversales.

-    **Diameter**: diamètre des barres d\'armature transversales

-    **Amount**: contient le nombre de barres d\'armature transversales.

-    **Spacing**: contient l\'espacement entre les armatures transversales.



## Script


**Voir aussi :**

[Arch API](Arch_API/fr.md), [Reinforcement API](Reinforcement_API/fr.md) et [FreeCAD Débuter avec les scripts](FreeCAD_Scripting_Basics/fr.md).

L\'outil Renfort des dalles peut être utilisé à partir de la console [Python](Python/fr.md) en utilisant la fonction suivante :



### Créer un renfort de dalle avec des armatures en forme de U 

Pour créer un renfort de dalles en forme de U comme indiqué dans les figures ci-dessus, vous pouvez utiliser la fonction makeSlabReinforcement comme suit :


```python
from SlabReinforcement.SlabReinforcement import makeSlabReinforcement
SlabReinforcementGroup = makeSlabReinforcement(
    parallel_rebar_type="UShapeRebar",
    parallel_front_cover=20,
    parallel_rear_cover=20,
    parallel_left_cover=10,
    parallel_right_cover=10,
    parallel_top_cover=30,
    parallel_bottom_cover=20,
    parallel_rounding=2,
    parallel_diameter=8,
    parallel_amount_spacing_check=True,
    parallel_amount_spacing_value=12,
    cross_rebar_type="UShapeRebar",
    cross_front_cover=20,
    cross_rear_cover=20,
    cross_left_cover=10,
    cross_right_cover=10,
    cross_top_cover=20,
    cross_bottom_cover=20,
    cross_rounding=2,
    cross_diameter=8,
    cross_amount_spacing_check=True,
    cross_amount_spacing_value=12,
    mesh_cover_along = "Bottom",
    structure=App.getDocument("slab").getObject("Beam"),
    facename='Face4',
)
```

-   Crée un objet `SlabReinforcementGroup` pour le ferraillage de dalle avec des armatures en forme de U pour la `structure` donnée, qui est une [Arch Structure](Arch_Structure/fr.md) dalle, et `facename`, qui est une face de cette structure.
    -   Si ni `structure` ni `facename` ne sont donnés, il prendra la face sélectionnée par l\'utilisateur comme entrée.

**Propriétés utilisées pour le renfort des dalles ayant des armatures en forme de U pour script de renfort**

**Propriétés des armatures dans la direction parallèle à la face sélectionnée :**

-    **parallel_rebar_type**: type de barre d\'armature pour les barres d\'armature parallèles pour le renforcement des dalles. Peut avoir quatre valeurs : \"StraightRebar\", \"LShapeRebar\", \"UShapeRebar\", \"BentShapeRebar\".

-    **parallel_front_cover**: distance entre la barre d\'armature parallèle et la face sélectionnée.

-    **parallel_rear_cover**: couverture arrière pour le renforcement de dalle des armatures parallèles.

-    **parallel_left_cover**: distance entre l\'extrémité gauche de la barre d\'armature parallèle et la face gauche de la structure.

-    **parallel_right_cover**: distance entre l\'extrémité droite de la barre d\'armature parallèle et la face droite de la structure.

-    **parallel_top_cover**: distance entre les barres d\'armature parallèles et la face supérieure de la structure.

-    **parallel_bottom_cover**: distance entre les barres d\'armature parallèles à partir de la face inférieure de la structure.

-    **parallel_diameter**: diamètre des barres d\'armature parallèles.

-    **parallel_amount_spacing_check**: si elle vaut True, alors la valeur de parallel_amount_spacing_value est utilisée comme nombre de barres, sinon la valeur de parallel_amount_spacing_value est utilisée comme espacement dans les barres parallèles.

-    **parallel_amount_spacing_value**: contient le nombre d\'armatures ou l\'espacement entre les armatures parallèles en fonction de la valeur de amount_spacing_check.

-    **parallel_rounding**: valeur d\'arrondi à appliquer aux coins des barres, exprimée en fois le parallel_diamètre.

**Propriétés des armatures dans le sens transversal de la face sélectionnée :**

-    **cross_rebar_type**: type d\'armature pour les armatures transversales pour le renforcement des dalles. Peut avoir quatre valeurs : \"StraightRebar\", \"LShapeRebar\", \"UShapeRebar\", \"BentShapeRebar\".

-    **cross_front_cover**: distance entre l\'armature transversale et la face transversale (face perpendiculaire à la face sélectionnée).

-    **cross_rear_cover**: couverture arrière pour le renfort de dalle des armatures transversales.

-    **cross_left_cover**: distance entre l\'extrémité gauche de l\'armature transversale et la face gauche de la structure.

-    **cross_right_cover**: distance entre l\'extrémité droite de la barre d\'armature et la face droite de la structure par rapport à la face transversale.

-    **cross_top_cover**: distance entre la barre d\'armature transversale et la face supérieure de la structure.

-    **cross_bottom_cover**: distance entre les barres d\'armature croisées de la face inférieure de la structure.

-    **cross_diameter**: diamètre des barres d\'armature transversales.

-    **cross_amount_spacing_check**: si elle vaut True, la valeur de cross_amount_spacing_value est utilisée comme nombre de barres, sinon la valeur de cross_amount_spacing_value est utilisée comme espacement entre les barres.

-    **cross_amount_spacing_value**: contient le nombre d\'armatures ou l\'espacement entre les armatures en fonction de la valeur de cross_amount_spacing_check.

-    **cross_rounding**: valeur d\'arrondi à appliquer aux coins des barres, exprimée en fois le cross_diameter.

**Propriétés communes des armatures parallèles et croisées :**

-    **mesh_cover_along**: peut avoir deux valeurs \"Top\" et \"Bottom\". Représente l\'alignement des mailles d\'armature le long de la face supérieure ou inférieure de la structure.

-    **structure**: objet de structure d\'arc. La valeur par défaut est None.

-    **facename**: face sélectionnée de la structure. La valeur par défaut est None.



### Éditer le renfort des dalles avec des armatures en forme de U 

Vous pouvez modifier les propriétés du renfort de dalle avec des armatures en forme de U en utilisant la fonction editSlabReinforcement comme suit :


```python
from SlabReinforcement.SlabReinforcement import editSlabReinforcement
SlabReinforcementGroup = editSlabReinforcement(
    SlabReinforcementGroup,
    parallel_rebar_type="UShapeRebar",
    parallel_front_cover=20,
    parallel_rear_cover=20,
    parallel_left_cover=10,
    parallel_right_cover=10,
    parallel_top_cover=30,
    parallel_bottom_cover=20,
    parallel_rounding=2,
    parallel_diameter=8,
    parallel_amount_spacing_check=True,
    parallel_amount_spacing_value=15,
    cross_rebar_type="UShapeRebar",
    cross_front_cover=20,
    cross_rear_cover=20,
    cross_left_cover=10,
    cross_right_cover=10,
    cross_top_cover=20,
    cross_bottom_cover=20,
    cross_rounding=2,
    cross_diameter=8,
    cross_amount_spacing_check=True,
    cross_amount_spacing_value=15,
    mesh_cover_along = "Bottom",
    structure=App.getDocument("slab").getObject("Beam"),
    facename='Face4',
)
```

-    `slabReinforcementGroup`est un objet groupe `Slab Reinforcement` déjà créé.

-   Les autres paramètres sont les mêmes que ceux requis par la fonction `makeSingleTieFourRebars()`.

vous pouvez changer n\'importe quelle propriété pour modifier le renfort des dalles.



---
⏵ [documentation index](../README.md) > [External_Command_Reference](Category_External_Command_Reference.md) > [Reinforcement](Category_Reinforcement.md) > Example Slab Having UShape Rebars Reinforcement Mesh/fr
