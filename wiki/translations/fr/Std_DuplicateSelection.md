---
- GuiCommand:/fr
   Name:Std DuplicateSelection
   Name/fr:Std Dupliquer la Sélection
   MenuLocation:Édition → Dupliquer la sélection
   Workbenches:tous
   SeeAlso:[Std Copier](Std_Copy/fr.md), [Std Coller](Std_Paste/fr.md)
---

# Std DuplicateSelection/fr

## Description

La commande **Std Dupliquer la sélection** duplique les objets dans le document actif.



## Utilisation

1.  Sélectionnez un ou plusieurs objets.
2.  Sélectionnez l\'option **Édition → Dupliquer la sélection** dans le menu.
3.  Si les objets ont des dépendances qui n\'ont pas été sélectionnées, une boîte de dialogue vous demandera de spécifier ceux qui doivent être inclus.



## Remarques

-   FreeCAD changera automatiquement les noms internes et, selon les préférences, les étiquettes des objets pour éviter les conflits de noms.



## Préférences

-   Les étiquettes en double sont autorisées si **Outils → Éditer les paramètres... → BaseApp → Preferences → Document → DuplicateLabels** est défini sur `True`. Ce paramètre peut également être modifié dans l\'[Éditeur de préférences](Preferences_Editor/fr#Document.md).





{{Std Base navi

}}



---
![](images/Button_right.svg) [documentation index](../README.md) > Std DuplicateSelection/fr
