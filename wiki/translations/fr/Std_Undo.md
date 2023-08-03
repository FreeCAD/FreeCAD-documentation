---
 GuiCommand:
   Name: Std Undo
   Name/fr: Std Annuler
   MenuLocation: Édition , Annuler
   Workbenches: Tous
   Shortcut: **Ctrl**+**Z**
   SeeAlso: Std_Redo/fr
---

# Std Undo/fr

## Description

La commande **Std Annuler** annule la dernière action.



## Utilisation

1.  Il existe plusieurs façons d\'appeler la commande :
    -   Appuyez sur le bouton **<img src="images/Std_Undo.svg" width=16px> [Std  Annuler](Std_Undo/fr.md)**.
    -   Sélectionnez l\'option **Édition → <img src="images/Std_Undo.svg" width=16px> Annuler** dans le menu.
    -   Utilisez le raccourci clavier : **Ctrl**+**Z**.

## Options

-   Pour annuler plusieurs actions, cliquez sur la petite flèche noire vers le bas à droite du bouton **<img src="images/Std_Undo.svg" width=16px> [Std Annuler](Std_Undo/fr.md)** et sélectionnez dans la liste.



## Préférences

-   La fonctionnalité Annuler/Rétablir peut être désactivée en définissant **Outils → Éditer les paramètres... → BaseApp → Preferences → Document → UsingUndo** sur `False`, mais ce n\'est pas recommandé. Ce paramètre peut également être modifié dans l\'[Éditeur de préférences](Preferences_Editor/fr#Document.md).
-   Le nombre maximum d\'étapes Annuler / Rétablir est contrôlé par **Outils → Éditer les paramètres... → BaseApp → Preferences → Document → MaxUndoSize**. Ce paramètre peut également être modifié dans l\'[Éditeur de préférences](Preferences_Editor/fr#Document.md).



## Script


**Voir aussi :**

[FreeCAD Script de base](FreeCAD_Scripting_Basics/fr.md).

Pour annuler la dernière action, utilisez la méthode `undo` de l\'objet document.


```python
import FreeCAD

FreeCAD.ActiveDocument.undo()
```

Lorsque vous exécutez FreeCAD en mode console pure (CLI), le mécanisme d\'annulation/rétablissement n\'est pas activé par défaut. Il doit être explicitement activé pour chaque document.


```python
import FreeCAD

FreeCAD.ActiveDocument.UndoMode = 1
```





{{Std Base navi

}}



---
⏵ [documentation index](../README.md) > Std Undo/fr
