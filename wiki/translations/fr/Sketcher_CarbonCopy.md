---
- GuiCommand   */fr
   Name   *Sketcher CarbonCopy
   Name/fr   *Sketcher Copie carbone
   MenuLocation   *Esquisse → Géométries d'esquisse → Copie carbone
   Workbenches   *[Sketcher](Sketcher_Workbench/fr.md)
   Shortcut   ***G** **W**
   Version   *0.17
---

# Sketcher CarbonCopy/fr

## Description

L\'outil **[<img src=images/Sketcher_CarbonCopy.svg style="width   *16px"> [Sketcher Copie carbone](Sketcher_CarbonCopy/fr.md)** copie toutes les géométries et contraintes d\'une autre esquisse dans l\'esquisse active.

Les contraintes dimensionnelles qui existaient avant la fonction de copie restent liées aux contraintes dimensionnelles de l\'esquisse d\'origine via les [expressions](expressions/fr.md).

## Utilisation

1.  Assurez-vous que vous êtes en mode édition d\'une **[<img src=images/Sketcher_NewSketch.svg style="width   *16px"> [Esquisse](Sketcher_NewSketch/fr.md)**. Cette esquisse est la cible de l\'opération.
2.  Appuyez sur le bouton **[<img src=images/Sketcher_CarbonCopy.svg style="width   *16px"> [Copie carbone](Sketcher_CarbonCopy/fr.md)**.
3.  Cliquez sur une arête d\'une autre esquisse. (Cette esquisse est la source de l\'opération.)
4.  Les éléments de géométrie ainsi que les contraintes sont copiés dans l\'esquisse active.
5.  Appuyez sur **Echap** ou sur le bouton droit de la souris pour terminer l\'opération.

## Remarques

-   Lorsque des esquisses sont utilisées dans l\'<img alt="" src=images/Workbench_PartDesign.svg  style="width   *24px;"> [atelier PartDesign](PartDesign_Workbench/fr.md), normalement l\'esquisse sur copie carbone doit être dans le même **[<img src=images/PartDesign_Body.svg style="width   *16px"> [PartDesign Corps](PartDesign_Body/fr.md)** que l\'esquisse active en cours. Si l\'esquisse à copier ne se trouve pas dans le [Corps](PartDesign_Body/fr.md) actif, le pointeur de la souris ne permet pas la sélection. Dans ce cas, maintenez **Ctrl** pour permettre la sélection d\'esquisses d\'autres corps.
-   Normalement, l\'esquisse à sélectionner doit être dans un plan parallèle à l\'esquisse active. Si l\'esquisse à copier n\'est pas parallèle à l\'esquisse active, maintenez **Ctrl** + **Alt** pour permettre la sélection d\'esquisses non parallèles. L\'objet sera alors ajusté au plan de l\'esquisse active. Remarqueː à ce jour, cela nécessite une sauvegarde et un rechargement du document pour le rendre visible. Cela fonctionne également pour les esquisses situées en dehors du [Corps](PartDesign_Body/fr.md) actif.
-   Comme les contraintes dimensionnelles copiées au carbone utilisent des expressions, elles sont rendues dans une couleur différente. La couleur peut être personnalisée avec les [Réglage des préférences](Preferences_Editor/fr.md) dans **Édition → Préférences → Sketcher → Couleurs → Couleur de contraintes dépendante de l'expression**.
-   Si le mode Sketcher a été changé en mode construction en utilisant **[<img src=images/Sketcher_ToggleConstruction.svg style="width   *24px"> [Basculer en géométrie de construction](Sketcher_ToggleConstruction/fr.md)**, toute la géométrie copiée sera créée en mode construction.

## Limitations

-   L\'esquisse complète est copiée, il n\'est pas possible de sélectionner uniquement une partie. Cependant, après la copie, vous pouvez supprimer les éléments indésirables de l\'esquisse copiée.





{{Sketcher_Tools_navi

}}



---
![](images/Right_arrow.png) [documentation index](../README.md) > [Sketcher](Sketcher_Workbench.md) > Sketcher CarbonCopy/fr
