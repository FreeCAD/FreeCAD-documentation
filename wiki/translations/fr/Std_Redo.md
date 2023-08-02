---
- GuiCommand:
   Name: Std Redo
   Name/fr: Std Rétablir
   MenuLocation: Édition -> Rétablir
   Workbenches: Tous
   Shortcut: **Ctrl**+**Y**
   SeeAlso: Std_Undo/fr
---

# Std Redo/fr

## Description

La commande **Std Rétablir** inverse l\'action de la commande [Std Annuler](Std_Undo/fr.md).



## Utilisation

1.  Il existe plusieurs façons d\'appeler la commande :
    -   Appuyez sur le bouton **<img src="images/Std_Redo.svg" width=16px> [Rétablir](Std_Redo/fr.md)**.
    -   Sélectionnez l\'option **Édition → <img src="images/Std_Redo.svg" width=16px> Rétablir** dans le menu.
    -   Utilisez le raccourci clavier : **Ctrl**+**Y**.

## Options

-   Pour Rétablir plusieurs actions, cliquez sur la flèche noire vers le bas à droite du bouton **<img src="images/Std_Redo.svg" width=16px> [Std Rétablir](Std_Redo.md)** et sélectionnez dans la liste.



## Préférences

-   La fonctionnalité Annuler/Rétablir peut être désactivée en définissant **Outils → Éditer les paramètres... → BaseApp → Preferences → Document → UsingUndo** sur `False`, mais ce n\'est pas recommandé. Ce paramètre peut également être modifié dans l\'[Editeur de préférences](Preferences_Editor/fr#Document.md).
-   Le nombre maximum d\'étapes Annuler / Rétablir est contrôlé par **Outils → Éditer les paramètres... → BaseApp → Preferences → Document → MaxUndoSize**. Ce paramètre peut également être modifié dans l\'[Éditeur de préférences](Preferences_Editor/fr#Document.md).



## Script


**Voir aussi :**

[FreeCAD Script de base](FreeCAD_Scripting_Basics/fr.md).

Pour Rétablir une action qui vient d\'être annulée, utilisez la méthode `redo` de l\'objet document.


```python
import FreeCAD

FreeCAD.ActiveDocument.redo()
```





{{Std Base navi

}}



---
⏵ [documentation index](../README.md) > Std Redo/fr
