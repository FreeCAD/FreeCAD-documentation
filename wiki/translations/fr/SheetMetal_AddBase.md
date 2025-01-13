---
 GuiCommand:
   Name: SheetMetal AddBase
   Name/fr: SheetMetal Tôle de base
   MenuLocation: SheetMetal , Créer une paroi/tôle
   Workbenches: SheetMetal_Workbench/fr
   Shortcut: **C** **B**
---

# SheetMetal AddBase/fr

## Description

La commande <img alt="" src=images/SheetMetal_AddBase.svg  style="width:24px;"> **SheetMetal Tôle de base** crée un objet de base SheetMetal à partir d\'une esquisse.

A partir d\'un contour ouvert, il crée un **profil** extrudé :

<img alt="" src=images/SheetMetal_AddBase-01.png  style="width:200px;"> <img alt="" src=images/Button_right.svg  style="width:16px;"> <img alt="" src=images/SheetMetal_AddBase-02.png  style="width:200px;">

A partir d\'un contour fermé, il crée une **tôle** de base (vide) :

<img alt="" src=images/SheetMetal_AddBase-03.png  style="width:200px;"> <img alt="" src=images/Button_right.svg  style="width:16px;"> <img alt="" src=images/SheetMetal_AddBase-04.png  style="width:200px;">



## Utilisation



### Profilage

1.  Sélectionnez une <img alt="" src=images/Workbench_Sketcher.svg  style="width:16px;"> [esquisse](Sketcher_Workbench/fr.md) à **contour ouvert**.
2.  Il y a plusieurs façons de lancer la commande :
    -   Appuyez sur le bouton **<img src="images/SheetMetal_AddBase.svg" width=16px> [Créer une paroi/tôle](SheetMetal_AddBase/fr.md)**.
    -   Sélectionnez l\'option **SheetMetal → <img src="images/SheetMetal_AddBase.svg" width=16px> Créer une paroi/tôle** du menu.
    -   Utilisez le raccourci clavier : **C** puis **B**.
    -   Cliquez avec le bouton droit de la souris dans la [vue en arborescence](Tree_view/fr.md) ou la [vue 3D](3D_view/fr.md) et sélectionnez l\'option **SheetMetal → <img src="images/SheetMetal_AddBase.svg" width=16px> Créer une paroi/tôle** dans le menu contextuel.
3.  Un objet **BaseBend** sera créé. Les coins du contour seront automatiquement convertis en plis arrondis.
4.  Ajustez les paramètres du profil dans l\'[éditeur de propriétés](Property_editor/fr.md) :
    -   
        **length**
        
        pour la longueur d\'extrusion du profil,

    -   
        **thickness**
        
        pour l\'épaisseur de la paroi du profil,

    -   
        **radius**
        
        pour le rayon intérieur des plis ajoutés automatiquement.



### Tôle

1.  Sélectionnez une <img alt="" src=images/Workbench_Sketcher.svg  style="width:16px;"> [esquisse](Sketcher_Workbench/fr.md) à **contour fermé**.
2.  Lancez la commande comme décrit ci-dessus.
3.  Ajustez les paramètres de la tôle dans l\'[éditeur de propriétés](Property_editor/fr.md) :
    -   
        **thickness**
        
        pour l\'épaisseur de la tôle.

:   

    :   (**length** et **radius** ne sont pas utilisées pour les tôles).



## Propriétés

Voir aussi: [Éditeur de propriétés](Property_editor/fr.md)

Un objet SheetMetal BaseBend est dérivé d\'un objet [Part Feature](Part_Feature/fr.md) ou, s\'il se trouve à l\'intérieur d\'un [PartDesign Corps](PartDesign_Body/fr.md), à partir d\'un objet [PartDesign Feature](PartDesign_Feature/fr.md), dont il hérite de toutes les propriétés. Il possède également les propriétés supplémentaires suivantes :



### Données


{{Properties_Title|Parameters}}

-    **Bend Side|Enumeration**: type de contre-dépouille, définit de quel côté d\'une courbe de profil l\'épaisseur s\'applique. {{value|Outside}} (par défaut), {{value|Inside}}, {{value|Middle}} (non utilisé pour les tôles).

-    **Bend Sketch|Link**: objet esquisse de la paroi. Lien vers l\'esquisse du profil/contour.

-    **Mid Plane|Bool**: extrusion symétrique par rapport au plan, longueur d\'un profil ou l\'épaisseur d\'une tôle s\'étend d\'un côté du plan de l\'esquisse si `False` (par défaut) ou symétriquement par rapport au plan de l\'esquisse. (par défaut) ou symétriquement des deux côtés si `True`.

-    **Reverse|Bool**: inverse la direction de l\'extrusion d\'un profil ou de l\'épaisseur d\'une tôle. Valeur par défaut : `False`.

-    **length|Length**: longueur d\'extrusion d\'un profil. Par défaut : {{value|100,00 mm}} (non utilisé pour les plaques).

-    **radius|Length**: rayon intérieur des plis ajoutés automatiquement. Par défaut : {{value|1,00 mm}} (non utilisé pour les plaques).

-    **thickness|Length**: épaisseur de la paroi d\'un profilé ou d\'une tôle. Valeur par défaut : {{value|1,00 mm}}.



---
⏵ [documentation index](../README.md) > [SheetMetal](Category_SheetMetal.md) > [Addons](Category_Addons.md) > [External Command Reference](Category_External Command Reference.md) > SheetMetal AddBase/fr
