---
- GuiCommand:
   Name:SheetMetal UnattendedUnfold
   Name/fr:SheetMetal Déplier sans assistance
   MenuLocation:SheetMetal - Unattended Unfold
   Workbenches:[SheetMetal](SheetMetal_Workbench/fr.md)
   Shortcut:**U**
   SeeAlso:[SheetMetal Déplier](SheetMetal_Unfold/fr.md)
---

# SheetMetal UnattendedUnfold/fr

## Description

La commande <img alt="" src=images/SheetMetal_UnattendedUnfold.svg  style="width:24px;"> [Unattended Unfold](SheetMetal_UnattendedUnfold/fr.md) déplie un objet en tôle.

Si le corps parent d\'une face planaire sélectionnée a déjà fait l\'objet d\'un dépliage, cet outil ignorera le menu du panneau des tâches. Sinon, il affichera un message d\'erreur demandant soit de \"définir un facteur K manuel\", soit d\'\"utiliser une feuille de définition de matériau\".

Avec la première utilisation de l\'outil <img alt="" src=images/SheetMetal_Unfold.svg  style="width:16px;"> [Déplier](SheetMetal_Unfold/fr.md), l\'étiquette du corps parent reçoit un suffixe (tel que *\_material_0.5din*), après cela, il est prêt à être utilisé avec cet outil.

## Utilisation

1.  Sélectionnez une face plane d\'une pièce de tôle.
2.  Activez la commande <img alt="" src=images/SheetMetal_UnattendedUnfold.svg  style="width:16px;"> [UnattendedUnfold](SheetMetal_UnattendedUnfold/fr.md) en utilisant l\'une des commandes suivantes :
    -   Le bouton **<img src="images/_SheetMetal_UnattendedUnfold.svg_" width=16px> [Unattended Unfold](SheetMetal_UnattendedUnfold/fr.md)
**
    -   Le bouton **SheetMetal → <img src="images/SheetMetal_UnattendedUnfold.svg" width=16px> [Unattended Unfold](SheetMetal_UnattendedUnfold/fr.md)** du menu.
    -   Le raccourci clavier : **U**

## Propriétés

Voir aussi: [Éditeur de propriétés](Property_editor/fr.md)

Un objet SheetMetal Unfold est dérivé d\'un objet [Part Feature](Part_Feature/fr.md) et hérite de toutes ses propriétés. Il n\'a pas de propriétés supplémentaires mais son étiquette a une valeur par défaut :

### Données


{{Properties_Title|Base}}

-    **Label|String**: Valeur par défaut : Le nom modifiable par l\'utilisateur de cet objet, il peut être toute chaîne UTF8 arbitraire.

## Limitations

Voir <img alt="" src=images/SheetMetal_Unfold.svg  style="width:16px;"> [Déplier](SheetMetal_Unfold/fr.md) pour les limitations.



---
![](images/Button_right.svg) [documentation index](../README.md) > [SheetMetal](Category_SheetMetal.md) > [Addons](Category_Addons.md) > [External Command Reference](Category_External Command Reference.md) > SheetMetal UnattendedUnfold/fr
