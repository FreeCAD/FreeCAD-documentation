---
- GuiCommand:/fr
   Name:Std_Edit
   Name/fr:Std Édition
   MenuLocation:Édition → Basculer le mode d'édition
   Workbenches:Tous
   SeeAlso:[Std Edition arborescence](Std_UserEditMode/fr.md)
---

# Std Edit/fr

## Description

La commande **Std Édition** active ou désactive le mode d\'édition d\'un objet.

## Utilisation

1.  Si aucun objet n\'est en mode édition : sélectionnez un seul objet.
2.  Sélectionnez l\'option **Édition → <img src="images/Std_Edit.svg" width=16px> Basculer le mode d'édition** dans le menu.
3.  Le mode d\'édition de l\'objet sélectionné est activé ou le mode d\'édition existant est désactivé.

## Remarques

-   Certains outils seront désactivés (grisés) dans l\'interface utilisateur lorsque le mode d\'édition d\'un objet est actif.
-   Tous les types d\'objets n\'ont pas de mode d\'édition.
-   La fonctionnalité disponible en mode édition dépend du type d\'objet.
-   Le mode édition peut également être activé en double-cliquant sur un objet dans la [Vue en arborescence](Tree_view/fr.md).

## Script


**Voir aussi :**

[FreeCAD Script de base](FreeCAD_Scripting_Basics/fr.md).

Pour activer le mode d\'édition d\'un objet, utilisez la méthode `setEdit` de l\'objet document. Cette méthode n\'est pas disponible si FreeCAD est en mode console.


```python
import FreeCADGui

FreeCADGui.ActiveDocument.setEdit("myObjectName",0)
```

Le deuxième argument est l\'EditMode. Les options suivantes sont disponibles :


```python
enum EditMode {Default = 0,
               Transform,
               Cutting,
               Color,
};
```

Pour désactiver le mode d\'édition d\'un objet, utilisez la méthode `resetEdit` de l\'objet document.


```python
import FreeCADGui

FreeCADGui.ActiveDocument.resetEdit()
```





{{Std Base navi

}}

---
[documentation index](../README.md) > Std Edit/fr
