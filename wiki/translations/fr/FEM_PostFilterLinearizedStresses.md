---
 GuiCommand:
   Name: FEM PostFilterLinearizedStresses
   Name/fr: FEM Graphique de linéarisation des critères
   MenuLocation: Résultats , Graphique de linéarisation des critères
   Workbenches: FEM_Workbench/fr
   SeeAlso: FEM_PostPipelineFromResult/fr, FEM_PostFilterDataAlongLine/fr,  FEM_tutorial/fr
---

# FEM PostFilterLinearizedStresses/fr

## Description

Crée un graphique de linéarisation des critères.

Pour en savoir plus sur les graphiques de linéarisation des critères, vous pouvez lire [cette description (en)](https://www.graspengineering.com/what-is-stress-linearization/).

<img alt="" src=images/FEM_Stress-Linearization-Plot-Example.png  style="width:500px;">

*Un graphique de linéarisation des critères*



## Utilisation

1.  Sélectionner un [filtre d\'écrêtage selon une ligne](FEM_PostFilterDataAlongLine/fr.md) créé précédemment avec l\'un des critères tracés :
    -   von Mises,
    -   Tresca,
    -   Principal majeur,
    -   Principal intermédiaire,
    -   Principal mineur,
    -   Composante XX du critère, {{Version/fr|0.22}}
    -   Composante XY du critère, {{Version/fr|0.22}}
    -   Composante XZ du critère, {{Version/fr|0.22}}
    -   Composante YY du critère, {{Version/fr|0.22}}
    -   Composante YZ du critère, {{Version/fr|0.22}}
    -   Composante ZZ du critère, {{Version/fr|0.22}}
2.  Lancer la commande soit :
    -   En appuyant sur le bouton **<img src="images/FEM_PostFilterLinearizedStresses.svg" width=16px> '''Graphique de linéarisation des critères'''**.
    -   En utilisant le menu **Résultats → <img src="images/FEM_PostFilterLinearizedStresses.svg" width=16px> Graphique de linéarisation des critères**.
3.  Un tracé XY avec les valeurs de critères linéarisés (membrane, membrane+flexion et total) le long de la ligne sera créé dans une fenêtre séparée. La quantité de critères tracée dans le filtre d\'écrêtage sera utilisée pour le calcul des critères linéarisés.





{{FEM Tools navi

}}



---
⏵ [documentation index](../README.md) > [FEM](Category_FEM.md) > FEM PostFilterLinearizedStresses/fr
