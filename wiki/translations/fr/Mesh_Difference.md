---
- GuiCommand:/fr
   Name:Mesh Difference
   Name/fr:Mesh Différence
   MenuLocation:Maillages → Opération booléenne → Différence
   Workbenches:[Mesh](Mesh_Workbench/fr.md)
   SeeAlso:[Mesh Union](Mesh_Union/fr.md), [Mesh Intersection](Mesh_Intersection/fr.md)
---

# Mesh Difference/fr

## Description

La commande **Différence** crée un nouvel objet maillé non paramétrique, un [Mesh Feature](Mesh_Feature/fr.md), qui est la différence de deux objets maillé : un objet maillé est coupé de l\'autre.

[OpenSCAD](http://www.openscad.org/) doit être installé pour utiliser cette commande et le chemin d\'accès à son exécutable doit être défini dans les [Préférences d\'OpenSCAD](OpenSCAD_Preferences/fr.md).

![](images/Mesh_Difference_example.png ) 
*A gauche deux objets maillés, à droite l'objet maillé qui est la différence de ces objets si le cube est sélectionné comme objet principal*



## Utilisation

1.  Sélectionnez l\'objet maillé principal.
2.  Ajoutez l\'objet maillé que vous souhaitez couper de l\'objet principal à la sélection. Les objets maillés doivent se chevaucher.
3.  Il existe plusieurs façons de lancer la commande :
    -   Appuyez sur le bouton **<img src="images/Mesh_Difference.svg" width=16px> [Différence](Mesh_Difference/fr.md)
**
    -   Sélectionnez l\'option **Maillages → Opération booléenne → <img src="images/Mesh_Difference.svg" width=16px> Différence** du menu.



## Propriétés

Voir : [Mesh Feature](Mesh_Feature/fr.md).





{{Mesh Tools navi

}}



---
![](images/Right_arrow.png) [documentation index](../README.md) > [Mesh](Mesh_Workbench.md) > Mesh Difference/fr
