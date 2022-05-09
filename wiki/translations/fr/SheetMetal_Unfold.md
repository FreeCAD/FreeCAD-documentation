---
- GuiCommand   */fr
   Name   *SheetMetal Unfold
   Name/fr   *SheetMetal Déplier
   MenuLocation   *SheetMetal → Unfold
   Workbenches   *[SheetMetal](SheetMetal_Workbench/fr.md)
   Shortcut   ***U**
   SeeAlso   *[Déplier sans assistance](SheetMetal_UnattendedUnfold/fr.md)
---

# SheetMetal Unfold/fr

## Description

La commande <img alt="" src=images/SheetMetal_Unfold.svg  style="width   *24px;"> **SheetMetal Unfold** permet de déplier un objet en tôle.

## Utilisation

1.  Sélectionnez une face plane de la pièce de tôle.
2.  Activez la commande <img alt="" src=images/SheetMetal_Unfold.svg  style="width   *16px;"> [Déplier](SheetMetal_Unfold/fr.md) en utilisant l\'une des commandes suivantes    *
    -   Le bouton **<img src="images/_SheetMetal_Unfold.svg_" width=16px> [Unfold](SheetMetal_Unfold/fr.md)**.
    -   Le bouton **SheetMetal → <img src="images/SheetMetal_Unfold.svg" width=16px> [Unfold](SheetMetal_Unfold/fr.md)** du menu.
    -   Le raccourci clavier    * **U**.
3.  Ajuster les options de dépliage dans le [Panneau des tâches](Task_panel/fr.md) en    *
    -   Sélectionnant les options de projection de l\'esquisse de dépliage.
    -   Sélectionnant la méthode de déduction du pliage avec [Material Definition Sheet](https   *//github.com/shaise/FreeCAD_SheetMetal#material-definition-sheet)    *
        - Utilisez une [fiche de définition du matériau](https   *//github.com/shaise/FreeCAD_SheetMetal#material-definition-sheet).
        - Sélectionnez un [K-factor](https   *//github.com/shaise/FreeCAD_SheetMetal#terminology) manuel puis la norme [ANSI ou DIN](https   *//de.wikipedia.org/wiki/Biegeverkürzung#Korrektur_durch_den_sog._k-Faktor) à appliquer.

## Propriétés

Voir aussi    * [Éditeur de propriétés](Property_editor/fr.md)

Un objet SheetMetal Unfold est dérivé d\'un objet [Part Feature](Part_Feature/fr.md) et hérite de toutes ses propriétés. Il n\'a pas de propriétés supplémentaires mais son étiquette a une valeur par défaut    *

### Données


{{Properties_Title|Base}}

-    {{PropertyData/fr|Label|String}}   * Valeur par défaut    * Le nom modifiable par l\'utilisateur de cet objet, il peut être toute chaîne UTF8 arbitraire.

## Limites

-   La tôle doit avoir une épaisseur constante , y compris dans les rayons
-   Les faces plates doivent être planes sans lignes de division.
-   Les angles de pliage doivent être des rayons avec des faces cylindriques.
-   La fonction de dépliage n\'est pas paramétrique pour le moment.




[Category   *SheetMetal](Category_SheetMetal.md) [Category   *Addons](Category_Addons.md) [Category   *External Command Reference](Category_External_Command_Reference.md)



---
![](images/Right_arrow.png) [documentation index](../README.md) > [SheetMetal](Category_SheetMetal.md) > [Addons](Category_Addons.md) > [External Command Reference](Category_External Command Reference.md) > SheetMetal Unfold/fr
