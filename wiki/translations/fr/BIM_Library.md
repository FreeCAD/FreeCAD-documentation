---
- GuiCommand:Addon/fr
   Name:BIM Library
   Name/fr:BIM Bibliothèque
   MenuLocation:3D Modeling → Library
   Workbenches:<img src="images/IFC.svg" width=16px> [BIM](BIM_Workbench/fr.md)
   Addon:BIM
   MenuLocation:3D Modeling → Library
   SeeAlso:[Arch Equipement](Arch_Equipment/fr.md)
---

## Description

L\'outil Bibliothèque BIM vous permet de placer dans le modèle en cours un objet de la [Bibliothèque de pièces](Parts_Library/fr.md). Il doit être installé via le [Addon Manager](Addon_Manager/fr.md) pour que cet outil soit disponible.

<img alt="" src=images/BIM_Library_screenshot.png  style="width:800px;"> 
*Above: Voir la boîte de dialogue '''Navigateur de bibliothèque''' dans le [Panneau des tâches](Task_panel/fr.md) à gauche*

## Utilisation

1.  Appuyez sur le bouton **<img src="images/BIM_Library.png" width=16px> '''BIM Library'''
**

    :   Résultat: Dans la [Vue combinée](Combo_view/fr.md) → [Panneau des tâches](Task_panel/fr.md) une boîte de dialogue intitulée {{MenuCommand|Library browser}} s\'affichera.
2.  Cliquez sur un fichier du Navigateur de la bibliothèque.
3.  Double-cliquez dessus ou appuyez sur le bouton **Insert**
4.  Cliquez sur un point dans la [vue 3D](3D_view/fr.md) ou entrez une coordonnée manuellement pour placer l\'objet.

## Options

-   Les fichiers [FCStd](FCStd/fr.md), [STEP](STEP/fr.md) et [BREP](BREP/fr.md) sont pris en charge. Seuls les fichiers STEP et BREP sont plaçables. Les fichiers FCStd ne vous permettront pas de choisir un emplacement, car ils pourraient être composés d\'une série complexe d\'objets avec des positions significatives. Lorsque vous choisissez un fichier FCStd, son contenu sera inséré à la position définie dans le fichier.
-   Les objets STEP et BREP sont insérés en tant que <img alt="Arch Equipment" src=images/Arch_Equipment.svg  style="width:24px;"> [Equipements](Arch_Equipment/fr.md) sans forme de base séparée. Ajouter ensuite une forme de base à ces objets détruira leur forme actuelle.
-   Lors du placement d\'un objet, vous pouvez choisir leur point d\'insertion entre l\'original (le point (`0,0,0`) défini dans le fichier), le haut, le milieu, le bas et la gauche, le centre et la droite.
-   La bibliothèque peut fonctionner hors ligne, auquel cas elle dépend du module complémentaire de bibliothèque de pièces à installer (et mettre à jour par l\'utilisateur) ou en ligne, auquel cas elle pointe directement à partir du [Parts Library Git repository](https://github.com/FreeCAD/FreeCAD-library) et permet de télécharger directement à partir de là.


 

[Category:BIM{{\#translation:}}](Category:BIM.md)
