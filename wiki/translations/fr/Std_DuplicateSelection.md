---
- GuiCommand:/fr
   Name:Std DuplicateSelection
   Name/fr:Std Dupliquer la Sélection
   MenuLocation:Edition → Dupliquer la sélection
   Workbenches:tous
   SeeAlso:[Std Copier](Std_Copy/fr.md), [Std Coller](Std_Paste/fr.md)
---

## Description

La commande **Std Dupliquer la sélection** duplique les objets dans le document actif.

## Utilisation

1.  Sélectionnez un ou plusieurs objets.
2.  Sélectionnez l\'option **Edition → Dupliquer la sélection** dans le menu.
3.  Si les objets ont des dépendances qui n\'ont pas été sélectionnées, une boîte de dialogue vous demandera de spécifier ceux qui doivent être inclus.

## Remarques

-   FreeCAD changera automatiquement les noms internes et, selon les préférences, les étiquettes des objets pour éviter les conflits de noms.

## Préférences

-   Les étiquettes en double sont autorisées si **Outils → Editer les paramètres... → BaseApp → Preferences → Document → DuplicateLabels** est défini sur `True`. Ce paramètre peut également être modifié dans l\'[Editeur de préférences](Preferences_Editor/fr#Document.md).

## Script

La commande **Std Dupliquer la sélection** peut être appliquée après avoir sélectionné un ou plusieurs objets dans la [Vue en arborescence](Tree_view/fr.md):


```python
FreeCADGui.runCommand('Std_DuplicateSelection')
```

La sélection peut être manuelle (en utilisant la souris) ou via la [Console Python](Python_console/fr.md).
Pour en savoir plus sur la sélection d\'objets de manière programmatique, reportez-vous à [Méthodes de sélection](Selection_methods/fr.md).





{{Std Base navi

}}  
