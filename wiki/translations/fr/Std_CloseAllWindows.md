---
- GuiCommand:
   Name: Std CloseAllWindows
   Name/fr: Std Fermer tout
   MenuLocation: Fichier -> Fermer tout
   Workbenches: Tous
   SeeAlso: Std_CloseActiveWindow/fr
---

# Std CloseAllWindows/fr

## Description

La commande **Std Fermer tout** ferme toutes les fenêtres, fermant ainsi tous les documents.



## Utilisation

1.  Sélectionnez l\'option **Fichier  → <img src="images/Std_CloseAllWindows.svg" width=16px> Fermer tout** dans le menu.
2.  S\'il y a des documents non enregistrés, une boîte de dialogue vous demandera de les enregistrer :
    -   Appuyez sur le bouton **Enregistrer** pour enregistrer le document actif. Si nécessaire, entrez d\'abord un nom de fichier.
    -   Appuyez sur le bouton **Supprimer** pour supprimer le document actif et perdre toutes les modifications.

## Options

-   Lorsque la boîte de dialogue s\'affiche: appuyez sur **Echap** ou sur le bouton **Annuler** pour abandonner la commande.
-   S\'il existe plusieurs documents non enregistrés: cochez la case {{CheckBox|TRUE|Appliquer la réponse à tous}} pour éviter d\'être invité à chaque fois pour chaque document non enregistré.



## Remarques

-   Un document peut également être fermé en cliquant dessus avec le bouton droit de la souris dans la [vue en arborescence](tree_view/fr.md) et en sélectionnant **Fermer le document** dans le menu contextuel.



## Préférences

-   Le dernier emplacement de fichier utilisé est stocké: **Outils → Éditer les paramètres... → BaseApp → Preferences → General → FileOpenSavePath**.



## Script


**Voir aussi :**

[FreeCAD Script de base](FreeCAD_Scripting_Basics/fr.md).

Pour fermer un document, utilisez la méthode `closeDocument` de l\'application FreeCAD. Pour un exemple de script, voir [Std Nouveau](Std_New/fr.md).





{{Std Base navi

}}



---
⏵ [documentation index](../README.md) > Std CloseAllWindows/fr
