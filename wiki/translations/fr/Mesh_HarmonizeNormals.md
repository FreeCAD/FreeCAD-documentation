---
- GuiCommand:/fr
   Name:Mesh HarmonizeNormals
   Name/fr:Mesh Harmoniser les normales‎
   MenuLocation:Maillages → Harmoniser les normales‎
   Workbenches:[Mesh](Mesh_Workbench/fr.md)
   SeeAlso:[Mesh Inverser les normales](Mesh_FlipNormals/fr.md)
---

## Description

La commande **Mesh Harmoniser les normales‎** harmonise les normales des objets maillés.

## Utilisation

1.  Sélectionnez un ou plusieurs objets maillés.
2.  Il existe plusieurs façons d\'appeler la commande:
    -   Appuyez sur le bouton **<img src="images/Mesh_HarmonizeNormals.svg" width=16px> [Harmonise les normales du maillage](Mesh_HarmonizeNormals/fr.md)
**
    -   Sélectionnez l\'option {{MenuCommand|Maillages → <img src="images/Mesh_HarmonizeNormals.svg" width=16px> Harmoniser les normales‎}} dans le menu.

## Remarques

-   Cette commande peut produire un maillage avec des normales inversées. La commande [Mesh Inverser les normales](Mesh_FlipNormals/fr.md) peut être utilisée pour corriger cela.
-   Pour une indication claire de l\'orientation des faces des objets maillés, assurez-vous que la propriété {{PropertyView/fr|Lighting}} des objets maillés est définie sur {{Value|One side}}. La couleur de l\'arrière de leurs faces dépendra alors des paramètres de rétroéclairage: {{MenuCommand|Edition → Préférences... → Affichage → Vue 3D → Couleur du rétroéclairage - Intensité}}. Voir: [Réglage des préférences](Preferences_Editor/fr#Vue_3D.md).





{{Mesh Tools navi

}}  
