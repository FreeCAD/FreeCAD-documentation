---
- GuiCommand:/fr
   Name:Std MergeProjects
   Name/fr:Std Fusion de projets
   MenuLocation:Fichier → Fusionner un projet...
   Workbenches:Tous
---

## Description

La commande **Std Fusion de projets** ajoute le contenu d\'un fichier FreeCAD dans le document actif.

## Utilisation

1.  Sélectionnez l\'option **Fichier → <img src="images/Std_MergeProjects.svg" width=16px> Fusionner un projet...** dans le menu.
2.  Sélectionnez un fichier FreeCAD dans la boîte de dialogue.
3.  Appuyez sur le bouton **Ouvrir**.

## Options

-   Appuyez sur **Echap** ou sur le bouton **Annuler** pour annuler la commande.

## Remarques

-   Un projet ne peut pas être fusionné avec lui-même, la sélection du fichier en cours n\'est pas autorisée.
-   FreeCAD changera automatiquement les noms internes et, selon les préférences, les étiquettes des objets pour éviter les conflits de noms.

## Préférences

-   Le dernier emplacement de fichier utilisé est stocké: **Outils → Edition des paramètres... → BaseApp → Preferences → General → FileOpenSavePath**.
-   Les étiquettes en double sont autorisées si **Outils → Edition des paramètres... → BaseApp → Preferences → Document → DuplicateLabels** est réglé sur `True`. Ce paramètre peut également être modifié dans [Editeur de préférences](Preferences_Editor/fr#Document.md).





{{Std Base navi

}}  
