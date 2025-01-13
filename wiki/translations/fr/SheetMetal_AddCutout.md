---
 GuiCommand:
   Name: SheetMetal AddCutout
   Name/fr: SheetMetal Découpe extrudée
   MenuLocation: SheetMetal , Découpe extrudée
   Workbenches: SheetMetal_Workbench/fr
   Shortcut: **E** **C**
   Version: 0.5.04
---

# SheetMetal AddCutout/fr

## Description

La commande <img alt="" src=images/SheetMetal_AddCutout.svg  style="width:16px;"> [SheetMetal Découpe extrudée](SheetMetal_AddCutout/fr.md) crée une découpe extrudée à partir d\'une extrusion d\'esquisse.

La différence entre une découpe \"normale\" et une découpe extrudée est que, dans ce dernier cas, les bords sont perpendiculaires à la face sélectionnée de l\'objet en tôle. L\'effet de la commande n\'est visible que si l\'esquisse n\'est pas parallèle à la face.

![](images/SheetMetal_AddCutout_Example.png )



*Une découpe extrudée basée sur une esquisse circulaire*



## Utilisation

1.  Sélectionnez une face plane et une esquisse avec un contour fermé (dans n\'importe quel ordre).
2.  Il y a plusieurs façons de lancer la commande :
    -   Appuyez sur le **<img src="images/SheetMetal_AddCutout.svg" width=16px> [Découpe extrudée](SheetMetal_AddCutout/fr.md)**.
    -   Sélectionnez l\'option **SheetMetal → <img src="images/SheetMetal_AddCutout.svg" width=16px> Découpe extrudée** du menu.
    -   Cliquez avec le bouton droit de la souris dans la [vue en arborescence](Tree_view/fr.md) ou la [vue 3D](3D_view/fr.md) et sélectionnez l\'option **SheetMetal → <img src="images/SheetMetal_AddCutout.svg" width=16px> Découpe extrudée** dans le menu contextuel.
    -   Utilisez le raccourci clavier : **E** puis **C**.
3.  Le [panneau des tâches](Task_panel/fr.md) *Paramètres de la découpe extrudée* s\'ouvre.
4.  Vous pouvez appuyer sur le bouton **Face** pour resélectionner la face plane.
5.  Vous pouvez appuyer sur le bouton **Esquisse** pour resélectionner une esquisse.
6.  Vous pouvez ajuster les paramètres dans le panneau des tâches.
7.  Appuyez sur le bouton **OK** pour terminer la commande et fermer le panneau des tâches.
8.  Un objet **ExtrudedCutout** sera créé et consistera en un ou plusieurs trous dans une ligne à travers l\'objet.
9.  Vous pouvez ajuster les paramètres dans l\'[éditeur de propriétés](Property_editor/fr.md).



## Propriétés

Voir aussi : [Éditeur de propriétés](Property_editor/fr.md)

Un objet SheetMetal ExtrudedCutout est dérivé d\'un objet [Part Feature](Part_Feature/fr.md) ou, s\'il se trouve à l\'intérieur d\'un [PartDesign Corps](PartDesign_Body/fr.md), à partir d\'un objet [PartDesign Feature](PartDesign_Feature/fr.md), dont il hérite de toutes les propriétés. Il possède également les propriétés supplémentaires suivantes :



### Données


{{Properties_Title|Extruded Cutout}}

-    **Cut Side|Enumeration**: valeur par défaut {{value|Inside}}. Côté de la coupe.

-    **Cut Type|Enumeration**: valeur par défaut {{value|Through everything both sides}}. Type de coupe.

-    **Extrusion Length1|Length|hidden**: valeur par défaut {{value|500.0 mm}}. Longueur de la direction de l\'extrusion 1.

-    **Extrusion Length2|Length|hidden**: valeur par défaut {{value|500.0 mm}}. Longueur de la direction de l\'extrusion 2.

-    **Selected Face|LinkSub**: l\'objet et la face sélectionnés.

-    **Sketch|Link**: esquisse de la découpe.


{{Properties_Title|Extruded Cutout Improvements}}

-    **Improve Cut|Bool**: valeur par défaut {{value|False}}. Améliore la géométrie de la découpe si elle entre dans la zone de coupe. Ne sélectionnez {{value|True}} que si la découpe a besoin d\'être corrigée, car elle peut être lente.

-    **Improve Level|IntegerConstraint|hidden**: valeur par défaut {{value|4}}. Niveau d\'amélioration de la qualité de la coupe. Plus de 10 peut prendre beaucoup de temps.

-    **Refine|Bool**: valeur par défaut {{value|False}}. Nettoie la géométrie.



---
⏵ [documentation index](../README.md) > [SheetMetal](Category_SheetMetal.md) > [Addons](Category_Addons.md) > [External Command Reference](Category_External Command Reference.md) > SheetMetal AddCutout/fr
