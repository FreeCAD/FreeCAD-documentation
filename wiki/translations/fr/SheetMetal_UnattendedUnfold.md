---
 GuiCommand:
   Name: SheetMetal UnattendedUnfold
   Name/fr: SheetMetal Déplier sans assistance
   MenuLocation: SheetMetal , Déplier sans assistance
   Workbenches: SheetMetal_Workbench/fr
   Shortcut: **U**
   SeeAlso: SheetMetal_Unfold/fr
---

# SheetMetal UnattendedUnfold/fr



## Description

La commande <img alt="" src=images/SheetMetal_UnattendedUnfold.svg  style="width:24px;"> [Déplier sans assistance](SheetMetal_UnattendedUnfold/fr.md) déplie un objet en tôle.

Cette commande n\'est pas disponible par défaut, voir [Remarques](#Remarques.md).

Si le corps parent d\'une face planaire sélectionnée a déjà fait l\'objet d\'un dépliage, cet outil ignorera le menu du panneau des tâches. Sinon, il affichera un message d\'erreur demandant soit de \"définir un facteur K manuel\", soit d\'\"utiliser une feuille de définition de matériau\".

Avec l\'outil <img alt="" src=images/SheetMetal_Unfold.svg  style="width:16px;"> [Déplier](SheetMetal_Unfold/fr.md), l\'étiquette du corps parent reçoit un suffixe (tel que *\_material_0.5din*), après cela, il est prêt à être utilisé avec cet outil.



## Utilisation

1.  Sélectionnez une face plane d\'une pièce de tôle.
2.  Il y a plusieurs façons de lancer la commande :
    -   Appuyez sur le bouton **<img src="images/SheetMetal_UnattendedUnfold.svg_" width=16px> [Déplier sans assistance](SheetMetal_UnattendedUnfold/fr.md)**.
    -   Sélectionnez l\'option **SheetMetal → <img src="images/SheetMetal_UnattendedUnfold.svg" width=16px> [Déplier sans assistance](SheetMetal_UnattendedUnfold/fr.md)** du menu.
    -   Cliquez avec le bouton droit de la souris dans la [vue en arborescence](Tree_view/fr.md) ou la [vue 3D](3D_view/fr.md) et sélectionnez l\'option **SheetMetal → <img src="images/SheetMetal_UnattendedUnfold.svg" width=16px> Déplier sans assistance** dans le menu contextuel.
    -   Utilisez le raccourci clavier : **U**.
3.  Un objet **Unfold** sera créé.
4.  Vous pouvez ajuster les paramètres dans l\'[éditeur de propriétés](Property_editor/fr.md).



## Remarques

Pour rendre cette commande disponible, activez d\'abord le mode ingénierie dans les préférences. Allez dans **Édition → Préférences → SheetMetal → Paramètres généraux** et réglez **Mode expérimenté** sur {{Value|Activer}}. La modification de cette préférence nécessite un redémarrage de FreeCAD.



## Propriétés

Voir aussi: [Éditeur de propriétés](Property_editor/fr.md)

Un objet SheetMetal Unfold est dérivé d\'un objet [Part Feature](Part_Feature/fr.md) et hérite de toutes ses propriétés. Il n\'a pas de propriétés supplémentaires.

## Limitations

Voir <img alt="" src=images/SheetMetal_Unfold.svg  style="width:16px;"> [Déplier](SheetMetal_Unfold/fr.md) pour les limitations.



---
⏵ [documentation index](../README.md) > [SheetMetal](Category_SheetMetal.md) > [Addons](Category_Addons.md) > [External Command Reference](Category_External%20Command%20Reference.md) > SheetMetal UnattendedUnfold/fr
