---
- GuiCommand:/fr
   Name:SheetMetal SketchOnSheet
   Name/fr:SheetMetal Perçage de paroi
   MenuLocation:SheetMetal → Sketch On Sheet metal
   Workbenches:[SheetMetal](SheetMetal_Workbench/fr.md)
   Shortcut:**M** **S**
---

# SheetMetal SketchOnSheet/fr

## Description

La commande <img alt="" src=images/SheetMetal_SketchOnSheet.svg  style="width:16px;"> [Perçage de paroi](SheetMetal_SketchOnSheet/fr.md) découpe des trous le long des parois pliées d\'un objet en tôle. Pour la disposition des trous, une <img alt="" src=images/Workbench_Sketcher.svg  style="width:16px;"> [esquisse](Sketcher_Workbench/fr.md) est utilisée.

Contrairement à la commande <img alt="" src=images/PartDesign_Pocket.svg  style="width:16px;"> [PartDesign Cavité](PartDesign_Pocket/fr.md) où les trous sont simplement découpés le long de la normale à l\'esquisse (axe z local), cet outil agit comme s\'il dépliait l\'objet en tôle, découpait les trous et repliait l\'objet.

## Utilisation


<div class="mw-translate-fuzzy">

1.  Sélectionner une *face plane*.
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


</div>


<div class="mw-translate-fuzzy">

## Remarques

-   L\'esquisse peut contenir plus d\'un contour.
-   Tout contour doit au moins toucher la face planaire, sinon il ne fera pas de trou du tout.


</div>

-   The sketch may contain more than just one outline.
-   Any outline has to touch the planar face, at least, otherwise it won\'t cut a hole at all.

## Propriétés

See also: [Property editor](Property_editor.md).

A SheetMetal SketchOnSheet object is derived from a [Part Feature](Part_Feature.md) object and inherits all its properties. It also has the following additional properties:

### Données


{{Properties_Title|Base}}

-    **Label|String**: Default value: The user editable name of this object, it may be any arbitrary UTF8 string.

-    **Base Feature|Link|hidden**: Base Feature. Link to the parent feature.

-    **_Body|LinkHidden|hidden**: Hidden link to the parent body.


{{Properties_Title|Parameters}}

-    **Sketch|Link**: \"Sketch on Sheetmetal\". Link to the hole layout/cut-out sketch.

-    **base Object|LinkSub**: \"Base Object\". Link to the planar face where the cut-out starts.

-    **kfactor|FloatConstraint**: \"Gap from Left Side\". Default: {{value|0,50}}.

## Exemple

<img alt="" src=images/SheetMetal_SketchOnSheet-05.png  style="width:300px;">


<div class="mw-translate-fuzzy">


*Un simple bidule*


</div>


<div class="mw-collapsible mw-collapsed">


<div class="mw-collapsible-content">

### Préparation


<div class="mw-translate-fuzzy">

Ce bidule est constitué d\'un objet en tôle pliée auquel on a ajouté des trous.  Et donc il faut préparer à l\'avance une esquisse de contour ouvert pour la tôle et un croquis pour la disposition des trous.  Une ligne droite de la première esquisse doit être coplanaire à l\'autre plan de l\'esquisse, cela permettra d\'obtenir une esquisse et une face coplanaires utilisées dans les étapes suivantes.


</div>

<img alt="" src=images/SheetMetal_SketchOnSheet-01.png  style="width:200px;"> 
*Seulement un contour et une disposition des trous*

### Processus de travail 

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




[Category:SheetMetal](Category:SheetMetal.md) [Category:Addons](Category:Addons.md) [Category:External Command Reference](Category:External_Command_Reference.md)

---
[documentation index](../README.md) > [SheetMetal](Category:SheetMetal.md) > SheetMetal SketchOnSheet/fr
