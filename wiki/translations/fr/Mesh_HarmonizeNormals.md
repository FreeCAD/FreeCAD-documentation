---
- GuiCommand:
   Name:Mesh HarmonizeNormals
   Name/fr:Mesh Harmoniser les normales‎
   MenuLocation:Maillages → Harmoniser les normales‎
   Workbenches:[Mesh](Mesh_Workbench/fr.md)
   SeeAlso:[Mesh Inverser les normales](Mesh_FlipNormals/fr.md)
---

# Mesh HarmonizeNormals/fr

## Description

La commande **Harmoniser les normales‎** harmonise les normales des objets maillés.



## Utilisation

1.  Sélectionnez un ou plusieurs objets maillés.
2.  Il existe plusieurs façons de lancer la commande :
    -   Appuyez sur le bouton **<img src="images/Mesh_HarmonizeNormals.svg" width=16px> [Harmoniser les normales](Mesh_HarmonizeNormals/fr.md)
**
    -   Sélectionnez l\'option **Maillages → <img src="images/Mesh_HarmonizeNormals.svg" width=16px> Harmoniser les normales‎** du menu.



## Remarques

-   Cette commande peut produire un maillage avec des normales inversées. La commande [Mesh Inverser les normales](Mesh_FlipNormals/fr.md) peut être utilisée pour corriger cela.
-   Pour une indication claire de l\'orientation des faces des objets maillés, assurez-vous que la propriété **Lighting** des objets maillés est définie à {{Value|One side}}. La couleur de l\'arrière de leurs faces dépendra alors des paramètres de rétroéclairage : **Edition → Préférences... → Affichage → Vue 3D → Couleur du rétroéclairage - Intensité**. Voir : [Réglage des préférences](Preferences_Editor/fr#Vue_3D.md).





{{Mesh Tools navi

}}



---
![](images/Button_right.svg) [documentation index](../README.md) > [Mesh](Mesh_Workbench.md) > Mesh HarmonizeNormals/fr
