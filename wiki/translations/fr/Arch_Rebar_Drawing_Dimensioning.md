---
- GuiCommand   */fr
   Name   *Arch Rebar Drawing Dimensioning
   Name/fr   *Arch Rebar Dessins dimensions
   MenuLocation   *
   Workbenches   *[Arch](Arch_Workbench/fr.md), [BIM](BIM_Workbench/fr.md)
   Version   *0.19
   SeeAlso   *[Reinforcement](Reinforcement_Workbench/fr.md), [Arch Nomenclature armature](Arch_Rebar_BOM/fr.md), [Reinforcement Nomenclature de façonnage des armatures](Reinforcement_Bar_Shape_Cut_List.md)
---

# Arch Rebar Drawing Dimensioning/fr

## Description

L\'outil [Dessins dimensions](Arch_Rebar_Drawing_Dimensioning/fr.md) permet à l\'utilisateur de créer un dessin d\'armatures et de leurs donner des dimensions.

Cette commande fait partie de l\'[atelier Reinforcement](Reinforcement_Workbench/fr.md), un [atelier externe](External_workbenches/fr.md) que vous pouvez installer avec le <img alt="" src=images/Std_AddonMgr.svg  style="width   *24px;"> [Gestionnaire d\'Addon](Std_AddonMgr/fr.md) via le menu **Outils → Gestionnaire d'Addon → Reinforcement**.

<img alt="" src=images/Arch_Rebar_Drawing_Dimensioning_example.svg  style="width   *800px;">



*Dessin et dimensionnement des armatures*

## Utilisation

1\. Ouvrez le modèle FreeCAD contenant les barres d\'armature créées à l\'aide de [Atelier Reinforcement](Reinforcement_Workbench/fr.md).

2\. Sélectionnez l\'objet **<img src="images/Arch_Structure.svg" width=16px> [Arch Structure](Arch_Structure/fr.md)** puis cliquez sur **<img src="images/Arch_Rebar_Drawing_Dimensioning.svg" width=16px> [Reinforcement Drawing Dimensioning](Arch_Rebar_Drawing_Dimensioning/fr.md)**.

3\. Une boîte de dialogue apparaîtra à l\'écran, comme indiqué ci-dessous.

<img alt="" src=images/ArchRebarDrawingDimensioning_dialog1.png  style="width   *800px;">

4\. Entrez tous les détails relatifs à la largeur du trait et à la couleur de l\'armature et de la structure.

5\. Cliquez sur **Next** et la boîte de dialogue sera mise à jour comme indiqué ci-dessous.

<img alt="" src=images/ArchRebarDrawingDimensioning_dialog2.png  style="width   *800px;">

6\. Entrez les détails des options de vues de dessin, de cotation et de décalage.

7\. Cliquez sur **Next** et la boîte de dialogue sera mise à jour comme indiqué ci-dessous.

<img alt="" src=images/ArchRebarDrawingDimensioning_dialog3.png  style="width   *800px;">

8\. Entrez l\'étiquette de cote et les détails de la ligne.

9\. Cliquez sur **Next** et la boîte de dialogue sera mise à jour comme indiqué ci-dessous.

<img alt="" src=images/ArchRebarDrawingDimensioning_dialog4.png  style="width   *800px;">

10\. Entrez les détails de dimension d\'une seule armature et de plusieurs armatures.

11\. Cliquez sur **Next** et la boîte de dialogue sera mise à jour comme indiqué ci-dessous.

<img alt="" src=images/ArchRebarDrawingDimensioning_dialog5.png  style="width   *800px;">

12\. Entrez les détails des décalages de cote et de ligne de cote.

13\. Cliquez sur le bouton **Finish** pour générer des dessins.

## Script


**Voir aussi    ***

[Arch API](Arch_API/fr.md), [API de renforts](Reinforcement_API/fr.md) et [FreeCAD Scripts de Base](FreeCAD_Scripting_Basics/fr.md).

L\'outil [Dimensionnement des dessins d\'armatures](Arch_Rebar_Drawing_Dimensioning/fr.md) peut être utilisé dans des [macros](macros/fr.md) et à partir de la console [Python](Python/fr.md) à l\'aide des fonctions suivantes    *

### Créer un dessin et des dimensions d\'armatures 


```python
from ReinforcementDrawing import make_reinforcement_drawing

structure_drawing_page_dict = make_reinforcement_drawing.makeStructuresReinforcementDrawing(
    structure_list=None,
    rebars_list=None,
    view="Front",
    rebars_stroke_width=0.35,
    rebars_color_style="Automatic",
    rebars_color=(0.67, 0.0, 0.0),
    structure_stroke_width=0.5,
    structure_color_style="Automatic",
    structure_color=(0.3, 0.9, 0.91),
    drawing_left_offset=20,
    drawing_top_offset=20,
    drawing_min_right_offset=20,
    drawing_min_bottom_offset=20,
    drawing_max_width=0,                        # Il est défini sur 0 pour définir automatiquement la largeur par défaut en fonction d'autres paramètres
    drawing_max_height=0,                       # Il est défini sur 0 pour définir automatiquement la hauteur par défaut en fonction d'autres paramètres
    template_file=str(Path(make_reinforcement_drawing.__file__).parent.absolute() / "Templates" / "A4_Landscape_blank.svg"),
    perform_dimensioning=True,
    dimension_rebars_filter_list=None,
    dimension_label_format="%M %C⌀%D,span=%S",
    dimension_font_family="DejaVu Sans",
    dimension_font_size=3,
    dimension_stroke_width=0.25,
    dimension_line_style="Continuous",
    dimension_line_color=(0.0, 0.0, 0.50),
    dimension_text_color=(0.0, 0.33, 0.0),
    dimension_single_rebar_line_start_symbol="None",
    dimension_single_rebar_line_end_symbol="FilledArrow",
    dimension_multi_rebar_line_start_symbol="FilledArrow",
    dimension_multi_rebar_line_end_symbol="FilledArrow",
    dimension_line_mid_point_symbol="Dot",
    dimension_left_offset=10,
    dimension_right_offset=10,
    dimension_top_offset=10,
    dimension_bottom_offset=10,
    dimension_left_offset_increment=6,
    dimension_right_offset_increment=6,
    dimension_top_offset_increment=6,
    dimension_bottom_offset_increment=6,
    dimension_single_rebar_outer_dim=False,
    dimension_multi_rebar_outer_dim=True,
    dimension_single_rebar_text_position_type="StartOfLine",
    dimension_multi_rebar_text_position_type="MidOfLine",
)
```

-   Il renvoie `structure_drawing_page_dict`, un dictionnaire avec la structure comme clé et la page correspondante de dessin des armatures comme valeur.

-    `structure_list`est la liste des objets structurels pour générer leur dessin des armatures. Si elles ne sont pas fournies, les structures seront sélectionnées dans le document actif agissant en tant qu\'hôte pour les objets d\'armature.

-    `rebars_list`est la liste des objets d\'armature à inclure dans le dessin. S\'ils ne sont pas fournis, les objets d\'armature ayant Host dans structure_list seront sélectionnés dans le document actif.

-    `view`spécifie la vue du dessin à générer. Il peut s\'agir de \"Front\", \"Rear\", \"Left\", \"Right\", \"Top\" or \"Bottom\". (Avant, Arrière, Gauche, Droite, Haut ou Bas).

-    `rebars_stroke_width`spécifie la largeur de trait des armatures dans le dessin SVG.

-    `rebars_color_style`spécifie le style de couleur des armatures. Réglez-le sur \"Automatique\" pour sélectionner automatiquement la couleur des armatures ou sur \"Personnalisé\" pour choisir la valeur de couleur de la forme à partir de la variable `rebars_color`.

-    `rebars_color`spécifie la couleur de remplissage des armatures dans le dessin SVG.

   Format   * (r, g, b)
   La valeur r, g, b doit être comprise entre 0 et 1, vous devrez peut-être diviser la valeur de r, g, b par 255 pour obtenir sa valeur entre 0 et 1
   Assurez-vous que r, g, b soient flottant
   Exemple   * (0.67, 0.0, 0.0)

-    `structure_stroke_width`spécifie la largeur de trait de la structure dans le dessin SVG.

-    `structure_color_style`spécifie le style de remplissage de la structure. Réglez-le sur \"Automatique\" pour sélectionner automatiquement la couleur de la structure ou sur \"Personnalisé\" pour choisir la valeur de couleur de la structure à partir de la variable `structure_color`.

-    `structure_color`spécifie la couleur de remplissage de la structure dans le dessin SVG. Format   * (r, g, b)

-    `drawing_left_offset`spécifie le décalage gauche de la vue de dessin sur `template_file`.

-    `drawing_top_offset`spécifie le décalage supérieur de la vue de dessin sur `template_file`.

-    `drawing_min_right_offset`spécifie le décalage minimum à droite de la vue de dessin sur `template_file`.

-    `drawing_min_bottom_offset`spécifie le décalage inférieur minimum de la vue de dessin sur `template_file`.

-    `drawing_max_width`spécifie la largeur maximale du dessin sur `template_file`.

-    `drawing_max_height`spécifie la hauteur maximale du dessin sur `template_file`.

-    `template_file`est le fichier modèle à utiliser pour la page de dessin des armatures.

-    `perform_dimensioning`spécifie si une cotation doit être créée pour les armatures dans le dessin.

-    `dimension_rebars_filter_list`est la liste des armatures à dimensionner. Définissez-le sur Aucun pour coter toutes les armatures visibles dans le dessin.

-    `dimension_label_format`est le format utilisé pour l\'étiquette de dimension.

   Exemple   * "%M %C⌀%D,span=%S"
   Ici   *  %M -> Rebar.Mark
         %C -> Rebar.Amount
         %D -> Rebar.Diameter
         %S -> Rebar span length

-    `dimension_font_family`est la famille de polices de l\'étiquette de dimension.

-    `dimension_font_size`est la taille de la police de l\'étiquette de dimension.

-    `dimension_stroke_width`est la largeur du trait de la ligne de cote.

-    `dimension_line_style`est le style de trait de la ligne de cote. Il peut s\'agir de \"Continuous\", \"Dash\", \"Dot\", \"DashDot\" ou \"DashDotDot\".

-    `dimension_line_color`est la couleur de la ligne de cote.

   Format   * (r, g, b)
   La valeur r, g, b doit être comprise entre 0 et 1, vous devrez peut-être diviser la valeur de r, g, b par 255 pour obtenir sa valeur entre 0 et 1
   Assurez-vous que r, g, b soient flottants

-    `dimension_text_color`est la couleur de l\'étiquette de dimension.

-    `dimension_single_rebar_line_start_symbol`est le symbole de début de la ligne de cote, si une seule armature est visible. Il peut s\'agir de \"FilledArrow\", \"Tick\", \"Dot\" ou \"None\".

-    `dimension_single_rebar_line_end_symbol`est le symbole de fin de ligne de cote, si une seule armature est visible. Il peut s\'agir de \"FilledArrow\", \"Tick\", \"Dot\" ou \"None\".

-    `dimension_multi_rebar_line_start_symbol`est le symbole de début de ligne de cote, dans le cas où plusieurs armatures sont visibles. Il peut s\'agir de \"FilledArrow\", \"Tick\", \"Dot\" ou \"None\".

-    `dimension_multi_rebar_line_end_symbol`est le symbole de fin de ligne de cote, dans le cas où plusieurs barres d\'armature sont visibles. Il peut s\'agir de \"FilledArrow\", \"Tick\", \"Dot\" ou \"None\".

-    `dimension_line_mid_point_symbol`est le symbole du milieu de la ligne de cote. Il peut s\'agir de \"Tick\", \"Dot\" ou \"None\".

-    `dimension_left_offset`spécifie le décalage gauche de la cote à partir du dessin.

-    `dimension_right_offset`spécifie le décalage à droite de la cote à partir du dessin.

-    `dimension_top_offset`spécifie le décalage supérieur de la cote à partir du dessin.

-    `dimension_bottom_offset`spécifie le décalage inférieur de la cote à partir du dessin.

-    `dimension_left_offset_increment`est l\'incrément du décalage gauche pour éloigner chaque nouvelle étiquette de cote du dessin.

-    `dimension_right_offset_increment`est l\'incrément du décalage droit pour éloigner chaque nouvelle étiquette de cote du dessin.

-    `dimension_top_offset_increment`est l\'incrément du décalage supérieur pour éloigner chaque nouvelle étiquette de cote du dessin.

-    `dimension_bottom_offset_increment`est l\'incrément du décalage inférieur pour éloigner chaque nouvelle étiquette de cote du dessin.

-    `dimension_single_rebar_outer_dim`spécifie si les lignes de cote doivent être en dehors du dessin d\'armature, dans le cas où une seule armature est visible.

-    `dimension_multi_rebar_outer_dim`spécifie si les lignes de cote doivent être à l\'extérieur du dessin d\'armature, dans le cas où plusieurs armatures sont visibles.

-    `dimension_single_rebar_text_position_type`spécifie le type de position de l\'étiquette de cote, si une seule armature est visible. Il peut s\'agir de \"StartOfLine\", \"MidOfLine\" ou \"EndOfLine\".

-    `dimension_multi_rebar_text_position_type`spécifie le type de position de l\'étiquette de cote, dans le cas où plusieurs armatures sont visibles. Il peut s\'agir de \"StartOfLine\", \"MidOfLine\" ou \"EndOfLine\".


<div class="mw-collapsible toccolours mw-collapsed">

##### Exemple


<div class="mw-collapsible-content">


```python
from pathlib import Path
import FreeCAD, Draft, Arch
from ColumnReinforcement import TwoTiesSixRebars
from ReinforcementDrawing import make_reinforcement_drawing

Rect = Draft.makeRectangle(400, 400)
Structure1 = Arch.makeStructure(Rect, height=1600)
Structure1.ViewObject.Transparency = 80
Structure2 = Arch.makeStructure(Rect, height=1600)
Structure2.ViewObject.Transparency = 80
Structure2.Placement = FreeCAD.Placement(FreeCAD.Vector(1000, 0, 0), FreeCAD.Rotation(FreeCAD.Vector(0, 0, 1), 0))
FreeCAD.ActiveDocument.recompute()

# Créer des barres d'armature droites
TwoTiesSixRebars.makeTwoTiesSixRebars(
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
    structure=Structure1,
    facename="Face6",
)

# Pour les barres de renfort en forme de L avec le crochet dirigé le long de l'axe des x.
TwoTiesSixRebars.makeTwoTiesSixRebars(
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
    structure=Structure2,
    facename="Face6",
)

# Créer un dessin et des dimensions d'armatures
for drawing_view in ("Front", "Rear", "Left", "Right", "Top", "Bottom")   *
    struct_drawing_page_dict = make_reinforcement_drawing.makeStructuresReinforcementDrawing(
        structure_list=None,
        rebars_list=None,
        view="Front",
        rebars_stroke_width=0.35,
        rebars_color_style="Automatic",
        rebars_color=(0.67, 0.0, 0.0),
        structure_stroke_width=0.5,
        structure_color_style="Automatic",
        structure_color=(0.3, 0.9, 0.91),
        drawing_left_offset=20,
        drawing_top_offset=20,
        drawing_min_right_offset=20,
        drawing_min_bottom_offset=20,
        drawing_max_width=0,                        # Il est défini sur 0 pour définir automatiquement la largeur par défaut en fonction d'autres paramètres
        drawing_max_height=0,                       # Il est défini sur 0 pour définir automatiquement la hauteur par défaut en fonction d'autres paramètres
        template_file=str(Path(make_reinforcement_drawing.__file__).parent.absolute() / "Templates" / "A4_Landscape_blank.svg"),
        perform_dimensioning=True,
        dimension_rebars_filter_list=None,
        dimension_label_format="%M %C⌀%D,span=%S",
        dimension_font_family="DejaVu Sans",
        dimension_font_size=3,
        dimension_stroke_width=0.25,
        dimension_line_style="Continuous",
        dimension_line_color=(0.0, 0.0, 0.50),
        dimension_text_color=(0.0, 0.33, 0.0),
        dimension_single_rebar_line_start_symbol="None",
        dimension_single_rebar_line_end_symbol="FilledArrow",
        dimension_multi_rebar_line_start_symbol="FilledArrow",
        dimension_multi_rebar_line_end_symbol="FilledArrow",
        dimension_line_mid_point_symbol="Dot",
        dimension_left_offset=10,
        dimension_right_offset=10,
        dimension_top_offset=10,
        dimension_bottom_offset=10,
        dimension_left_offset_increment=6,
        dimension_right_offset_increment=6,
        dimension_top_offset_increment=6,
        dimension_bottom_offset_increment=6,
        dimension_single_rebar_outer_dim=False,
        dimension_multi_rebar_outer_dim=True,
        dimension_single_rebar_text_position_type="StartOfLine",
        dimension_multi_rebar_text_position_type="MidOfLine",
    )
    for drawing_page in struct_drawing_page_dict.values()   *
        drawing_view = drawing_page.Views[0]
        drawing_view.setExpression(
            "LeftOffset",
            u".Template.Width.Value / 2 - .Width.Value * .Scale / 2",
        )
        drawing_view.setExpression(
            "TopOffset",
            u".Template.Height.Value / 2 - .Height.Value * .Scale / 2",
        )
        drawing_view.recompute(True)
        drawing_page.recompute(True)

```


</div>


</div>

# <img alt="" src=images/Arch_Rebar_Drawing.svg  style="width   *32px;"> Dessins des armatures 

## Utilisation 

1\. Ouvrez le modèle FreeCAD contenant les barres d\'armature créées à l\'aide de [Addon Reinforcement](Reinforcement_Addon/fr.md).

2\. Dans la console FreeCAD Python, copiez l\'extrait de code ci-dessous pour générer le dessin des armatures à partir de différentes vues pour chaque élément [Arch Structure](Arch_Structure/fr.md). 
```python
from ReinforcementDrawing.make_reinforcement_drawing import (
    makeStructuresReinforcementDrawing,
)

for view in ("Front", "Rear", "Left", "Right", "Top", "Bottom")   *
    makeStructuresReinforcementDrawing(view=view)
```

## Objet ReinforcementDrawingView 

Un objet de la vue SVG Dessin des armatures.

### Propriétés

-    **Structure**   * L\'objet structure agissant en tant qu\'hôte pour les armatures à inclure dans le dessin.

-    **Rebars**   * La liste des objets d\'armature à inclure dans le dessin.

-    **View**   * La vue du dessin des armatures à générer. Il peut s\'agir de \"Front\", \"Rear\", \"Left\", \"Right\", \"Top\" ou \"Bottom\".

-    **PositionType**   * Le type de position du dessin d\'armature sur le gabarit. Il peut être \"Automatique\" pour calculer l\'emplacement du dessin en utilisant **LeftOffset**, **TopOffset**, **MinRightOffset** et **MinBottomOffset** OU \"Personnalisé\" pour définir l\'emplacement en utilisant **X** et **Y**.

-    **RebarsStrokeWidth**   * La largeur de trait des armatures dans le dessin des armatures SVG.

-    **RebarsColorStyle**   * Le style de couleur des armatures dans le dessin des armatures SVG. Réglez-le sur \"Automatique\" pour sélectionner automatiquement la couleur des armatures OU sur \"Personnalisé\" pour choisir la valeur de couleur de la forme dans **RebarsColor**.

-    **RebarsColor**   * La couleur des armatures dans le dessin des armatures SVG.

-    **StructureStrokeWidth**   * La largeur du trait de la structure dans le SVG du dessin d\'armature.

-    **StructureColorStyle**   * Le style de couleur de la structure dans le dessin des armatures SVG. Réglez-le sur \"Automatique\" pour sélectionner automatiquement la couleur des armatures, \"Personnalisé\" pour choisir la valeur de couleur de la forme de **StructureColor** OU \"Aucun\" pour ne pas remplir la structure.

-    **StructureColor**   * La couleur de la structure dans le dessin des armatures SVG.

-    **Template**   * Le modèle pour la vue de dessin des armatures.

-    **Width**   * La largeur de la vue SVG du dessin des armatures.

-    **Height**   * La hauteur de la vue de dessin des armatures SVG.

-    **LeftOffset**   * Le décalage gauche de la vue de dessin des armatures sur un modèle.

-    **TopOffset**   * Le décalage supérieur de la vue de dessin des armatures sur un modèle.

-    **MinRightOffset**   * Le décalage minimum à droite de la vue de dessin des armatures sur un modèle.

-    **MinBottomOffset**   * Le décalage inférieur minimum de la vue de dessin des armatures sur un modèle.

-    **MaxWidth**   * La largeur maximale de la vue du dessin des armatures.

-    **MaxHeight**   * La hauteur maximale de la vue du dessin des armatures.

-    **VisibleRebars**   * La liste des objets d\'armature visibles dans la vue de dessin.

-    **DimensionLeftOffset**   * Le décalage gauche pour chaque nouvel objet ReinforcementDimensioning.

-    **DimensionRightOffset**   * Le décalage droit pour chaque nouvel objet ReinforcementDimensioning.

-    **DimensionTopOffset**   * Le décalage supérieur pour chaque nouvel objet ReinforcementDimensioning.

-    **DimensionBottomOffset**   * Le décalage inférieur pour chaque nouvel objet ReinforcementDimensioning.

## Script 


**Voir aussi    ***

[Arch API](Arch_API/fr.md), [API de renforts](Reinforcement_API/fr.md) et [FreeCAD Scripts de Base](FreeCAD_Scripting_Basics/fr.md).

Les fonctions dessins de Reinforcement peuvent être utilisées dans des [macros](macros/fr.md) et dans la console [Python](Python/fr.md) en utilisant les fonctions suivantes    *

### Créer une vue de dessin de l\'armature 

#### Pour une structure 


```python
from ReinforcementDrawing.make_reinforcement_drawing import (
    makeReinforcementDrawing,
)

reinforcement_drawing_page = makeReinforcementDrawing(
    structure,
    rebars_list,
    view,
    rebars_stroke_width,
    rebars_color_style,
    rebars_color,
    structure_stroke_width,
    structure_color_style,
    structure_color,
    drawing_left_offset,
    drawing_top_offset,
    drawing_min_right_offset,
    drawing_min_bottom_offset,
    drawing_max_width,
    drawing_max_height,
    template_file,
    dimension_left_offset,
    dimension_right_offset,
    dimension_top_offset,
    dimension_bottom_offset,
)
```

-   Crée un objet `ReinforcementDrawingView` pour la liste d\'objets [structure](Arch_Structure/fr.md) et [rebar](Arch_Rebar/fr.md).

-   Il renvoie le `reinforcement_drawing_page` de type `TechDraw   *   *DrawPage`.

-    `view`spécifie la vue du dessin à générer. Il peut s\'agir de \"Front\", \"Rear\", \"Left\", \"Right\", \"Top\" or \"Bottom\".

-    `rebars_stroke_width`spécifie la largeur de trait des armatures dans le dessin SVG.

-    `rebars_color_style`spécifie le style de couleur des armatures. Réglez-le sur \"Automatique\" pour sélectionner automatiquement la couleur des armatures ou sur \"Personnalisé\" pour choisir la valeur de couleur de la forme à partir de la variable `rebars_color`.

-    `rebars_color`spécifie la couleur de remplissage des armatures dans le dessin SVG.

   Format    * (r, g, b)
   La valeur r, g, b doit être comprise entre 0 et 1, vous devrez peut-être diviser la valeur de r, g, b par 255 pour obtenir sa valeur entre 0 et 1
   Assurez-vous que r, g, b soient flottants
   Exemple   * (0.67, 0.0, 0.0)

-    `structure_stroke_width`spécifie la largeur de trait de la structure dans le dessin SVG.

-    `structure_color_style`spécifie le style de remplissage de la structure. Réglez-le sur \"Automatique\" pour sélectionner automatiquement la couleur de la structure ou sur \"Personnalisé\" pour choisir la valeur de couleur de la structure à partir de la variable `structure_color`.

-    `structure_color`spécifie la couleur de remplissage de la structure dans le dessin SVG. Format   * (r, g, b)

-    `drawing_left_offset`spécifie le décalage gauche de la vue de dessin sur `template_file`.

-    `drawing_top_offset`spécifie le décalage supérieur de la vue de dessin sur `template_file`.

-    `drawing_min_right_offset`spécifie le décalage minimum à droite de la vue de dessin sur `template_file`.

-    `drawing_min_bottom_offset`spécifie le décalage inférieur minimum de la vue de dessin sur `template_file`.

-    `drawing_max_width`spécifie la largeur maximale du dessin sur `template_file`.

-    `drawing_max_height`spécifie la hauteur maximale du dessin sur `template_file`.

-    `template_file`est le fichier modèle à utiliser pour la page de dessin de ferraillage.

-    `dimension_left_offset`spécifie le décalage gauche de la cote à partir du dessin.

-    `dimension_right_offset`spécifie le décalage à droite de la cote à partir du dessin.

-    `dimension_top_offset`spécifie le décalage supérieur de la cote à partir du dessin.

-    `dimension_bottom_offset`spécifie le décalage inférieur de la cote à partir du dessin.


<div class="mw-collapsible toccolours mw-collapsed">

##### Exemple 


<div class="mw-collapsible-content">


```python
from pathlib import Path
import FreeCAD, Draft, Arch
from ColumnReinforcement import TwoTiesSixRebars
from ReinforcementDrawing import make_reinforcement_drawing

Rect = Draft.makeRectangle(400, 400)
Structure = Arch.makeStructure(Rect, height=1600)
Structure.ViewObject.Transparency = 80
FreeCAD.ActiveDocument.recompute()

# Créer des barres d'armature droites
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

rebars = Draft.get_objects_of_type(FreeCAD.ActiveDocument.Objects, "Rebar")

# Créer le schéma de barres d'armature
for drawing_view in ("Front", "Rear", "Left", "Right", "Top", "Bottom")   *
    make_reinforcement_drawing.makeReinforcementDrawing(
        structure=Structure,
        rebars_list=rebars,
        view=drawing_view,
        rebars_stroke_width=0.35,
        rebars_color_style="Automatic",
        rebars_color=(0.67, 0.0, 0.0),
        structure_stroke_width=0.5,
        structure_color_style="Automatic",
        structure_color=(0.3, 0.9, 0.91),
        drawing_left_offset=20,
        drawing_top_offset=20,
        drawing_min_right_offset=20,
        drawing_min_bottom_offset=20,
        drawing_max_width=0,                    # Il est défini sur 0 pour définir automatiquement la largeur par défaut en fonction d'autres paramètres
        drawing_max_height=0,                   # Il est défini sur 0 pour définir automatiquement la hauteur par défaut en fonction d'autres paramètres
        template_file=str(Path(make_reinforcement_drawing.__file__).parent.absolute() / "Templates" / "A4_Landscape_blank.svg"),
        dimension_left_offset=10,
        dimension_right_offset=10,
        dimension_top_offset=10,
        dimension_bottom_offset=10,
    )
```


</div>


</div>

#### Pour plusieurs structures 


```python
from ReinforcementDrawing.make_reinforcement_drawing import (
    makeStructuresReinforcementDrawing,
)

structure_drawing_page_dict = makeStructuresReinforcementDrawing(
    structure_list=None,
    rebars_list=None,
    view="Front",
    rebars_stroke_width=REBARS_STROKE_WIDTH,
    rebars_color_style=REBARS_COLOR_STYLE,
    rebars_color=REBARS_COLOR,
    structure_stroke_width=STRUCTURE_STROKE_WIDTH,
    structure_color_style=STRUCTURE_COLOR_STYLE,
    structure_color=STRUCTURE_COLOR,
    drawing_left_offset=DRAWING_LEFT_OFFSET,
    drawing_top_offset=DRAWING_TOP_OFFSET,
    drawing_min_right_offset=DRAWING_MIN_RIGHT_OFFSET,
    drawing_min_bottom_offset=DRAWING_MIN_BOTTOM_OFFSET,
    drawing_max_width=DRAWING_MAX_WIDTH,
    drawing_max_height=DRAWING_MAX_HEIGHT,
    template_file=TEMPLATE_FILE,
)
```

-   Il renvoie `structure_drawing_page_dict`, un dictionnaire avec la structure comme clé et la page de dessin des armatures correspondante comme valeur.

-    `structure_list`est la liste des objets structurels pour générer leur dessin des armatures. Si elles ne sont pas fournies, les structures seront sélectionnées à partir du document actif agissant comme hôte pour les objets d\'armature.

-    `rebars_list`est la liste des objets d\'armature à inclure dans le dessin. S\'ils ne sont pas fournis, les objets d\'armature ayant Host dans structure_list seront sélectionnés à partir du document actif.


<div class="mw-collapsible toccolours mw-collapsed">

##### Exemple 


<div class="mw-collapsible-content">


```python
from pathlib import Path
import FreeCAD, Draft, Arch
from ColumnReinforcement import TwoTiesSixRebars
from ReinforcementDrawing import make_reinforcement_drawing

Rect = Draft.makeRectangle(400, 400)
Structure1 = Arch.makeStructure(Rect, height=1600)
Structure1.ViewObject.Transparency = 80
Structure2 = Arch.makeStructure(Rect, height=1600)
Structure2.ViewObject.Transparency = 80
Structure2.Placement = FreeCAD.Placement(FreeCAD.Vector(1000, 0, 0), FreeCAD.Rotation(FreeCAD.Vector(0, 0, 1), 0))
FreeCAD.ActiveDocument.recompute()

# Créer des barres d'armature droites
TwoTiesSixRebars.makeTwoTiesSixRebars(
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
    structure=Structure1,
    facename="Face6",
)

# Pour barres de renfort en forme de L avec le crochet dirigé le long de l'axe des x.
TwoTiesSixRebars.makeTwoTiesSixRebars(
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
    structure=Structure2,
    facename="Face6",
)

# Créer le schéma de barres d'armature
for drawing_view in ("Front", "Rear", "Left", "Right", "Top", "Bottom")   *
    make_reinforcement_drawing.makeStructuresReinforcementDrawing(
        structure_list=None,
        rebars_list=None,
        view=drawing_view,
        rebars_stroke_width=0.35,
        rebars_color_style="Automatic",
        rebars_color=(0.67, 0.0, 0.0),
        structure_stroke_width=0.5,
        structure_color_style="Automatic",
        structure_color=(0.3, 0.9, 0.91),
        drawing_left_offset=20,
        drawing_top_offset=20,
        drawing_min_right_offset=20,
        drawing_min_bottom_offset=20,
        drawing_max_width=0,                    # Il est défini sur 0 pour définir automatiquement la largeur par défaut en fonction d'autres paramètres
        drawing_max_height=0,                   # Il est défini sur 0 pour définir automatiquement la hauteur par défaut en fonction d'autres paramètres
        template_file=str(Path(make_reinforcement_drawing.__file__).parent.absolute() / "Templates" / "A4_Landscape_blank.svg"),
        dimension_left_offset=10,
        dimension_right_offset=10,
        dimension_top_offset=10,
        dimension_bottom_offset=10,
    )
```


</div>


</div>

# <img alt="" src=images/Arch_Rebar_Dimensioning.svg  style="width   *32px;"> Dimensions des armatures 

## Utilisation 

1\. Ouvrez le modèle FreeCAD contenant les barres d\'armature créées à l\'aide de [Addon Reinforcement](Reinforcement_Addon/fr.md).

2\. Dans la console FreeCAD Python, copiez l\'extrait de code ci-dessous pour générer le dessin et la cotation des armatures à partir de différentes vues pour chaque élément [Arch Structure](Arch_Structure/fr.md). 
```python
from ReinforcementDrawing.make_reinforcement_drawing import (
    makeStructuresReinforcementDrawing,
)

for view in ("Front", "Rear", "Left", "Right", "Top", "Bottom")   *
    struct_drawing_page_dict = makeStructuresReinforcementDrawing(
        view=view, perform_dimensioning=True
    )
    for drawing_page in struct_drawing_page_dict.values()   *
        drawing_view = drawing_page.Views[0]
        drawing_view.setExpression(
            "LeftOffset",
            u".Template.Width.Value / 2 - .Width.Value * .Scale / 2",
        )
        drawing_view.setExpression(
            "TopOffset",
            u".Template.Height.Value / 2 - .Height.Value * .Scale / 2",
        )
        drawing_view.recompute(True)
        drawing_page.recompute(True)

```

## L\'objet ReinforcementDimensioning 

Un objet Rebar Vue Dimensionnement SVG.

### Propriétés 

-    **ParentDrawingView**   * l\'objet ReinforcementDrawingView parent contenant le dessin de l\'objet [Rebar](Arch_Rebar/fr.md).

-    **Rebar**   * L\'objet [Rebar](Arch_Rebar/fr.md) pour effectuer le dimensionnement.

-    **WayPointsType**   * Le type de ligne de cote WayPoints. Il peut être \"Automatique\" (pour effectuer automatiquement le dimensionnement de l\'objet [Rebar](Arch_Rebar/fr.md)) ou \"Personnalisé\" pour utiliser **WayPoints** pour effectuer le dimensionnement.

-    **WayPoints**   * Une liste de points vectoriels à utiliser pour générer une ligne de cote.

-    **TextPositionType**   * Le type de position du texte de cote. Il peut s\'agir de \"StartOfLine\", \"MidOfLine\" ou \"EndOfLine\".

-    **DimensionFormat**   * Le format de l\'étiquette de dimension.

   Exemple    * "%M %C⌀%D,span=%S"
   Ici    *  %M -> Rebar.Mark
         %C -> Rebar.Amount
         %D -> Rebar.Diameter
         %S -> Rebar span length

-    **Font**   * la famille de polices de l\'étiquette de dimension.

-    **FontSize**   * La taille de la police de l\'étiquette de dimension.

-    **StrokeWidth**   * La largeur du trait de la ligne de cote.

-    **LineStyle**   * Le style de trait de la ligne de cote. Il peut s\'agir de \"Continuous\", \"Dash\", \"Dot\", \"DashDot\" ou \"DashDotDot\".

-    **LineColor**   * La couleur de la ligne de cote.

-    **TextColor**   * La couleur de l\'étiquette de dimension.

-    **LineStartSymbol**   * Le symbole de début de la ligne de cote. Il peut s\'agir de \"FilledArrow\", \"Tick\", \"Dot\" ou \"None\".

-    **LineEndSymbol**   * Le symbole de fin de la ligne de cote. Il peut s\'agir de \"FilledArrow\", \"Tick\", \"Dot\" ou \"None\".

-    **LineMidPointSymbol**   * Le symbole des milieux de la ligne de cote. Il peut s\'agir de \"Tick\", \"Dot\" ou \"None\".

-    **DimensionLeftOffset**   * le décalage à gauche pour la cotation automatique des armatures.

-    **DimensionRightOffset**   * le bon décalage pour la cotation automatique des armatures.

-    **DimensionTopOffset**   * le décalage supérieur pour la cotation automatique des armatures.

-    **DimensionBottomOffset**   * Le décalage inférieur pour la cotation automatique des armatures.

-    **SingleRebar_LineStartSymbol**   * Le symbole de début de ligne de cote, dans le cas d\'une seule armature est visible. Il peut s\'agir de \"FilledArrow\", \"Tick\", \"Dot\" ou \"None\". Il est utilisé uniquement lorsque **WayPointsType** est défini sur \"Automatique\".

-    **SingleRebar_LineEndSymbol**   * Le symbole de fin de ligne de cote, en cas d\'armature simple, est visible. Il peut s\'agir de \"FilledArrow\", \"Tick\", \"Dot\" ou \"None\". Il est utilisé uniquement lorsque **WayPointsType** est défini sur \"Automatique\".

-    **MultiRebar_LineStartSymbol**   * Le symbole de début de ligne de cote, si plusieurs armatures sont visibles. Il peut s\'agir de \"FilledArrow\", \"Tick\", \"Dot\" ou \"None\". Il est utilisé uniquement lorsque **WayPointsType** est défini sur \"Automatique\".

-    **MultiRebar_LineEndSymbol**   * Le symbole de fin de ligne de cote, si plusieurs barres d\'armature sont visibles. Il peut s\'agir de \"FilledArrow\", \"Tick\", \"Dot\" ou \"None\". Il est utilisé uniquement lorsque **WayPointsType** est défini sur \"Automatique\".

-    **SingleRebar_OuterDimension**   * Indique si les lignes de cote doivent être en dehors du dessin d\'armature, dans le cas où une seule armature est visible. Il est utilisé uniquement lorsque **WayPointsType** est défini sur \"Automatique\".

-    **MultiRebar_OuterDimension**   * Indique si les lignes de cote doivent être en dehors du dessin d\'armature, dans le cas où plusieurs armatures sont visibles. Il est utilisé uniquement lorsque **WayPointsType** est défini sur \"Automatique\".

-    **SingleRebar_TextPositionType**   * il spécifie le type de position de l\'étiquette de cote, dans le cas où une seule armature est visible. Il peut s\'agir de \"StartOfLine\", \"MidOfLine\" ou \"EndOfLine\". Il est utilisé uniquement lorsque **WayPointsType** est défini sur \"Automatique\".

-    **MultiRebar_TextPositionType**   * Il spécifie le type de position de l\'étiquette de dimension, dans le cas où plusieurs armatures sont visibles. Il peut s\'agir de \"StartOfLine\", \"MidOfLine\" ou \"EndOfLine\". Il est utilisé uniquement lorsque **WayPointsType** est défini sur \"Automatique\".

## Script 


**Voir aussi    ***

[Arch API](Arch_API/fr.md), [API de renforts](Reinforcement_API/fr.md) et [FreeCAD Scripts de Base](FreeCAD_Scripting_Basics/fr.md).

Les fonctions dimensions de Reinforcement peuvent être utilisées dans des [macros](macros/fr.md) et dans la console [Python](Python/fr.md) en utilisant les fonctions suivantes    *

### Créer un objet Reinforcement dimensionnement 


```python
from ReinforcementDrawing.ReinforcementDimensioning import (
    makeReinforcementDimensioningObject,
)

dimension_object = makeReinforcementDimensioningObject(
    rebar,
    parent_drawing_view,
    drawing_page=None,
    dimension_label_format="%M %C⌀%D,span=%S",
    dimension_font_family="DejaVu Sans",
    dimension_font_size=3,
    dimension_stroke_width=0.25,
    dimension_line_style="Continuous",
    dimension_line_color=(0.0, 0.0, 0.50),
    dimension_text_color=(0.0, 0.33, 0.0),
    dimension_single_rebar_line_start_symbol="None",
    dimension_single_rebar_line_end_symbol="FilledArrow",
    dimension_multi_rebar_line_start_symbol="FilledArrow",
    dimension_multi_rebar_line_end_symbol="FilledArrow",
    dimension_line_mid_point_symbol="Dot",
    dimension_left_offset_increment=10,
    dimension_right_offset_increment=10,
    dimension_top_offset_increment=10,
    dimension_bottom_offset_increment=10,
    dimension_single_rebar_outer_dim=False,
    dimension_multi_rebar_outer_dim=True,
    dimension_single_rebar_text_position_type="StartOfLine",
    dimension_multi_rebar_text_position_type="MidOfLine",
)
```

-   Crée et renvoie un objet `ReinforcementDimensioning` pour l\'objet `rebar` donné.

-    `parent_drawing_view`est l\'objet `ReinforcementDrawingView` contenant un dessin de l\'objet `rebar`.

-    `drawing_page`est l\'objet de type TechDraw    *   * DrawPage utilisé pour afficher `parent_drawing_view`.

-    `dimension_label_format`est le format utilisé pour l\'étiquette de dimension.

   Exemple    * "%M %C⌀%D,span=%S"
   Ici    *  %M -> Rebar.Mark
         %C -> Rebar.Amount
         %D -> Rebar.Diameter
         %S -> Rebar span length

-    `dimension_font_family`est la famille de polices de l\'étiquette de dimension.

-    `dimension_font_size`est la taille de la police de l\'étiquette de dimension.

-    `dimension_stroke_width`est la largeur du trait de la ligne de cote.

-    `dimension_line_style`est le style de trait de la ligne de cote. Il peut s\'agir de \"Continuous\", \"Dash\", \"Dot\", \"DashDot\" ou \"DashDotDot\".

-    `dimension_line_color`est la couleur de la ligne de cote.

   Format    * (r, g, b)
   La valeur de r, g, b doit être comprise entre 0 et 1, vous devrez peut-être diviser la valeur de r, g, b par 255 pour obtenir sa valeur entre 0 et 1
   Assurez-vous que r, g, b soient flottants

-    `dimension_text_color`est la couleur de l\'étiquette de dimension.

-    `dimension_single_rebar_line_start_symbol`est le symbole de début de la ligne de cote, dans le cas où une seule armature est visible. Il peut s\'agir de \"FilledArrow\", \"Tick\", \"Dot\" ou \"None\".

-    `dimension_single_rebar_line_end_symbol`est le symbole de fin de ligne de cote, si une seule armature est visible. Il peut s\'agir de \"FilledArrow\", \"Tick\", \"Dot\" ou \"None\".

-    `dimension_multi_rebar_line_start_symbol`est le symbole de début de ligne de cote, dans le cas où plusieurs armatures sont visibles. Il peut s\'agir de \"FilledArrow\", \"Tick\", \"Dot\" ou \"None\".

-    `dimension_multi_rebar_line_end_symbol`est le symbole de fin de ligne de cote, au cas où plusieurs armatures seraient visibles. Il peut s\'agir de \"FilledArrow\", \"Tick\", \"Dot\" ou \"None\".

-    `dimension_line_mid_point_symbol`est le symbole du milieu de la ligne de cote. Il peut s\'agir de \"Tick\", \"Dot\" ou \"None\".

-    `dimension_left_offset_increment`est l\'incrément du décalage gauche pour éloigner chaque nouvelle étiquette de cote du dessin.

-    `dimension_right_offset_increment`est l\'incrément du décalage droit pour éloigner chaque nouvelle étiquette de cote du dessin.

-    `dimension_top_offset_increment`est l\'incrément du décalage supérieur pour éloigner chaque nouvelle étiquette de cote du dessin.

-    `dimension_bottom_offset_increment`est l\'incrément du décalage inférieur pour éloigner chaque nouvelle étiquette de cote du dessin.

-    `dimension_single_rebar_outer_dim`spécifie si les lignes de cote doivent être en dehors du dessin d\'armature, dans le cas où une seule armature est visible.

-    `dimension_multi_rebar_outer_dim`spécifie si les lignes de cote doivent être en dehors du dessin d\'armature, dans le cas où plusieurs armatures sont visibles.

-    `dimension_single_rebar_text_position_type`spécifie le type de position de l\'étiquette de cote, si une seule armature est visible. Il peut s\'agir de \"StartOfLine\", \"MidOfLine\" ou \"EndOfLine\".

-    `dimension_multi_rebar_text_position_type`spécifie le type de position de l\'étiquette de cote, si plusieurs armatures sont visibles. Il peut s\'agir de \"StartOfLine\", \"MidOfLine\" ou \"EndOfLine\".


<div class="mw-collapsible toccolours mw-collapsed">

##### Exemple 


<div class="mw-collapsible-content">


```python
from pathlib import Path
import FreeCAD, Draft, Arch
from ColumnReinforcement import TwoTiesSixRebars
from ReinforcementDrawing import make_reinforcement_drawing
from ReinforcementDrawing.ReinforcementDimensioning import (
    makeReinforcementDimensioningObject,
)

Rect = Draft.makeRectangle(400, 400)
Structure = Arch.makeStructure(Rect, height=1600)
Structure.ViewObject.Transparency = 80
FreeCAD.ActiveDocument.recompute()

# Créer des barres d'armature droites
TwoTiesSixRebars.makeTwoTiesSixRebars(
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

rebars = Draft.get_objects_of_type(FreeCAD.ActiveDocument.Objects, "Rebar")

# Créer le schéma de barres d'armature
drawing_page = make_reinforcement_drawing.makeReinforcementDrawing(
    structure=Structure,
    rebars_list=rebars,
    view="Front",
    rebars_stroke_width=0.35,
    rebars_color_style="Automatic",
    rebars_color=(0.67, 0.0, 0.0),
    structure_stroke_width=0.5,
    structure_color_style="Automatic",
    structure_color=(0.3, 0.9, 0.91),
    drawing_left_offset=20,
    drawing_top_offset=20,
    drawing_min_right_offset=20,
    drawing_min_bottom_offset=20,
    drawing_max_width=0,                    # Il est défini sur 0 pour définir automatiquement la largeur par défaut en fonction d'autres paramètres
    drawing_max_height=0,                   # Il est défini sur 0 pour définir automatiquement la hauteur par défaut en fonction d'autres paramètres
    template_file=str(Path(make_reinforcement_drawing.__file__).parent.absolute() / "Templates" / "A4_Landscape_blank.svg"),
    dimension_left_offset=10,
    dimension_right_offset=10,
    dimension_top_offset=10,
    dimension_bottom_offset=10,
)

visible_rebars = drawing_page.Views[0].VisibleRebars

# Créer le dimensionnement des armatures pour une seule armature
makeReinforcementDimensioningObject(
    visible_rebars[0],
    parent_drawing_view,
    drawing_page=None,
    dimension_label_format="%M %C⌀%D,span=%S",
    dimension_font_family="DejaVu Sans",
    dimension_font_size=3,
    dimension_stroke_width=0.25,
    dimension_line_style="Continuous",
    dimension_line_color=(0.0, 0.0, 0.50),
    dimension_text_color=(0.0, 0.33, 0.0),
    dimension_single_rebar_line_start_symbol="None",
    dimension_single_rebar_line_end_symbol="FilledArrow",
    dimension_multi_rebar_line_start_symbol="FilledArrow",
    dimension_multi_rebar_line_end_symbol="FilledArrow",
    dimension_line_mid_point_symbol="Dot",
    dimension_left_offset_increment=10,
    dimension_right_offset_increment=10,
    dimension_top_offset_increment=10,
    dimension_bottom_offset_increment=10,
    dimension_single_rebar_outer_dim=False,
    dimension_multi_rebar_outer_dim=True,
    dimension_single_rebar_text_position_type="StartOfLine",
    dimension_multi_rebar_text_position_type="MidOfLine",
)

# Créer le dimensionnement des armatures pour toutes les armatures visibles sur la vue de dessin
for visible_rebar in visible_rebars   *
    makeReinforcementDimensioningObject(
        visible_rebar,
        parent_drawing_view,
        drawing_page=None,
        dimension_label_format="%M %C⌀%D,span=%S",
        dimension_font_family="DejaVu Sans",
        dimension_font_size=3,
        dimension_stroke_width=0.25,
        dimension_line_style="Continuous",
        dimension_line_color=(0.0, 0.0, 0.50),
        dimension_text_color=(0.0, 0.33, 0.0),
        dimension_single_rebar_line_start_symbol="None",
        dimension_single_rebar_line_end_symbol="FilledArrow",
        dimension_multi_rebar_line_start_symbol="FilledArrow",
        dimension_multi_rebar_line_end_symbol="FilledArrow",
        dimension_line_mid_point_symbol="Dot",
        dimension_left_offset_increment=10,
        dimension_right_offset_increment=10,
        dimension_top_offset_increment=10,
        dimension_bottom_offset_increment=10,
        dimension_single_rebar_outer_dim=False,
        dimension_multi_rebar_outer_dim=True,
        dimension_single_rebar_text_position_type="StartOfLine",
        dimension_multi_rebar_text_position_type="MidOfLine",
    )
```


</div>


</div>







[Category   *External Command Reference](Category_External_Command_Reference.md) [Category   *Reinforcement](Category_Reinforcement.md)



---
![](images/Right_arrow.png) [documentation index](../README.md) > [External Command Reference](Category_External Command Reference.md) > [Reinforcement](Category_Reinforcement.md) > [Arch](Arch_Workbench.md) > Arch Rebar Drawing Dimensioning/fr
