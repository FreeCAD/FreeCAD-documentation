---
- GuiCommand:/fr
   Name:Std Open
   Name/fr:Std Ouvrir
   MenuLocation:Fichier → Ouvrir...
   Workbenches:Tous
   Shortcut:**Ctrl**+**O**
   SeeAlso:[Std Importer](Std_Import/fr.md), [Std Nouveau](Std_New/fr.md)
---

## Description

La commande **Std Ouvrir** ouvre un fichier. Si le fichier n\'est pas un fichier FreeCAD natif (\*.FCStd), sa géométrie sera importée dans un nouveau document. Voir [Std Importer](Std_Import/fr.md) pour plus d\'informations.

## Utilisation

1.  Il existe plusieurs façons d\'appeler la commande:
    -   Appuyez sur le bouton **<img src="images/Std_Open.svg" width=16px> [Std Ouvrir](Std_Open/fr.md)**.
    -   Sélectionnez l\'option **Fichier → <img src="images/Std_Open.svg" width=16px> Ouvrir...** dans le menu.
    -   Utilisez le raccourci clavier: **Ctrl**+**O**.
2.  Sélectionnez éventuellement le format de fichier correct dans la boîte de dialogue.
3.  Sélectionner un fichier.
4.  Appuyez sur le bouton **Ouvrir**.

## Options

-   Appuyez sur **Echap** ou sur le bouton **Annuler** pour annuler la commande.

## Préférences

-   Le dernier emplacement de fichier utilisé est stocké: **Outils → Editer les paramètres... → BaseApp → Preferences → General → FileOpenSavePath**.

## Script


**Voir aussi:**

[FreeCAD Script de base](FreeCAD_Scripting_Basics/fr.md).

Pour ouvrir un document, utilisez la méthode `open(filepath)` ou la méthode `openDocument(filepath, [hidden<nowiki>=</nowiki>False])` de l\'application FreeCAD.

Ces méthodes créent et renvoient un document et y chargent un fichier projet. L\'argument `filepath` doit être une chaîne pointant vers un fichier existant. Si le fichier n\'existe pas ou si le fichier ne peut pas être chargé, une exception I/O est levée. Dans ce cas, le document créé est conservé, mais sera vide. Si `hidden<nowiki>=</nowiki>True` est utilisé, le document ne sera pas affiché dans l\'interface graphique et aucun onglet n\'apparaîtra pour lui. Cela permet d\'effectuer des opérations automatiques sur un document et de le fermer sans perturber l\'interface utilisateur.

Pour un exemple de script, voir [Std Nouveau](Std_New/fr#Script.md).





{{Std Base navi

}}  
