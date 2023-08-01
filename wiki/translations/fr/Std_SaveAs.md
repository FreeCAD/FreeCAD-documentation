---
- GuiCommand:
   Name: Std SaveAs
   Name/fr: Std Enregistrer sous
   MenuLocation: Fichier - Enregistrer sous...
   Workbenches: Tous
   SeeAlso: [Std Enregistrer une copie](Std_SaveCopy.md), [Std Enregistrer](Std_Save/fr.md)
---

# Std SaveAs/fr

## Description

La commande **Std Enregistrer sous** enregistre le document actif sous un nouveau nom de fichier.



## Utilisation

1.  Sélectionnez l\'option **Fichier → <img src="images/Std_SaveAs.svg" width=16px> Enregistrer sous...** dans le menu.
2.  Entrez un nom de fichier dans la boîte de dialogue.
3.  Appuyez sur le bouton **Enregistrer**.

## Options

-   Appuyez sur **Echap** ou sur le bouton **Annuler** pour annuler la commande.



## Remarques

-   Cette commande peut également être utilisée pour enregistrer des graphiques de dépendance. Voir [Std Graphique de dépendance](Std_DependencyGraph/fr.md).



## Préférences

-   Le dernier emplacement de fichier utilisé est stocké: **Outils → Éditer les paramètres... → BaseApp → Preferences → General → FileOpenSavePath**.



## Script


**Voir aussi :**

[FreeCAD Script de base](FreeCAD_Scripting_Basics/fr.md).

Pour enregistrer un document sous un nouveau nom, utilisez la méthode `saveAs` de l\'objet document. Pour un exemple de script, voir [Std Nouveau](Std_New/fr.md).





{{Std Base navi

}}



---
⏵ [documentation index](../README.md) > Std SaveAs/fr
