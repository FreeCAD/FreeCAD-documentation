---
- GuiCommand:/fr
   Name:Arch Rebar Dimensioning
   Name/fr:Arch Dimensions des armatures
   MenuLocation:Arch → Rebar → Rebar Dimensioning
   Workbenches:[Arch](Arch_Workbench/fr.md), [BIM](BIM_Workbench/fr.md)
   SeeAlso:[Arch Dessin d'armatures](Arch_Rebar_Drawing/fr.md), [Addon Reinforcement](Reinforcement_Addon/fr.md)
   Version:0.19
---

# Arch Rebar Dimensioning/fr

Remarque: le travail ci-dessous est présent dans la branche de développement de l\'atelier Reinforcement [ici](https://github.com/amrit3701/FreeCAD-Reinforcement/tree/develop)

## Description

L\'outil [Dimensionnement des armatures](Arch_Rebar_Dimensioning/fr.md) permet à l\'utilisateur de créer des cotations pour les armatures dans [Dessin d\'armatures](Arch_Rebar_Drawing/fr.md).

Cette commande fait partie de l\'[Addon Reinforcement](Reinforcement_Addon/fr.md), un [atelier externe](External_workbenches/fr.md) que vous pouvez installer avec le <img alt="" src=images/Std_AddonMgr.svg  style="width:24px;"> [Gestionnaire d\'Addon](Std_AddonMgr/fr.md) via le menu **Outils → Gestionnaire d'Addon → Reinforcement**.

<img alt="" src=images/Arch_Rebar_Drawing_Dimensioning_example.svg  style="width:1000px;">



*Dessin et dimensionnement des armatures*

## Utilisation

1\. Ouvrez le modèle FreeCAD contenant les barres d\'armature créées à l\'aide de [Addon Reinforcement](Reinforcement_Addon/fr.md).

2\. Dans la console FreeCAD Python, copiez l\'extrait de code ci-dessous pour générer le dessin et la cotation des armatures à partir de différentes vues pour chaque élément [Arch Structure](Arch_Structure/fr.md). 
```python
from ReinforcementDrawing.make_reinforcement_drawing import (
    makeStructuresReinforcementDrawing,
)

for view in ("Front", "Rear", "Left", "Right", "Top", "Bottom"):
    struct_drawing_page_dict = makeStructuresReinforcementDrawing(
        view=view, perform_dimensioning=True
    )
    for drawing_page in struct_drawing_page_dict.values():
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

Un objet de la vue SVG Dimensionnement des barres d\'armature.

### Propriétés

-    {{PropertyData/fr|ParentDrawingView}}: l\'objet ReinforcementDrawingView parent contenant le dessin de l\'objet [Rebar](Arch_Rebar/fr.md).

-    {{PropertyData/fr|Rebar}}: L\'objet [Rebar](Arch_Rebar/fr.md) pour effectuer le dimensionnement.

-    {{PropertyData/fr|WayPointsType}}: Le type de ligne de cote WayPoints. Il peut être \"Automatic\" (pour effectuer automatiquement le dimensionnement de l\'objet [Rebar](Arch_Rebar/fr.md)) ou \"Personnalisé\" pour utiliser {{PropertyData/fr|WayPoints}} pour effectuer le dimensionnement.

-    {{PropertyData/fr|WayPoints}}: Une liste de points vectoriels à utiliser pour générer une ligne de cote.

-    {{PropertyData/fr|TextPositionType}}: Le type de position du texte de cote. Il peut s\'agir de \"StartOfLine\", \"MidOfLine\" ou \"EndOfLine\".

-    {{PropertyData/fr|DimensionFormat}}: Le format de l\'étiquette de dimension.

   Exemple: "%M %C⌀%D,span=%S"
   Here: %M -> Rebar.Mark
         %C -> Rebar.Amount
         %D -> Rebar.Diameter
         %S -> Rebar span length

-    {{PropertyData/fr|Font}}: la famille de polices de l\'étiquette de dimension.

-    {{PropertyData/fr|FontSize}}: la taille de la police de l\'étiquette de dimension.

-    {{PropertyData/fr|StrokeWidth}}: La largeur du trait de la ligne de cote.

-    {{PropertyData/fr|LineStyle}}: Le style de trait de la ligne de cote. Il peut s\'agir de \"Continuous\", \"Dash\", \"Dot\", \"DashDot\" ou \"DashDotDot\".

-    {{PropertyData/fr|LineColor}}: La couleur de la ligne de cote.

-    {{PropertyData/fr|TextColor}}: La couleur de l\'étiquette de dimension.

-    {{PropertyData/fr|LineStartSymbol}}: Le symbole de début de la ligne de cote. Il peut s\'agir de \"FilledArrow\", \"Tick\", \"Dot\" ou \"None\".

-    {{PropertyData/fr|LineEndSymbol}}: Le symbole de fin de la ligne de cote. Il peut s\'agir de \"FilledArrow\", \"Tick\", \"Dot\" ou \"None\".

-    {{PropertyData/fr|LineMidPointSymbol}}: Le symbole des points médians de la ligne de cote. Il peut s\'agir de \"Tick\", \"Dot\" ou \"None\".

-    {{PropertyData/fr|DimensionLeftOffset}}: Le décalage gauche pour la cotation automatisée des armatures.

-    {{PropertyData/fr|DimensionRightOffset}}: le bon décalage pour la cotation automatique des armatures.

-    {{PropertyData/fr|DimensionTopOffset}}: le décalage supérieur pour la cotation automatique des armatures.

-    {{PropertyData/fr|DimensionBottomOffset}}: Le décalage inférieur pour la cotation automatique des armatures.

-    {{PropertyData/fr|SingleRebar_LineStartSymbol}}: Le symbole de début de ligne de cote, dans le cas d\'une seule armature est visible. Il peut s\'agir de \"FilledArrow\", \"Tick\", \"Dot\" ou \"None\". Il est utilisé uniquement lorsque {{PropertyData/fr|WayPointsType}} est défini sur \"Automatic\".

-    {{PropertyData/fr|SingleRebar_LineEndSymbol}}: Le symbole de fin de ligne de cote, en cas d\'armature simple, est visible. Il peut s\'agir de \"FilledArrow\", \"Tick\", \"Dot\" ou \"None\". Il est utilisé uniquement lorsque {{PropertyData/fr|WayPointsType}} est défini sur \"Automatic\".

-    {{PropertyData/fr|MultiRebar_LineStartSymbol}}: Le symbole de début de ligne de cote, si plusieurs armatures sont visibles. Il peut s\'agir de \"FilledArrow\", \"Tick\", \"Dot\" ou \"None\". Il est utilisé uniquement lorsque {{PropertyData/fr|WayPointsType}} est défini sur \"Automatic\".

-    {{PropertyData/fr|MultiRebar_LineEndSymbol}}: Le symbole de fin de ligne de cote, si plusieurs armatures sont visibles. Il peut s\'agir de \"FilledArrow\", \"Tick\", \"Dot\" ou \"None\". Il est utilisé uniquement lorsque {{PropertyData/fr|WayPointsType}} est défini sur \"Automatic\".

-    {{PropertyData/fr|SingleRebar_OuterDimension}}: Indique si les lignes de cote doivent être en dehors du dessin d\'armature, dans le cas où une seule armature est visible. Il est utilisé uniquement lorsque {{PropertyData/fr|WayPointsType}} est défini sur \"Automatic\".

-    {{PropertyData/fr|MultiRebar_OuterDimension}}: Indique si les lignes de cote doivent être en dehors du dessin d\'armature, dans le cas où plusieurs armatures sont visibles. Il est utilisé uniquement lorsque {{PropertyData/fr|WayPointsType}} est défini sur \"Automatic\".

-    {{PropertyData/fr|SingleRebar_TextPositionType}}: il spécifie le type de position de l\'étiquette de cote, dans le cas où une seule armature est visible. Il peut s\'agir de \"StartOfLine\", \"MidOfLine\" ou \"EndOfLine\". Il est utilisé uniquement lorsque {{PropertyData/fr|WayPointsType}} est défini sur \"Automatic\".

-    {{PropertyData/fr|MultiRebar_TextPositionType}}: Il spécifie le type de position de l\'étiquette de dimension, dans le cas où plusieurs armatures sont visibles. Il peut s\'agir de \"StartOfLine\", \"MidOfLine\" ou \"EndOfLine\". Il est utilisé uniquement lorsque {{PropertyData/fr|WayPointsType}} est défini sur \"Automatic\".

## Script


**Voir aussi:**

[Arch API](Arch_API/fr.md), [API des armatures](Reinforcement_API/fr.md), [Arch Dessin d\'armature](Arch_Rebar_Drawing/fr.md) et [Débuter avec les scripts FreeCAD](FreeCAD_Scripting_Basics/fr.md).

L\'outil [Dimensionnement des armatures](Arch_Rebar_Dimensioning/fr.md) peut être utilisé dans [macros](macros/fr.md) et à partir de la console [Python](Python/fr.md) à l\'aide des fonctions suivantes:

### Créer un objet de dimension d\'armature 


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

-   Crée et renvoie un objet `ReinforcementDimensioning` pour un objet `rebar` donné.

-    `parent_drawing_view`est l\'objet `ReinforcementDrawingView` contenant le dessin de l\'objet `rebar`.

-    `drawing_page`est l\'objet de type TechDraw::DrawPage utilisé pour afficher `parent_drawing_view`.

-    `dimension_label_format`est le format utilisé pour l\'étiquette de dimension.

   Exemple: "%M %C⌀%D,span=%S"
   Ici: %M -> Rebar.Mark
         %C -> Rebar.Amount
         %D -> Rebar.Diameter
         %S -> Rebar span length

-    `dimension_font_family`est la famille de polices de l\'étiquette de dimension.

-    `dimension_font_size`est la taille de la police de l\'étiquette de dimension.

-    `dimension_stroke_width`est la largeur du trait de la ligne de cote.

-    `dimension_line_style`est le style de trait de la ligne de cote. Il peut s\'agir de \"Continuous\", \"Dash\", \"Dot\", \"DashDot\" ou \"DashDotDot\".

-    `dimension_line_color`est la couleur de la ligne de cote.

   Format: (r, g, b)
   La valeur r, g, b doit être comprise entre 0 et 1, vous devrez peut-être diviser la valeur de r, g, b par 255 pour obtenir sa valeur entre 0 et 1
   Assurez-vous que r, g, b doivent être flottants

-    `dimension_text_color`est la couleur de l\'étiquette de dimension.

-    `dimension_single_rebar_line_start_symbol`est le symbole de début de la ligne de cote, si une seule armature est visible. Il peut s\'agir de \"FilledArrow\", \"Tick\", \"Dot\" ou \"None\".

-    `dimension_single_rebar_line_end_symbol`est le symbole de fin de ligne de cote, si une seule armature est visible. Il peut s\'agir de \"FilledArrow\", \"Tick\", \"Dot\" ou \"None\".

-    `dimension_multi_rebar_line_start_symbol`est le symbole de début de ligne de cote, dans le cas où plusieurs armatures sont visibles. Il peut s\'agir de \"FilledArrow\", \"Tick\", \"Dot\" ou \"None\".

-    `dimension_multi_rebar_line_end_symbol`est le symbole de fin de ligne de cote, au cas où plusieurs armatures seraient visibles. Il peut s\'agir de \"FilledArrow\", \"Tick\", \"Dot\" ou \"None\".

-    `dimension_line_mid_point_symbol`est le symbole des points médians de la ligne de cote. Il peut s\'agir de \"Tick\", \"Dot\" ou \"None\".

-    `dimension_left_offset_increment`est l\'incrément du décalage gauche pour éloigner chaque nouvelle étiquette de cote du dessin.

-    `dimension_right_offset_increment`est l\'incrément du décalage à droite pour éloigner chaque nouvelle étiquette de cote du dessin.

-    `dimension_top_offset_increment`est l\'incrément du décalage supérieur pour éloigner chaque nouvelle étiquette de cote du dessin.

-    `dimension_bottom_offset_increment`est l\'incrément du décalage inférieur pour éloigner chaque nouvelle étiquette de cote du dessin.

-    `dimension_single_rebar_outer_dim`spécifie si les lignes de cote doivent être en dehors du dessin d\'armature, dans le cas où une seule armature est visible.

-    `dimension_multi_rebar_outer_dim`spécifie si les lignes de cote doivent être en dehors du dessin d\'armature, dans le cas où plusieurs armatures sont visibles.

-    `dimension_single_rebar_text_position_type`spécifie le type de position de l\'étiquette de cote, si une seule armature est visible. Il peut s\'agir de \"StartOfLine\", \"MidOfLine\" ou \"EndOfLine\".

-    `dimension_multi_rebar_text_position_type`spécifie le type de position de l\'étiquette de cote, si plusieurs armatures sont visibles. Il peut s\'agir de \"StartOfLine\", \"MidOfLine\" ou \"EndOfLine\".

##### Exemple


```python
from pathlib import Path
import FreeCAD, Draft, Arch
from ColumnReinforcement import TwoTiesSixRebars
from ReinforcementDrawing import make_reinforcement_drawing
from ReinforcementDrawing.ReinforcementDimensioning import (
    makeReinforcementDimensioningObject,
)


# Cela ne fonctionne pas si la structure n'est pas basée sur une face.
# Structure = Arch.makeStructure(length=1000, width=400, height=400)

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
    drawing_max_width=0,                    # It is set to 0 to automatically set default width based on other parameters
    drawing_max_height=0,                   # It is set to 0 to automatically set default height based on other parameters
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
for visible_rebar in visible_rebars:
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







[<img src="images/Property.png" style="width:16px"> External Command Reference](Category_External_Command_Reference.md) [<img src="images/Property.png" style="width:16px"> Reinforcement](Category_Reinforcement.md)

---
[documentation index](../README.md) > [External Command Reference](Category_External Command Reference.md) > [Arch](Arch_Workbench.md) > Arch Rebar Dimensioning/fr
