---
 GuiCommand:
   Name: SheetMetal SketchOnSheet
   Name/fr: SheetMetal Perçage de paroi
   MenuLocation: SheetMetal , Sketch On Sheet metal
   Workbenches: SheetMetal_Workbench/fr
   Shortcut: **M** **S**
---

# SheetMetal SketchOnSheet/fr

## Description

La commande <img alt="" src=images/SheetMetal_SketchOnSheet.svg  style="width:16px;"> [Perçage de paroi](SheetMetal_SketchOnSheet/fr.md) découpe des trous le long des parois pliées d\'un objet en tôle. Pour la disposition des trous, une <img alt="" src=images/Workbench_Sketcher.svg  style="width:16px;"> [esquisse](Sketcher_Workbench/fr.md) est utilisée.

Contrairement à la commande <img alt="" src=images/PartDesign_Pocket.svg  style="width:16px;"> [PartDesign Cavité](PartDesign_Pocket/fr.md) où les trous sont simplement découpés le long de la normale à l\'esquisse (axe z local), cet outil agit comme s\'il dépliait l\'objet en tôle, découpait les trous et repliait l\'objet.

## Utilisation

1.  Sélectionner une **face plane**.
2.  Sélectionner une face coplanaire <img alt="" src=images/Workbench_Sketcher.svg  style="width:16px;"> [esquisse](Sketcher_Workbench/fr.md). (c\'est-à-dire située sur le même plan) pour la **disposition des trous** (de préférence à partir de la [Vue en arborescence](Tree_view/fr.md)).
    -   **Remarque:** N\'oubliez pas la touche **Control**/**Command** !
3.  Activez la commande <img alt="" src=images/SheetMetal_SketchOnSheet.svg  style="width:16px;"> Sketch Perçage de paroi en faisant :
    -   
        **<img src="images/SheetMetal_SketchOnSheet.svg" width=16px> [Sketch On Sheet metal](SheetMetal_SketchOnSheet/fr.md)
**
        
        .

    -   
        **SheetMetal → <img src="images/SheetMetal_SketchOnSheet.svg" width=16px> Sketch On Sheet metal
**
        
        menu déroulant

    -   Raccourci clavier : **M** puis **S**

## Remarques

-   L\'esquisse peut contenir plus d\'un contour.
-   Tout contour doit au moins toucher la face planaire, sinon il ne fera pas de trou du tout.

## Propriétés

Voir aussi : [Éditeur de propriétés](Property_editor/fr.md)

Un objet SheetMetal SketchOnSheet est dérivé d\'un objet [Part Feature](Part_Feature/fr.md) et hérite de toutes ses propriétés. Il possède également les propriétés supplémentaires suivantes :

### Données


{{Properties_Title|Base}}

-    {{PropertyData/fr|Label|String}}: Valeur par défaut : Le nom modifiable par l\'utilisateur de cet objet, il peut être toute chaîne UTF8 arbitraire.

-    {{PropertyData/fr|Base Feature|Link|hidden}}: Fonctionnalité de base. Lien vers la caractéristique parent.

-    {{PropertyData/fr|_Body|LinkHidden|hidden}}: Lien caché vers le corps du parent.


{{Properties_Title|Parameters}}

-    {{PropertyData/fr|Sketch|Link}}: \"Esquisse sur tôle\". Lien vers l\'esquisse de la disposition des trous/découpe.

-    {{PropertyData/fr|base Object|LinkSub}}: \"Objet de base\". Lien vers la face plane où commence la découpe.

-    {{PropertyData/fr|kfactor|FloatConstraint}}: \"Ecart par rapport au côté gauche\". Valeur par défaut : {{value|0,50}}.

## Exemple

<img alt="" src=images/SheetMetal_SketchOnSheet-05.png  style="width:300px;"> 
*Un simple bidule*


<div class="mw-collapsible mw-collapsed">


<div class="mw-collapsible-content">

### Préparation

Ce bidule est constitué d\'un objet en tôle pliée auquel on a ajouté des trous.  Et donc il faut préparer à l\'avance une esquisse de contour ouvert pour la tôle et un croquis pour la disposition des trous.  Une ligne droite de la première esquisse doit être coplanaire à l\'autre plan de l\'esquisse, cela permettra d\'obtenir une esquisse et une face coplanaires utilisées dans les étapes suivantes.

<img alt="" src=images/SheetMetal_SketchOnSheet-01.png  style="width:200px;"> 
*Seulement un contour et une disposition des trous*

### Déroulement des tâches 

1.  1.  Créer un objet en tôle pliée
    2.  Sélectionnez l\'esquisse **contour**  <img alt="" src=images/SheetMetal_SketchOnSheet-02.png  style="width:240px;">
    3.  Appuyez sur le bouton  <img alt="" src=images/SheetMetal_SketchOnSheet-03.png  style="width:240px;">  
    4.  Découpez des trous
    5.  Sélectionnez la **face planaire**.
    6.  Sélectionnez l\'esquisse **disposition des trous**  <img alt="" src=images/SheetMetal_SketchOnSheet-04.png  style="width:240px;">
    7.  Appuyez sur le bouton  <img alt="" src=images/SheetMetal_SketchOnSheet-05.png  style="width:240px;">  C\'est fait!  

2.  Quelques conseils
    1.  Vérifier si l\'épaisseur de l\'objet plié est construite sur le côté droit.  <img alt="" src=images/SheetMetal_SketchOnSheet-06.png  style="width:240px;">  Le contour jaune doit se trouver sur la face supérieure du pli inférieur (comme indiqué). Pour inverser la direction, définissez la valeur de la propriété **Bend Side** (Outside \<-\> Inside).  
    2.  **Les formes de trous** ne touchant pas la face plane utilisée ne découperont pas de trous dans l\'objet plié.  <img alt="" src=images/SheetMetal_SketchOnSheet-07.png  style="width:240px;"> Le rectangle inférieur qui touche à peine ladite face découpe un trou alors que la forme de fente supérieure ne le fait pas.


</div>


</div>



---
⏵ [documentation index](../README.md) > [SheetMetal](Category_SheetMetal.md) > [Addons](Category_Addons.md) > [External Command Reference](Category_External Command Reference.md) > SheetMetal SketchOnSheet/fr
