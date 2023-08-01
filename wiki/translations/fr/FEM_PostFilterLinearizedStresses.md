---
- GuiCommand:
   Name: FEM PostFilterLinearizedStresses
   Name/fr: FEM Graphique de linéarisation des contraintes
   MenuLocation: Résultats - Graphique de linéarisation des contraintes
   Workbenches: [FEM](FEM_Workbench/fr.md)
   SeeAlso: [FEM Pipeline de résultats](FEM_PostPipelineFromResult/fr.md), [FEM Filtre d'écrêtage selon une ligne](FEM_PostFilterDataAlongLine/fr.md),  [FEM Tutoriel](FEM_tutorial/fr.md)
---

# FEM PostFilterLinearizedStresses/fr

## Description

Crée un graphique de linéarisation des contraintes.

Pour en savoir plus sur les graphiques de linéarisation des contraintes, vous pouvez lire [cette description (en)](https://www.graspengineering.com/what-is-stress-linearization/).

<img alt="" src=images/FEM_Stress-Linearization-Plot-Example.png  style="width:500px;">

*Un graphique de linéarisation des contraintes.*

## Utilisation

1.  Sélectionnez un [filtre d\'écrêtage selon une ligne](FEM_PostFilterDataAlongLine/fr.md) déjà créé.
2.  Lancez la commande de l\'une des façons suivantes :
    -   en appuyant sur le bouton **<img src="images/FEM_PostFilterLinearizedStresses.svg" width=16px> '''Graphique de linéarisation des contraintes'''**.
    -   en sélectionnant le menu **Résultats → <img src="images/FEM_PostFilterLinearizedStresses.svg" width=16px> Graphique de linéarisation des contraintes**.
3.  Un tracé XY avec les valeurs de contraintes linéarisées (membrane, membrane+flexion et total) le long de la ligne sera créé dans une fenêtre séparée.





{{FEM Tools navi

}}



---
⏵ [documentation index](../README.md) > [FEM](Category_FEM.md) > FEM PostFilterLinearizedStresses/fr
