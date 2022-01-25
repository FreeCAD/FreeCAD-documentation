---
- GuiCommand:/fr
   Name:Arch Rebar Footing Reinforcement
   Name/fr:Arch Rebar Renforts de semelle
   MenuLocation:Arch → Rebar tools → Footing Reinforcement
   Workbenches:[Arch](Arch_Workbench/fr.md)
   SeeAlso:[Reinforcement](Reinforcement_Workbench/fr.md), [Arch Armature personnalisée](Arch_Rebar/fr.md)
---

# Arch Rebar Footing Reinforcement/fr

## Description

L\'outil [Renforts de semelle](Arch_Rebar_Footing_Reinforcement/fr.md) permet à l\'utilisateur de créer des barres de renforcement à l\'intérieur d\'un objet semelle [Arch Structure](Arch_Structure/fr.md).

Cette commande fait partie de l\'[atelier Reinforcement](Reinforcement_Workbench/fr.md), un [atelier externe](External_workbenches/fr.md) que vous pouvez installer avec le <img alt="" src=images/Std_AddonMgr.svg  style="width:24px;"> [Gestionnaire d\'Addon](Std_AddonMgr/fr.md) via le menu **Outils → Gestionnaire d'Addon → Reinforcement**.

![](images/Isometric_view_of_Columns_footing.png ) 
*Un exemple de renfort de semelle dans une semelle [Arch Structure](Arch_Structure/fr.md)*

![](images/Front_View_of_Column_footing.png ) 
*Vue de face de l'exemple de renfort de semelle*

## Utilisation

1\. Sélectionnez la face verticale d\'une semelle **<img src="images/Arch_Structure.svg" width=16px> [Arch Structure](Arch_Structure/fr.md)** préalablement créée comme le montre l\'image ci-dessous.

![](images/Footing_Face_selected.png ) 
*Face sélectionnée de la semelle Arch Structure*

2\. Sélectionnez ensuite **[Footng Reinforcement](Arch_Rebar_Footing_Reinforcement/fr.md)** dans les outils d\'armature.

3\. Une boîte de dialogue de renfort de semelle apparaît à l\'écran, comme illustré ci-dessous.

![](images/Footing_Reinforcement_GUI_.png ) 
*Boîte de dialogue pour l'armature de la semelle*

4\. Sélectionnez le type de barre souhaité et les autres données d\'entrée pour les barres dans la direction parallèle à la face sélectionnée dans le maillage de renfort de la semelle comme le montre l\'image ci-dessous.

![](images/Input_Fields_for_Parallel_rebars_in_footing_GUI_Dialog_box.png ) 
*Boîte de dialogue pour le renfort de la semelle des armatures dans la direction parallèle à la face sélectionnée.*

5\. Maintenant, cliquez sur le bouton Next ou sélectionnez Cross Rebars dans la vue en liste et remplissez les données souhaitées pour les données d\'entrée pour les barres dans la direction transversale de la face sélectionnée dans le maillage de renfort de la semelle comme le montre l\'image ci-dessous.

![](images/GUICrossRebarInputsFooting.png ) 
*Boîte de dialogue pour le renfort de la semelle des armatures dans le sens transversal de la face sélectionnée*

6\. Cliquez sur suivant ou cliquez sur Columns dans la vue en liste et remplissez l\'entrée souhaitée pour les colonnes dans le renfort de la semelle. Ici, vous pouvez choisir d\'ajouter ou non des armatures secondaires dans les colonnes.

![](images/Columns_input_fields_for_column_footing.png ) 
*Boîte de dialogue pour les champs de saisie des colonnes dans le renfort de la semelle.*

7\. Cliquez sur suivant ou cliquez sur Ties dans la vue en liste et remplissez les données souhaitées pour Ties dans les colonnes de renfort de la semelle.

![](images/Ties_input_fields_for_column_footing.png ) 
*Boîte de dialogue pour les champs de saisie des attaches dans les colonnes de renfort de la semelle*.

8\. Cliquez sur suivant ou cliquez sur Main rebars dans la vue en liste et remplissez les données souhaitées pour les armatures principales dans les colonnes de renfort de la semelle.

![](images/Main_Rebar_input_fields_for_column_footing.png ) 
*Boîte de dialogue pour les champs de saisie des armatures principales dans les colonnes de renfort de la semelle.*

Remarque : les étapes 9 et 10 ne sont nécessaires que si le contrôle des barres d\'armature secondaires est activé à l\'étape 6.

9\. Cliquez sur suivant ou cliquez sur XDir Secondary rebar dans la vue en liste et remplissez l\'entrée souhaitée pour les armatures secondaires dans la direction X dans une colonne dans le renfort de la semelle.

![](images/X_Direction_secondary_rebar_sinput_fields_for_column_footing_Reinforcement.png ) 
*Boîte de dialogue pour les champs de saisie des armatures de direction X dans les colonnes de renfort de la semelle.*

9\. Cliquez sur suivant ou cliquez sur YDir Secondary rebar dans la vue en liste et remplissez l\'entrée souhaitée pour les armatures secondaires dans la direction Y dans une colonne dans le renfort de la semelle.

![](images/Y_Direction_secondary_rebars_input_fields_for_Column_footing_reinforcement.png ) 
*Boîte de dialogue pour les champs de saisie des armatures de direction Y dans les colonnes de renfort de la semelle.*

11\. Cliquez sur **OK** ou **Apply** ou **Finish** pour générer le renforcement de la semelle.
12. Cliquez sur **Cancel** pour quitter la boîte de dialogue.

## Propriétés

**Propriétés des barres d\'armature en direction parallèle à la face sélectionnée dans la semelle renforcée :**

-   {{ PropertyData\|Mesh Cover Along}} : représente l\'alignement du maillage des barres d\'armature le long de la face supérieure et/ou inférieure de la structure. Peut avoir trois valeurs : \"Top\", \"Bottom\" et \"Both\".
-   {{ PropertyData\|Rebar Type}} : type de barre d\'armature pour les barres d\'armature parallèles pour le renfort de la semelle. Peut avoir trois valeurs : \'StraightRebar\', \'LShapeRebar\' et \'UShapeRebar\'.
-   {{ PropertyData\|Front Cover}} : distance entre la barre d\'armature parallèle et la face sélectionnée.
-   {{ PropertyData\|Left Cover}} : distance entre l\'extrémité gauche de la barre d\'armature parallèle et la face gauche de la structure.
-   {{ PropertyData\|Right Cover}} : distance entre l\'extrémité droite de la barre d\'armature parallèle et la face droite de la structure.
-   {{ PropertyData\|Bottom Cover}} : distance entre les barres d\'armature parallèles et la face inférieure de la structure.
-   {{ PropertyData\|Top Cover}} : distance entre les barres d\'armature parallèles depuis la face supérieure de la structure.
-   {{ PropertyData\|Rear Cover}} : couverture arrière pour le renfort de la semelle des barres d\'armature parallèles.
-   {{ PropertyData\|Rounding}} : valeur d\'arrondi à appliquer aux coins des barres, exprimée en fois le diamètre des barres d\'armature parallèles.
-   {{ PropertyData\|Diameter}} : Diamètre des barres d\'armature parallèles
-   {{ PropertyData\|Amount}} : contient le nombre de barres d\'armature parallèles.
-   {{ PropertyData\|Spacing}} : contient l\'espacement entre les barres d\'armature parallèles.

**Propriétés des armatures dans le sens transversal par rapport à la face sélectionnée dans la semelle renforcée :**

-    **Rebar Type**: type de barre d\'armature pour les armatures transversales pour le renfort des semelles. Peut avoir trois valeurs : \'StraightRebar\', \'LShapeRebar\' et \'UShapeRebar\'.

-    **Front Cover**: distance entre l\'armature transversale et la face transversale (face perpendiculaire à la face sélectionnée).

-    **Left Cover**: distance entre l\'extrémité gauche de l\'armature transversale et la face gauche de la structure.

-    **Right Cover**: distance entre l\'extrémité droite de la barre d\'armature transversale et la face droite de la structure.

-    **Bottom Cover**: distance entre les armatures transversales et la face inférieure de la structure.

-    **Top Cover**: distance entre les barres d\'armature transversales depuis la face supérieure de la structure.

-    **Rear Cover**: couverture arrière pour le renforcement de la semelle des armatures transversales.

-    **Rounding**: valeur d\'arrondi à appliquer aux coins des barres, exprimée en fois le diamètre des armatures transversales.

-    **Diameter**: diamètre des armatures transversales

-    **Amount**: contient le nombre d\'armatures transversales.

-    **Spacing**: contient l\'espacement entre les armatures transversales.

**Propriétés pour les colonnes dans la semelle renforcée :**

-    **Front Cover**: distance entre la face sélectionnée et les colonnes.

-    **Couverture gauche**: distance entre la face gauche et les colonnes.

-    **Right Cover**: distance entre la face droite et les colonnes.

-    **Rear Cover**: distance entre la face arrière et les colonnes.

-    **Column Width**: largeur de la colonne.

-    **Column Length**: longueur de la colonne.

-    **X direction column amount**: contient le nombre de colonnes dans le sens des x. Si le bouton radio Quantité dans le sens X est activé.

-    **X direction column spacing**: contient l\'espacement entre les colonnes dans le sens des x. Si le bouton radio d\'espacement dans le sens X est activé.

-    **Y direction column amount**: contient le nombre de colonnes dans le sens des y. Si la case d\'option Quantité dans le sens des Y est activée.

-    **Y direction column spacing**: contient l\'espacement entre les colonnes dans le sens des y. Si la case d\'option Espacement dans le sens des Y est activée.

-    **Add Secondary Rebars**: si la case est cochée, ajoute des barres secondaires dans les directions x et y dans les colonnes.

**Propriétés des attaches dans les colonnes de la semelle renforcée :**

-    **Top Cover**: couverture supérieure pour les liens à l\'extérieur de la semelle à partir de l\'extrémité des barres d\'armature principales.

-    **Bottom Cover**: couverture inférieure des attaches à partir du bas des barres d\'armature principales dans la semelle près du treillis.

-    **Diameter**: diamètre des attaches.

-    **Bent Angle**: angle de pliage des attaches.

-    **Extension Factor**: facteur d\'extension pour le bord étendu des attaches.

-    **Tie Number**: contient le nombre de barres d\'armature ou l\'espacement entre les attaches, si le bouton radio Number est activé.

-    **Tie Spacing**: contient l\'espacement entre les attaches, si le bouton radio Spacing est activé.

**Propriétés des armatures principales des colonnes de la semelle renforcée :**

-    **Type d'armature**: type d\'armature pour les armatures principales du poteau. Prend deux entrées différentes pour \'StraightRebar\', \'LShapeRebar\'.

-    **Hook Orientation**: orientation du crochet des barres d\'armature principales dans les colonnes si le type de barre d\'armature principale est LShapeRebar. Prend huit orientations différentes pour les crochets en forme de L, à savoir \'Top Inside\', \'Top Outside\', \'Bottom Inside\', \'Bottom Outside\', \'Top Left\', \'Top Right\', \'Bottom Left\', \'Bottom Right\'.

-    **Hook Extend Along**: Direction du crochet de la barre d\'armature principale (LShapeRebar). Il a deux options \"axe x\" et \"axe y\".

-    **Hook Extension**: spécifie la longueur du crochet de la barre d\'armature principale (LShapeRebar).

-    **Rebar Rounding**: valeur d\'arrondi à appliquer aux coins des barres, exprimée en fois le diamètre de la barre d\'armature principale.

-    **Top Offset**: décalage supérieur des barres d\'armature principales dans la colonne à l\'extérieur de la face supérieure de la semelle.

-    **Diameter**: diamètre des barres d\'armature principales dans les colonnes.

**Propriétés des armatures de direction X dans les colonnes de la semelle renforcée :**

Barres le long de la direction x, sauf les barres principales.

-    **Rebar Type**: type de barres d\'armature dans le sens des x d\'une colonne, avec deux valeurs : \'StraightRebar\' et \'LShapeRebar\'.

-    **Hook Orientation**: prend huit orientations différentes pour les crochets en forme de L, à savoir \'Top Inside\', \'Top Outside\', \'Bottom Inside\', \'Bottom Outside\', \'Top Left\', \'Top Right\', \'Bottom Left\', \'Bottom Right\'.

-    **Hook Extension**: longueur du crochet des barres d\'armature en forme de L.

-    **Rounding**: valeur d\'arrondi à appliquer aux coins des barres d\'armature en L, exprimée en fois le diamètre.

-    **Top Offset**: distance entre les barres d\'armature à partir de la face supérieure de la structure.

-    **Number#Diameter**: Jeu de numéros\#Diamètre des barres d\'armature dans l\'axe x.

**Propriétés des armatures de direction Y dans les colonnes de la semelle renforcée :**

Barres de renfort le long de la direction y, à l\'exception des barres de renfort principales.

-    **Rebar Type**: type de barres d\'armature dans l\'axe des y. Il a deux valeurs, \'StraightRebar\' et \'LShapeRebar\'.

-    **Hook Orientation**: orientation des crochets de type LS. Il prend huit orientations différentes pour les crochets en forme de L, à savoir \'Top Inside\', \'Top Outside\', \'Bottom Inside\', \'Bottom Outside\', \'Top Left\', \'Top Right\', \'Bottom Left\', \'Bottom Right\'.

-    **Hook Extension**: longueur du crochet des barres d\'armature en forme de L.

-    **Rounding**: valeur d\'arrondi à appliquer aux coins des barres d\'armature en L, exprimée en fois le diamètre.

-    **Top Offset**: distance entre les barres d\'armature à partir de la face supérieure de la structure.

-    **Number#Diameter**: jeu de numéros\#Diamètre des barres d\'armature dans la direction y.

## Script


**Voir aussi :**

[Arch API](Arch_API/fr.md), [Reinforcement API](Reinforcement_API/fr.md) et [FreeCAD Scripts de bases](FreeCAD_Scripting_Basics/fr.md).

L\'outil Renforts de semelle peut être utilisé à partir de la console [Python](Python/fr.md) en utilisant la fonction suivante :

### Créer un renfort de semelle 


```python
from FootingReinforcement.FootingReinforcement import makeFootingReinforcement

footingReinforcementGroup = makeFootingReinforcement(
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
    column_front_cover,
    column_left_cover,
    column_right_cover,
    column_rear_cover,
    tie_top_cover,
    tie_bottom_cover,
    tie_bent_angle,
    tie_extension_factor,
    tie_diameter,
    tie_number_spacing_check,
    tie_number_spacing_value,
    column_main_rebar_diameter,
    column_main_rebars_t_offset,
    cross_amount_spacing_value,
    column_width,
    column_length,
    xdir_column_amount_spacing_check = True,
    xdir_column_amount_spacing_value = 1,
    ydir_column_amount_spacing_check = True,
    ydir_column_amount_spacing_value = 1,
    parallel_rounding = 2,
    parallel_l_shape_hook_orintation = "Alternate",
    cross_rounding = 2,
    cross_l_shape_hook_orintation = "Alternate",
    column_main_rebars_type = "StraightRebar",
    column_main_hook_orientation = "Bottom Outside",
    column_main_hook_extend_along = "x-axis",
    column_l_main_rebar_rounding = 2,
    column_main_hook_extension = 40,
    column_sec_rebar_check = False,
    column_sec_rebars_t_offset = (400, 400),
    column_sec_rebars_number_diameter = (
        "1#8mm+1#8mm+1#8mm",
        "1#8mm+1#8mm+1#8mm",
    ),
    column_sec_rebars_type = (
        "StraightRebar",
        "StraightRebar",
    ),
    column_sec_hook_orientation = (
        "Top Inside",
        "Top Inside",
    ),
    column_l_sec_rebar_rounding = (2, 2),
    column_sec_hook_extension = (40, 40),
    mesh_cover_along = "Bottom",
    structure = None,
    facename = None,
)
```

-   Crée un objet `footingReinforcementGroup` à partir des données `structure`, qui est une [Arch Structure](Arch_Structure/fr.md) et `facename` qui est une face de cette structure.
    -   Si aucun `structure` ou `facename` n\'est donné, il prendra en entrée la face sélectionnée par l\'utilisateur.

**Propriétés des barres d\'armature dans la direction parallèle à la face sélectionnée :**

-    `parallel_rebar_type`: type de barre d\'armature pour les barres d\'armature parallèles pour le renfort des semelles. Peut avoir trois valeurs : \'StraightRebar\', \'LShapeRebar\', \'UShapeRebar\'.

-    `parallel_front_cover`: distance entre la barre d\'armature parallèle et la face sélectionnée.

-    `parallel_rear_cover`: couverture arrière pour le renforcement de la semelle des barres d\'armature parallèles.

-    `parallel_left_cover`: distance entre l\'extrémité gauche de la barre d\'armature parallèle et la face gauche de la structure.

-    `parallel_right_cover`: distance entre l\'extrémité droite de la barre d\'armature parallèle et la face droite de la structure.

-    `parallel_top_cover`: distance entre les barres d\'armature parallèles et la face supérieure de la structure.

-    `parallel_bottom_cover`: distance entre les barres d\'armature parallèles à partir de la face inférieure de la structure.

-    `parallel_diameter`: diamètre des barres d\'armature parallèles.

-    `parallel_amount_spacing_check`: mis à True, alors la valeur de parallel\_amount\_spacing\_value est utilisée comme nombre de barres, sinon la valeur de parallel\_amount\_spacing\_value est utilisée comme espacement dans les barres parallèles.

-    `parallel_amount_spacing_value`: contient le nombre d\'armatures ou l\'espacement entre les armatures parallèles en fonction de la valeur de amount\_spacing\_check.

-    `parallel_rounding`: valeur d\'arrondi à appliquer aux coins des barres, exprimée en fois le parallel\_diamètre.

-    `parallel_l_shape_hook_orintation`: représente l\'orientation du crochet de la barre d\'armature parallèle en forme de L si le type de barre parallèle est LShapeRebar. Peut avoir trois valeurs : \"Left\", \"Right\", \"Alternate\".

**Propriétés des barres d\'armature dans le sens transversal de la face sélectionnée :**

-    `cross_rebar_type`: type de barre d\'armature pour les armatures transversales pour le renforcement des semelles. Peut avoir trois valeurs : \'StraightRebar\', \'LShapeRebar\', \'UShapeRebar\'.

-    `cross_front_cover`: distance entre la barre d\'armature transversale et la face transversale (face perpendiculaire à la face sélectionnée).

-    `cross_rear_cover`: couverture arrière pour le renforcement de la semelle des armatures transversales.

-    `cross_left_cover`: distance entre l\'extrémité gauche de l\'armature transversale et la face gauche de la structure.

-    `cross_right_cover`: distance entre l\'extrémité droite de la barre d\'armature et la face droite de la structure par rapport à la face transversale.

-    `cross_top_cover`: distance entre la barre d\'armature transversale et la face supérieure de la structure.

-    `cross_bottom_cover`: distance entre les barres d\'armature croisées depuis la face inférieure de la structure.

-    `cross_diameter`: diamètre des barres d\'armature transversales.

-    `cross_amount_spacing_check`: mis à True, la valeur de cross\_amount\_spacing\_value est utilisée comme nombre de barres, sinon la valeur de cross\_amount\_spacing\_value est utilisée comme espacement entre les barres.

-    `cross_amount_spacing_value`: contient le nombre de barres ou l\'espacement entre les barres en fonction de la valeur de cross\_amount\_spacing\_check.

-    `cross_rounding`: valeur d\'arrondi à appliquer aux coins des barres, exprimée en fois le cross\_diameter.

-    `cross_l_shape_hook_orintation`: représente l\'orientation du crochet de la barre d\'armature transversale en forme de L si le type de barre transversale est LShapeRebar. Peut avoir trois valeurs : \"Left\", \"Right\", \"Alternate\".

**Propriétés pour les colonnes dans la semelle renforcée :**

-    `column_front_cover`: distance entre la face et les colonnes sélectionnées.

-    `column_left_cover`: distance entre la face gauche et les colonnes.

-    `column_right_cover`: distance entre la face et les colonnes de droite.

-    `column_rear_cover`: distance entre la face arrière et les colonnes arrière.

-    `column_width`: largeur des colonnes.

-    `column_length`: longueur des colonnes.

-    `xdir_column_amount_spacing_check`: mis à True, alors la valeur de xdir\_column\_amount\_spacing\_value est utilisée comme nombre de colonnes, sinon la valeur de xdir\_column\_amount\_spacing\_value est utilisée comme espacement entre les colonnes dans la direction x.

-    `xdir_column_amount_spacing_value`: contient le nombre de colonnes ou l\'espacement entre les colonnes dans le sens x en fonction de la valeur de xdir\_column\_amount\_spacing\_check.

-    `ydir_column_amount_spacing_check`: mis à True, alors la valeur de ydir\_column\_amount\_spacing\_value est utilisée comme nombre de colonnes, sinon la valeur de ydir\_column\_amount\_spacing\_value est utilisée comme espacement entre les colonnes dans la direction y.

-    `ydir_column_amount_spacing_value`: contient le nombre de colonnes ou l\'espacement entre les colonnes dans le sens des y en fonction de la valeur de ydir\_column\_amount\_spacing\_check.

-    `column_sec_rebar_check`: mis à True, ajoute des barres secondaires dans les directions x et y dans les colonnes.

**Propriétés des attaches dans les colonnes de la semelle renforcée :**

-    `tie_top_cover`: couverture supérieure des attaches à l\'extérieur de la semelle depuis l\'extrémité des barres d\'armature principales.

-    `tie_bottom_cover`: couverture inférieure des attaches à partir du bas des barres d\'armature principales dans la semelle près du treillis.

-    `tie_bent_angle`: angle de courbure des attaches.

-    `tie_extension_factor`: facteur d\'extension du bord étendu des attaches.

-    `tie_diameter`: diamètre des attaches.

-    `tie_number_spacing_check`: mis à True, alors la valeur de tie\_number\_spacing\_value est utilisée comme nombre de liens, sinon la valeur de tie\_number\_spacing\_value est utilisée comme espacement dans les liens.

-    `tie_number_spacing_value`: contient le nombre d\'égalités ou l\'espacement entre les égalités en fonction de la valeur de tie\_number\_spacing\_check.

**Propriétés des armatures principales des colonnes de la semelle renforcée :**

-    `column_main_rebar_diameter`: diamètre des barres d\'armature principales dans les colonnes.

-    `column_main_rebars_t_offset`: décalage supérieur des barres d\'armature principales dans la colonne à l\'extérieur de la semelle.

-    `column_main_hook_extend_along`: direction du crochet de la barre d\'armature principale (LShapeRebar). Il a deux options \"x-axis\" et \"y-axis\".

-    `column_l_main_rebar_rounding`: valeur d\'arrondi à appliquer aux coins des barres, exprimée en fois le diamètre de la colonne\_main\_rebar\_.

-    `column_main_hook_extension`: indique la longueur du crochet de la barre d\'armature principale (LShapeRebar).

-    `column_main_rebars_type`: type de barre d\'armature pour les barres d\'armature principales du poteau. Prend deux entrées différentes pour \'StraightRebar\', \'LShapeRebar\'. La valeur par défaut est StraightRebar.

-    `column_main_hook_orientation`: orientation du crochet des barres principales dans les colonnes si column\_main\_rebars\_type est LShapeRebar. Prend huit orientations différentes pour les crochets en forme de L, à savoir \'Top Inside\', \'Top Outside\', \'Bottom Inside\', \'Bottom Outside\', \'Top Left\', \'Top Right\', \'Bottom Left\', \'Bottom Right\'.

**Propriétés pour les directions secondaires X et Y des barres d\'armature des colonnes de la semelle renforcée :**

-    `column_sec_rebars_t_offset`et `sec_rebars_b_offset` sont des n-uplets (xdir\_rebars\_t\_offset, ydir\_rebars\_t\_offset) qui définissent les distances de décalage (ou hauteur) pour les armatures secondaires de direction x et de direction y par rapport aux faces supérieures de la structure, respectivement.

-    `column_sec_rebars_number_diameter`est un tuple (xdir\_rebars\_number\_diameter, ydir\_rebars\_number\_diameter) qui définit le jeu de nombres\#diamètres des barres secondaires de direction x et de direction y, respectivement.

-    `column_sec_rebars_type`est un tuple (xdir\_rebars\_type, ydir\_rebars\_type) qui définit le type des barres secondaires de direction x et de direction y, respectivement ; il peut avoir `"StraightRebar"` ou `"LShapeRebar"` comme type de barre.

-    `column_sec_hook_orientation`est un tuple (xdir\_hook\_orientation, ydir\_hook\_orientation) qui définit l\'orientation du crochet secondaire en forme de LS dans les directions x et y. Il peut avoir `"StraightRebar"` ou `"LShapeRebar"` comme type de barre d\'armature ; il peut avoir `"Top Inside"`, `"Top Outside"`, `"Bottom Inside"`, `"Bottom Outside"`, `"Top Right"`, `"Top Left"`, `"Bottom Right"` ou `"Bottom Left"` comme orientation du crochet.

-    `column_l_sec_rebar_rounding`est un tuple (l\_xdir\_rebar\_rounding, l\_ydir\_rebar\_rounding) qui détermine le rayon de courbure des barres d\'armature secondaires en forme de LS dans les directions x et y, exprimé sous forme de fois le diamètre des barres d\'armature en forme de LS dans les directions x et y, respectivement.

-    `column_sec_hook_extension`est un tuple (xdir\_hook\_extension, ydir\_hook\_extension) qui définit la longueur du crochet des barres d\'armature secondaires en forme de LS dans les directions x et y.

**Propriétés communes de la semelle renforcée :**

-    `mesh_cover_along`: peut avoir trois valeurs : \"Top\", \"Bottom\" et \"Both\". Représente l\'alignement des mailles d\'armature le long de la face supérieure et/ou inférieure de la structure.

-    `structure`: objet Arch structure. La valeur par défaut est None.

-    `facename`: face sélectionnée de la structure. La valeur par défaut est None.

### Edition de Renforts de semelle 

Vous pouvez modifier les propriétés de Renforts de semelle à l\'aide de la fonction suivante


```python
from FootingReinforcement.FootingReinforcement import editFootingReinforcement

footingReinforcementGroup = editFootingReinforcement(
    footingReinforcementGroup,
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
    column_front_cover,
    column_left_cover,
    column_right_cover,
    column_rear_cover,
    tie_top_cover,
    tie_bottom_cover,
    tie_bent_angle,
    tie_extension_factor,
    tie_diameter,
    tie_number_spacing_check,
    tie_number_spacing_value,
    column_main_rebar_diameter,
    column_main_rebars_t_offset,
    cross_amount_spacing_value,
    column_width,
    column_length,
    xdir_column_amount_spacing_check = True,
    xdir_column_amount_spacing_value = 1,
    ydir_column_amount_spacing_check = True,
    ydir_column_amount_spacing_value = 1,
    parallel_rounding = 2,
    parallel_l_shape_hook_orintation = "Alternate",
    cross_rounding = 2,
    cross_l_shape_hook_orintation = "Alternate",
    column_main_rebars_type = "StraightRebar",
    column_main_hook_orientation = "Bottom Outside",
    column_main_hook_extend_along = "x-axis",
    column_l_main_rebar_rounding = 2,
    column_main_hook_extension = 40,
    column_sec_rebar_check = False,
    column_sec_rebars_t_offset = (400, 400),
    column_sec_rebars_number_diameter = (
        "1#8mm+1#8mm+1#8mm",
        "1#8mm+1#8mm+1#8mm",
    ),
    column_sec_rebars_type = (
        "StraightRebar",
        "StraightRebar",
    ),
    column_sec_hook_orientation = (
        "Top Inside",
        "Top Inside",
    ),
    column_l_sec_rebar_rounding = (2, 2),
    column_sec_hook_extension = (40, 40),
    mesh_cover_along = "Bottom",
    structure = None,
    facename = None,
)
```

-    `footngReinforcementGroup`est un objet groupe `Footing Reinforcement` préalablement créé.

-   Les autres paramètres sont les mêmes que ceux requis par la fonction `makeFootingReinforcement()`.



---
![](images/Right_arrow.png) [documentation index](../README.md) > [Reinforcement](Category_Reinforcement.md) > [Arch](Arch_Workbench.md) > Arch Rebar Footing Reinforcement/fr
