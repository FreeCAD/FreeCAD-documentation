---
 GuiCommand:
   Name: Sketcher RectangularArray
   Name/fr: Sketcher Répétition linéaire
   MenuLocation: Esquisse , Outils d'esquisse , Créer une répétition linéaire
   Workbenches: Sketcher_Workbench/fr
   Shortcut: **Z** **A**
   Version: 0.16
---

# Sketcher RectangularArray/fr

## Description

La commande <img alt="" src=images/Sketcher_RectangularArray.svg  style="width:16px;"> [Sketcher Répétition linéaire](Sketcher_RectangularArray/fr.md) crée un réseau d\'éléments sélectionnés d\'esquisses.



## Utilisation

1.  Sélectionnez les éléments de l\'esquisse dans le [panneau des tâches](Task_panel/fr.md) ou dans la [vue 3D](3D_view/fr.md).
2.  Il existe plusieurs façons de lancer la commande :
    -   Appuyez sur le bouton **[<img src=images/Sketcher_RectangularArray.svg style="width:16px"> [Créer une répétition linéaire](Sketcher_RectangularArray/fr.md)**.
    -   Sélectionnez l\'option **Esquisse → Outils d'esquisse → [<img src=images/Sketcher_RectangularArray.svg style="width:16px"> Créer une répétition linéaire** du menu.
3.  Spécifiez les options du réseau dans la fenêtre de dialogue qui s\'ouvre.
4.  Appuyez sur le bouton **OK**.
5.  Déplacez la souris dans la [vue 3D](3D_view/fr.md) vers le point de référence souhaité.En maintenant **Ctrl** enfoncée, l\'angle par rapport au point de référence peut être fixé par pas de 5°. {{Version/fr|0.20}}
6.  Cliquez avec le bouton gauche de la souris dans la vue 3D pour créer la répétition.
7.  Pour définir les distances entre les éléments de la répétition, modifiez les contraintes dimensionnelles de la répétition.

## Options

![](images/Sketcher_RectangularArray_Options.jpg )

La **Répétition linéaire** a les options suivantes :

-   **Colonnes** : nombre de colonnes du réseau.
-   **Rangées** : nombre de rangées du réseau.
-   **Espacement vertical/horizontal égal** : si la distance verticale entre les éléments de la répétition doit être la même que la distance horizontale.
-   **Contraindre la séparation entre éléments** : lorsque cette option est cochée, la distance entre les éléments de la répétition sera contrainte.Si vous savez par exemple seulement que vous avez besoin d\'une répétition de 23 x 15 mm, utilisez cette option pour pouvoir ensuite modifier ces contraintes aux dimensions dont vous avez besoin.
-   **Clone** : si cette option est sélectionnée, les contraintes dimensionnelles sont remplacées par des contraintes géométriques dans les copies, de sorte que toute modification de l\'élément original se reflète également dans les copies.





{{Sketcher_Tools_navi

}}



---
⏵ [documentation index](../README.md) > [Sketcher](Sketcher_Workbench.md) > Sketcher RectangularArray/fr
