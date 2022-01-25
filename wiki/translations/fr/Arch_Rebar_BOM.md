---
- GuiCommand:/fr
   Name:Arch Rebar BOM
   Name/fr:Arch Rebar Nomenclature armature
   MenuLocation:Reinforcement → Bill Of Material
   Workbenches:[Arch](Arch_Workbench/fr.md), [BIM](BIM_Workbench/fr.md)
   Version:0.19
   SeeAlso:[Reinforcement](Reinforcement_Workbench/fr.md), [Reinforcement Tableau des armatures](Reinforcement_Bar_Bending_Schedule/fr.md), [Arch Rebar Dimensions des armatures](Arch_Rebar_Drawing_Dimensioning/fr.md)
---

# Arch Rebar BOM/fr

## Description

L\'outil [Nomenclature (BOM)](Arch_Rebar_BOM/fr.md) permet à l\'utilisateur de créer une nomenclature de barres d\'armature.

Cette commande fait partie de l\'[atelier Reinforcement](Reinforcement_Workbench/fr.md), un [atelier externe](External_workbenches/fr.md) que vous pouvez installer avec le <img alt="" src=images/Std_AddonMgr.svg  style="width:24px;"> [Gestionnaire d\'Addon](Std_AddonMgr/fr.md) via le menu **Outils → Gestionnaire d'Addon → Reinforcement**.

<img alt="" src=images/Arch_Rebar_BOM_example.png  style="width:1000px;">



*Nomenclature de barres d'armature*

## Utilisation

1\. Sélectionnez les objets **<img src="images/Arch_Rebar.svg" width=16px> [Arch Armature personnalisée](Arch_Rebar/fr.md)** que vous souhaitez inclure dans la nomenclature ou sélectionnez les objets **<img src="images/Arch_Structure.svg" width=16px> [Arch Structure](Arch_Structure/fr.md)** pour inclure les objets **<img src="images/Arch_Rebar.svg" width=16px> [Arch Armature personnalisée](Arch_Rebar/fr.md)** hébergés par celui-ci dans la nomenclature. Si rien n\'est sélectionné, la nomenclature sera générée pour tous les **<img src="images/Arch_Rebar.svg" width=16px> [Arch Armature personnalisée](Arch_Rebar/fr.md)** et les objets Rebar2 présents dans le modèle.

2\. Sélectionnez ensuite **<img src="images/Arch_Rebar_BOM.svg" width=16px> [Bill Of Material](Arch_Rebar_BOM/fr.md)** dans les outils d\'armature.

3\. Une boîte de dialogue apparaîtra à l\'écran, comme indiqué ci-dessous.

<img alt="" src=images/BOMDialog_General.png  style="width:500px;">



*Boîte de dialogue pour l'outil de nomenclature de barres d'armature Arch*

4\. Modifiez les données en fonction de vos besoins.

5\. Pour modifier la **<img src="images/Arch_Rebar_BOM.svg" width=16px> [Bill Of Material](Arch_Rebar_BOM/fr.md)** des configurations SVG, cliquez sur **Edit SVG Configurations**. Une boîte de dialogue apparaîtra comme illustré ci-dessous.

<img alt="" src=images/BOMDialog_SVG.png  style="width:500px;">



*Boîte de dialogue pour l'édition de la configuration SVG de la nomenclature de Armature personnalisée *

6\. Modifiez les configurations **<img src="images/Arch_Rebar_BOM.svg" width=16px> [Bill Of Material](Arch_Rebar_BOM/fr.md)** SVG, puis cliquez sur **OK** pour appliquer les modifications.

7\. Cliquez sur **OK** ou **Apply** pour générer la nomenclature des armatures.

8\. Cliquez sur **Cancel** pour quitter la boîte de dialogue.

## Propriétés

**Général:**

-    {{PropertyData/fr|Column Headers}}: dictionnaire avec column\_data comme clé et tuple (column\_display\_header, column\_sequence) comme valeur.

-    {{PropertyData/fr|Column Units}}: dictionnaire avec des clés : \"Diameter\", \"RebarLength\", \"RebarsTotalLength\" et leurs unités correspondantes comme valeur.

-    {{PropertyData/fr|Diameter Weight Map}}: dictionnaire avec le diamètre comme clé et le poids correspondant comme valeur.

-    {{PropertyData/fr|Rebar Length Type}}: type de longueur d\'armature spécifie le type de longueur d\'armature utilisé pour les calculs de nomenclature, c\'est-à-dire \"RealLength\" ou \"LengthWithSharpEdges\".

-    {{PropertyData/fr|Rebar Objects}}: liste d\'objets ArchRebar et/ou rebar2 et/ou structures (pour sélectionner ArchRebar dans cette structure).

**SVG :**

-    {{PropertyData/fr|Font Family}}: famille de polices de texte dans la table BOM SVG.

-    {{PropertyData/fr|Font Filename}}: nom de fichier de police correspondant à la famille de polices requise en mode console.

-    {{PropertyData/fr|Font Size}}: taille de police en mm.

-    {{PropertyData/fr|Column Width}}: largeur de chaque colonne dans la table BOM SVG.

-    {{PropertyData/fr|Row Height}}: hauteur de chaque ligne dans la table BOM SVG.

-    {{PropertyData/fr|Left Offset}}: décalage gauche de la table BOM SVG.

-    {{PropertyData/fr|Top Offset}}: décalage supérieur de la table BOM SVG.

-    {{PropertyData/fr|Minimum Right Offset}}: décalage minimal à droite de la table BOM SVG.

-    {{PropertyData/fr|Minimum Bottom Offset}}: décalage inférieur minimum de la table BOM SVG.

-    {{PropertyData/fr|Maximum Width}}: largeur maximale de la table BOM SVG.

-    {{PropertyData/fr|Maximum Height}}: hauteur maximale de la table BOM SVG.

-    {{PropertyData/fr|Template File}}: fichier svg de modèle pour BOM SVG.

-    {{PropertyData/fr|Output File}}: fichier de sortie SVG BOM.

## Script


**Voir aussi :**

[Arch API](Arch_API/fr.md), [API de renforts](Reinforcement_API/fr.md) et [FreeCAD Scripts de Base](FreeCAD_Scripting_Basics/fr.md).

L\'outil [Bill Of Material](Arch_Rebar_BOM/fr.md) peut être utilisé dans des [macros](macros/fr.md) et à partir de la console [Python](Python/fr.md) à l\'aide des fonctions suivantes :

### Créer une feuille de nomenclature 


```python
bom_spreadsheet = makeBillOfMaterial(
    column_headers=None,
    column_units=None,
    dia_weight_map=None,
    rebar_length_type=None,
    rebar_objects=None,
    obj_name="RebarBillOfMaterial",
)
```

-   Crée un `RebarBillOfMaterial` objet de feuille de calcul pour un `rebar_objects` donné.
    -   Si la liste `rebar_objects` est vide, la feuille de calcul `RebarBillOfMaterial` sera créée pour toutes les armatures d\'un modèle.

-    `column_headers`est un dictionnaire avec des clés : \"Host\", \"Mark\", \"RebarsCount\", \"Diameter\", \"RebarLength\", \"RebarsTotalLength\" et les valeurs sont des tuple de column\_header et leur numéro de séquence.

   Exemple : {
                "Host": ("Member", 1),
                "Mark": ("Mark", 2),
                "RebarsCount": ("No. of Rebars", 3),
                "Diameter": ("Diameter in mm", 4),
                "RebarLength": ("Length in m/piece", 5),
                "RebarsTotalLength": ("Total Length in m", 6),
            }
            mettez le numéro de séquence de la colonne à 0 pour cacher la colonne.

-    `column_units`est un dictionnaire avec des clés : \"Diameter\", \"RebarLength\", \"RebarsTotalLength\" et leurs unités correspondantes comme valeur.

   Exemple : {
                "Diameter": "mm",
                "RebarLength": "m",
                "RebarsTotalLength": "m",
            }

-    `dia_weight_map`est un dictionnaire dont le diamètre est la clé et le poids correspondant la valeur.

   Syntaxe : {
                6: FreeCAD.Units.Quantity("0.222 kg/m"),
                8: FreeCAD.Units.Quantity("0.395 kg/m"),
                10: FreeCAD.Units.Quantity("0.617 kg/m"),
                12: FreeCAD.Units.Quantity("0.888 kg/m"),
                ...,
            }

-    `rebar_length_type`spécifie le type de longueur d\'armature utilisé pour les calculs de nomenclature; il peut s\'agir de \"RealLength\" ou \"LengthWithSharpEdges\".

-    `rebar_objects`est une liste d\'objets ArchRebar et/ou rebar2 et/ou structures (pour sélectionner ArchRebar dans cette structure).

#### Exemple


```python
import FreeCAD, Draft, Arch
from ColumnReinforcement import TwoTiesSixRebars
from BillOfMaterial import BillOfMaterial_Spreadsheet


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
    structure=Structure1,
    facename="Face6",
)


# Pour les barres de renfort en forme de L avec le crochet dirigé le long de l'axe des x.
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
    structure=Structure2,
    facename="Face6",
)

COLUMN_UNITS = {
    "Diameter": "mm",
    "RebarLength": "m",
    "RebarsTotalLength": "m",
}

COLUMN_HEADERS = {
    "Host": ("Member", 1),
    "Mark": ("Mark", 2),
    "RebarsCount": ("No. of Rebars", 3),
    "Diameter": ("Diameter in " + COLUMN_UNITS["Diameter"], 4),
    "RebarLength": ("Length in " + COLUMN_UNITS["RebarLength"] + "/piece", 5),
    "RebarsTotalLength": ("Total Length in " + COLUMN_UNITS["RebarsTotalLength"], 6),
}

DIA_WEIGHT_MAP = {
    6: FreeCAD.Units.Quantity("0.222 kg/m"),
    8: FreeCAD.Units.Quantity("0.395 kg/m"),
    10: FreeCAD.Units.Quantity("0.617 kg/m"),
    12: FreeCAD.Units.Quantity("0.888 kg/m"),
    14: FreeCAD.Units.Quantity("1.206 kg/m"),
    16: FreeCAD.Units.Quantity("1.578 kg/m"),
    18: FreeCAD.Units.Quantity("2.000 kg/m"),
    20: FreeCAD.Units.Quantity("2.466 kg/m"),
    22: FreeCAD.Units.Quantity("2.980 kg/m"),
    25: FreeCAD.Units.Quantity("3.854 kg/m"),
    28: FreeCAD.Units.Quantity("4.830 kg/m"),
    32: FreeCAD.Units.Quantity("6.313 kg/m"),
    36: FreeCAD.Units.Quantity("7.990 kg/m"),
    40: FreeCAD.Units.Quantity("9.864 kg/m"),
    45: FreeCAD.Units.Quantity("12.490 kg/m"),
    50: FreeCAD.Units.Quantity("15.410 kg/m"),
}

# Créer une feuille de nomenclature pour toutes les armatures d'un modèle
BillOfMaterial_Spreadsheet.makeBillOfMaterial(
    column_headers=COLUMN_HEADERS,
    column_units=COLUMN_UNITS,
    dia_weight_map=DIA_WEIGHT_MAP,
    rebar_length_type="RealLength",
)

# Créer une feuille de nomenclature pour les barres d'armature dans Structure1
BillOfMaterial_Spreadsheet.makeBillOfMaterial(
    column_headers=COLUMN_HEADERS,
    column_units=COLUMN_UNITS,
    dia_weight_map=DIA_WEIGHT_MAP,
    rebar_length_type="LengthWithSharpEdges",
    rebar_objects=[Structure1],
)

```

### Créer une nomenclature SVG 


```python
makeBillOfMaterialSVG(
    column_headers: Optional[Dict[str, Tuple[str, int]]] = None,
    column_units: Optional[Dict[str, str]] = None,
    dia_weight_map: Optional[Dict[float, FreeCAD.Units.Quantity]] = None,
    rebar_length_type: Optional[
        Literal["RealLength", "LengthWithSharpEdges"]
    ] = None,
    font_family: Optional[str] = None,
    font_filename: Optional[str] = None,
    font_size: Optional[float] = None,
    column_width: Optional[float] = None,
    row_height: Optional[float] = None,
    bom_left_offset: Optional[float] = None,
    bom_top_offset: Optional[float] = None,
    bom_min_right_offset: Optional[float] = None,
    bom_min_bottom_offset: Optional[float] = None,
    bom_table_svg_max_width: Optional[float] = None,
    bom_table_svg_max_height: Optional[float] = None,
    template_file: Optional[str] = None,
    output_file: Optional[str] = None,
    rebar_objects: Optional[List] = None,
    reinforcement_group_by: Optional[Literal["Mark", "Host"]] = None,
    return_svg_only: bool = False,
) -> BOMContent
```

-   Crée et renvoie un objet RebarBillOfMaterial\_SVG `BOMContent` pour un `rebar_objects` donné.
    -   Si la liste `rebar_objects` est vide, alors l\'objet `BOMContent` sera créé pour toutes les armatures d\'un modèle.

-    `column_headers`est un dictionnaire avec les clés : \"Host\", \"Mark\", \"RebarsCount\", \"Diameter\", \"RebarLength\", \"RebarsTotalLength\" et les valeurs sont un tuple de column\_header et leur numéro de séquence.

   Exemple : {
                "Host": ("Member", 1),
                "Mark": ("Mark", 2),
                "RebarsCount": ("No. of Rebars", 3),
                "Diameter": ("Diameter in mm", 4),
                "RebarLength": ("Length in m/piece", 5),
                "RebarsTotalLength": ("Total Length in m", 6),
            }
            mettez le numéro de séquence de la colonne sur 0 pour masquer la colonne.

-    `column_units`est un dictionnaire avec les clés : \"Diameter\", \"RebarLength\", \"RebarsTotalLength\" et leurs unités correspondantes comme valeur.

   Exemple : {
                "Diameter": "mm",
                "RebarLength": "m",
                "RebarsTotalLength": "m",
            }

-    `dia_weight_map`est un dictionnaire avec le diamètre comme clé et le poids correspondant comme valeur.

   Syntaxe : {
                6: FreeCAD.Units.Quantity("0.222 kg/m"),
                8: FreeCAD.Units.Quantity("0.395 kg/m"),
                10: FreeCAD.Units.Quantity("0.617 kg/m"),
                12: FreeCAD.Units.Quantity("0.888 kg/m"),
                ...,
            }

-    `rebar_length_type`spécifie le type de longueur d\'armature utilisé pour les calculs de nomenclature; il peut s\'agir de \"RealLength\" ou \"LengthWithSharpEdges\".

-    `font_family`spécifie la famille de polices du texte de données.

-    `font_filename`spécifie le nom du fichier de police ou le chemin complet du fichier de police correspondant à font\_family. Ceci est nécessaire si vous travaillez en mode console pure, sans aucune interface graphique.

-    `font_size`spécifie la taille de la police du texte de données.

-    `column_width`spécifie la largeur de chaque colonne dans la table de nomenclature SVG.

-    `row_height`spécifie la hauteur de chaque ligne dans le SVG de table de nomenclature.

-    `bom_left_offset`spécifie le décalage gauche de la nomenclature SVG sur `template_file`.

-    `bom_top_offset`spécifie le décalage supérieur de la nomenclature SVG sur `template_file`.

-    `bom_min_right_offset`spécifie le décalage minimum à droite de la nomenclature SVG sur `template_file`.

-    `bom_min_bottom_offset`spécifie le décalage inférieur minimum de la nomenclature SVG sur `template_file`

-    `bom_table_SVG_max_width`spécifie la largeur maximale de la table de nomenclature en SVG.

-    `bom_table_SVG_max_height`spécifie la hauteur maximale de la table de nomenclature en SVG.

-    `template_file`spécifie le fichier modèle utilisé pour y placer la table de nomenclature générée. Il doit s\'agir d\'un fichier de modèle TechDraw valide sous la forme [here](Svg_Namespace.md).

-    `output_file`spécifie le fichier de sortie pour écrire la nomenclature SVG générée.

-    `rebar_objects`est une liste d\'objets ArchRebar et / ou rebar2 et / ou structures (pour sélectionner ArchRebar dans cette structure).

-    `reinforcement_group_by`spécifie comment les objets de renforcement doivent être groupés; il peut s\'agir de \"Mark\" ou \"Host\".

-    `return_SVG_only`spécifie si l\'objet `BOMContent` doit être créé ou non. Si `return_SVG_only` est Vrai, alors ni `BOMContent` objet n\'est créé ni SVG n\'est écrit dans `output_file`. Et il renvoie l\'élément SVG.

#### Exemple 


```python
from pathlib import Path
import FreeCAD, Draft, Arch
from ColumnReinforcement import TwoTiesSixRebars
from BillOfMaterial import BillOfMaterial_SVG


# Cela ne fonctionne pas si la structure n'est pas basée sur une face
# Structure = Arch.makeStructure(length=1000, width=400, height=400)

Rect = Draft.makeRectangle(400, 400)
Structure1 = Arch.makeStructure(Rect, height=1600)
Structure1.ViewObject.Transparency = 80
Structure2 = Arch.makeStructure(Rect, height=1600)
Structure2.ViewObject.Transparency = 80
Structure2.Placement = FreeCAD.Placement(FreeCAD.Vector(1000, 0, 0), FreeCAD.Rotation(FreeCAD.Vector(0, 0, 1), 0))
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
    structure=Structure1,
    facename="Face6",
)


# Pour barres de renfort en forme de L avec le crochet dirigé le long de l'axe des x.
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
    structure=Structure2,
    facename="Face6",
)

COLUMN_UNITS = {
    "Diameter": "mm",
    "RebarLength": "m",
    "RebarsTotalLength": "m",
}

COLUMN_HEADERS = {
    "Host": ("Member", 1),
    "Mark": ("Mark", 2),
    "RebarsCount": ("No. of Rebars", 3),
    "Diameter": ("Diameter in " + COLUMN_UNITS["Diameter"], 4),
    "RebarLength": ("Length in " + COLUMN_UNITS["RebarLength"] + "/piece", 5),
    "RebarsTotalLength": ("Total Length in " + COLUMN_UNITS["RebarsTotalLength"], 6),
}

DIA_WEIGHT_MAP = {
    6: FreeCAD.Units.Quantity("0.222 kg/m"),
    8: FreeCAD.Units.Quantity("0.395 kg/m"),
    10: FreeCAD.Units.Quantity("0.617 kg/m"),
    12: FreeCAD.Units.Quantity("0.888 kg/m"),
    14: FreeCAD.Units.Quantity("1.206 kg/m"),
    16: FreeCAD.Units.Quantity("1.578 kg/m"),
    18: FreeCAD.Units.Quantity("2.000 kg/m"),
    20: FreeCAD.Units.Quantity("2.466 kg/m"),
    22: FreeCAD.Units.Quantity("2.980 kg/m"),
    25: FreeCAD.Units.Quantity("3.854 kg/m"),
    28: FreeCAD.Units.Quantity("4.830 kg/m"),
    32: FreeCAD.Units.Quantity("6.313 kg/m"),
    36: FreeCAD.Units.Quantity("7.990 kg/m"),
    40: FreeCAD.Units.Quantity("9.864 kg/m"),
    45: FreeCAD.Units.Quantity("12.490 kg/m"),
    50: FreeCAD.Units.Quantity("15.410 kg/m"),
}

# Créer une feuille de nomenclature SVG pour toutes les armatures d'un modèle
BillOfMaterial_SVG.makeBillOfMaterialSVG(
    column_headers=COLUMN_HEADERS,
    column_units=COLUMN_UNITS,
    dia_weight_map=DIA_WEIGHT_MAP,
    rebar_length_type="RealLength",
    font_family = "DejaVu Sans",
    font_filename = "DejaVuSans.ttf",
    font_size = 3,
    column_width = 30,
    row_height = 10,
    bom_left_offset = 6,
    bom_top_offset = 40,
    bom_min_right_offset = 6,
    bom_min_bottom_offset = 6,
    bom_table_svg_max_width = 0,
    bom_table_svg_max_height = 0,
    template_file = str(Path(BillOfMaterial_SVG.__file__).parent.absolute() / "BOMTemplate.svg"),
    output_file = None,
    reinforcement_group_by = "Host",
)

# Créer une feuille de nomenclature SVG pour les barres d'armature dans Structure1
BillOfMaterial_SVG.makeBillOfMaterialSVG(
    column_headers = COLUMN_HEADERS,
    column_units = COLUMN_UNITS,
    dia_weight_map = DIA_WEIGHT_MAP,
    rebar_length_type = "LengthWithSharpEdges",
    font_family = "DejaVu Sans",
    font_filename = "DejaVuSans.ttf",
    font_size = 3,
    column_width = 30,
    row_height = 10,
    bom_left_offset = 6,
    bom_top_offset = 40,
    bom_min_right_offset = 6,
    bom_min_bottom_offset = 6,
    bom_table_svg_max_width = 0,
    bom_table_svg_max_height = 0,
    template_file = str(Path(BillOfMaterial_SVG.__file__).parent.absolute() / "BOMTemplate.svg"),
    rebar_objects=[Structure1],
    reinforcement_group_by = "Host",
)
```



---
![](images/Right_arrow.png) [documentation index](../README.md) > [External Command Reference](Category_External Command Reference.md) > [Reinforcement](Category_Reinforcement.md) > [Arch](Arch_Workbench.md) > Arch Rebar BOM/fr
