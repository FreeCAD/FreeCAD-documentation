---
- GuiCommand:/fr
   Name:Std Copy
   Name/fr:Std Copier
   MenuLocation:Édition → Copier
   Workbenches:Tous
   Shortcut:**Ctrl**+**C**
   SeeAlso:[Std Couper](Std_Cut/fr.md), [Std Coller](Std_Paste/fr.md), [Std Dupliquer la sélection](Std_DuplicateSelection/fr.md)
---

## Description

La commande **Std Copie** copie les objets dans le presse-papiers.

## Utilisation

1.  Sélectionnez un ou plusieurs objets.
2.  Il existe plusieurs façons d\'appeler la commande:
    -   Appuyez sur le bouton **<img src="images/Std_Copy.svg" width=16px> [Opération de copie](Std_Copy/fr.md)**.
    -   Sélectionnez l\'option **Edition → <img src="images/Std_Copy.svg" width=16px> Copier** dans le menu.
    -   Sélectionnez l\'option **<img src="images/Std_Copy.svg" width=16px> Copier** dans le menu contextuel de la [Vue en arborescence](Tree_view/fr.md).
    -   Utilisez le raccourci clavier: **Ctrl**+**C**.
3.  Si les objets ont des dépendances qui n\'ont pas été sélectionnées, une boîte de dialogue vous demandera de spécifier ceux qui doivent être inclus.

## Remarques

-   Lorsque vous travaillez dans une fenêtre de texte FreeCAD, une zone de saisie ou une feuille de calcul, le raccourci clavier standard **Ctrl**+**C**, dans presque tous les cas, ne lance pas la commande *\' Std Copier*\'mais utilise à la place la fonction Copy du système d\'exploitation.
-   Il n\'est pas possible de copier-coller des objets natifs entre FreeCAD et d\'autres applications.

## Script

La commande **Std Copie** peut être appliquée après avoir sélectionné un ou plusieurs objets dans la [Vue en arborescence](Tree_view/fr.md):


```python
FreeCADGui.runCommand('Std_Copy')
FreeCADGui.runCommand('Std_Paste')
```

La sélection peut être manuelle (en utilisant la souris) ou via la [Console Python](Python_console/fr.md).
Pour en savoir plus sur la sélection d\'objets de manière programmatique, reportez-vous à [Méthodes de sélection](Selection_methods/fr.md).





{{Std Base navi

}}  
