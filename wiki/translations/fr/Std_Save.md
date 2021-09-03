---
- GuiCommand:/fr
   Name:Std Save
   Name/fr:Std Enregistrer
   MenuLocation:Fichier → Enregistrer
   Workbenches:Tous
   Shortcut:**Ctrl**+**S**
   SeeAlso:[Std Enregistrer sous](Std_SaveAs/fr.md), [Std Enregistrer une copie](Std_SaveCopy.md), [Std Tout enregistrer](Std_SaveAll.md)
---

## Description

La commande **Std Enregistrer** enregistre le document actif.

## Utilisation

1.  Il existe plusieurs façons d\'appeler la commande:
    -   Appuyez sur le bouton **<img src="images/Std_Save.svg" width=16px> [Std Enregistrer](Std_Save.md)**.
    -   Sélectionnez l\'option **File → <img src="images/Std_Save.svg" width=16px> Enregistrer** dans le menu.
    -   Utilisez le raccourci clavier: **Ctrl**+**S**.
2.  Pour les nouveaux documents: saisissez un nom de fichier dans la boîte de dialogue et appuyez sur le bouton **Enregistrer**.

## Options

-   Appuyez sur **Echap** ou sur le bouton **Annuler** pour annuler la commande.

## Remarques

-   Cette commande peut également être utilisée pour enregistrer des graphiques de dépendance. Voir [Std Graphique de dépendance](Std_DependencyGraph/fr.md).

## Préférences

-   Le dernier emplacement de fichier utilisé est stocké: **Outils → Editer les paramètres... → BaseApp → Preferences → General → FileOpenSavePath**.

## Script


**Voir aussi:**

[FreeCAD Script de base](FreeCAD_Scripting_Basics/fr.md).

Pour enregistrer un document, utilisez la méthode `save` de l\'objet document. Un nouveau document doit d\'abord être enregistré avec la méthode `saveAs` de l\'objet document. Pour un exemple de script, voir [Std Nouveau](Std_New/fr.md).





{{Std Base navi

}}  
