---
- GuiCommand:/fr
   Name:SheetMetal AddWall
   Name/fr:SheetMetal Tôle pliée
   MenuLocation:SheetMetal → Make Wall
   Workbenches:[SheetMetal](SheetMetal_Workbench/fr.md)
   Shortcut:**W**
---

# SheetMetal AddWall/fr

## Description

La commande <img alt="" src=images/SheetMetal_Bend.svg  style="width:24px;"> **SheetMetal AddWall** crée un pli sur le bord sélectionné.

<img alt="" src=images/PostBend.png  style="width:320px;">

## Utilisation


<div class="mw-translate-fuzzy">

Pour ajouter un pli:

1.  Basculez vers l\'<img alt="" src=images/Sheetmetal_workbench_icon.svg  style="width:22px;"> [atelier SheetMetal](SheetMetal_Workbench/fr.md).
2.  Commencez avec une plaque de base ou une feuille, sélectionnez un ou plusieurs bords pour recevoir un pli.
3.  Cliquez sur l\'outil <img alt="" src=images/SheetMetal_Bend.svg  style="width:24px;"> **Bend** pour ajouter un pli.


</div>


**Remarque**

: Pour créer une plaque de base, utilisez un contour 2D fermé - de préférence une <img alt="" src=images/Sketcher_NewSketch.svg  style="width:24px;">. [Esquisse](Sketcher_NewSketch/fr.md) - avec le <img alt="" src=images/SheetMetal_AddBase.svg  style="width:24px;"> [Tôle de base](SheetMetal_AddBase/fr.md).
Au lieu de cela, vous pouvez également générer une plaque de base avec l\'une des méthodes suivantes :

:\* Method 1: <img alt="" src=images/Part_Box.svg  style="width:24px;"> [Part Cube](Part_Box/fr.md)

:\* Method 2: un solide extrudé fait avec <img alt="" src=images/Part_Extrude.svg  style="width:24px;"> [Part Extrusion](Part_Extrude/fr.md) à partir d\'un :

::\* <img alt="" src=images/Draft_Rectangle.svg  style="width:24px;"> [Draft Rectangle](Draft_Rectangle/fr.md) ou un

::\* <img alt="" src=images/Draft_Wire.svg  style="width:24px;"> [Draft Polyligne](Draft_Wire/fr.md) ou une

::\* <img alt="" src=images/Sketcher_NewSketch.svg  style="width:24px;"> [Sketcher Nouvelle esquisse](Sketcher_NewSketch/fr.md)

::\* Utilisez <img alt="" src=images/Part_Thickness.svg  style="width:24px;"> [Part Évidement](Part_Thickness/fr.md) pour créer une coque (**Typiquement avec la valeur d'épaisseur de la tôle.**)

:\* Method 3: <img alt="" src=images/PartDesign_Body.svg  style="width:24px;"> [PartDesign Corps](PartDesign_Body/fr.md) contenant soit un

::\* <img alt="" src=images/PartDesign_AdditiveBox.svg  style="width:24px;"> [PartDesign Cube additif](PartDesign_AdditiveBox.md) ou une

::\* <img alt="" src=images/PartDesign_Pad.svg  style="width:24px;"> [PartDesign Protrusion](PartDesign_Pad/fr.md) fabriquée à partir d\'une <img alt="" src=images/Sketcher_NewSketch.svg  style="width:24px;"> [Sketch Nouvelle esquisse](Sketcher_NewSketch/fr.md).

::\* Utilisez <img alt="" src=images/PartDesign_Thickness.svg  style="width:24px;"> [PartDesign Epaisseur](PartDesign_Thickness/fr.md) pour créer une coque (**Typiquement avec la valeur d'épaisseur de la tôle.**)

:   

    :   Si vous commencez avec un <img alt="" src=images/PartDesign_Body.svg  style="width:24px;"> PartDesign Corps, vous pouvez mélanger des fonctions de tôlerie avec des fonctions PartDesign telles que <img alt="" src=images/PartDesign_Pocket.svg  style="width:24px;"> [PartDesign Cavité](PartDesign_Pocket/fr.md) ou <img alt="" src=images/PartDesign_Hole.svg  style="width:24px;"> [PartDesign Perçages](PartDesign_Hole/fr.md).

## Propriétés

See also: [Property editor](Property_editor.md).

A SheetMetal Bend object is derived from a [Part Feature](Part_Feature.md) object and inherits all its properties. It also has the following additional properties and its label has a default value:

### Données


{{Properties_Title|Base}}


<div class="mw-translate-fuzzy">

-    {{PropertyData/fr|Label}}: Nom donné par l\'utilisateur à l\'objet dans la [vue en arborescence](tree_view/fr.md).


</div>


{{Properties_Title|Parameters}}


<div class="mw-translate-fuzzy">

-    {{PropertyData/fr|angle}}: angle de pliage.

-    {{PropertyData/fr|extend1}}: prolonge le mur sur le côté gauche.

-    {{PropertyData/fr|extend2}}: prolonge le mur sur le côté droit.

-    {{PropertyData/fr|gap1}}: espace depuis le côté gauche.

-    {{PropertyData/fr|gap2}}: espace depuis le côté droit.

-    {{PropertyData/fr|invert}}: inverse la direction du pli.

-    {{PropertyData/fr|length}}: longueur du mur.

-    {{PropertyData/fr|mitreangle1}}: angle d\'onglet de pliage sur le côté gauche.

-    {{PropertyData/fr|mitreangle2}}: angle d\'onglet de pliage sur le côté droit.

-    {{PropertyData/fr|radius}}: rayon de courbure.

-    {{PropertyData/fr|relief Type}}: rectangle ou Rond. Activé uniquement lorsqu\'une valeur d\'espacement est définie.

-    {{PropertyData/fr|reliefd}}: profondeur du relief. Activé uniquement lorsqu\'une valeur d\'écart est définie.

-    {{PropertyData/fr|reliefw}}: largeur du relief. Activé uniquement lorsqu\'une valeur d\'espacement est définie.

-    {{PropertyData/fr|kfactor}}: facteur K (également appelé facteur neutre) pour le pli. Utilisé pour calculer la tolérance de pliage lors du dépliage.

-    {{PropertyData/fr|unfold}}: False (par défaut) ou True. Si c\'est vrai, déplie le pli.


</div>


{{Properties_Title|Parameters Ex}}

-    **Auto Miter|Bool**: \"Enable Auto Miter\". Default: `True`.

-    **extend1|Distance**: \"Extend from Left Side\". Default: {{value|0,00 mm}}.

-    **extend2|Distance**: \"Extend from Right Side\". Default: {{value|0,00 mm}}.

-    **kfactor|FloatConstraint**: \"Location of Neutral Line. Caution: Using ANSI standards, not DIN.\".  Default: {{value|0,50}}. K factor (also known as neutral factor) for the bend. Used to calculate bend allowance when unfolding.

-    **max Extend Dist|Length**: \"Auto Miter maximum Extend Distance\". Default: {{value|5,00 mm}}.

-    **min Gap|Length**: \"Auto Miter Minimum Gap\". Default: {{value|5,00 mm}}.

-    **miterangle1|Angle**: \"Bend Miter Angle from Left Side\". Default angle: {{value|0,00°}}.

-    **miterangle2|Angle**: \"Bend Miter Angle from Right Side\". Default angle: {{value|0,00°}}.

-    **offset|Distance**: \"Offset Bend\". Default: {{value|0,00 mm}}.

-    **unfold|Bool**: \"Shows Unfold View of Current Bend\". Default:  `True` unfolds the bend.


{{Properties_Title|Parameters Ex2}}

-    **Sketch|Link**: \"Sketch Object\".

-    **sketchflip|Bool**: \"Flip Sketch Direction\". Default: `False`.

-    **sketchinvert|Bool**: \"Invert Sketch Start\". Default: `False`.


{{Properties_Title|Parameters Ex3}}

-    **Length List|FloatList**: \"Length of Wall List\". Default: {{value|[10,00]}}.

-    **bend AList|FloatList**: \"Bend Angle List\". Default: {{value|[90,00]}}.


{{Properties_Title|Parameters Relief}}

-    **Relief Factor|Float**: \"Relief Factor\". Default: {{value|0,70}}.

-    **Use Relief Factor|Bool**: \"Use Relief Factor\". Default: `False`.

-    **min Relief Gap|Length**: \"Minimum Gap to Relief Cut\". Default: {{value|1,00 mm}}.

-    **relief Type|Enumeration**: \"Relief Type\". {{value|Rectangle}} (default), {{value|Round}}. Enabled only when a gap value is set.

-    **reliefd|Length**: \"Relief Depth\". Default: {{value|1,00 mm}}. Enabled only when a gap value is set.

-    **reliefw|Length**: \"Relief Width\". Default: {{value|0,80 mm}}. Enabled only when a gap value is set.

## Exemple

<img alt="" src=images/SheetMetal_AddWall-01.png  style="width:300px;">


<div class="mw-translate-fuzzy">

<img alt="" src=images/SheetMetal_AddWall-01.png  style="width:300px;"> 
*Un plateau tout simple*


</div>


<div class="mw-translate-fuzzy">


<div class="mw-collapsible mw-collapsed">


<div class="mw-collapsible-content">

### Préparation


</div>

Ce plateau est constitué d\'une ébauche rectangulaire à laquelle on a ajouté des parois sur les bords de son contour. Il faut donc préparer à l\'avance un croquis de contour pour l\'ébauche.

<img alt="" src=images/SheetMetal_AddWall-02.png  style="width:200px;">


<div class="mw-translate-fuzzy">

<img alt="" src=images/SheetMetal_AddWall-02.png  style="width:200px;"> 
*Un simple contour rectangulaire*


</div>

### Processus de travail 


<div class="mw-translate-fuzzy">

1.  1.  Créer une ébauche
    2.  Sélectionnez l\'esquisse de contour  <img alt="" src=images/SheetMetal_AddWall-03.png  style="width:240px;">
    3.  Appuyez sur le bouton  <img alt="" src=images/SheetMetal_AddWall-04.png  style="width:240px;">  (L\'ébauche est générée dans la direction z  .

2.  Ajouter des murs aux bords du contour
    1.  Sélectionnez les **bords du contour** du blanc  <img alt="" src=images/SheetMetal_AddWall-05.png  style="width:240px;">.
    2.  Appuyez sur le bouton  <img alt="" src=images/SheetMetal_AddWall-06.png  style="width:240px;">
    3.  Si le pli est à 90° vers le bas, mettez la valeur de la propriété **invert** à true pour inverser le sens (et **length** à une valeur plus faible pour les petits murs)  <img alt="" src=images/SheetMetal_AddWall-01.png  style="width:240px;">.  

3.  Ajouter d\'autres parois
    1.  Sélectionnez les **bords extérieurs supérieurs** du plateau  <img alt="" src=images/SheetMetal_AddWall-08.png  style="width:240px;">.
    2.  Appuyez sur le bouton  <img alt="" src=images/SheetMetal_AddWall-09.png  style="width:240px;"> 
    3.  Les parois sont un peu trop longuess (mais joliment taillées) et il faut donc mettre la propriété **longueur** à une valeur inférieure  <img alt="" src=images/SheetMetal_AddWall-10.png  style="width:240px;">.
    4.  Si vous aimez que les plis se mettent vers l\'extérieur mettez la valeur **invert** à true  <img alt="" src=images/SheetMetal_AddWall-11.png  style="width:240px;">.


</div>

C\'est fait!


</div>


</div>




[Category:SheetMetal](Category:SheetMetal.md) [Category:Addons](Category:Addons.md) [Category:External Command Reference](Category:External_Command_Reference.md)

---
[documentation index](../README.md) > [SheetMetal](Category:SheetMetal.md) > SheetMetal AddWall/fr
