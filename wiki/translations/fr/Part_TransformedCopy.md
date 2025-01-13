---
 GuiCommand:
   Name: Part TransformedCopy
   Name/fr: Part Copie transformée
   MenuLocation: Part , Créer une copie , Copie transformée
   Workbenches: Part_Workbench/fr
   Version: 0.19
   SeeAlso: Part_SimpleCopy/fr
---

# Part TransformedCopy/fr



## Description

La commande <img alt="" src=images/Part_TransformedCopy.svg  style="width:24px;"> **Part Copie transformée** crée des copies non paramétriques d\'objets. Elle est destinée aux objets imbriqués dans des conteneurs.

Les **Placement** des copies sont ajustées, en tenant compte de l\'emplacement du ou des conteneurs, de manière à ce que leur position et leur rotation par rapport au système de coordonnées global soient identiques à celles des objets d\'origine. Si les objets sélectionnés ne sont pas imbriqués, ou s\'ils sont imbriqués dans un conteneur avec un placement par défaut, cette commande produit les mêmes résultats que [Part Copie simple](Part_SimpleCopy/fr.md).



## Utilisation

1.  Sélectionnez un ou plusieurs objets.
2.  Sélectionnez l\'option **Part → Créer une copie → <img src="images/Part_TransformedCopy.svg" width=16px> Copie transformée** du menu.



## Propriétés

Voir aussi : [Éditeur de propriétés](Property_editor/fr.md)

Les objets créés sont des objets [Part Feature](Part_Feature/fr.md) sans propriétés supplémentaires.





{{Part_Tools_navi

}}



---
⏵ [documentation index](../README.md) > [Part](Part_Workbench.md) > Part TransformedCopy/fr
