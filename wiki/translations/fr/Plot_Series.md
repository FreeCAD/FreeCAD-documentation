---
- GuiCommand:/fr
   Name:Plot Series
   Name/fr:Plot Séries
   MenuLocation:Plot → Configurer les séries‏‎
   Workbenches:[Plot](Plot_Workbench/fr.md)
---

# Plot Series/fr

## Description

Le module plot standard fournit déjà un outil permettant de modifier le style des séries du graphique <img alt="" src=images/Matplotlib_edit_subplot.png  style="width:24px;">. Mais si vous installez l\'<img alt="" src=images/Workbench_Plot.svg  style="width:24px;"> [atelier Plot](Plot_Workbench/fr.md) en utilisant le [Gestionnaire d\'Addon](Std_AddonMgr.md), un outil plus complet et plus simple sera disponible.

<img alt="" src=images/Plot_MultiAxes_Example.png  style="width:600px;">

## Utilisation

Sélectionnez l\'onglet du graphique que vous voulez modifier et exécutez cet outil. Sélectionnez ensuite la série à éditer et procédez à la définition des nouvelles options. Vous pouvez même supprimer la série sélectionnée.

![Remove the selected series](images/Plot_Remove_Series.png ) 
*Bouton de suppression de la série sélectionnée*

## Options

-   **Label** : Vous pouvez définir l\'étiquette. Les formules mathématiques [LaTeX](https://www.latex-project.org/) sont acceptées.
-   **No label** : Si cette option est sélectionnée, la série n\'est pas affichée dans la légende du graphique. Sinon, la série sera affichée dans la légende avec l\'étiquette appropriée.
-   **Line Style** : Le style de ligne considéré. Utilisez \"\_draw\_nothing\" pour ne pas considérer les lignes pour cette série spécifique.
-   **Line Width** : La largeur de la ligne.
-   **Marker** : Le marqueur considéré. Utilisez \"\_draw\_nothing\" pour ne pas considérer les marqueurs pour cette série spécifique.
-   **Marker Size** : La taille du marqueur.
-   **Color** : La couleur de la série.





{{Plot_Tools_navi

}} 

_ _

---
[documentation index](../README.md) > [External_Workbenches](Category_External_Workbenches.md) > Plot Series/fr
