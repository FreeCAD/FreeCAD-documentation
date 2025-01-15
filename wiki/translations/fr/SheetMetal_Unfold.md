---
 GuiCommand:
   Name: SheetMetal Unfold
   Name/fr: SheetMetal Déplier
   MenuLocation: SheetMetal , Déplier
   Workbenches: SheetMetal_Workbench/fr
   Shortcut: **U**
   SeeAlso: SheetMetal_UnattendedUnfold/fr
---

# SheetMetal Unfold/fr

## Description

La commande <img alt="" src=images/SheetMetal_Unfold.svg  style="width:24px;"> **SheetMetal Déplier** permet de déplier une tôle.



## Utilisation

1.  Sélectionnez une face plane de tôle.
2.  Il y a plusieurs façons de lancer la commande :
    -   Appuyez sur le bouton **<img src="images/_SheetMetal_Unfold.svg_" width=16px> [Déplier](SheetMetal_Unfold/fr.md)**.
    -   Sélectionnez l\'option **SheetMetal → <img src="images/SheetMetal_Unfold.svg" width=16px> [Déplier](SheetMetal_Unfold/fr.md)** du menu.
    -   Cliquez avec le bouton droit de la souris dans la [vue en arborescence](Tree_view/fr.md) ou la [vue 3D](3D_view/fr.md) et sélectionnez l\'option **SheetMetal → <img src="images/SheetMetal_Unfold.svg" width=16px> [Déplier](SheetMetal_Unfold/fr.md)** dans le menu contextuel.
    -   Utilisez le raccourci clavier : **U**.
3.  Le [panneau des tâches](Task_panel/fr.md) *Déplier l\'objet en tôle* s\'ouvre.
4.  Ajustez les options de dépliage dans le [panneau des tâches](Task_panel/fr.md) :
    -   Vous pouvez activer les options de projection de l\'esquisse de dépliage et définir les couleurs.
    -   Vous pouvez activer l\'option d\'exportation.
    -   Si vous n\'utilisez pas de **Fiche de définition du matériau** (voir [Remarques](#Remarques.md)) :
        1.  Réglez l\'option **Fiche de définition du matériau** sur {{Value|Facteur K manuel}}.
        2.  Vous pouvez activer les boutons radio ANSI ou DIN (voir [Remarques](#Remarques.md)).
        3.  Ajustez la valeur du facteur K manuel (voir [Remarques](#Remarques.md)).
    -   Vous pouvez activer la transparence de l\'objet déplié.
5.  Appuyez sur le bouton **OK** pour terminer la commande et fermer le panneau des tâches.
6.  Un objet **Unfold** sera créé.
7.  Vous pouvez ajuster les paramètres dans l\'[éditeur de propriétés](Property_editor/fr.md).



## Remarques

-   Voir les sections [Material Definition Sheet](https://github.com/shaise/FreeCAD_SheetMetal#material-definition-sheet) et [K-factor](https://github.com/shaise/FreeCAD_SheetMetal#physical-material-definitions) de la page du projet pour plus d\'informations.
-   Pour une explication des différentes plages de valeurs des facteurs K ISO et ANSI, voir le tableau sur la page [this](https://de.wikipedia.org/wiki/Biegeverkürzung#Korrektur_durch_den_sog._k-Faktor) (en allemand).



## Propriétés

Voir aussi : [Éditeur de propriétés](Property_editor/fr.md)

Un objet SheetMetal Unfold est dérivé d\'un objet [Part Feature](Part_Feature/fr.md) et hérite de toutes ses propriétés. Il n\'a pas de propriétés supplémentaires.



## Limites

-   La tôle doit avoir une épaisseur constante.
-   Les faces planes ne doivent pas contenir de lignes de séparation.
-   Les faces planes doivent être réellement planes et non des approximations de B-splines.
-   Les faces des angles de pliage doivent être réellement cylindriques et non des approximations de B-splines.
-   Versions antérieures à 0.5.00 : la fonction de dépliage Unfold n\'est pas paramétrique. Si le modèle est modifié, vous devez le déplier à nouveau.



---
⏵ [documentation index](../README.md) > [SheetMetal](Category_SheetMetal.md) > [Addons](Category_Addons.md) > [External Command Reference](Category_External%20Command%20Reference.md) > SheetMetal Unfold/fr
