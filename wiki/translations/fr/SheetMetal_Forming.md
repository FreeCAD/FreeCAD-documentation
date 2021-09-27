---
- GuiCommand:/fr
   Name:SheetMetal Forming
   Name/fr:SheetMetal Outil d'emboutissage
   MenuLocation:SheetMetal → Make Forming in Wall
   Workbenches:[SheetMetal](SheetMetal_Workbench/fr.md)
   Shortcut:**M** **F**
---

# SheetMetal Forming/fr

## Description

La commande <img alt="" src=images/SheetMetal_Forming.svg  style="width:24px;"> **SheetMetal Forming** crée une forme emboutie dans une paroi en tôle à l\'aide d\'un objet solide distinct.

Le plan arrière du solide définissant la forme et la face à emboutir sont utilisés pour positionner et orienter la forme emboutie, c\'est-à-dire que leurs systèmes de coordonnées locales auront la même origine et la même orientation par défaut. L\'angle autour de l\'axe z et les décalages dans les directions x, y et z peuvent être modifiés en changeant les valeurs des paramètres dans la fenêtre des propriétés.

Une esquisse peut être ajoutée pour multiplier et distribuer la forme emboutie selon des motifs réguliers ou irréguliers (en utilisant les points centraux de cercles ou d\'arcs).

Une petite sélection de fonctions qui peuvent être créées :

<img alt="" src=images/SheetMetal_Forming-08.png  style="width:200px;"> <img alt="" src=images/SheetMetal_Forming-09.png  style="width:200px;"> <img alt="" src=images/SheetMetal_Forming-10.png  style="width:200px;"> <img alt="" src=images/SheetMetal_Forming-11.png  style="width:200px;"> 
*fossettes, persiennes, découpes dessinées, ponts*

## Utilisation

### Fossette

1.  Sélectionnez la face de l\'objet SheetMetal à emboutir.
2.  Sélectionnez la **face inférieure** (face arrière) de la forme définissant le solide.
    -   **Remarque:** n\'oubliez pas la touche **Control**/**Command**!
3.  Activez la commande <img alt="" src=images/SheetMetal_Forming.svg  style="width:16px;"> [Outil d\'emboutissage](SheetMetal_Forming/fr.md) en utilisant :
    -   le bouton **<img src="images/SheetMetal_Forming.svg" width=16px> [Make Forming in Wall](SheetMetal_Forming/fr.md)**.
    -   par le menu déroulant **SheetMetal → <img src="images/SheetMetal_Forming.svg" width=16px> Make Forming in Wall
**
    -   par le raccourci clavier : **M** puis **F**

### Persienne

1.  Sélectionnez la face de l\'objet SheetMetal à emboutir.
2.  Sélectionnez la **face inférieure** (face arrière) de la forme définissant le solide.
3.  Sélectionnez une **face latérale** adjacente à la face inférieure pour marquer la zone à découper.
    -   **Remarque:** n\'oubliez pas la touche **Control**/**Command**!
4.  Activez la commande <img alt="" src=images/SheetMetal_Forming.svg  style="width:16px;"> [Make Forming in Wall](SheetMetal_Forming/fr.md) (voir ci-dessus)

### Pont

1.  Sélectionnez la face de l\'objet SheetMetal à emboutir.
2.  Sélectionnez la **face inférieure** (face arrière) de la forme définissant le solide.
3.  Sélectionnez une **face latérale** adjacente à la face inférieure pour marquer une zone à découper.
4.  Sélectionnez la **face opposée** adjacente à la face inférieure pour marquer l\'autre zone à découper.
    -   **Remarque:** n\'oubliez pas la touche **Control**/**Command**!
5.  Activez la commande <img alt="" src=images/SheetMetal_Forming.svg  style="width:16px;"> [Make Forming in Wall](SheetMetal_Forming/fr.md) (voir ci-dessus)

### Découpe dessinée 

1.  Sélectionnez la face de l\'objet SheetMetal à emboutir.
2.  Sélectionnez la **face inférieure** (face arrière) de la forme définissant le solide.
3.  Sélectionnez la **face supérieure** opposée à la face inférieure pour marquer la zone à découper.
    -   **Remarque:** n\'oubliez pas la touche **Control**/**Command**!
4.  Activez la commande <img alt="" src=images/SheetMetal_Forming.svg  style="width:16px;"> [Make Forming in Wall](SheetMetal_Forming/fr.md) (voir ci-dessus)

### Multiplication et motif 

Pour multiplier et modeler la fonction emboutie, une **esquisse** contenant des cercles et des arcs peut être ajoutée à la propriété {{PropertyData/fr|Sketch}} de l\'objet **WallForming**.

Les points centraux des cercles ou des arcs sont utilisés pour fournir des positions où placer les instances de la caractéristique en relief. Ils n\'influencent pas l\'orientation des instances.

L\'orientation dépend toujours de l\'orientation de la première face sélectionnée.

### Ajouter des congés 

1.  Passez à l\'<img alt="" src=images/Workbench_PartDesign.svg  style="width:16px;"> [atelier PartDesign](PartDesign_Workbench/fr.md).
2.  Sélectionnez un bord sur la face supérieure de l\'objet SheetMetal pour recevoir un congé.
3.  Activez le <img alt="" src=images/PartDesign_Fillet.svg  style="width:16px;"> [Congé](PartDesign_Fillet/fr.md) en utilisant la commande :
    -   par le bouton **<img src="images/PartDesign_Fillet.svg" width=16px> [Congé](PartDesign_Fillet/fr.md)
**
    -   par le menu déroulant **Conception de pièce → Appliquer une fonction d'habillage → <img src="images/PartDesign_Fillet.svg" width=16px> Congé
**
4.  Mettez la propriété  (C\'est assez **important** pour le prochain congé).
5.  Sélectionnez un bord sur la face inférieure de l\'objet SheetMetal pour recevoir un congé.
6.  Activez le <img alt="" src=images/PartDesign_Fillet.svg  style="width:16px;"> [Congé](PartDesign_Fillet/fr.md) (voir ci-dessus)

## Propriétés

Voir aussi : [Éditeur de propriétés](Property_editor/fr.md)

Un objet SheetMetal WallForming est dérivé d\'un objet [Part Feature](Part_Feature/fr.md) et hérite de toutes ses propriétés. Il possède également les propriétés supplémentaires suivantes :

### Données


{{Properties_Title|Base}}

-    {{PropertyData/fr|Label|String}}: Valeur par défaut : Le nom modifiable par l\'utilisateur de cet objet, il peut être toute chaîne UTF8 arbitraire.

-    {{PropertyData/fr|Base Feature|Link|hidden}}: Fonctionnalité de base. Lien vers la caractéristique parent.

-    {{PropertyData/fr|_Body|LinkHidden|hidden}}:


{{Properties_Title|Parameters}}

-    {{PropertyData/fr|Suppress Feature|Bool}}: \"Suppression de la fonction de formation\". La valeur par défaut est `False`.

-    {{PropertyData/fr|angle|Angle}}: \"Angle de position de l\'outil\". Angle par défaut : {{value|0,00°}}.

-    {{PropertyData/fr|base Object|LinkSub}}: \"Objet de base\". Lien vers la face planaire à emboutir.

-    {{PropertyData/fr|offset|VectorDistance}}: \"Décalage par rapport au centre de la face\". Valeur par défaut : {{value|[0,00 mm, 0,00 mm, 0,00 mm]}}.

-    {{PropertyData/fr|thickness|Distance}}: \"Epaisseur de la tôle\". Epaisseur de la {{PropertyData/fr|Base Feature||hidden}} :.

-    {{PropertyData/fr|tool Object|LinkSub}}: \"Objet Outil de Formage\". Lien vers la face planaire utilisée pour positionner l\'outil de formage.


{{Properties_Title|Parameters1}}

-    {{PropertyData/fr|Sketch|Link}}: \"Esquisse de point sur la tôle\". Lien vers l\'esquisse contenant des informations sur la manière de multiplier et de distribuer les instances de l\'outil de formage. (Les points centraux des cercles et des arcs sont utilisés pour créer et positionner ces instances).

## Exemple

<img alt="" src=images/SheetMetal_Forming-01.png  style="width:300px;"> <img alt="" src=images/SheetMetal_Forming-02.png  style="width:300px;"> 
*Un bol hexagonal avec centre repoussé*


<div class="mw-collapsible mw-collapsed">


<div class="mw-collapsible-content">

### Préparation

Ce bol est fait d\'un objet en tôle pliée avec une forme emboutie, les deux doivent être préparés à l\'avance.

Il n\'est pas nécessaire de travailler avec des esquisses coplanaires ici.

<img alt="" src=images/SheetMetal_Forming-03.png  style="width:200px;"> 
*Bol en tôle et objet embouti*

### Processus de travail 

1.  Sélectionnez la paroi de l\'objet SheetMetal à emboutir.
2.  Sélectionnez la **face arrière** de la forme définissant le solide (N\'oubliez pas la touche <img alt="" src=images/SheetMetal_Forming-04.png  style="width:240px;">
3.  Appuyez sur le bouton ou utilisez le raccourci clavier :  <img alt="" src=images/SheetMetal_Forming-05.png  style="width:240px;">
4.  Filetter les arêtes vives :
    -   Retournez le bol et sélectionnez une ou plusieurs arêtes pour les plus petits rayons intérieurs.
    -   Appuyez sur le bouton <img alt="" src=images/SheetMetal_Forming-12.png  style="width:240px;"> **\--\>**\' <img alt="" src=images/SheetMetal_Forming-02.png  style="width:240px;">
    -   Retournez à nouveau le bol et sélectionnez une ou plusieurs arêtes pour les plus grands rayons extérieurs.
    -   Appuyez sur le bouton <img alt="" src=images/SheetMetal_Forming-13.png  style="width:240px;"> **\--\>**\' <img alt="" src=images/SheetMetal_Forming-01.png  style="width:240px;">  Fait!  
5.  Modifier l\'orientation et la position (doit être fait avant la mise en congés).
    -   Activez l\'objet <img alt="" src=images/SheetMetal_Forming.svg  style="width:16px;"> WallForming dans la [Vue en arborescence](Tree_view/fr.md).
    -   Définissez la valeur de la propriété  <img alt="" src=images/SheetMetal_Forming-14.png  style="width:240px;">
    -   Définir la valeur de la propriété  <img alt="" src=images/SheetMetal_Forming-06.png  style="width:240px;"> Ici, il est clair que cela n\'a pas de sens de déplacer la géométrie en relief en dehors du mur sélectionné.  
    -   Définir la valeur de la propriété  <img alt="" src=images/SheetMetal_Forming-07.png  style="width:240px;"> Au moins, le FreeCAD ne plante pas quand une pièce a deux corps\....  

    1.  Quelques conseils
    2.  La hauteur du solide de définition détermine la profondeur de la forme emboutie. Cela signifie que changer le paramètre **offset, z** pour modifier la profondeur ne donnera pas les résultats escomptés.
    3.  La géométrie emboutie est constituée d\'un objet coquille c\'est-à-dire qu\'elle a une épaisseur constante. Et donc le solide de définition doit être décalable, sinon l\'outil échouera à créer l\'emboutissage.
    4.  Si les bords extérieurs sont filetés en premier, cela peut déchirer l\'objet en plusieurs morceaux lorsque les rayons sont définis trop grands.


</div>


</div>




_ _ _

---
[documentation index](../README.md) > [SheetMetal](Category_SheetMetal.md) > SheetMetal Forming/fr
