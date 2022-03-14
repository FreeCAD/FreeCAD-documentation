---
- GuiCommand:/fr
   Name:Arch Rebar BeamReinforcement
   Name/fr:Arch Rebar Poutre
   MenuLocation:Arch → Rebar tools → Beam Reinforcement<br>3D/BIM → Reinforcement → Beam Reinforcement
   Workbenches:[Arch](Arch_Workbench/fr.md), [BIM](BIM_Workbench/fr.md)
   Version:0.19
   SeeAlso:[Reinforcement](Reinforcement_Workbench.md), [Arch Armature personnalisée](Arch_Rebar/fr.md), [Arch Armature 2x6](Arch_Rebar_ColumnReinforcement_TwoTiesSixRebars/fr.md), 
---

# Arch Rebar BeamReinforcement/fr

## Description

L\'outil [Rebar Poutre](Arch_Rebar_BeamReinforcement/fr.md) permet à l\'utilisateur de créer des barres d\'armature à l\'intérieur d\'un objet poutre [Arch Structure](Arch_Structure/fr.md).

L\'outil [Rebar Poutre](Arch_Rebar_BeamReinforcement.md) est également intégré dans [atelier BIM](BIM_Workbench/fr.md).

Cette commande fait partie de l\'[atelier Reinforcement](Reinforcement_Workbench/fr.md), un [atelier externe](External_workbenches/fr.md) qui peut être installé avec le <img alt="" src=images/Std_AddonMgr.svg  style="width:24px;"> [Gestionnaire d\'Addon](Std_AddonMgr/fr.md) via le menu **Outils → Gestionnaire d'Addon → Reinforcement**.

![](images/Arch_Rebar_BeamReinforcement_example.png )



*Renforcement de poutres à l'intérieur d'une poutre [Arch Structure](Arch_Structure/fr.md)*

## Utilisation

1\. Sélectionnez la face droite d\'une poutre créée précédemment **<img src="images/_Arch_Structure.svg" width=16px> [Arch Structure](Arch_Structure/fr.md)** ayant la longueur le long de l\'axe des x. Ou sélectionnez la face avant d\'un faisceau précédemment créé **<img src="images/Arch_Structure.svg" width=16px> [Arch Structure](Arch_Structure/fr.md)** ayant la longueur le long de l\'axe des y.

2\. Ensuite, sélectionnez **<img src="images/_Arch_Rebar_ColumnReinforcement.svg" width=16px> [ Beam Reinforcement](Arch_Rebar_BeamReinforcement/fr.md)** dans les outils d\'armature.

3\. Une boîte de dialogue apparaîtra à l\'écran, comme indiqué ci-dessous.

:   <img alt="" src=images/BeamReinforcementDialog_Stirrups.png  style="width:700px;">



*Boîte de dialogue de l'outil Arch Rebar BeamReinforcement*

4\. Sélectionnez le type de ferraillage souhaité.

5\. Donnez des entrées pour les données relatives aux étriers.

6\. Cliquez sur **Next** et la boîte de dialogue sera mise à jour comme indiqué ci-dessous.

:   <img alt="" src=images/BeamReinforcementDialog_TopRebars.png  style="width:700px;">



*Boîte de dialogue pour les données Top Rebars*

7\. Définissez les données pour les barres d\'armature supérieures.


{{ColoredParagraph|#f8f9fa|

: Pour éditer la valeur Number#Diameter@Offset value, cliquez sur le bouton d'édition **Edit** en regard du label Number#Diameter@Offset. Une boîte de dialogue apparaîtra comme indiqué ci-dessous.

:<img src="images/Beam_TopReinforcement_NumberDiameterOffset.png" width=500px>

: Pour modifier la valeur du type de barre, cliquez sur le bouton d'édition **Edit** en regard de l'étiquette Type de barre. Une boîte de dialogue apparaîtra comme indiqué ci-dessous.

:<img src="images/Beam_TopReinforcement_RebarType.png" width=300px>

: Pour modifier la valeur d'orientation du crochet, cliquez sur le bouton d'édition **Edit** en regard de l'étiquette Orientation du crochet. Une boîte de dialogue apparaîtra comme indiqué ci-dessous

:<img src="images/Beam_TopReinforcement_HookOrientation.png" width=300px>

: Pour modifier la valeur de l'extension de crochet, cliquez sur le bouton d'édition **Edit** en regard de l'étiquette de l'extension de crochet. Une boîte de dialogue apparaîtra comme indiqué ci-dessous.

:<img src="images/Beam_TopReinforcement_HookExtension.png" width=300px>

: Pour modifier la valeur d’arrondi de la barre LR, cliquez sur le bouton Edition **Edit** en regard de l’étiquette Arrondi. Une boîte de dialogue apparaîtra comme indiqué ci-dessous.

:<img src="images/Beam_TopReinforcement_LRebarRounding.png" width=300px>

: Pour modifier la valeur d'espacement des calques, cliquez sur le bouton d'édition **Edit** en regard de l'étiquette Espacement des calques. Une boîte de dialogue apparaîtra comme indiqué ci-dessous.

:<img src="images/Beam_TopReinforcement_LayerSpacing.png" width=300px>
}}

8\. Cliquez sur **Next** et la boîte de dialogue sera mise à jour comme indiqué ci-dessous.

:   <img alt="" src=images/BeamReinforcementDialog_BottomRebars.png  style="width:700px;">



*Boîte de dialogue pour les données Bottom Rebars*

9\. Définissez des données pour les barres d\'armature inférieures similaires aux données des barres d\'armature supérieures.

10\. Cliquez sur **Next** et la boîte de dialogue sera mise à jour comme indiqué ci-dessous.

:   <img alt="" src=images/BeamReinforcementDialog_LeftRebars.png  style="width:700px;">



*Boîte de dialogue pour les données des barres de cisaillement à gauche*

11\. Définissez les données pour les barres d\'armature de cisaillement gauche.


{{ColoredParagraph|#f8f9fa|

: Pour éditer la valeur Number#Diameter@Offset, cliquez sur le bouton d'édition **Edit** en regard du label Number#Diameter@Offset. Une boîte de dialogue apparaîtra comme indiqué ci-dessous.

:<img src="images/Beam_ShearReinforcement_NumberDiameterOffset.png" width=500px>

: Pour modifier la valeur du type de barre, cliquez sur le bouton d'édition **Edit** en regard de l'étiquette Type de barre. Une boîte de dialogue apparaîtra comme indiqué ci-dessous.

:<img src="images/Beam_ShearReinforcement_RebarType.png" width=300px>

: Pour modifier la valeur d'orientation du crochet, cliquez sur le bouton d'édition **Edit** en regard de l'étiquette Orientation du crochet. Une boîte de dialogue apparaîtra comme indiqué ci-dessous.

:<img src="images/Beam_ShearReinforcement_HookOrientation.png" width=300px>

: Pour modifier la valeur de l'extension de crochet, cliquez sur le bouton d'édition **Edit** en regard de l'étiquette de l'extension de crochet. Une boîte de dialogue apparaîtra comme indiqué ci-dessous.

:<img src="images/Beam_ShearReinforcement_HookExtension.png" width=300px>

: Pour modifier la valeur LRebar Rounding , cliquez sur le bouton d'edition **Edit** en regard de l’étiquette Arrondi. Une boîte de dialogue apparaîtra comme indiqué ci-dessous.

:<img src="images/Beam_ShearReinforcement_LRebarRounding.png" width=300px>
}}

12\. Cliquez sur **Next** et la boîte de dialogue sera mise à jour comme indiqué ci-dessous.

:   <img alt="" src=images/BeamReinforcementDialog_RightRebars.png  style="width:700px;">



*Boîte de dialogue pour les données des barres de cisaillement à droite*

13\. Définissez des données pour les barres d'armature de cisaillement droites similaires à celles des données d'armatures de cisaillement gauche.

14\. Cliquez sur **OK** ou **Apply** pour générer un ferraillage de poutre.

15\. Cliquez sur **Cancel** pour quitter la boîte de dialogue.

## Propriétés

**Stirrups (étriers) :**

-    {{PropertyData/fr|Left Cover}}: La distance entre l\'extrémité gauche de l\'étrier et la face gauche de la structure.

-    {{PropertyData/fr|Right Cover}}: La distance entre l\'extrémité droite de l\'étrier et la face droite de la structure.

-    {{PropertyData/fr|Top Cover}}: La distance entre les étriers de la face supérieure de la structure.

-    {{PropertyData/fr|Bottom Cover}}: La distance entre les étriers de la face inférieure de la structure.

-    {{PropertyData/fr|Offset}}: La distance entre l\'étrier et la face sélectionnée/arrière de la structure.

-    {{PropertyData/fr|Diameter}}: Diamètre de l\'étrier.

-    {{PropertyData/fr|Bent Angle}}: L\'angle plié définit l\'angle aux extrémités d\'un étrier.

-    {{PropertyData/fr|Extension Factor}}: Le facteur d\'extension définit la longueur de l\'extrémité de l\'étrier, exprimée en fois le diamètre.

-    {{PropertyData/fr|Number}}: Le nombre d\'étriers.

-    {{PropertyData/fr|Spacing}}: La distance entre les axes de chaque étrier.

**Top/Bottom Reinforcement Rebars :** Barres d\'armature présentes sur la face supérieure/inférieure de la poutre

-    {{PropertyData/fr|NumberDiameterOffset}}: Un tuple de Number\#Diameter\@Offset chaîne. Chaque élément du tuple représente le ferraillage pour chaque nouveau calque.

-    {{PropertyData/fr|Rebar Type}}: Liste de tuple de type de barres d\'armature.

-    {{PropertyData/fr|Hook Orientation}}: Liste de tuple d\'orientation des crochets en forme de L.

-    {{PropertyData/fr|Hook Extension}}: Liste des tuple de longueur d\'hameçon de barres d\'armature en forme de L.

-    {{PropertyData/fr|Rounding}}: Liste des tuple d\'une valeur d\'arrondi à appliquer aux coins des barres d\'armature LShape, exprimés en diamètre.

-    {{PropertyData/fr|Layer Spacing}}: Liste des espacements entre deux couches de renforcement consécutives.

**Left/Right Reinforcement Rebars :** Barres d\'armature présentes à gauche et à droite de la poutre

-    {{PropertyData/fr|NumberDiameterOffset}}: Chaîne de Number\#Diameter\@Offset pour les barres d\'armature.

-    {{PropertyData/fr|Rebar Type}}: Liste des types de barres d\'armature.

-    {{PropertyData/fr|Hook Orientation}}: Liste d\'orientation des crochets en forme de L.

-    {{PropertyData/fr|Hook Extension}}: Liste des longueurs d\'hameçon des barres d\'armature LShape.

-    {{PropertyData/fr|Rounding}}: Liste d\'une valeur d\'arrondi à appliquer aux coins des armatures LShape, exprimée en fois le diamètre.

-    {{PropertyData/fr|Rebar Spacing}}: Espace libre entre les barres d\'armature consécutives.

## Script


**Voir aussi :**

[Arch API](Arch_API/fr.md), [Reinforcement API](Reinforcement_API/fr.md) et [FreeCAD Scripts de bases](FreeCAD_Scripting_Basics/fr.md).

L'outil BeamReinforcement peut être utilisé dans une [macros](macros/fr.md) et dans la console [Python](Python/fr.md) en utilisant la fonction suivante:

### Créer des étriers à deux pattes 


```python
RebarGroup = makeReinforcement(
    l_cover_of_stirrup,
    r_cover_of_stirrup,
    t_cover_of_stirrup,
    b_cover_of_stirrup,
    offset_of_stirrup,
    bent_angle,
    extension_factor,
    dia_of_stirrup,
    number_spacing_check,
    number_spacing_value,
    top_reinforcement_number_diameter_offset,
    top_reinforcement_rebar_type,
    top_reinforcement_layer_spacing,
    bottom_reinforcement_number_diameter_offset,
    bottom_reinforcement_rebar_type,
    bottom_reinforcement_layer_spacing,
    left_rebars_number_diameter_offset,
    left_rebars_type,
    left_rebars_spacing,
    right_rebars_number_diameter_offset,
    right_rebars_type,
    right_rebars_spacing,
    top_reinforcement_l_rebar_rounding=2,
    top_reinforcement_hook_extension=40,
    top_reinforcement_hook_orientation="Front Inside",
    bottom_reinforcement_l_rebar_rounding=2,
    bottom_reinforcement_hook_extension=40,
    bottom_reinforcement_hook_orientation="Front Inside",
    left_l_rebar_rounding=2,
    left_rebars_hook_extension=40,
    left_rebars_hook_orientation="Front Inside",
    right_l_rebar_rounding=2,
    right_rebars_hook_extension=40,
    right_rebars_hook_orientation="Front Inside",
    structure=None,
    facename=None,
)

```

-   Crée un objet `RebarGroup` à partir de la `structure` donnée, qui est une [Structure Arch](Arch_Structure/fr.md), et de `facename` qui est une face de cet objet structure.
    -   Si ni `structure` ni `facename` n\'est donné, ce sera la face selectionné par l\'utilisateur qui sera prise.

-    `l_cover_of_stirrup`, `r_cover_of_stirrup`, `t_cover_of_stirrup`, `b_cover_of_stirrup` et `offset_of_stirrup` sont des distances internes décalées pour le motif aux faces de la structure. Ce sont respectivement les décalages gauche, droit, haut, bas et avant/arrière.

-    `bent_angle`définit l\'angle de la pointe de la boucle de renforcement de l\'étrier.

-    `extension_factor`définit la longueur de la pointe de la boucle de renforcement de l\'étrier, exprimée en multiple du diamètre.

-    `dia_of_stirrup`est le diamètre de l\'étrier.

-    `number_spacing_check`mis à `True`, il créera autant d\'étriers que donné par `number_spacing_value`. Mis à `False`, il créera un étrier séparé par la valeur numérique de `number_spacing_value`.

-    `number_spacing_spue`spécifie le nombre d\'étriers ou la valeur de la séparation qui les sépare, en fonction de `number_spacing_check`.

-    `top_reinforcement_number_diameter_offset`et `bottom_reinforcement_number_diameter_offset` sont un tuple de la chaîne number\_diameter\_offset. Chaque élément du tuple représente le ferraillage pour chaque nouvel ensemble.

   Syntaxe : (
               "number1#diameter1@offset1+number2#diameter2@offset2+...",
               "number3#diameter3@offset3+number4#diameter4@offset4+...",
               ...,
           )

-    `top_reinforcement_rebar_type`et `bottom_reinforcement_rebar_type` spécifient le type de barres d\'armature supérieure/inférieure.

   Valeurs possibles :
   1. 'StraightRebar' ou 'LShapeRebar'
', ...) et le nombre d'éléments du tuple doivent être égaux au nombre d'ensembles d'armatures.
   3. [
', ...),
', ...),
          ...
      ]
      chaque élément de la liste est un tuple, qui spécifie le type d'armature de chaque couche de ferraillage. Chaque élément du tuple représente rabar_type pour chaque ensemble de barres d’armature.
   4. [
,
', ...),
          ...
      ]

-    `top_reinforcement_layer_spacing`et `bottom_reinforcement_layer_spacing` sont l\'espacement entre deux ensembles de ferraillage consécutifs.

   Valeurs possibles :

, ...) et le nombre d'éléments du tuple doit être égal à un de moins que le nombre d'ensembles.

-    `left_rebars_number_diameter_offset`et `right_rebars_number_diameter_offset` sont une chaîne de number\_diameter\_offset.

   Syntaxe : "number1#diameter1@offset1+number2#diameter2@offset2+..."

-    `left_rebars_type`et `right_rebars_type` spécifient le type de barres d\'armature gauche/droite.

   Valeurs possibles :
   1. 'StraightRebar' ou 'LShapeRebar'
', ...) et chaque élément du tuple représente rabar_type pour chaque ensemble de barres d’armature.

-    `left_rebars_spacing`et `right_rebars_spacing` est un espacement clair entre les barres d\'armature consécutives.

-    `top_reinforcement_l_rebar_rounding`et `bottom_reinforcement_l_rebar_rounding` sont les paramètres qui déterminent le rayon de courbure des barres d\'armature haut/bas en forme de l, exprimé en multiple du diamètre. La syntaxe possible est semblable à celle décrite ci-dessus pour `top_reinforcement_rebar_type` / `bottom_reinforcement_rebar_type`.

-    `top_reinforcement_hook_extension`et `bottom_reinforcement_hook_extension` sont la longueur du crochet des barres d\'armature LShaped. La syntaxe possible est semblable à celle décrite ci-dessus pour `top_reinforcement_rebar_type` / `bottom_reinforcement_rebar_type`.

-    `top_reinforcement_hook_orientation`et `bottom_reinforcement_hook_orientation` spécifient l\'orientation du crochet LShaped. Elle peut prendre pour valeur `"Front Inside"`, `"Front Outside"`, `"Rear Inside"` ou `"Rear Outside"`. La syntaxe possible est semblable à celle décrite ci-dessus pour `top_reinforcement_rebar_type` / `bottom_reinforcement_rebar_type`.

-    `left_l_rebar_rounding`et `right_l_rebar_rounding` sont les paramètres qui déterminent le rayon de courbure des barres d\'armature gauche/droite en forme de LS, exprimé en multiple du diamètre. La syntaxe possible est semblable à celle décrite ci-dessus pour `left_rebars_type` / `right_rebars_type`.

-    `left_rebars_hook_extension`et `right_rebars_hook_extension` sont les longueurs du crochet des armatures LShaped. La syntaxe possible est semblable à celle décrite ci-dessus pour `left_rebars_type` / `right_rebars_type`.

-    `left_rebars_hook_orientation`et `right_rebars_hook_orientation` spécifient l\'orientation du crochet LShaped. Elle peut prendre pour valeur `"Front Inside"`, `"Front Outside"`, `"Rear Inside"` ou `"Rear Outside"`. La syntaxe possible est similaire à celle décrite ci-dessus pour `left_rebars_type` / `right_rebars_type`.

#### Exemple


```python
import FreeCAD, Arch
from BeamReinforcement import TwoLeggedBeam

Structure = Arch.makeStructure(length=3000.0,width=200.0,height=400.0)
Structure.ViewObject.Transparency = 80
FreeCAD.ActiveDocument.recompute()

RebarGroup = TwoLeggedBeam.makeReinforcement(
    l_cover_of_stirrup=20,
    r_cover_of_stirrup=20,
    t_cover_of_stirrup=20,
    b_cover_of_stirrup=20,
    offset_of_stirrup=100,
    bent_angle=135,
    extension_factor=4,
    dia_of_stirrup=8,
    number_spacing_check=False,
    number_spacing_value=200,
    top_reinforcement_number_diameter_offset=("1#20@-60+2#16@-60+1#20@-60", "3#16@-100"),
    top_reinforcement_rebar_type="LShapeRebar",
    top_reinforcement_layer_spacing=30,
    bottom_reinforcement_number_diameter_offset=("1#20@-60+2#16@-60+1#20@-60", "3#16@-100"),
    bottom_reinforcement_rebar_type="LShapeRebar",
    bottom_reinforcement_layer_spacing=30,
    left_rebars_number_diameter_offset="1#16@-100+1#16@-100+1#16@-100",
    left_rebars_type="LShapeRebar",
    left_rebars_spacing=30,
    right_rebars_number_diameter_offset="1#16@-100+1#16@-100+1#16@-100",
    right_rebars_type="LShapeRebar",
    right_rebars_spacing=30,
    top_reinforcement_l_rebar_rounding=2,
    top_reinforcement_hook_extension=100,
    top_reinforcement_hook_orientation="Rear Outside",
    bottom_reinforcement_l_rebar_rounding=2,
    bottom_reinforcement_hook_extension=100,
    bottom_reinforcement_hook_orientation="Rear Outside",
    left_l_rebar_rounding=2,
    left_rebars_hook_extension=80,
    left_rebars_hook_orientation=("Rear Inside", "Front Inside", "Rear Inside"),
    right_l_rebar_rounding=2,
    right_rebars_hook_extension=80,
    right_rebars_hook_orientation=("Front Inside", "Rear Inside", "Front Inside"),
    structure=Structure,
    facename="Face6",
)
```



---
![](images/Right_arrow.png) [documentation index](../README.md) > [Reinforcement](Category_Reinforcement.md) > [Arch](Arch_Workbench.md) > Arch Rebar BeamReinforcement/fr
