---
 GuiCommand:
   Name: Std CloseActiveWindow
   Name/fr: Std Fermer
   MenuLocation: Fichier , Fermer
   Workbenches: Tous
   Shortcut: **Ctrl**+**W**
   SeeAlso: Std_CloseAllWindows/fr
---

# Std CloseActiveWindow/fr

## Description

La commande *\'Std Fermer*\' ferme la fenêtre active. Pour fermer un document, toutes ses fenêtres doivent être fermées.



## Utilisation

1.  Il existe plusieurs façons d\'appeler la commande:
    -   Sélectionnez l\'option **Fichier → <img src="images/Std_CloseActiveWindow.svg" width=16px> Fermer** dans le menu.
    -   Utilisez le raccourci clavier: **Ctrl**+**W**.
2.  Pour fermer un document: répétez cette opération pour toutes les fenêtres qui lui appartiennent.
3.  Lors de la fermeture de la dernière fenêtre d\'un document non enregistré, une boîte de dialogue vous invite à l\'enregistrer:
    -   Appuyez sur le bouton **Enregistre le document actif** pour enregistrer le document. Si nécessaire, entrez d\'abord un nom de fichier.
    -   Appuyez sur le bouton **Abandonner** pour supprimer le document et perdre toutes les modifications.

## Options

-   Lorsque la boîte de dialogue s\'affiche: appuyez sur **Echap** ou sur le bouton **Annuler** pour abandonner la commande.



## Remarques

-   La commande ne peut fermer que les fenêtres [ancrées](Std_ViewDockUndockFullscreen/fr.md).
-   Un document peut également être fermé en cliquant dessus avec le bouton droit de la souris dans la [vue en arborescence](Tree_view/fr.md) et en sélectionnant **Fermer le document** dans le menu contextuel.



## Préférences

-   Le dernier emplacement de fichier utilisé est stocké: **Outils → Editer les paramètres... → BaseApp → Preferences → General → FileOpenSavePath**.



## Script


**Voir aussi:**

[FreeCAD Script de base](FreeCAD_Scripting_Basics/fr.md).

Pour fermer un document, utilisez la méthode `closeDocument` de l\'application FreeCAD. Pour un exemple de script, voir [ Std Nouveau](Std_New/fr.md).





{{Std Base navi

}}



---
⏵ [documentation index](../README.md) > Std CloseActiveWindow/fr
