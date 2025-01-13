---
 GuiCommand:
   Name: SheetMetal AddWall
   Name/fr: SheetMetal Rebord
   MenuLocation: SheetMetal , Créer un rebord
   Workbenches: SheetMetal_Workbench/fr
   Shortcut: **W**
---

# SheetMetal AddWall/fr

## Description

La commande <img alt="" src=images/SheetMetal_AddWall.svg  style="width:24px;"> **SheetMetal Rebord** crée des rebords sur les bords sélectionnés d\'une plaque de base. En modifiant la propriété **angle** d\'un rebord, on peut le transformer en bord rabattu.

Un **bord** est constitué d\'un coude cylindrique à 90° et d\'une bande plane (paroi).

<img alt="" src=images/SheetMetal_AddWall-12.png  style="width:200px;"> <img alt="" src=images/Button_right.svg  style="width:16px;"> <img alt="" src=images/SheetMetal_AddWall-13.png  style="width:200px;"> 
*Deux bords sélectionnés → deux bords*

La réinitialisation de la propriété **angle** à environ 180° dans une deuxième étape créera un **bord rabattu** à la place.

<img alt="" src=images/SheetMetal_AddWall-14.png  style="width:200px;"> <img alt="" src=images/Button_right.svg  style="width:16px;"> <img alt="" src=images/SheetMetal_AddWall-15.png  style="width:200px;"> 
*Deux bords sélectionnés → deux bords rabattus*



## Utilisation

1.  Sélectionnez un ou plusieurs bords d\'une tôle de base.
2.  Il y a plusieurs façons de lancer la commande :
    -   Pressez le bouton **<img src="images/SheetMetal_AddWall.svg" width=16px> [Créer un rebord](SheetMetal_AddWall/fr.md)**.
    -   Sélectionnez l\'option **SheetMetal → <img src="images/SheetMetal_AddWall.svg" width=16px> Créer un rebord** du menu.
    -   Cliquez avec le bouton droit de la souris dans la [vue en arborescence](Tree_view/fr.md) ou la [vue 3D](3D_view/fr.md) et sélectionnez l\'option **SheetMetal → <img src="images/SheetMetal_AddWall.svg" width=16px> Créer un rebord** dans le menu contextuel.
    -   Utilisez le raccourci clavier : **W**.
3.  Le [panneau des tâches](Task_panel/fr.md) *Paramètres du rebord* s\'ouvre (introduit dans la version 0.5.00).
4.  Vous pouvez appuyer sur le bouton **Sélectionner** pour ajouter d\'autres bords.
    -   Appuyez sur le bouton **Aperçu** pour terminer la sélection et afficher les modifications.
5.  Vous pouvez ajuster les paramètres dans le panneau des tâches.
6.  Appuyez sur le bouton **OK** pour terminer la commande et fermer le panneau des tâches.
7.  Un objet **Bend** sera créé, composé d\'une nouvelle bride à chaque bord sélectionné.
8.  Ajustez les paramètres dans l\'[éditeur de propriétés](Property_editor/fr.md).



## Remarques

Pour créer une plaque de base, utilisez un contour 2D fermé, de préférence une <img alt="" src=images/Sketcher_NewSketch.svg  style="width:24px;"> [Esquisse](Sketcher_NewSketch/fr.md) avec la commande <img alt="" src=images/SheetMetal_AddBase.svg  style="width:24px;"> [Créer une paroi de base ](SheetMetal_AddBase/fr.md).

Il est également possible de créer une plaque de base (vierge) à l\'aide des commandes de l\'<img alt="" src=images/Workbench_Part.svg  style="width:16px;"> [atelier Part](Part_Workbench/fr.md) ou de l\'<img alt="" src=images/Workbench_PartDesign.svg  style="width:16px;"> [atelier PartDesign](PartDesign_Workbench/fr.md).

Pour créer une ébauche avec l\'[atelier Part](Part_Workbench/fr.md) : :

1.  Créez un solide en utilisant soit :
    -   <img alt="" src=images/Part_Box.svg  style="width:16px;"> [Part Cube](Part_Box/fr.md).
    -   <img alt="" src=images/Part_Extrude.svg  style="width:16px;"> [Part Extrusion](Part_Extrude/fr.md) de :
        -   Un <img alt="" src=images/Draft_Rectangle.svg  style="width:16px;"> [Draft Rectangle](Draft_Rectangle/fr.md).
        -   Une <img alt="" src=images/Draft_Wire.svg  style="width:16px;"> [Draft Polyligne](Draft_Wire/fr.md).
        -   Une <img alt="" src=images/Sketcher_NewSketch.svg  style="width:16px;"> [Esquisse](Sketcher_NewSketch/fr.md).
2.  Assurez-vous que l\'une des dimensions de la boîte ou la distance d\'extrusion est égale à l\'épaisseur de la tôle.

Pour créer une ébauche avec l\'[atelier PartDesign](PartDesign_Workbench/fr.md) :

1.  Créez un solide en utilisant soit :
    -   Un <img alt="" src=images/PartDesign_AdditiveBox.svg  style="width:16px;"> [Cube additif](PartDesign_AdditiveBox/fr.md).
    -   Une <img alt="" src=images/PartDesign_Pad.svg  style="width:16px;"> [PartDesign Protrusion](PartDesign_Pad/fr.md) d\'une <img alt="" src=images/Sketcher_NewSketch.svg  style="width:16px;"> [Esquisse](Sketcher_NewSketch/fr.md).
2.  Assurez-vous que l\'une des dimensions de la boîte ou la propriété **Length** du bloc est égale à l\'épaisseur de la tôle.

Si vous commencez avec un <img alt="" src=images/PartDesign_Body.svg  style="width:16px;"> [PartDesign Corps](PartDesign_Body/fr.md), vous pouvez mélanger des caractéristiques de SheetMetal avec des caractéristiques PartDesign telles que <img alt="" src=images/PartDesign_Pocket.svg  style="width:16px;"> [PartDesign Cavité](PartDesign_Pocket/fr.md) ou <img alt="" src=images/PartDesign_Hole.svg  style="width:16px;"> [PartDesign Perçage](PartDesign_Hole/fr.md).



## Propriétés

Voir aussi : [Éditeur de propriétés](Property_editor/fr.md)

Un objet SheetMetal Bend est dérivé d\'un objet [Part Feature](Part_Feature/fr.md) ou, s\'il se trouve à l\'intérieur d\'un [PartDesign Corps](PartDesign_Body/fr.md), à partir d\'un objet [PartDesign Feature](PartDesign_Feature/fr.md), dont il hérite de toutes les propriétés. Il possède également les propriétés supplémentaires suivantes :



### Données


{{Properties_Title|Parameters}}

-    **Bend Type|Enumeration**: type de pliage. {{value|Matériau à l'extérieur}} (par défaut), {{value|Matériau à l'intérieur}}, {{value|Épaisseur à l'extérieur}}, {{value|Décalage}}.

-    **Length Spec|Enumeration**: type de spécification de longueur. {{value|Droite}} (par défaut), {{value|Bord extérieur}}, {{value|Bord intérieur}}, {{value|Tangentiel}}. {{Version/fr|0.21}}

-    **angle|Angle**: angle de pliage. Angle par défaut : {{value|90,00°}}.

-    **base Object|LinkSub**: objet de base. Lien vers la face planaire devant recevoir une courbure.

-    **extend1|Distance**: extension du côté gauche. Valeur par défaut : {{value|0,00 mm}}.

-    **extend2|Distance**: extension du côté droit. Valeur par défaut : {{value|0,00 mm}}.

-    **gap1|Distance**: écart par rapport au côté gauche. Valeur par défaut : {{value|0,00 mm}}.

-    **gap2|Distance**: écart depuis le côté droit. Valeur par défaut : {{value|0,00 mm}}.

-    **invert|Bool**: inverser la direction du pliage. Valeur par défaut : `False`.

-    **length|Length**: longueur de la paroi. Valeur par défaut : {{value|10,00 mm}}.

-    **radius|Length**: rayon de courbure. Valeur par défaut : {{value|1,00 mm}}.

-    **radius|Length**: rayon de courbure. La valeur par défaut dépend de la propriété du rayon de l\'élément parent :

    -   Cette propriété n\'existe pas : cette propriété est définie sur {{value|1,00 mm}}.
    -   Cette propriété contient une valeur numérique : une expression liant cette propriété est insérée dans cette propriété.
    -   Cette propriété contient une expression : l\'expression est copiée dans cette propriété.


{{Properties_Title|Parameters Ex}}

-    **Auto Miter|Bool**: activer l\'onglet automatique. Valeur par défaut : `True`.

-    **kfactor|FloatConstraint**: emplacement de la ligne neutre. Attention : utilise les normes ANSI et non DIN.Par défaut : {{value|0,50}}. Facteur K (également connu sous le nom de facteur neutre) pour le pli. Utilisé pour calculer la marge de pliage lors du dépliage.

-    **max Extend Dist|Length**: distance maximale d\'extension de l\'onglet automatique. Valeur par défaut : {{value|5,00 mm}}.

-    **min Gap|Length**: espace minimum de l\'onglet automatique. Valeur par défaut : {{value|0,20 mm}}.

-    **min Relief Gap|Length**: espace minimum pour la contre-dépouille. Valeur par défaut : {{value|1,00 mm}}.

-    **offset|Distance**: décaler le pli. Valeur par défaut : {{value|0,00 mm}}.

-    **unfold|Bool**: montrer la vue dépliée du pliage en cours. Valeur par défaut : `False`, `True` déplie le pli.


{{Properties_Title|Parameters Ex2}}

-    **Sketch|Link**: objet de l\'esquisse.

-    **sketchflip|Bool**: retourner la direction de l\'esquisse. Valeur par défaut : `False`.

-    **sketchinvert|Bool**: inverser le début de l\'esquisse. Valeur par défaut : `False`.


{{Properties_Title|Parameters Ex3}}

-    **Length List|FloatList**: longueur de la liste des parois. Valeur par défaut : {{value|[10.00]}}.

-    **bend AList|FloatList**: liste des angles de pliage. Valeur par défaut : {{value|[90.00]}}.


{{Properties_Title|Parameters Miterangle}}

-    **miterangle1|Angle**: angle de l\'onglet de pliage depuis le côté gauche. Angle par défaut : {{value|0,00°}}.

-    **miterangle2|Angle**: angle de l\'onglet de pliage depuis le côté droit. Angle par défaut : {{value|0,00°}}.


{{Properties_Title|Parameters Perforation}}

-    **Nonperforation Max Length|Length**: longueur maximale de la non-perforation. Valeur par défaut : {{value|5 mm}}.

-    **Perforate|Bool**: activer la perforation. Valeur par défaut : `False`.

-    **Perforation Angle|Angle**: angle de la perforation. Valeur par défaut : {{value|0 °}}.

-    **Perforation initial Length|Length**: longueur initiale de la perforation. Par défaut : {{value|5 mm}}.

-    **Perforation Max Length|Length**: longueur maximale de la perforation. Par défaut : {{value|5 mm}}.


{{Properties_Title|Parameters Relief}}

-    **Relief Factor|Float**: facteur de contre-dépouille. Valeur par défaut : {{value|0,70}}.

-    **Use Relief Factor|Bool**: utiliser le facteur de contre-dépouille. Valeur par défaut : `False`.

-    **relief Type|Enumeration**: type de contre-dépouille. {{value|Rectangle}}. (par défaut), {{value|Round}}. Activé uniquement lorsqu\'une valeur d\'écart est définie.

-    **reliefd|Length**: profondeur de la contre-dépouille. Valeur par défaut : {{value|1,00 mm}}. Activé uniquement lorsqu\'une valeur d\'espace est définie.

-    **reliefw|Length**: largeur de la contre-dépouille. Valeur par défaut : {{value|0,80 mm}}. Activé uniquement lorsqu\'une valeur d\'espace est définie.



## Exemple

<img alt="" src=images/SheetMetal_AddWall-01.png  style="width:300px;"> 
*Un plateau tout simple*


<div class="mw-collapsible mw-collapsed">


<div class="mw-collapsible-content">



### Préparation

Ce plateau est constitué d\'une ébauche rectangulaire à laquelle on a ajouté des parois sur les bords de son contour. Il faut donc préparer à l\'avance un croquis de contour pour l\'ébauche.

<img alt="" src=images/SheetMetal_AddWall-02.png  style="width:200px;"> 
*Un simple contour rectangulaire*



### Déroulement des tâches 

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
    3.  Les parois sont un peu trop longues et il faut donc mettre la propriété **longueur** à une valeur inférieure  <img alt="" src=images/SheetMetal_AddWall-10.png  style="width:240px;">.
    4.  Si vous aimez que les plis se mettent vers l\'extérieur mettez la valeur **invert** à true  <img alt="" src=images/SheetMetal_AddWall-11.png  style="width:240px;">.

C\'est fait!


</div>


</div>



---
⏵ [documentation index](../README.md) > [SheetMetal](Category_SheetMetal.md) > [Addons](Category_Addons.md) > [External Command Reference](Category_External Command Reference.md) > SheetMetal AddWall/fr
