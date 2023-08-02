---
- GuiCommand:
   Name: Arch Rebar Drawing
   Name/fr: Arch Dessin d'armature
   MenuLocation: Arch -> Rebar
   Workbenches: Arch_Workbench/fr, BIM_Workbench/fr
   SeeAlso: Arch_Rebar_Dimensioning/fr, Reinforcement_Addon/fr
   Version: 0.19
---

# Arch Rebar Drawing/fr

Remarque: le travail ci-dessous est présent dans la branche de développement de l\'atelier Reinforcement [ici](https://github.com/amrit3701/FreeCAD-Reinforcement/tree/develop)

## Description

L\'outil [Dessin d\'armature](Arch_Rebar_Drawing/fr.md) permet à l\'utilisateur de créer un dessin d\'armatures.

Cette commande fait partie de l\'[extension Reinforcement](Reinforcement_Addon/fr.md), un [atelier externe](External_workbenches/fr.md) que vous pouvez installer avec le <img alt="" src=images/Std_AddonMgr.svg  style="width:24px;"> [Gestionnaire des extensions](Std_AddonMgr/fr.md) via le menu **Outils → Gestionnaire des extensions → Reinforcement**.

<img alt="" src=images/Arch_Rebar_Drawing_example.svg  style="width:800px;">



*Dessin et dimensionnement des armatures*

## Utilisation

1\. Ouvrez le modèle FreeCAD contenant les barres d\'armature créées à l\'aide de l\'[extension Reinforcement](Reinforcement_Addon/fr.md).

2\. Dans la console FreeCAD Python, copiez l\'extrait de code ci-dessous pour générer le dessin à partir de différentes vues pour chaque élément [Arch Structure](Arch_Structure/fr.md). 
```python
from ReinforcementDrawing.make_reinforcement_drawing import (
    makeStructuresReinforcementDrawing,
)

for view in ("Front", "Rear", "Left", "Right", "Top", "Bottom"):
    makeStructuresReinforcementDrawing(view=view)
```

## Objet ReinforcementDrawingView 

Un objet de la vue SVG Dessin des armatures.

### Propriétés

-    {{PropertyData/fr|Structure}}: L\'objet de structure agissant en tant qu\'hôte pour les armatures à inclure dans le dessin.

-    {{PropertyData/fr|Rebars}}: La liste des objets d\'armature à inclure dans le dessin.

-    {{PropertyData/fr|View}}: La vue du dessin de ferraillage à générer. Il peut s\'agir de \"Front\", \"Rear\", \"Left\", \"Right\", \"Top\" ou \"Bottom\".

-    {{PropertyData/fr|PositionType}}: Le type de position du dessin d\'armature sur le gabarit. Il peut être \"Automatic\" pour calculer l\'emplacement du dessin en utilisant {{PropertyData/fr|LeftOffset}}, {{PropertyData/fr|TopOffset}}, {{PropertyData/fr|MinRightOffset}} et {{PropertyData/fr|MinBottomOffset}} OU \"Custom\" pour définir l\'emplacement en utilisant {{PropertyData/fr|X}} et {{PropertyData/fr|Y}}.

-    {{PropertyData/fr|RebarsStrokeWidth}}: La largeur de trait des armatures dans le svg de dessin d\'armature.

-    {{PropertyData/fr|RebarsColorStyle}}: Le style de couleur des armatures dans le svg de dessin d\'armature. Réglez-le sur \"Automatic\" pour sélectionner automatiquement la couleur des armatures OU \"Custom\" pour choisir la valeur de couleur de la forme à partir de {{PropertyData/fr|RebarsColor}}.

-    {{PropertyData/fr|RebarsColor}}: La couleur des armatures dans le svg de dessin d\'armature.

-    {{PropertyData/fr|StructureStrokeWidth}}: La largeur de trait de la structure dans le svg de dessin d\'armature.

-    {{PropertyData/fr|StructureColorStyle}}: Le style de couleur de la structure dans le svg de dessin d\'armature. Réglez-le sur \"Automatic\" pour sélectionner automatiquement la couleur des armatures, \"Custom\" pour choisir la valeur de couleur de la forme de {{PropertyData/fr|StructureColor}} OU \"None\" pour ne pas remplir la structure.

-    {{PropertyData/fr|StructureColor}}: La couleur de la structure dans le svg de dessin d\'armature.

-    {{PropertyData/fr|Template}}: Le modèle pour la vue de dessin de ferraillage.

-    {{PropertyData/fr|Width}}: La largeur du svg de vue de dessin d\'armature.

-    {{PropertyData/fr|Height}}: La hauteur du svg de vue de dessin d\'armature.

-    {{PropertyData/fr|LeftOffset}}: Le décalage gauche de la vue du dessin de ferraillage sur le gabarit.

-    {{PropertyData/fr|TopOffset}}: Le décalage supérieur de la vue du dessin de ferraillage sur le gabarit.

-    {{PropertyData/fr|MinRightOffset}}: Le décalage minimum à droite de la vue du dessin de ferraillage sur le gabarit.

-    {{PropertyData/fr|MinBottomOffset}}: Le décalage inférieur minimum de la vue du dessin d\'armature sur le gabarit.

-    {{PropertyData/fr|MaxWidth}}: La largeur maximale de la vue du dessin de ferraillage.

-    {{PropertyData/fr|MaxHeight}}: La hauteur maximale de la vue du dessin de ferraillage.

-    {{PropertyData/fr|VisibleRebars}}: La liste des objets d\'armature visibles dans la vue de dessin.

-    {{PropertyData/fr|DimensionLeftOffset}}: Le décalage gauche pour chaque nouvel objet ReinforcementDimensioning.

-    {{PropertyData/fr|DimensionRightOffset}}: Le décalage droit pour chaque nouvel objet ReinforcementDimensioning.

-    {{PropertyData/fr|DimensionTopOffset}}: Le décalage supérieur pour chaque nouvel objet ReinforcementDimensioning.

-    {{PropertyData/fr|DimensionBottomOffset}}: Le décalage inférieur pour chaque nouvel objet ReinforcementDimensioning.

## Script


**Voir aussi:**

[Arch API](Arch_API/fr.md), [Reinforcement API](Reinforcement_API/fr.md) et [FreeCAD Scripts de bases](FreeCAD_Scripting_Basics/fr.md).

L\'outil [Dessin d\'armature](Arch_Rebar_Drawing/fr.md) peut être utilisé dans [macros](macros/fr.md) et à partir de la console [Python](Python/fr.md) à l\'aide des fonctions suivantes:

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

-   Crée un objet `ReinforcementDrawingView` pour une liste d\'objets [Arch Structure](Arch_Structure/fr.md) et [Arch Armature personnalisée](Arch_Rebar/fr.md).

-   Il renvoie le `reinforcement_drawing_page` de type `TechDraw::DrawPage`.

-    `view`spécifie la vue du dessin à générer. Il peut s\'agir de \"Front\", \"Rear\", \"Left\", \"Right\", \"Top\" ou \"Bottom\".

-    `rebars_stroke_width`spécifie la largeur de trait des armatures dans le dessin svg.

-    `rebars_color_style`spécifie le style de couleur des armatures. Réglez-le sur \"Automatic\" pour sélectionner automatiquement la couleur des armatures ou sur \"Custom\" pour choisir la valeur de couleur de la forme à partir de la variable `rebars_color`.

-    `rebars_color`spécifie la couleur de remplissage des armatures dans le dessin svg.

   Format: (r, g, b)
   La valeur r, g, b doit être comprise entre 0 et 1, vous devrez peut-être diviser la valeur de r, g, b par 255 pour obtenir sa valeur entre 0 et 1
   Assurez-vous que r, g, b doivent être flottants
   Exemple: (0.67, 0.0, 0.0)

-    `structure_stroke_width`spécifie la largeur de trait de la structure dans le dessin svg.

-    `structure_color_style`spécifie le style de remplissage de la structure. Réglez-le sur \"Automatique\" pour sélectionner automatiquement la couleur de la structure ou \"Custom\" pour choisir la valeur de couleur de la structure à partir de la variable `structure_color`.

-    `structure_color`spécifie la couleur de remplissage de la structure dans le dessin svg. Format: (r, g, b)

-    `drawing_left_offset`spécifie le décalage gauche de la vue de dessin sur `template_file`.

-    `drawing_top_offset`spécifie le décalage supérieur de la vue de dessin sur `template_file`.

-    `drawing_min_right_offset`spécifie le décalage minimum à droite de la vue de dessin sur `template_file`.

-    `drawing_min_bottom_offset`spécifie le décalage inférieur minimum de la vue de dessin sur `template_file`.

-    `drawing_max_width`spécifie la largeur maximale du dessin sur `template_file`.

-    `drawing_max_height`spécifie la hauteur maximale du dessin sur `template_file`.

-    `template_file`est le fichier modèle à utiliser pour la page de dessin de ferraillage.

-    `dimension_left_offset`spécifie le décalage gauche de la cote par rapport au dessin.

-    `dimension_right_offset`spécifie le décalage droit de la cote par rapport au dessin.

-    `dimension_top_offset`spécifie le décalage supérieur de la cote à partir du dessin.

-    `dimension_bottom_offset`spécifie le décalage inférieur de la cote à partir du dessin.

##### Exemple


```python
from pathlib import Path
import FreeCAD, Draft, Arch
from ColumnReinforcement import TwoTiesSixRebars
from ReinforcementDrawing import make_reinforcement_drawing


# Cela ne fonctionne pas si la structure n'est pas basée sur une face.
# Structure = Arch.makeStructure(length=1000, width=400, height=400)

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
for drawing_view in ("Front", "Rear", "Left", "Right", "Top", "Bottom"):
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
        drawing_max_width=0,                    # It is set to 0 to automatically set default width based on other parameters
        drawing_max_height=0,                   # It is set to 0 to automatically set default height based on other parameters
        template_file=str(Path(make_reinforcement_drawing.__file__).parent.absolute() / "Templates" / "A4_Landscape_blank.svg"),
        dimension_left_offset=10,
        dimension_right_offset=10,
        dimension_top_offset=10,
        dimension_bottom_offset=10,
    )
```

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

-   Il renvoie `structure_drawing_page_dict`, un dictionnaire avec la structure comme clé et la page de dessin de ferraillage correspondante comme valeur.

-    `structure_list`est la liste des objets structurels pour générer leur dessin de ferraillage. Si elles ne sont pas fournies, les structures seront sélectionnées à partir du document actif agissant comme hôte pour les objets d\'armature.

-    `rebars_list`est la liste des objets d\'armature à inclure dans le dessin. S\'ils ne sont pas fournis, les objets d\'armature ayant Host dans structure_list seront sélectionnés à partir du document actif.

##### Exemple 


```python
from pathlib import Path
import FreeCAD, Draft, Arch
from ColumnReinforcement import TwoTiesSixRebars
from ReinforcementDrawing import make_reinforcement_drawing


# Cela ne fonctionne pas si la structure n'est pas basée sur une face.
# Structure = Arch.makeStructure(length=1000, width=400, height=400)

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
for drawing_view in ("Front", "Rear", "Left", "Right", "Top", "Bottom"):
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
        drawing_max_width=0,                    # It is set to 0 to automatically set default width based on other parameters
        drawing_max_height=0,                   # It is set to 0 to automatically set default height based on other parameters
        template_file=str(Path(make_reinforcement_drawing.__file__).parent.absolute() / "Templates" / "A4_Landscape_blank.svg"),
        dimension_left_offset=10,
        dimension_right_offset=10,
        dimension_top_offset=10,
        dimension_bottom_offset=10,
    )
```



---
⏵ [documentation index](../README.md) > [External Command Reference](Category_External Command Reference.md) > [Reinforcement](Category_Reinforcement.md) > [Arch](Arch_Workbench.md) > Arch Rebar Drawing/fr
