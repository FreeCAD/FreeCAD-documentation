---
- GuiCommand:/fr
   Name:Std Export
   Name/fr:Std Exporter
   MenuLocation:Fichier → Exporter...
   Workbenches:Tous
   Shortcut:**Ctrl**+**E**
   SeeAlso:[Std Générer un pdf](Std_PrintPdf/fr.md), [Std Importer](Std_Import/fr.md), [Préférences d'Import Export](Import_Export_Preferences/fr.md)
---

## Description

La commande **Std Exporter** exporte les objets sélectionnés vers un format de fichier différent. De nombreux formats de fichiers sont pris en charge et pour certains formats, plusieurs options d\'exportation existent. Voir [Import Export](Import_Export/fr.md) pour plus d\'informations.

## Utilisation

1.  Sélectionnez un ou plusieurs objets. Pour éviter d\'exporter des objets invisibles ou en double:
    -   Soyez prudent lorsque vous utilisez **Ctrl**+**A** pour sélectionner tous les objets. Cela sélectionnera également des objets invisibles.
    -   Sélectionnez un [PartDesign Corps](PartDesign_Body/fr.md) en sélectionnant uniquement le corps lui-même ou sa dernière fonction.
    -   Sélectionnez un [Std Group](Std_Group/fr.md) ou un [Std Part](Std_Part/fr.md) en sélectionnant uniquement l\'objet parent lui-même ou les objets imbriqués à l\'intérieur.
    -   N\'utilisez pas la commande [Std Tout sélectionner](Std_SelectAll/fr.md) car elle sélectionnera également les sous-éléments des Corps PartDesign.
    -   Pour la même raison, la commande [Std Sélection par boîte](Std_BoxSelection/fr.md) doit être évitée dans FreeCAD version 0.18 et antérieure.
2.  Il existe plusieurs façons d\'appeler la commande:
    -   Sélectionnez l\'option {{MenuCommand|Fichier → <img src="images/Std_Export.svg" width=16px> Exporter...}} dans le menu.
    -   Utilisez le raccourci clavier: **Ctrl**+**E**..
3.  Sélectionnez le format de fichier correct dans la boîte de dialogue.
4.  Entrez un nom de fichier.
5.  Appuyez sur le bouton **Enregistrer**.

## Options

-   Appuyez sur **Echap** ou sur le bouton **Annuler** pour annuler la commande.

## Remarques

-   Pour exporter un [objet maillé](Mesh_Workbench/fr.md) dans un format de fichier solide, il doit d\'abord être converti. Voir le tutoriel [Importer depuis STL ou OBJ](Import_from_STL_or_OBJ/fr.md).
-   Certains ateliers ont des commandes d\'exportation supplémentaires. Voir: [Import Export](Import_Export/fr.md).

## Préférences

-   Voir: [Préférences Import Export](Import_Export_Preferences/fr.md).
-   Le dernier emplacement de fichier utilisé est stocké: {{MenuCommand|Outils → Editer les paramètres... → BaseApp → Preferences → General → FileOpenSavePath}}.
-   Le dernier filtre d\'exportation utilisé est stocké: {{MenuCommand|Outils → Editer les paramètres... → BaseApp → Preferences → General → FileExportFilter}}.





{{Std Base navi

}}  

[Category:File\_Formats{{\#translation:}}](Category:File_Formats.md)
