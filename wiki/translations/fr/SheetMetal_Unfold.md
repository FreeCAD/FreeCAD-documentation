---
- GuiCommand:/fr
   Name:SheetMetal Unfold
   Name/fr:SheetMetal Déplier
   MenuLocation:SheetMetal → Unfold
   Workbenches:[SheetMetal](SheetMetal_Workbench/fr.md)
   Shortcut:**U**
   SeeAlso:[Déplier sans assistance](SheetMetal_UnattendedUnfold/fr.md)
---

# SheetMetal Unfold/fr

## Description

La commande <img alt="" src=images/SheetMetal_Unfold.svg  style="width:24px;"> **SheetMetal Unfold** permet de déplier un objet en tôle.

## Utilisation

Pour déplier une pièce de tôlerie:

1.  Basculez vers <img alt="" src=images/Sheetmetal_workbench_icon.svg  style="width:22px;"> [atelier SheetMetal](SheetMetal_Workbench/fr.md).
2.  Sélectionnez une face plane de la pièce de tôlerie. **Remarque**: la face doit être un plan, l\'épaisseur doit être constante .
3.  Cliquez sur l\'outil <img alt="" src=images/SheetMetal_Unfold.svg  style="width:24px;"> **Unfold** pour afficher un menu dans le panneau des tâches pour gérer les options de dépliage.
4.  Sélectionnez les options de projection de la future esquisse aplatie
5.  Sélectionnez la règle de déduction des plis avec [Kfactor](https://github.com/shaise/FreeCAD_SheetMetal#terminology):
    -   Utilisez [Material Definition Sheet](https://github.com/shaise/FreeCAD_SheetMetal#material-definition-sheet)
    -   Ou sélectionnez un manuel [Kfactor](https://github.com/shaise/FreeCAD_SheetMetal#terminology) puis la norme ANSI ou DIN à appliquer.

## Propriétés

Voir aussi : [Éditeur de propriétés](Property_editor/fr.md)

Cet outil crée un objet Déplier et n\'a pas de représentation propre dans la [Vue en arborescence](Tree_view/fr.md) ou ailleurs et n\'a donc pas de propriétés.

L\'objet *Unfold*, quant à lui, est dérivé d\'un objet [Part Feature](Part_Feature/fr.md) et hérite de toutes ses propriétés. Il n\'a pas de propriétés supplémentaires mais son étiquette a une valeur par défaut :

### Données


{{Properties_Title|Base}}

-    {{PropertyData/fr|Label|String}}: Valeur par défaut : Le nom modifiable par l\'utilisateur de cet objet, il peut être toute chaîne UTF8 arbitraire.

## Limites

-   La tôle doit avoir une épaisseur constante , y compris dans les rayons
-   Les faces plates doivent être planes sans lignes de division.
-   Les angles de pliage doivent être des rayons avec des faces cylindriques.
-   La fonction de dépliage n\'est pas paramétrique pour le moment.




[Category:SheetMetal](Category:SheetMetal.md) [Category:Addons](Category:Addons.md) [Category:External Command Reference](Category:External_Command_Reference.md)

---
[documentation index](../README.md) > [SheetMetal](Category:SheetMetal.md) > SheetMetal Unfold/fr
