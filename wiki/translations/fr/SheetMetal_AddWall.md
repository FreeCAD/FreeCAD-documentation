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

Pour ajouter un pli:

1.  Basculez vers l\'<img alt="" src=images/Sheetmetal_workbench_icon.svg  style="width:22px;"> [atelier SheetMetal](SheetMetal_Workbench/fr.md).
2.  Commencez avec une plaque de base ou une feuille, sélectionnez un ou plusieurs bords pour recevoir un pli.
3.  Cliquez sur l\'outil <img alt="" src=images/SheetMetal_AddWall.svg  style="width:24px;"> [Make Wall](SheetMetal_AddWall/fr.md) pour ajouter un pli.


**Remarque**

: Pour créer une plaque de base, utilisez un contour 2D fermé - de préférence une <img alt="" src=images/Sketcher_NewSketch.svg  style="width:24px;">. _.
Au lieu de cela, vous pouvez également générer une plaque de base avec l\'une des méthodes suivantes :

:\* Method 1: <img alt="" src=images/Part_Box.svg  style="width:24px;"> [Part Cube](Part_Box/fr.md)

:\* Method 2: un solide extrudé fait avec <img alt="" src=images/Part_Extrude.svg  style="width:24px;"> [Part Extrusion](Part_Extrude/fr.md) à partir d\'un :

::\* <img alt="" src=images/Draft_Rectangle.svg  style="width:24px;"> [Draft Rectangle](Draft_Rectangle/fr.md) ou un

::\* <img alt="" src=images/Draft_Wire.svg  style="width:24px;"> [Draft Polyligne](Draft_Wire/fr.md) ou une

::\* <img alt="" src=images/Sketcher_NewSketch.svg  style="width:24px;"> [Sketcher Nouvelle esquisse](Sketcher_NewSketch/fr.md)

::\* Utilisez <img alt="" src=images/Part_Thickness.svg  style="width:24px;"> [Part Évidement](Part_Thickness/fr.md) pour créer une coque (**Typiquement avec la valeur d'épaisseur de la tôle.**)

:\* Method 3: <img alt="" src=images/PartDesign_Body.svg  style="width:24px;"> [PartDesign Corps](PartDesign_Body/fr.md) contenant soit un

::\* <img alt="" src=images/PartDesign_AdditiveBox.svg  style="width:24px;"> [PartDesign Cube additif](PartDesign_AdditiveBox.md) ou une

::\* <img alt="" src=images/PartDesign_Pad.svg  style="width:24px;"> _.

::\* Utilisez <img alt="" src=images/PartDesign_Thickness.svg  style="width:24px;"> [PartDesign Epaisseur](PartDesign_Thickness/fr.md) pour créer une coque (**Typiquement avec la valeur d'épaisseur de la tôle.**)

:   

    :   Si vous commencez avec un <img alt="" src=images/PartDesign_Body.svg  style="width:24px;"> PartDesign Corps, vous pouvez mélanger des fonctions de tôlerie avec des fonctions PartDesign telles que <img alt="" src=images/PartDesign_Pocket.svg  style="width:24px;"> _.

## Propriétés

Voir aussi : [Éditeur de propriétés](Property_editor/fr.md)

Un objet SheetMetal Bend est dérivé d\'un objet [Part Feature](Part_Feature/fr.md) et hérite de toutes ses propriétés. Il possède également les propriétés supplémentaires suivantes :

### Données


{{Properties_Title|Base}}

-    {{PropertyData/fr|Label|String}}: Valeur par défaut : Le nom modifiable par l\'utilisateur de cet objet, il peut être toute chaîne UTF8 arbitraire.

-    {{PropertyData/fr|Base Feature|Link|hidden}}: Fonctionnalité de base. Lien vers la caractéristique parent.

-    {{PropertyData/fr|_Body|LinkHidden|hidden}}: Lien caché vers le corps du parent.


{{Properties_Title|Parameters}}

-    {{PropertyData/fr|Bend Type|Enumeration}}: \"Type de pliage\". {{value|Material Outside}}, {{value|Material Inside}}, {{value|Thickness Outside}}. (par défaut), {{value|Material Inside}}, {{value|Thickness Outside}}, {{value|Offset}}.

-    {{PropertyData/fr|angle|Angle}}: \"Angle de pliage\". Angle par défaut : {{value|90,00°}}.

-    {{PropertyData/fr|base Object|LinkSub}}: \"Objet de base\". Lien vers la face planaire devant recevoir une courbure.

-    {{PropertyData/fr|gap1|Distance}}: \"Ecart par rapport au côté gauche\". Valeur par défaut : {{value|0,00 mm}}.

-    {{PropertyData/fr|gap2|Distance}}: \"Ecart depuis le côté droit\". Valeur par défaut : {{value|0,00 mm}}.

-    {{PropertyData/fr|invert|Bool} :} "Inverser la direction du pliage". Valeur par défaut : `False`.
    * {{PropertyData/fr|length|Length}} : "Longueur du mur". Valeur par défaut : {{value|10,00 mm}}.
    * {{PropertyData/fr|radius|Length}} : "Rayon de courbure". Valeur par défaut : {{value|1,00 mm}}.

    {{Properties_Title|Parameters Ex}}

    * {{PropertyData/fr|Auto Miter|Bool}} : "Activer l'onglet automatique". Valeur par défaut : `True`.
    * {{PropertyData/fr|extend1|Distance}} : "Étendre à partir du côté gauche". Valeur par défaut : {{value|0,00 mm}}.
    * {{PropertyData/fr|extend2|Distance} :} "Extension à partir du côté droit". Valeur par défaut : {{value|0,00 mm}}.
    * {{PropertyData/fr|kfactor|FloatConstraint}} : "Emplacement de la ligne neutre. Attention : Utiliser les normes ANSI et non DIN.". </br>Par défaut : {{value|0,50}}. Facteur K (également connu sous le nom de facteur neutre) pour le coude. Utilisé pour calculer la marge de pliage lors du dépliage.
    * {{PropertyData/fr|max Extend Dist|Length}} : "Distance maximale d'extension de l'onglet automatique". Valeur par défaut : {{value|5,00 mm}}.
    * {{PropertyData/fr|min Gap|Length}} : "L'espacement minimum de l'onglet automatique. Valeur par défaut : {{value|5,00 mm}}.
    * {{PropertyData/fr|miterangle1|Angle}} : "Angle de l'onglet de pliage depuis le côté gauche". Angle par défaut : {{value|0,00°}}.
    * {{PropertyData/fr|miterangle2|Angle}} : "Angle de pliage à partir du côté droit. Angle par défaut : {{value|0,00°}}.
    * {{PropertyData/fr|offset|Distance}} : "Coude décalé". Valeur par défaut : {{value|0,00 mm}}.
    * {{PropertyData/fr|unfold|Bool}} : "Montre la vue dépliée du pliage en cours". Valeur par défaut : `False`. </br> `True` Déplie le pli.

    {{Properties_Title|Parameters Ex2}}

    * {{PropertyData/fr|Sketch|Link}} : "Objet de l'esquisse".
    * {{PropertyData/fr|sketchflip|Bool}} : "Retourner la direction de l'esquisse". Valeur par défaut : `False`.
    * {{PropertyData/fr|sketchinvert|Bool}} : "Inverser le début de l'esquisse". Valeur par défaut : `False`.

    {{Properties_Title|Parameters Ex3}}

    * {{PropertyData/fr|Length List|FloatList}} : "Longueur de la liste des parois". Valeur par défaut : {{value|[10,00]}}.
    * {{PropertyData/fr|bend AList|FloatList}} : "Liste des angles de pliage". Valeur par défaut : {{value|[90,00]}}.

    {{Properties_Title|Parameters Relief}}

    * {{PropertyData/fr|Relief Factor|Float}} : "Facteur de soulagement". Valeur par défaut : {{value|0,70}}.
    * {{PropertyData/fr|Use Relief Factor|Bool} :} "Use Relief Factor". Valeur par défaut : `False`.
    * {{PropertyData/fr|min Relief Gap|Length}} : "Espace minimum pour la coupe en relief". Valeur par défaut : {{value|1,00 mm}}.
    * {{PropertyData/fr|relief Type|Enumeration}} : "Type de relief". {{value|Rectangle}} (valeur par défaut), {{value|Rectangle}}. (par défaut), {{value|Round}}. Activé uniquement lorsqu'une valeur d'écart est définie.
    * {{PropertyData/fr|reliefd|Length}} : "Profondeur du relief". Valeur par défaut : {{value|1,00 mm}}. Activé uniquement lorsqu'une valeur d'écart est définie.
    * {{PropertyData/fr|reliefw|Length}} : "Largeur du relief". Valeur par défaut : {{value|0,80 mm}}. Activé uniquement lorsqu'une valeur d'écart est définie.

    == Exemple ==

    <img src="images/SheetMetal_AddWall-01.png" width=300px>
    *Un plateau tout simple*
    <div class="mw-collapsible mw-collapsed">
    <div class="mw-collapsible-content">

    === Préparation ===

    Ce plateau est constitué d'une ébauche rectangulaire à laquelle on a ajouté des parois sur les bords de son contour. Il faut donc préparer à l'avance un croquis de contour pour l'ébauche.

    <img src="images/SheetMetal_AddWall-02.png" width=200px>
    *Un simple contour rectangulaire*

    === Processus de travail ===

    ## Créer une ébauche
    ## Sélectionnez l'esquisse de contour </br> <img src="images/SheetMetal_AddWall-03.png" width=240px> 
    ## Appuyez sur le bouton **<img src="images/SheetMetal_AddBase.svg" width=16px> [Make Base Wall](SheetMetal_AddBase/fr.md)** ou utilisez le raccourci clavier : **C** puis **F**. </br> <img src="images/SheetMetal_AddWall-04.png" width=240px> </br> (L'ébauche est générée dans la direction z </br> </br>.
    # Ajouter des murs aux bords du contour 
    ## Sélectionnez les '''bords du contour''' du blanc </br> <img src="images/SheetMetal_AddWall-05.png" width=240px>.
    ## Appuyez sur le bouton **<img src="images/SheetMetal_AddWall.svg" width=16px> [Make Wall](SheetMetal_AddWall/fr.md)** ou utilisez le raccourci clavier : **W**. </br> <img src="images/SheetMetal_AddWall-06.png" width=240px>
    ## Si le pli est à 90° vers le bas, mettez la valeur de la propriété '''invert''' à true pour inverser le sens (et '''length''' à une valeur plus faible pour les petits murs) </br> <img src="images/SheetMetal_AddWall-01.png" width=240px>. </br> </br>
    # Ajouter d'autres parois
    ## Sélectionnez les '''bords extérieurs supérieurs''' du plateau </br> <img src="images/SheetMetal_AddWall-08.png" width=240px>.
    ## Appuyez sur le bouton **<img src="images/SheetMetal_AddWall.svg" width=16px> [Make Wall](SheetMetal_AddWall/fr.md)** ou utilisez le raccourci clavier : **W**.  </br> <img src="images/SheetMetal_AddWall-09.png" width=240px> </br>
    ## Les parois sont un peu trop longues et il faut donc mettre la propriété '''longueur''' à une valeur inférieure </br> <img src="images/SheetMetal_AddWall-10.png" width=240px>.
    ## Si vous aimez que les plis se mettent vers l'extérieur mettez la valeur '''invert''' à true </br> <img src="images/SheetMetal_AddWall-11.png" width=240px>. 

    C'est fait!
    </div> 
    </div> 


    

    [[Category:SheetMetal]]
    [[Category:Addons]]
    [[Category:External Command Reference\]\]

---
[documentation index](../README.md) > [SheetMetal](Category_SheetMetal.md) > SheetMetal AddWall/fr
