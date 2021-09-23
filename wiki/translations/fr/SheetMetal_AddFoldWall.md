---
- GuiCommand:/fr
   Name:SheetMetal AddFoldWall
   Name/fr:SheetMetal Pli sur tôle
   MenuLocation:SheetMetal → Fold a Wall
   Workbenches:[SheetMetal](SheetMetal_Workbench/fr.md)
   Shortcut:**C** **F**
---

## Description

La commande <img alt="" src=images/SheetMetal_AddFoldWall.svg  style="width:24px;"> **SheetMetal AddFoldWall** permet de plier une tôle selon une ligne choisie avec un rayon de courbure spécifié.

## Utilisation

1.  Sélectionner une face plane de l\'objet SheetMetal
2.  Sélectionnez une ligne coplanaire
3.  Appuyez sur le bouton ou utilisez le raccourci clavier : **C** puis **F**.

## Propriétés

Voir aussi: [Éditeur de propriétés](Property_editor/fr.md)

Un objet SheetMetal Pli sur tôle est dérivé d\'un objet [Part Feature](Part_Feature/fr.md) et hérite de toutes ses propriétés. Il possède également les propriétés supplémentaires suivantes :

### Données


{{Properties_Title|Base}}

-    {{PropertyData/fr|Label|String}}: Valeur par défaut : Le nom modifiable par l\'utilisateur de cet objet, il peut être toute chaîne UTF8 arbitraire.

-    {{PropertyData/fr|Base Feature|Link|hidden}}: Fonctionnalité de base. Lien vers la caractéristique parent.

-    {{PropertyData/fr|_Body|LinkHidden|hidden}}: Lien caché vers le corps du parent.


{{Properties_Title|Parameters}}

-    {{PropertyData/fr|Bend Line|Link}}: \"Liste des lignes de référence de pliage\". Liens vers les objets de la ligne de pliage.

-    {{PropertyData/fr|Position|Enumeration}}: \"Position de la ligne de pliage\". {{value|forward}} (valeur par défaut), {{value|middle}}, {{value|backward}}.

-    {{PropertyData/fr|angle|Angle}}: \"Angle de pliage\". Angle par défaut : {{value|90,00°}}.

-    {{PropertyData/fr|base Object|LinkSub}}: \"Objet de base\". Lien vers la face planaire à plier.

-    {{PropertyData/fr|invert|Bool}}: \"Inverser la direction du pliage\". Valeur par défaut : `False`.

-    {{PropertyData/fr|invertbend|Bool}}: \"Inverser la direction de pliage du solide\". Valeur par défaut : `False`. `True` permute le côté de la ligne à plier.

-    {{PropertyData/fr|kfactor|FloatConstraint}}: \"Position de l\'axe neutre\". Valeur par défaut : {{value|0,50}}.

-    {{PropertyData/fr|radius|Length}}: \"Rayon de pliage \". Valeur par défaut : {{value|1,00 mm}}.

-    {{PropertyData/fr|unfold|Bool}}: \"Pliage déplié\". Valeur par défaut : `False`.

## Exemple

<img alt="" src=images/SheetMetal_AddFoldWall-01.png  style="width:300px;"> 
*Un simple clip*


<div class="mw-collapsible mw-collapsed">


<div class="mw-collapsible-content">

### Préparation

Ce clip est fait d\'un blanc qui reçoit trois plis et donc nous avons besoin de quatre schémas préparés à l\'avance :

:   \- un pour le contour plus la fente (vierge)
:   \- un pour le pliage de la pointe
:   \- un pour le pliage vers le haut
:   \- un pour le pliage vers le bas

La façon la plus simple de garantir qu\'une face de la découpe et toutes les lignes de pliage sont coplanaires est de créer toutes les esquisses sur le même plan - le **XY\_Plane** dans ce cas.

Les lignes de pliage pourraient être créées avec d\'autres outils, mais bon, nous avons une <img alt="" src=images/Workbench_Sketcher.svg  style="width:24px;">[esquisse](Sketcher_Workbench/fr.md) !

<img alt="" src=images/SheetMetal_AddFoldWall-21.png  style="width:280px;"> <img alt="" src=images/SheetMetal_AddFoldWall-20.png  style="width:200px;"> 
*Esquisses sur leur plan commun et leur représentation dans l'arbre de conception*

### Processus de travail 

1.  Créer une ébauche
    1.  Sélectionnez l\'esquisse de contour
    2.  Appuyez sur le bouton ou utilisez le raccourci clavier :  <img alt="" src=images/SheetMetal_AddFoldWall-02.png  style="width:120px;"> <img alt="" src=images/SheetMetal_AddFoldWall-03.png  style="width:280px;"> 
2.  Plier la pointe
    1.  Sélectionner la **face inférieure** de l\'ébauche.
    2.  Sélectionnez l*\'esquisse* nommée ***Tip Fold line*** (de préférence à partir de l\'arborescence)  (et n\'oubliez pas la touche contrôle/commande ).
    3.  Appuyez sur le ou utilisez le raccourci clavier : <img alt="" src=images/SheetMetal_AddFoldWall-10.png  style="width:120px;"> <img alt="" src=images/SheetMetal_AddFoldWall-04.png  style="width:120px;"> <img alt="" src=images/SheetMetal_AddFoldWall-05.png  style="width:280px;">
    4.  Le pli doit être à 90° vers le bas et donc certaines valeurs dans la fenêtre des propriétés doivent être définies par exemple :  - la valeur **angle** à 60°  - la valeur **inverser** à true pour un pliage vers le haut  .
3.  Créer le pli vers le bas
    1.  Sélectionnez la **face inférieure** de l\'ébauche.
    2.  Et ensuite le **croquis** nommé ***Pli descendant ligne***.
    3.  Appuyez sur le ou utilisez le raccourci clavier : <img alt="" src=images/SheetMetal_AddFoldWall-11.png  style="width:120px;"> <img alt="" src=images/SheetMetal_AddFoldWall-06.png  style="width:120px;"> <img alt="" src=images/SheetMetal_AddFoldWall-07.png  style="width:280px;">
    4.  Réglez la valeur *angle* à 92°.
    5.  Si la mauvaise section de la pièce a bougé, réglez la valeur **invertbend** sur true  .
    6.  Pour créer le pliage vers le haut
    7.  sélectionnez la **face inférieure** de la pièce brute.
    8.  puis le **sketch** nommé ***Up-Fold line***.
    9.  Appuyez sur le bouton ou utilisez le raccourci clavier : <img alt="" src=images/SheetMetal_AddFoldWall-12.png  style="width:120px;"> <img alt="" src=images/SheetMetal_AddFoldWall-08.png  style="width:120px;"> <img alt="" src=images/SheetMetal_AddFoldWall-09.png  style="width:280px;">
    10. Définissez la valeur **angle** à 80°.
    11. Si le pli est vers le bas définir la valeur **invert** à true.
    12. Si nécessaire, mettez la valeur **invertbend** à true.  

C\'est fait!

Remarque : dans la vie réelle, le pliage vers le haut doit être effectué avant le pliage vers le bas. Seul le monde virtuel de la CAO nous permet de plier à travers un matériau solide. De cette façon, l\'orientation de la section statique ne change pas.  Toutes les esquisses se trouvent sur le même plan pour éviter les esquisses attachées aux faces mobiles.


</div>


</div>




[Category:SheetMetal](Category:SheetMetal.md) [Category:Addons](Category:Addons.md) [Category:External Command Reference](Category:External_Command_Reference.md)
